from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Land(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Gathering(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Adventure(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Crafting(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=64, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Reputation(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=64, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=64, blank=True)
    price = models.IntegerField()
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE)
    reputation_value = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64, blank=True)
    price = models.IntegerField()
    count = models.IntegerField()
    gathering = models.ForeignKey(Gathering, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    crafting = models.ForeignKey(Crafting, on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE)
    reputation_value = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Training(models.Model):
    name = models.CharField(max_length=64, blank=True)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
