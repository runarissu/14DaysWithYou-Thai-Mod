################################################################################
## SPLASHSCREEN BABYYYY
################################################################################
label splashscreen:
    init -2:
        $ persistent.dlc_14nwy_ver = "000000"
    init:
        if renpy.variant("web"):
            $ renpy.quit()
        if renpy.exists('14 Nights With You/14nightswithyou.rpyc') or renpy.exists('14nightswithyou-free/14 Nights With You/14nightswithyou.rpyc') or renpy.exists('14nightswithyou-paid/14 Nights With You/14nightswithyou.rpyc'):
            if renpy.variant("mobile"):
                $ persistent.dlc_14nightswithyou = False
                $ persistent.dlc_14nightswithyou_type = "none"
            else:
                $ persistent.dlc_14nightswithyou = True
                if persistent.dlc_14dwy_ver == persistent.dlc_14nwy_ver:
                    $ persistent.dlc_14nwy_comp = True
                else:
                    $ persistent.dlc_14nwy_comp = False
        else:
            $ persistent.dlc_14nightswithyou = False
            $ persistent.dlc_14nightswithyou_type = "none"
        
        default preferences.volume.music = 0.6
        default preferences.volume.sfx = 0.9
        default preferences.volume.ambience = 0.8
        $ renpy.restart_interaction()

    scene black
    show cutielogo with pixellate
    play audio "audio/ui/cutiesai.ogg"
    $ persistent.game_open += 1
    $ mainmenutext = random.choice(mainmenulist)
    with Pause(3)
    hide cutielogo with fade

    python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('1410181514519515256', callbacks=callbacks, log=False)
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Watching anime with Ren',
                'large_image_key': '14dwy_logo',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

    if persistent.warningscreen == True:
        call screen gamewarning
    else:
        call screen over18 with GlitchDissolve
        $ renpy.pause(hard=True)

################################################################################
## VERSION NUMBER GEHEHEHEHEHHEE
################################################################################
screen versionscreen():
    vbox:
        xalign 0.99
        yalign 1
        if renpy.variant("pc"):
            text "Ver [version_number]" size 25 text_align 1.0:
                outlines [(absolute(1), "#141414", absolute(0), absolute(0))]
        if renpy.variant("mobile"):
            text "{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{noalt}YOU ARE USING A THIRD-PARTY APP\nBUGS AND ERRORS ARE TO BE EXPECTED\nPLAY ON PC FOR THE BEST EXPERIENCE\n(Ver [version_number]){/noalt}{/color}{/font}" size 25:
                outlines [(absolute(2), "#141414", absolute(0), absolute(0))]

################################################################################
## GAME INTRO BS IDK LOL
################################################################################
label start:
    if renpy.variant("web"):
        $ renpy.quit()
    scene black
    $ quick_menu = False
    $ _skipping = False
    pause 0.5
    play music "audio/bgm/Start Of The Day.ogg" fadein 1 fadeout 1
    pause 0.5
    if renpy.variant("mobile"):
        show screen androidversion
    else:
        show screen charamenu
    with dissolve
    $ renpy.pause(hard=True)

label game_start:
    scene black
    show glitch_2:
        parallel:
            xzoom -1.0
            alpha 0.1
            function WaveShader(10.0,1.0,0.1)
    show de_2:
        parallel:
            alpha 0.1
            matrixcolor TintMatrix("#65caf8")
            function WaveShader(3.0,3.0,0.2)
    stop music fadeout 1
    with GlitchDissolve

    ## FIRST NAME
    if player == "":
        $ player = "Angel"
    $ player_fl = player[:1].upper()
    $ ch_angel = player

    ## LAST NAME
    if surname == "":
        $ surname = "Mentior"
    $ surname_fl = surname[:1].upper()

    ## STREAMER STUFF
    if persistent.streamermode == True:
        $ fuck = "ugh"
        $ fucked = "messed"
        $ damn = "dang"
        $ dammit = "dangit"
        $ shit = "crap"
        $ pissing = "pouring"
        $ asshole = "loser"

    ## DEAD END STUFF
    if persistent.menumissing == True:
        $ rh_o = "{glitch=15.0}{size=+3}"
        $ rh_c = "{/size}{/glitch}"
        $ de_o = "{color=#a30b11}{s}"
        $ de_c = "{/s}{/color}"
    if persistent.menumissing == False:
        $ rh_o = ""
        $ rh_c = ""
        $ de_o = ""
        $ de_c = ""

    ## MISC STUFF
    if player == "Ren" or player == "ren":
        $ ch_angel = "{color=#9d64fd}Ren{/color}"
        $ ch_ren = "{color=#ff66cb}Ren{/color}"
    if player == "Moth" or player == "moth":
        $ ch_angel = "{color=#9d64fd}Moth{/color}"
        $ ch_moth = "{color=#5269b9}Moth{/color}"
    if player == "Violet" or player == "violet":
        $ ch_angel = "{color=#9d64fd}Violet{/color}"
        $ ch_violet = "{color=#c6b3f8}Violet{/color}"
    if player == "Elanor" or player == "elanor":
        $ ch_angel = "{color=#9d64fd}Elanor{/color}"
        $ ch_elanor = "{color=#d8c365}Elanor{/color}"
    if player == "Conan" or player == "conan":
        $ ch_angel = "{color=#9d64fd}Conan{/color}"
        $ ch_conan = "{color=98d2ff}Conan{/color}"
    if player == "Jae" or player == "jae":
        $ ch_angel = "{color=#9d64fd}Jae{/color}"
        $ ch_jae = "{color=#faa97e}Jae{/color}"
    if player == "Leon" or player == "leon":
        $ ch_angel = "{color=#9d64fd}Leon{/color}"
        $ ch_leon = "{color=#ee6c6d}Leon{/color}"
    if player == "Teo" or player == "teo":
        $ ch_angel = "{color=#9d64fd}Teo{/color}"
        $ ch_teo = "{color=#93b482}Teo{/color}"
    if player == "Olivia" or player == "olivia":
        $ ch_angel = "{color=#9d64fd}Olivia{/color}"
        $ ch_olivia = "{color=#a8a7a7}Olivia{/color}"
    if player == "Kiara" or player == "kiara":
        $ ch_angel = "{color=#9d64fd}Kiara{/color}"
        $ ch_kiara = "{color=#b18f84}Kiara{/color}"

    ## 14 NIGHTS WITH YOU DLCs
    if persistent.dlc_14nightswithyou == True:
        jump DLC_14NWY
    else:
        pass

label cont:
    ## STARTING STUFF
    play music "audio/bgm/Notice Me.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/static.ogg"
    window hide
    if persistent.warningscreen == True:
        call screen gamewarning
    if unlockable != "what else?":
        call unlockables from _call_unlockables
    if persistent.menumissing == True:
        rfade "{renvoid=1}were you looking for me, [player]?{/renvoid}" with dissolve
        rfade "{renvoid=1}hehe, you're so cute.{/renvoid}" with dissolve
        rfade "{renvoid=1}...{/renvoid}" with dissolve
        rfade "{renvoid=1}alright, are you ready to try again?{/renvoid}" with dissolve
        rfade "{renvoid=1}this time... i'll help you out.{/renvoid}" with dissolve
    elif persistent.dayend == True:
        rfade "{renvoid=1}...[player]?{/renvoid}" with DistortDissolve
        rfade "{renvoid=1}You're back...?{/renvoid}" with DistortDissolve
        rfade "{renvoid=1}Hah~ I can't wait to see you again...{/renvoid}" with DistortDissolve
    else:
        rfade "{renvoid=1}[player], huh...?{/renvoid}" with dissolve
        rfade "{renvoid=1}I see...{/renvoid}" with dissolve
        rfade "{renvoid=1}I can't wait to officially meet you...{/renvoid}" with dissolve
    pause 0.5
    scene black with GlitchDissolve
    pause 3.0
    jump day1

################################################################################
## LOL
################################################################################
label pathpoint:
    scene black
    #show text "\n"
    hide screen dayscalendar
    stop ambience fadeout 2.0
    $ quick_menu = False
    $ _skipping = False
    with GlitchDissolve

    if persistent.warningscreen == True:
        call screen gamewarning
    elif ending_demo == "obtained":
        $ config.skipping = None
        $ persistent.dayend = True
        $ ending_demo = "unobtained" ## so players can replay from the beginning
        if persistent.menumissing == True:
            $ persistent.menumissing = False
        call screen demopoint
    elif ending_good == "obtained":
        $ config.skipping = None
        $ ending_good = "unobtained"
        if persistent.dlc_14nightswithyou_type == "paid" and persistent.dlc_14nwy_comp == False:
            return
        call screen savepoint
    elif persistent.deadendings >= 5:
        jump deadend5
    elif persistent.deadendings == 4:
        jump deadend4
    elif persistent.deadendings == 3:
        jump deadend3
    elif persistent.deadendings == 2:
        jump deadend2
    elif persistent.deadendings == 1:
        jump deadend1
    else:
        $ config.skipping = None
        $ ending_demo = "unobtained"
        call screen demopoint

################################################################################
## SAVEPOINT
################################################################################
screen savepoint():
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    style_prefix "popupblack"
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            vbox:
                xalign 0.5
                text "{color=#FF66CB}{font=fonts/Orbitron-Regular.ttf}END OF DAY [calendar_day]!{/font}{/color}" size 55
            vbox:
                text "The next day will soon begin! Would you like to save your progress?":
                    size 25
                    xalign 0.5
                text "{color=#8f8f8f}({b}WARNING:{/b} Quicksaving will overwrite any previous saves!)\n{/color}":
                    size 20
                    xalign 0.5
            hbox:
                xalign 0.5
                spacing 30
                textbutton _("YES") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), QuickSave(message='PROGRESS HAS BEEN SAVED!', newest=True), SetVariable("persistent.dayend", True), Jump(skipday)] hovered [Play("sound", "audio/ui/click1.ogg")]
                textbutton _("NO") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), Jump(skipday)] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("QUIT") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), MainMenu(confirm=False)] hovered Play("sound", "audio/ui/click1.ogg")

################################################################################
## DEMO END
################################################################################
screen demopoint():
    add "other_dark"
    add "glitch_2":
        xzoom -1.0
        alpha 0.1
    add "de_2":
        alpha 0.1
        matrixcolor TintMatrix("#65caf8")
    
    frame:
        at slidedown, choice_fade
        background Frame(["gui/boxes/frame.png"], 30,30,30,30)
        padding (40,80)
        align (0.5,0.5)
        xsize 800
        vbox:
            xalign 0.5
            spacing 10
            vbox:
                xalign 0.5
                text "END OF THE DEMO":
                    size 55
                    color "#FF66CB"
                    font "fonts/Orbitron-Black.ttf"
            vbox:
                text "{size=+5}{font=Orbitron-Black.ttf}Thanks for playing!{/font}{/size}\nHave you tried to get all the different endings yet?\n\nIf you're looking for even more 14DWY content, feel free to check out the official {a=https://discord.gg/14dayswithyou}Discord{/a} | {a=https://14dayswithyou.tumblr.com}Tumblr{/a} | {a=https://twitter.com/14dayswithyou}Twitter{/a} | {a=https://bsky.app/profile/cutiesai.com}Bluesky{/a} for game development progress and lore drops!\n":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                    justify True
                    text_align 0.5
            hbox:
                xalign 0.5
                spacing 30
                textbutton _("RETURN TO MENU"):
                    text_style "ss_button"
                    action MainMenu(confirm=False)
    add "gui/misc/hearts.png" pos (1250, 680) at slideup, choice_fade

    imagebutton auto "demo_cutiesai_%s":
        at slideright, choice_fade
        align (0.98,0.98)
        action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("demo_bubble")]
        hovered Play("sound", "audio/ui/click2.ogg")

    if demo_bubble == True:
        frame:
            background Frame(["bubble_bottomright"], gui.choice_button_borders)
            padding (50,20)
            at slideright, choice_fade
            align (0.85,0.97)
            vbox:
                textbutton _("I'm {color=#ffcdeb}Saint{/color} (cutiesai), the sole developer of 14DWY! If you'd like to support me, here's my Ko-Fi!"):
                    text_style "button_text_bubble"
                    action [Play("sound", "audio/ui/blip.ogg"), OpenURL("https://ko-fi.com/cutiesai")]
                    hovered [Play("sound", "audio/ui/click1.ogg")]

################################################################################
## UNDERAGE WARNING
################################################################################
screen gamewarning():
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    style_prefix "popupblack"
    frame:
        align (0.5,0.5)
        vbox:
            xalign 0.5
            vbox:
                xalign 0.5
                text "PLEASE READ!":
                    font "fonts/Orbitron-Regular.ttf"
                    size 55
                    color "#FF66CB"
            vbox:
                text "{i}14 Days With You{/i} is intended for adults (18 and over).":
                    size 25
                    xalign 0.5
                text "Minors are prohibited from playing or interacting in any capacity.\n":
                    size 25
                    xalign 0.5
                text "{color=#8f8f8f}To avoid unlawful access, your game has now been restricted.\n{/color}":
                    size 20
                    xalign 0.5
            hbox:
                xalign 0.5
                spacing 20
                textbutton _("REMOVE RESTRICTION"):
                    text_style "cutietext"
                    text_color "#FF66CB"
                    text_hover_color "#9d64fd"
                    hovered [Play("sound", "audio/ui/click1.ogg")]
                    if renpy.variant("mobile"):
                        action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", True), OpenURL("https://14dayswithyou.tumblr.com/restriction"), MainMenu(confirm=False)]
                    if renpy.variant("pc"):
                        action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", True), OpenURL("https://14dayswithyou.tumblr.com/restriction"), Quit(confirm=False)]
                textbutton _("EXIT THE GAME"):
                    text_style "cutietext"
                    text_color "#FF66CB"
                    text_hover_color "#9d64fd"
                    hovered [Play("sound", "audio/ui/click1.ogg")]
                    if renpy.variant("mobile"):
                        action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", True), MainMenu(confirm=False)]
                    if renpy.variant("pc"):
                        action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", True), Quit(confirm=False)]

###############################################################################
## welcome to me progressively getting more unhinged as this script goes on
###############################################################################
style cutietext:
    selected_color "#FF66CB"
    hover_color "#9d64fd"
    idle_color "#898989"
    insensitive_color "#c5c5c5"
    bold True
    size 30
    font "fonts/Assistant-Regular.ttf"

style buttontext:
    selected_color "#898989"
    hover_color "#9d64fd"
    idle_color "#FF66CB"
    insensitive_color "#565656"
    bold True
    size 30
    font "fonts/Assistant-Regular.ttf"

style button_text_bubble:
    selected_color "#FF66CB"
    hover_color "#9d64fd"
    idle_color "#f8f8f8"
    insensitive_color "#f8f8f8"
    size 25
    font "fonts/VT323-Regular.ttf"
    text_align 0.5
    align (0.5,0.5)

