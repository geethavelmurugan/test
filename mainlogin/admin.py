# Import the UserProfile model individually.
from mainlogin.models import *
from django.contrib import admin



# Import the UserProfile model with Category and Page.
# If you choose this option, you'll want to modify the import statement you've already got to include UserProfile.
# from logininew.models import Category, Page, UserProfile

admin.site.register(UserProfile)
# admin.site.register(Advertisement.Advertisementadmin)




