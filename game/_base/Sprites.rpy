# Image system based on LayeredImage()


# Attempting to define a layeredImage here.
# TODO: Transition this to a statement equivalannt.
# TODO: Tie into Girl().
layeredimage test:
    #image_format "character/test/{image}.png"

    # body > head (eyes > mouth > eyebrows > hair) > breasts > pubes > arms
    attribute body null
    group body if_any "bare" auto variant "bare":
        anchor (0.0,0.0)
        zoom 0.75
        attribute none default

    group body if_not "bare" auto variant "hairy":
        anchor (0.0,0.0)
        zoom 0.75
        attribute none default

    group head auto prefix "head":
        anchor (0.0,0.0)
        zoom 0.75
        attribute base default

    group brows auto prefix "brows":
        anchor (0.0,0.0)
        zoom 0.75
        attribute normal default

    group eyes auto prefix "eyes":
        anchor (0.0,0.0)
        zoom 0.75
        attribute normal default

    group mouth auto prefix "mouth":
        anchor (0.0,0.0)
        zoom 0.75
        attribute normal default

    group hair auto:
        anchor (0.0,0.0)
        zoom 0.75
        attribute normal default

#    attribute pubic null #IDEA: May not work, possible bug
#    group pubic auto

    attribute arms null
    group arms if_any "up" auto variant "up":
        anchor (0.0,0.0)
        zoom 0.75
        attribute collargloves default

    group arms if_not "up" auto variant "normal":
        anchor (0.0,0.0)
        zoom 0.75
        attribute collargloves default

    # Chest layer must happen after arms to avoid bad overlapping.
    group chest auto:
        anchor (0.0,0.0)
        zoom 0.75
        attribute none default

    # bra > panty > inner > lower > dress > outer > neck > wrist
#    group bra auto

    group panty auto

    group lower auto variant "down"

    group lower auto variant "wet"

    group hose auto

    group inner auto

    group inner auto variant "up"

    group bottom auto

    group bottom auto variant "down"

    attribute dress null  #IDEA: See above
    group dress auto

    group outer auto

    group outer auto variant "up"

#IDEA: Check about separating arms and accessories.
    #group neck auto

    #group wrist auto

    group overlay auto multiple

    group overlay auto variant "pussy" multiple

    group overlay auto variant "face" multiple
