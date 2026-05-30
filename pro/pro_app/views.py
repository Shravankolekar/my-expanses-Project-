from django.shortcuts import render , redirect
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

    return render(request , "singup.html" , {"error": error} )

def login_page(request):
    
    error = ""
    
    if request.method == "POST" :
        
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        
        login_user = user_login.objects.filter(email = email , password = password).first()
        if login_user:
            return redirect("addexpancess")
        else:
            error = "Enter a Currect Username and Password"  
    
    return render(request , "login.html" , {"error" : error} )


def addexpancess(request):
    
    error = ""
    
    if request.method == "POST":
        
        try:
            expancess.objects.create(
                category = request.POST.get("category"),
                amount = request.POST.get("amount"),
                note = request.POST.get("note"),
                payment_method = request.POST.get("payment_method")
            )
            error = "done"
        except :
            error = "Enter a Currect Information"
    
    return render(request , "addexpances.html" , {"error" : error} )
