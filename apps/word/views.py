from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


count =0
# Create your views here.
def index(request):
    if request.method != "POST":
        request.session['random_word'] 
        return render(request, 'word/index.html', count)
    
      

def generator(request):
    print "inside generator"
    if 'count' in request.session:
        request.session['random_word'] = get_random_string(length=13)
        request.session['count'] += 1
        return redirect("/")
    else:
        request.session['random_word'] = get_random_string(length=13)
        request.session['count'] = 1
        return redirect("/")