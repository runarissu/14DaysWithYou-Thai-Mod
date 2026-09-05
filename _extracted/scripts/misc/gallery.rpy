################################################################################
# RenPy documentation my beloved
################################################################################
init python:
    g = Gallery()

    g.button("D1_library")
    g.condition("persistent.cg_d1_library")
    g.unlock_image("CG D1_LIBRARY")

    g.button("D2_rain")
    g.condition("persistent.cg_d2_rain")
    g.unlock_image("CG D2_RAIN")

    g.button("D3_manga")
    g.condition("persistent.cg_d3_manga")
    g.unlock_image("CG D3_MANGA")

    g.button("D4_aquarium")
    g.condition("persistent.cg_d4_aquarium")
    g.unlock_image("CG D4_AQUARIUM")

    g.button("D5_beach")
    g.condition("persistent.cg_d5_beach")
    g.unlock_image("CG D5_BEACH")

    g.button("D5_alley")
    g.condition("persistent.cg_d5_alleyway1")
    g.unlock_image("CG D5_ALLEYWAY1")
    g.condition("persistent.cg_d5_alleyway2")
    g.unlock_image("CG D5_ALLEYWAY2")

    g.button("DE_3_1")
    g.condition("persistent.cg_de1")
    g.unlock_image("de_1")

    g.button("DE_3_2")
    g.condition("persistent.cg_de2")
    g.unlock_image("de_2")

    g.button("DE_3_3")
    g.condition("persistent.cg_de3")
    g.unlock_image("de_3")

    g.button("D1_NSFW")
    g.condition("persistent.cg_d1_nsfw1")
    g.unlock_image("CG D1_NSFW1")
    g.condition("persistent.cg_d1_nsfw2")
    g.unlock_image("CG D1_NSFW2")
    g.condition("persistent.cg_d1_nsfw3")
    g.unlock_image("CG D1_NSFW3")

    g.button("D2_NSFW")
    g.condition("persistent.cg_d2_nsfw1")
    g.unlock_image("CG D2_NSFW1")

    g.button("D3_NSFW")
    g.condition("persistent.cg_d3_nsfw1")
    g.unlock_image("CG D3_NSFW1")

    g.button("D4_NSFW")
    g.condition("persistent.cg_d4_nsfw1")
    g.unlock_image("CG D4_NSFW1")

    g.button("D5_NSFW")
    g.condition("persistent.cg_d5_nsfw1")
    g.unlock_image("CG D5_NSFW1")

