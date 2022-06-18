from typing import Text
from typing_extensions import SupportsIndex
from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home import  models
from django.db import transaction
from django.contrib.auth.models import User ,auth
import  time
def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        print (title , desc)
        task = models.Task(TaskTitle = title , TaskDesc = desc)
        task.save(transaction.commit)
        time.sleep(1)
        
        context = {'success': True}
        
    return render(request , 'First page.html',context)
    
def task(request):
    # cal = models.Patien.object.get(pk=id)
    allpat = models.Patien.objects.all()
    context = {'pat' : allpat,
   # 'cal' : cal}
    }
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        daten = request.POST.get('daten',False)
        print (nom , prenom , daten)
        add = models.Patien(PatNom = nom , PatPrenom = prenom , PatNais = daten)
        add.save(transaction.commit)
    return render(request, 'task.html',context)

def patient(request):
  # cal = models.Patien.object.get(pk=id)
    allpat = models.Cluster.objects.all()
    context = {'pat' : allpat,
    # 'cal' :1
    }
    
    if request.method == 'POST':
        nom = request.POST['Username']
        prenom = request.POST['Tweet']
        daten = request.POST['Retweet']
        print (nom , prenom , daten)
        add = models.Cluster(UserName = nom , Tweet = prenom , Retweet = daten)
        add.save(transaction.commit)
    
    print( allpat)
    return render(request,'Second Page 1.html',context)

def addpatien(request):
    allpat = models.Cluster.objects.all()
    context = {'pat' : allpat,
    'cal' : 0}
    
    if request.method == 'POST':
        nom = request.POST['Username']
        prenom = request.POST['Tweet']
        daten = request.POST['Retweet']
        print (nom , prenom , daten)
        add = models.Cluster(UserName = nom , Tweet = prenom , Retweet = daten)
        add.save(transaction.commit)
    
    print( allpat)
    return render(request,'Second Page 2.html',context)
def addpatien3(request):
    allpat = models.Cluster.objects.all()
    context = {'pat' : allpat,
    'cal' : 2}
    
    if request.method == 'POST':
        nom = request.POST['Username']
        prenom = request.POST['Tweet']
        daten = request.POST['Retweet']
        print (nom , prenom , daten)
        add = models.Cluster(UserName = nom , Tweet = prenom , Retweet = daten)
        add.save(transaction.commit)
    
    print( allpat)
    return render(request,'Second Page 3.html',context)
def addpatien4(request):
    allpat = models.Cluster.objects.all()
    context = {'pat' : allpat,
    'cal' : 3}
    
    if request.method == 'POST':
        nom = request.POST['Username']
        prenom = request.POST['Tweet']
        daten = request.POST['Retweet']
        print (nom , prenom , daten)
        add = models.Cluster(UserName = nom , Tweet = prenom , Retweet = daten)
        add.save(transaction.commit)
    
    print( allpat)
    return render(request,'Second Page 4.html',context)
def addpatien5(request):
    allpat = models.Cluster.objects.all()
    context = {'pat' : allpat,
    'cal' : 4}
    
    if request.method == 'POST':
        nom = request.POST['Username']
        prenom = request.POST['Tweet']
        daten = request.POST['Retweet']
        print (nom , prenom , daten)
        add = models.Cluster(UserName = nom , Tweet = prenom , Retweet = daten)
        add.save(transaction.commit)
    
    print( allpat)
    return render(request,'Second Page 5.html',context)
def addpatien6(request):
    allpat = models.Cluster.objects.all()
    context = {'pat' : allpat,
    'cal' : 5}
    
    if request.method == 'POST':
        nom = request.POST['Username']
        prenom = request.POST['Tweet']
        daten = request.POST['Retweet']
        print (nom , prenom , daten)
        add = models.Cluster(UserName = nom , Tweet = prenom , Retweet = daten)
        add.save(transaction.commit)
    
    print( allpat)
    return render(request,'Second Page 6.html',context)
def addpatien7(request):
    allpat = models.Cluster.objects.all()
    context = {'pat' : allpat,
    'cal' : 6}
    
    if request.method == 'POST':
        nom = request.POST['Username']
        prenom = request.POST['Tweet']
        daten = request.POST['Retweet']
        print (nom , prenom , daten)
        add = models.Cluster(UserName = nom , Tweet = prenom , Retweet = daten)
        add.save(transaction.commit)
    
    print( allpat)
    return render(request,'Second Page 6.html',context)
def addpatien8(request):
    allpat = models.Cluster.objects.all()
    context = {'pat' : allpat,
    'cal' : 1}
    
    if request.method == 'POST':
        nom = request.POST['Username']
        prenom = request.POST['Tweet']
        daten = request.POST['Retweet']
        print (nom , prenom , daten)
        add = models.Cluster(UserName = nom , Tweet = prenom , Retweet = daten)
        add.save(transaction.commit)
    
    print( allpat)
    return render(request,'Second Page 7.html',context)
# Create your views here.



def delpatien(request,id):
    try:
        supp = models.Patien.objects.get(PatId = id)
        supp.delete()
    except Exception:
        print(" aled")
    return redirect ('task')
def edit(request,id):
    allpat = models.Patien.objects.get(pk=id)
    print(allpat.PatNais)
    context = {'pat' : allpat}
    if request.method == 'POST':
             nom = request.POST['nom']
             prenom = request.POST['prenom']
             daten = request.POST['daten']
             models.Patien.objects.filter(pk=id).update(PatNom = nom , PatPrenom = prenom , PatNais = daten)
             return redirect('/task')

        
    
    return render(request,'edit.html',context)

def login(request):

    if request.method == 'POST':
        nom = request.POST.get('username')
        motdepass = request.POST.get('password')

        try:
            user = authenticate(username=nom ,password=motdepass)
            if user is not None:
                print("it work ")
                return redirect('/task')
            else:
                print("do not work ")
          
            
        except Exception as identifier :
            
            return redirect('/task')


    return render(request,'login.html')