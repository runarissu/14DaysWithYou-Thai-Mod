################################################################################
## Thai Screen Translations — 14 Days With You
##
## Redefines screens that contain hardcoded English text (not using _()).
## Uses _preferences.language to switch text based on selected language.
################################################################################

init python:
    def _is_thai():
        return _preferences.language == "thai"

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
            text ("ปรับแต่งตัวละครหลักไหม?" if _is_thai() else "Customise the main character?"):
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
                text ("\"{color=#FF66CB}{b}โหมดสตรีมเมอร์{/b}{/color}\" กำลังเปิดอยู่\nกรุณาปิดเพื่อใช้ฟีเจอร์นี้" if _is_thai() else "\"{color=#FF66CB}{b}Streamer Mode{/b}{/color}\" is currently enabled.\nPlease disable it to use this feature."):
                    size 22
                    font "fonts/Assistant-Regular.ttf"
                    color "#141414"
                    text_align 0.5
            elif persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid" and persistent.dlc_14nwy_comp == False:
                    text ("กรุณาอัปเดตเกมหลักและ DLC\nเพื่อปลดล็อกส่วนนี้" if _is_thai() else "Please update the base game and its DLC\nto unlock this section."):
                        size 22
                        textalign 0.5
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
            elif persistent.dlc_14nightswithyou == True:
                text ("ต้องการเปิดใช้งาน DLC 18+ ไหม?" if _is_thai() else "Do you want to enable the 18+ DLC?"):
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
                text ("คุณยังไม่มี DLC! เข้าชม\n{a=https://cutiesai.itch.io/}{b}cutiesai.itch.io{/b}{/a} เพื่อเปิดใช้ฟีเจอร์นี้" if _is_thai() else "You don't own any DLCs! Visit\n{a=https://cutiesai.itch.io/}{b}cutiesai.itch.io{/b}{/a} to enable this feature"):
                    size 22
                    font "fonts/Assistant-Regular.ttf"
                    color "#141414"
                    text_align 0.5

    ## Profile section hehe
    hbox:
        at slidedown
        pos (789,678)
        text ("14 Days With You ยังเป็นเดโมอยู่!\nลองสนับสนุน cutiesai\nที่ {a=https://ko-fi.com/cutiesai}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Ko-Fi{/color}{/font}{/a}, {a=https://cutiesai.itch.io/14dayswithyou}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Itch{/color}{/font}{/a}, หรือ {a=https://discord.gg/14dayswithyou}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Discord{/color}{/font}{/a}!" if _is_thai() else "14 Days With You is still a demo!\nConsider supporting cutiesai\non {a=https://ko-fi.com/cutiesai}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Ko-Fi{/color}{/font}{/a}, {a=https://cutiesai.itch.io/14dayswithyou}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Itch{/color}{/font}{/a}, or {a=https://discord.gg/14dayswithyou}{font=fonts/VT323-Regular.ttf}{color=#FF66CB}Discord{/color}{/font}{/a}!"):
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
            text ("อยู่ใน DM ของ Haruko เหรอ? ฉันยังดีอยู่\nเราไม่เหมือนกันนะ <3 ([they]/[them])" if _is_thai() else "You're in Haruko's DMs? I'm in sane\nWe are not the same <3 ([they]/[them])"):
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
                text ("ยินดีต้อนรับกลับมา!" if _is_thai() else "WELCOME BACK!"):
                    size 30
                    font "fonts/Orbitron-Black.ttf"
                    color "#141414"
            else:
                text ("สวัสดีจ้า!" if _is_thai() else "HELLO THERE!"):
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
            text ("- เปลี่ยนไอคอนสักที\n- Passw0rd_777 {size=-10}(ใช้ศูนย์นะ!!!){/size}\n- 01101100 01101111 01101100\n- ใต้กระดาษโน้ต" if _is_thai() else "- change my icon somehow\n- Passw0rd_777 {size=-10}(with a zero!!!){/size}\n- 01101100 01101111 01101100\n- underneath the stickynote"):
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
            tooltip"{color=#ff66cb}{size=+5}@[username_moth]{/size}{/color}\nMOTH, ATLAS | THEY/ANY"
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
## screen over18() — 18+ warning screen
################################################################################

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
            text ("คำเตือน!" if _is_thai() else "WARNING!"):
                text_align 0.5
                outlines [ (absolute(7), "362A46", absolute(2), absolute(2)) ]
                font "fonts/Orbitron-Black.ttf"
                size 80
                color "#FF66CB"
                kerning 10

        hbox:
            xalign 0.5
            text ("\"14 Days With You\" เป็นเดโมของเกมแนวสยองขวัญ/โรแมนติกที่กำลังจะวางจำหน่าย และมีไว้สำหรับผู้เล่นอายุ 18 ปีขึ้นไป เนื้อเรื่องจะเข้มขึ้นเรื่อยๆ เมื่อตอนใหม่ออก ผู้เล่นควรใช้วิจารณญาณด้วยตนเอง\n\n{color=#9d64fd}{b}เดโมนี้มี:{/b}{/color} คำพูดหยาบคายเล็กน้อย สยองขวัญ ฉากนองเลือด และธีมที่น่าขนลุก เช่น การถูกตามตัว ความรุนแรง ความตาย และการฆาตกรรม รวมถึงข้อความที่ลายตา การสั่นของหน้าจอ และอาจทำให้ผู้ที่มีอาการชักแบบไวต่อแสงเกิดอาการชักได้ ดูรายการเตือนเนื้อหาทั้งหมดได้ที่ {a=https://cutiesai.com/14dwy}คลิกที่นี่{/a}\n" if _is_thai() else "\"14 Days With You\" is a demo for an upcoming horror/romance game, and is intended to be played by those who are 18 and older. Themes will get darker as more \"Days\" are released. Player discretion is advised.\n\n{color=#9d64fd}{b}THIS DEMO INVOLVES:{/b}{/color} mild coarse language, horror, gore, and unsettling themes such as being stalked, violence, death, and murder. It also involves eye-straining text, screen shakes, and the potential to cause seizures for those with photosensitive epilepsy. For the full list of content warnings, please {a=https://cutiesai.com/14dwy}click here{/a}.\n"):
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
                    action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", False), Confirm(("{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}สำคัญมาก!{/font}{/size}{/color}\nยืนยันว่าคุณ{color=#a30b11}{b}อายุ 18 ปี{u}ขึ้นไป{/u}{/b}{/color}\nและได้อ่านรายการเตือนเนื้อหาแล้ว?" if _is_thai() else "{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}IMPORTANT!{/font}{/size}{/color}\nConfirm you are {color=#a30b11}{b}18 OR {u}OVER{/u}{/b}{/color} and have\nlooked at the list of content warnings?"), yes=MainMenu(confirm=False), no=None, confirm_selected=False)]
        else:
            hbox:
                spacing 30
                xalign 0.5
                hbox:
                    textbutton _("I AM {u}UNDER{/u} 18"):
                        text_style "ss_button"
                        hovered [Play("sound", "audio/ui/click1.ogg")]
                        action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", True), Confirm(("{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}สำคัญมาก!{/font}{/size}{/color}\nยืนยันว่าคุณ{color=#a30b11}{b}{u}อายุต่ำกว่า{/u} 18 ปี{/b}{/color}\nและได้อ่านทุกอย่างถูกต้องแล้ว?" if _is_thai() else "{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}IMPORTANT!{/font}{/size}{/color}\nConfirm you are {color=#a30b11}{b}{u}UNDER{/u} 18{/b}{/color} and have\n read everything correctly?"), Quit(), no=None, confirm_selected=False)]
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
                        action [Play("sound", "audio/ui/accept.ogg"), SetVariable("persistent.warningscreen", False), Confirm(("{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}สำคัญมาก!{/font}{/size}{/color}\nยืนยันว่าคุณ{color=#a30b11}{b}อายุ 18 ปี{u}ขึ้นไป{/u}{/b}{/color}\nและได้อ่านทุกอย่างถูกต้องแล้ว?" if _is_thai() else "{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}IMPORTANT!{/font}{/size}{/color}\nConfirm you are {color=#a30b11}{b}18 OR {u}OVER{/u}{/b}{/color} and have\n read everything correctly?"), yes=Jump("loginscreen"), no=None, confirm_selected=False)]
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
## screen customiselogin() — login screen
################################################################################

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
            text ("{size=+20}ยินดีต้อนรับกลับมา!{/size}\nกรุณาใส่ชื่อผู้ใช้ CorUpdates เพื่อดำเนินการต่อ" if _is_thai() else "{size=+20}WELCOME BACK!{/size}\nEnter your CorUpdates username to continue"):
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
                text ("สวัสดีจ้า, angel! {size=-5}👋😇{/size}" if _is_thai() else "Hello, angel! {size=-5}👋😇{/size}"):
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
                text ("เป็นคอนเทนต์ครีเอเตอร์หรือสตรีมเมอร์ไหม?" if _is_thai() else "Are you a content creator or live streamer?"):
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
## screen androidversion() — Android version warning + name/pronoun setup
################################################################################

screen androidversion():
    tag menu
    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    style_prefix "popupblack"
    frame:
        align (0.5, 0.5)
        vbox:
            align (0.5,0.5)
            text ("{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}เดโมนี้ไม่รองรับ\nแอปของบุคคลที่สามส่วนใหญ่\n{size=-20}เล่นบน PC (Windows, Linux, Mac) เพื่อประสบการณ์ที่ดีที่สุด{/size}{/color}{/font}\n" if _is_thai() else "{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}THIS DEMO IS NOT COMPATIBLE\nWITH MOST THIRD-PARTY APPS\n{size=-20}Play on PC (Windows, Linux, Mac) for the best experience{/size}{/color}{/font}\n"):
                size 45
                textalign 0.5
                align (0.5,0.5)
            text "{image=gui/misc/divider.png}":
                textalign 0.5
                align (0.5,0.5)
            text ("{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}อยากให้เรียกคุณว่าอะไร?{/color}{/font}" if _is_thai() else "{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}What name would you like to be called?{/color}{/font}"):
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
            text ("{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}คุณใช้สรรพนามอะไร?{/color}{/font}" if _is_thai() else "{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}What pronouns do you use?{/color}{/font}"):
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


################################################################################
## screen versionscreen() — version number display
################################################################################

screen versionscreen():
    vbox:
        xalign 0.99
        yalign 1
        if renpy.variant("pc"):
            text ("เวอร์ชัน [version_number]" if _is_thai() else "Ver [version_number]") size 25 text_align 1.0:
                outlines [(absolute(1), "#141414", absolute(0), absolute(0))]
        if renpy.variant("mobile"):
            text ("{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{noalt}คุณกำลังใช้แอปของบุคคลที่สาม\nอาจพบบั๊กและข้อผิดพลาดได้\nเล่นบน PC เพื่อประสบการณ์ที่ดีที่สุด\n(เวอร์ชัน [version_number]){/noalt}{/color}{/font}" if _is_thai() else "{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{noalt}YOU ARE USING A THIRD-PARTY APP\nBUGS AND ERRORS ARE TO BE EXPECTED\nPLAY ON PC FOR THE BEST EXPERIENCE\n(Ver [version_number]){/noalt}{/color}{/font}") size 25:
                outlines [(absolute(2), "#141414", absolute(0), absolute(0))]


################################################################################
## screen savepoint() — end of day save prompt
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
                text ("{color=#FF66CB}{font=fonts/Orbitron-Regular.ttf}จบวันที่ [calendar_day]!{/font}{/color}" if _is_thai() else "{color=#FF66CB}{font=fonts/Orbitron-Regular.ttf}END OF DAY [calendar_day]!{/font}{/color}") size 55
            vbox:
                text ("วันถัดไปจะเริ่มขึ้นเร็วๆ นี้! อยากบันทึกความคืบหน้าไหม?" if _is_thai() else "The next day will soon begin! Would you like to save your progress?"):
                    size 25
                    xalign 0.5
                text ("{color=#8f8f8f}({b}คำเตือน:{/b} การเซฟด่วนจะเขียนทับเซฟก่อนหน้าทั้งหมด!)\n{/color}" if _is_thai() else "{color=#8f8f8f}({b}WARNING:{/b} Quicksaving will overwrite any previous saves!)\n{/color}"):
                    size 20
                    xalign 0.5
            hbox:
                xalign 0.5
                spacing 30
                textbutton _("YES") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), QuickSave(message='PROGRESS HAS BEEN SAVED!', newest=True), SetVariable("persistent.dayend", True), Jump(skipday)] hovered [Play("sound", "audio/ui/click1.ogg")]
                textbutton _("NO") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), Jump(skipday)] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("QUIT") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), MainMenu(confirm=False)] hovered Play("sound", "audio/ui/click1.ogg")


