# Testing Enviroment
#
# This file is for all major/minor testing. This eventually be replaced by playground mode 
# (Functional "gameplay-loop" but w/ dev cheats)

define testenv = Location("University Square", adjacent=
                            ["Classroom","Danger Room", "Image Test"], dayCycle=True)

define exampleClothes = {}

define exampleOutfit = Outfit(top="Nothing")

define exampleActor = Actor("Buster", fallback="busted",outfits={'busted','busting'})

# Test label for layeredimage
# TODO: Make a proper sprite test environment
# TODO: Remove this label
label imageTest:

    show test

    "This is the layeredimage system test."

    #Base test
    test bare "I should be bare."
    test "I should even be bare down there!"
    show test -bare
    test none "Not any more though."
    show test -none
    test "I prefer to wear gloves even when naked."
    show test up
    test "If this worked, the test should end now and return you to the menu."

    jump testenv


# Testing label for Actors
label actorTest:
    show danger_room
    # call wardrobe # this is where I would summon a wardrobe system
    ## IF I HAD ONE
    menu:
        "Analyze Buster":
            exampleActor "I am Buster!"
        "Back":
            jump testenv
        # "Main Menu":
        #     $ MainMenu(confirm=False)()
    jump actorTest

# Test label using Location.
label testenv:
    $ renpy.scene()
    $ renpy.show(testenv.getBackground())
    menu:
        "You are in the University Square. What would you like to do?"

        "Chat":
            #call Chat
            pass
        "Wait" if current_time != "Night":
            "You wait around a bit."
            # call Wait
            # call EventCalls
            # call Girls_Location
            pass
        "Systems Testing":
            menu:
                "Image System Test":
                    jump imageTest
                "Actor Testing":
                    jump actorTest
                "Back":
                    jump testenv
        "Go somewhere else":
            $ locationMenu(testenv)
        "Main Menu":
            $ MainMenu(confirm=False)()

    jump testenv