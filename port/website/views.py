from django.shortcuts import render

# Create your views here.



def home(request):
    context = {
        'name': request.session.get('name', 'Guest'),
        'phone': request.session.get('phone', 'Not set'),
        'experience': request.session.get('experience', 'Beginner'),
        'address': request.session.get('address', 'Not set'),
        'role': 'Casual Web Developer · Aspiring Professional',
    }
    return render(request, 'pages/index.html', context)

from django.shortcuts import render, redirect
from .forms import CreateUserForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'pages/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import LoginForm

def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("")  # change to your homepage URL name
    else:
        form = LoginForm()

    return render(request, "pages/login.html", {"form": form})


from django.shortcuts import render, redirect

def edit_profile(request):
    if request.method == 'POST':
        request.session['name'] = request.POST.get('name')
        request.session['phone'] = request.POST.get('phone')
        request.session['experience'] = request.POST.get('experience')
        request.session['address'] = request.POST.get('address')

        return redirect('')

    return render(request, 'pages/edit_profile.html')


