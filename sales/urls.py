from django.urls import path
from .views import (
    SaleDetailView,
    home_view,
    SaleListView,

)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='list'),
    path('sales/<pk>/', SaleDetailView.as_view(), name= 'detail'),

]
