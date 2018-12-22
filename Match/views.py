from django.shortcuts import render
from . models import user
from . main_match import main_match
import json
from django.http import HttpResponse

def match(request):
    return render(request, 'match.html')

def matching(request):
    username = request.POST.get('username')
    product_link = request.POST.get('url')
    category1 = request.POST.get('category1')
    category2 = request.POST.get('category2')
    user_id = user.get_id(username)
    info = [user_id, product_link, category1, category2]
    result = main_match(info)
    return HttpResponse(json.dumps(result))
