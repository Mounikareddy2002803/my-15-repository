from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'mouni','l':[11,12,13]}
    return render(request,'loop.html',d)