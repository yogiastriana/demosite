from django.urls import path

from .views import runs_view, m2_runs_view, save_run_view, delete_run, session_mvoh_run, session_m2_run, session_m3_run, session_m4_run, save_session_run_view, save_session_m2_run_view, save_session_m3_run_view,  run_output_view, get_single_saved_run, get_single_saved_run_m2, get_single_saved_run_m3, get_single_saved_run_m4, save_session_m4_run_view, calculate_ticker_correlation_view, calculate_m4_ticker_correlation_view, run_detail_view, m4_run_detail_view, session_f1_run, f1_runs_view, f1_run_detail_view, delete_f1_run, save_session_f1_run_view

urlpatterns = [
    path('', runs_view, name="runs_mvoh"),
    path('m2/', m2_runs_view, name="runs_m2"),
    path('save-run/', save_run_view, name="save-run"),
    path('delete-run/', delete_run, name='delete-run'),
    path('get-run-data/', get_single_saved_run, name="get-run-data"),
    path('get-run-data-m2/', get_single_saved_run_m2, name="get-run-data-m2"),
    path('get-run-data-m3/', get_single_saved_run_m3, name="get-run-data-m3"),
    path('get-run-data-m4/', get_single_saved_run_m4, name="get-run-data-m4"),
    path('run-detail/<int:run_id>/', run_detail_view, name="run-detail"),
    path('m4-run-detail/<int:run_id>/', m4_run_detail_view, name="m4-run-detail"),
    path('session-mvoh-run/<int:id>/', session_mvoh_run, name='session-mvoh-run'),
    path('session-m2-run/<int:id>/', session_m2_run, name='session-m2-run'),
    path('session-m3-run/<int:id>/', session_m3_run, name='session-m3-run'),
    path('session-m4-run/<int:id>/', session_m4_run, name='session-m4-run'),
    path('save-session-mvoh-run/', save_session_run_view, name='save-session-mvoh-run'),
    path('save-session-m2-run/', save_session_m2_run_view, name='save-session-m2-run'),
    path('save-session-m3-run/', save_session_m3_run_view, name='save-session-m3-run'),
    path('save-session-m4-run/', save_session_m4_run_view, name='save-session-m4-run'),
    path('mvoh-run-output/<int:id>/', run_output_view, name='mvoh-run-output'),
    path('calculate-ticker-correlation/', calculate_ticker_correlation_view, name='calculate-ticker-correlation'),
    path('calculate-m4-ticker-correlation/', calculate_m4_ticker_correlation_view, name='calculate-m4-ticker-correlation'),
    # Rebalancing
    path('rebalancing/f1/', f1_runs_view, name="runs_f1"),
    path('rebalancing/f1-run-detail/<int:run_id>/', f1_run_detail_view, name="f1-run-detail"),
    path('rebalancing/delete-run/', delete_f1_run, name='delete-f1-run'),
    path('rebalancing/session-f1-run/<int:id>/', session_f1_run, name='session-f1-run'),
    path('save-session-f1-run/', save_session_f1_run_view, name='save-session-f1-run'),
]

