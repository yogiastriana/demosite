from django.urls import path

from .views import input_form_view, output_view, fetch_m4_error_view, current_m4_result_view, run_m4_model_view

urlpatterns = [
    path('m4-input/', input_form_view, name="m4-input"),
    path('m4-result/', output_view, name="m4-result"),
    path('run-m4-model/', run_m4_model_view, name="run-m4-model"),
    path('current-m4-result/', current_m4_result_view, name="current-m4-result"),
    path('fetch-m4-error/', fetch_m4_error_view, name='fetch-m4-error'),
]