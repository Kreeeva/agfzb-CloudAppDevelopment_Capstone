from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    Name = models.CharField(null=False, max_length=30, default='Name')
    Description = models.CharField(max_length=1000)

    def __str__(self):
        return "Car Make: " + self.Name + "," + \
               "Description: " + self.Description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    Carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    Name = models.CharField(null=False, max_length=30,default="Name")
    Dealer_id = models.IntegerField(default=0)
    Type = models.CharField(null=False, max_length=30,default="Type")
    Year = models.DateField(default=now)

    def __str__(self):
        return "Car Model:" + self.Name 



# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.review = review
        self.purchase = purchase
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""
        self.id = ""
        self.sentiment = ""
    def __str__(self):
        return  "Dealer review:" + self.review
