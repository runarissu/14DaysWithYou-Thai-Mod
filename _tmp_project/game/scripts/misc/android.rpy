screen androidversion():
    tag menu
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    style_prefix "popupblack"
    frame:
        align (0.5, 0.5)
        vbox:
            align (0.5,0.5)
            text "{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}THIS DEMO IS NOT COMPATIBLE\nWITH MOST THIRD-PARTY APPS\n{size=-20}Play on PC (Windows, Linux, Mac) for the best experience{/size}{/color}{/font}\n":
                size 45
                textalign 0.5
                align (0.5,0.5)
            text "{image=gui/misc/divider.png}":
                textalign 0.5
                align (0.5,0.5)
            text "{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}What name would you like to be called?{/color}{/font}":
                size 40
                textalign 0.5
                align (0.5,0.5)
            button:
                align (0.5,0.5)
                key_events True
                action player_input.Toggle()
                input:
                    length 15
                    value player_input
            text "{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}What pronouns do you use?{/color}{/font}":
                size 40
                textalign 0.5
                align (0.5,0.5)
            hbox:
                align (0.5, 0.5)
                spacing 10
                textbutton _("SHE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("pronoun", "female"), refresh_pronouns] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("HE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("pronoun", "male"), refresh_pronouns] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("THEY") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("pronoun", "neutral"), refresh_pronouns] hovered Play("sound", "audio/ui/click1.ogg")

    imagebutton auto "gui/ui/forward_%s.png" action [Play("sound", "audio/ui/accept.ogg"), Hide ("androidversion"), Jump("cont")] at amm_button anchor (0.5, 0.5) pos (0.69, 0.8) hovered Play("sound", "audio/ui/click2.ogg")

style mobilebutton:
    selected_color "#FF66CB"
    hover_color "#9d64fd"
    idle_color "#898989"
    bold True
    size 30
    font "fonts/Assistant-Regular.ttf"