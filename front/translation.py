from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Daytime)
class DaytimeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Gathering)
class GatheringTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Adventure)
class AdventureTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Crafting)
class CraftingTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Land)
class LandTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Weapon)
class WeaponTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(EquipmentSlot)
class EquipmentSlotTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Reputation)
class ReputationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Guild)
class GuildTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Training)
class TrainingTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(NPC)
class NPCTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Companion)
class CompanionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Talent)
class SpellTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(MaterialType)
class MaterialTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Material)
class MaterialTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ComponentType)
class IngredientTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Component)
class IngredientTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Plant)
class PlantTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(MagicSchool)
class MagicSchoolTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Monster)
class MonsterTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Boss)
class BossTranslationOptions(TranslationOptions):
    fields = ('name',)
