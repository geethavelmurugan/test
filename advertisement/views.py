# Create your views here.

import logging
import pprint
from advertisement.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.context_processors import csrf 
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext, string_concat
from advertisement.forms import ProductSearchForm

import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet



def post_page(request):
    return render_to_response('advertisement/ad.html', { }, context_instance=RequestContext(request)) 


def category_page(request):

        entries = Category.objects.all()
        path=request.path
        print path
        return render_to_response('advertisement/category.html',{'category' : entries, 'path':path},context_instance=RequestContext(request)
    )
        


def add_product(request):
    success=False
    
    product = Product()
    product.user = User.objects.get(id=request.POST['user'])
    product.category  = Category.objects.get(id=request.POST['category'])
    print product.category.id
    product.subcategory  = SubCategory.objects.get(id=request.POST['subcategory'])
    print product.subcategory.id
    
    
    
# car
    if product.subcategory.id == 1:
        print "car"
        cars1=Cars()
        cars1.brand=Carbrand.objects.get(id=request.POST['brand'])
        cars1.model=Carmodel.objects.get(id=request.POST['model'])
        cars1.year=Year.objects.get(id=request.POST['year'])
        cars1.kmsdriven=request.POST.get('kmsdriven')
        cars1.color=Color.objects.get(id=request.POST['color'])
        cars1.fueltype=Fueltype.objects.get(id=request.POST['fueltype'])
        cars1.save()
        product.cars=cars1    
    
# mobile phones    
    if product.subcategory.id == 8:
        print "mobile"
        mobiles1=Mobiles()
        mobiles1.mobilebrandname = Mobilebrand.objects.get(id=request.POST['mobilebrandname'])
        mobiles1.mobilemodelname = Mobilemodel.objects.get(id=request.POST['mobilemodelname']) 
        mobiles1.mobile_os = Os.objects.get(id=request.POST['mobile_os']) 
        mobiles1.mobile_sim = Sim.objects.get(id=request.POST['mobile_sim']) 
        mobiles1.mobile_include = Mobileinclude.objects.get(id=request.POST['mobile_include']) 
        mobiles1.save()
        product.mobile=mobiles1

# Tablets

    if product.subcategory.id == 9:
        
        tablets1 = Tablets()
        tablets1.tabletbrandname = Tabletbrand.objects.get(id=request.POST['tabletbrandname'])
        tablets1.save()
        product.tablets=tablets1
        
# Accessoties

    if product.subcategory.id == 10:
        
        access1 = Access()
        access1.accesstypename = Accesstype.objects.get(id=request.POST['accesstypename'])
        access1.accessbrandname = Accessbrand.objects.get(id=request.POST['accessbrandname'])
        access1.save()
        product.access=access1        


    product.photo = request.FILES.get('photo')
    product.title  = request.POST.get('title', '')
    product.condition  = request.POST.get('condition','')
    product.description  = request.POST.get('description', '')
    
    product.price  = request.POST.get('price')
    product.addtype  = request.POST.get('addtype', '')
    product.city=City.objects.get(id=request.POST['city'])
    product.locality=Locality.objects.get(id=request.POST['locality'])
     
    product.you_are  = request.POST.get('you_are', '')
    product.you_name   = request.POST.get('you_name', '')
    product.you_email   = request.POST.get('you_email', '')
    product.you_phone   = request.POST.get('you_phone', '')

    product.save()
    success=True
    ctx = {'success':success}
    return render_to_response('advertisement/ad.html', ctx , context_instance=RequestContext(request))
   
    
    
 
def post_add(request, subid=None):
    userid= request.user.id
   
    print subid
    subcategory = SubCategory.objects.get(id=subid)
    print subcategory.name
    subcategoryname= subcategory.name
    print subcategory.category_id
    categoryid=subcategory.category_id
    category=Category.objects.get(id=categoryid)
    print category.name
    categoryname=category.name
    categoryicon = category.icon
    
  
    categorynew=Category.objects.get(pk=categoryid)
    subcategorynew=SubCategory.objects.get(pk=subid)
    
    mobilebrand1 = Mobilebrand.objects.all()[0:4]
    mobilebrand2 = Mobilebrand.objects.all()[4:6]
    mobilemodel1 = Mobilemodel.objects.all()[0:4]
    mobilemodel2 = Mobilemodel.objects.all()[4:6]
    os = Os.objects.all()
    sim = Sim.objects.all()
    mobileinclude = Mobileinclude.objects.all()
    tabletbrand = Tabletbrand.objects.all()[0:4]
    tabletbrand1 = Tabletbrand.objects.all()[4:6]

    
    accessbrand = Accessbrand.objects.all()
    
    accesstype = Accesstype.objects.all()[0:4]
    accesstype1 = Accesstype.objects.all()[4:6]

    carbrand=Carbrand.objects.all()[0:6]
    carbrand1=Carbrand.objects.all()[6:11]
    carmodel=Carmodel.objects.all()[0:3]
    carmodel1=Carmodel.objects.all()[3:6]
    year=Year.objects.all()
    color=Color.objects.all()
    fueltype=Fueltype.objects.all()
    city=City.objects.all()

    city=City.objects.all()
    locality=Locality.objects.all()
    pondicherrylocality=Locality.objects.all()[0:3]
    chennailocality=Locality.objects.all()[3:5]


  
   
    ctx = {'userid':userid,'subcategoryname':subcategoryname,'categoryname':categoryname,'categoryicon':categoryicon,'subid':subid,'categoryid':categoryid, 
           'mobilebrand1':mobilebrand1,'mobilebrand2':mobilebrand2,'mobilemodel1':mobilemodel1,'mobilemodel2':mobilemodel2,'os':os,'sim':sim,'mobileinclude':mobileinclude,
           'tabletbrand':tabletbrand,'tabletbrand1':tabletbrand1,'accesstype':accesstype,'accessbrand':accessbrand,'accesstype1':accesstype1,
           'carbrand':carbrand,'carbrand1':carbrand1,'carmodel':carmodel,'carmodel1':carmodel1,'year':year,'color':color,
           'fueltype':fueltype,'city':city,'locality':locality,'pondicherrylocality':pondicherrylocality,'chennailocality':chennailocality,
          }
    return render_to_response('advertisement/ad.html', ctx , context_instance=RequestContext(request))


def sub_category(request, id=None):
    subcategory = SubCategory.objects.filter(category_id=id)
    path=request.path
    print path
    ctx = {'subcategory':subcategory,'path':path}
    return render_to_response('advertisement/category.html', ctx , context_instance=RequestContext(request))

def notes(request):
    form = ProductSearchForm(request.GET)
    notes = form.search()
    return render_to_response('advertisement/notes.html', {'notes': notes})



def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.title for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')