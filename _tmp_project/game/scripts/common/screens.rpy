################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=False)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=False)
    color "#9d64fd"
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb_offset -12

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile, yminimum=104, xminimum=24, ymaximum=104, xmaximum=24)
    thumb_offset -12

style slider:
    ysize gui.slider_size
    xsize 450
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    thumb_offset -30

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/boxes/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        fixed:
            align (0.5,0.7)
            xysize (1190,190)
            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"
            text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage()

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label

style window:
    background Image("gui/ui/textbox.png", xalign=0.5,yalign=1.0,xpos=0.5,ypos=1.0)
    xfill True
    yfill True
    align (0.5,1.0)
    xysize (1920,450)

style namebox:
    align (0.0,-0.1)

style say_label:
    outlines [ (absolute(4), "#362A46", absolute(0), absolute(0)) ]
    font "fonts/Orbitron-Black.ttf"
    size 40
    kerning 5
    ypos -15
    align (0.0,0.5)

style say_dialogue:
    color "#f8f8f8"
    justify True
    line_leading 5
    #text_align 0.5
    outlines [ (absolute(3), "#362A46", absolute(0), absolute(0)) ]
    font "fonts/VarelaRound-Regular.ttf"
    size 30
    align (0.0,0.0)


##    xpos gui.dialogue_xpos
##    xsize gui.dialogue_width
##    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    font "fonts/Assistant-Regular.ttf"
    size 30
    bold True
    color "#FD64CC"
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    add "images/bg/other_dark.webp" alpha 0.3 at choice_fade
    add "triangles_light" alpha 0.1
    if choice_style == "default":
        style_prefix "choice"
        vbox:
            align (0.98,0.8)
            anchor (0.98,0.8)
            for i in items:
                textbutton i.caption action i.action at choice_hov
            at choice_fade
    elif choice_style == "box":
        style_prefix "twochoice"
        vpgrid:
            align (0.5,0.5)
            spacing 30
            cols 2
            for i in items:
                textbutton i.caption action i.action #at choice_hov
            at choice_fade
    else:
        style_prefix "choice"
        vbox:
            for i in items:
                textbutton i.caption action i.action at choice_hov
            at choice_fade

transform choice_hov: 
    on hover: 
        align (0.98,0.8)
        anchor (0.98,0.8)
        linear 0.3 zoom 1.1
    on idle: 
        align (0.98,0.8)
        anchor (0.98,0.8)
        linear 0.3 zoom 1.0
    on hide:
        align (0.98,0.8)
        anchor (0.98,0.8)
        linear 1.0 alpha 0.0

transform choice_fade:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style twochoice_vbox is hbox
style twochoice_button is button
style twochoice_button_text is button_text


style choice_vbox:
    spacing 20

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound ("audio/ui/click1.ogg")
    activate_sound ("audio/ui/choice.ogg")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

style twochoice_vbox:
    align (0.5,0.5)
    anchor (0.5,0.5)

style twochoice_button is default:
    properties gui.button_properties("twochoice_button")
    hover_sound ("audio/ui/click1.ogg")
    activate_sound ("audio/ui/choice.ogg")

