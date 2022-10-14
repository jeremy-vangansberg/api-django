from django.shortcuts import render
from . import forms
from requests import Session
import json


def api(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '9161a226-c054-438a-8edb-f7fe66853898'
    }
    session = Session()
    session.headers.update(headers)


    if request.method =="POST" :
        form = forms.ApiForm(request.POST)
        if form.is_valid() :
            response = session.get(url, params=form.cleaned_data)
            print(form.cleaned_data)
            form.save()
            info = json.loads(response.text)
            return render(request, 'api_app/reponse_formulaire.html', context = {'form' : form, 'info' :info})
    else :
        form = forms.ApiForm()
    return render(request, 'api_app/formulaire.html', context = {'form' : form})
