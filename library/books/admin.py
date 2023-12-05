from django.contrib import admin
from books.models import Books,Patron,Borrow
# Register your models here.
admin.site.register(Books)
admin.site.register(Patron)
admin.site.register(Borrow)