from multiprocessing import context
from users_app.models import User
from django.shortcuts import redirect, render

# Create your views here.


def add(request):
    # check for request
    if request.method == "POST":
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        email = request.POST["email"]
        age = request.POST["age"]

        # then create obj
        user= User.objects.create(first_name=fname, last_name=lname, email_address=email, age=age)
        # session
        request.session["message"] = "the user added successfuly"

        # redirect to no neding for resubmitt
        return redirect("/")
        # session

    context = {
        "message": request.session.pop("message","")
    }

    return render(request,"index.html", context)


def show(request):
    #get all users
    user=User.objects.all()
    context={
        "user":user
    }

    return render(request,"list.html",context)