################################################################################
## screen demopoint() — demo end screen
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
                text ("จบเดโมแล้ว" if _is_thai() else "END OF THE DEMO"):
                    size 55
                    color "#FF66CB"
                    font "fonts/Orbitron-Black.ttf"
            vbox:
                text ("{size=+5}{font=fonts/Orbitron-Black.ttf}ขอบคุณที่เล่น!{/font}{/size}\nลองหาตอนจบทั้งหมดหรือยัง?\n\nถ้าอยากหาคอนเทนต์ 14DWY เพิ่มเติม ไปติดตามได้ที่ {a=https://discord.gg/14dayswithyou}Discord{/a} | {a=https://14dayswithyou.tumblr.com}Tumblr{/a} | {a=https://twitter.com/14dayswithyou}Twitter{/a} | {a=https://bsky.app/profile/cutiesai.com}Bluesky{/a} เพื่อดูความคืบหน้าการพัฒนาและเรื่องราวเบื้องหลังของเกม!\n" if _is_thai() else "{size=+5}{font=Orbitron-Black.ttf}Thanks for playing!{/font}{/size}\nHave you tried to get all the different endings yet?\n\nIf you're looking for even more 14DWY content, feel free to check out the official {a=https://discord.gg/14dayswithyou}Discord{/a} | {a=https://14dayswithyou.tumblr.com}Tumblr{/a} | {a=https://twitter.com/14dayswithyou}Twitter{/a} | {a=https://bsky.app/profile/cutiesai.com}Bluesky{/a} for game development progress and lore drops!\n"):
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
## screen gamewarning() — underage restriction warning
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
                text ("กรุณาอ่าน!" if _is_thai() else "PLEASE READ!"):
                    font "fonts/Orbitron-Regular.ttf"
                    size 55
                    color "#FF66CB"
            vbox:
                text ("{i}14 Days With You{/i} มีไว้สำหรับผู้ใหญ่ (18 ปีขึ้นไป)" if _is_thai() else "{i}14 Days With You{/i} is intended for adults (18 and over)."):
                    size 25
                    xalign 0.5
                text ("ห้ามผู้เยาว์เล่นหรือมีส่วนร่วมในทุกรูปแบบ\n" if _is_thai() else "Minors are prohibited from playing or interacting in any capacity.\n"):
                    size 25
                    xalign 0.5
                text ("{color=#8f8f8f}เพื่อป้องกันการเข้าถึงโดยไม่ชอบด้วยกฎหมาย เกมของคุณถูกจำกัดแล้ว\n{/color}" if _is_thai() else "{color=#8f8f8f}To avoid unlawful access, your game has now been restricted.\n{/color}"):
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


