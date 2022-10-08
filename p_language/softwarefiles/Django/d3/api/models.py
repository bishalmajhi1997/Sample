from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
#Clean,save,delete
class Musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=100)
class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()
#Field choice,null,blank,choices
class Person1(models.Model):
    SHIRT_SIZES=(
          ("S","Small"),
          ("M","Medium"),
          ("L","Large"),
          )
    name=models.CharField(max_length=50)
    shirt_size=models.CharField(max_length=1,choices=SHIRT_SIZES)
class Runner(models.Model):
    MedalType=models.TextChoices('MedalType','GOLD SILVER BRONZE')
    name=models.CharField(max_length=60)
    medal=models.CharField(blank=True,choices=MedalType.choices,max_length=10)
#Primary_key
class Fruit(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    #Automatic primary key
    #id=models.BigAutoField(primary_key=True)
#Verbose Field name
#class Verbosename(models.Model):
#    first_name=models.CharField("person's first name",max_length=30)
#    f1=models.CharField(max_length=30)
#    api=models.ForeignKey(api,on_delete=models.CASCADE,verbose_name="The related api")
#    sites=models.ManyToManyField(Site,verbose_name="List of sites")
#    place=models.OneToOneField(Place,on_delete=models.CASCADE,verbose_name="related_place")
#Relation:Many-to-one
class Manufacturer(models.Model):
    pass
class Car(models.Model):
    manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    #company_that_makes_it=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
#Relation:Many-to-Many
class Topping(models.Model):
    pass
class Pizz(models.Model):
    toppings=models.ManyToManyField(Topping)
class Person3(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Group(models.Model):
    name=models.CharField(max_length=128)
    members=models.ManyToManyField(Person3,through="Membership")
    def __str__(self):
        return self.name
class Membership(models.Model):
    person=models.ForeignKey(Person3,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    date_joined=models.DateField()
    invite_reason=models.CharField(max_length=64)
#from api.models import ZipCode
#Field name rstrications
#class Example(models.Model):

#    pass=models.IntegerField()
#CommomnField
#Meta options
class Ox(models.Model):
    horn_length=models.IntegerField()
    class Meta:
        ordering=["horn_length"]
        verbose_name_plural="oxen"
#Models Method
import datetime
class Person4(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    def baby_boomer_status(self):
        if self.birth_date < datetime.date(1997,8,8):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1998,1,1):
            return "baby-boomer"
        else:
            return 'post-boomer'
    @property
    def full_name(self):
        return "%s %s "%(self.first_name,self.last_name)
class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()
    def save(self,*args,**kwargs):
        if self.name=="Yoko ones blog !":
            return
        else:
            super().save(*args,*kwargs)
#Model Inheritance#Abstract base class
class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    class Meta:
        abstract=True
        ordering=["name"]
class Student(CommonInfo):
    home_group=models.CharField(max_length=5)
    class Meta(CommonInfo.Meta):
        db_table="student_info"
#Model Multiple inheritance
class CommonInfo1(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    class Meta:
        abstract=True
        ordering=["name"]
class Unmanaged(models.Model):
    class Meta:
        abstract=True
        managed=False

class Student1(CommonInfo1,Unmanaged):
    home_group=models.CharField(max_length=5)
    class Meta(CommonInfo1.Meta,Unmanaged.Meta):
        db_table="student_info"
#Related_name and Related_query
#Multitable inheritance
class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
class Resturant(Place):
    server_hot_dogs=models.BooleanField(default=False)
    serves_pizza=models.BooleanField(default=False)
    #place_ptr=models.OneToOneField(Place,on_delete=models.CASCADE,parent_link=True,primary_key=True,)
#class Supplier(Place):
#    customers=models.ManyToManyField(Place)
#Proxy models in multitable inheritance
class Person6(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
class MyPerson(Person6):
    class Meta:
        proxy=True
    def do_something(self):
        pass
class OrderPerson(Person6):
    class Meta:
        ordering=["last_name"]
        proxy=True
#ProxyModels managers
class NewManager(models.Manager):
    pass
class ExtraManager(models.Model):
    secondary=NewManager()
    class Meta:
        abstract=True
class MyPerson1(Person6,ExtraManager):
    objects=NewManager()
    class Meta:
        proxy=True
#Multiple Inheritance
#class Piece(models.Model):
#    pass
class Article(models.Model):
    article_id=models.AutoField(primary_key=True)
    #article_piece=models.OneToOneField(Piece,on_delete=models.CASCADE,parent_link=True)
class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    #book_piece=models.OneToOneField(Piece,on_delete=models.CASCADE,parent_link=True)
class BookReview(Book,Article):
    pass
