from django.db import models
from django.urls import reverse


class Daytime(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weapon', args=[str(self.id)])


class EquipmentSlot(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Land(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('land', args=[str(self.id)])


class Gathering(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gathering', args=[str(self.id)])


class Adventure(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('adventure', args=[str(self.id)])


class Crafting(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crafting', args=[str(self.id)])


class Reputation(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reputation', args=[str(self.id)])


class Guild(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)
    land_difficulty = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('region_card', args=[str(self.id)])


class Location(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    exploration = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    quest = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Companion(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    quest = models.BooleanField(blank=True, null=True, default=False)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    comfort = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companion_card', args=[str(self.id)])


class NPC(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    reputation_value = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)
    building = models.BooleanField(default=False)
    equipment_slot = models.ForeignKey(EquipmentSlot, on_delete=models.CASCADE, blank=True, null=True,
                                       help_text="If not a building")
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True,
                               help_text="If equipment_slot is weapon")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    value = models.IntegerField(default=1)
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
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["gathering", "adventure", "crafting", "land", "weapon"]

    def __str__(self):
        if self.gathering:
            return '{} +{}'.format(self.gathering, self.value)
        elif self.adventure:
            return '{} +{}'.format(self.adventure, self.value)
        elif self.crafting:
            return '{} +{}'.format(self.crafting, self.value)
        elif self.land:
            return '{} +{}'.format(self.land, self.value)
        elif self.weapon:
            return '{} +{}'.format(self.weapon, self.value)


class Training(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)
    difficulty = models.IntegerField(blank=True, null=True)
    recovery = models.IntegerField(blank=True, null=True)
    gold_reward = models.IntegerField(blank=True, null=True)
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    level = models.IntegerField(default=1)
    price = models.IntegerField(blank=True, null=True)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    reputation_guild_value = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