################################################################################
## screen streamingmode() — streamer mode toggle
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
                text ("โหมดสตรีมเมอร์" if _is_thai() else "STREAMER MODE"):
                    size 55
                    font "fonts/Orbitron-Black.ttf"
                    color "#FF66CB"
                    xalign 0.5
                vbox:
                    text ("\nการเปิดโหมดนี้จะทำสิ่งต่อไปนี้:" if _is_thai() else "\nEnabling this mode will do the following:"):
                        color "#9d64fd"
                        size 25
                        xalign 0.5
                        text_align 0.5
                    text ("- ซ่อนการแสดงเวลาของอุปกรณ์\n- จำกัดคำหยาบคาย\n- ปิดคอนเทนต์ทางเพศทั้งหมด (รวมถึง DLC 18+)\n- โหมดนี้{u}ไม่{/u}เปลี่ยนแปลงความสยองขวัญ ความรุนแรง และเนื้อหาที่มืดมนในเดโม!" if _is_thai() else "- Hide any instances of your device's internal clock\n- Limit the amount of strong language used\n- Disable all sexual content (including the 18+ DLC)\n- This mode currently {u}does not{/u} change the horror, gore, and darker elements found within the demo!"):
                        size 23
                        xalign 0.5
                        justify True
                        text_align 0.0
            hbox:
                align (0.5,0.5)
                spacing 30
                textbutton _("ENABLE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("persistent.streamermode", True)] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("DISABLE") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("persistent.streamermode", False)] hovered Play("sound", "audio/ui/click1.ogg")
            text ("หากอยากรู้ว่าสามารถบันทึกหรือสตรีมอะไรได้บ้าง กรุณา{a=https://cutiesai.com/14dwy}เข้าเว็บไซต์นี้{/a} จะเปิดในเบราว์เซอร์ของคุณ!" if _is_thai() else "If you'd like to know what you're allowed to record or livestream, please {a=https://cutiesai.com/14dwy}visit this webpage{/a}. It'll open in your browser!"):
                size 20
                xalign 0.5
                color "#8f8f8f"
                text_align 0.5

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Hide("streamingmode")] at amm_button, slideleft anchor (0.5, 0.5) pos (0.28, 800) hovered Play("sound", "audio/ui/click2.ogg")


################################################################################
## screen relprofile() — profile editing screen
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
            text ("อยากอัปเดตสถานะไหม?" if _is_thai() else "Want to update your status?"):
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
            text ("เปลี่ยนชื่อผู้ใช้ไหม?" if _is_thai() else "Change your username?"):
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
## screen customcharacter() — custom angel creation screen
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
            text ("อยากให้เรียกคุณว่าอะไร?" if _is_thai() else "What would you like to be called?"):
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
            text ("คุณใช้สรรพนามอะไร?" if _is_thai() else "What pronouns do you use?"):
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
            text ("ความยาวผม" if _is_thai() else "CUSTOM HAIR LENGTH"):
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
            text ("เนื้อผม" if _is_thai() else "CUSTOM HAIR TEXTURE"):
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
                text ("{color=#ff66cb}ชื่อเต็ม:{/color} [player] [surname]" if _is_thai() else "{color=#ff66cb}FULL NAME:{/color} [player] [surname]")
                text ("{color=#ff66cb}สรรพนาม:{/color} [they]/[them]" if _is_thai() else "{color=#ff66cb}PRONOUNS:{/color} [they]/[them]")
                text ("{color=#ff66cb}อายุ:{/color} ผู้ใหญ่\n" if _is_thai() else "{color=#ff66cb}AGE:{/color} adult\n")
                if customise_hair == "hair_7":
                    text ("{color=#ff66cb}ทรงผม:{/color} [hair_texture], [hair_length]" if _is_thai() else "{color=#ff66cb}HAIRSTYLE:{/color} [hair_texture], [hair_length]")
                    text ("{color=#ff66cb}สีผม:{/color} ซ่อนอยู่" if _is_thai() else "{color=#ff66cb}HAIR COLOUR:{/color} hidden")
                elif hair_length != "bald":
                    text ("{color=#ff66cb}ทรงผม:{/color} [hair_texture], [hair_length]" if _is_thai() else "{color=#ff66cb}HAIRSTYLE:{/color} [hair_texture], [hair_length]")
                    text ("{color=#ff66cb}สีผม:{/color} [hair_colour]" if _is_thai() else "{color=#ff66cb}HAIR COLOUR:{/color} [hair_colour]")
                else:
                    text ("{color=#ff66cb}ทรงผม:{/color} เดิม [hair_texture], ตอนนี้ [hair_length]" if _is_thai() else "{color=#ff66cb}HAIRSTYLE:{/color} formerly [hair_texture], now [hair_length]")
                    text ("{color=#ff66cb}สีผม:{/color} เดิม [hair_colour]" if _is_thai() else "{color=#ff66cb}HAIR COLOUR:{/color} formerly [hair_colour]")
                text ("{color=#ff66cb}สีตา:{/color} [eye_colour]\n" if _is_thai() else "{color=#ff66cb}EYE COLOUR:{/color} [eye_colour]\n")
                text ("{color=#ff66cb}อาชีพ:{/color} บรรณารักษ์\n" if _is_thai() else "{color=#ff66cb}OCCUPATION:{/color} librarian\n")
                text ("{color=#ff66cb}ที่อยู่:{/color} {font=fonts/FlowBlock-Regular.ttf}555 คิดว่าฉันจะสปอยล์ข้อมูลนี้ตั้งแต่ตอนนี้เหรอ{/font}, Corland Bay\n" if _is_thai() else "{color=#ff66cb}HOME ADDRESS:{/color} {font=fonts/FlowBlock-Regular.ttf}lol like I'd spoil this information so early on{/font}, Corland Bay\n")
                text ("{color=#ff66cb}คนรู้จัก:{/color} Leon Davis (เพื่อน), \"Moth\" (เพื่อน), {font=fonts/FlowBlock-Regular.ttf}Ren (แฟนในอนาคต){/font}, Violet Garcia (เพื่อนบ้าน), Elanor Creston (เพื่อนร่วมงาน), Conan O'Rourke (นายจ้าง), {font=fonts/FlowBlock-Regular.ttf}สปอยล์, สปอยล์ สปอยล์ แหะๆ{/font}\n" if _is_thai() else "{color=#ff66cb}KNOWN AFFILIATES:{/color} Leon Davis (friend), \"Moth\" (friend), {font=fonts/FlowBlock-Regular.ttf}Ren (future boyfriend){/font}, Violet Garcia (neighbour), Elanor Creston (coworker), Conan O'Rourke (employer), {font=fonts/FlowBlock-Regular.ttf}spoilers, spoiler spoil hehe{/font}\n")
                text ("{color=#ff66cb}ครอบครัว:{/color} ไม่ทราบ" if _is_thai() else "{color=#ff66cb}KNOWN FAMILY:{/color} unknown")

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
## screen custompronouns() — custom pronoun input screen
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
                text ("เลือกสรรพนามที่คุณต้องการ!\n" if _is_thai() else "CHOOSE YOUR PREFERRED PRONOUNS!\n"):
                    font "fonts/Orbitron-Black.ttf"
                    size 30
            hbox:
                spacing 20
                xalign 0.5
                text ("{b}สรรพนามประธาน{/b}    {color=#8f8f8f}{size=-5}she | he | they{/size}{/color}" if _is_thai() else "{b}Subjective Pronoun{/b}    {color=#8f8f8f}{size=-5}she | he | they{/size}{/color}"):
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
                text ("{b}สรรพนามกรรม{/b}    {color=#8f8f8f}{size=-5}her | him | them{/size}{/color}" if _is_thai() else "{b}Objective Pronoun{/b}    {color=#8f8f8f}{size=-5}her | him | them{/size}{/color}"):
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
                text ("{b}คำแสดงความเป็นเจ้าของ{/b}    {color=#8f8f8f}{size=-5}her | his | their{/size}{/color}" if _is_thai() else "{b}Possesive Adjective{/b}    {color=#8f8f8f}{size=-5}her | his | their{/size}{/color}"):
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
                text ("{b}สรรพนามแสดงความเป็นเจ้าของ{/b}    {color=#8f8f8f}{size=-5}hers | his | theirs{/size}{/color}" if _is_thai() else "{b}Posessive Pronoun{/b}    {color=#8f8f8f}{size=-5}hers | his | theirs{/size}{/color}"):
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
                text ("{b}สรรพนามสะท้อนกลับ{/b}    {color=#8f8f8f}{size=-5}herself | himself | themself{/size}{/color}" if _is_thai() else "{b}Reflective Pronoun{/b}    {color=#8f8f8f}{size=-5}herself | himself | themself{/size}{/color}"):
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
                text ("{b}คำเรียก{/b}    {color=#8f8f8f}{size=-5}woman | man | person{/size}{/color}" if _is_thai() else "{b}Word for{/b}    {color=#8f8f8f}{size=-5}woman | man | person{/size}{/color}"):
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
                text ("{b}คำเรียก{/b}    {color=#8f8f8f}{size=-5}girlfriend | boyfriend | partner{/size}{/color}" if _is_thai() else "{b}Word for{/b}    {color=#8f8f8f}{size=-5}girlfriend | boyfriend | partner{/size}{/color}"):
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
                text ("{b}คำเรียก{/b}    {color=#8f8f8f}{size=-5}wife | husband | spouse{/size}{/color}" if _is_thai() else "{b}Word for{/b}    {color=#8f8f8f}{size=-5}wife | husband | spouse{/size}{/color}"):
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
                text ("แบบไหนเหมาะกว่า?" if _is_thai() else "WHICH IS MORE FITTING?"):
                    font "fonts/Orbitron-Black.ttf"
                    size 25
            hbox:
                xalign 0.5
                spacing 30
                textbutton _("is") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("are", "is")] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("are") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("are", "are")] hovered Play("sound", "audio/ui/click1.ogg")
            hbox:
                xalign 0.5
                text ("เธอคือ... | เขาคือ... | พวกเขาคือ..." if _is_thai() else "she is... | he is... | they are..."):
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
                    text ("อ้า? {color=#9d64fd}{b}[person] ดีตา{/b}{/color} คนนั่นเป็นใคร?" if _is_thai() else "Hm? Who's that {color=#9d64fd}{b}[gorgeous] [person]{/b}{/color} over there?"):
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
                hbox:
                    xalign 0.5
                    text ("นั่น [player!l!c]! {color=#9d64fd}{b}[they!c] [are]{/b}{/color}{color=#9d64fd}{b}[partner]{/b}{/color}ของฉันนะ, แต่…" if _is_thai() else "That's [player!l!c]! {color=#9d64fd}{b}[they!c] [are]{/b}{/color} my {color=#9d64fd}{b}[partner]{/b}{/color}, but…"):
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
                hbox:
                    xalign 0.5
                    text ("ฉันอยากให้{color=#9d64fd}{b}[them]{/b}{/color}เป็น{color=#9d64fd}{b}[spouse]{/b}{/color}ของฉัน" if _is_thai() else "I want {color=#9d64fd}{b}[them]{/b}{/color} to be my {color=#9d64fd}{b}[spouse]{/b}{/color}."):
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
                hbox:
                    xalign 0.5
                    text ("กรุณาอย่าแตะหนังสือของ{color=#9d64fd}{b}[their]{/b}{/color} นั่นเป็นของ{color=#9d64fd}{b}[theirs]{/b}{/color}" if _is_thai() else "Please don't touch {color=#9d64fd}{b}[their]{/b}{/color} book. That's {color=#9d64fd}{b}[theirs]{/b}{/color}."):
                        font "fonts/Assistant-Regular.ttf"
                        color "#141414"
                        size 25
                hbox:
                    xalign 0.5
                    text ("{color=#9d64fd}{b}[they!c]{/b}{/color}บอกฉันเองว่า{color=#9d64fd}{b}[themself]{/b}{/color}" if _is_thai() else "{color=#9d64fd}{b}[they!c]{/b}{/color} told me that {color=#9d64fd}{b}[themself]{/b}{/color}."):
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
                text ("อยากให้คนอื่นมองเห็นคุณ\nแบบไหน?" if _is_thai() else "HOW WOULD YOU LIKE TO BE\nPERCEIVED BY OTHERS?"):
                    font "fonts/Orbitron-Black.ttf"
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
## screen rellegend() — WIP legend popup
################################################################################

