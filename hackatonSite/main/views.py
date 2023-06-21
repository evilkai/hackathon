from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib import messages

from .models import Student, Ad, Telegram
from django.contrib.auth.models import User, Group
from .defs import getDate, setDate, isAuth, convertDocPdf, StipendList
from .certificateStudy import study_statement
from .certificateStipend import income_statement
from .botIATE import send_message

from django.views.generic import DetailView

# Create your views here.
date = getDate

sdnts = Student.objects.all()


def profile(request):
    if not request.user.is_staff or request.user.is_superuser:
        for sdnt in sdnts:
            fullname = sdnt.fullname.split()
            print(request.user.first_name + "???" + fullname[1])
            print(request.user.last_name + "???" + fullname[0])
            if request.user.first_name == fullname[1] and request.user.last_name == fullname[0]:
                stud = sdnt
                break

        return render(request, 'main/profile.html', {'student': stud})
    else: return render(request, 'main/profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')




def register(request):
    signal = 0
    if not(request.user.is_authenticated):
        if request.method == "POST":
                for sdnt in sdnts:
                    if sdnt.registration==False:
                        if request.POST.get('studentID')==sdnt.studentID:

                            
                            fullname = sdnt.fullname.split()


                            if request.POST.get('password1')==request.POST.get('password2'):
                                userName=request.POST.get('login')
                                firstName=fullname[1]
                                lastName=fullname[0]
                                newUser=User.objects.create(username=userName, first_name=firstName, last_name=lastName)

                                newUser.set_password(request.POST.get('password1'))

                                
                                newUser.save()
                                sdnt.registration=True
                                sdnt.save()

                                return redirect("home")
                            else:
                                signal = 2
                        else: signal = 1
                    else: signal = 3

    return render(request, "registration/register.html", {'signal': signal})







##################################

def schedule(request):
    return render(request, 'main/schedule.html')



def index(request):
    ads = Ad.objects.all()
    ads = list(reversed(ads))
    return render(request, 'main/index.html', {'ads': ads, 'date':date})


def adpage(request, pk_page):
    page=Ad.objects.get(id=pk_page)
    if request.method=="GET":
        if request.GET.get('delete'):
            page.delete()
            print("DA")
            redirect('http://127.0.0.1:8000/')
    return render(request, 'main/adpage.html',  {'page':page, 'date':date  })



def createad(request):
    if request.user.is_staff:
        if request.method=="POST":
                
                adel = Ad.objects.create(title=request.POST.get('title') , description = request.POST.get('description'))
                adel.save()
                adlist= set()
                ads = Telegram.objects.all()
                for ad in ads:
                    adlist.add(ad.tgID)
                send_message(request.POST.get('title'), request.POST.get('description'), adlist)

        return render(request,'main/createad.html')
























######################################################


def certificateStudy(request):
    for sdnt in sdnts:
        fullname = sdnt.fullname.split()
        print(request.user.first_name + "???" + fullname[1])
        print(request.user.last_name + "???" + fullname[0])
        if request.user.first_name == fullname[1] and request.user.last_name == fullname[0]:
            studentDict = dt = {'FIO': sdnt.fullname, 
                                'course': sdnt.year, 
                                'docx_file': 
                                'demo.docx', 
                                'direction': sdnt.direction,
                                'form':  sdnt.form,
                                'country': sdnt.country,
                                'basis': sdnt.basis,
                                'date': getDate() }
            study_statement(**studentDict)
            convertDocPdf()
            break

    return render(request, 'main/certificateStudy.html')






def certificateStipend(request):
    for sdnt in sdnts:
        fullname = sdnt.fullname.split()
        print(request.user.first_name + "???" + fullname[1])
        print(request.user.last_name + "???" + fullname[0])
        if request.user.first_name == fullname[1] and request.user.last_name == fullname[0]:
            studentDict = dt = {'FIO': sdnt.fullname, 
                                'docx_file': 
                                'demo.docx', 
                                'date': getDate(),
                                'stlist': StipendList
                                }
            income_statement(sdnt.studentID, **studentDict)
            convertDocPdf()
            break

    return render(request, 'main/certificateStipend.html')