style twochoice_button_text is default:
    properties gui.button_text_properties("twochoice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100
    if quick_menu:
        hbox:
            at slideup
            align (0.5,1.0)
            add "gui/ui/textbox_b.png"
        hbox:
            at slideup
            style_prefix "quick"
            align (1.0,1.0)
            imagebutton auto "gui/qm/qs_back_%s.png" xpos -275 ypos -19 action [Play("sound", "audio/ui/blip.ogg"), Rollback()] hovered [Play("sound", "audio/ui/click2.ogg")] tooltip "back"
            imagebutton auto "gui/qm/qs_history_%s.png" xpos -250 ypos -19 action [Play("sound", "audio/ui/blip.ogg"), ShowMenu('history')] hovered [Play("sound", "audio/ui/click2.ogg")] tooltip "history"
            imagebutton auto "gui/qm/qs_skip_%s.png" xpos -225 ypos -19 action [Play("sound", "audio/ui/blip.ogg"), Skip()] alternate Skip(fast=True, confirm=True) hovered [Play("sound", "audio/ui/click2.ogg")] tooltip "skip"
            imagebutton auto "gui/qm/qs_auto_%s.png" xpos -200 ypos -19 action [Play("sound", "audio/ui/blip.ogg"), Preference("auto-forward", "toggle")] hovered [Play("sound", "audio/ui/click2.ogg")] tooltip "autoplay"
            imagebutton auto "gui/qm/qs_save_%s.png" xpos -175 ypos -19 action [Play("sound", "audio/ui/blip.ogg"), ShowMenu('save')] hovered [Play("sound", "audio/ui/click2.ogg")] tooltip "save"
            imagebutton auto "gui/qm/qs_load_%s.png" xpos -150 ypos -19 action [Play("sound", "audio/ui/blip.ogg"), ShowMenu('load')] hovered [Play("sound", "audio/ui/click2.ogg")] tooltip "load"
            imagebutton auto "gui/qm/qs_settings_%s.png" xpos -125 ypos -19 action [Play("sound", "audio/ui/blip.ogg"), ShowMenu('preferences')] hovered [Play("sound", "audio/ui/click2.ogg")] tooltip "settings"
            imagebutton auto "gui/qm/qs_quit_%s.png" xpos -100 ypos -19 action [Play("sound", "audio/ui/blip.ogg"), MainMenu()] hovered [Play("sound", "audio/ui/click2.ogg")] tooltip "quit" 

        $ tooltip = GetTooltip()
        if tooltip:
            nearrect:
                focus "tooltip"
                prefer_top True
                frame:
                    background Frame("socials_black", 20,20,20,20) align (0.5,0.5)
                    padding (15,5,15,5)
                    margin (0,0,0,40)
                    text tooltip


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")


        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")



## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu
    $ username_angel = persistent.corupdate_user
    if persistent.menumissing == True:
        on 'show' action Play("music", "audio/bgm/Notice Me.ogg")
        add "bg/other_red.webp":
            at choice_fade
        add "de_1":
            alpha 0.3
        add "fade_quickbar":
            align (0.5,1.0) 
            at choice_fade, slideright
    else:
        on 'show' action Play("music", "audio/bgm/Fairy Voice.ogg")
        add "bg/desktop_bg.webp":
            at choice_fade
        add "peffect"
        add "gui/ui/textbox_b.png":
            align (0.5,1.0)
            at choice_fade, slideup
        fixed:
            xysize (1100,660)
            anchor (0.5,0.5)
            pos (0.6,0.45)
            add "menu_ren":
                align (0.5,0.5)
                at slideright
            imagebutton auto "gui/ui/more_%s.png" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("renchatter", renpy.random.choice(renchatterlist)), ToggleVariable("welcome_chatter")] align (0.98,0.98) hovered Play("sound", "audio/ui/click2.ogg") at choice_fade, slideright
        frame:
            background Frame(["status_box"], gui.choice_button_borders)
            pos (650,240)
            xysize (400,130)
            text "[mainmenutext]":
                    font "fonts/Assistant-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
            at slidedown

                
        if welcome_chatter == True:
            frame:
                background Frame(["gui/boxes/bubble_black.png"], gui.choice_button_borders)
                padding (50,15,50,15)
                pos (0.81,0.725)
                anchor (1.0,1.0)
                text "[renchatter]":
                    text_align 0.5
                at choice_fade, slideright

    vbox:
        align (1.0,0.0)
        if renpy.variant("mobile"):
            text "Android [version_number]":
                size 25
                xalign 1.0
                outlines [ (1, "141414", absolute(0), absolute(0)) ]
        else:
            text "Version [version_number]":
                size 25
                xalign 1.0
                outlines [ (1, "141414", absolute(0), absolute(0)) ]
        if persistent.dlc_14nightswithyou == True:
            if persistent.dlc_14nightswithyou_type == "paid":
                if persistent.dlc_14nwy_comp == True:
                    text "[[DLC] 14 Nights With You ({})".format(persistent.dlc_14nightswithyou_type.upper()):
                        size 18
                        textalign 1.0
                        xalign 1.0
                        outlines [ (1, "141414", absolute(0), absolute(0)) ]
                else:
                    text "14 Nights With You DLC installed but isn't compatible\nwith this version! Please download the latest versions.":
                        size 18
                        textalign 1.0
                        xalign 1.0
                        outlines [ (1, "141414", absolute(0), absolute(0)) ]
            else:
                text "[[DLC] 14 Nights With You ({})".format(persistent.dlc_14nightswithyou_type.upper()):
                    size 18
                    xalign 1.0
                    outlines [ (1, "141414", absolute(0), absolute(0)) ]
        else:
            text "No DLCs installed":
                size 18
                xalign 1.0
                outlines [ (1, "141414", absolute(0), absolute(0)) ]

    ## quit
    imagebutton auto "gui/qm/qs_quit_%s.png" action [Play("sound", "audio/ui/blip.ogg"), Quit(confirm=not main_menu)] hovered [Play("sound", "audio/ui/click2.ogg")] align (0.97,0.983) at choice_fade, slideup

    hbox:
        pos (0.02,0.957)
        if persistent.menumissing == True:
            text "TRy t0 st{glitch=5}{font=Orbitron-Black.ttf}{color=#f8f8f8}{size=23}@R t A N3{/size}{/color}{/font}{/glitch}W sa{glitch=7}{font=Orbitron-Black.ttf}{color=#f8f8f8}{size=23}V E{/size}{/color}{/font}{/glitch}, {font=fonts/Orbitron-Regular.ttf}ANg 3L. ..{/font}":
                    font "fonts/Orbitron-Black.ttf"
                    color "#f8f8f8"
                    size 23
        else:
            text "WELCOME BACK, {font=fonts/Orbitron-Regular.ttf}[username_angel!u].{/font}":
                font "fonts/Orbitron-Black.ttf"
                color "#f8f8f8"
                size 23
        at choice_fade, slideup
    
    hbox:
        pos (0.88,0.958)
        if persistent.streamermode == True:
            text "FEB 14  ·  02:14":
                font "fonts/Assistant-Regular.ttf"
                color "#f8f8f8"
                size 20
        elif persistent.menumissing == True:
            text "10SHI  ·  77:77777777":
                xoffset -40
                font "fonts/Assistant-Regular.ttf"
                color "#f8f8f8"
                size 20
        else:
            timer 0.30 action update_time repeat True
            text "[month!u] [day]  ·  [hours:0=2]:[min:0=2]":
                font "fonts/Assistant-Regular.ttf"
                color "#f8f8f8"
                size 20
        at choice_fade, slideup

    ## good LORT this is ugly
    grid 2 5:
        spacing 40
        align (0.05,0.25)
        at slideleft
        if persistent.menumissing == True:
            vbox:
                align (0.5,0.5)
                imagebutton auto "fade_folder_%s"  action [Play("sound", "audio/ui/accept.ogg"), refresh_username_angel, Start()] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "14DWY.exe":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#f8f8f8"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#141414", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "fade_folder_alt_%s"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("load")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "L 0ad":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#f8f8f8"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#141414", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "fade_folder_alt_%s"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("deletedata")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "mANA9e D@t A":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#f8f8f8"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#141414", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "fade_folder_alt_%s"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("preferences")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "s3tTI NG5":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#f8f8f8"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#141414", absolute(0), absolute(0)) ]
        else:
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/ui/folder_pink_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), refresh_username_angel, Start()] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "14DaysWithYou":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/ui/folder_purple_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("about")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "Credits":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/ui/folder_purple_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("load")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "Load":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/socials/links/socials_discord_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), OpenURL("https://discord.gg/14dayswithyou")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "Discord":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/ui/folder_purple_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("album")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "Gallery":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/socials/links/socials_twitter_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), OpenURL("https://twitter.com/14DaysWithYou")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "Twitter":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/ui/folder_purple_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("preferences")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "Settings":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/socials/links/socials_tumblr_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), OpenURL("https://tumblr.com/14dayswithyou")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "Tumblr":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/ui/folder_purple_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("deletedata")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "Manage Data":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/socials/links/socials_extra_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), OpenURL("https://cutiesai.com")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text "cutiesai":
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]

    if persistent.menumissing == True:
        vbox:
            align (0.8,0.6)
            spacing 20
            text "====-       :----\n+=+++=====------=-====\n===++++======-===+-=====\n====+++++++====+*+=======\n====+++++++++=+**+======-\n--===+++++++++**+======-\n-=====+*****##*+=+===-\n-===++**##***++=====\n=++++++++++=====\n--===++=====\n-===+===\n-=":
                size 50
                font "fonts/VT323-Regular.ttf"
                line_spacing -2
                kerning 4
                align (0.5,0.5)
                text_align 0.5
                color "#850106"

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    #if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.game_menu_background
    else:
        add gui.game_menu_background

    vbox:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    frame:
        style_prefix "popupblack"
        xsize 800
        align (0.5,0.5)
        at slidedown
        vbox:
            align (0.5,0.5)
            text "{size=+30}{color=#f8f8f8}CREDITS!{/color}{/size}" style "popupbox_text_pink"
            text "BGM & glitch SFX: {a=http://yacft.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Yuli Audio Craft{/size}{/color}{/font}{/a}" style "popupbox_text_pink"
            text "Nature & ambience SFX: {a=https://pixabay.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Pixabay{/size}{/color}{/font}{/a}" style "popupbox_text_pink"
            text "Background stock images: {a=https://www.pexels.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Pexels{/size}{/color}{/font}{/a}" style "popupbox_text_pink"
            text "Kinetic text tags & shaders: {a=https://wattson.itch.io}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Wattson{/size}{/color}{/font}{/a}" style "popupbox_text_pink"
            text "Discord rich presence: {a=https://arianeb.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Ariane Barnes{/size}{/color}{/font}{/a}" style "popupbox_text_pink"
            text "Game engine: {font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Ren'Py [renpy.version_only]{/size}{/color}{/font}" style "popupbox_text_pink"
            text "{color=#9d64fd}Everything else:{/color} {a=https://cutiesai.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Saint (cutiesai){/size}{/color}{/font}{/a}" style "popupbox_text_pink"
            text "\n{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}And a big thank you to those who have\nsupported the demo!{/size}{/color}{/font}" style "popupbox_text_pink"

    add "images/misc/ur honor hes baby.png":
        zoom 0.3
        pos (1200,500)
        at slideright

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideup anchor (0.5, 0.5)pos (485,830) hovered Play("sound", "audio/ui/click2.ogg")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    add "gui/misc/popup_decor_top.png":
        align (0.2,0.1)
        at slideleft
    add "gui/misc/popup_decor_bottom.png":
        align (0.8,0.9)
        at slideright
    style_prefix "popupblack"

    frame:
        align (0.5,0.5)
        at slidedown
        has vbox
        hbox:
            xalign 0.5
            spacing 5
            text "{color=#9d64fd}SAVE{/color} FILES | ":
                font "fonts/Orbitron-Black.ttf"
                size 65
                color "#f8f8f8"
                align (0.5,0.5)
            hbox:
                yoffset 17
                for i in range(1, 15):
                    textbutton str(i) action FilePage(i)
                text " · ":
                    yalign 0.5
                textbutton _("QUICKSAVES") action FilePage("quick")
        grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{color=#ff66cb}{b}SAVED{/b}{/color} | {#file_time}%B %d, %H:%M"), empty=_("ERR0R: EMPTY FILE!")):
                            style "slot_time_text"
                            ypos 20
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
    
    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideup anchor (0.5, 0.5)pos (230,920) hovered Play("sound", "audio/ui/click2.ogg")


screen load():
    tag menu
    if persistent.warningscreen == True:
        use gamewarning()
    else:
        add "gui/bg/menu_bg_chara.png"
        add "triangles_light"
        add "gui/misc/popup_decor_top.png":
            align (0.2,0.1)
            at slideleft
        add "gui/misc/popup_decor_bottom.png":
            align (0.8,0.9)
            at slideright
        style_prefix "popupblack"

        frame:
            align (0.5,0.5)
            at slidedown
            has vbox
            hbox:
                xalign 0.5
                spacing 5
                text "{color=#9d64fd}LOAD{/color} FILES | ":
                    font "fonts/Orbitron-Black.ttf"
                    size 65
                    color "#f8f8f8"
                    align (0.5,0.5)
                hbox:
                    yoffset 17
                    for i in range(1, 15):
                        textbutton str(i) action FilePage(i)
                    text " · ":
                        yalign 0.5
                    textbutton _("QUICKSAVES") action FilePage("quick")
            grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"
                    spacing gui.slot_spacing
                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1
                        button:
                            action FileAction(slot)
                            has vbox
                            add FileScreenshot(slot) xalign 0.5
                            text FileTime(slot, format=_("{color=#ff66cb}{b}READY TO LOAD!{/b}{/color} | {#file_time}%B %d, %H:%M"), empty=_("ERR0R: EMPTY FILE!")):
                                style "slot_time_text"
                                ypos 20
                            text FileSaveName(slot):
                                style "slot_name_text"
                            key "save_delete" action FileDelete(slot)
        
        imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideup anchor (0.5, 0.5)pos (230,920) hovered Play("sound", "audio/ui/click2.ogg")
    if persistent.fdwyupdate == True and persistent.warningscreen == False:
        use updatewarning()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    top_margin 11

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
screen preferences():
    tag menu
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    add "gui/bg/menu_base.png" at slidedown

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideup anchor (0.5, 0.5) pos (369,255) hovered Play("sound", "audio/ui/click2.ogg")
    imagebutton auto "gui/ui/quit_%s.png" action [Play("sound", "audio/ui/blip.ogg"), Quit(confirm=True)] at amm_button, slideup anchor (0.5, 0.5) pos (369,370) hovered Play("sound", "audio/ui/click2.ogg")

    viewport:
        style_prefix "slider"
        area (540, 280, 540, 280)
        mousewheel True
        scrollbars "vertical"
        pos (470,205)
        at slidedown
        frame:
            background None
            xsize 500
            padding (20,0,20,0)
            vbox:
                spacing 40
                vbox:
                    text "MUSIC VOLUME":
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value Preference("music volume")
                vbox:
                    text "AMBIENCE VOLUME":
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value MixerValue("ambience")
                vbox:
                    text "SOUND VOLUME":
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value Preference("sound volume")
                vbox:
                    text "DIALOGUE SPEED":
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value Preference("text speed")
                vbox:
                    text "AUTOPLAY SPEED":
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value Preference("auto-forward time")

    if renpy.variant("pc"):
        vbox:
            xysize (399,399)
            pos (1074,190)
            at slidedown
            vbox:
                align (0.5,0.5)
                spacing 10
                text "SCREEN DISPLAY":
                        font "fonts/Orbitron-Black.ttf"
                        size 30
                        color "#9D64FD"
                        text_align 1.0
                hbox:
                    style_prefix "radio"
                    align (0.5,0.5)
                    spacing 40
                    imagebutton:
                        idle "gui/chara/screen_windows_idle.png"
                        hover "gui/chara/screen_windows_hover.png"
                        selected_idle "gui/chara/screen_windows_selected.png"
                        selected_hover "gui/chara/screen_windows_selected.png"
                        action [Preference("display", "window"), Play("sound", "audio/ui/accept.ogg")] hovered [Play("sound", "audio/ui/click2.ogg")]
                    imagebutton:
                        idle "gui/chara/screen_fullscreen_idle.png"
                        hover "gui/chara/screen_fullscreen_hover.png"
                        selected_idle "gui/chara/screen_fullscreen_selected.png"
                        selected_hover "gui/chara/screen_fullscreen_selected.png"
                        action [Preference("display", "fullscreen"), Play("sound", "audio/ui/accept.ogg")] hovered [Play("sound", "audio/ui/click2.ogg")]
            vbox:
                align (0.8,0.5)
                ypos 80
                spacing 15
                vbox:
                    style_prefix "check"
                    spacing 5
                    textbutton _("skip all the text") action [Play("sound", "audio/ui/click.ogg"), Preference("skip", "toggle")] hovered [Play("sound", "audio/ui/click2.ogg")]
                    textbutton _("skip after choices") action [Play("sound", "audio/ui/click.ogg"), Preference("after choices", "toggle")] hovered [Play("sound", "audio/ui/click2.ogg")]
                    textbutton _("streamer mode") action [Play("sound", "audio/ui/click.ogg"), ToggleVariable("persistent.streamermode", True)] hovered [Play("sound", "audio/ui/click2.ogg")]
        if renpy.variant("mobile"):
            vbox:
                xysize (399,399)
                pos (1078,180)
                label _("Dialogue Options")
            vbox:
                xpos 1420
                ypos 720
                spacing 25
                style_prefix "check"
                textbutton _("skip all the text") action [Play("sound", "audio/ui/click.ogg"), Preference("skip", "toggle")] hovered [Play("sound", "audio/ui/click2.ogg")]
                textbutton _("skip after choices") action [Play("sound", "audio/ui/click.ogg"), Preference("after choices", "toggle")] hovered [Play("sound", "audio/ui/click2.ogg")]
            hbox:
                add "gui/misc/hearts.png":
                    zoom 0.6
                    xpos 1520
                    ypos 840

    fixed:
        pos (927,653)
        xysize (523,282)
        at slidedown
        hbox:
            align (0.5,0.5)
            text "still a wip hehe":
                    font "fonts/Orbitron-Regular.ttf"
                    size 25
                    color "#141414"
                    text_align 1.0
            

    add "images/misc/just a silly littol guy.png":
        zoom 0.9
        pos (540,600)
        at slideleft

    fixed:
        at slideleft
        drag:
            pos (452,520)
            drag_raise True
            draggable True
            add "gui/misc/stickynote.png"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    ysize gui.slider_size

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 500


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu
    predict False
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    frame:
        at slidedown
        align 0.5,0.5
        xysize (1000,740)
        style_prefix "popupblack"
    viewport id "hist":
        at slidedown
        area (650, 260, 900, 630)
        align (0.5,0.55)
        yinitial 1.0
        draggable False
        mousewheel True
        scrollbars "vertical"
        vbox:
            for h in _history_list:
                if h.who:
                    label h.who:
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                            text_size 40
                            text_bold True
                            top_margin 30

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                frame background None bottom_margin 10 right_margin 30:
                    text "> [what]"

                if not _history_list:
                    label _("The dialogue history is empty.")
    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideup anchor (0.5, 0.5) pos(0.2,0.799) hovered Play("sound", "audio/ui/click2.ogg")

define gui.history_allow_tags = { "alt", "noalt", "color", "b", "i", "ch" }


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):
    ## Ensure other screens do not get input while this screen is displayed.
    zorder 200
    style_prefix "confirm"
    add "images/bg/other_dark.webp" alpha 0.8 at choice_fade
    add "triangles_light" alpha 0.05 at choice_fade
    add "gui/misc/popup_decor_top.png" align (0.5,0.5) offset (0,-120) at slideleft, choice_fade
    add "gui/misc/popup_decor_bottom.png" align (0.5,0.5) offset (0,180) at slideright, choice_fade
    frame:
        at slideup, choice_fade
        vbox:
            spacing 30
            xsize 450
            hbox:
                align (0.5,0.5)
                label _(message):
                    align (0.5,0.5)
                    style "confirm_prompt"
            hbox:
                align (0.5,0.5)
                spacing 100
                textbutton _("YES") action yes_action
                textbutton _("NO") action no_action
    add "gui/misc/hearts.png" pos (1160, 600) at slidedown, choice_fade

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/boxes/popup_black.png", 121, 47)
    padding (50, 95, 50, 50)
    align (0.5,0.5)

