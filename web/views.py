from django.shortcuts import render
from .models import Award,Education,Experience,Work,Contact,Service,Counter

# Create your views here.

app_name="web"

def index (request):
    context={}
    return render (request,'web/index.html',context)

def Profile (request):
    context={
        'award':Award.objects.all(),
        'education':Education.objects.all(),
        'experience':Experience.objects.all(),
        'service' :Service.objects.all(),
        'counter' :Counter.objects.all()
    }
    print(Award.objects.all())
    return render (request,'web/profile.html',context)

def Gallery (request):
    context={
        'work':Work.objects.all()
    }
    return render (request,'web/gallery.html',context)

def Connect (request):
    context={}
    if request.method == 'POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(name=name,email=email,subject=subject,message=message)
        form.save()

  
    return render (request,'web/connect.html',context)

