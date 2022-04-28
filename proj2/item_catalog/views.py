from django.shortcuts import render


# Create your views here.
def home(req):
    data = {'page_title': "Docs App",
            'greet': "Welcome to Home Page"}
    return render(req, 'item_catalog/home.html', context=data)
