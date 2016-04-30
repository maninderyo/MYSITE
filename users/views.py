from django.shortcuts import render,redirect

# Create your views here.
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings

def controller(request):
    if request.user.is_authenticated():
        return redirect('posts:list')
    else:
        return HttpResponseRedirect('register')

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    variables ={
    'form': form
    }
 
    return render(request,'registration/register.html',variables,)
 
def register_success(request):
    return render(request,'registration/success.html',{})
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return redirect('posts:list')

def contact(request):
    form=ContactForm(request.POST or None)
    title="Contact Us..."
    if form.is_valid():
        send_mail(form.cleaned_data.get('subject'), 
            form.cleaned_data.get('content'), 
            settings.EMAIL_HOST_USER,
            [form.cleaned_data.get('reciever')], 
            fail_silently=False)
        title="successfully sent"
        form=ContactForm()
    context={
        "form":form,
        "title":title,
    }
    return render(request,"forms.html",context)