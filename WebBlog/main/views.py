from django.shortcuts import HttpResponse,render,redirect
from WebBlog.connectToDB import *
import requests
from django.conf import settings

def authorization(request):
    return render(request, "authorization.html")
 
def main(request):
    
    
    
    name = request.GET.get("name",'')
    tag = request.GET.get("tag",'')
    password = request.GET.get("password")
    idFromMake = request.GET.get("id",'')

    titleFromMake =  request.POST.get("title",'')
    textFromMake = request.POST.get("text",'')
    tagFromMake = request.POST.get("tag",'')

   
   
  
    

    if "nameAdmin" in request.COOKIES:
        adminName = request.COOKIES.get("nameAdmin")


    if(checkData(titleFromMake,textFromMake,tagFromMake)):
        context = {'post': titleFromMake,'text':textFromMake,'tegs':tagFromMake,'id':id,}
        return render(request, "makePost.html",context)
    
    if 'img' in request.FILES:
         imgFromMake = request.FILES['img']  
         if(idFromMake != "" and titleFromMake != "" and textFromMake != "" ):
            updatePost(titleFromMake,textFromMake,clearTegs(tagFromMake),imgFromMake,idFromMake,adminName)
         elif(titleFromMake != "" and textFromMake != ""):
            addPost(titleFromMake,textFromMake,clearTegs(tagFromMake),imgFromMake,adminName)
   
  
    
    
   
    
    
   
    allpost ={}
    if(tag == ""):
        allpost =  takeAllPost()
    else:
        allpost = takeTegOfPosts(tag)
    
  
   
    
    context = {'isAdmin': checkAdmin(name,password)[0],'posts':  allpost,'primaryKey':takeIdOfPost(),'img':takeAllImg()}
    response = render(request, "main.html",context=context)

       
    if "nameAdmin" in request.COOKIES:
        adminName = request.COOKIES.get("nameAdmin")
        print(adminName)
    else:
        response.set_cookie("nameAdmin",checkAdmin(name,password)[1] )

    return response



def AdminPost(request):
    name = request.GET.get("name")
    id = request.GET.get("id")

    if(id != ""):
        deltePost(id)


    
    
    context = {'post': name,'text':takeTextOfPost(name),'tegs':takeTegToPost(name),'img':takeImg(name)}
    return render(request, "AdminPost.html",context=context)
 
def makePost(request):
    name = request.GET.get("name")
    id = request.GET.get("id")

    
    
  
    if(name!=""):
        context = {'post': name,'text':takeTextOfPost(name),'tegs':takeTegToPost(name),'id':id,}
    else:
         context = {'post': "",'text': "",'tegs': ""}
   


    return render(request, "makePost.html",context=context)
 

def post(request):
    name = request.GET.get("name")
    context = {'post': name,'text':takeTextOfPost(name),'tegs':takeTegToPost(name),'img':takeImg(name)}
    return render(request, "post.html",context=context)
