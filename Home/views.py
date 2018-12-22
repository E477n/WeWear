from django.shortcuts import render
from django.http import Http404
from .models import user, userstyle
from django.http import HttpResponse
import json


def index(request):
    return render(request, 'index.html')

# def detail(request, User_id):
#     try:
#         user = User.objects.get(pk=User_id)
#     except User.DoesNotExist:
#         raise Http404("User does not exist")
#     return render(request, 'userDetail.html', {'id': str(User_id)})

def logIn(request):
    um = request.POST.get('username')
    pw = request.POST.get('password')
    return HttpResponse(user.checkLogIn(um, pw))

def signIn(request):
    em = request.POST.get('email')
    um = request.POST.get('username')
    pw = request.POST.get('password')
    pw_check = request.POST.get('password_check')
    sx = request.POST.get('sex')
    bd = request.POST.get('birthday')
    jo = request.POST.get('job')
    expd = request.POST.get('expenditure')
    user_info = [em, um, pw, sx, bd, jo,expd]
    return HttpResponse(user.checkSignIn(user_info))

def insertStyleInfo1(request):
    style_set = request.POST.getlist('style_set1')
    return HttpResponse(userstyle.style_info_update(style_set))
def insertStyleInfo2(request):
    style_set = request.POST.getlist('style_set2')
    return HttpResponse(userstyle.style_info_update(style_set))

def getUserInfo(request):
    user_n = request.POST.get('username')
    return HttpResponse(user.getUserInfoByUsername(user_n))

def startMatching(request):
    pdc_link = request.POST.get('product_link')
    print(pdc_link)
    context = {
        'pdc_link': pdc_link
    }
    return render(request, 'match.html', context)