style popupbox_text_pink:
    color "#FF66CB"
    font "Orbitron-Black.ttf"
    size 30
    text_align 0.5
    align (0.5,0.5)

style tempname_text:
    font "fonts/VT323-Regular.ttf"
    color "#f8f8f8"
    size 25
    align (0.0,0,5)

style gallery_buttontext:
    selected_color "#9d64fd"
    hover_color "#141414"
    idle_color "#FF66CB"
    bold True
    size 24
    font "fonts/Assistant-Regular.ttf"

style socials_buttontext:
    selected_color "#FF66CB"
    hover_color "#9d64fd"
    idle_color "#f8f8f8"
    insensitive_color "#8d8d8d"
    bold False
    size 22
    font "fonts/Assistant-Regular.ttf"
    outlines [ (absolute(1), "141414", absolute(1), absolute(1)) ]

style customise_buttontext:
    selected_color "#9d64fd"
    hover_color "#FF66CB"
    idle_color "#f8f8f8"
    size 35
    bold False
    font "fonts/VT323-Regular.ttf"

style notepad:
    font "fonts/ReenieBeanie-Regular.ttf"
    size 48
    color "#141414"

style ss_button:
    outlines [ (absolute(3), "362A46", absolute(2), absolute(2)) ]
    font "fonts/VarelaRound-Regular.ttf"
    size 30
    idle_color "#FF66CB"
    hover_color "#9d64fd"
    bold True

style terminal_button:
    font "fonts/VT323-Regular.ttf"
    color "#f8f8f8"
    size 25
    idle_color "#f8f8f8"
    hover_color "#FF66CB"

style popupblack_frame:
    background Frame(["gui/boxes/popup_black.png"], gui.confirm_frame_borders)
    xminimum 600
    xmaximum 1300
    text_align 0.5
    padding (50, 120, 50, 80)

style popupblack_text:
    font "fonts/Assistant-Regular.ttf"
    color "#f8f8f8"
    size 25

style popupwhite_frame:
    background Frame(["gui/boxes/popup_white.png"], 130, 140, 130, 110)
    xminimum 600
    xmaximum 1300
    text_align 0.5
    padding (50, 120, 50, 80)

style popupwhite_text:
    font "fonts/Assistant-Regular.ttf"
    color "#141414"
    size 25

style popup_button:
    padding (3,3,3,3)
    #maximum (42,42)
    #minimum(42,42)
    selected_color "#FF66CB"
    hover_color "#9d64fd"
    idle_color "#f8f8f8"
    font "fonts/VT323-Regular.ttf"
    size 30
    text_align 0.5

## only until I finish da game
style popup_button2:
    padding (3,3,3,3)
    maximum (42,42)
    minimum(42,42)
    selected_color "#8f8f8f"
    hover_color "#8f8f8f"
    idle_color "#8f8f8f"
    font "fonts/VT323-Regular.ttf"
    size 30
    text_align 0.5

###############################################################################
## CHARACTER MENUUUUUU OOOOOOOOWOOOOOOOO
###############################################################################
screen charamenu():
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    add "gui/bg/cc_base.png" at slidedown
    vbox:
        at slidedown
        pos (1296, 300)
        spacing -5
        xminimum 408
        vbox:
            align (0.5,0.5)
            text "Customise the main character?":
                size 22
                font "fonts/Assistant-Regular.ttf"
                color "#f8f8f8"
        hbox:
            align (0.5,0.5)
            vbox:
                align (0.5,0.5)
                textbutton _("DEFAULT") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("custom_angel", False), refresh_custom_angel] hovered [Play("sound", "audio/ui/click1.ogg")]
            vbox:
                align (0.5,0.5)
                textbutton _("CUSTOM") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("custom_angel", True), assign_colours, Show("customcharacter", dissolve)] hovered [Play("sound", "audio/ui/click1.ogg")]

    vbox:
        at slidedown
        pos (1296,796)
        spacing -5
        xminimum 408
        vbox:
            align (0.5, 0.5)
            if persistent.streamermode == True:
                text "\"{color=#FF66CB}{b}Streamer Mode{/b}{/color}\" is currently enabled.\nPlease disable it to use this feature.":
                    size 22
                    font "fonts/Assistant-Regular.ttf"
                    color "#141414"
                    text_align 0.5
            elif persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid" and persistent.dlc_14nwy_comp == False:
                    text "Please update the base game and its DLC\nto unlock this section.":
                        size 22
                        textalign 0.5
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
            elif persistent.dlc_14nightswithyou == True:
                text "Do you want to enable the 18+ DLC?":
                    size 22
                    font "fonts/Assistant-Regular.ttf"
                    color "#141414"
                    text_align 0.5
                hbox:
                    align (0.5,0.5)
                    spacing 90
                    textbutton _("YES") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("dlc_14nightswithyou_scenes", True), Show("customisensfw", dissolve)] hovered [Play("sound", "audio/ui/click1.ogg")]
                    textbutton _("NO") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("dlc_14nightswithyou_scenes", False)] hovered Play("sound", "audio/ui/click1.ogg")
            else:
                text "You don't own any DLCs! Visit\n{a=https://cutiesai.itch.io/}{b}cutiesai.itch.io{/b}{/a} to enable this feature":
                    size 22
                    font "fonts/Assistant-Regular.ttf"
                    color "#141414"
                    text_align 0.5

    ## Profile section hehe
    hbox:
        at slidedown
        pos (789,678)
        text "14 Days With You is still a demo!\nConsider supporting cutiesai\non {a=https://ko-fi.com/cutiesai}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Ko-Fi{/color}{/font}{/a}, {a=https://cutiesai.itch.io/14dayswithyou}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Itch{/color}{/font}{/a}, or {a=https://discord.gg/14dayswithyou}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Discord{/color}{/font}{/a}!":
            size 28
            font "fonts/VT323-Regular.ttf"
            color "#141414"
            text_align 0.5
    vbox:
        at slidedown
        pos (773,459)
        spacing -5
        text "{font=fonts/Orbitron-Black.ttf}{color=#5f5f5f}[player] {/color}{/font}" size 40
        text "{font=fonts/Assistant-Regular.ttf}{color=#898989}@[username_angel!u]{/color}{/font}" size 20
    vbox:
        at slidedown
        pos (773,554)
        spacing -5
        if update_angel == "status":
            text "You're in Haruko's DMs? I'm in sane\nWe are not the same <3 ([they]/[them])":
                font "fonts/Assistant-Regular.ttf"
                color "#898989"
                size 25
        else:
            frame:
                background None
                xysize (384,54)
                text "{font=fonts/Assistant-Regular.ttf}{color=#898989}[update_angel]{/color}{/font}" size 25

    ## pwofile
    hbox:
        pos (397,260)
        imagebutton idle "icon_profile" action [Play("sound", "audio/ui/cancel.ogg"), Show("relprofile")] hovered Play("sound", "audio/ui/click_chime.ogg")
        at profile_zoom, slidedown

    ## user thingy
    vbox:
        at slidedown
        pos (257,420)
        spacing -8
        xminimum 435
        hbox:
            align (0.5,0.5)
            if persistent.dayend == True:
                text "WELCOME BACK!":
                    size 30
                    font "fonts/Orbitron-Black.ttf"
                    color "#141414"
            else:
                text "HELLO THERE!":
                    size 30
                    font "fonts/Orbitron-Black.ttf"
                    color "#141414"
        hbox:
            align (0.5,0.5)
            if persistent.streamermode == True:
                text "FEB 14  ·  02:14":
                    font "fonts/Assistant-Regular.ttf"
                    color "#8f8f8f"
                    size 20
            else:
                timer 0.30 action update_time repeat True
                text "[month!u] [day]  ·  [hours:0=2]:[min:0=2]":
                    font "fonts/Assistant-Regular.ttf"
                    color "#8f8f8f"
                    size 20

## Easter Eggs
    imagebutton:
        idle "gui/misc/logo sticker.png"
        hover "gui/misc/logo sticker.png"
        anchor (0.5, 0.5)
        pos (230,875)
        action [Play("sound", "audio/ui/cancel.ogg"), OpenURL("https://cutiesai.com/14dwy")]
        hovered Play("sound", "audio/ui/click2.ogg")
        at sticker_button, slidedown 
    vbox:
        at slidedown
        pos (248, 594)
        xsize 386
        spacing 10
        vbox:
            text "- change my icon somehow\n- Passw0rd_777 {size=-10}(with a zero!!!){/size}\n- 01101100 01101111 01101100\n- underneath the stickynote":
                font "fonts/ReenieBeanie-Regular.ttf"
                color "#141414"
                bold False
                size 40
                text_align 0.0
        vbox:
            xalign 0.5
            button:
                key_events True
                align (0.5,0.5)
                action unlockable_input.Toggle()
                input:
                    length 500
                    value unlockable_input
                    font "fonts/ReenieBeanie-Regular.ttf"
                    color "#850106"
                    bold False
                    size 70
                    pixel_width 356
                    allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ## map icons
    fixed:
        at slidedown
        if custom_angel == True:
            imagebutton auto "angel_sprite_%s":
                pos (1476,580)
                action NullAction()
                tooltip "{color=#ff66cb}{size=+5}@[username_angel!u]{/size}{/color}\n[player!u], [surname!u] | [they!u]/[them!u]"
        else:
            imagebutton:
                idle "gui/socials/sprites/angel.png"
                hover "gui/socials/sprites/angel.png"
                pos (1476,580)
                action NullAction()
                tooltip "{color=#ff66cb}{size=+5}@[username_angel!u]{/size}{/color}\n[player!u], [surname!u] | [they!u]/[them!u]"
        imagebutton auto "sprite_ren_%s":
            action NullAction()
            pos (1510,553)
            tooltip "{color=#ff66cb}{size=+5}@[username_ren]{/size}{/color}\n{glitch=3}{font=fonts/VT323-Regular.ttf}{size=20}{color=#f8f8f8}FUTURE, HUSBAND{/glitch} | HE/THEY"
        imagebutton auto "sprite_moth_%s":
            action NullAction()
            pos (1374,641)
            tooltip"{color=#ff66cb}{size=+5}@[username_moth]{/size}{/color}\nMOTH, ATLAS | THEY/ANY" ## Once Moth's real name is unlocked, this will change
        imagebutton auto "sprite_violet_%s":
            action NullAction()
            pos (1596,602)
            tooltip"{color=#ff66cb}{size=+5}@[username_violet]{/size}{/color}\nVIOLET, GARCIA | SHE/HER"
        imagebutton auto "sprite_elanor_%s":
            action NullAction()
            pos (1608,523)
            tooltip"{color=#ff66cb}{size=+5}@[username_elanor]{/size}{/color}\nELANOR, CRESTON | SHE/THEY"
        imagebutton auto "sprite_conan_%s":
            action NullAction()
            pos (1625,475)
            tooltip"{color=#ff66cb}{size=+5}@[username_conan]{/size}{/color}\nCONAN, O'ROURKE | HE/THEY"
        imagebutton auto "sprite_jae_%s":
            action NullAction()
            pos (1591,441)
            tooltip"{color=#ff66cb}{size=+5}@[username_jae]{/size}{/color}\nJAE-HYUN, KIM | HE/HIM"
        imagebutton auto "sprite_leon_%s":
            action NullAction()
            pos (1340,607)
            tooltip"{color=#ff66cb}{size=+5}@[username_leon]{/size}{/color}\nLEON, DAVIS | HE/HIM"
        imagebutton auto "sprite_teo_%s":
            action NullAction()
            pos (1330,437)
            tooltip"{color=#ff66cb}{size=+5}@[username_teo]{/size}{/color}\nTEODORE, ALVARADO | HE/HIM"
        imagebutton auto "sprite_olivia_%s":
            action NullAction()
            pos (1501,475)
            tooltip"{color=#ff66cb}{size=+5}@[username_olivia]{/size}{/color}\nOLIVIA, DAWHAN | SHE/HER"
        imagebutton auto "sprite_kiara_%s":
            action NullAction()
            pos (1481,660)
            tooltip"{color=#ff66cb}{size=+5}@[username_kiara]{/size}{/color}\nKIARA, CRESTON | SHE/ANY"
        


    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                background Frame(["gui/boxes/frame.png"], 20,20,20,20)
                align (0.5,0.5)
                padding (30,10,30,10)
                margin (0,0,0,10)
                text tooltip:
                    font "fonts/VT323-Regular.ttf"
                    size 20
                    color "#f8f8f8"
                    text_align 0.5

    ## butttons because I forget
    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Hide("charamenu"), MainMenu(confirm=False)] at amm_button, slideleft anchor (0.5, 0.5) pos (0.06, 975) hovered Play("sound", "audio/ui/click2.ogg")
    imagebutton auto "gui/ui/forward_%s.png" action [Play("sound", "audio/ui/accept.ogg"), Hide ("charamenu"), Jump("game_start")] at amm_button, slideright anchor (0.5, 0.5) pos (0.94, 975) hovered Play("sound", "audio/ui/click2.ogg")

################################################################################
## TRANSITIONS AND TRANSFORMS BS
################################################################################
# *Jenna Marbles shutting her flip phone shut gif*
transform profile_zoom:
    zoom 1.0

transform vcright:
    xalign 0.8
    
# CROWDED CROWDED GIRLS MOVE AWAY FROM EACH OTHER
transform cleft:
    xalign 0.1

# same as above but to the right
transform cright:
    xalign 0.9

# TWO SPRITES GETTING CLOSER TO EACH OTHER... THEY MIGHT KISS
transform tleft:
    xalign 0.3

# TWO THE RIGHT NOW YO ONE HOP THIS TIME ONE HOP TH
transform tright:
    xalign 0.7

# RAAAAAAAAHHHHHHHHH
transform ffullyleft:
    xalign 0.2

transform fleft:
    xalign 0.4

transform fright:
    xalign 0.7

transform ffullyright:
    xalign 0.8

# EASTER EGGSSSSSSSSS
transform mpfullyleft:
    xalign 0.2

transform mpleft:
    xalign 0.5

transform mpright:
    xalign 0.7

transform mpfullyright:
    xalign 0.9

# sprite center small jump/pop
transform spop:
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

# sprite center big jump/pop
transform bpop:
    linear 0.1 yoffset -50
    linear 0.1 yoffset 0

# sprite close small jump/pop
transform clspop:
    xalign 0.1
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

# sprite close big jump/pop
transform clbpop:
    xalign 0.1
    linear 0.1 yoffset -50
    linear 0.1 yoffset 0

# sprite close small jump/pop
transform crspop:
    xalign 0.9
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

# sprite close big jump/pop
transform crbpop:
    xalign 0.9
    linear 0.1 yoffset -50
    linear 0.1 yoffset 0

# sprite close small jump/pop
transform tlspop:
    xalign 0.3
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

# sprite close big jump/pop
transform tlbpop:
    xalign 0.3
    linear 0.1 yoffset -50
    linear 0.1 yoffset 0

