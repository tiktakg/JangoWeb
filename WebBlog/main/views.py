from django.shortcuts import HttpResponse,render
from WebBlog.connectToDB import *

import requests

def authorization(request):
    return render(request, "authorization.html")
 
def main(request):
    
    name = request.GET.get("name")
    tag = request.GET.get("tag")
    password = request.GET.get("password")

    titleFromMake =  request.POST.get("title",'')
    textFromMake = request.POST.get("text",'')
    tagFromMake = request.POST.get("tag",'')
    imgFromMake = request.POST.get("img",'')
    idFromMake = request.POST.get("iddd",'')

    
    if(titleFromMake != "" and textFromMake != ""):
        addPost(titleFromMake,textFromMake,tagFromMake,imgFromMake)
    # else:
    #     print("eror")
    #     return render(request, "eror.html")
    
    allpost ={}
    if(tag == ""):
        print("Tag empty")
        allpost =  takeAllPost()
    else:
        allpost = takeTegOfPosts(tag)
    
   
    
    context = {'isAdmin': checkAdmin(name,password),'posts':  allpost,'primaryKey':takeIdOfPost(),'img':takeImg("firstNote")}
    return render(request, "main.html",context=context)



def AdminPost(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    if(id != ""):
        deltePost(id)


    context = {'post': name,'text':takeTextOfPost(name),'tegs':takeTegToPost(name)}
    return render(request, "AdminPost.html",context=context)
 
def makePost(request):
    name = request.GET.get("name")
    if(name!=""):
        context = {'post': name,'text':takeTextOfPost(name),'tegs':takeTegToPost(name)}
    else:
         context = {'post': "",'text': "",'tegs': ""}
   


    return render(request, "makePost.html",context=context)
 

def post(request):
    name = request.GET.get("name")
    context = {'post': name,'text':takeTextOfPost(name),'tegs':takeTegToPost(name)}
    return render(request, "post.html",context=context)
