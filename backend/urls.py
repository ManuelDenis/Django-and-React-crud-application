from django.urls import path
from backend import views

urlpatterns = [
    path('author_list/', views.AuthorList.as_view(), name='author'),
]