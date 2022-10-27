from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def home_page(request):
    title = "Crypto Live"
    toto = {"titlekey" : title}
    return render(request, 'divers/home_page.html', context=toto)

def contact_page(request):
    return render(request, 'divers/contact_page.html')

def about_page(request):
    return render(request, 'divers/about_page.html')

@login_required
def special_view(request):
    return render(request, 'divers/special_view_page.html')

class SignupPage(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'