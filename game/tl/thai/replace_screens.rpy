################################################################################
## Thai Language Selector — 14 Days With You
##
## Adds a small language toggle button in the top-left corner of the screen.
## The toggle is always visible so the player can switch between English
## and Thai at any time.
################################################################################

style thai_lang_button is button:
    xsize 60
    ysize 30

style thai_lang_button_text is button_text:
    size 16
    color "#888888"
    hover_color "#ffffff"
    selected_color "#9D64FD"
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

## Show the overlay screen at startup and keep it shown
init python:
    if "thai_language_toggle" not in config.overlay_screens:
        config.overlay_screens.append("thai_language_toggle")

    def _thai_show_toggle():
        renpy.show_screen("thai_language_toggle")

    config.start_callbacks = config.start_callbacks + [_thai_show_toggle]
