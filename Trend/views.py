from django.shortcuts import render
import json
from . models import product
from . models import user
from . models import userstyle
from django.http import Http404
from django.http import HttpResponse
from . ran import randomNewProduct
from . update_one_style import update_one_style

def trend(request):
    products = product.objects(wid__in=randomNewProduct())
    context = {
        'products': products
    }
    return render(request, 'trend.html', context)

def loadMore(request):
    product_json = {}
    page = int(request.POST.get('page'))
    product_list = randomNewProduct()
    if (page+1)*20 < len(product_list):
        for i in range(20):
            try:
                single_product = product.objects(wid=product_list[page*20+i])
                p_wid = single_product[0].wid
                p_title = single_product[0].title
                p_url = single_product[0].url
                p_favour_count = single_product[0].favour_count
                p_info = {'wid':p_wid, 'title': p_title, 'url':p_url, 'favour_count':p_favour_count}
                product_json['product'+str(i)] = p_info
            except:
                print("loaderror")
                continue
        return HttpResponse(json.dumps(product_json))
    else:
        return HttpResponse('end')

def likeCount(request):
    um = request.POST.get('username')
    productId = request.POST.get('productId')
    count = int(request.POST.get('likeChange'))
    # print(count)
    count_before = int(product.objects(wid=productId)[0].favour_count)
    updateCount = str(count_before + count)
    # print(updateCount)
    favour_count_success = product.updateFavour_count(productId, updateCount);
    try:
        if(um!="NULL"):
            if(product.getStyleById(productId)!=None):
                u_id = user.get_id(um)
                print(u_id)
                update_one_style(u_id, productId, count)
    except:
        print("update userstyle failed")
    return HttpResponse(favour_count_success)
    # for i in pdclike:
    #     print(i._id)
    #     i.save(validate=False)
    #     count_before = i.favour_count
    #     i.update(set__favour_count=str(count_before + count))
    #     print(count_before + count)
    #     i.save(validate=False)
    #     pdclike[0].save(validate=False)
    #     print(i.favour_count)
# def trend(request):
#     products = docs.db_clr_pdc.objects
#     context = {
#         'ProductInfo': products
#     }
#     return render(request, 'trend.html', context)