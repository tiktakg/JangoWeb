from django.shortcuts import HttpResponse,render



def authorization(request):
    return render(request, "authorization.html")
 
def main(request):
    return render(request, "main.html")
 