# sprite close small jump/pop
transform trspop:
    xalign 0.7
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

# sprite close big jump/pop
transform trbpop:
    xalign 0.7
    linear 0.1 yoffset -50
    linear 0.1 yoffset 0

# LET ME FLICKER IMAGES PLS
transform flicker:
    linear 2.0 alpha 0.0
    choice:
        pause 1
    choice:
        pause 0.2
    choice:
        pause 0.5
    choice:
        pause 1.5
    linear 2.0 alpha 1.0
    repeat

# JUMPSCARE HEHEHEHE
transform jumpscare:
    xalign 0.5
    yalign 0.5
    ease .5 zoom 3.0 xoffset -10 yoffset 10

## Slide effect
transform slidein:
    ease 0.3 xoffset 20

transform slideout:
    ease 0.3 xoffset 0

transform slideleft:
    xoffset -35
    ease 0.5 xoffset 0

transform slideright:
    xoffset 35
    ease 0.5 xoffset 0

transform slidedown:
    yoffset -35
    ease 0.5 yoffset 0

transform slideup:
    yoffset 35
    ease 0.5 yoffset 0

transform fadeywadey:
    alpha 0
    linear 0.5 alpha 1

## misc
transform amm_button: 
    on hover: 
        linear 0.3 zoom 1.05   
    on idle:
        linear 0.3 zoom 1.0

transform sticker_button:
    on hover:
        rotate -30
        linear 0.3 zoom 1.05   
    on idle:
        rotate -30
        linear 0.3 zoom 1.0

transform newscroll:
    crop (-637, 0, 637, 41)
    ease 20.0 crop (637, 0, 637, 41)
    repeat

transform hehehe:
    offscreenleft
    alpha 0.0
    easein 1.0 xalign 0.5 alpha 1.0

## matrixcolour wahoo
transform fadetint:
    matrixcolor SaturationMatrix(0.9)*ContrastMatrix(2.9)*HueMatrix(90)

transform ghosttint:
    matrixcolor TintMatrix("#d5c6de")*OpacityMatrix(0.5)*SaturationMatrix(3)*ContrastMatrix(2)*HueMatrix(310)

################################################################################
## CTC BS
################################################################################
image ctc:
    "ctc_carat"
    alpha 1
    block:
        linear 1.0 alpha 1
        "ctc_carat"
        linear 1 alpha 0.0
        repeat

################################################################################
## SCREEN EFFECTS BABY LESSGOOOOOOO
################################################################################
# dust particle effect: white, purple, pink/main menu
image peffect= SnowBlossom(At("images/effects/dust.png", flicker), border=0, count=30, start=0, fast=False, yspeed=(-50, -10), xspeed=(-20,40), horizontal=False)
image peffectp= SnowBlossom(At("images/effects/dustp.png", flicker), border=0, count=30, start=0, fast=False, yspeed=(-50, -10), xspeed=(-20,40), horizontal=False)
image peffectmm= SnowBlossom(At("images/effects/dustmm.png", flicker), border=0, count=20, start=0, fast=False, yspeed=(-20, -10), xspeed=(-10,20), horizontal=False)

# industrial smoke effect
image ceffect= Fixed(SnowBlossom(At("images/effects/cloud.png", flicker), border=-350, count=7, start=0, fast=False, xspeed=(0, -500), yspeed=(0, -60), horizontal=False))

#smoke effect
image seffect= Fixed(SnowBlossom(At("images/effects/cloud.png", flicker), border=-5, count=10, start=0, fast=False, xspeed=(0, 500), yspeed=(30, -500), horizontal=False))

#rain effect
image reffect= Fixed(SnowBlossom(At("images/effects/rain.png", flicker), border=0, count=100, start=0, fast=False, xspeed=(0, 0), yspeed=(1000, 2000), horizontal=False))

# dissolve effect
default GlitchDissolve = ImageDissolve("images/effects/glitch.png", 2.0, ramplen=256, reverse=True)
default DistortDissolve = ImageDissolve("images/effects/glitch 2.webp", 0.5, ramplen=256, reverse=True)

# flash effect
default owie = Fade(0.1, 0.0, 0.5, color="#a30b11")

################################################################################
## CALLBACK
################################################################################
init -1 python:
    def blip1(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/ui/blip1.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def blip2(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/ui/blip2.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def blip3(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/ui/blip3.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def blip4(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/ui/blip4.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def blip5(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/sfx/whispers.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

################################################################################
## PROBS SHOULDNT PUT THE CURSOR STUFF HERE
################################################################################
define config.mouse = {}
define config.mouse['default'] = [("gui/ui/arrow.png",0,0)]

################################################################################
## CAWENDAR OWO
################################################################################
screen dayscalendar():
    zorder 99
    default socialhover = False
    fixed:
        at slideleft
        button:
            pos (124,62)
            focus_mask True 
            imagebutton auto "gui/ui/socialtab_%s.png" action [Play("sound", "audio/ui/choice.ogg"), SetScreenVariable("socialhover", False), ShowMenu("relationmenu")] hovered [Play("sound", "audio/ui/blip.ogg"), SetScreenVariable("socialhover", True)] unhovered SetScreenVariable("socialhover", False)

            if socialhover:
                at slidein
            else:
                at slideout

        add "gui/ui/calendar.png":
            pos (18,18)

        frame:
            background None
            pos (33,60)
            xminimum 150
            vbox:
                spacing -20
                xalign 0.5
                hbox:
                    xalign 0.5
                    text "{noalt}DAY{/noalt}":
                        size 20
                        font "fonts/Orbitron-Regular.ttf"
                        color "#f8f8f8"
                        text_align 0.5
                hbox:
                    xalign 0.5
                    text "{noalt}[calendar_day]{/noalt}":
                        size 64
                        font "fonts/Orbitron-Regular.ttf"
                        color "#f8f8f8"
                        text_align 0.5

################################################################################
## hehehe secret <3
################################################################################
transform poggywoggy:
        linear 1 xoffset -3 yoffset 3
        linear 1 xoffset 4 yoffset -4 
        linear 1 xoffset 2 yoffset -2
        linear 1 xoffset 4 yoffset -4
        linear 1 xoffset -1 yoffset 1
        linear 1 xoffset -2 yoffset 2
        linear 1 xoffset 2 yoffset -2
        linear 1 xoffset -1 yoffset 1
        linear 1 xoffset -2 yoffset 2
        repeat

################################################################################
## elder scrollin or something idk
################################################################################
image triangles_light:
    "gui/misc/triangles_light.png"
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0
    linear 30.0 xalign 1.0 yalign 1.0
    repeat

################################################################################
## CGI MENUWU
################################################################################
screen menuwu():
    default socialhover = False
    button:
        xpos -70
        ypos 20
        focus_mask True 
        imagebutton auto "gui/ui/socialtab_%s.png" action [Play("sound", "audio/ui/click2.ogg"), SetScreenVariable("socialhover", False), ShowMenu('preferences')] hovered [SetScreenVariable("socialhover", True)] unhovered SetScreenVariable("socialhover", False)
        if socialhover:
            at slidein
        else:
            at slideout

################################################################################
## STREAMER MODE BABYYYYYYYY
################################################################################
screen streamingmode():
    modal True
    add "images/bg/other_dark.webp" alpha 0.8 at choice_fade
    style_prefix "popupblack"
    frame:
        at slidedown
        align (0.5, 0.5)
        vbox:
            xmaximum 600
            spacing 20
            vbox:
                align (0.5,0.5)
                text "STREAMER MODE":
                    size 55
                    font "fonts/Orbitron-Black.ttf"
                    color "#FF66CB"
                    xalign 0.5
                vbox:
                    text "\nEnabling this mode will do the following:":
                        color "#9d64fd"
                        size 25
                        xalign 0.5
                        text_align 0.5
                    text "- Hide any instances of your device's internal clock\n- Limit the amount of strong language used\n- Disable all sexual content (including the 18+ DLC)\n- This mode currently {u}does not{/u} change the horror, gore, and darker elements found within the demo!":
                        size 23
                        xalign 0.5
                        justify True
                        text_align 0.0
            hbox:
                align (0.5,0.5)
                spacing 30
                textbutton _("ENABLE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("persistent.streamermode", True)] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("DISABLE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("persistent.streamermode", False)] hovered Play("sound", "audio/ui/click1.ogg")
            text "If you'd like to know what you're allowed to record or livestream, please {a=https://cutiesai.com/14dwy}visit this webpage{/a}. It'll open in your browser!":
                size 20
                xalign 0.5
                color "#8f8f8f"
                text_align 0.5

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Hide("streamingmode")] at amm_button, slideleft anchor (0.5, 0.5) pos (0.28, 800) hovered Play("sound", "audio/ui/click2.ogg")

################################################################################
## HEEUUUUUGHGHGHGHGSDGSHJ
################################################################################
screen relprofile():
    tag menu
    modal True
    add "images/bg/other_dark.webp" alpha 0.8 at choice_fade
    frame:
        at choice_fade
        background Frame(["gui/boxes/popup_black.png"], gui.confirm_frame_borders)
        align (0.7,0.5)
        xysize (400,400)
        vpgrid:
            cols 2
            area (350, 310, 350, 310)
            scrollbars "vertical"
            mousewheel True
            align (0.5,0.75)
            spacing 7
            imagebutton:
                idle "picon_angel"
                hover "picon_angel_hover"
                selected_idle "picon_angel_selected"
                selected_hover "picon_angel_hover"
                action SetVariable("angel_icon", "def")
            imagebutton:
                idle "picon_angelalt"
                hover "picon_angelalt_hover"
                selected_idle "picon_angelalt_selected"
                selected_hover "picon_angelalt_hover"
                action SetVariable("angel_icon", "alt")
            imagebutton:
                idle "picon_teohonkers"
                hover "picon_teohonkers_hover"
                selected_idle "picon_teohonkers_selected"
                selected_hover "picon_teohonkers_hover"
                action SetVariable("angel_icon", "teo")
            imagebutton:
                idle "picon_renhonkers"
                hover "picon_renhonkers_hover"
                selected_idle "picon_renhonkers_selected"
                selected_hover "picon_renhonkers_hover"
                action SetVariable("angel_icon", "ren")
            imagebutton:
                idle "picon_renayaya"
                hover "picon_renayaya_hover"
                selected_idle "picon_renayaya_selected"
                selected_hover "picon_renayaya_hover"
                action SetVariable("angel_icon", "ayaya")
            imagebutton:
                idle "picon_redacted"
                hover "picon_redacted_hover"
                selected_idle "picon_redacted_selected"
                selected_hover "picon_redacted_hover"
                action SetVariable("angel_icon", "redacted")
            imagebutton:
                idle "picon_cutiesai"
                hover "picon_cutiesai_hover"
                selected_idle "picon_cutiesai_selected"
                selected_hover "picon_cutiesai_hover"
                action SetVariable("angel_icon", "cutiesai")
            imagebutton:
                idle "picon_mon"
                hover "picon_mon_hover"
                selected_idle "picon_mon_selected"
                selected_hover "picon_mon_hover"
                action SetVariable("angel_icon", "mon")
            imagebutton:
                idle "picon_ten"
                hover "picon_ten_hover"
                selected_idle "picon_ten_selected"
                selected_hover "picon_ten_hover"
                action SetVariable("angel_icon", "ten")
            imagebutton:
                idle "picon_puppy"
                hover "picon_puppy_hover"
                selected_idle "picon_puppy_selected"
                selected_hover "picon_puppy_hover"
                action SetVariable("angel_icon", "puppy")
            imagebutton:
                idle "picon_chii"
                hover "picon_chii_hover"
                selected_idle "picon_chii_selected"
                selected_hover "picon_chii_hover"
                action SetVariable("angel_icon", "chii")
            imagebutton:
                idle "picon_eve"
                hover "picon_eve_hover"
                selected_idle "picon_eve_selected"
                selected_hover "picon_eve_hover"
                action SetVariable("angel_icon", "eve")
            if custom_angel == True:
                imagebutton:
                    idle "picon_angelsprite"
                    hover "picon_angelsprite_hover"
                    selected_idle "picon_angelsprite_selected"
                    selected_hover "picon_angelsprite_hover"
                    action SetVariable("angel_icon", "sprite")

    frame:
        at choice_fade
        background Frame(["gui/boxes/popup_black.png"], gui.confirm_frame_borders)
        align (0.28,0.37)
        xysize (700,200)
        vbox:
            align (0.5,0.7)
            text "Want to update your status?":
                font "fonts/Orbitron-Black.ttf"
                color "#f8f8f8"
                size 30
            button:
                key_events True
                xalign 0.5
                action update_angel_input.Toggle()
                input:
                    length 40
                    bold False
                    value update_angel_input
                    pixel_width 480

    frame:
        at choice_fade
        background Frame(["gui/boxes/popup_white.png"], gui.confirm_frame_borders)
        align (0.36,0.63)
        xysize (550,200)
        vbox:
            align (0.5,0.7)
            text "Change your username?":
                font "fonts/Orbitron-Black.ttf"
                color "#141414"
                size 30
            button:
                key_events True
                xalign 0.5
                action username_angel_input.Toggle()
                input:
                    length 15
                    bold False
                    color "#9D64FD"
                    value username_angel_input
                    exclude " `~!@#$%^&*-=+\|;:'\"[]{}(),<>/?"
    if custom_angel == True:
        imagebutton auto "gui/ui/more_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Show("customcharacter", dissolve)] at amm_button, choice_fade anchor (0.5, 0.5) pos (0.21, 604) hovered Play("sound", "audio/ui/click2.ogg")
        imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), refresh_status_angel, refresh_username_angel, Hide("relprofile")] at amm_button, choice_fade anchor (0.5, 0.5) pos (0.21, 712) hovered Play("sound", "audio/ui/click2.ogg")
    else:
        imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), refresh_status_angel, refresh_username_angel, Hide("relprofile")] at amm_button, choice_fade anchor (0.5, 0.5) pos (0.21, 665) hovered Play("sound", "audio/ui/click2.ogg")

################################################################################
## LOGIN SCREEN (after warning)
################################################################################
label loginscreen:
    scene black
    $ quick_menu = False
    $ _skipping = False
    pause 2.0
    show screen customiselogin
    with pixellate
    $ renpy.pause(hard=True)
    $ persistent.dlc_14nwy_ver = persistent.dlc_14nwy_ver

