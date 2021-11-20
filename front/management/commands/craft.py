import datetime

from django.core.management.base import BaseCommand
from django.core.cache import cache
from front.models import Material, Plant, Component

woods = Material.objects.filter(material_type__name="Woods")
metals = Material.objects.filter(material_type__name="Metals")
fibers = Material.objects.filter(material_type__name="Fibers")
leathers = Material.objects.filter(material_type__name="Leathers")
stones = Material.objects.filter(material_type__name="Stones")
saps = Component.objects.filter(component_type__name="Sap")
gems = Component.objects.filter(component_type__name="Gem")
pollens = Component.objects.filter(component_type__name="Pollen")
powders = Component.objects.filter(component_type__name="Powder")


class Command(BaseCommand):
    help = "Generation du cache des crafts"

    def handle(self, *args, **options):
        datetime_debut = datetime.datetime.now()

        print('v001')
        v001()
        print('v002')
        v002()
        print('v003')
        v003()
        print('v004')
        v004()
        print('index')
        ano_index()

        datetime_fin = datetime.datetime.now()
        print("Durée du batch : {}".format(datetime_fin - datetime_debut))


def ano_index():
    index = {}
    for ano_nom in ['V001', 'V002', 'V003']:
        ano = cache.get('CRAFT_{}'.format(ano_nom))
        index[ano_nom] = {'nom': ano['nom']}
    cache.set('CRAFT_INDEX', index, timeout=None)


def v001():
    base = 10
    code = 'V001'
    nom = 'Trolley'
    ano = {'code': code, 'nom': nom, 'order': 6,
           'th': ['Wooden frame', 'Metal axle', 'Fixing cord', 'Woodworking', 'Forge', 'Sewing', 'Forest', 'Mountain', 'Swamp', 'Underground'],
           'elems': {}
           }

    for wood in woods:
        for metal in metals:
            for fiber in fibers:
                forest = 15 + (0.2625 * metal.flexibility) + (0.2625 * wood.flexibility) + (0.225 * fiber.flexibility) + (0.0875 * metal.density) + (0.0875 * wood.density) + (0.075 * fiber.density)
                mountain = 15 + (0.2625 * metal.hardness) + (0.2625 * wood.hardness) + (0.225 * fiber.hardness) + (0.0875 * metal.rigidity) + (0.0875 * wood.rigidity) + (0.075 * fiber.rigidity)
                swamp = 15 + (0.2625 * metal.purity) + (0.2625 * wood.purity) + (0.225 * fiber.purity) + (0.0875 * metal.hardness) + (0.0875 * wood.hardness) + (0.075 * fiber.hardness)
                underground = 5 + (0.2625 * metal.absorbency) + (0.2625 * wood.absorbency) + (0.225 * fiber.absorbency) + (0.0875 * metal.flexibility) + (0.0875 * wood.flexibility) + (0.075 * fiber.flexibility)
                ano['elems']['{}/{}/{}'.format(wood, metal, fiber)] = \
                    {'Wooden frame': wood, 'Metal axle': metal, 'Fixing cord': fiber,
                     'Woodworking': wood.craft_difficulty+base, 'Forge': metal.craft_difficulty+base, 'Sewing': fiber.craft_difficulty+base,
                     'Forest': round(forest), 'Mountain': round(mountain), 'Swamp': round(swamp), 'Underground': round(underground)}

    cache.set('CRAFT_{}'.format(code), ano, timeout=None)