screen album():
    tag menu
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    add "gui/bg/gallery_base.png" at slidedown

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideup anchor (0.5, 0.5) pos (110, 760) hovered Play("sound", "audio/ui/click2.ogg")
    imagebutton auto "gui/ui/more_%s.png" action [Play("sound", "audio/ui/blip.ogg"), Show("deletedata")] at amm_button,slideup anchor (0.5, 0.5) pos (110, 880) hovered Play("sound", "audio/ui/click2.ogg")

    vbox:
        pos (482,130)
        xysize (400,165)
        spacing -80
        at slidedown
        vbox:
            align (0.5,0.5)
            text "REN'S HAIR IS...":
                font "fonts/Orbitron-Black.ttf"
                size 36
                color "#141414"
        hbox:
            align (0.5,0.5)
            spacing 30
            textbutton _("SHORT") text_style "gallery_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("ren_hair", "short")] hovered [Play("sound", "audio/ui/click1.ogg")] ypos -5
            textbutton _("MEDIUM") text_style "gallery_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("ren_hair", "normal")] hovered [Play("sound", "audio/ui/click1.ogg")] ypos -5
            textbutton _("LONG") text_style "gallery_buttontext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("ren_hair", "long")] hovered [Play("sound", "audio/ui/click1.ogg")] ypos -5

    viewport:
        area (747,204,747,204)
        pos (101,351)
        draggable False
        mousewheel True
        scrollbars "vertical"
        at slidedown
        vbox:
            spacing 5
            if gallery_day == "01":
                if persistent.d1_ending_gooding == True:
                    text "- {s}Make it to the next Day{/s}" style "notepad"
                else:
                    text "- Make it to the next Day" style "notepad"
                if persistent.d1_badending == True:
                    text "- {s}Obtain a Dead End{s}" style "notepad"
                else:
                    text "- Obtain a Dead End" style "notepad"
                if persistent.d1_inviteren == True:
                    text "- {s}Invite a stranger to your place{/s}" style "notepad"
                else:
                    text "- Invite a stranger to your place" style "notepad"
                if persistent.d1_sleepoutside == True:
                    text "- {s}Make Ren sleep on your couch{/s}" style "notepad"
                else:
                    text "- Make Ren sleep on your couch" style "notepad"
                if persistent.d1_blocknumber == True:
                    text "- {s}Block Ren's number{/s}" style "notepad"
                else:
                    text "- Block Ren's number" style "notepad"
            if gallery_day == "02":
                if persistent.d2_ending_gooding == True:
                    text "- {s}Make it to the next Day{/s}" style "notepad"
                else:
                    text "- Make it to the next Day" style "notepad"
                if persistent.d2_badending == True:
                    text "- {s}Obtain a Dead End{/s}" style "notepad"
                else:
                    text "- Obtain a Dead End" style "notepad"
                if persistent.d2_visitren == True:
                    text "- {s}Visit Ren's apartment{/s}" style "notepad"
                else:
                    text "- Visit Ren's apartment" style "notepad"
                if persistent.d2_visitangel == True:
                    text "- {s}Go back to your apartment with your date{/s}" style "notepad"
                else:
                    text "- Go back to your apartment with your date" style "notepad"
                if persistent.d2_killolivia == True:
                    text "- {s}Learn about someone's death{/s}" style "notepad"
                else:
                    text "- Learn about someone's death" style "notepad"
            if gallery_day == "03":
                if persistent.d3_ending_gooding == True:
                    text "- {s}Make it to the next Day{/s}" style "notepad"
                else:
                    text "- Make it to the next Day" style "notepad"
                if persistent.d3_badending == True:
                    text "- {s}Obtain a Dead End{/s}" style "notepad"
                else:
                    text "- Obtain a Dead End" style "notepad"
                if persistent.d3_declinedate == True:
                    text "- {s}Decline someone's proposition{/s}" style "notepad"
                else:
                    text "- Decline someone's proposition" style "notepad"
                if persistent.d3_meetmoth == True:
                    text "- {s}Talk to your online bestie{/s}" style "notepad"
                else:
                    text "- Talk to your online bestie" style "notepad"
                if persistent.d3_inviteover == True:
                    text "- {s}Invite someone to your apartment{/s}" style "notepad"
                else:
                    text "- Invite someone to your apartment" style "notepad"
                if persistent.d3_scareren == True:
                    text "- {s}Try and scare Ren{/s}" style "notepad"
                else:
                    text "- Try and scare Ren" style "notepad"
            if gallery_day == "04":
                if persistent.d4_ending_gooding == True:
                    text "- {s}Make it to the next Day{/s}" style "notepad"
                else:
                    text "- Make it to the next Day" style "notepad"
                if persistent.d4_badending == True:
                    text "- {s}Obtain a Dead End{/s}" style "notepad"
                else:
                    text "- Obtain a Dead End" style "notepad"
                if persistent.d4_visitangel == True:
                    text "- {s}Go home before the storm hits{/s}" style "notepad"
                else:
                    text "- Go home before the storm hits" style "notepad"
                if persistent.d4_snooparound == True:
                    text "- {s}Snoop around Ren's apartment{/s}" style "notepad"
                else:
                    text "- Snoop around Ren's apartment" style "notepad"
                if persistent.d4_killteo == True:
                    text "- {s}Learn about someone's death{/s}" style "notepad"
                else:
                    text "- Learn about someone's death" style "notepad"
                if persistent.d4_icecream == True:
                    text "- {s}Get some ice-cream with your childhood friend{/s}" style "notepad"
                else:
                    text "- Get some ice-cream with your childhood friend" style "notepad"
            if gallery_day == "05":
                if persistent.d5_ending_gooding == True:
                    text "- {s}Make it to the next Day{/s}" style "notepad"
                else:
                    text "- Make it to the next Day" style "notepad"
                if persistent.d5_badending == True:
                    text "- {s}Obtain a Dead End{/s}" style "notepad"
                else:
                    text "- Obtain a Dead End" style "notepad"
                if persistent.d5_visitviolet == True:
                    text "- {s}Ask your neighbour for some help{/s}" style "notepad"
                else:
                    text "- Ask your neighbour for some help" style "notepad"
                if persistent.d5_dismissren == True:
                    text "- {s}Ask Ren to leave you alone{/s}" style "notepad"
                else:
                    text "- Ask Ren to leave you alone" style "notepad"
                if persistent.d5_visitren == True:
                    text "- {s}Visit Ren's apartment{/s}" style "notepad"
                else:
                    text "- Visit Ren's apartment" style "notepad"
                if persistent.d5_kickfigure == True:
                    text "- {s}Kick someone in the leg{/s}" style "notepad"
                else:
                    text "- Kick someone in the leg" style "notepad"

    fixed:
        pos (87,156)
        xysize (360,95)
        at slidedown
        grid 7 2:
            spacing 15
            align (0.5,0.5)
            textbutton "01" text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("gallery_day", "01")] hovered [Play("sound", "audio/ui/click1.ogg")]
            textbutton "02" text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("gallery_day", "02")] hovered [Play("sound", "audio/ui/click1.ogg")]
            textbutton "03" text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("gallery_day", "03")] hovered [Play("sound", "audio/ui/click1.ogg")]
            textbutton "04" text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("gallery_day", "04")] hovered [Play("sound", "audio/ui/click1.ogg")]
            textbutton "05" text_style "popup_button" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("gallery_day", "05")] hovered [Play("sound", "audio/ui/click1.ogg")]
            textbutton "06" text_style "popup_button2" action NullAction()
            textbutton "07" text_style "popup_button2" action NullAction()
            textbutton "08" text_style "popup_button2" action NullAction()
            textbutton "09" text_style "popup_button2" action NullAction()
            textbutton "10" text_style "popup_button2" action NullAction()
            textbutton "11" text_style "popup_button2" action NullAction()
            textbutton "12" text_style "popup_button2" action NullAction()
            textbutton "13" text_style "popup_button2" action NullAction()
            textbutton "14" text_style "popup_button2" action NullAction()

    ## this is the most godawful coding I've ever done
    if persistent.terminal_unlocked == False:
        frame:
            xysize (614,290)
            pos (244,680)
            background None
            at slidedown
            vbox:
                align (0.5,0.5)
                spacing 10
                vbox:
                    align (0.5,0.5)
                    spacing 3
                    vbox:
                        align (0.5,0.5)
                        text "USERNAME":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 40
                                align (0.5,0.5)
                                text_align 0.5
                                kerning 5
                    vbox:
                        align (0.5,0.5)
                        frame:
                            xysize (247,37)
                            background Frame(["socials_offblack"], 20,20,20,20)
                            padding (15,5,15,5)
                            button:
                                key_events True
                                xalign 0.5
                                action gallery_username_input.Toggle()
                                input:
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                                    kerning 5
                                    bold False
                                    value gallery_username_input
                                    pixel_width 200
                vbox:
                    align (0.5,0.5)
                    spacing 3
                    vbox:
                        align (0.5,0.5)
                        text "PASSWORD":
                                font "fonts/VT323-Regular.ttf"
                                color "#f8f8f8"
                                size 40
                                align (0.5,0.5)
                                text_align 0.5
                                kerning 5
                    vbox:
                        align (0.5,0.5)
                        frame:
                            xysize (247,37)
                            background Frame(["socials_offblack"], 20,20,20,20)
                            padding (15,5,15,5)
                            button:
                                key_events True
                                xalign 0.5
                                action gallery_password_input.Toggle()
                                input:
                                    font "fonts/VT323-Regular.ttf"
                                    color "#f8f8f8"
                                    size 20
                                    align (0.5,0.5)
                                    text_align 0.5
                                    kerning 5
                                    bold False
                                    value gallery_password_input
                                    pixel_width 200
            vbox:
                align (1.0,1.0)
                if gallery_username == "ren.exe" and gallery_password == "Passw0rd_777":
                    textbutton ">>" text_style "terminal_button" action SetVariable("persistent.terminal_unlocked", True) at choice_fade
                elif gallery_username == "sledgehacker" and gallery_password == "Passw0rd_777":
                    textbutton ">>" text_style "terminal_button" action OpenURL("https://www.youtube.com/watch?v=dQw4w9WgXcQ") at choice_fade
    else:
        frame:
            at slidedown
            xysize (614,290)
            pos (244,680)
            background None
            viewport:
                draggable False
                mousewheel True
                scrollbars "vertical"
                at choice_fade
                vbox:
                    if persistent.fact_name == True:
                        text "{color=#FF66CB}{size=+5}NAME:{/size}{/color} REN ({font=FlowBlock-Regular.ttf}LMAO YOU_THOUGHT{/font})" style "terminal_button"
                    else:
                        text "{color=#FF66CB}{size=+5}NAME:{/size}{/color}{font=FlowBlock-Regular.ttf} REN (LMAO YOU_THOUGHT){/font}" style "terminal_button"
                    if persistent.fact_dob == True:
                        text "{color=#FF66CB}{size=+5}DOB:{/size}{/color} ???" style "terminal_button"
                    else:
                        text "{color=#FF66CB}{size=+5}DOB:{/size}{/color}{font=FlowBlock-Regular.ttf} 00/00/XXXX{/font}" style "terminal_button"
                    if persistent.fact_job == True:
                        text "{color=#FF66CB}{size=+5}OCCUPATION:{/size}{/color} FREELANCE PROGRAMMER" style "terminal_button"
                    else:
                        text "{color=#FF66CB}{size=+5}OCCUPATION:{/size}{/color}{font=FlowBlock-Regular.ttf} FREELANCE PROGRAMMER{/font}" style "terminal_button"
                    ## unlockable stuff (surely there's an easier way to do this?????? lawd)
                    text "{color=#FF66CB}{size=+5}\nKNOWN FACTS:{/size}{/color}" style "terminal_button"
                    if persistent.fact_tempermentshy == True:
                        text "- TIMID AND AWKWARD, LIKE HARUKO FROM \"ATTACK ON GIANTS\"" style "terminal_button"
                    else:
                        text "- {font=FlowBlock-Regular.ttf}TIMID AND AWKWARD, LIKE HARUKO FROM \"ATTACK ON GIANTS\"{/font}" style "terminal_button"
                    if persistent.fact_mannerism1 == True:
                        text "- SCRATCHES AT JAW WHEN UNSURE OR UNCOMFORTABLE" style "terminal_button"
                    else:
                        text "- {font=FlowBlock-Regular.ttf}SCRATCHES AT JAW WHEN UNSURE OR UNCOMFORTABLE{/font}" style "terminal_button"
                    if persistent.fact_mannerism2 == True:
                        text "- PICKS AT SLEEVES WHEN ANXIOUS" style "terminal_button"
                    else:
                        text "- {font=FlowBlock-Regular.ttf}PICKS AT SLEEVES WHEN ANXIOUS{/font}" style "terminal_button"
                    if persistent.fact_food == True:
                        text "- FAVOURITE FOOD IS STRAWBERRY SWEETROLL" style "terminal_button"
                    else:
                        text "- {font=FlowBlock-Regular.ttf}FAVOURITE FOOD IS STRAWBERRY SWEETROLL{/font}" style "terminal_button"
                    if persistent.fact_drink == True:
                        text "- FAVOURITE DRINK IS BLACK COFFEE" style "terminal_button"
                    else:
                        text "- {font=FlowBlock-Regular.ttf}FAVOURITE DRINK IS BLACK COFFEE{/font}" style "terminal_button"
                    if persistent.fact_cosmetics == True:
                        text "- USES CONCEALER AND HAIR DYE" style "terminal_button"
                    else:
                        text "- {font=FlowBlock-Regular.ttf}USES CONCEALER AND HAIR DYE{/font}" style "terminal_button"

                    if persistent.fact_residence == True:
                        text "- LIVES IN THE BETTER PARTS OF CORLAND BAY" style "terminal_button"
                        text "- HAS A RESIDENCY AT SUNSHINE HILLS APARTMENTS" style "terminal_button"
                    else:
                        text "- {font=FlowBlock-Regular.ttf}LIVES IN THE BETTER PARTS OF CORLAND BAY{/font}" style "terminal_button"
                        text "- {font=FlowBlock-Regular.ttf}HAS A RESIDENCY AT SUNSHINE HILLS APARTMENTS{/font}" style "terminal_button"
                    if persistent.fact_awy == True:
                        text "- HAS AN INTEREST IN \"ALWAYS WITH YOU\"" style "terminal_button"
                    else:
                        text "- {font=FlowBlock-Regular.ttf}HAS AN INTEREST IN \"ALWAYS WITH YOU\"{/font}" style "terminal_button"
                    textbutton "{size=+10}LOG OUT{/size}" text_style "terminal_button" action ToggleVariable("persistent.terminal_unlocked") align (0.5,0.5) at choice_fade

    vpgrid:
        area (850, 794, 850, 794)
        pos (963,165)
        cols 2
        if persistent.dlc_14nightswithyou == True:
            rows 7
        else:
            rows 5
        draggable False
        mousewheel True
        scrollbars "vertical"
        spacing 20
        at slidedown
        add g.make_button(name="D1_library", unlocked="gui/gallery/D1_library.png", locked="gui/gallery/locked.png")
        if persistent.dlc_14nightswithyou == True:
            add g.make_button(name="D1_NSFW", unlocked="gui/gallery/D1_nsfw.png", locked="gui/gallery/locked.png")
        add g.make_button(name="D2_rain", unlocked="gui/gallery/D2_rain.png", locked="gui/gallery/locked.png")
        if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
            add g.make_button(name="D2_NSFW", unlocked="gui/gallery/nsfw_placeholder.png", locked="gui/gallery/locked.png")
        add g.make_button(name="D3_manga", unlocked="gui/gallery/D3_manga.png", locked="gui/gallery/locked.png")
        if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
            add g.make_button(name="D3_NSFW", unlocked="gui/gallery/nsfw_placeholder.png", locked="gui/gallery/locked.png")
        add g.make_button(name="D4_aquarium", unlocked="gui/gallery/D4_aquarium.png", locked="gui/gallery/locked.png")
        if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
            add g.make_button(name="D4_NSFW", unlocked="gui/gallery/nsfw_placeholder.png", locked="gui/gallery/locked.png")
        add g.make_button(name="D5_beach", unlocked="gui/gallery/D5_beach.png", locked="gui/gallery/locked.png")
        add g.make_button(name="D5_alley", unlocked="gui/gallery/D5_alleyway.png", locked="gui/gallery/locked.png")
        if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
            add g.make_button(name="D5_NSFW", unlocked="gui/gallery/nsfw_placeholder.png", locked="gui/gallery/locked.png")
        add g.make_button(name="DE_3_1", unlocked="gui/gallery/secret.png", locked="gui/gallery/locked.png")
        add g.make_button(name="DE_3_2", unlocked="gui/gallery/secret.png", locked="gui/gallery/locked.png")
        add g.make_button(name="DE_3_3", unlocked="gui/gallery/secret.png", locked="gui/gallery/locked.png")