from django.urls import path

from . import views

app_name = 'items'

urlpatterns = [
    path('', views.items, name='items'),
    path('tech/', views.index, name='index'),
    path('new/', views.new, name = 'new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    # path('', views.techy, name='technician'),

]