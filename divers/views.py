from django.shortcuts import render

def home_page(request):
    title = "Crypto Live"
    toto = {"titlekey" : title}
    return render(request, 'divers/home_page.html', context=toto)

def contact_page(request):
    return render(request, 'divers/contact_page.html')

def about_page(request):
    return render(request, 'divers/about_page.html')