screen customiselogin():
    modal True
    add "bg/desktop_bg.webp"
    add "peffect"
    frame:
        at choice_fade
        background Frame(["gui/boxes/frame.png"])
        padding (30,80)
        align (0.5,0.5)
        vbox:
            align (0.5,0.5)
            spacing 20
            text "====-       :----\n+=+++=====------=-====\n===++++======-===+-=====\n====+++++++====+*+=======\n====+++++++++=+**+======-\n--===+++++++++**+======-\n-=====+*****##*+=+===-\n-===++**##***++=====\n=++++++++++=====\n--===++=====\n-===+===\n-=":
                size 15
                font "fonts/VT323-Regular.ttf"
                line_spacing -2
                kerning 1
                bold True
                align (0.5,0.5)
                text_align 0.5
                color "#ff66cb"
            text "{size=+20}WELCOME BACK!{/size}\nEnter your CorUpdates username to continue":
                size 25
                font "fonts/VT323-Regular.ttf"
                color "#f8f8f8"
                text_align 0.5
                align (0.5,0.5)
            frame:
                background Frame(["socials_offblack"], 20,20,20,20)
                padding (15,5,15,5)
                align (0.5,0.5)
                xysize (250,40)
                input:
                    default ""
                    value VariableInputValue("persistent.corupdate_user")
                    exclude " `~!@#$%^&*-=+\|;:'\"[]{}(),<>/?"
                    font "fonts/VT323-Regular.ttf"
                    size 28
                    length 15
                    bold False
                    text_align 0.5
                    align (0.5,0.5)
            textbutton _("ENTER") text_style "buttontext" action [Play("sound", "audio/ui/blip.ogg"), Hide("customiselogin"), MainMenu(confirm=False)] at choice_fade hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5) sensitive persistent.corupdate_user != ""
    vbox:
        at choice_fade
        align (0.98,0.98)
        spacing 10
        frame:
            background Frame(["bubble_bottomright"], gui.choice_button_borders)
            padding (50,25)
            xalign 1.0
            vbox:
                text "Hello, angel! {size=-5}👋😇{/size}":
                    size 25
                    font "fonts/VT323-Regular.ttf"
                    color "#f8f8f8"
                    text_align 0.5
                    align (0.5,0.5)
        frame:
            background Frame(["bubble_bottomright"], gui.choice_button_borders)
            padding (50,25)
            xalign 1.0
            vbox:
                text "Are you a content creator or live streamer?":
                    size 25
                    font "fonts/VT323-Regular.ttf"
                    color "#f8f8f8"
                    text_align 0.5
                    align (0.5,0.5)
        frame:
            background Frame(["bubble_bottomright"], gui.choice_button_borders)
            padding (50,20)
            xalign 1.0
            textbutton _("If so, click here for more options!") text_style "button_text_bubble" action [Play("sound", "audio/ui/blip.ogg"), Show("streamingmode", dissolve)] at choice_fade hovered [Play("sound", "audio/ui/click1.ogg")]

################################################################################
## CREATE CUSTOM ANGEL YEEHAWWWW
################################################################################
screen customcharacter():
    modal True
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    add "gui/bg/customise_base.png" at choice_fade
    add "player_sprite":
        at choice_fade
        pos (432,215)

    vbox:
        at choice_fade
        pos (385, 833)
        spacing -5
        xminimum 432
        vbox:
            align (0.5,0.5)
            text "What would you like to be called?":
                size 22
                font "fonts/Assistant-Regular.ttf"
                color "#f8f8f8"
        hbox:
            align (0.5,0.5)
            vbox:
                align (0.5,0.5)
                hbox:
                    button:
                        key_events True
                        xalign 0.5
                        action player_input.Toggle()
                        input:
                            length 12
                            color "#ff66cb"
                            value player_input
                            exclude "`~!@#$%^&*_-=+\|;:'\"[]{}(),<>./?"
            vbox:
                align (0.5,0.5)
                hbox:
                    button:
                        key_events True
                        xalign 0.5
                        action surname_input.Toggle()
                        input:
                            length 12
                            color "#9D64FD"
                            value surname_input
                            exclude "`~!@#$%^&*_-=+\|;:'\"[]{}(),<>./?"
    vbox:
        at choice_fade
        pos (853, 833)
        spacing -5
        xminimum 432
        hbox:
            align (0.5, 0.5)
            text "What pronouns do you use?":
                size 22
                font "fonts/Assistant-Regular.ttf"
                color "#141414"
        hbox:
            align (0.5, 0.5)
            spacing 10
            textbutton _("SHE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("pronoun", "female"), refresh_pronouns] hovered Play("sound", "audio/ui/click1.ogg")
            textbutton _("HE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("pronoun", "male"), refresh_pronouns] hovered Play("sound", "audio/ui/click1.ogg")
            textbutton _("THEY") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("pronoun", "neutral"), refresh_pronouns] hovered Play("sound", "audio/ui/click1.ogg")
            textbutton _("CUSTOM") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), refresh_pronouns, SetVariable("pronoun", "custom"), Show("custompronouns", dissolve), refresh_pronouns] hovered [Play("sound", "audio/ui/click1.ogg")]

    vbox:
        at choice_fade
        pos (384, 452)
        xminimum 200
        yminimum 300
        vbox:
            align (0.5,0.5)
            spacing 3
            textbutton _("FACE") text_style "customise_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_category", "face")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
            textbutton _("EYES") text_style "customise_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_category", "eyes")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
            textbutton _("HAIR") text_style "customise_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_category", "hair")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
            textbutton _("BODY") text_style "customise_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_category", "body")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
            textbutton _("MISC") text_style "customise_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_category", "misc"), assign_colours] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)

    if customise_category == "face":
        vpgrid:
            at choice_fade
            cols 2
            area (653, 193, 597, 528)
            spacing 25
            scrollbars "vertical"
            mousewheel True
            imagebutton auto "customisation_face_1_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_face", "face_1")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_face_2_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_face", "face_2")] hovered Play("sound", "audio/ui/click2.ogg")
        vpgrid:
            at choice_fade
            cols 2
            area (1339, 153, 180, 780)
            spacing 20
            imagebutton auto "skintone_1_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_17")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_2_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_18")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_3_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_19")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_4_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_20")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_5_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_21")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_6_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_22")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_7_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_23")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_8_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_24")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_9_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_25")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "skintone_10_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_skintone", "cc_26")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
    elif customise_category == "eyes":
        vpgrid:
            at choice_fade
            cols 2
            area (653, 193, 597, 528)
            spacing 25
            scrollbars "vertical"
            mousewheel True
            imagebutton auto "customisation_eyes_1_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_eyes", "eyes 1"), SetVariable("customise_iris", "iris_1")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_eyes_2_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_eyes", "eyes 2"), SetVariable("customise_iris", "iris_2")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_lashes_1_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_lashes", "lashes 0")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_lashes_2_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_lashes", "lashes 1")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_lashes_3_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_lashes", "lashes 2")] hovered Play("sound", "audio/ui/click2.ogg")
        vpgrid:
            at choice_fade
            cols 2
            area (1339, 153, 180, 780)
            spacing 20
            imagebutton auto "palette_1_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_1")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_2_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_2")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_3_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_3")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_4_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_4")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_5_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_5")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_6_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_6")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_7_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_7")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_8_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_8")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_9_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_9")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_10_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_10")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_11_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_11")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_12_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_12")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_13_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_13")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_14_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_14")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_15_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_15")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_16_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_iriscolour", "cc_16")] hovered Play("sound", "audio/ui/click2.ogg")
    elif customise_category == "hair":
        vpgrid:
            at choice_fade
            cols 2
            area (653, 193, 597, 528)
            spacing 25
            scrollbars "vertical"
            mousewheel True
            imagebutton auto "customisation_hair_1_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_hair", "hair_1"), refresh_hair] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_hair_2_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_hair", "hair_2"), refresh_hair] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_hair_3_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_hair", "hair_3"), refresh_hair] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_hair_4_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_hair", "hair_4"), refresh_hair] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_hair_5_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_hair", "hair_5"), refresh_hair] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_hair_6_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_hair", "hair_6"), refresh_hair] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_hair_7_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_hair", "hair_7"), refresh_hair] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_hair_8_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_hair", "hair_8"), refresh_hair] hovered Play("sound", "audio/ui/click2.ogg")
        vpgrid:
            at choice_fade
            cols 2
            area (1339, 153, 180, 780)
            spacing 20
            imagebutton auto "palette_1_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_1")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_2_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_2")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_3_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_3")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_4_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_4")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_5_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_5")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_6_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_6")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_7_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_7")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_8_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_8")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_9_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_9")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_10_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_10")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_11_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_11")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_12_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_12")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_13_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_13")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_14_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_14")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_15_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_15")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "palette_16_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_strandcolour", "cc_16")] hovered Play("sound", "audio/ui/click2.ogg")
        frame:
            at choice_fade
            background Frame(["gui/boxes/frame.png"], 30,30,30,30)
            pos (384,788)
            xysize (432,155)
            has vbox
            align (0.5,0.5)
            text "CUSTOM HAIR LENGTH":
                font "fonts/Orbitron-Black.ttf"
                color "#9d64fd"
                size 25
                align (0.5,0,5)
            vbox:
                align (0.5,0.5)
                spacing -10
                hbox:
                    align (0.5,0,5)
                    spacing 15
                    textbutton _("SHORT") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_length", "short")] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("MEDIUM") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_length", "mid-length")] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("LONG") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_length", "long")] hovered Play("sound", "audio/ui/click1.ogg")
                hbox:
                    align (0.5,0,5)
                    spacing 15
                    textbutton _("BALD") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_length", "bald")] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("HIDDEN") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_length", "hidden")] hovered Play("sound", "audio/ui/click1.ogg")

        frame:
            at choice_fade
            background Frame(["gui/boxes/frame.png"], 30,30,30,30)
            pos (852,788)
            xysize (432,155)
            has vbox
            align (0.5,0.5)
            text "CUSTOM HAIR TEXTURE":
                font "fonts/Orbitron-Black.ttf"
                color "#9d64fd"
                size 25
                align (0.5,0,5)
            vbox:
                align (0.5,0.5)
                spacing -10
                hbox:
                    align (0.5,0.5)
                    spacing 15
                    textbutton _("STRAIGHT") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_texture", "straight")] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("WAVY") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_texture", "wavy")] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("CURLY") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_texture", "curly")] hovered Play("sound", "audio/ui/click1.ogg")
                hbox:
                    align (0.5,0.5)
                    spacing 15
                    textbutton _("COILY") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_texture", "coily")] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("BRAIDED") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_texture", "braided")] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("LOCS") text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("hair_texture", "locs")] hovered Play("sound", "audio/ui/click1.ogg")
    elif customise_category == "body":
        vpgrid:
            at choice_fade
            cols 2
            area (653, 193, 597, 528)
            spacing 25
            scrollbars "vertical"
            mousewheel True
            imagebutton auto "customisation_body_1_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_body", "body 1")] hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "customisation_body_2_%s" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("customise_body", "body 2")] hovered Play("sound", "audio/ui/click2.ogg")
        vpgrid:
            at choice_fade
            cols 2
            area (1339, 153, 180, 780)
            spacing 20
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
    elif customise_category == "misc":
        vbox:
            at choice_fade
            pos (653,193)
            xysize (597,520)
            vbox:
                align (0.5,0.5)
                style_prefix "tempname"
                text "{color=#ff66cb}FULL NAME:{/color} [player] [surname]"
                text "{color=#ff66cb}PRONOUNS:{/color} [they]/[them]"
                text "{color=#ff66cb}AGE:{/color} adult\n"
                if customise_hair == "hair_7":
                    text "{color=#ff66cb}HAIRSTYLE:{/color} [hair_texture], [hair_length]"
                    text "{color=#ff66cb}HAIR COLOUR:{/color} hidden"
                elif hair_length != "bald":
                    text "{color=#ff66cb}HAIRSTYLE:{/color} [hair_texture], [hair_length]"
                    text "{color=#ff66cb}HAIR COLOUR:{/color} [hair_colour]"
                else:
                    text "{color=#ff66cb}HAIRSTYLE:{/color} formerly [hair_texture], now [hair_length]"
                    text "{color=#ff66cb}HAIR COLOUR:{/color} formerly [hair_colour]"
                text "{color=#ff66cb}EYE COLOUR:{/color} [eye_colour]\n"
                text "{color=#ff66cb}OCCUPATION:{/color} librarian\n"
                text "{color=#ff66cb}HOME ADDRESS:{/color} {font=fonts/FlowBlock-Regular.ttf}lol like I'd spoil this information so early on{/font}, Corland Bay\n"
                text "{color=#ff66cb}KNOWN AFFILIATES:{/color} Leon Davis (friend), \"Moth\" (friend), {font=fonts/FlowBlock-Regular.ttf}Ren (future boyfriend){/font}, Violet Garcia (neighbour), Elanor Creston (coworker), Conan O'Rourke (employer), {font=fonts/FlowBlock-Regular.ttf}spoilers, spoiler spoil hehe{/font}\n"
                text "{color=#ff66cb}KNOWN FAMILY:{/color} unknown"

        vpgrid:
            at choice_fade
            cols 2
            area (1339, 153, 180, 780)
            spacing 20
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")
            imagebutton auto "character_null_%s" action NullAction() hovered Play("sound", "audio/ui/click2.ogg")

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), refresh_pronouns, refresh_name, Hide("customcharacter", dissolve)] at amm_button, slideleft anchor (0.5, 0.5) pos (300, 875) hovered Play("sound", "audio/ui/click2.ogg")

