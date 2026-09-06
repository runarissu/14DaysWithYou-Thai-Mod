################################################################################
## Thai Language Selector — 14 Days With You
##
## Adds a small language toggle button in the top-left corner of the screen.
## The toggle is always visible so the player can switch between English
## and Thai at any time.
## Default language is set to Thai on first launch.
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

## --- Set default language to Thai on first launch ---
init -100 python:
    if persistent._thai_first_launch is None:
        persistent._thai_first_launch = True
        _preferences.language = "thai"

## --- Register overlay screen so it's always visible ---
## config.overlay_screens makes the screen show on top of every other screen
init -1 python:
    if "thai_language_toggle" not in config.overlay_screens:
        config.overlay_screens.append("thai_language_toggle")

## --- Thai version of mainmenulist (shown on main menu) ---
init 5 python:
    mainmenulist_thai = [
        "ถ้าชอบเดโม ลอง{a=https://cutiesai.itch.io/14dayswithyou/rate?source=game}ให้คะแนน{/a}บน itch.io ดูนะ!",
        "อยากช่วยแปลเดโม?\nเข้า{a=https://discord.gg/14dayswithyou}Discord ทางการ{/a}แล้วบอกได้เลย!",
        "ดูอัปเดตล่าสุดได้ที่{a=https://cutiesai.itch.io/14dayswithyou}หน้า Itch ทางการ{/a}!",
        "อยากสนับสนุนผู้พัฒนา? ไปที่{a=https://ko-fi.com/cutiesai}Ko-Fi{/a}ได้เลย!",
    ]

    # Override mainmenulist when Thai is active (runs after default init)
    if _preferences.language == "thai":
        mainmenulist = list(mainmenulist_thai)
        # Also re-roll mainmenutext if it was already set to English
        try:
            if mainmenutext and mainmenutext not in mainmenulist_thai:
                mainmenutext = renpy.random.choice(mainmenulist_thai)
        except NameError:
            pass
