from django.db import models
from rest_framework import serializers

class Meal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    complexity = models.PositiveSmallIntegerField()
    soup  = models.PositiveSmallIntegerField(default=0)
    takeaway = models.PositiveSmallIntegerField(default=0)
    sweet = models.PositiveSmallIntegerField(default=0)
    meat = models.PositiveSmallIntegerField(default=0)
    cold = models.PositiveSmallIntegerField(default=0)
    remains = models.PositiveSmallIntegerField(default=0)
    fish = models.PositiveSmallIntegerField(default=0)
    salad = models.PositiveSmallIntegerField(default=0)
    fast = models.PositiveSmallIntegerField(default=0)
    vegetarian = models.PositiveSmallIntegerField(default=0)
    meatloaf = models.PositiveSmallIntegerField(default=0)
    noodles = models.PositiveSmallIntegerField(default=0)
    mushrooms = models.PositiveSmallIntegerField(default=0)
    broccoli = models.PositiveSmallIntegerField(default=0)
    shrimps = models.PositiveSmallIntegerField(default=0)
    zucchini = models.PositiveSmallIntegerField(default=0)
    ham = models.PositiveSmallIntegerField(default=0)
    rice = models.PositiveSmallIntegerField(default=0)
    pizza = models.PositiveSmallIntegerField(default=0)
    fruits = models.PositiveSmallIntegerField(default=0)
    gnocci = models.PositiveSmallIntegerField(default=0)
    spinach = models.PositiveSmallIntegerField(default=0)
    beans = models.PositiveSmallIntegerField(default=0)
    sugar = models.PositiveSmallIntegerField(default=0)
    apples = models.PositiveSmallIntegerField(default=0)
    cauliflower = models.PositiveSmallIntegerField(default=0)
    feta = models.PositiveSmallIntegerField(default=0)
    chicken = models.PositiveSmallIntegerField(default=0)
    eggs = models.PositiveSmallIntegerField(default=0)
    tuna = models.PositiveSmallIntegerField(default=0)
    curd_cheese = models.PositiveSmallIntegerField(default=0)
    lentils = models.PositiveSmallIntegerField(default=0)
    cheese = models.PositiveSmallIntegerField(default=0)
    yeast = models.PositiveSmallIntegerField(default=0)
    sweet_potatoes = models.PositiveSmallIntegerField(default=0)
    sausage = models.PositiveSmallIntegerField(default=0)
    gorgonzola = models.PositiveSmallIntegerField(default=0)
    pineapple = models.PositiveSmallIntegerField(default=0)
    potatoes = models.PositiveSmallIntegerField(default=0)
    dumplings = models.PositiveSmallIntegerField(default=0)
    cabbage = models.PositiveSmallIntegerField(default=0)
    tomatoes = models.PositiveSmallIntegerField(default=0)

    def update(self, *args, **kwargs):
        for name,values in kwargs.items():
            try:
                setattr(self,name,values)
            except KeyError:
                pass

        self.save()

class MealSerialize(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    complexity = serializers.IntegerField()
    soup  = serializers.IntegerField()
    takeaway = serializers.IntegerField()
    sweet = serializers.IntegerField()
    meat = serializers.IntegerField()
    cold = serializers.IntegerField()
    remains = serializers.IntegerField()
    fish = serializers.IntegerField()
    salad = serializers.IntegerField()
    fast = serializers.IntegerField()
    vegetarian = serializers.IntegerField()
    meatloaf = serializers.IntegerField()
    noodles = serializers.IntegerField()
    mushrooms = serializers.IntegerField()
    broccoli = serializers.IntegerField()
    shrimps = serializers.IntegerField()
    zucchini = serializers.IntegerField()
    ham = serializers.IntegerField()
    rice = serializers.IntegerField()
    pizza = serializers.IntegerField()
    fruits = serializers.IntegerField()
    gnocci = serializers.IntegerField()
    spinach = serializers.IntegerField()
    beans = serializers.IntegerField()
    sugar = serializers.IntegerField()
    apples = serializers.IntegerField()
    cauliflower = serializers.IntegerField()
    feta = serializers.IntegerField()
    chicken = serializers.IntegerField()
    eggs = serializers.IntegerField()
    tuna = serializers.IntegerField()
    curd_cheese = serializers.IntegerField()
    lentils = serializers.IntegerField()
    cheese = serializers.IntegerField()
    yeast = serializers.IntegerField()
    sweet_potatoes = serializers.IntegerField()
    sausage = serializers.IntegerField()
    gorgonzola = serializers.IntegerField()
    pineapple = serializers.IntegerField()
    potatoes = serializers.IntegerField()
    dumplings = serializers.IntegerField()
    cabbage = serializers.IntegerField()
    tomatoes = serializers.IntegerField()
