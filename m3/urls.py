from django.urls import path

from .views import input_form_view, output_view, fetch_m3_error_view, current_m3_result_view, run_m3_model_view

urlpatterns = [
    path('m3-input/', input_form_view, name="m3-input"),
    path('m3-result/', output_view, name="m3-result"),
    path('run-m3-model/', run_m3_model_view, name="run-m3-model"),
    path('current-m3-result/', current_m3_result_view, name="current-m3-result"),
    path('fetch-m3-error/', fetch_m3_error_view, name='fetch-m3-error'),
]