from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'hotspot'
urlpatterns = [
    #ex: /hotspot/
    path('', views.index, name='index'),
    #ex: /hotspot/8/
    path('<int:layout_id>/', views.layout_detail, name='layout detail'),
    #ex: /hotspot/8/edit
    path('<int:layout_id>/edit', views.layout_edit, name='edit layout'),
    #ex: /hotspot/add
    path('add/', views.layout_add, name='add layout'),

    path('view/', views.layout_view, name='view layouts'),
]
