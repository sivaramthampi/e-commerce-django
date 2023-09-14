from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
def call(r):
    return render(r,'home.html',{'name':'World'})

from .models import items

def dbitemsdisp(req):
    page = loader.get_template("dbitemdisp.html")
    db = items.objects.all()
    data = {'Category': 'Electronics',
            'items':db
            }
    response = page.render(data,req)
    return HttpResponse(response)

def product(req,reqid):
    page = loader.get_template("products_d.html")
    obj = items.objects.all()
    data = {'Category': 'Electronics',
            'items':obj.get(id=reqid)
            }
    response = page.render(data,req)
    return HttpResponse(response)

def addtocart(req):
    proid = req.GET['pid']
    qty = req.GET['qty']
    response = HttpResponse("Items Added to Cart")
    print(req.session)
    cartitems={}
    if req.session.__contains__('cartdata2'):
        cartitems = req.session['cartdata2']    
    cartitems[proid] = qty
    req.session['cartdata2'] = cartitems
    print(cartitems)
    return response

def viewcart(req):
    page = loader.get_template('cart.html')
    if req.session.__contains__('cartdata2'):
        for key in req.session.keys():
            itemdb = []
            if key == 'cartdata2':
                key=key
                Items = list(req.session[key].items())
                for i in range(len(Items)):
                    proid = Items[i][0]
                    qty = Items[i][1]
                    db = items.objects.get(id=proid)
                    itemdb.append({
                        'product':proid,
                        'quantity':qty,
                        'name':db.name,
                        'price':db.price,
                        'total':int(qty)*db.price
                    })
        fullamt = 0
        for i in itemdb:
            for k,v in i.items():
                if k == 'total':
                    fullamt = fullamt + int(v)
        data = {"carteddata":itemdb,'full':fullamt}
        response = page.render(data,req)
        return HttpResponse(response)
    else:
        response = page.render({"carteddata":"Cart is empty 🤕"},req)
        return HttpResponse(response)


def jgetdata(req):
    newitem = []
    for i in items.objects.all():
        newitem.append({
            'id':i.id,
            'name':i.name,
            'price':i.price,
            'description':i.description,
            'features':i.features
        })
    data = {'convdata':newitem}
    print(items.objects.all())
    return JsonResponse(data)

def search(req):
    page = loader.get_template('search.html')
    data = {}
    response = page.render(data,req)
    return HttpResponse(response)
from .models import items
def getdata(req,val):
    newitem = []
    for i in items.objects.filter(name__contains = val):
        newitem.append({
            'id':i.id,
            'name':i.name,
            'price':i.price,
            'description':i.description,
            'features':i.features
        })
    data = {'fd':newitem}
    return JsonResponse(data)

def plotter(req):
    page = loader.get_template('ploting.html')
    data = {}
    response = page.render({},req)
    return HttpResponse(response)
