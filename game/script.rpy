# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chiaki")


# The game starts here.

# Testing to see if the commits work...

label start:
    # variables showing chiaki points and t/f values
    default chiakiclicked = 0
    default chiakibed = False
    default chiakicomputer = False
    scene bg bedroom

    show chiaki_idle

    if chiakiclicked ==2:
        jump doneobjects
    else: 
        call screen chiaki_sprite

        screen chiaki_sprite: 
            if chiakibed == False:
                imagebutton:
                    xanchor 0.5
                    yanchor 1.0
                    xpos 0.2
                    ypos 0.74
                    idle "chiaki_idle.png"
                    hover "chiaki_idle.png"
                    action Jump("GOHERE")

            if chiakicomputer == False:
                imagebutton: 
                    xanchor 0.5
                    yanchor 1.0
                    xpos 0.78
                    ypos 0.75
                    idle "chiaki_idle.png"
                    hover "chiaki_idle.png"
                    action Jump("compute")



label GOHERE:

    c "hai guys"
    $ chiakiclicked += 1
    $chiakibed = True
    jump start

label compute:

    c "im at the computer!!"
    $ chiakiclicked += 1
    $chiakicomputer = True
    jump start

label doneobjects:

    c "okay bye bye!!"

    # This ends the game.

    return
