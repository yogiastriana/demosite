from django.urls import path

from .views import input_form_view, output_view, run_mvoh_model_view, current_mvoh_result_view, fetch_mvoh_error_view, fetch_mvoh_ticker_view

urlpatterns = [
    path('input/', input_form_view, name="mvoh-input"),
    path('mvoh-result/', output_view, name="mvoh-result"),
    path('run-mvoh-model/', run_mvoh_model_view, name="run-mvoh-model"),
    path('current-mvoh-result/', current_mvoh_result_view, name="current-mvoh-result"),
    path('fetch-mvoh-error/', fetch_mvoh_error_view, name='fetch-mvoh-error'),
    path('fetch-ticker-data/', fetch_mvoh_ticker_view, name='fetch-mvoh-tciker'),
]