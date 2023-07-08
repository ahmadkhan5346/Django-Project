from django.urls import path
from app.views import FileDataApiView, SearchDataApiView


urlpatterns = [
    path("file_data/", FileDataApiView.as_view(), name="insert_file_data"),
    path("search-data/<str:data>/", SearchDataApiView.as_view(), name="insert_file_data"),
]
