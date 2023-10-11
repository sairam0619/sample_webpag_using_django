from django.shortcuts import render,redirect
from projapp.models import contactm
from projapp.forms import contactmform


# Create your views here.
def home(request):
    return render (request,'tempapp/home.html')
def about(request):
    return render (request,'tempapp/about.html')
def services(request):
    return render (request,'tempapp/services.html')
def gallery(request):
    return render (request,'tempapp/gallery.html')

def register(request):
    contacts=contactm.objects.all()
    return render (request,'tempapp/register.html', {'emp':contacts})
def base(request):
    return render (request,'tempapp/base.html')

def contactv(request): 
    form = contactmform()
    if request.method=='post':
        form=contactmform(request.post)
        if form.is_valid():
            form.save()
  
            return redirect("/thankyou")
    return render (request,'tempapp/contact.html',{'form':form})

def thankyou_view(request):
    return render(request,'tempapp/thankyou.html')
