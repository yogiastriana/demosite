from django.urls import path

from .views import rebalancing_dashboard, input_form_view, output_view, run_rebalancing_f1_view, current_f1_result_view, fetch_f1_ticker_view, fetch_f1_error_view, fetch_f1_quarterly_data_view, saved_f1_run_output_view, fetch_saved_f1_quarterly_data_view

urlpatterns = [
    path('', rebalancing_dashboard, name="rebalancing"),
    path('input/', input_form_view, name="f1-input"),
    path('f1-result/', output_view, name="f1-result"),
    # path('run-m4-model/', run_m4_model_view, name="run-m4-model"),
    path('current-f1-result/', current_f1_result_view, name="current-f1-result"),
    path('fetch-f1-error/', fetch_f1_error_view, name='fetch-f1-error'),
    path('run-rebalancing-f1/', run_rebalancing_f1_view, name='run-rebalancing-f1'),
    path('fetch-ticker-data/', fetch_f1_ticker_view, name='fetch-f1-ticker'),
    path('fetch-quarterly-data/', fetch_f1_quarterly_data_view),
    path('fetch-saved-quarterly-data/', fetch_saved_f1_quarterly_data_view),
    path('saved-f1-run-output/<int:id>/', saved_f1_run_output_view, name='saved-f1-run-output'),
]