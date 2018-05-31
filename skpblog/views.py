from django.shortcuts import render
# Create your views here.
def index(req):
    return render(req,'index.html')


def writeblog(req):
    return render(req,'writeblog.html')

def login(req):
    return render(req,'login.html')