from django.shortcuts import HttpResponse,render
from WebBlog.connectToDB import *


def authorization(request):
    return render(request, "authorization.html")
 
def main(request):
    
    name = request.GET.get("name")
    tag = request.GET.get("tag")
    password = request.GET.get("password")
    context = {'isAdmin': checkAdmin(name,password),'posts': takeAllPost(),'tag':tag}
    return render(request, "main.html",context=context)

def post(request):
    name = request.GET.get("post")
    context = {'post': "firstNotes",'text':takeTextOfPost('firstNotes'),'tegs':takeTegOfPost('firstNotes')}
    return render(request, "post.html",context=context)

def AdminPost(request):
    name = request.GET.get("post")
    check = request.GET.get("delete")
    if(check == "true"):
        deltePost(name)
        
    context = {'post': "firstNotes",'text':takeTextOfPost('firstNotes'),'tegs':takeTegOfPost('firstNotes')}
    return render(request, "AdminPost.html",context=context)
 
def makePost(request):
    context = {'post': "firstNotes",'text':takeTextOfPost('firstNotes'),'tegs':takeTegOfPost('firstNotes')}
    return render(request, "makePost.html",context=context)
 


