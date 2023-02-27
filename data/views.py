from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from .predictor import *

    
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        answers = []
        for q in questions:
            print(request.POST.get(q.question))
              
            v =  request.POST.get(q.question)
            answers.append(v)
            print(answers)
        predictions = make_prediction("dataproject/static/data.csv", answers)
        if predictions == "Yes":
            result = "you should contact your child's healthcare provider for further evaluation. Some of the behaviors you reported may be indicative of ASD."
            context = {
                'result': result
            }
        else:
            result = "your child does not show significant signs of ASD. If you continue to have concerns about your child's behavior, however, you should discuss them with your child's physician."
            context = {
                'result': result
            }
        return render(request, 'data/result.html', context)  
    questions=QuesModel.objects.all()
    context = {
        'questions': questions
            }
    return render(request, "data/home.html",context)

def addQuestion(request):    
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'data/addQuestion.html',context)
     
 
def register(request):
    if request.user.is_authenticated:
        return redirect('data/home.html') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('data/loginForm.html')
        context={
            'form':form,
        }
        return render(request,'data/register.html',context)
 
def loginForm(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'data/loginForm.html',context)
def graphs(request):
    context={}
    return render(request,'data/graphs.html',context)
 
def logoutForm(request):
    logout(request)
    return redirect('/')