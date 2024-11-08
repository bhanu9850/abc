from django.urls import path
from demo.views import *

urlpatterns = [
    path("",BooksList.as_view(), name='books-list'),
    path("create-book/",BookCreate.as_view(), name='create-book'),
    path("delete-book/<str:id>",DeleteBook.as_view(), name='delete-book'),
    path("update-book/<str:id>",BookUpdate.as_view(), name='update-book'),

]