screen rellegend():
    vbox:
        pos (220, 730)
        text ("กำลังทำอยู่! ฉันยังไม่เสร็จเรื่องนี้" if _is_thai() else "WIP! I'm still doing something with this"):
            outlines [ (absolute(4), "848788", absolute(0), absolute(0)) ]
            font "fonts/VarelaRound-Regular.ttf"
            size 30
            kerning 3
            bold True
            text_align 1.0


################################################################################
## screen relcontacts() — contacts popup (WIP)
################################################################################

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
                text ("{font=fonts/Assistant-Regular.ttf}{color=#141414}กำลังทำอยู่ ฮ่าๆ{/color}{/font}" if _is_thai() else "{font=fonts/Assistant-Regular.ttf}{color=#141414}wip lol{/color}{/font}") size 35
        imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Hide("relcontacts")] at amm_button anchor (0.5, 0.5)pos (340,930) hovered Play("sound", "audio/ui/click2.ogg")


################################################################################
## screen newsbanner() — scrolling news banner
################################################################################

screen newsbanner():
    hbox:
        pos (197,5)
        hbox:
            at newscroll
            text ("ข่าวด่วน: Ren คือเบสบอย และนี่ยังเป็นงานที่กำลังทำอยู่" if _is_thai() else "BREAKING NEWS: REN IS BEST BOY AND THIS IS STILL A WIP."):
                color "#f8f8f8"
                font "fonts/VT323-Regular.ttf"
                size 25
                align (0.5,0.5)


################################################################################
## screen relationmenu() — socials/relationship menu screen
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
            text ("สวัสดี, [player!u]!" if _is_thai() else "HELLO, [player!u]!"):
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
## screen chat_main() — main socials chat feed
################################################################################

screen chat_main():
    frame:
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
                        text ("เปิดแอปโปรไฟล์เพื่อเริ่มต้น!" if _is_thai() else "open the profile app to get started!"):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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


################################################################################
## screen chat_private() — private/hidden chat feed
################################################################################

screen chat_private():
    frame:
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
                    text ("ฉันได้กลิ่นคนชอบแอบดูนะ :p" if _is_thai() else "i smell someone who likes to snoop :p"):
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
                    text ("? กรุ๊ปนี้คืออะไรวะ" if _is_thai() else "? wtf is this gc"):
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
                            text ("หวี @UNSENT_FROM_HEAVEN คืนนี้ยังนัดกันอยู่ใช่ไหม? <3" if _is_thai() else "Hiii @UNSENT_FROM_HEAVEN are we still on for tonight? <3"):
                                font "fonts/VT323-Regular.ttf"
                                color "#141414"
                                size 32
                                align(0.5,0.5)
                                text_align 0.5
                        else:
                            text ("บัญชีนี้ถูกยกเลิกแล้ว" if _is_thai() else "This account has been terminated."):
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


################################################################################
## screen chat_work() — work group chat feed
################################################################################