style confirm_prompt_text:
    font "fonts/Assistant-Regular.ttf"
    size 25
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    font "fonts/Orbitron-Black.ttf"
    size 25
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 9
            text _("WE ZOOMIN BOIS"):
                outlines [(absolute(2), "#141414", absolute(0), absolute(0))]
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos 1025
    background Frame("misc/blank.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("misc/blank.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/boxes/frame.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            align (0.5,1.0)
            add "gui/ui/textbox_b.png"
        hbox:
            spacing 30
            align (0.5,0.5)
            pos (0.73,0.973)
            textbutton _("BACK") action Rollback()
            textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("AUTO") action Preference("auto-forward", "toggle")
            textbutton _("HISTORY") action ShowMenu("history")
            textbutton _("SAVE") action ShowMenu("save")
            textbutton _("LOAD") action ShowMenu("load")
            textbutton _("MENU") action ShowMenu("preferences")

        #hbox:
        #    spacing 20
        #   align (0.5,0.5)
        #    pos (0.85,0.97)
        #    add "gui/ui/textbox_b.png"
        #    textbutton _("BACK") action Rollback()
        #    textbutton _("HISTORY") action ShowMenu("history")
        #    textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True)
        #    textbutton _("AUTO") action Preference("auto-forward", "toggle")
        #    textbutton _("MENU") action ShowMenu()


style window:
    variant "small"
    background Image("gui/phone/textbox.png", ypos=1.0, xalign=0.5, yalign=1.0)

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    thumb_offset -30

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
