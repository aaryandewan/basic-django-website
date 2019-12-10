from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('item/', views.item, name = 'item'),
    path('info/', views.info, name = "info"),
    path('<int:item_id>/', views.detail, name = "detail" ),
    #add form
    path('add', views.create_item, name = "create"),
]