################################################################################
## FINALLY... CUSTOM PRONOUNS... OGHHHHHhhhhh
################################################################################
screen custompronouns():
    modal True
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    frame:
        style_prefix "popupblack"
        pos (200,90)
        xsize 800
        vbox:
            xalign 0.5
            hbox:
                xalign 0.5
                text "CHOOSE YOUR PREFERRED PRONOUNS!\n":
                    font "Orbitron-Black.ttf"
                    size 30
            hbox:
                spacing 20
                xalign 0.5
                text "{b}Subjective Pronoun{/b}    {color=#8f8f8f}{size=-5}she | he | they{/size}{/color}":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                button:
                    key_events True
                    ypos -10
                    action they_input.Toggle()
                    input:
                        length 10
                        value they_input         
            hbox:
                spacing 20
                xalign 0.5
                text "{b}Objective Pronoun{/b}    {color=#8f8f8f}{size=-5}her | him | them{/size}{/color}":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                button:
                    key_events True
                    ypos -10
                    action them_input.Toggle()
                    input:
                        length 10
                        value them_input
            hbox:
                spacing 20
                xalign 0.5
                text "{b}Possesive Adjective{/b}    {color=#8f8f8f}{size=-5}her | his | their{/size}{/color}":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                button:
                    key_events True
                    ypos -10
                    action their_input.Toggle()
                    input:
                        length 10
                        value their_input
            hbox:
                spacing 20
                xalign 0.5
                text "{b}Posessive Pronoun{/b}    {color=#8f8f8f}{size=-5}hers | his | theirs{/size}{/color}":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                button:
                    key_events True
                    ypos -10
                    action theirs_input.Toggle()
                    input:
                        length 10
                        value theirs_input
            hbox:
                spacing 20
                xalign 0.5
                text "{b}Reflective Pronoun{/b}    {color=#8f8f8f}{size=-5}herself | himself | themself{/size}{/color}":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                button:
                    key_events True
                    ypos -10
                    action themself_input.Toggle()
                    input:
                        length 14
                        value themself_input
            hbox:
                spacing 20
                xalign 0.5
                text "{b}Word for{/b}    {color=#8f8f8f}{size=-5}woman | man | person{/size}{/color}":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                button:
                    key_events True
                    ypos -10
                    action person_input.Toggle()
                    input:
                        length 12
                        value person_input
            hbox:
                spacing 20
                xalign 0.5
                text "{b}Word for{/b}    {color=#8f8f8f}{size=-5}girlfriend | boyfriend | partner{/size}{/color}":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                button:
                    key_events True
                    ypos -10
                    action partner_input.Toggle()
                    input:
                        length 12
                        value partner_input
            hbox:
                spacing 20
                xalign 0.5
                text "{b}Word for{/b}    {color=#8f8f8f}{size=-5}wife | husband | spouse{/size}{/color}":
                    font "fonts/Assistant-Regular.ttf"
                    size 25
                button:
                    key_events True
                    ypos -10
                    action spouse_input.Toggle()
                    input:
                        length 12
                        value spouse_input
            hbox:
                xalign 0.5
                text "\n{image=gui/misc/divider.png}":
                    text_align 0.5
            hbox:
                xalign 0.5
                text "WHICH IS MORE FITTING?":
                    font "Orbitron-Black.ttf"
                    size 25
            hbox:
                xalign 0.5
                spacing 30
                textbutton _("is") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("are", "is")] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("are") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("are", "are")] hovered Play("sound", "audio/ui/click1.ogg")
            hbox:
                xalign 0.5
                text "she is... | he is... | they are...":
                    font "fonts/Assistant-Regular.ttf"
                    size 20
                    color "#8f8f8f"
    frame:
        style_prefix "popupwhite"
        pos (1030,500)
        vbox:
            align (0.5,0.5)
            xsize 580
            vbox:
                xalign 0.5
                hbox:
                    xalign 0.5
                    text "Hm? Who's that {color=#9d64fd}{b}[gorgeous] [person]{/b}{/color} over there?":
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
                hbox:
                    xalign 0.5
                    text "That's [player!l!c]! {color=#9d64fd}{b}[they!c] [are]{/b}{/color} my {color=#9d64fd}{b}[partner]{/b}{/color}, but…":
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
                hbox:
                    xalign 0.5
                    text "I want {color=#9d64fd}{b}[them]{/b}{/color} to be my {color=#9d64fd}{b}[spouse]{/b}{/color}.":
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
                hbox:
                    xalign 0.5
                    text "Please don't touch {color=#9d64fd}{b}[their]{/b}{/color} book. That's {color=#9d64fd}{b}[theirs]{/b}{/color}.":
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
                hbox:
                    xalign 0.5
                    text "{color=#9d64fd}{b}[they!c]{/b}{/color} told me that {color=#9d64fd}{b}[themself]{/b}{/color}.":
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
            vbox:
                xalign 1.0
                text "- Ren xo":
                    font "fonts/ReenieBeanie-Regular.ttf"
                    color "#141414"
                    size 60
                    text_align 1.0

    frame:
        style_prefix "popupblack"
        pos (1030, 140)
        vbox:
            xsize 580
            xalign 0.5
            hbox:
                xalign 0.5
                text "HOW WOULD YOU LIKE TO BE\nPERCEIVED BY OTHERS?":
                    font "Orbitron-Black.ttf"
                    size 25
                    text_align 0.5
            hbox:
                xalign 0.5
                spacing 30
                textbutton _("feminine") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("gorgeous", "pretty")] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("androgynous") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("gorgeous", "gorgeous")] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("masculine") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("gorgeous", "handsome")] hovered Play("sound", "audio/ui/click1.ogg")

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), refresh_pronouns, Hide ("custompronouns", dissolve)] at amm_button anchor (0.5, 0.5) pos (0.1, 955) hovered Play("sound", "audio/ui/click2.ogg")

################################################################################
## SOCIALS POPUP SCREENS
################################################################################
screen rellegend():
    vbox:
        pos (220, 730)
        text "WIP! I'm still doing something with this":
            outlines [ (absolute(4), "848788", absolute(0), absolute(0)) ]
            font "fonts/VarelaRound-Regular.ttf"
            size 30
            kerning 3
            bold True
            text_align 1.0

screen relcontacts():
    tag menu
    modal True
    viewport:
        at choice_fade
        add "images/bg/other_dark.webp" alpha 0.3
        add "gui/boxes/popup_white.png" pos (300,125)
        vbox:
            align (0.5,0.5)
            spacing 45
            vbox:
                xalign 0.5
                text "{font=fonts/Assistant-Regular.ttf}{color=#141414}wip lol{/color}{/font}" size 35
        imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Hide("relcontacts")] at amm_button anchor (0.5, 0.5)pos (340,930) hovered Play("sound", "audio/ui/click2.ogg")

screen relsecurity():
    tag menu
    modal True
    add "images/bg/other_dark.webp" alpha 0.8 at choice_fade
    
    frame:
        background Frame(["gui/boxes/popup_white.png"], 130, 140, 130, 110)
        padding (20, 60, 20, 20)
        align (0.5,0.5)
        add "gui/socials/camera/securityfeed.webp":
            align (0.5,0.5)
        at choice_fade
    if cam_feed == True:
        if cam_chance in range(7,10):
            add cam_display:
                align (0.5,0.555)
                at choice_fade
        else:
            pass

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), SetVariable("cam_display","None"), SetVariable("cam_feed",False), Hide("relsecurity")] at amm_button anchor (0.5, 0.5)pos (340,930) hovered Play("sound", "audio/ui/click2.ogg")

################################################################################
## cutietutorials (<- knows nothing about make up)
################################################################################
screen reltutorial():
    hbox:
        xpos 5
        ypos 180
        imagebutton auto "gui/ui/text_tut_1_%s.png" action [Play("sound", "audio/ui/accept.ogg"), Hide ("reltutorial", dissolve)] hovered Play("sound", "audio/ui/click2.ogg") at hehehe

################################################################################
## scrolly thang yahhooey
################################################################################
screen newsbanner():
    hbox:
        pos (197,5)
        hbox:
            at newscroll
            text "BREAKING NEWS: REN IS BEST BOY AND THIS IS STILL A WIP.":
                color "#f8f8f8"
                font "fonts/VT323-Regular.ttf"
                size 25
                align (0.5,0.5)

################################################################################
## CHARACTER STATUS THING OMG THIS TOOK 9 YEARS OFF MY LIFE
################################################################################
screen relationmenu():
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    add "gui/bg/ss_base.png"

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button anchor (0.5, 0.5)pos (80,1000) hovered Play("sound", "audio/ui/click2.ogg")

    use newsbanner
    
    add "icon_profile":
        pos (252,100)
        zoom 1.5

    vpgrid:
        cols 2
        area(480,480,480,480)
        align (0.5,0.5)
        pos (750,215)
        spacing -130

        if unlock_profile == True:
            imagebutton auto "gui/socials/apps/profile_%s.png" action [Play("sound", "audio/ui/accept.ogg"), Show("relprofile")] at amm_button anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")
        else:
            imagebutton auto "gui/socials/apps/locked_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), None] anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")
        if unlock_help == True:
            imagebutton auto "gui/socials/apps/help_%s.png" action [Play("sound", "audio/ui/accept.ogg"), If(renpy.get_screen("rellegend"), false=Show("rellegend"), true=Hide("rellegend"))] at amm_button anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")
        else:
            imagebutton auto "gui/socials/apps/locked_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), None] anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")
        if unlock_security == True:
            imagebutton auto "gui/socials/apps/security_%s.png" action [Play("sound", "audio/ui/accept.ogg"), Show("relsecurity")] at amm_button anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")
        else:
            imagebutton auto "gui/socials/apps/locked_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), None] anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")
        if unlock_contacts == True:
            imagebutton auto "gui/socials/apps/locked_%s.png" action [Play("sound", "audio/ui/accept.ogg"), Show("relcontacts")] at amm_button anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")
        else:
            imagebutton auto "gui/socials/apps/locked_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), None] anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")

    vbox:
        xpos 365
        ypos 320
        xalign 0.5
        vbox:
            text "HELLO, [player!u]!":
                size 32
                font "fonts/Orbitron-Black.ttf"
                color "#141414"
        hbox:
            align (0.5,0.5)
            ypos 8
            if persistent.streamermode == True:
                text "FEB 14  ·  02:14":
                    font "fonts/Assistant-Regular.ttf"
                    color "#8f8f8f"
                    size 25
            else:
                timer 0.30 action update_time repeat True
                text "[month!u] [day]  ·  [hours:0=2]:[min:0=2]":
                    font "fonts/Assistant-Regular.ttf"
                    color "#8f8f8f"
                    size 25

    vbox:
        pos (1090,939)
        spacing -18
        textbutton _("> OPEN {b}SOCIALS{/b} TAB") text_style "socials_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("socials_tab", "main")] hovered [Play("sound", "audio/ui/click1.ogg")]
        textbutton _("> OPEN {b}WORK{/b} GROUP CHAT") text_style "socials_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("socials_tab", "work")] hovered [Play("sound", "audio/ui/click1.ogg")] sensitive meet_elanor == True and meet_conan == True
        textbutton _("> OPEN {b}???{/b}") text_style "socials_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("socials_tab", "private")] hovered [Play("sound", "audio/ui/click1.ogg")] sensitive d4_snooping == True

    if socials_tab == "main":
        use chat_main
    if socials_tab == "work":
        use chat_work
    if socials_tab == "private":
        use chat_private

    vbox:
        pos (1762,934)
        textbutton "{size=+50}+{/size}" text_style "socials_buttontext" action NullAction() sensitive False

################################################################################
## LOCATIONS (still part of da relationship screen!!!!!!!)
################################################################################
    fixed:
        ## MOTH LOCATION
        if meet_moth == True:
            add "icon_moth":
                zoom 0.2
                if location_moth == "pier":
                    xpos 500
                    ypos 590
                elif location_moth == "library":
                    xpos 770
                    ypos 730
                elif location_moth == "bluemoss":
                    xpos 770
                    ypos 750
                elif location_moth == "home":
                    xpos 75
                    ypos 500
                elif location_moth == "oh":
                    xpos 860
                    ypos 605
                elif location_moth == "sh":
                    xpos 845
                    ypos 725
                elif location_moth == "random":
                    xpos 650
                    ypos 800
                else:
                    xpos 650
                    ypos 800
        else:
            pass

        ## VIOLET
        if meet_violet == True:
            add "icon_violet":
                zoom 0.2
                if location_violet == "pier":
                    xpos 400
                    ypos 650
                elif location_violet == "library":
                    xpos 725
                    ypos 750
                elif location_violet == "bluemoss":
                    xpos 790
                    ypos 760
                elif location_violet == "home":
                    xpos 850
                    ypos 590
                elif location_violet == "random":
                    xpos 870
                    ypos 970
                elif location_violet == "work":
                    xpos 640
                    ypos 900
                else:
                    xpos 870
                    ypos 970
        else:
            pass

        ## ELANOR
        if meet_elanor == True:
            add "icon_elanor":
                zoom 0.2
                if location_elanor == "pier":
                    xpos 420
                    ypos 635
                elif location_elanor == "library":
                    xpos 750
                    ypos 720
                elif location_elanor == "bluemoss":
                    xpos 730
                    ypos 780
                elif location_elanor == "home":
                    xpos 440
                    ypos 900
                elif location_elanor == "apartment":
                    xpos 835
                    ypos 610
                elif location_elanor == "random":
                    xpos 480
                    ypos 820
                elif location_elanor == "aquarium":
                    xpos 660
                    ypos 780
                else:
                    xpos 480
                    ypos 820
        else:
            pass

        ## REN
        if meet_ren == True:
            add "icon_ren":
                zoom 0.2
                if location_ren == "pier":
                    xpos 460
                    ypos 670
                elif location_ren == "library":
                    xpos 720
                    ypos 710
                elif location_ren == "bluemoss":
                    xpos 830
                    ypos 760
                elif location_ren == "home":
                    xpos 860
                    ypos 730
                elif location_ren == "oh":
                    xpos 820
                    ypos 580
                elif location_ren == "random":
                    xpos 730
                    ypos 750
                elif location_ren == "aquarium":
                    xpos 665
                    ypos 840
                else:
                    xpos 730
                    ypos 750
        else:
            pass

        ## CONAN
        if meet_conan == True:
            add "icon_conan":
                zoom 0.2
                if location_conan == "pier":
                    xpos 405
                    ypos 690
                elif location_conan == "library":
                    xpos 770
                    ypos 700
                elif location_conan == "bluemoss":
                    xpos 720
                    ypos 800
                elif location_conan == "home":
                    xpos 350
                    ypos 880
                elif location_conan == "random":
                    xpos 270
                    ypos 980
                elif location_conan == "work":
                    xpos 773
                    ypos 698
                else:
                    xpos 270
                    ypos 980
        else:
            pass

        ## JAE
        if meet_jae == True:
            add "icon_jae":
                zoom 0.2
                if location_jae == "pier":
                    xpos 500
                    ypos 690
                elif location_jae == "library":
                    xpos 680
                    ypos 750
                elif location_jae == "bluemoss":
                    xpos 780
                    ypos 840
                elif location_jae == "home":
                    xpos 550
                    ypos 580
                elif location_jae == "random":
                    xpos 500
                    ypos 500
                    
                elif location_jae == "street":
                    xpos 730
                    ypos 660
                elif location_jae == "city":
                    xpos 115
                    ypos 500
                else:
                    xpos 730
                    ypos 660
        else:
            pass

        ## LEON
        if meet_leon == True:
            add "icon_leon":
                zoom 0.2
                if location_leon == "pier": 
                    xpos 475
                    ypos 690
                elif location_leon == "library":
                    xpos 695
                    ypos 730
                elif location_leon == "bluemoss":
                    xpos 760
                    ypos 850
                elif location_leon == "home":
                    xpos 570
                    ypos 825
                elif location_leon == "random":
                    xpos 730
                    ypos 920
                elif location_leon == "street":
                    xpos 705
                    ypos 680
                elif location_leon == "aquarium":
                    xpos 630
                    ypos 800
                else:
                    xpos 705
                    ypos 680
        else:
            pass

        ## TEO
        if status_teo == False:
            $ location_teo = "graveyard"
        elif meet_teo == True:
            add "icon_teo":
                zoom 0.2
                if location_teo == "pier":
                    xpos 480
                    ypos 650
                elif location_teo == "library":
                    xpos 750
                    ypos 690
                elif location_teo == "bluemoss":
                    xpos 730
                    ypos 830
                elif location_teo == "home":
                    xpos 185
                    ypos 695
                elif location_teo == "random":
                    xpos 640
                    ypos 720
                elif location_teo == "aquarium":
                    xpos 670
                    ypos 810
                elif location_teo == "graveyard":
                    xpos -100
                    ypos -100
                else:
                    xpos 640
                    ypos 720
        else:
            pass

        ## OLIVIA
        if status_olivia == False:
            $ location_olivia = "graveyard"
        elif meet_olivia == True:
            add "icon_olivia":
                zoom 0.2
                if location_olivia == "pier":
                    xpos 450
                    ypos 755
                elif location_olivia == "library":
                    xpos 705
                    ypos 750
                elif location_olivia == "bluemoss":
                    xpos 800
                    ypos 800
                elif location_olivia == "home":
                    xpos 810
                    ypos 610
                elif location_olivia == "work":
                    xpos 450
                    ypos 755
                elif location_olivia == "random":
                    xpos 620
                    ypos 720
                elif location_olivia == "graveyard":
                    xpos -100
                    ypos -100
                else:
                    xpos 620
                    ypos 720
        else:
            pass

        ## KIARA
        if meet_kiara == True:
            add "icon_kiara":
                zoom 0.2
                if location_kiara == "pier":
                    xpos 390
                    ypos 630
                elif location_kiara == "library":
                    xpos 730
                    ypos 730
                elif location_kiara == "bluemoss":
                    xpos 750
                    ypos 760
                elif location_kiara == "home":
                    xpos 470
                    ypos 900
                elif location_kiara == "oh":
                    xpos 835
                    ypos 600
                elif location_kiara == "random":
                    xpos 610
                    ypos 980
                else:
                    xpos 610
                    ypos 980
        else:
            pass

