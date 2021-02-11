from django.db import models


class Daytime(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Land(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Gathering(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Adventure(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Crafting(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Reputation(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class RecipeType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(blank=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)
    land_difficulty = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    exploration = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    reputation_value = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    type = models.ForeignKey(RecipeType, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    gathering = models.ForeignKey(Gathering, on_delete=models.CASCADE, blank=True, null=True)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, blank=True, null=True)
    crafting = models.ForeignKey(Crafting, on_delete=models.CASCADE, blank=True, null=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    reputation_value = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Training(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)
    difficulty = models.IntegerField(blank=True, null=True)
    recovery = models.IntegerField(blank=True, null=True)
    gold_reward = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class NPC(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