screen chat_work():
    frame:
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
                    text ("เตือนปิดหน้าต่างในห้องพักพนักงานด้วย ขอบคุณ" if _is_thai() else "Reminder to shut the window in the employee lounge. Thank you."):
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
                    text ("วันที่ 14 ของการทำวิชวลโนเวลตัวเองระหว่างเวลางาน >:3" if _is_thai() else "Day 14 of me making my own visual novel during work hours >:3"):
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
                    text ("ใครเห็นปากกาฉันไหม? ฉันวางไว้ที่ไหนสักที่แล้ว!" if _is_thai() else "Has anyone seen my pen? I left it somewhere!"):
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
                    text ("ที่ Teo ตูดใหญ่ไม่พอผ่านหน้าต่างพนักงานนี่ โอ้ยย" if _is_thai() else "the way Teo's fat dumpy won't fit through the staff window eoghhh"):
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
## screen deletedata() — DLC management & data deletion screen
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
            has vbox
            align (0.5,0.5)
            spacing 10
            text ("DLC ที่ติดตั้งแล้ว" if _is_thai() else "INSTALLED DLCS"):
                font "fonts/Orbitron-Black.ttf"
                color "#FF66CB"
                size 50
                align (0.5,0.5)
            vbox:
                align (0.5,0.5)
                spacing 20
                vbox:
                    align (0.5,0.5)
                    text ("{image=14NWY symbol} แพ็ค DLC \"14 Nights With You\"" if _is_thai() else "{image=14NWY symbol} \"14 Nights With You\" DLC pack"):
                        size 30
                        color "#f8f8f8"
                        align (0.5,0.5)
                    text ("เพิ่มคอนเทนต์ 18+/NSFW ให้กับเกม ดูรายละเอียดเพิ่มเติมได้ที่หน้า Itch {a=https://cutiesai.itch.io/14nightswithyou}คลิกที่นี่เพื่อดาวน์โหลด{/a}" if _is_thai() else "Adds additional 18+/NSFW content to the game. Please view the Itch page for more information. {a=https://cutiesai.itch.io/14nightswithyou}Click here to download{/a}."):
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
                        text ("เวอร์ชันฟรี" if _is_thai() else "FREE version"):
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
                        text ("เวอร์ชันเสียเงิน" if _is_thai() else "PAID version"):
                            size 25
                            color "#f8f8f8"

        frame:
            at slideup
            style_prefix "popupwhite"
            xysize (700,180)
            text ("ติดตั้งได้แค่{u}หนึ่ง{/u}แพ็คเท่านั้น! เวอร์ชันฟรีและเวอร์ชันเสียเงินติดตั้งพร้อมกันไม่ได้" if _is_thai() else "Make sure to only install {u}one{/u} pack! The FREE and PAID versions cannot be installed at the same time."):
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
            text ("การจัดการข้อมูล" if _is_thai() else "DATA MANAGEMENT"):
                font "fonts/Orbitron-Black.ttf"
                color "#FF66CB"
                size 50
                xalign 0.5
            text ("ตัวเลือกเพิ่มเติมจะปรากฏที่นี่เมื่อคุณปลดล็อกแล้ว\n" if _is_thai() else "More options will show up here once you unlock them\n"):
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
                    action Confirm(("{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}เดี๋ยวนะ, รอก่อน!{/font}{/size}{/color}\nแน่ใจนะว่าจะ{color=#a30b11}{b}ลบ{/b}{/color}ไฟล์เซฟ\nทั้งหมด? ทำกลับไม่ได้นะ!" if _is_thai() else "{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}WOAH, WAIT!{/font}{/size}{/color}\nAre you sure you want to {color=#a30b11}{b}DELETE{/b}{/color} all of\nyour save files? You can't undo this!"), delete_saves)
                text ("นี่จะลบไฟล์เซฟและเซฟอัตโนมัติทั้งหมด\n{u}จะไม่{/u}ลบข้อมูลที่บันทึกไว้ของคุณ!" if _is_thai() else "This will delete all your save files and autosaves.\nThis {u}will not{/u} delete any of your stored data!"):
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
                        action [Function(delete_persistent), Confirm(("{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}เดี๋ยวนะ, รอก่อน!{/font}{/size}{/color}\nแน่ใจนะว่าจะ{color=#a30b11}{b}ลบ{/b}{/color}ข้อมูล\nทั้งหมด? ไม่รวมไฟล์เซฟนะ!" if _is_thai() else "{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}WOAH, WAIT!{/font}{/size}{/color}\nAre you sure you want to {color=#a30b11}{b}DELETE{/b}{/color} all of\nyour data? This does not include\nsave files!"), yes=Return(), no=None), SetVariable("persistent.warningscreen", True)]
                    else:
                        action Confirm(("{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}เดี๋ยวนะ, รอก่อน!{/font}{/size}{/color}\nแน่ใจนะว่าจะ{color=#a30b11}{b}ลบ{/b}{/color}ข้อมูล\nทั้งหมด? ไม่รวมไฟล์เซฟนะ!" if _is_thai() else "{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}WOAH, WAIT!{/font}{/size}{/color}\nAre you sure you want to {color=#a30b11}{b}DELETE{/b}{/color} all of\nyour data? This does not include\nsave files!"), [delete_persistent, renpy.utter_restart])
                text ("นี่จะลบข้อมูลที่บันทึกไว้{u}ทั้งหมด{/i} (รวมถึงแกลเลอรีและความสำเร็จ) และรีเซ็ตเกมกลับสู่สถานะเริ่มต้น" if _is_thai() else "This will delete {u}all{/i} stored data (including your gallery and achievements) and reset the game back to its default state."):
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
                        action Confirm(("{color=#FF66CB}{size=+20}{font=fonts/Orbitron-Black.ttf}เดี๋ยวนะ, รอก่อน!{/font}{/size}{/color}\nแน่ใจนะว่าจะ{color=#a30b11}{b}ปฏิเสธ{/b}{/color}\nความช่วยเหลือของ Ren? ทำกลับไม่ได้นะ!" if _is_thai() else "{color=#FF66CB}{size=+20}{font=Orbitron-Black.ttf}WOAH, WAIT!{/font}{/size}{/color}\nAre you sure you want to {color=#a30b11}{b}DISMISS{/b}{/color}\nRen's help? You can't undo this!"), yes=[SetVariable("persistent.menumissing", False), renpy.utter_restart], no=SetVariable("persistent.menumissing", True))
                    text ("ไม่ต้องการความช่วยเหลือจาก Ren? นี่จะพาเขากลับไป\nที่หน้าเมนูหลัก\n\n{b}Ren จะยังจำคุณได้อยู่!{/b}" if _is_thai() else "Don't need Ren's help? This will bring him back to the\nmain menu screen.\n\n{b}Ren will still remember you!{/b}"):
                        color "#8f8f8f"
                        size 20
                        textalign 0.5

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideleft anchor (0.5, 0.5) pos (170,0.71) hovered Play("sound", "audio/ui/click2.ogg")


################################################################################
## screen updatewarning() — save file update warning popup
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
            text ("[player!u], รอก่อน!" if _is_thai() else "[player!u], WAIT!"):
                font "fonts/Orbitron-Black.ttf"
                color "#FF66CB"
                size 40
                align (0.5,0.5)
            text ("เพิ่งอัปเดตเป็น Day 5.5 ไหม? ถ้าใช่ ไฟล์เซฟเก่าอาจใช้ไม่ได้และอาจมีข้อผิดพลาด กรุณาเริ่มเกมใหม่เพื่อหลีกเลี่ยงปัญหา\n" if _is_thai() else "Did you recently update to Day 5.5? If so, older save files might not work and may lead to errors. Please start a new game to avoid any issues.\n"):
                color "#141414"
                font "fonts/Assistant-Regular.ttf"
                size 25
                textalign 0.5
            textbutton _("DISMISS") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("persistent.fdwyupdate", False), Hide("updatewarning")] hovered Play("sound", "audio/ui/click1.ogg") align (0.5,0.5)


