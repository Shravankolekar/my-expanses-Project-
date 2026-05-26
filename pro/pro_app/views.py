from django.shortcuts import render
from .models import user_login , expancess

# Create your views here.
def singup_page(request):
    error = ""
    if request.method == "POST":
        
        if user_login.objects.filter(email = request.POST.get("email")).exists():
            error = "Email already exists"
        else:
            user_login.objects.create(
                email = request.POST.get("email"),
                password  = request.POST.get("password")
            )
            error = "login"

    return render(request , "singup.html" , {"error": error})


