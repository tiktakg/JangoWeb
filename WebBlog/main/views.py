from django.shortcuts import HttpResponse,render
from WebBlog.connectToDB import *
from PIL import Image

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
    imgFromMake = request.POST.get("img",'')

    
    
    if(checkData(titleFromMake,textFromMake,tagFromMake)):
        context = {'post': titleFromMake,'text':textFromMake,'tegs':tagFromMake,'id':id,}
        return render(request, "makePost.html",context)

    if(idFromMake != "" and titleFromMake != "" and textFromMake != ""):
        updatePost(titleFromMake,textFromMake,clearTegs(tagFromMake),imgFromMake,idFromMake)
    elif(titleFromMake != "" and textFromMake != ""):
        addPost(titleFromMake,textFromMake,clearTegs(tagFromMake),imgFromMake)
   
    
   
    print(tag)
    allpost ={}
    if(tag == ""):
        allpost =  takeAllPost()
    else:
        allpost = takeTegOfPosts(tag)
    
  
   
    
    context = {'isAdmin': checkAdmin(name,password),'posts':  allpost,'primaryKey':takeIdOfPost(),'img':takeAllImg()}
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
