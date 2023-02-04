from django.urls import path
from backend import views
from backend.views import index

urlpatterns = [
    path('', index, name="index"),
    path('author_list/', views.AuthorList.as_view(), name='author'),
]