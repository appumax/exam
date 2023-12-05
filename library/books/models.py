from django.db import models

# Create your models here.
class Books(models.Model):
    Title=models.CharField(max_length=80)
    Author=models.CharField(max_length=80)
    Genre=models.CharField(max_length=80)
    ISBN=models.IntegerField()
    Availability=models.BooleanField()

    def __str__(self):
        return f"Book.no:{self.ISBN},Title:{self.Title}"
class Patron(models.Model):
    Name=models.CharField(max_length=80)
    Contact_no=models.BigIntegerField()
    membership_id=models.IntegerField()

    def __str__(self):
        return f"{self.membership_id}"

class Borrow(models.Model):
    Title=models.ForeignKey(Books,on_delete=models.CASCADE)
    membership_id=models.ForeignKey(Patron,on_delete=models.CASCADE)
    Borrow_date=models.DateField(auto_now=True)
    Return_date=models.DateField(null=True)

