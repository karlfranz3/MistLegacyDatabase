from django.contrib import admin
from front.models import Region, Reputation, Location, Recipe, Book, Training, Weapon, Land, Gathering, Adventure, Crafting, RecipeType, Daytime, NPC
from modeltranslation.admin import TranslationAdmin


@admin.register(Daytime)
class DaytimeAdmin(TranslationAdmin):
    pass


@admin.register(Weapon)
class WeaponAdmin(TranslationAdmin):
    pass


@admin.register(Land)
class LandAdmin(TranslationAdmin):
    pass


@admin.register(Gathering)
class GatheringAdmin(TranslationAdmin):
    pass


@admin.register(Adventure)
class AdventureAdmin(TranslationAdmin):
    pass


@admin.register(Crafting)
class CraftingAdmin(TranslationAdmin):
    pass


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    pass


@admin.register(Reputation)
class ReputationAdmin(TranslationAdmin):
    pass


@admin.register(Location)
class LocationAdmin(TranslationAdmin):
    pass


@admin.register(RecipeType)
class RecipeTypeAdmin(TranslationAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    pass


@admin.register(Book)
class BookAdmin(TranslationAdmin):
    pass


@admin.register(Training)
class TrainingAdmin(TranslationAdmin):
    pass


@admin.register(NPC)
class NPCAdmin(TranslationAdmin):
    pass
