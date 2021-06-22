from django.urls import path
from . import views


urlpatterns = [
    path('my-collection', views.my_collection, name='my-collection'),
    path('add-paper-id=<int:paper_id>/return=<path:return_url>', views.add_collection, name='add-collection'),
    path('delete-paper-id=<int:paper_id>/return=<path:return_url>', views.delete_collection, name='delete_collection'),
]
