from django.urls import path

from books.views import Borrowed

urlpatterns=[

    path('borrow/<int:user_id>',Borrowed),
]