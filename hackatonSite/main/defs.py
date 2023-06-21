import datetime
import calendar
from django.contrib.auth.models import Group
from .models import Student
from docx2pdf import convert



def getDate():
    print((datetime.date(2023, 4, 30)-datetime.date.today()).days)
    return datetime.date.today()

def dateStat(date):
    if date-datetime.date.today()<=0:
        return 0
    else: return 1


def next_month():
    somedate = datetime.date.today()
    months = 1
    month = somedate.month - 1 + months
    year = somedate.year + month // 12
    month = month % 12 + 1
    day = min(somedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def setDate(k):
    somedate=getDate()
    q1=datetime.date(somedate.year, 3, 31)
    q2=datetime.date(somedate.year, 6, 30)
    q3=datetime.date(somedate.year, 9, 30)
    q4=datetime.date(somedate.year, 12, 31)
    quarter=(q1,q2,q3,q4)
    if k==True:
        for el in quarter:
            if el > q1:
                return el
    else:
        return datetime.date(somedate.year, somedate.month, calendar.monthrange(somedate.year,somedate.month)[1])


def getGroups():
    
    GROUP_CHOICES = []
    GROUP_CHOICES.append(("all","all"))
    for group in Group.objects.all():
        GROUP_CHOICES.append((group.name, group.name))
    return GROUP_CHOICES


groups = []
for group in Group.objects.all():
    groups.append(group.name)

def isAuth(User):
    global groups
    for group in User.groups.all():
        if group.name=="Client":
            return "Client"
        elif group.name in groups:
            return "Staff"
        

def convertDocPdf():
    
    folderDir = "C:/DjangoProjects/hackatonSite/main/static/images/"
    inputFile = folderDir + "demo.docx"
    outputFile = folderDir + "demo2.pdf"
    convert(inputFile, outputFile)




























#########################################

StipendList = [
    
        ['январь', ['111222333','12312','124352'], ['12312','124352']],
        ['февраль', ['111222333','12312','124352'], ['12312','124352']],
        ['март', ['111222333','12312','124352'], ['111222333','12312','124352']],
        ['апрель', ['111222333','12312','124352'], ['111222333','12312','124352']],
        ['май', ['111222333','12312','124352'], ['111222333','12312','124352']]
    


]