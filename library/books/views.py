from django.shortcuts import render
from django.http import HttpResponse
from books.models import Books,Patron,Borrow
# Create your views here.

def Borrowed(request,user_id):
    user=Borrow.objects.get(id=user_id)
    borrow_list=[]
    for b in user:
        borrow_list.append({'Membership_id':b.membership_id,'Borrow_date':b.Borrow_date})
    context={'list':borrow_list
             }
    return render(request,"l_temp/borrowing.html",context)
