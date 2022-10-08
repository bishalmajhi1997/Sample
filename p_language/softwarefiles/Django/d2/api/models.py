from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
#clean,save,delete
class Musican(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=100)
class Album(models.Model):
    artist=models.ForeignKey(Musican,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()
#Field Types,Field option
class Person1(models.Model):
    SHIRT_SIZES=(
         ("S","Small"),
         ("M","Medium"),
         ("L","Large")
    )
    name=models.CharField(max_length=100)
    shirt_size=models.CharField(max_length=1,choices=SHIRT_SIZES)
#Enumeration of Field types,field Options
class Runner(models.Model):
    MedalType=models.TextChoices('MedalType','GOLD SILVER BRONZE')
    name=models.CharField(blank=True,choices=MedalType.choices,max_length=10)
#Default,help_text,primary key
class Fruit(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    id=models.BigAutoField(primary_key=True)
#Automatic primary key Fields
#Relationships
#1Many_to_one relationships
class Manufacturer(models.Model):
    pass
class Car(models.Model):
    manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    company_that_makes_it=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)

#2Many-to-many relationships
class Topping(models.Model):
    pass
class Pizza(models.Model):
    toppings=models.ManyToManyField(Topping)
#ExtraField of many_to many relationships
class Person2(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Group(models.Model):
    name=models.CharField(max_length=128)
    members=models.ManyToManyField(Person2,through='Membership')
    def __str__(self):
        return self.name
class Membership(models.Model):
    person=models.ForeignKey(Person2,on_delete=models.CASCADE)
    date_joined=models.DateField()
    invite_reason=models.CharField(max_length=64)
#One_to_one relationship
#from geography.models import ZipCode
#class Resturant(models.Model):
#    zip_code=models.Foreignkey(ZipCode,on_delete=models.SET_NULL,blank=True,null=True)
#Field name restrications
#class Example(models.Model):
#     pass=models.IntegerField()
#    foo__bar=models.IntegerField()
#Meta options
class Ox(models.Model):
    horn_length=models.IntegerField()
    class Meta:
        ordering=["horn_length"]
        verbose_name_plural="oxen"
#Model Attributes and Models mthos
import datetime
class Person9(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    def baby_boomer_status(self):
        if self.birth_date < datetime.date(1997,16,5):
            return 'baby boomer'
        else:
            return 'post-boomer'
    @property
    def full_name(self):
        return '%s %s'%(self.first_name,self.last_name)
#Overriding predefined model methods
class Blog(models.Model):
    name=models.CharField(max_length=1000)
    tagline=models.TextField()
    def save(self,*args,**kwargs):
        do_something()
        super().save(*args,**kwargs)
        do_something_else()
class Blog2(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()
    def save(self,*args,**kwargs):
        if self.name=="Yoko Ono's blog.":
            return
        else:
            super().save(*args,**kwargs)
#Abstract base classes
class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    class Meta:
        abstract=True
class Student(CommonInfo):
    home_group=models.CharField(max_length=5)
#Meta Inheritance
class CommonInfo2(models.Model):
    class Meta:
        abstract=True
        ordering=["name"]
class Student1(CommonInfo2):
    class Meta(CommonInfo2.Meta):
        db_table="student_info"

class CommonInf(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    class Meta:
        abstract=True
        ordering=["name"]
class Unmanaged(models.Model):
    class Meta:
        abstract=True
        managed=False
class Student3(CommonInf,Unmanaged):
    hoem_group=models.CharField(max_length=5)
    class meta(CommonInfo.Meta,Unmanaged.Meta):
        pass
class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
class Restrurant(Place):
    serves_hot_dogs=models.BooleanField(default=False)
    serves_pizza=models.BooleanField(default=False)
    place_ptr=models.OneToOneField(Place,on_delete=models.CASCADE,parent_link=True,primary_key=True)
class Supplier(Place):
    customers=models.ManyToManyField(Place)
#Proxy Model
class Person5(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
class MyPerson(Person5):
    class Meta:
        proxy=True
    def do_something(self):
        pass
class OrederedPerson(Person):
    class Meta:
        ordering:["last_name"]
        proxy=True
#Procy model Managers
class NewManager(models.Manager):
    pass
    class Meta:
        proxy=True
#Create an ABstract class For the new manager
class ExtraManagers(models.Model):
    seconday=NewManager()
    class Meta:
        abstract=True
class MyPerson1(Person5,ExtraManagers):
    class Meta:
        proxy=True
#Multiple Inheritance
class Article(models.Model):
    article_id=models.AutoField(primary_key=True)
class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
class BookReview(Book,Article):
    pass
#Multiple inheritance and onetoone field
class Piece(models.Model):
    pass
class Article1(Piece):
    article_piece=models.OneToOneField(Piece,on_delete=models.CASCADE,parent_link=True)
class BookReview(Book,Article1):
    pass
