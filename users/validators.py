from django.core.exceptions import ValidationError

# Define a list of public domains to exclude
PUBLIC_DOMAINS = [
    "gmail.com", "yahoo.com", "hotmail.com", "outlook.com"
]

def corporate_or_educational_email_validator(email):
    domain = email.split('@')[-1]
    if domain in PUBLIC_DOMAINS:
        raise ValidationError("Please use a corporate or educational email address.")