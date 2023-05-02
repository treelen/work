from django.shortcuts import render
from .models import Contact
from django.views.generic.base import View
# Create your views here.

class Contacts(View):
    def get(self,request):
        contacts = Contact.objects.all()
        context={
            'contacts':contacts
        }
        return render(request,'contacts/contact.html',context)
    
    