################################################################################
## screen playtester() — playtester/debug mode screen
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
                text ("เปิด/ปิดโหมดเทสต์:" if _is_thai() else "Toggle playtest mode:"):
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
                text ("เปิด/ปิดการพบตัวละคร:" if _is_thai() else "Toggle meetings:"):
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
                text ("เปิด/ปิดการตาย:" if _is_thai() else "Toggle deaths:"):
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
                text ("กระโดดไปทันที:" if _is_thai() else "Immediately jump to:"):
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
## screen main_menu() — main menu screen (from common/screens.rpy)
################################################################################

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
            imagebutton auto "gui/ui/more_%s.png" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("renchatter", renpy.random.choice(renchatterlist_thai if _is_thai() else renchatterlist)), ToggleVariable("welcome_chatter")] align (0.98,0.98) hovered Play("sound", "audio/ui/click2.ogg") at choice_fade, slideright
        frame:
            background Frame(["status_box"], gui.choice_button_borders)
            pos (650,240)
            xysize (400,130)
            at slidedown
            if _is_thai():
                default _thai_menu_text = renpy.random.choice(mainmenulist_thai)
                text "[_thai_menu_text]":
                    font "fonts/Assistant-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
            else:
                text "[mainmenutext]":
                    font "fonts/Assistant-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)


        if welcome_chatter == True:
            frame:
                background Frame(["gui/boxes/bubble_black.png"], gui.choice_button_borders)
                padding (50,15,50,15)
                pos (0.81,0.725)
                anchor (1.0,1.0)
                text "[renchatter]":
                    text_align 0.5
                    if _is_thai():
                        font "fonts/Assistant-Regular.ttf"
                at choice_fade, slideright

    vbox:
        align (1.0,0.0)
        if renpy.variant("mobile"):
            text ("แอนดรอยด์ [version_number]" if _is_thai() else "Android [version_number]"):
                size 25
                xalign 1.0
                outlines [ (1, "141414", absolute(0), absolute(0)) ]
        else:
            text ("เวอร์ชัน [version_number]" if _is_thai() else "Version [version_number]"):
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
                    text ("ติดตั้ง DLC 14 Nights With You แล้วแต่ไม่รองรับ\nเวอร์ชันนี้! กรุณาดาวน์โหลดเวอร์ชันล่าสุด" if _is_thai() else "14 Nights With You DLC installed but isn't compatible\nwith this version! Please download the latest versions."):
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
            text ("ยังไม่ได้ติดตั้ง DLC" if _is_thai() else "No DLCs installed"):
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
            text ("ยินดีต้อนรับกลับมา, {font=fonts/Orbitron-Regular.ttf}[username_angel!u].{/font}" if _is_thai() else "WELCOME BACK, {font=fonts/Orbitron-Regular.ttf}[username_angel!u].{/font}"):
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
                text ("เครดิต" if _is_thai() else "Credits"):
                    font "fonts/VarelaRound-Regular.ttf"
                    color "#141414"
                    size 20
                    text_align 0.5
                    align (0.5,0.5)
                    outlines [ (2, "#f8f8f8", absolute(0), absolute(0)) ]
            vbox:
                align (0.5,0.5)
                imagebutton auto "gui/ui/folder_purple_%s.png"  action [Play("sound", "audio/ui/accept.ogg"), ShowMenu("load")] hovered [Play("sound", "audio/ui/click1.ogg")] align (0.5,0.5)
                text ("โหลด" if _is_thai() else "Load"):
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
                text ("แกลเลอรี" if _is_thai() else "Gallery"):
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
                text ("ตั้งค่า" if _is_thai() else "Settings"):
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
                text ("จัดการข้อมูล" if _is_thai() else "Manage Data"):
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


################################################################################
## screen about() — credits screen (from common/screens.rpy)
################################################################################

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
            text ("{font=fonts/Orbitron-Black.ttf}{size=+30}{color=#f8f8f8}เครดิต!{/color}{/size}{/font}" if _is_thai() else "{size=+30}{color=#f8f8f8}CREDITS!{/color}{/size}") style "popupbox_text_pink"
            text ("{font=fonts/Assistant-Regular.ttf}BGM & เอฟเฟกต์เสียงกลิตช์: {a=http://yacft.com}{color=#f8f8f8}{size=-2}Yuli Audio Craft{/size}{/color}{/a}{/font}" if _is_thai() else "BGM & glitch SFX: {a=http://yacft.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Yuli Audio Craft{/size}{/color}{/font}{/a}") style "popupbox_text_pink"
            text ("{font=fonts/Assistant-Regular.ttf}เอฟเฟกต์เสียงธรรมชาติ & บรรยากาศ: {a=https://pixabay.com}{color=#f8f8f8}{size=-2}Pixabay{/size}{/color}{/a}{/font}" if _is_thai() else "Nature & ambience SFX: {a=https://pixabay.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Pixabay{/size}{/color}{/font}{/a}") style "popupbox_text_pink"
            text ("{font=fonts/Assistant-Regular.ttf}รูปพื้นหลังสต็อก: {a=https://www.pexels.com}{color=#f8f8f8}{size=-2}Pexels{/size}{/color}{/a}{/font}" if _is_thai() else "Background stock images: {a=https://www.pexels.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Pexels{/size}{/color}{/font}{/a}") style "popupbox_text_pink"
            text ("{font=fonts/Assistant-Regular.ttf}แท็กข้อความเคลื่อนไหว & เชดเดอร์: {a=https://wattson.itch.io}{color=#f8f8f8}{size=-2}Wattson{/size}{/color}{/a}{/font}" if _is_thai() else "Kinetic text tags & shaders: {a=https://wattson.itch.io}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Wattson{/size}{/color}{/font}{/a}") style "popupbox_text_pink"
            text ("{font=fonts/Assistant-Regular.ttf}Discord สถานะการเล่น: {a=https://arianeb.com}{color=#f8f8f8}{size=-2}Ariane Barnes{/size}{/color}{/a}{/font}" if _is_thai() else "Discord rich presence: {a=https://arianeb.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Ariane Barnes{/size}{/color}{/font}{/a}") style "popupbox_text_pink"
            text ("{font=fonts/Assistant-Regular.ttf}เอนจินเกม: {color=#f8f8f8}{size=-2}Ren'Py [renpy.version_only]{/size}{/color}{/font}" if _is_thai() else "Game engine: {font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Ren'Py [renpy.version_only]{/size}{/color}{/font}") style "popupbox_text_pink"
            text ("{font=fonts/Assistant-Regular.ttf}{color=#9d64fd}ทุกอย่างอื่น:{/color} {a=https://cutiesai.com}{color=#f8f8f8}{size=-2}Saint (cutiesai){/size}{/color}{/a}{/font}" if _is_thai() else "{color=#9d64fd}Everything else:{/color} {a=https://cutiesai.com}{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}Saint (cutiesai){/size}{/color}{/font}{/a}") style "popupbox_text_pink"
            text ("\n{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}และขอบคุณมากๆ สำหรับทุกคนที่\nสนับสนุนเดโม!{/size}{/color}{/font}" if _is_thai() else "\n{font=fonts/Assistant-Regular.ttf}{color=#f8f8f8}{size=-2}And a big thank you to those who have\nsupported the demo!{/size}{/color}{/font}") style "popupbox_text_pink"

    add "images/misc/ur honor hes baby.png":
        zoom 0.3
        pos (1200,500)
        at slideright

    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Return()] at amm_button, slideup anchor (0.5, 0.5)pos (485,830) hovered Play("sound", "audio/ui/click2.ogg")


################################################################################
## screen save() — save file screen (from common/screens.rpy)
################################################################################

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
            text ("{color=#9d64fd}เซฟ{/color}ไฟล์ | " if _is_thai() else "{color=#9d64fd}SAVE{/color} FILES | "):
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


################################################################################
## screen load() — load file screen (from common/screens.rpy)
################################################################################

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
                text ("{color=#9d64fd}โหลด{/color}ไฟล์ | " if _is_thai() else "{color=#9d64fd}LOAD{/color} FILES | "):
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


################################################################################
## screen preferences() — settings screen (from common/screens.rpy)
################################################################################

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
                    text ("ระดับเสียงเพลง" if _is_thai() else "MUSIC VOLUME"):
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value Preference("music volume")
                vbox:
                    text ("ระดับเสียงบรรยากาศ" if _is_thai() else "AMBIENCE VOLUME"):
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value MixerValue("ambience")
                vbox:
                    text ("ระดับเสียงเอฟเฟกต์" if _is_thai() else "SOUND VOLUME"):
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value Preference("sound volume")
                vbox:
                    text ("ความเร็วข้อความ" if _is_thai() else "DIALOGUE SPEED"):
                        font "fonts/Orbitron-Black.ttf"
                        size 25
                        color "f8f8f8"
                        text_align 1.0
                    bar value Preference("text speed")
                vbox:
                    text ("ความเร็วเล่นอัตโนมัติ" if _is_thai() else "AUTOPLAY SPEED"):
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
                text ("การแสดงผล" if _is_thai() else "SCREEN DISPLAY"):
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
            text ("ยังทำอยู่ หึๆ" if _is_thai() else "still a wip hehe"):
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


