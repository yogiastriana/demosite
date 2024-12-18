from django.urls import path

from .views import input_form_view, output_view, fetch_m8_error_view, current_m8_result_view, run_m8_model_view

urlpatterns = [
    path('m8-input/', input_form_view, name="m8-input"),
    path('m8-result/', output_view, name="m8-result"),
    path('run-m8-model/', run_m8_model_view, name="run-m8-model"),
    path('current-m8-result/', current_m8_result_view, name="current-m8-result"),
    path('fetch-m8-error/', fetch_m8_error_view, name='fetch-m8-error'),
]