from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('item/', views.item, name = 'item'),
    path('info/', views.info, name = "info"),
    path('<int:item_id>/', views.detail, name = "detail" ),
    #add form
    path('add', views.create_item, name = "create"),
    #edit item
    path('update/<int:id>/', views.update_item, name = 'update_item'),
    #delete item
    path(r'^delete/<int:id>/', views.delete_item, name = 'delete_item')
]