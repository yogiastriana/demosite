from django.urls import path

from .views import tickers_view, delete_ticker_view, save_ticker_view

urlpatterns = [
    path('', tickers_view, name="tickers"),
    path('delete-ticker/', delete_ticker_view, name="delete-ticker"),
    path('save-ticker/', save_ticker_view, name="save-ticker"),
]