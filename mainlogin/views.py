#views.py

from mainlogin.forms import UserForm, UserProfileForm
import logging
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
from advertisement.models import *


def home(request):
    
      return render_to_response('mainlogin/login.html', { }, context_instance=RequestContext(request)) 
#       return render_to_response('mainlogin/login.html') 
#     return HttpResponse('/login/')
 
@csrf_protect 
def user_login(request):
    def errorHandle(error):
        form = UserForm()
        return render_to_response('mainlogin/login.html', {
                'error' : error,
                'form' : form,
        },context_instance=RequestContext(request))
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    form = UserForm(request.POST) # A form bound to the POST data
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
 
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
 
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/start/')
            else:
                # An inactive account was used - no logging in!
                error = ugettext('Account disable')
                return errorHandle(error)
                
        else:
            # Bad login details were provided. So we can't log the user in.
            error = ugettext('Invalid user')

#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse('Invalid login details')
            return errorHandle(error)
            
 
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
#          print'successfull'
#          return HttpResponse("login.")
#     return render(request, 'mainlogin/userpage.html', {}) 
      form = UserForm() # An unbound form
      
       
      
    return render_to_response('mainlogin/userpage.html', {}, context_instance=RequestContext(request)
)

@csrf_protect
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
 
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
 
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
 
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
 
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
 
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
 
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
 
            # Now we save the UserProfile model instance.
            profile.save()
 
            # Update our variable to tell the template registration was successful.
            registered = True
 
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors
 
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
 
    # Render the template depending on the context.
    return render_to_response('mainlogin/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
                                context_instance=RequestContext(request))
     
#     return render_to_response('/', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
#                                 context_instance=RequestContext(request))
     

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@csrf_protect
def user_page(request):
    return render_to_response('mainlogin/userpage.html',
        context_instance=RequestContext(request)
    )
#  

def start(request):
     category = Category.objects.all()
     path=request.path
     return render_to_response('mainlogin/userpage.html',{'category':category,'path':path},context_instance=RequestContext(request)
    )
    
def sub_category1(request,categoryname,id=None):
    
    print id
    subcategory = SubCategory.objects.filter(category_id=id)
    path=request.path
    ctx = {'subcategory':subcategory,'categoryname':categoryname,'path':path}
    return render_to_response('mainlogin/userpage.html', ctx , context_instance=RequestContext(request))

def View_ads(request,subcategoryname,id=None):
    
    print id
    product = Product.objects.filter(subcategory_id=id)
    path=request.path
    ctx = {'subcategoryname':subcategoryname,'product':product,'path':path}
    return render_to_response('mainlogin/userpage.html', ctx , context_instance=RequestContext(request))