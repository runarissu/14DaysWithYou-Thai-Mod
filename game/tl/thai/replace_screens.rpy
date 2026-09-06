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

    # Thai version of renchatterlist (Ren's random chatter on main menu)
    renchatterlist_thai = [
        "วันนี้กินข้าวรึยัง?",
        f"{persistent.game_open} เป็นเลขที่ชอบที่สุดเลย!\nนี่คือจำนวนครั้งที่เปิดเกมนะ! >///<",
        "อย่าลืมดื่มน้ำนะ, Angel!",
        "คิดถึงจัง!",
        f"แล้วก็... ครั้งที่ {persistent.game_open}!\n ...อ่อ? ก็ฉันนับว่าเปิดเกมกี่ครั้งไง!",
        "รักนะรักนะรักนะรักนะรักนะ!",
        "ตี 2 แล้วนะ เวลาเล่น 14DWY ได้แล้ว",
        "รักนะ, Angel!",
        "โอ? กลับมาเร็วจัง?",
        "คิดถึงจังเลย",
        "ฉันกำลังคิดถึงคุณอยู่นะ, Angel.",
        "คุณกำลังคิดถึงฉันอยู่รึเปล่า? อาาา...",
        "...ฉันเห็นคุณนะ ^^",
        "อ่านหนังสือด้วยกันไหม?",
        "พักผ่อนบ้างไหม? ไปด้วยกันได้ไหม? ^^",
        "กินข้าวเที่ยงด้วยกันวันนี้ไหม?",
        "มีหนังสือแนะนำบ้างไหม?",
        "ยังชอบ Haruko อยู่ไหม? ...แค่ถามดู",
        "อย่าสนใจ Leon แล้วมาอยู่กับฉันวันนี้สิ!",
        "สวัสดี, Angel.",
        "ไม่ได้คุยกับยันเดเรคนอื่นใช่ไหม?",
        "ได้ยินมาว่ามีบอท Discord 14DWY\nที่ทำเหมือนกับฉันเปี๊ยบเลย...",
        "อ่านหนังสือด้วยกันไหม? แค่สองคนนะ",
        "...อยากจับผมฉันไหม? ^^",
        "*จู๊ววววว* คิดถึงจัง, Angel!",
        "ชอบกดปุ่มจังเลยนะ? :)",
        "คุณก็คิดถึงฉันเหมือนกันใช่ไหม? ก็เลยมาที่นี่?",
        "โอ้ ดูสิ! คนน่ารักที่สุดในจักรวาลมาแล้ว!",
    ]
