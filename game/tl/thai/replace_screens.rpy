################################################################################
## Thai Language Selector — 14 Days With You
##
## Adds a small language toggle button in the bottom-left corner of the screen.
## Uses config.overlay_screens so it shows on every screen without overriding
## any existing game screens.
##
## The toggle is minimal and unobtrusive — just two text buttons.
################################################################################

## Small floating language toggle, bottom-left corner
screen thai_language_toggle():
    zorder 200
    frame:
        background None
        pos (10, 10)
        hbox:
            spacing 10
            textbutton "EN":
                action Language(None)
                text_size 16
                text_color "#888888"
                selected_idle_color "#9D64FD"
                selected_hover_color "#9D64FD"
                hovered_color "#ffffff"
            textbutton "ไทย":
                action Language("thai")
                text_font "tl/thai/NotoSansThai-UI.ttf"
                text_size 16
                text_color "#888888"
                selected_idle_color "#9D64FD"
                selected_hover_color "#9D64FD"
                hovered_color "#ffffff"

## Register as overlay screen — shows on all screens
init python:
    if "thai_language_toggle" not in config.overlay_screens:
        config.overlay_screens.append("thai_language_toggle")
