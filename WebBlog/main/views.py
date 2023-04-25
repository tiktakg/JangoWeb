from django.shortcuts import HttpResponse,render
from WebBlog.connectToDB import *
from django.core.files.base import ContentFile

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

    
    from PIL import Image
    from io import BytesIO
    import os

    buffer = BytesIO()
    if 'img' in request.FILES and request.FILES['img']:
        file = request.FILES['img']
        print(file)
       
        

       


    if(idFromMake != "" and titleFromMake != "" and textFromMake != ""):
        updatePost(titleFromMake,textFromMake,tagFromMake,buffer,idFromMake)
    elif(titleFromMake != "" and textFromMake != ""):
        addPost(titleFromMake,textFromMake,tagFromMake,buffer)
   
    
   
    
    allpost ={}
    if(tag == ""):
        allpost =  takeAllPost()
    else:
        allpost = takeTegOfPosts(tag)
    
  
   
    
    context = {'isAdmin': 0,'posts':  allpost,'primaryKey':takeIdOfPost(),'img':takeAllImg()}
    return render(request, "main.html",context=context)



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
