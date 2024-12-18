from django.urls import path

from .views import input_form_view, output_view, fetch_m5_error_view, current_m5_result_view, run_m5_model_view

urlpatterns = [
    path('m5-input/', input_form_view, name="m5-input"),
    path('m5-result/', output_view, name="m5-result"),
    path('run-m5-model/', run_m5_model_view, name="run-m5-model"),
    path('current-m5-result/', current_m5_result_view, name="current-m5-result"),
    path('fetch-m5-error/', fetch_m5_error_view, name='fetch-m5-error'),
]