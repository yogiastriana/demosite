from django.urls import path

from .views import input_form_view, output_view, fetch_m2_error_view, run_m2_model_view, current_m2_result_view

urlpatterns = [
    path('m2-input/', input_form_view, name="m2-input"),
    path('m2-result/', output_view, name="m2-result"),
    path('run-m2-model/', run_m2_model_view, name="run-m2-model"),
    path('current-m2-result/', current_m2_result_view, name="current-m2-result"),
    path('fetch-m2-error/', fetch_m2_error_view, name='fetch-m2-error'),
]