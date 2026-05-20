from django.shortcuts import render
from .models import Login ,  Expense , Income
from django.http import HttpResponse

# Create your views here.

def login_page(request):
    
    if request.method == "POST":
        user_email = request.POST.get("user_email"),
        
        #if Login.objects.filter(user_email = user_email).exists():
        
        Login.objects.create(
            user_email = user_email,
            passworde = request.POST.get("passworde")
        )
        
    return render(request, 'login.html')