################################################################################
## screen album() — gallery/achievements screen (from misc/gallery.rpy)
################################################################################

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
            text ("ผมของ Ren คือ..." if _is_thai() else "REN'S HAIR IS..."):
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
                    text "- {s}ไปให้ถึงวันถัดไป{/s}" style "notepad"
                else:
                    text ("- ไปให้ถึงวันถัดไป" if _is_thai() else "- Make it to the next Day") style "notepad"
                if persistent.d1_badending == True:
                    text "- {s}ได้รับตอนจบ Dead End{/s}" style "notepad"
                else:
                    text ("- ได้รับตอนจบ Dead End" if _is_thai() else "- Obtain a Dead End") style "notepad"
                if persistent.d1_inviteren == True:
                    text "- {s}ชวนคนแปลกหน้ามาที่บ้าน{/s}" style "notepad"
                else:
                    text ("- ชวนคนแปลกหน้ามาที่บ้าน" if _is_thai() else "- Invite a stranger to your place") style "notepad"
                if persistent.d1_sleepoutside == True:
                    text "- {s}ให้ Ren นอนบนโซฟา{/s}" style "notepad"
                else:
                    text ("- ให้ Ren นอนบนโซฟา" if _is_thai() else "- Make Ren sleep on your couch") style "notepad"
                if persistent.d1_blocknumber == True:
                    text "- {s}บล็อกเบอร์ของ Ren{/s}" style "notepad"
                else:
                    text ("- บล็อกเบอร์ของ Ren" if _is_thai() else "- Block Ren's number") style "notepad"
            if gallery_day == "02":
                if persistent.d2_ending_gooding == True:
                    text "- {s}ไปให้ถึงวันถัดไป{/s}" style "notepad"
                else:
                    text ("- ไปให้ถึงวันถัดไป" if _is_thai() else "- Make it to the next Day") style "notepad"
                if persistent.d2_badending == True:
                    text "- {s}ได้รับตอนจบ Dead End{/s}" style "notepad"
                else:
                    text ("- ได้รับตอนจบ Dead End" if _is_thai() else "- Obtain a Dead End") style "notepad"
                if persistent.d2_visitren == True:
                    text "- {s}ไปเยี่ยมอพาร์ตเมนต์ของ Ren{/s}" style "notepad"
                else:
                    text ("- ไปเยี่ยมอพาร์ตเมนต์ของ Ren" if _is_thai() else "- Visit Ren's apartment") style "notepad"
                if persistent.d2_visitangel == True:
                    text "- {s}กลับไปอพาร์ตเมนต์ของคุณกับคนที่นัด{/s}" style "notepad"
                else:
                    text ("- กลับไปอพาร์ตเมนต์ของคุณกับคนที่นัด" if _is_thai() else "- Go back to your apartment with your date") style "notepad"
                if persistent.d2_killolivia == True:
                    text "- {s}รู้เรื่องการเสียชีวิตของใครบางคน{/s}" style "notepad"
                else:
                    text ("- รู้เรื่องการเสียชีวิตของใครบางคน" if _is_thai() else "- Learn about someone's death") style "notepad"
            if gallery_day == "03":
                if persistent.d3_ending_gooding == True:
                    text "- {s}ไปให้ถึงวันถัดไป{/s}" style "notepad"
                else:
                    text ("- ไปให้ถึงวันถัดไป" if _is_thai() else "- Make it to the next Day") style "notepad"
                if persistent.d3_badending == True:
                    text "- {s}ได้รับตอนจบ Dead End{/s}" style "notepad"
                else:
                    text ("- ได้รับตอนจบ Dead End" if _is_thai() else "- Obtain a Dead End") style "notepad"
                if persistent.d3_declinedate == True:
                    text "- {s}ปฏิเสธคำชวนของใครบางคน{/s}" style "notepad"
                else:
                    text ("- ปฏิเสธคำชวนของใครบางคน" if _is_thai() else "- Decline someone's proposition") style "notepad"
                if persistent.d3_meetmoth == True:
                    text "- {s}คุยกับเพื่อนออนไลน์สนิท{/s}" style "notepad"
                else:
                    text ("- คุยกับเพื่อนออนไลน์สนิท" if _is_thai() else "- Talk to your online bestie") style "notepad"
                if persistent.d3_inviteover == True:
                    text "- {s}ชวนใครบางคนมาที่อพาร์ตเมนต์{/s}" style "notepad"
                else:
                    text ("- ชวนใครบางคนมาที่อพาร์ตเมนต์" if _is_thai() else "- Invite someone to your apartment") style "notepad"
                if persistent.d3_scareren == True:
                    text "- {s}พยายามทำให้ Ren ตกใจ{/s}" style "notepad"
                else:
                    text ("- พยายามทำให้ Ren ตกใจ" if _is_thai() else "- Try and scare Ren") style "notepad"
            if gallery_day == "04":
                if persistent.d4_ending_gooding == True:
                    text "- {s}ไปให้ถึงวันถัดไป{/s}" style "notepad"
                else:
                    text ("- ไปให้ถึงวันถัดไป" if _is_thai() else "- Make it to the next Day") style "notepad"
                if persistent.d4_badending == True:
                    text "- {s}ได้รับตอนจบ Dead End{/s}" style "notepad"
                else:
                    text ("- ได้รับตอนจบ Dead End" if _is_thai() else "- Obtain a Dead End") style "notepad"
                if persistent.d4_visitangel == True:
                    text "- {s}กลับบ้านก่อนพายุจะมา{/s}" style "notepad"
                else:
                    text ("- กลับบ้านก่อนพายุจะมา" if _is_thai() else "- Go home before the storm hits") style "notepad"
                if persistent.d4_snooparound == True:
                    text "- {s}แอบดูรอบๆ อพาร์ตเมนต์ของ Ren{/s}" style "notepad"
                else:
                    text ("- แอบดูรอบๆ อพาร์ตเมนต์ของ Ren" if _is_thai() else "- Snoop around Ren's apartment") style "notepad"
                if persistent.d4_killteo == True:
                    text "- {s}รู้เรื่องการเสียชีวิตของใครบางคน{/s}" style "notepad"
                else:
                    text ("- รู้เรื่องการเสียชีวิตของใครบางคน" if _is_thai() else "- Learn about someone's death") style "notepad"
                if persistent.d4_icecream == True:
                    text "- {s}ไปกินไอศกรีมกับเพื่อนสมัยเด็ก{/s}" style "notepad"
                else:
                    text ("- ไปกินไอศกรีมกับเพื่อนสมัยเด็ก" if _is_thai() else "- Get some ice-cream with your childhood friend") style "notepad"
            if gallery_day == "05":
                if persistent.d5_ending_gooding == True:
                    text "- {s}ไปให้ถึงวันถัดไป{/s}" style "notepad"
                else:
                    text ("- ไปให้ถึงวันถัดไป" if _is_thai() else "- Make it to the next Day") style "notepad"
                if persistent.d5_badending == True:
                    text "- {s}ได้รับตอนจบ Dead End{/s}" style "notepad"
                else:
                    text ("- ได้รับตอนจบ Dead End" if _is_thai() else "- Obtain a Dead End") style "notepad"
                if persistent.d5_visitviolet == True:
                    text "- {s}ขอความช่วยเหลือจากเพื่อนบ้าน{/s}" style "notepad"
                else:
                    text ("- ขอความช่วยเหลือจากเพื่อนบ้าน" if _is_thai() else "- Ask your neighbour for some help") style "notepad"
                if persistent.d5_dismissren == True:
                    text "- {s}ขอให้ Ren ปล่อยคุณไป{/s}" style "notepad"
                else:
                    text ("- ขอให้ Ren ปล่อยคุณไป" if _is_thai() else "- Ask Ren to leave you alone") style "notepad"
                if persistent.d5_visitren == True:
                    text "- {s}ไปเยี่ยมอพาร์ตเมนต์ของ Ren{/s}" style "notepad"
                else:
                    text ("- ไปเยี่ยมอพาร์ตเมนต์ของ Ren" if _is_thai() else "- Visit Ren's apartment") style "notepad"
                if persistent.d5_kickfigure == True:
                    text "- {s}เตะใครบางคนที่ขา{/s}" style "notepad"
                else:
                    text ("- เตะใครบางคนที่ขา" if _is_thai() else "- Kick someone in the leg") style "notepad"

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
                        text ("ชื่อผู้ใช้" if _is_thai() else "USERNAME"):
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
                        text ("รหัสผ่าน" if _is_thai() else "PASSWORD"):
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
                        text ("{color=#FF66CB}{size=+5}ชื่อ:{/size}{/color} REN ({font=FlowBlock-Regular.ttf}LMAO YOU_THOUGHT{/font})" if _is_thai() else "{color=#FF66CB}{size=+5}NAME:{/size}{/color} REN ({font=FlowBlock-Regular.ttf}LMAO YOU_THOUGHT{/font})") style "terminal_button"
                    else:
                        text ("{color=#FF66CB}{size=+5}ชื่อ:{/size}{/color}{font=FlowBlock-Regular.ttf} REN (LMAO YOU_THOUGHT){/font}" if _is_thai() else "{color=#FF66CB}{size=+5}NAME:{/size}{/color}{font=FlowBlock-Regular.ttf} REN (LMAO YOU_THOUGHT){/font}") style "terminal_button"
                    if persistent.fact_dob == True:
                        text ("{color=#FF66CB}{size=+5}วันเกิด:{/size}{/color} ???" if _is_thai() else "{color=#FF66CB}{size=+5}DOB:{/size}{/color} ???") style "terminal_button"
                    else:
                        text ("{color=#FF66CB}{size=+5}วันเกิด:{/size}{/color}{font=FlowBlock-Regular.ttf} 00/00/XXXX{/font}" if _is_thai() else "{color=#FF66CB}{size=+5}DOB:{/size}{/color}{font=FlowBlock-Regular.ttf} 00/00/XXXX{/font}") style "terminal_button"
                    if persistent.fact_job == True:
                        text ("{color=#FF66CB}{size=+5}อาชีพ:{/size}{/color} โปรแกรมเมอร์ฟรีแลนซ์" if _is_thai() else "{color=#FF66CB}{size=+5}OCCUPATION:{/size}{/color} FREELANCE PROGRAMMER") style "terminal_button"
                    else:
                        text ("{color=#FF66CB}{size=+5}อาชีพ:{/size}{/color}{font=FlowBlock-Regular.ttf} โปรแกรมเมอร์ฟรีแลนซ์{/font}" if _is_thai() else "{color=#FF66CB}{size=+5}OCCUPATION:{/size}{/color}{font=FlowBlock-Regular.ttf} FREELANCE PROGRAMMER{/font}") style "terminal_button"
                    ## unlockable stuff (surely there's an easier way to do this?????? lawd)
                    text ("{color=#FF66CB}{size=+5}\nข้อมูลที่ทราบ:{/size}{/color}" if _is_thai() else "{color=#FF66CB}{size=+5}\nKNOWN FACTS:{/size}{/color}") style "terminal_button"
                    if persistent.fact_tempermentshy == True:
                        text ("- ขี้อายและเงอะงะ เหมือน Haruko จาก \"ATTACK ON GIANTS\"" if _is_thai() else "- TIMID AND AWKWARD, LIKE HARUKO FROM \"ATTACK ON GIANTS\"") style "terminal_button"
                    else:
                        text ("- {font=FlowBlock-Regular.ttf}ขี้อายและเงอะงะ เหมือน Haruko จาก \"ATTACK ON GIANTS\"{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}TIMID AND AWKWARD, LIKE HARUKO FROM \"ATTACK ON GIANTS\"{/font}") style "terminal_button"
                    if persistent.fact_mannerism1 == True:
                        text ("- เกาคางเวลาไม่มั่นใจหรือไม่สบายใจ" if _is_thai() else "- SCRATCHES AT JAW WHEN UNSURE OR UNCOMFORTABLE") style "terminal_button"
                    else:
                        text ("- {font=FlowBlock-Regular.ttf}เกาคางเวลาไม่มั่นใจหรือไม่สบายใจ{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}SCRATCHES AT JAW WHEN UNSURE OR UNCOMFORTABLE{/font}") style "terminal_button"
                    if persistent.fact_mannerism2 == True:
                        text ("- ดึงแขนเสื้อเวลาวิตกกังวล" if _is_thai() else "- PICKS AT SLEEVES WHEN ANXIOUS") style "terminal_button"
                    else:
                        text ("- {font=FlowBlock-Regular.ttf}ดึงแขนเสื้อเวลาวิตกกังวล{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}PICKS AT SLEEVES WHEN ANXIOUS{/font}") style "terminal_button"
                    if persistent.fact_food == True:
                        text ("- อาหารโปรดคือสตรอว์เบอร์รี่สวีตโรล" if _is_thai() else "- FAVOURITE FOOD IS STRAWBERRY SWEETROLL") style "terminal_button"
                    else:
                        text ("- {font=FlowBlock-Regular.ttf}อาหารโปรดคือสตรอว์เบอร์รี่สวีตโรล{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}FAVOURITE FOOD IS STRAWBERRY SWEETROLL{/font}") style "terminal_button"
                    if persistent.fact_drink == True:
                        text ("- เครื่องดื่มโปรดคือกาแฟดำ" if _is_thai() else "- FAVOURITE DRINK IS BLACK COFFEE") style "terminal_button"
                    else:
                        text ("- {font=FlowBlock-Regular.ttf}เครื่องดื่มโปรดคือกาแฟดำ{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}FAVOURITE DRINK IS BLACK COFFEE{/font}") style "terminal_button"
                    if persistent.fact_cosmetics == True:
                        text ("- ใช้คอนซีลเลอร์และย้อมผม" if _is_thai() else "- USES CONCEALER AND HAIR DYE") style "terminal_button"
                    else:
                        text ("- {font=FlowBlock-Regular.ttf}ใช้คอนซีลเลอร์และย้อมผม{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}USES CONCEALER AND HAIR DYE{/font}") style "terminal_button"

                    if persistent.fact_residence == True:
                        text ("- อาศัยอยู่ในย่านดีของ Corland Bay" if _is_thai() else "- LIVES IN THE BETTER PARTS OF CORLAND BAY") style "terminal_button"
                        text ("- พักอยู่ที่ Sunshine Hills Apartments" if _is_thai() else "- HAS A RESIDENCY AT SUNSHINE HILLS APARTMENTS") style "terminal_button"
                    else:
                        text ("- {font=FlowBlock-Regular.ttf}อาศัยอยู่ในย่านดีของ Corland Bay{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}LIVES IN THE BETTER PARTS OF CORLAND BAY{/font}") style "terminal_button"
                        text ("- {font=FlowBlock-Regular.ttf}พักอยู่ที่ Sunshine Hills Apartments{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}HAS A RESIDENCY AT SUNSHINE HILLS APARTMENTS{/font}") style "terminal_button"
                    if persistent.fact_awy == True:
                        text ("- สนใจ \"ALWAYS WITH YOU\"" if _is_thai() else "- HAS AN INTEREST IN \"ALWAYS WITH YOU\"") style "terminal_button"
                    else:
                        text ("- {font=FlowBlock-Regular.ttf}สนใจ \"ALWAYS WITH YOU\"{/font}" if _is_thai() else "- {font=FlowBlock-Regular.ttf}HAS AN INTEREST IN \"ALWAYS WITH YOU\"{/font}") style "terminal_button"
                    textbutton ("{size=+10}ออกจากระบบ{/size}" if _is_thai() else "{size=+10}LOG OUT{/size}") text_style "terminal_button" action ToggleVariable("persistent.terminal_unlocked") align (0.5,0.5) at choice_fade

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
