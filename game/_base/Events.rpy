
image study_day = "StudyDay.jpg"

# TODO: LONG TERM, ALL WRITING IN PLAINTEXT CODE (LIKE BELOW)
# SHOULD EVENTUALLY BE REPLACED W/ A STRING REFERENCE CALLING BACK TO A JSON FILE
# /FUNCTIONALITY TO DETERMINE WHICH STRING FROM WHICH FILE IS CALLED WILL BE DETERMINED 
# BASED ON PLAYERS PREFERRED LANGUAGE, AKA THIS IS FOR LOCALIZATION!

# TODO: Player Character as a class which is used when defining the player character

# TODO: All "#!" copied code or code that needs to be replaced/replicated. 
# DO NOT UNCOMMENT THESE OR USE THEM IN PRODUCTION

# ORIGINAL CHARACTER DEFINITION BLOCK, ONLY USE THE COLORS!

#! define ch_r = Character('[RogueX.Name]', color="#85bb65", image = "arrow", show_two_window=True)
#! define ch_p = Character('[Player.Name]', color="#87CEEB", show_two_window=True)
#! define ch_x = Character('Professor X', color="#a09400", image = "arrow", show_two_window=True)

# Character Block
define p = Character("Zero",
                     who_color="#000000")
define x = Character("Professor X",
                     who_color="#a09400")
define r = Character("Rogue",
                     who_color="#85bb65")

$ PlayerSkinTone = "#028800"

label intro:
    $ renpy.scene()
    show study_day

    # TrainDoc:
    # All caps are left-over from when I was manually transcribing from 0.991h, sorry.

    "YOU'VE ARRIVED IN EARLY EVENING AT THE XAVIER INSTITUE, WHERE YOU'VE BEEN PROMISED A NEW HOME."

    "THINGS HAVE BEEN TOUGHT FOR MUTANTS IN THE YEARS SINCE APOCALYPSE'S FALL, BUT THIS SOUNDS LIKE IT MIGHT BE A GOOD DEAL."

    # "SELECT CHARACTER NAME HERE"

    $ p.name = renpy.input("What is your name?", default="Zero", length = 10)

    "[p.name]"

    # if in developer mode, test player text color
    if config.developer:
        $ renpy.say(p, "text")

    menu:
        "What is your skin color?"
        "Self-Select":
            # TO BE REPLACED BY PALLETE FUNCTIONALITY
            $ PlayerSkinTone = "#028800"
        "Green":
            $ PlayerSkinTone = "#028800"
        "Black":
            $ PlayerSkinTone = "#7a4e0a"
        "Brown":
            $ PlayerSkinTone ="#ad7114"
        "White":
            $ PlayerSkinTone = "#000cff"

    # if config.developer:
    #     $ renpy.say(p, "text")
    
    #! show Professor at SpriteLoc(StageLeft)
    #! with dissolve

    x "WELCOME TO THE XAVIER INSTITUTE FOR HIGHER LEARNING. THIS IS A HOME FOR ALL MUTANTS TO LEARN AND GROW."
    x "My name is Charles Xavier, and I have dedicated my life to helping other mutants such as yourself."
    x "I know that you've had a difficult time, but you will be safe here."
    x "You'll have classes in the day to teach you the skills you'll need, and training in the danger room for self defense."
    x "Since you're on your own, we'll provide a small stipend for your day-to-day needs."
    x "Did you have any questions for me young man?"

    p "Why did you even bring me here, I don't have any \"super powers.\""

    x "Nonsense, my boy. You have an incredibly useful ability..."
    x "the power to negate other powers, even including my own."
    #! $ RogueX.Loc = bg_current
    #! $ RogueX.FaceChange("surprised")
    #! $ RogueX.SpriteLoc = StageFarRight
    #! show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    #! with easeinright
    r "What's that Prof? This new kid can negate mutant powers?"
    #! $ RogueX.Mouth = "normal"
    #! $ RogueX.SpriteLoc = StageRight
    #! show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) with ease
    r "Maybe even my own?"
    x "That is correct, [r.name], though currently, his powers are weak and uncontrolled."
    x "One day, however, he may even be able to help you turn your powers off permanently."
    r "! ..."
    #! $ RogueX.FaceChange("smile")

    # TrainDoc: imo the line below should read "Rogue, since you're here..."
    x "Since you're here, why don't you show our new guest around the mansion?"
    x "This young lady is named [r.name], one of our veteran students."
    # TrainDoc: holy shit waiting all the way until you leave to introduce someone,classy professor...
    x "And [r.name], this young man goes by the name \"[p.name]\"."

    #! hide Professor
    #! with easeoutright

    #! $ RogueX.SpriteLoc = StageCenter
    #! show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
    #! with ease
    #! $ ActiveGirls.append(RogueX) if RogueX not in ActiveGirls else ActiveGirls

    menu:
        r "A pleasure ta meet ya, [p.name]. Let me give ya the lay of the place." 
        "It's nice to meet you too.":
                #! $ RogueX.Statup("Love", 200, 20)
                #! $ RogueX.FaceChange("smile", 1)
                r "Oh, a gentleman. I think we'll really get along."                          
                #! $ RogueX.Blush = 0
                r "Ok, so let me show ya around. . ."
        "The \"lay\" of the place, eh?":
                #! $ RogueX.Statup("Love", 200, 10)
                #! $ RogueX.Brows = "normal"     
                #! $ RogueX.Eyes = "surprised"
                #! $ RogueX.Mouth = "smile"
                #! $ RogueX.Blush = 1
                r "Wha- what? N, no, that's not what I meant! I'm just giving you the campus tour!"
                #! $ RogueX.FaceChange("bemused")
                #! $ RogueX.Statup("Inbt", 200, 20)
                #! $ RogueX.Statup("Obed", 200, 20)
                r "Hmm. . ."           
                #! $ RogueX.Statup("Lust", 90, 3)
                #! $ RogueX.FaceChange("normal")
                #! $ RogueX.Eyes = "surprised"
                r "Anyways, let's get this back on track. . ."
                #! $ RogueX.FaceChange("smile", 0)
        "Whatever.":            
                #! $ RogueX.Statup("Obed", 200, 20)
                #! $ RogueX.FaceChange("sad")
                #! $ RogueX.Brows = "normal"
                r "Tsk, well ok, let's get started."
        "Screw off.":
                #! $ RogueX.Statup("Love", 200, -30)
                #! $ RogueX.Statup("Obed", 200, 30)
                #! $ RogueX.FaceChange("angry")
                #! show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
                #! with vpunch
                r "Well I never!"
                r "Hmph, I have to give the tour anyways, so get mov'in. . ."

    jump my_room