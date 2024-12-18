from django.urls import path

from .views import input_form_view, output_view, fetch_m7_error_view, current_m7_result_view, run_m7_model_view

urlpatterns = [
    path('m7-input/', input_form_view, name="m7-input"),
    path('m7-result/', output_view, name="m7-result"),
    path('run-m7-model/', run_m7_model_view, name="run-m7-model"),
    path('current-m7-result/', current_m7_result_view, name="current-m7-result"),
    path('fetch-m7-error/', fetch_m7_error_view, name='fetch-m7-error'),
]