# Base Actor Class (and examples?)
#
# Actors will be anything (usually a character/person) the player can interact with

init -2 python:
    import re

    # Intent: TODO: Write Inventory intent
    #   Intent
    #   Here
    # Occurrence: Instanced by default for all Actor objects
    class Inventory(renpy.store.object):
        """ """
        def __init__(self):
            pass
            
    # Intent:
    #   Wardrobe contains 
    #       - all clothing pieces for an Actor
    #       - all pre-defined outfits for an Actor
    #   Also contains 
    # Occurrence: Instanced by default for all Actor objects
    class Wardrobe(renpy.store.object):
        def __init__(self, clothing, outfits, **kwargs):
            """
            Wardrobe contains the Outfits for a character 
            and handles changing the active outfit

                :param clothing: all possible clothing pieces for a character
                :type clothing: Dictionary (string, Dictionary(string, value))
                    ex  {'skirt': {'exposure':0}, 'bikini': {'exposure':9}}
                
                :param outfits: Collection of possible outfits for Actor
                :type outfits: Set (TODO: change data structure used?)
            """
            self.clothing = clothing
            self.outfits = outfits

            self.fallback = outfits[0] #fallback/default outfit
            self.active = kwargs.pop('active',self.fallback) 
            #default to using fallback outfit via a string
            #TODO: grab an Outfit object from Outfits based on a string passed to 'active', not a string

    # Intent:
    #   Single state of a characters current clothing, data store
    #   Collection of clothing pieces
    # Occurrence: Instanced by default for all Actor objects
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
            # self.acc = ["","",""] # top accessories

            self.layers = [self.panties, self.bra, self.legs, 
                            self.inner, self.bottom, self.dress, self.top, self.outer]

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

    # Intent: TODO: Write Schedule intent
    #   Intent
    #   Here
    # Occurrence: Instanced by default for all Actor objects
    class Schedule(renpy.store.object):
            """ """
            def __init__(self):
                pass

    # Intent: TODO: Write Statistics intent
    #   Intent
    #   Here
    # Occurrence: Instanced by default for all Actor objects
    class Statistics(renpy.store.object):
            """ """
            def __init__(self):
                pass
    
    class Actor(ADVCharacter):
        def __init__(self, name, kind=None, **kwargs):
            """
            Actors are all non-player characters whom the player might interact with.
                :param name: character's "writer" name, 
                :            also corresponds to ADVCharacter self.name
                :type name: string
                :param kind: is this character based off of another Character, 
                :            also corresponds to ADVCharacter self.name
                :type kind : renpy.store.ADVCharacter
            TODO: Layout definition of Actor a little more precisely?
            """

            '''   
            NAME
                Seperate var from self.name, allows names like: "Player's Conscience".
                Keeps problems related to our Actor's name have special characters
                minimized if not outright prevented.
            '''   
            self.actName = name
            self.trimmed = re.sub('[ ]','_',re.sub("[']",'',self.actName)).lower()
        
            '''
            BASIC-ACTOR
            '''
            self.isBasic = kwargs.pop('isBasic',false)
            if self.isBasic:
                self.hasInventory = True
                self.hasWardrobe = True
                self.hasSchedule = True
                self.hasLocation = True
                self.hasStats = True

            '''
            INVENTORY
                * Intent for an Inventory here.
                By default all Actor objects have an inventory.
                But, by specifying "hasInventory=False" in kwargs,
                an Actor object will not have an inventory object.
            TODO: Write an intent for what the inventory does above *
            '''
            if not self.isBasic:
                self.hasInventory = kwargs.pop("hasInventory",True)
                if self.hasInventory:
                    self.inventory = Inventory()

            '''
            WARDROBE AND OUTFITS
                Construct Actor's Wardrobe
                Contains a default fallback outfit and a collection of possible outfits,
                alongside all pieces of clothing an Actor can wear.
                By default all Actor objects have an Wardrobe.
                But, by specifying "hasWardrobe=False" in kwargs,
                an Actor object will not have an Wardrobe object.
            TODO: PASS NOT STRING BUT ACTUAL OUTFIT OBJECT OR SOMETHING
            '''
            if not self.isBasic:
                self.hasWardrobe = kwargs.pop("hasWardrobe",True)
                if self.hasWardrobe:
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
                        kwargs.pop('outfits',{'default','nude'}))
                        
                    # Set Actor's Active Outfit, if the actor has a Wardrobe
                    self.outfit = self.wardrobe.active
            
            '''
            SCHEDULE
                Construct Actor's Schedule
                * Intent for a Schedule here.
                ! Definition of Schedule by it's contents. 
            TODO: Write an intent for what the schedule does above *
            TODO: Write a definition for what the schedule contains above !
            '''
            if not self.isBasic:
                self.hasSchedule = kwargs.pop("hasSchedule",True)
                if self.hasSchedule:
                    self.schedule = Schedule()

            '''
            LOCATION
                *
                !
            TODO: Write an intent for what the location does above *
            TODO: Write a definition for what the location contains above !
            '''
            if not self.isBasic:
                self.hasLocation = kwargs.pop("hasLocation",True)
                if self.hasLocation:
                    self.location = kwargs.pop('location',unsassigned)
                #TODO: Location history functionality?
            

            '''
            STATS
                *
                !
            TODO: Write an intent for what the Stats object does above *
            TODO: Write a definition for what the Stats object contains above !
            '''
            if not self.isBasic:
                self.hasStats = kwargs.pop("hasStats",True)
                if self.hasStats:
                    self.statistics = Statistics() 

            '''
            ADVCharacter
                Actor has a class is intended to be a writer friendly expansion upon
                the actor object when using the "Character()" function.
                See renpy/renpy/character.py:662 to see what ADVCharacter contains.
            # TODO: Add param(s) for character base image (ADVCharacter ) Done?
            #       (This will be overlayed with the Outfit as a LayeredImage)
            # TODO: Add params (etc) which determine prefixes and suffixes
            '''

            super(Actor, self).__init__(self.actName, kind, **kwargs)

            # self.color = '#000000' if 'color' not in kwargs
