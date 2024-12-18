from django.urls import path

from .views import users_view, single_user_view, update_user_status_role_view, user_setting_view, password_reset_request_view, password_reset_confirm_view, delete_user_view

urlpatterns = [
    path('', users_view, name="users"),
    path('user-detail/<int:id>/', single_user_view, name="user-detail"),
    path("user/<int:user_id>/update-status-role/", update_user_status_role_view, name="update-user-status-role"),
    path("setting/", user_setting_view, name="user-setting"),
    path('password-reset/', password_reset_request_view, name='password-reset-request'),
    path('reset-password/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
    path('delete-user/', delete_user_view, name="delete-user")
]