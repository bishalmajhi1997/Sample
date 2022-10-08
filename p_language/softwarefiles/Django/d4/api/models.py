from django.db import models

# Create your models here.
class Student(models.Model):
    FRESHMAN="FR"
    SOPHOMORE="SO"
    JUNIOR="JR"
    SENIOR="SR"
    GRADUATE="GR"
    YEAR_IN_SCHOOL_CHOICES=[
      (FRESHMAN,"Freshman"),
      (SOPHOMORE,"Sophmore"),
      (JUNIOR,"Junior"),
      (SENIOR,"Senior"),
      (GRADUATE,"Graduate")
    ]
    year_in_school=models.CharField(max_length=2,choices=YEAR_IN_SCHOOL_CHOICES,default=FRESHMAN)
    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR,self.SENIOR}
