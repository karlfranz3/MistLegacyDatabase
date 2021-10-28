from django.db import models
from django.urls import reverse
from djgeojson.fields import PointField, PolygonField
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField
from .toolbox import centroid


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

    def get_absolute_url(self):
        return reverse('guild', args=[str(self.id)])


class Region(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)
    land_difficulty = models.IntegerField(blank=True, null=True)
    geom = PolygonField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    @property
    def map_poi(self):
        tooltip = "<p>{}</br>{} {} {}".format(
            self.name, self.land, _("Difficulty"), self.land_difficulty)
        tooltip = tooltip + '</p>'
        return tooltip

    @property
    def coordinates(self):
        if self.geom:
            return str(centroid(self.geom)['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None


class Location(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    exploration = models.IntegerField(blank=True, null=True)
    quest = models.BooleanField(blank=True, null=True, default=False)
    geom = PointField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="location_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    @property
    def map_poi(self):
        tooltip = "<p>{}</br>{}: {}</br>{}: {}".format(
            self.name,
            _("Exploration"), self.exploration,
            _("Quest"), self.quest)
        if self.training_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Training"))
            for training in self.training_set.all():
                tooltip = tooltip + '{} ({})</br>'.format(training.adventure, training.difficulty)
        if self.book_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Book"))
            for book in self.book_set.all():
                tooltip = tooltip + '{} ({}/{})</br>'.format(book.__str__(), book.reputation, book.reputation_guild_value)
        if self.recipe_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Recipe"))
            for recipe in self.recipe_set.all():
                tooltip = tooltip + '{} ({}/{})</br>'.format(recipe.name, recipe.reputation, recipe.reputation_guild_value)
        if self.spell_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Spell/Skill"))
            for spell in self.spell_set.all():
                rep = spell.reputation or spell.guild
                tooltip = tooltip + '{} ({}/{})</br>'.format(spell.name, rep, spell.reputation_guild_value)
        tooltip = tooltip + '</p>'
        return tooltip

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None

    @property
    def icon_width(self):
        if self.icon:
            return self.icon.width
        else:
            return None

    @property
    def icon_height(self):
        if self.icon:
            return self.icon.height
        else:
            return None

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None


class Companion(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    lvl = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    quest = models.BooleanField(blank=True, null=True, default=False)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True)
    weapon_lvl = models.IntegerField(blank=True, null=True)
    comfort = models.IntegerField(blank=True, null=True)
    convenience = models.IntegerField(blank=True, null=True)
    armor = models.IntegerField(blank=True, null=True)
    life = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class CompanionSkill(models.Model):
    companion = models.ForeignKey(Companion, null=False, blank=False, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, null=True, blank=True, on_delete=models.CASCADE)
    gathering = models.ForeignKey(Gathering, null=True, blank=True, on_delete=models.CASCADE, default=None)
    land = models.ForeignKey(Land, null=True, blank=True, on_delete=models.CASCADE, default=None)
    crafting = models.ForeignKey(Crafting, null=True, blank=True, on_delete=models.CASCADE, default=None)
    bonus = models.IntegerField(null=False, blank=False)


class NPC(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class Recipe(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    reputation_guild_value = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)
    building = models.BooleanField(default=False)
    equipment_slot = models.ForeignKey(EquipmentSlot, on_delete=models.CASCADE, blank=True, null=True,
                                       help_text="If not a building")
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True,
                               help_text="If equipment_slot is weapon")
    blueflag = models.ForeignKey('BlueFlags', on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    def get_absolute_url(self):
        return reverse('recipe_card', args=[str(self.id)])

    def get_reputation(self):
        if self.reputation:
            return '{} {}'.format(self.reputation, self.reputation_guild_value)
        elif self.guild:
            return '{} {}'.format(self.guild, self.reputation_guild_value)

    def get_location(self):
        if self.location:
            return self.location
        elif self.blueflag:
            return self.blueflag
        else:
            return None


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
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    reputation_guild_value = models.IntegerField(blank=True, null=True, default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)
    blueflag = models.ForeignKey('BlueFlags', on_delete=models.CASCADE, blank=True, null=True, default=None)

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

    def get_absolute_url(self):
        return reverse('book_card', args=[str(self.id)])

    def get_reputation(self):
        if self.reputation:
            return '{} {}'.format(self.reputation, self.reputation_guild_value)
        elif self.guild:
            return '{} {}'.format(self.guild, self.reputation_guild_value)

    def get_location(self):
        if self.location:
            return self.location
        elif self.blueflag:
            return self.blueflag
        else:
            return None


class Training(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    difficulty = models.IntegerField(blank=True, null=True)
    daytime = models.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True, default=3)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class Spell(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    level = models.IntegerField(default=1)
    price = models.IntegerField(blank=True, null=True)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    reputation_guild_value = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    def get_absolute_url(self):
        return reverse('spell_card', args=[str(self.id)])

    def get_reputation(self):
        if self.reputation:
            return '{} {}'.format(self.reputation, self.reputation_guild_value)
        elif self.guild:
            return '{} {}'.format(self.guild, self.reputation_guild_value)


class MaterialType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class IngredientType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Material(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE, blank=False, null=False)
    level = models.IntegerField(blank=False, null=False)
    density = models.IntegerField(blank=True, null=True)
    purity = models.IntegerField(blank=True, null=True)
    flexibility = models.IntegerField(blank=True, null=True)
    rigidity = models.IntegerField(blank=True, null=True)
    hardness = models.IntegerField(blank=True, null=True)
    radiance = models.IntegerField(blank=True, null=True)
    absorbency = models.IntegerField(blank=True, null=True)
    lightness = models.IntegerField(blank=True, null=True)
    durability = models.IntegerField(blank=False, null=False)
    craft_difficulty = models.IntegerField(blank=True, null=True)
    harvest_difficulty = models.IntegerField(blank=True, null=True)
    cooldown = models.FloatField(blank=True, null=True)
    encumbrance = models.IntegerField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="material_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None

    @property
    def icon_width(self):
        if self.icon:
            return self.icon.width
        else:
            return None

    @property
    def icon_height(self):
        if self.icon:
            return self.icon.height
        else:
            return None

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class Ingredient(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    ingredient_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, blank=False, null=False)
    level = models.IntegerField(blank=False, null=False)
    lithram = models.IntegerField(blank=True, null=True)
    magnam = models.IntegerField(blank=True, null=True)
    radiam = models.IntegerField(blank=True, null=True)
    hydram = models.IntegerField(blank=True, null=True)
    pyram = models.IntegerField(blank=True, null=True)
    stratam = models.IntegerField(blank=True, null=True)
    frimam = models.IntegerField(blank=True, null=True, default=None)
    lectram = models.IntegerField(blank=True, null=True, default=None)
    psycham = models.IntegerField(blank=True, null=True, default=None)
    elioam = models.IntegerField(blank=True, null=True, default=None)
    craft_difficulty = models.IntegerField(blank=True, null=True)
    encumbrance = models.IntegerField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="ingredient_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None

    @property
    def icon_width(self):
        if self.icon:
            return self.icon.width
        else:
            return None

    @property
    def icon_height(self):
        if self.icon:
            return self.icon.height
        else:
            return None

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class Plant(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    level = models.IntegerField(blank=False, null=False)
    activator = models.IntegerField(blank=True, null=True)
    binder = models.IntegerField(blank=True, null=True)
    energizer = models.IntegerField(blank=True, null=True)
    deteriorator = models.IntegerField(blank=True, null=True)
    focuser = models.IntegerField(blank=True, null=True)
    fortifier = models.IntegerField(blank=True, null=True)
    putrefier = models.IntegerField(blank=True, null=True)
    stimulator = models.IntegerField(blank=True, null=True)
    tranquilizer = models.IntegerField(blank=True, null=True)
    toner = models.IntegerField(blank=True, null=True)
    craft_difficulty = models.IntegerField(blank=True, null=True)
    harvest_difficulty = models.IntegerField(blank=True, null=True)
    cooldown = models.FloatField(blank=True, null=True)
    encumbrance = models.IntegerField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="plant_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None

    @property
    def icon_width(self):
        if self.icon:
            return self.icon.width
        else:
            return None

    @property
    def icon_height(self):
        if self.icon:
            return self.icon.height
        else:
            return None

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class BlueFlags(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    geom = PointField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="blueflag_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    @property
    def map_poi(self):
        tooltip = "<p>{}</br>".format(self.name)
        if self.blueflagsstep_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Step"))
            for step in self.blueflagsstep_set.all():
                if step.adventure:
                    tooltip = tooltip + '{}% {} ({})</br>'.format(step.percent, step.adventure, step.difficulty)
                elif step.weapon:
                    tooltip = tooltip + '{}% {} ({})</br>'.format(step.percent, step.weapon, step.difficulty)
                elif step.gathering:
                    tooltip = tooltip + '{}% {} ({})</br>'.format(step.percent, step.gathering, step.difficulty)
        tooltip = tooltip + '</br>{}(s):</br>'.format(_("Reward"))
        if self.blueflagsreward_set.all().exists():
            for reward in self.blueflagsreward_set.all():
                tooltip = tooltip + '{} ({})</br>'.format(reward.__str__(), reward.number)
        if self.book_set.all().exists():
            for book in self.book_set.all():
                tooltip = tooltip + '{} {}</br>'.format(_("Book"), book.__str__())
        if self.recipe_set.all().exists():
            for recipe in self.recipe_set.all():
                tooltip = tooltip + '{} {}</br>'.format(_("Recipe"), recipe.__str__())
        tooltip = tooltip + '</p>'
        return tooltip

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None


class BlueFlagsStep(models.Model):
    flag = models.ForeignKey(BlueFlags, null=False, blank=False, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, null=True, blank=True, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, null=True, blank=True, on_delete=models.CASCADE, default=None)
    gathering = models.ForeignKey(Gathering, null=True, blank=True, on_delete=models.CASCADE, default=None)
    difficulty = models.IntegerField(null=False, blank=False)
    percent = models.IntegerField(default=0, null=False, blank=False)


class BlueFlagsReward(models.Model):
    flag = models.ForeignKey(BlueFlags, null=False, blank=False, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, null=True, blank=True, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(blank=False, null=False)

    def __str__(self):
        if self.material:
            return self.material.name
        elif self.ingredient:
            return self.ingredient.name
        elif self.plant:
            return self.plant.name
        else:
            return _('-- no translation yet --')


class Elixir(models.Model):
    geom = PointField(blank=True, null=True)

    def __str__(self):
        return _('Vigor')

    @property
    def map_poi(self):
        return self.__str__()

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None


class GatheringPoint(models.Model):
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    geom = PointField(blank=True, null=True)

    def __str__(self):
        if self.material:
            return self.material.name
        elif self.plant:
            return self.plant.name
        else:
            return _('-- no translation yet --')

    @property
    def map_poi(self):
        if self.material:
            return '{} x {}'.format(self.material.name, self.number)
        if self.plant:
            return '{} x {}'.format(self.plant.name, self.number)

    @property
    def icon_url(self):
        if self.material and self.material.icon:
            return self.material.icon.url
        elif self.plant and self.plant.icon:
            return self.plant.icon.url
        else:
            return None

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None


class Guide(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    link = models.CharField(max_length=256, blank=True, null=True)
    author = models.CharField(max_length=64, blank=True, null=True)
    contact = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        ordering = ["name"]
