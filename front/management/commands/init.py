from django.core.management.base import BaseCommand, CommandError
from front.models import Land, Weapon, Gathering, Adventure, Crafting, Reputation, RecipeType, Daytime


class Command(BaseCommand):
    help = 'Initialize data'

    def handle(self, *args, **options):
        #Land(name_en="Forest", name_fr="Forêt").save()
        #Land(name_en="Mists", name_fr="Brumes").save()
        #Land(name_en="Mountain", name_fr="Montagne").save()
        #Land(name_en="Swamp", name_fr="Marais").save()
        #Land(name_en="Underground", name_fr="Souterrain").save()

        #Weapon(name_en="Axe", name_fr="Hache").save()
        #Weapon(name_en="Dagger", name_fr="Dague").save()
        #Weapon(name_en="Mace", name_fr="Masse").save()
        #Weapon(name_en="Spear", name_fr="Lance").save()
        #Weapon(name_en="Sword", name_fr="Epée").save()

        #Gathering(name_en="Botany", name_fr="Botanique").save()
        #Gathering(name_en="Mining", name_fr="Minage").save()
        #Gathering(name_en="Hunting", name_fr="Chasse").save()
        #Gathering(name_en="Lumberjacking", name_fr="Coupe").save()

        #Adventure(name_en="Academic", name_fr="Académie").save()
        #Adventure(name_en="Athletics", name_fr="Athlétisme").save()
        #Adventure(name_en="Exploration", name_fr="Exploration").save()
        #Adventure(name_en="Perception", name_fr="Perception").save()
        #Adventure(name_en="Persuasion", name_fr="Persuasion").save()
        #Adventure(name_en="Strategy", name_fr="Stratégie").save()
        #Adventure(name_en="Subterfuge", name_fr="Larçin").save()

        #Crafting(name_en="Forge", name_fr="Forge").save()
        #Crafting(name_en="Sewing", name_fr="Couture").save()
        #Crafting(name_en="Stoneworking", name_fr="Taille").save()
        #Crafting(name_en="Woodworking", name_fr="Ebenisterie").save()
        #Crafting(name_en="Tanning", name_fr="Tannage").save()

        #Reputation(name_en="Gantras", name_fr="Gantras").save()
        #Reputation(name_en="Goodneigbhor", name_fr="Bonvoisin").save()
        #Reputation(name_en="Kortombe", name_fr="Kortombe").save()
        #Reputation(name_en="Larcen", name_fr="Larcen").save()
        #Reputation(name_en="Thorval", name_fr="Thorval").save()

        #RecipeType(name_en="Weapon", name_fr="Arme").save()
        #RecipeType(name_en="Building", name_fr="Batiments").save()
        #RecipeType(name_en="Serum", name_fr="Serum").save()
        #RecipeType(name_en="Jewellery", name_fr="Bijoux").save()

        #Daytime(name_en="Night", name_fr="Nuit").save()
        #Daytime(name_en="Day", name_fr="Jour").save()
        #Daytime(name_en="Always", name_fr="Permanent").save()

        pass