################################################################################
## CHARACTER ACCOUNTS (still part of da relationship screen!!!!!!!)
################################################################################
screen chat_main():
    frame:
        ## I'm going insane vpgrid's pos won't go in the spot I want and I'm too lazy to do something about it
        pos (1052,100)
        background None
        vpgrid:
            bottom_margin 10
            cols 1
            rows 11
            area(760,790,760,790)
            align (0.4,0.5)
            spacing 19
            scrollbars "vertical"
            mousewheel True

            ## Angel
            fixed:
                xfit True
                yfit True
                frame:
                    background Frame("status_box", 28,28,28,28)
                    padding (40,20,40,20)
                    xsize 580
                    yminimum 107
                    ymaximum 107
                    pos (130,35)
                    if update_angel == "status":
                        text "open the profile app to get started!":
                            font "fonts/VT323-Regular.ttf"
                            color "#141414"
                            size 32
                            align(0.5,0.5)
                            text_align 0.5
                    else:
                        text "[update_angel]":
                            font "fonts/VT323-Regular.ttf"
                            color "#141414"
                            size 32
                            align(0.5,0.5)
                            text_align 0.5
                add "icon_angel":
                    zoom 0.75
                    pos (1,33)
                frame:
                    background None
                    align (1.0,0.0)
                    offset (-30,10)
                    hbox:
                        spacing 10
                        frame:
                            background Frame("socials_angel", 20,20,20,20)
                            padding (15,5,15,5)
                            text "@[username_angel!u]":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 20
                                align (0.5,0.5)
                                text_align 0.5
                        frame:
                            background Frame("socials_black", 20,20,20,20)
                            padding (15,5,15,5)
                            text "[they!u]/[them!u]":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 20
                                align (0.5,0.5)
                                text_align 0.5
                        add "heart_like":
                            align (0.5,0.5)

            ## moth
            if meet_moth == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_moth == True:
                            text "[update_moth]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_moth == True:
                        add "icon_moth":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_moth == True:
                                    background Frame("socials_moth", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_moth!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "THEY/ANY":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_moth == True:
                                vbar value AnimatedValue(affection_moth, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_moth == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_moth >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_moth >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_moth <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

            ## violet
            if meet_violet == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_violet == True:
                            text "[update_violet]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_violet == True:
                        add "icon_violet":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_violet == True:
                                    background Frame("socials_violet", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_violet!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "SHE/HER":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_violet == True:
                                vbar value AnimatedValue(affection_violet, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_violet == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_violet >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_violet >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_violet <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

            ## elanor
            if meet_elanor == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_elanor == True:
                            text "[update_elanor]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_elanor == True:
                        add "icon_elanor":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_elanor == True:
                                    background Frame("socials_elanor", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_elanor!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "SHE/THEY":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_elanor == True:
                                vbar value AnimatedValue(affection_elanor, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_elanor == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_elanor >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_elanor >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_elanor <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

            ## ren
            if meet_ren == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_ren == True:
                            text "[update_ren]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_ren == True:
                        add "icon_ren":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_ren == True:
                                    background Frame("socials_ren", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_ren!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "HE/THEY":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_ren == True:
                                vbar value AnimatedValue(affection_ren, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_ren == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_ren >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_ren >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_ren <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

            ## conan
            if meet_conan == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_conan == True:
                            text "[update_conan]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_conan == True:
                        add "icon_conan":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_conan == True:
                                    background Frame("socials_conan", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_conan!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "HE/THEY":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_conan == True:
                                vbar value AnimatedValue(affection_conan, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_conan == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_conan >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_conan >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_conan <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

            ## jae
            if meet_jae == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_jae == True:
                            text "[update_jae]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_jae == True:
                        add "icon_jae":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_jae == True:
                                    background Frame("socials_jae", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_jae!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "HE/HIM":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_jae == True:
                                vbar value AnimatedValue(affection_jae, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_jae == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_jae >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_jae >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_jae <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

            ## leon
            if meet_leon == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_leon == True:
                            text "[update_leon]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_leon == True:
                        add "icon_leon":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_leon == True:
                                    background Frame("socials_leon", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_leon!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "HE/HIM":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_leon == True:
                                vbar value AnimatedValue(affection_leon, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_leon == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_leon >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_leon >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_leon <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

            ## teo
            if meet_teo == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_teo == True:
                            text "[update_teo]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_teo == True:
                        add "icon_teo":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_teo == True:
                                    background Frame("socials_teo", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_teo!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "HE/HIM":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_teo == True:
                                vbar value AnimatedValue(affection_teo, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_teo == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_teo >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_teo >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_teo <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

            ## olivia
            if meet_olivia == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_olivia == True:
                            text "[update_olivia]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_olivia == True:
                        add "icon_olivia":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_olivia == True:
                                    background Frame("socials_olivia", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_olivia!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "SHE/HER":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_olivia == True:
                                vbar value AnimatedValue(affection_olivia, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_olivia == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_olivia >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_olivia >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_olivia <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"
            ## kiara
            if meet_kiara == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_kiara == True:
                            text "[update_kiara]":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_kiara == True:
                        add "icon_kiara":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_kiara == True:
                                    background Frame("socials_kiara", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_kiara!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "SHE/ANY":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            if status_kiara == True:
                                vbar value AnimatedValue(affection_kiara, affection_total):
                                    minimum (35,30)
                                    maximum (35,30)
                                    left_bar Frame("heart_empty", 35,30)
                                    if status_kiara == False:
                                        right_bar Frame("heart_terminated", 35,30)
                                    elif affection_kiara >= 20:
                                        right_bar Frame("heart_love", 35,30)
                                    elif affection_kiara >= 10:
                                        right_bar Frame("heart_like", 35,30)
                                    elif affection_kiara <= 5:
                                        right_bar Frame("heart_dislike", 35,30)
                                    else:
                                        right_bar Frame("heart_neutral", 35,30)
                            else:
                                add "heart_terminated"

screen chat_private():
    frame:
        ## I'm going insane vpgrid's pos won't go in the spot I want and I'm too lazy to do something about it
        pos (1052,100)
        background None
        vpgrid:
            bottom_margin 10
            cols 1
            rows 4
            area(760,790,760,790)
            align (0.4,0.5)
            spacing 19
            scrollbars "vertical"
            mousewheel True

            fixed:
                xfit True
                yfit True
                frame:
                    background Frame("status_box", 28,28,28,28)
                    padding (40,20,40,20)
                    xsize 580
                    yminimum 107
                    ymaximum 107
                    pos (130,35)
                    text "i smell someone who likes to snoop :p":
                        font "fonts/VT323-Regular.ttf"
                        color "#141414"
                        size 32
                        align(0.5,0.5)
                        text_align 0.5
                add "icon_river":
                    zoom 0.75
                    pos (1,33)
                frame:
                    background None
                    align (1.0,0.0)
                    offset (-30,10)
                    hbox:
                        spacing 10
                        frame:
                            background Frame("socials_river", 20,20,20,20)
                            padding (15,5,15,5)
                            text "@UNSENT_FROM_HEAVEN":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 20
                                align (0.5,0.5)
                                text_align 0.5
                        frame:
                            background Frame("socials_black", 20,20,20,20)
                            padding (15,5,15,5)
                            text "HE/ANY":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 20
                                align (0.5,0.5)
                                text_align 0.5

            fixed:
                xfit True
                yfit True
                frame:
                    background Frame("status_box", 28,28,28,28)
                    padding (40,20,40,20)
                    xsize 580
                    yminimum 107
                    ymaximum 107
                    pos (130,35)
                    text "? wtf is this gc":
                        font "fonts/VT323-Regular.ttf"
                        color "#141414"
                        size 32
                        align(0.5,0.5)
                        text_align 0.5
                add "icon_redacted":
                    zoom 0.75
                    pos (1,33)
                frame:
                    background None
                    align (1.0,0.0)
                    offset (-30,10)
                    hbox:
                        spacing 10
                        frame:
                            background Frame("socials_redacted", 20,20,20,20)
                            padding (15,5,15,5)
                            text "@SLEDGEHACKER":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 20
                                align (0.5,0.5)
                                text_align 0.5
                        frame:
                            background Frame("socials_black", 20,20,20,20)
                            padding (15,5,15,5)
                            text "THEY/HE":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 20
                                align (0.5,0.5)
                                text_align 0.5

            ## olivia
            if meet_olivia == True:
                fixed:
                    xfit True
                    yfit True
                    frame:
                        background Frame("status_box", 28,28,28,28)
                        padding (40,20,40,20)
                        xsize 580
                        yminimum 107
                        ymaximum 107
                        pos (130,35)
                        if status_olivia == True:
                            text "Hiii @UNSENT_FROM_HEAVEN are we still on for tonight? <3":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text "This account has been terminated.":
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                    if status_olivia == True:
                        add "icon_olivia":
                            zoom 0.75
                            pos (1,33)
                    else:
                        add "icon_default":
                            zoom 0.75
                            pos (1,33)
                    frame:
                        background None
                        align (1.0,0.0)
                        offset (-30,10)
                        hbox:
                            spacing 10
                            frame:
                                if status_olivia == True:
                                    background Frame("socials_olivia", 20,20,20,20)
                                else:
                                    background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "@[username_olivia!u]":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                            frame:
                                background Frame("socials_black", 20,20,20,20)
                                padding (15,5,15,5)
                                text "SHE/HER":
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5

screen chat_work():
    frame:
        ## I'm going insane vpgrid's pos won't go in the spot I want and I'm too lazy to do something about it
        pos (1052,100)
        background None
        vpgrid:
            bottom_margin 10
            cols 1
            rows 11
            area(760,790,760,790)
            align (0.4,0.5)
            spacing 19
            scrollbars "vertical"
            mousewheel True

            ## 10chimes
            fixed:
                xfit True
                yfit True
                frame:
                    background Frame("status_box", 28,28,28,28)
                    padding (40,20,40,20)
                    xysize (580,107)
                    pos (130,35)
                    text "Reminder to shut the window in the employee lounge. Thank you.":
                        font "fonts/VT323-Regular.ttf"
                        color "#141414"
                        size 32
                        align(0.5,0.5)
                        text_align 0.5
                add "icon_conan":
                    zoom 0.75
                    pos (1,33)
                frame:
                    background None
                    align (1.0,0.0)
                    offset (-30,10)
                    hbox:
                        spacing 10
                        frame:
                            background Frame("socials_conan", 20,20,20,20)
                            padding (15,5,15,5)
                            text "@[username_conan]":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 19
                                align (0.5,0.5)
                                text_align 0.5
                        frame:
                            background Frame("socials_black", 20,20,20,20)
                            padding (15,5,15,5)
                            text "HE/THEY":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 19
                                align (0.5,0.5)
                                text_align 0.5

            ## cutiesai
            fixed:
                xfit True
                yfit True
                frame:
                    background Frame("status_box", 28,28,28,28)
                    padding (40,20,40,20)
                    xysize (580,107)
                    pos (130,35)
                    text "Day 14 of me making my own visual novel during work hours >:3":
                        font "fonts/VT323-Regular.ttf"
                        color "#141414"
                        size 32
                        align(0.5,0.5)
                        text_align 0.5
                add "icon_cutiesai":
                    zoom 0.75
                    pos (1,33)
                frame:
                    background None
                    align (1.0,0.0)
                    offset (-30,10)
                    hbox:
                        spacing 10
                        frame:
                            background Frame("socials_cutiesai", 20,20,20,20)
                            padding (15,5,15,5)
                            text "@CUTIESAI":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 19
                                align (0.5,0.5)
                                text_align 0.5
                        frame:
                            background Frame("socials_black", 20,20,20,20)
                            padding (15,5,15,5)
                            text "SHE/ANY":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 19
                                align (0.5,0.5)
                                text_align 0.5


            ## 10chimes
            fixed:
                xfit True
                yfit True
                frame:
                    background Frame("status_box", 28,28,28,28)
                    padding (40,20,40,20)
                    xysize (580,107)
                    pos (130,35)
                    text "Has anyone seen my pen? I left it somewhere!":
                        font "fonts/VT323-Regular.ttf"
                        color "#141414"
                        size 32
                        align(0.5,0.5)
                        text_align 0.5
                add "icon_elanor":
                    zoom 0.75
                    pos (1,33)
                frame:
                    background None
                    align (1.0,0.0)
                    offset (-30,10)
                    hbox:
                        spacing 10
                        frame:
                            background Frame("socials_elanor", 20,20,20,20)
                            padding (15,5,15,5)
                            text "@[username_elanor]":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 19
                                align (0.5,0.5)
                                text_align 0.5
                        frame:
                            background Frame("socials_black", 20,20,20,20)
                            padding (15,5,15,5)
                            text "SHE/THEY":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 19
                                align (0.5,0.5)
                                text_align 0.5

            ## 10chimes
            fixed:
                xfit True
                yfit True
                frame:
                    background Frame("status_box", 28,28,28,28)
                    padding (40,20,40,20)
                    xysize (580,107)
                    pos (130,35)
                    text "the way Teo's fat dumpy won't fit through the staff window eoghhh":
                        font "fonts/VT323-Regular.ttf"
                        color "#141414"
                        size 32
                        align(0.5,0.5)
                        text_align 0.5
                add "icon_10chimes":
                    zoom 0.75
                    pos (1,33)
                frame:
                    background None
                    align (1.0,0.0)
                    offset (-30,10)
                    hbox:
                        spacing 10
                        frame:
                            background Frame("socials_10chimes", 20,20,20,20)
                            padding (15,5,15,5)
                            text "@10CHIMES":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 19
                                align (0.5,0.5)
                                text_align 0.5
                        frame:
                            background Frame("socials_black", 20,20,20,20)
                            padding (15,5,15,5)
                            text "ANY/ALL":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 19
                                align (0.5,0.5)
                                text_align 0.5

################################################################################
## splashscreen stuff yehaawww
################################################################################
image cutielogo = "gui/bg/splashscreen.png"

screen over18():
    add "images/bg/other_dark.webp"
    add "peffectp"
    add "glitch_2":
        alpha 0.09
    vbox:
        align (0.5,0.5)
        xsize 1000
        hbox:
            xalign 0.5
            text "WARNING!":
                text_align 0.5
                outlines [ (absolute(7), "362A46", absolute(2), absolute(2)) ]
                font "fonts/Orbitron-Black.ttf"
                size 80
                color "#FF66CB"
                kerning 10

        hbox:
            xalign 0.5
            text "\"14 Days With You\" is a demo for an upcoming horror/romance game, and is intended to be played by those who are 18 and older. Themes will get darker as more \"Days\" are released. Player discretion is advised.\n\n{color=#9d64fd}{b}THIS DEMO INVOLVES:{/b}{/color} mild coarse language, horror, gore, and unsettling themes such as being stalked, violence, death, and murder. It also involves eye-straining text, screen shakes, and the potential to cause seizures for those with photosensitive epilepsy. For the full list of content warnings, please {a=https://cutiesai.com/14dwy}click here{/a}.\n":
                text_align 0.5
                justify True
                outlines [ (absolute(1), "362A46", absolute(0), absolute(0)) ]
                font "fonts/Assistant-Regular.ttf"
                if renpy.variant("mobile"):
                    size 35
                else:
                    size 28
                color "#f8f8f8"

        if renpy.variant("mobile"):
            hbox:
                xalign 0.5
                textbutton _("AGREE AND CONTINUE"):
                    text_style "ss_button"
                    hovered [Play("sound", "audio/ui/click1.ogg")]
                    action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", False), Confirm("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}IMPORTANT!{/font}{/size}{/color}\nConfirm you are {color=#a30b11}{b}18 OR {u}OVER{/u}{/b}{/color} and have\nlooked at the list of content warnings?", yes=MainMenu(confirm=False), no=None, confirm_selected=False)]
        else:
            hbox:
                spacing 30
                xalign 0.5
                hbox:
                    textbutton _("I AM {u}UNDER{/u} 18"):
                        text_style "ss_button"
                        hovered [Play("sound", "audio/ui/click1.ogg")]
                        action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", True), Confirm("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}IMPORTANT!{/font}{/size}{/color}\nConfirm you are {color=#a30b11}{b}{u}UNDER{/u} 18{/b}{/color} and have\n read everything correctly?", Quit(), no=None, confirm_selected=False)]
                hbox:
                    text "|":
                        text_align 0.5
                        outlines [ (absolute(3), "362A46", absolute(0), absolute(0)) ]
                        font "fonts/Assistant-Regular.ttf"
                        size 28
                        color "#f8f8f8"
                hbox:
                    textbutton _("I AM {u}OVER{/u} 18"):
                        text_style "ss_button"
                        hovered [Play("sound", "audio/ui/click1.ogg")]
                        action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", False), Confirm("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}IMPORTANT!{/font}{/size}{/color}\nConfirm you are {color=#a30b11}{b}18 OR {u}OVER{/u}{/b}{/color} and have\n read everything correctly?", yes=Jump("loginscreen"), no=None, confirm_selected=False)]
                hbox:
                    text "|":
                        text_align 0.5
                        outlines [ (absolute(3), "362A46", absolute(0), absolute(0)) ]
                        font "fonts/Assistant-Regular.ttf"
                        size 28
                        color "#f8f8f8"
                hbox:
                    textbutton _("QUIT THE GAME"):
                        text_style "ss_button"
                        hovered [Play("sound", "audio/ui/click1.ogg")]
                        action [Play("sound", "audio/ui/accept.ogg"), Quit()]

################################################################################
## RenPyyyyy Shakeeee Effectttt yippeeee (out of date but whatevaaaa)
## for my own ref: https://www.renpy.org/wiki/renpy/doc/cookbook/Shake_effect
################################################################################
init:
    python:
        import math
        class Shaker(object):  
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                } 

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                self.start = [ self.anchors.get(i, i) for i in start ]
                self.dist = dist
                self.child = child
                
            def __call__(self, t, sizes):             
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor          
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):
            move = Shaker(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
            time,
            child,
            add_sizes=True,
            **properties)

        Shake = renpy.curry(_Shake)

init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

################################################################################
## yuhhh
################################################################################
screen deletedata():
    tag menu
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    
    vbox:
        align (0.2,0.5)
        spacing 30
        frame:
            at slidedown
            style_prefix "popupblack"
            xsize 700
            #xysize (750,400)
            has vbox
            align (0.5,0.5)
            spacing 10
            text "INSTALLED DLCS":
                font "fonts/Orbitron-Black.ttf"
                color "#FF66CB"
                size 50
                align (0.5,0.5)
            vbox:
                align (0.5,0.5)
                spacing 20
                vbox:
                    align (0.5,0.5)
                    text "{image=14NWY symbol} \"14 Nights With You\" DLC pack":
                        size 30
                        color "#f8f8f8"
                        align (0.5,0.5)
                    text "Adds additional 18+/NSFW content to the game. Please view the Itch page for more information. {a=https://cutiesai.itch.io/14nightswithyou}Click here to download{/a}.":
                        size 20
                        color "#8f8f8f"
                        text_align 0.5
                        align (0.5,0.5)
                hbox:
                    align (0.5,0.5)
                    spacing 40
                    hbox:
                        align (0.0,0.5)
                        spacing 10
                        if persistent.dlc_14nightswithyou_type == "free":
                            add "gui/button/checkbox_selected_foreground.png":
                                align (0.5,0.5)
                        else:
                            add "gui/button/checkbox_foreground.png":
                                align (0.5,0.5)
                        text "FREE version":
                            size 25
                            color "#f8f8f8"
                    hbox:
                        align (0.0,0.5)
                        spacing 10
                        if persistent.dlc_14nightswithyou_type == "paid":
                            add "gui/button/checkbox_selected_foreground.png":
                                align (0.5,0.5)
                        else:
                            add "gui/button/checkbox_foreground.png":
                                align (0.5,0.5)
                        text "PAID version":
                            size 25
                            color "#f8f8f8"

        frame:
            at slideup
            style_prefix "popupwhite"
            xysize (700,180)
            text "Make sure to only install {u}one{/u} pack! The FREE and PAID versions cannot be installed at the same time.":
                size 20
                color "#141414"
                text_align 0.5
                align (0.5,0.5)

    frame:
        at slideright
        style_prefix "popupblack"
        xsize 700
        align (0.8,0.5)
        has vbox
        align (0.5,0.5)
        vbox:
            align (0.5,0.5)
            text "DATA MANAGEMENT":
                font "fonts/Orbitron-Black.ttf"
                color "#FF66CB"
                size 50
                xalign 0.5
            text "More options will show up here once you unlock them\n":
                size 23
                xalign 0.5
                textalign 0.5
        vbox:
            align (0.5,0.5)
            spacing 30
            vbox:
                align (0.5,0.5)
                textbutton _("{size=+5}DELETE ALL SAVE FILES{/size}"):
                    xalign 0.5
                    text_style "cutietext"
                    text_color "#9d64fd"
                    text_hover_color "#FF66CB"
                    hovered [Play("sound", "audio/ui/click1.ogg")]
                    action Confirm("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}WOAH, WAIT!{/font}{/size}{/color}\nAre you sure you want to {color=#a30b11}{b}DELETE{/b}{/color} all of\nyour save files? You can't undo this!", delete_saves)
                text "This will delete all your save files and autosaves.\nThis {u}will not{/u} delete any of your stored data!":
                    color "#8f8f8f"
                    size 20
                    textalign 0.5
            vbox:
                align (0.5,0.5)
                textbutton _("{size=+5}DELETE STORED DATA / START FRESH{/size}"):
                    xalign 0.5
                    text_style "cutietext"
                    text_color "#9d64fd"
                    text_hover_color "#FF66CB"
                    hovered [Play("sound", "audio/ui/click1.ogg")]
                    if persistent.warningscreen == True:
                        action [Function(delete_persistent), Confirm("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}WOAH, WAIT!{/font}{/size}{/color}\nAre you sure you want to {color=#a30b11}{b}DELETE{/b}{/color} all of\nyour data? This does not include\nsave files!", yes=Return(), no=None), SetVariable("persistent.warningscreen", True)]
                    else:
                        action Confirm("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}WOAH, WAIT!{/font}{/size}{/color}\nAre you sure you want to {color=#a30b11}{b}DELETE{/b}{/color} all of\nyour data? This does not include\nsave files!", [delete_persistent, renpy.utter_restart])
                text "This will delete {u}all{/i} stored data (including your gallery and achievements) and reset the game back to its default state.":
                    color "#8f8f8f"
                    size 20
                    xalign 0.5
                    textalign 0.5
            if persistent.menumissing == True:
                vbox:
                    align (0.5,0.5)
                    textbutton _("{size=+5}RESET REN.EXE{/size}"):
                        xalign 0.5
                        text_style "cutietext"
                        text_color "#850106"
                        text_hover_color "#FF66CB"
                        hovered [Play("sound", "audio/ui/click1.ogg")]
                        action Confirm("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}WOAH, WAIT!{/font}{/size}{/color}\nAre you sure you want to {color=#a30b11}{b}DISMISS{/b}{/color}\nRen's help? You can't undo this!", yes=[SetVariable("persistent.menumissing", False), renpy.utter_restart], no=SetVariable("persistent.menumissing", True))
                    text "Don't need Ren's help? This will bring him back to the\nmain menu screen.\n\n{b}Ren will still remember you!{/b}":
                        color "#8f8f8f"
                        size 20
                        textalign 0.5

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideleft anchor (0.5, 0.5) pos (170,0.71) hovered Play("sound", "audio/ui/click2.ogg")

################################################################################
## GIRL MATH GIRL MATH GIRL MATH!!!! (it was not, in fact, girl math)
################################################################################
label girlmath:
    ## Is today the day I learn how to use append and remove????? No lmao
    if status_moth == False:
        $ affection_moth = 0
    if status_violet == False:
        $ affection_violet = 0
    if status_elanor == False:
        $ affection_elanor = 0
    if status_conan == False:
        $ affection_conan = 0
    if status_jae == False:
        $ affection_jae = 0
    if status_leon == False:
        $ affection_leon = 0
    if status_teo == False:
        $ affection_teo = 0
    if status_olivia == False:
        $ affection_olivia = 0
    if status_kiara == False:
        $ affection_kiara = 0

    $ highest_affinity = max(affection_moth, affection_violet, affection_elanor, affection_conan, affection_jae, affection_leon, affection_teo, affection_olivia, affection_kiara)

    if affection_violet == highest_affinity:
        $ li_name = "Violet"
        $ li_they = "she"
        $ li_them = "her"
        $ li_hair = "silver"
        $ li_are = "is"
    if affection_moth == highest_affinity:
        $ li_name = "Moth"
        $ li_they = "they"
        $ li_them = "them"
        $ li_hair = "navy"
        $ li_are = "are"
    if affection_elanor == highest_affinity:
        $ li_name = "Elanor"
        $ li_they = "she"
        $ li_them = "her"
        $ li_hair = "light blonde"
        $ li_are = "is"
    if affection_conan == highest_affinity:
        $ li_name = "Conan"
        $ li_they = "he"
        $ li_them = "him"
        $ li_hair = "red"
        $ li_are = "is"
    if affection_jae == highest_affinity:
        $ li_name = "Jae"
        $ li_they = "he"
        $ li_them = "him"
        $ li_hair = "dyed blonde"
        $ li_are = "is"
    if affection_leon == highest_affinity:
        $ li_name = "Leon"
        $ li_they = "he"
        $ li_them = "him"
        $ li_hair = "brown"
        $ li_are = "is"
    if affection_teo == highest_affinity:
        $ li_name = "Teo"
        $ li_they = "he"
        $ li_them = "him"
        $ li_hair = "dyed green"
        $ li_are = "is"
    if affection_olivia == highest_affinity:
        $ li_name = "Olivia"
        $ li_they = "she"
        $ li_them = "her"
        $ li_hair = "black"
        $ li_are = "is"
    if affection_kiara == highest_affinity:
        $ li_name = "Kiara"
        $ li_they = "she"
        $ li_them = "her"
        $ li_hair = "dark blonde"
        $ li_are = "is"

################################################################################
## QUESTION STUFF
################################################################################
screen screenput():
    style_prefix "popupblack"
    modal True
    frame:
        align (0.5,0.5)
        xysize (900, 300)
        vbox:
            align (0.5,0.5)
            text "[input_prompt]":
                font "fonts/Orbitron-Regular.ttf"
                color "#f8f8f8"
                size 40
            button:
                xalign 0.5
                action input_actual.Toggle()
                input:
                    length 30
                    value input_actual
    imagebutton auto "gui/ui/forward_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button anchor (0.5, 0.5) pos (0.72, 0.62) hovered Play("sound", "audio/ui/click2.ogg")

################################################################################
## thank you Ren discord bot code that I made I love you Ren discord bot code that I made
################################################################################
default renchatterlist = [
    "Have you eaten today?",
    f"{persistent.game_open} is my new favourite number now!\nThat's how many times you've opened my game! >///<",
    "Make sure to drink some water, Angel!",
    "I've missed you!",
    f"Aaaand... That's number {persistent.game_open}! ...Hm? Oh, I'm keeping\ntrack of how many times you've opened my game!",
    "LOVEYOULOVEYOULOVEYOULOVEYOULOVEYOU!",
    "Honey it's 2AM, time to play some 14DWY",
    "I love you, Angel!",
    "Oh? Back so soon?",
    "One bad gloop and she do what I yoinky",
    "I was just thinking about you, Angel.",
    "Were you thinking about me? H-Haaah...",
    "...I can see you ^^",
    "Want to read a book together?",
    "Taking some time off? Can I join you? ^^",
    "Want to eat lunch with me today?",
    "Have any book recommendations for me?",
    "Do you still like Haruko? ...Just checking.",
    "Ignore Leon and hang out with me today!",
    "Hello, Angel.",
    "You're not talking to other yanderes, are you?",
    "I heard there's a 14DWY Discord bot that\ndoes the exact same thing as me...",
    "Do you want to read a book together? Just the two of us?",
    "...Want to touch my hair? ^^",
    "*CHUUUUUUU* I've missed you, Angel!",
    "You must really like pressing buttons, huh? :)",
    "Were you thinking about me too? Is that why you're here?",
    "Oh, look! The cutest person in the entire UNIVERSE is here!",
]

default mainmenulist = [
    "If you're enjoying the demo so far, please\nconsider {a=https://cutiesai.itch.io/14dayswithyou/rate?source=game}giving it a rating{/a} on itch.io!",
    "Want to help translate the demo?\nJoin the {a=https://discord.gg/14dayswithyou}official Discord server{/a} and ask!",
    "Check the {a=https://cutiesai.itch.io/14dayswithyou}official Itch page{/a} for all\nthe latest demo updates!",
    "If you'd like to support me, please\nconsider checking out my {a=https://ko-fi.com/cutiesai}Ko-Fi{/a} page!",
]

################################################################################
## popup for the load menu
################################################################################
screen updatewarning():  
    frame:
        at slideright
        pos (0.5,0.5)
        align (0.5,0.5)
        style_prefix "popupwhite"
        vbox:
            maximum (500, 60)
            align (0.5, 0.5)
            text "[player!u], WAIT!":
                font "fonts/Orbitron-Black.ttf"
                color "#FF66CB"
                size 40
                align (0.5,0.5)
            text "Did you recently update to Day 5.5? If so, older save files might not work and may lead to errors. Please start a new game to avoid any issues.\n":
                color "#141414"
                font "fonts/Assistant-Regular.ttf"
                size 25
                textalign 0.5
            textbutton _("DISMISS") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("persistent.fdwyupdate", False), Hide("updatewarning")] hovered Play("sound", "audio/ui/click1.ogg") align (0.5,0.5)

################################################################################
## Playtester screen
################################################################################
screen playtester():
    modal True
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    frame:
        style_prefix "popupwhite"
        align (0.5,0.5)
        vbox:
            align (0.5,0.5)
            spacing 30
            vbox:
                align (0.5,0.5)
                text "Toggle playtest mode:":
                    font "fonts/Orbitron-Black.ttf"
                    size 35
                    color "#9d64fd"
                    text_align 0.5
                hbox:
                    align (0.5,0.5)
                    spacing 80
                    textbutton _("YES") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("playtest", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("NO") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("playtest", False)] hovered Play("sound", "audio/ui/click1.ogg")
            vbox:
                align (0.5,0.5)
                text "Toggle meetings:":
                    font "fonts/Orbitron-Black.ttf"
                    size 35
                    color "#9d64fd"
                    text_align 0.5
                    xalign 0.5
                grid 5 2:
                    align (0.5,0.5)
                    textbutton _("REN") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_ren", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("MOTH") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_moth", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("VIOLET") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_violet", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("ELANOR") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_elanor", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("CONAN") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_conan", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("JAE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_jae", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("LEON") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_leon", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("TEO") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_teo", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("OLIVIA") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_olivia", True)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("KIARA") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("meet_kiara", True)] hovered Play("sound", "audio/ui/click1.ogg")
            vbox:
                align (0.5,0.5)
                text "Toggle deaths:":
                    font "fonts/Orbitron-Black.ttf"
                    size 35
                    color "#9d64fd"
                    text_align 0.5
                hbox:
                    align (0.5,0.5)
                    spacing 80
                    textbutton _("OLIVIA") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("status_olivia", False)] hovered Play("sound", "audio/ui/click1.ogg")
                    textbutton _("TEO") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("status_teo", False)] hovered Play("sound", "audio/ui/click1.ogg")
            vbox:
                align (0.5,0.5)
                text "Immediately jump to:":
                    font "fonts/Orbitron-Black.ttf"
                    size 35
                    color "#9d64fd"
                    text_align 0.5
                    xalign 0.5
                grid 3 5:
                    align (0.5,0.5)
                    textbutton _("DAY 1") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("day1")] hovered Play("sound", "audio/ui/click1.ogg") align (1.0,0.5)
                    textbutton _("18+ SCENE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("day1_wahooscene")] hovered Play("sound", "audio/ui/click1.ogg") align (0.5,0.5)
                    textbutton _("DEAD END") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("deadend1")] hovered Play("sound", "audio/ui/click1.ogg") align (0.0,0.5)
                    textbutton _("DAY 2") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), Jump("day2")] hovered Play("sound", "audio/ui/click1.ogg") align (1.0,0.5)
                    textbutton _("18+ SCENE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("day2_wahooscene")] hovered Play("sound", "audio/ui/click1.ogg") align (0.0,0.5)
                    textbutton _("DEAD END") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("deadend2")] hovered Play("sound", "audio/ui/click1.ogg") align (0.0,0.5)
                    textbutton _("DAY 3") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("day3")] hovered Play("sound", "audio/ui/click1.ogg") align (1.0,0.5)
                    textbutton _("18+ SCENE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("day3_wahooscene")] hovered Play("sound", "audio/ui/click1.ogg") align (0.5,0.5)
                    textbutton _("DEAD END") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("deadend3")] hovered Play("sound", "audio/ui/click1.ogg") align (0.0,0.5)
                    textbutton _("DAY 4") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("day4")] hovered Play("sound", "audio/ui/click1.ogg") align (1.0,0.5)
                    textbutton _("18+ SCENE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("day4_wahooscene")] hovered Play("sound", "audio/ui/click1.ogg") align (0.5,0.5)
                    textbutton _("DEAD END") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("deadend4")] hovered Play("sound", "audio/ui/click1.ogg") align (0.0,0.5)
                    textbutton _("DAY 5") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True),  Jump("day5")] hovered Play("sound", "audio/ui/click1.ogg") align (1.0,0.5)
                    textbutton _("18+ SCENE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("day5_wahooscene")] hovered Play("sound", "audio/ui/click1.ogg") align (0.5,0.5)
                    textbutton _("DEAD END") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("quick_menu", True), SetVariable ("_skipping", True), Jump("deadend5")] hovered Play("sound", "audio/ui/click1.ogg") align (0.0,0.5)

################################################################################
## grahhhhh
################################################################################
init -20 python:
    import discord_rpc
    import time

    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))

label before_main_menu:
    python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('1410181514519515256', callbacks=callbacks, log=False)
        start = time.time()
        print(start)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'I can see you, Angel...',
                'start_timestamp': start,
                'large_image_key': '14dwy_logo'
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

    return

################################################################################
## INIT AND DEFINE STUFF IDK HOW TO ORGANISE
################################################################################
init python:
    ## popup text
    layout.DELETE_SAVE = _("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}[player!u], WAIT!{/font}{/size}{/color}\nAre you sure you want to delete\nthis save file?")
    layout.OVERWRITE_SAVE = _("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}[player!u], WAIT!{/font}{/size}{/color}\nDo you want to overwrite this save?\nYou won't get it back!")
    layout.LOADING = _("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}[player!u], WAIT!{/font}{/size}{/color}\nLoading will lose any unsaved progress!\nDo you still want to continue?")
    layout.QUIT = _("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}[player!u], WAIT!{/font}{/size}{/color}\nAre you sure you want to quit the game?\nYou will lose any unsaved progress!")
    layout.MAIN_MENU = _("{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}[player!u], WAIT!{/font}{/size}{/color}\nReturn to the main menu?\nYou will lose any unsaved progress!")

    ## music stuff
    renpy.music.register_channel("ambience", "ambience", True)

    ## time/clock stuff
    import time
    import datetime
    from datetime import datetime

    hours = 0
    min = 0
    day = 0
    month = 0
    year = 0

    def update_time():
        time = datetime.now()
        globals() ["hours"] = time.hour
        globals() ["min"] = time.minute
        globals() ["day"] = time.day
        globals() ["month"] = time.strftime('%b')
        globals() ["year"] = time.year
        renpy.restart_interaction()

    def delete_persistent():
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)
        return

    def delete_saves():
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
        return

    def renvoid_tag(tag, argument, contents):
        global colour_fade
        sc_size = int(argument)
        gl_size = int(argument)
        return [
                (renpy.TEXT_TAG, u"glitch={}".format(gl_size)),
                (renpy.TEXT_TAG, u"sc={}".format(sc_size)),
                (renpy.TEXT_TAG, "font=VT323-Regular.ttf"),
                (renpy.TEXT_TAG, "size=45"),
                (renpy.TEXT_TAG, u"color={}".format(colour_fade)),
            ] + contents + [
                (renpy.TEXT_TAG, "/color"),
                (renpy.TEXT_TAG, "/size"),
                (renpy.TEXT_TAG, "/font"),
                (renpy.TEXT_TAG, u"/sc"),
                (renpy.TEXT_TAG, u"/glitch"),
            ]
    config.custom_text_tags["renvoid"] = renvoid_tag

    def refresh_username_angel():
        global username_angel
        global username_angel_input
        if username_angel == "":
            username_angel = persistent.corupdate_user
        elif persistent.corupdate_user == "":
            username_angel_input = VariableInputValue("username_angel", default=False)
            username_angel = "AOG_FAN"
        else: username_angel = username_angel

    def refresh_status_angel():
        global update_angel
        global update_angel_input
        if update_angel == "status":
            update_angel == "Test open the profile app to get started!"
        elif update_angel == "":
            update_angel_input = VariableInputValue("update_angel", default=False)
            update_angel = "status"
        else:
            update_angel = update_angel
    
    def refresh_name():
        global player
        global player_fl
        global ch_angel
        if player == "":
            player = "Angel"
        player_fl = player[:1].upper()
        ch_angel = player

    def refresh_hair():
        global customise_hair
        global hair_length
        global hair_texture
        global player_hair
        if customise_hair == "hair_1":
            hair_texture = "straight"
            hair_length = "short"
            player_hair = "visible"
        if customise_hair == "hair_2":
            hair_texture = "straight"
            hair_length = "short"
            player_hair = "visible"
        if customise_hair == "hair_3":
            hair_texture = "wavy"
            hair_length = "long"
            player_hair = "visible"
        if customise_hair == "hair_4":
            hair_texture = "braided"
            hair_length = "long"
            player_hair = "visible"
        if customise_hair == "hair_5":
            hair_texture = "locs"
            hair_length = "mid-length"
            player_hair = "visible"
        if customise_hair == "hair_6":
            hair_texture = "coily"
            hair_length = "mid-length"
            player_hair = "visible"
        if customise_hair == "hair_7":
            hair_texture = "straight"
            hair_length = "hidden"
            player_hair = "hidden"
        if customise_hair == "hair_8":
            hair_texture = "straight"
            hair_length = "bald"
            player_hair = "hidden"

    ## the way I did this is geninely embarrassing don't look at this section
    def assign_colours():
        global customise_strandcolour
        global curstomise_iriscolour
        global hair_colour
        global eye_colour
        global eye_colour

        if customise_strandcolour == "cc_1":
            hair_colour = hc_1
        if customise_strandcolour == "cc_2":
            hair_colour = hc_2
        if customise_strandcolour == "cc_3":
            hair_colour = hc_3
        if customise_strandcolour == "cc_4":
            hair_colour = hc_4
        if customise_strandcolour == "cc_5":
            hair_colour = hc_5
        if customise_strandcolour == "cc_6":
            hair_colour = hc_6
        if customise_strandcolour == "cc_7":
            hair_colour = hc_7
        if customise_strandcolour == "cc_8":
            hair_colour = hc_8
        if customise_strandcolour == "cc_9":
            hair_colour = hc_9
        if customise_strandcolour == "cc_10":
            hair_colour = hc_10
        if customise_strandcolour == "cc_11":
            hair_colour = hc_11
        if customise_strandcolour == "cc_12":
            hair_colour = hc_12
        if customise_strandcolour == "cc_13":
            hair_colour = hc_13
        if customise_strandcolour == "cc_14":
            hair_colour = hc_14
        if customise_strandcolour == "cc_15":
            hair_colour = hc_15
        if customise_strandcolour == "cc_16":
            hair_colour = hc_16

        if customise_iriscolour == "cc_1":
            eye_colour = ec_1
        if customise_iriscolour == "cc_2":
            eye_colour = ec_2
        if customise_iriscolour == "cc_3":
            eye_colour = ec_3
        if customise_iriscolour == "cc_4":
            eye_colour = ec_4
        if customise_iriscolour == "cc_5":
            eye_colour = ec_5
        if customise_iriscolour == "cc_6":
            eye_colour = ec_6
        if customise_iriscolour == "cc_7":
            eye_colour = ec_7
        if customise_iriscolour == "cc_8":
            eye_colour = ec_8
        if customise_iriscolour == "cc_9":
            eye_colour = ec_9
        if customise_iriscolour == "cc_10":
            eye_colour = ec_10
        if customise_iriscolour == "cc_11":
            eye_colour = ec_11
        if customise_iriscolour == "cc_12":
            eye_colour = ec_12
        if customise_iriscolour == "cc_13":
            eye_colour = ec_13
        if customise_iriscolour == "cc_14":
            eye_colour = ec_14
        if customise_iriscolour == "cc_15":
            eye_colour = ec_15
        if customise_iriscolour == "cc_16":
            eye_colour = ec_16

    def refresh_pronouns():
        global they
        global them
        global their
        global theirs
        global themself
        global person
        global baby
        global partner
        global spouse
        global are
        global gorgeous
        if pronoun == "female":
            they = "she"
            them = "her"
            their = "her"
            theirs = "hers"
            themself = "herself"
            baby = "girl"
            person = "woman"
            are = "is"
            partner = "girlfriend"
            spouse = "wife"
            gorgeous = "pretty"
        elif pronoun == "male":
            they = "he"
            them = "him"
            their = "his"
            theirs = "his"
            themself = "himself"
            baby = "boy"
            person = "man"
            are = "is"
            partner = "boyfriend"
            spouse = "husband"
            gorgeous = "handsome"
        elif pronoun == "neutral":
            they = "they"
            them = "them"
            their = "their"
            theirs = "theirs"
            themself = "themself"
            baby = "person"
            person = "person"
            are = "are"
            partner = "partner"
            spouse = "spouse"
            gorgeous = "gorgeous"
        else:
            they = they
            them = them
            their = their
            theirs = theirs
            themself = themself
            baby = "person"
            person = person
            partner = partner
            spouse = spouse
            are = are
            gorgeous = gorgeous
    
    def refresh_custom_angel():
        global player
        global surname
        global they
        global them
        global their
        global theirs
        global themself
        global person
        global baby
        global partner
        global spouse
        global are
        global gorgeous
        if custom_angel == False:
            player = "Angel"
            surname = "Mentior"
            they = "they"
            them = "them"
            their = "their"
            theirs = "theirs"
            themself = "themself"
            baby = "person"
            person = "person"
            are = "are"
            partner = "partner"
            spouse = "spouse"
            gorgeous = "gorgeous"
