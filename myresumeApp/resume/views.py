from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile,Experience,Educations,Certification,Projects
# Create your views here.
def home(request):

    bio ={
    'profile':Profile.objects.all(),
        'exp':Experience.objects.all(),
       'edu':Educations.objects.all(),
        'cert':Certification.objects.all(),
        'pro':Projects.objects.all(),

        }

    return render(request,'index.html',bio)