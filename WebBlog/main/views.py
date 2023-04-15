from django.shortcuts import HttpResponse,render
from WebBlog.connectToDB import *


def authorization(request):
    return render(request, "authorization.html")
 
def main(request):
    name = request.GET.get("name")
    password = request.GET.get("password")
    context = {'isAdmin': checkAdmin(name,password),'posts': takeAllPost()}
    return render(request, "main.html",context=context)

def post(request):
    name = request.GET.get("post")
    context = {'post': "firstNotes",'text':takeTextOfPost('firstNotes')}
    return render(request, "post.html",context=context)

def AdminPost(request):
    name = request.GET.get("post")
    context = {'post': "firstNotes",'text':takeTextOfPost('firstNotes')}
    return render(request, "AdminPost.html",context=context)
 
 


