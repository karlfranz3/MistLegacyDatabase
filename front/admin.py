from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from front.models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Daytime)
class DaytimeAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Weapon)
class WeaponAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(EquipmentSlot)
class EquipmentSlotAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Land)
class LandAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Gathering)
class GatheringAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Adventure)
class AdventureAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Crafting)
class CraftingAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Reputation)
class ReputationAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Guild)
class GuildAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Region)
class RegionAdmin(LeafletGeoAdmin):
    exclude = ('name',)
    list_display = ('name_en', 'name_fr', 'land', 'land_difficulty')


@admin.register(Location)
class LocationAdmin(LeafletGeoAdmin):
    exclude = ('name',)
    list_display = ('name_en', 'name_fr', 'region', 'exploration')


@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr', 'reputation', 'guild', 'reputation_guild_value', 'price', 'location')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'reputation', 'guild', 'reputation_guild_value', 'price', 'location')


@admin.register(Training)
class TrainingAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr', 'adventure', 'location', 'difficulty')


@admin.register(NPC)
class NPCAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr', 'location')


@admin.register(Companion)
class CompanionAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr', 'location', 'quest', 'comfort', 'weapon')


@admin.register(Spell)
class SpellAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr', 'reputation', 'guild', 'reputation_guild_value', 'price', 'location', 'npc')


@admin.register(MaterialType)
class MaterialTypeAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Material)
class MaterialAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr', 'material_type', 'level', 'craft_difficulty', 'harvest_difficulty', 'encumbrance')


@admin.register(IngredientType)
class IngredientTypeAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr')


@admin.register(Ingredient)
class IngredientAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr', 'ingredient_type', 'level', 'craft_difficulty', 'encumbrance')


@admin.register(Plant)
class PlantAdmin(TranslationAdmin):
    list_display = ('name_en', 'name_fr', 'level', 'craft_difficulty', 'harvest_difficulty', 'encumbrance')


@admin.register(BlueFlags)
class BlueFlagsAdmin(LeafletGeoAdmin):
    exclude = ('name',)
    list_display = ('name_en', 'name_fr')


@admin.register(BlueFlagsStep)
class BlueFlagsStepAdmin(admin.ModelAdmin):
    list_display = ('flag', 'adventure', 'weapon', 'gathering', 'difficulty',)


@admin.register(BlueFlagsReward)
class BlueFlagsRewardAdmin(admin.ModelAdmin):
    list_display = ('flag', 'material', 'ingredient', 'plant', 'number',)


@admin.register(Elixir)
class ElixirAdmin(LeafletGeoAdmin):
    pass


@admin.register(GatheringPoint)
class GatheringPointAdmin(LeafletGeoAdmin):
    list_display = ('material', 'plant')


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
