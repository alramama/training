from django.urls import path
from . import views

app_name = 'bids'

urlpatterns = [
    path('', views.BIDListView.as_view(), name='all'),
    #path('open', views.openpage, name='openpage'),
    path('bids/<int:pk>/detail', views.BIDDetailView.as_view(), name='bid_detail'),
    path('bids/create/', views.BIDCreateView.as_view(), name='bid_create'),
    path('bids/<int:pk>/update/', views.BIDUpdateView.as_view(), name='bid_update'),
    path('bids/<int:pk>/delete/', views.BIDDeleteView.as_view(), name='bid_delete'),
    path('bids/<int:pk>/delete/', views.BIDDeleteView.as_view(), name='bid_delete'),
    path("index1", views.index1, name="index1")

]
