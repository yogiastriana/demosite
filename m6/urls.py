from django.urls import path

from .views import input_form_view, output_view, fetch_m6_error_view, current_m6_result_view, run_m6_model_view

urlpatterns = [
    path('m6-input/', input_form_view, name="m6-input"),
    path('m6-result/', output_view, name="m6-result"),
    path('run-m6-model/', run_m6_model_view, name="run-m6-model"),
    path('current-m6-result/', current_m6_result_view, name="current-m6-result"),
    path('fetch-m6-error/', fetch_m6_error_view, name='fetch-m6-error'),
]