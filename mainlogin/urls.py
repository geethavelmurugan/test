from django.conf.urls import patterns, include, url
from mainlogin.views import *
from advertisement.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mainlogin.views.home', name='home'),
    # url(r'^mainlogin/', include('mainlogin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^home/$', 'mainlogin.views.home', name='home'),
    url(r'^login/$', 'mainlogin.views.user_login', name='user_login'),
    url(r'^new_user/$', 'mainlogin.views.register', name='register'),
    url(r'^logout/$', 'mainlogin.views.logout_view', name='logout_view'),
    url(r'^userpage/$', 'mainlogin.views.user_page',name='userpage'),
    url(r'^start/$', 'mainlogin.views.start',name='start'),
    url(r'^postpage/$', 'advertisement.views.post_page',name='post_page'),
    url(r'^addproduct/$', 'advertisement.views.add_product',name='add_product'),
    url(r'^categorypage/$', 'advertisement.views.category_page',name='category'),
    url(r'^postadd/(?P<subid>.*)/$', 'advertisement.views.post_add',name='post_add'),
    url(r'^subcategory/(?P<id>\d+)/$', 'advertisement.views.sub_category',name='sub_category'),
    url(r'^category/(?P<categoryname>.*)/(?P<id>\d+)$', 'mainlogin.views.sub_category1',name='sub_category1'),
    url(r'^subcategory/(?P<subcategoryname>.*)/(?P<id>\d+)$', 'mainlogin.views.View_ads',name='View_ads'),
    url(r'^notes/$', 'advertisement.views.notes',name='notes'),
    url(r'^search/', include('haystack.urls')),
 
   )