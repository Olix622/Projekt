# from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

# def hello(request):
#     return HttpResponse('Hello, world!')

# class HelloView(TemplateView):
#     template_name = 'cwierkacz/hello.html'


def home(request):
    return render(request, 'cwierkacz/index.html')


def signup(request):

    if request.method == "POST":
        nazwa_uzytkownika = request.POST['nazwa_uzytkownika']
        email = request.POST['email']
        imie = request.POST['imie']
        nazwisko = request.POST['nazwisko']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(nazwa_uzytkownika, email, password1)
        myuser.imie = imie
        myuser.nazwisko = nazwisko

        myuser.save()

        messages.success(request, "Rejestracja zakończona sukcesem")

        return redirect("logowanie")

    return render(request, 'cwierkacz/signup.html')


def signin(request):
    if request.method == 'POST':
        nazwa_uzytkownika = request.POST['login']
        password1 = request.POST['password1']

        user = authenticate(login=nazwa_uzytkownika, password=password1)

        if user is not None:
            login(request, user)
            imie = user.imie
            return redirect(request, "cwierkacz/index.html", {'imie': imie})

        else:
            messages.error(request, "Nieprawidłowe dane")
            return redirect('home')
    return render(request, 'cwierkacz/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "Wylogowany")
    return redirect('home')