def v002():
    base = 15
    code = 'V002'
    nom = "Apprentice's tablet"
    ano = {'code': code, 'nom': nom, 'order': 7,
           'th': ['Polarizing stone', 'Elemental binder', 'Focusing Gem', 'Telluric essence', 'Stoneworking', 'Herbalism', 'Alchemy', 'Fire', 'Water', 'Wind'],
           'elems': {}
           }

    for stone in stones:
        for sap in saps:
            for gem in gems:
                for powder in powders:
                    fire = 10 + (0.2 * stone.radiance) + 0.2 * (sap.pyram + gem.pyram + powder.pyram)
                    water = 10 + (0.2 * stone.purity) + 0.2 * (sap.hydram + gem.hydram + powder.hydram)
                    wind = 10 + (0.2 * stone.lightness) + 0.2 * (sap.stratam + gem.stratam + powder.stratam)
                    ano['elems']['{}/{}/{}'.format(stone, sap, gem, powder)] = \
                        {'Polarizing stone': stone, 'Elemental binder': sap, 'Focusing Gem': gem, 'Telluric essence': powder,
                         'Stoneworking': max(stone.craft_difficulty,gem.craft_difficulty)+base, 'Herbalism': sap.craft_difficulty+base, 'Alchemy': powder.craft_difficulty+base,
                         'Fire': round(fire), 'Water': round(water), 'Wind': round(wind)}

    cache.set('CRAFT_{}'.format(code), ano, timeout=None)


def v003():
    base = 15
    code = 'V003'
    nom = "Apprentice's scepter"
    ano = {'code': code, 'nom': nom, 'order': 8,
           'th': ['Stick of life', 'Focusing Gem', 'Telluric essence', 'Evocation aroma', 'Woodworking', 'Stoneworking', 'Alchemy', "Herbalism", 'Light'],
           'elems': {}
           }

    for wood in woods:
        for gem in gems:
            for powder in powders:
                for pollen in pollens:
                    light = 10 + (0.2 * wood.rigidity) + 0.2 * (gem.elioam + powder.elioam + pollen.elioam)
                    ano['elems']['{}/{}/{}'.format(wood, gem, powder, pollen)] = \
                        {'Stick of life': wood, 'Focusing Gem': gem, 'Telluric essence': powder, 'Evocation aroma': pollen,
                         'Woodworking': wood.craft_difficulty+base, 'Stoneworking': gem.craft_difficulty+base, 'Alchemy': powder.craft_difficulty+base, 'Herbalism': pollen.craft_difficulty+base,
                         'Light': round(light)}

    cache.set('CRAFT_{}'.format(code), ano, timeout=None)


def v004():
    base = 10
    code = 'V004'
    nom = "Apprentice's grimoire"
    ano = {'code': code, 'nom': nom, 'order': 7,
           'th': ['Reinforced Coverage', 'Elemental binder', 'Focusing Gem', 'Evocation aroma', 'Tanning', 'Herbalism', 'Stoneworking', 'Fire', 'Light', 'Water', 'Wind'],
           'elems': {}
           }

    for leather in leathers:
        for sap in saps:
            for gem in gems:
                for pollen in pollens:
                    fire = 10 + (0.15 * leather.radiance) + 0.15 * (sap.pyram + gem.pyram + pollen.pyram)
                    water = 10 + (0.15 * leather.purity) + 0.15 * (sap.hydram + gem.hydram + pollen.hydram)
                    wind = 10 + (0.15 * leather.lightness) + 0.15 * (sap.stratam + gem.stratam + pollen.stratam)
                    light = 10 + (0.15 * leather.rigidity) + 0.15 * (sap.elioam + gem.elioam + pollen.elioam)
                    ano['elems']['{}/{}/{}'.format(leather, sap, gem, pollen)] = \
                        {'Reinforced Coverage': leather, 'Elemental binder': sap, 'Focusing Gem': gem, 'Evocation aroma': pollen,
                         'Tanning': leather.craft_difficulty+base, 'Herbalism': max(sap.craft_difficulty+base, pollen.craft_difficulty), 'Stoneworking': gem.craft_difficulty+base,
                         'Fire': round(fire), 'Light': round(light), 'Water': round(water), 'Wind': round(wind)}

    cache.set('CRAFT_{}'.format(code), ano, timeout=None)
