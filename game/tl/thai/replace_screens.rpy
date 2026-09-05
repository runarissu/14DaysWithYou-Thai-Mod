################################################################################
## Thai Language Selector — 14 Days With You
##
## Adds a small language toggle button in the bottom-left corner of the screen.
## Uses config.overlay_screens so it shows on every screen without overriding
## any existing game screens.
################################################################################

style thai_lang_button is button:
    xsize 50
    ysize 30

style thai_lang_button_text is button_text:
    size 16
    color "#888888"
    hover_color "#ffffff"
    selected_idle_color "#9D64FD"
    selected_hover_color "#9D64FD"

screen thai_language_toggle():
    zorder 200
    frame:
        background None
        pos (10, 10)
        hbox:
            spacing 10
            textbutton "EN":
                action Language(None)
                style "thai_lang_button"
            textbutton "ไทย":
                action Language("thai")
                style "thai_lang_button"
                text_font "tl/thai/NotoSansThai-UI.ttf"

init python:
    if "thai_language_toggle" not in config.overlay_screens:
        config.overlay_screens.append("thai_language_toggle")
