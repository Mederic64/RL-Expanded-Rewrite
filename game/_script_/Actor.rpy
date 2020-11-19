# Base Actor Class (and examples?)
#
# Actors will be anything (usually a character/person) the player can interact with

init -2 python:
    import re

    # Intent: TODO: Write Inventory intent
    #   Intent
    #   Here
    # Occurrence: Inventory instanced for all Actor objects
    class Inventory(renpy.store.object):
        """ """
        def __init__(self):
            pass
            
    # Intent:
    #   Wardrobe contains 
    #       - all clothing pieces for an Actor
    #       - all pre-defined outfits for an Actor
    #   Also contains 
    # Occurrence: Instanced for all Actor objects
    class Wardrobe(renpy.store.object):
        def __init__(self, clothing, fallback, outfits):
            """
            Wardrobe contains the Outfits for a character 
            and handles changing the active outfit

                :param clothing: all possible clothing pieces for a character
                :type clothing: Dictionary (string, Dictionary(string, value))
                        ex  {'skirt': {'exposure':0}, 'bikini': {'exposure':9}}

                :param fallback: fallback/default outfit for a character
                :type fallback: Outfit(renpy.store.object)
                
                :param outfits: Collection of possible outfits for Actor
                :type outfits: Set (TODO: change data structure used?)
            """
            self.clothing = clothing

            self.active = fallback
            self.fallback = fallback
            self.outfits = outfits

    # Intent:
    #   Single state of a characters current clothing, data store
    #   Collection of clothing pieces
    # Occurrence: Instanced for all Actor objects
    class Outfit(renpy.store.object):
        def __init__(self, **kwargs):
            # outfit statistics
            self._nude = 0  # no clothes at all (does not include acces.)
            self._undressed = 0 # aka functionally nude (includes acces.)
            self._upSkirt = 0
            self._upTop = 0
            self._pantiesDown = 0

            # outfit other stats
            self._exposure = 0
            self._shame = 0 # move this over to actor?
            
            # outfit layers
            self.panties = kwargs.pop('panties',"N/A") # panties
            self.bra = kwargs.pop('bra',"N/A") # bra
            self.legs = kwargs.pop('leg',"N/A") # below bottoms
            self.inner = kwargs.pop('inner',"N/A") # inner top
            self.bottom = kwargs.pop('bottom',"N/A") # legs
            self.dress = kwargs.pop('dress',"N/A") # "full-body" clothing
            self.top = kwargs.pop('top',"N/A") # upper body
            self.outer = kwargs.pop('outer',"N/A") # upper body (ex: jackets, coats)

            self.layers = [self.panties, self.bra, self.legs, 
                            self.inner, self.bottom, self.dress, self.top, self.outer]

        """
            layers by priority:
                0 panties
                1 bra
                2 legs (hose)
                3 inner (inner shirt/top layer)
                4 bottom
                5 dress
                6 top
                7 outer
        """
        def getLayers(self):
            strOut = ""
            for i, v in enumerate(self.layers):
                strOut += "Layer {}: {}\n".format(i,v)
                # renpy.log(strOut)
            return strOut

        def getExposure(self):
            try:
                return self._exposure
            except AttributeError:
                renpy.log("ERROR, ATTRIBUTE %s DOES NOT EXIST" % _exposure)

            # functions
            #   check taboo (ex: response from actor)
            #   check exposure
            #   check traits
            #   checks but not the fun/money kind
            # come up with more checks if needed
            

            # self.acc = ["","",""] # top accessories
    
    # Intent: TODO: Write Schedule intent
    #   Intent
    #   Here
    # Occurrence: Instanced for all Actor objects
    class Schedule(renpy.store.object):
            """ """
            def __init__(self):
                pass
    
    """
    Actor INTENT:
        (data storage) RELATIONSHIPS (helper functions)
        ADVCharacter extended functionality
        INVENTORY (object)
        WARDROBE (object)
        SCHEDULE (object)
        SEX
        STATS (dynamic)
            parsed variables
            relationships
            ex: Actor.statA (after creation)
        LOCATION
            current, past, going, home
        ACTIONS (MAYBE: integrate action history w/ dialog history?)
    """
    class Actor(ADVCharacter):
        def __init__(self, name, kind=None, **kwargs):
            """
            Actors are all non-player characters whom the player might interact with.
                TODO: Layout definition of Actor a little more precisely?

                :param name: character's "writer" name, 
                :            also corresponds to ADVCharacter self.name
                :type name: string
                :param kind: is this character based off of another Character, 
                :            also corresponds to ADVCharacter self.name
                :type kind : renpy.store.ADVCharacter
            """                   

            ### MISC
            
            # Actor's Name
            # Seperate from self.name so we can have thing's like "Player's Conscience",
            # thus keeping problems related to our Actor's name have special characters-
            # minimized if not outright prevented.
            self.actName = name

            ### INVENTORY

            # Construct Actor's Inventory
            # TODO: Scope out how inventory is used for NPCs (because atm,
            #       it seems like having a player-like inventory is pretty impractical)
            self.inventory = Inventory()

            ### CLOTHING AND WARDROBE

            # Construct Actor's Wardrobe
            # Contains a default fallback outfit and a Set of possible outfits,
            # alongside all pieces of clothing an Actor can wear.
            # TODO: PASS NOT STRING BUT ACTUAL OUTFIT OBJECT OR SOMETHING
            self.wardrobe = Wardrobe(
                kwargs.pop('clothing',{
                    'defaultPanties':{'exposure':0},
                    'defaultBra':{'exposure':0},
                    'defaultLegs':{'exposure':0},
                    'defaultInner':{'exposure':0},
                    'defaultBottom':{'exposure':0},
                    'defaultDress':{'exposure':0},
                    'defaultTop':{'exposure':0},
                    'defaultOuter':{'exposure':0}}),
                kwargs.pop('fallback',"default"),
                kwargs.pop('outfits',{'default','nude'}))
            # Set Actor's Active Outfit
            self.outfit = self.wardrobe.active

            ### SCHEDULE

            # Construct Actor's Schedule
            # TODO: Schedule description here
            self.schedule = Schedule()

            ### ADVCharacter(object)

            # TODO: Add param(s) for character base image (ADVCharacter )
            #       (This will be overlayed with the Outfit as a LayeredImage)
            # TODO: Add params (etc) which determine prefixes and suffixes

            super(Actor, self).__init__(name, kind, **kwargs)

            if 'color' not in kwargs:
                self.color = '#000000'

            # Actor's Name
            # TODO: Get a better regex to replace the copied from location below
            # self.name = re.sub('[ ]','_',re.sub("[']",'',name)).lower()
