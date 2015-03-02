from django.db import models
from django.forms import ModelForm
from mainlogin.models import User


STATE_CHOICES = (
    ('seller', 'Seller'),
    ('buyer', 'Buyer')
   )

condition = (
    ('used', 'Used'),
    ('new', 'New')
   )

you=( ('individual','Individual'),('dealer','Dealer'))

# Begin Mobile models ..........
   
# mobile Phone

class Mobilebrand(models.Model):
     mobilebrand = models.CharField(max_length=50,null=True)
          
     def __unicode__(self):
        return self.mobilebrand 
     
class Mobilemodel(models.Model):
     mobilemodel = models.CharField(max_length=50,null=True)
      
     def __unicode__(self):
        return self.mobilemodel    
     
class Os(models.Model):
     os = models.CharField(max_length=50,null=True)
     
     def __unicode__(self):
        return self.os
     
class Sim(models.Model):
     sim = models.CharField(max_length=50,null=True)
     
     def __unicode__(self):
        return self.sim
    
class Mobileinclude(models.Model):
     mobileinclude = models.CharField(max_length=50,null=True)
     
     def __unicode__(self):
        return self.mobileinclude

class MobilesManager(models.Manager):
     def get_query_set(self):
        return (super(MobilesManager, self).get_query_set().order_by('mobilebrandname'))
    
     def __unicode__(self):
        return self.mobilebrandname
    

class MobilesAbstract(models.Model):
    mobilebrandname=models.ForeignKey(Mobilebrand)
    mobilemodelname = models.ForeignKey(Mobilemodel)
    mobile_os = models.ForeignKey(Os)
    mobile_sim = models.ForeignKey(Sim)
    mobile_include = models.ForeignKey(Mobileinclude)
     
    class Meta:
       abstract = True


class Mobiles(MobilesAbstract):
    objects = MobilesManager()
    

    
# Tablets  

class Tabletbrand(models.Model):
     tabletbrand = models.CharField(max_length=50,null=True)  
     
     def __unicode__(self):
        return self.tabletbrand

class TabletsManager(models.Manager):
     def get_query_set(self):
        return (super(TabletsManager, self).get_query_set().order_by('tabletbrandname'))

class TabletsAbstract(models.Model):
    tabletbrandname=models.ForeignKey(Tabletbrand)
    

    class Meta:
       abstract = True

   
class Tablets(TabletsAbstract):
    objects = TabletsManager()
    
# Accessories

class Accesstype(models.Model):
     accesstype = models.CharField(max_length=50,null=True)
     
     def __unicode__(self):
        return self.accesstype

     
class Accessbrand(models.Model):
     accessbrand = models.CharField(max_length=50,null=True)   
    
     def __unicode__(self):
        return self.accessbrand
    
class AccessManager(models.Manager):
     def get_query_set(self):
        return (super(AccessManager, self).get_query_set().order_by('accesstypename'))

class AccessAbstract(models.Model):
    accesstypename=models.ForeignKey(Accesstype)
    accessbrandname = models.ForeignKey(Accessbrand)

    class Meta:
       abstract = True

class Access(AccessAbstract):
    objects = AccessManager()
 
# Ends Mobile Brand ...........

# Begin Car brand

class Carbrand(models.Model):
    carbrand=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.carbrand
    
class Carmodel(models.Model):
    carmodel=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.carmodel

class Motorbrand(models.Model):
    motorbrand=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.motorbrand
    
class Motormodel(models.Model):
    motormodel=models.CharField(max_length=50)

    def __unicode__(self):
        return self.motormodel
    
class Scooterbrand(models.Model):
    scooterbrand=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.scooterbrand
    
class Scootermodel(models.Model):
    scootermodel=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.scootermodel

class Spare_Producttype(models.Model):
    spare_producttype=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.spare_producttype

class Buses_Vehicletype(models.Model):
    buses_vehicletype=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.buses_vehicletype
    
class Construction_Vehicletype(models.Model):
    construction_vehicletype=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.construction_vehicletype
 
class Year(models.Model):
    year=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.year

class Color(models.Model):
    color=models.CharField(max_length=50)  
    
    def __unicode__(self):
        return self.color

class Fueltype(models.Model):
    fueltype=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.fueltype

class CarsManager(models.Manager):
    def get_cars(self):
        return (super(CarsManager, self).get_query_set().order_by('carbrand'))

class CarsAbstract(models.Model):
 
    brand = models.ForeignKey(Carbrand)
    model=models.ForeignKey(Carmodel)
    year = models.ForeignKey(Year)
    kmsdriven=models.CharField(max_length=10)
    color=models.ForeignKey(Color)
    fueltype=models.ForeignKey(Fueltype)
    
    class Meta:
        abstract = True
 

class Cars(CarsAbstract):
    object= CarsManager()

# Ends Car model

     
class City(models.Model):
    city=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.city

class Locality(models.Model):
    locality=models.CharField(max_length=50)
    city_ref_id= models.ForeignKey(City)
    
    def __unicode__(self):
        return self.locality


class Category(models.Model):
    icon = models.ImageField(upload_to='static/img', blank=True)
    name = models.CharField(max_length=250)
 
    def __unicode__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50)
     
    def __unicode__(self):
         return self.name


class Product(models.Model):
    user = models.ForeignKey(User)
    photo = models.ImageField(upload_to='static/img',blank=True)
    category = models.ForeignKey(Category,null=False)
    subcategory = models.ForeignKey(SubCategory,null=False)
    title = models.CharField(max_length=200)
    condition = models.CharField(max_length=25,choices=condition,default='used') 
    description = models.TextField(max_length=20, verbose_name="Describe what makes your ad unique:*")
    price = models.FloatField(default='$',help_text=".00") 
    addtype = models.CharField(max_length=25,choices=STATE_CHOICES,default="seller") 
    you_are = models.CharField(max_length=20,choices=you,default="individual")
    you_name = models.CharField(max_length=20)
    you_email = models.CharField(max_length=30)
    you_phone = models.CharField(max_length=12)
    timestamp = models.DateTimeField(auto_now=True)
    city=models.ForeignKey(City)
    locality=models.ForeignKey(Locality)
    
   
    cars=models.OneToOneField(Cars,null=True,blank=True)
    mobile = models.OneToOneField(Mobiles,null=True,blank=True)
    tablets = models.OneToOneField(Tablets,null=True,blank=True)
    access = models.OneToOneField(Access,null=True,blank=True)
    
    

    def __unicode__(self):
        return self.title

class ProductForm(ModelForm):
    class Meta:
        model = Product
        
# class Note(models.Model):
#     title = models.CharField(max_length=1000)
#     body = models.TextField()
#     timestamp = models.DateTimeField(auto_now=True)

#     def __unicode__(self):
#         return self.title