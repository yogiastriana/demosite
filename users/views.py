from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, PasswordResetRequestForm, PasswordResetConfirmForm
from .tokens import email_verification_token 
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from .models import UserProfile
from runs.models import Run
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login/')
def users_view(request):

    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request, 'users/user-list.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Attempt to access or create the profile explicitly
            profile = UserProfile.objects.get(user=user)
            
            # Check if the user is active and the profile status is approved
            if user.is_active and profile.status == 'approved':
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.error(request, "Your account is not approved or inactive.")
                return render(request, 'login.html')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Check if a user with the same email (username) already exists
            email = form.cleaned_data['email']
            if User.objects.filter(username=email).exists():
                messages.error(request, "A user with that email already exists.")
            else:
                # Save user but keep it inactive
                user = form.save(commit=False)
                user.is_active = False 
                user.save()

                # Create UserProfile only if it doesn't exist
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                
                # Assign default values for status and role
                user_profile.phone_number=form.cleaned_data['phone_number']
                user_profile.status = 'unapproved'  
                user_profile.role = 'user' 
                user_profile.save()

                # Prepare email confirmation
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = email_verification_token.make_token(user)
                confirmation_url = f"{settings.FRONTEND_URL}/confirm-email/{uid}/{token}/"

                # Send email with confirmation link (use an HTML template here)
                send_mail(
                    subject="Email Confirmation",
                    message=f"Please confirm your email by clicking the following link: {confirmation_url}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False,
                )

                messages.success(request, "Registration successful! Please check your email to confirm your registration.")
                return redirect('login')  
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def confirm_email_view(request, uidb64, token):
    try:
        # Decode uid and get the user ID
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Verify the token and activate the user if valid
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True  # Activate the account
        user.save()

        messages.success(request, "Your email has been confirmed. You can now log in.")
        return redirect('login')  # Redirect to the login page
    else:
        # Invalid token or user
        messages.error(request, "The confirmation link is invalid or has expired.")
        return redirect('login')


@login_required(login_url='/login/')
def logout_view(request):
    request.session.flush()
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def single_user_view(request, id):
    
    user = User.objects.get(id=id)
    runs = Run.objects.filter(user_id=id)

    context = {
        'user': user,
        'runs': runs
    }

    return render(request, 'users/single-user.html', context)


def update_user_status_role_view(request, user_id):
    if request.method == 'POST':
        # Assuming you have code here to update the user
        user_profile = UserProfile.objects.get(user_id=user_id)
        user_profile.status = request.POST.get('status')
        user_profile.role = request.POST.get('role')
        user_profile.save()

        # Return the updated values as JSON
        return JsonResponse({'status': user_profile.status, 'role': user_profile.role})
    

@login_required(login_url='/login/')
def user_setting_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        
        # Update password if provided
        password = request.POST.get('password')
        if password:
            user.set_password(password)  # Hash the password if changing it

        user.save()  # Save the user data

        # Update user profile
        user_profile = get_object_or_404(UserProfile, user=user)
        user_profile.phone_number = request.POST.get('phone_number')
        user_profile.save()  # Save the user profile data

        # Return a success message as HTML
        return JsonResponse({"message": "User data updated successfully!"})
    else:
        user = get_object_or_404(User, id=request.user.id)

        context = {
            'user': user
        }

        return render(request, 'users/setting.html', context)


@login_required(login_url='/login/')
def delete_user_view(request):
    user_id = request.POST.get('user_id')
    user = User.objects.get(id=user_id)
    user.delete()
    
    users = User.objects.all()  
    
    return render(request, 'template-parts/user-list.html', {'users': users})  


def password_reset_request_view(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "auth/password-reset-email.html"  # HTML template path
                    c = {
                        "email": user.email,
                        'domain': get_current_site(request).domain,
                        "site_name": "Your Site Name",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                        "protocol": 'https' if request.is_secure() else 'http',
                    }
                    email_body = render_to_string(email_template_name, c)
                    email = EmailMessage(subject, email_body, to=[user.email])
                    email.content_subtype = "html"  # Ensure email content is treated as HTML
                    email.send()
                messages.success(request, "A password reset email has been sent.")
            else:
                messages.error(request, "No user is associated with this email.")
            return redirect("password-reset-request")
    else:
        form = PasswordResetRequestForm()

    return render(request, 'auth/password-reset-request.html', {'form': form})


def password_reset_confirm_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = PasswordResetConfirmForm(request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password1']
                user.set_password(new_password)
                user.save()
                messages.success(request, "Your password has been set. You can now log in.")
                return redirect('login')  
        else:
            form = PasswordResetConfirmForm()
    else:
        messages.error(request, "The password reset link is invalid.")
        return redirect('password-reset-request')

    return render(request, 'auth/password-reset-confirm.html', {'form': form})
