from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .processing import *

def index(request):
    return render(request,'index.html')

def predict(request):
    if request.method == 'POST':
        myform = indexForm(request.POST)
        if myform.is_valid():
            article = (myform['article'].value())
            date = (myform['date'].value())
            symbol = myform['symbol'].value()
            features = get_all_features(article,date,symbol)
            print(features)
            output = get_prediction(features)[0]
            print(output)
            if output == 0:
                res = "The Stock is expected go DOWN for the day"
            else:
                res = "The Stock is expected go UP for the day"
        return render(request, 'index.html', {'article':article,'date':date,'output':res})
    elif request.method == 'GET':
        return redirect('index')