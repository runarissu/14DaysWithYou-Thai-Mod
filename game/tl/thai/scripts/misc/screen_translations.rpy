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
            text ("\"14 Days With You\" เป็นเดโมของเกมแนวสยองขวัญ/โรแมนติกที่กำลังจะวางจำหน่าย และมีไว้สำหรับผู้เล่นอายุ 18 ปีขึ้นไป เนื้อเรื่องจะเข้มขึ้นเรื่อยๆ เมื่อตอนใหม่ออก ผู้เล่นควรใช้ดุลยพินิจด้วยตนเอง\n\n{color=#9d64fd}{b}เดโมนี้มี:{/b}{/color} คำพูดหยาบคายเล็กน้อย สยองขวัญ ความรุนแรง และธีมที่น่าขนลุบ เช่น การถูกตามตัว ความรุนแรง ความตาย และการฆาณกรรม รวมถึงข้อความที่ลาตา การสั่นของหน้าจอ และอาจทำให้ผู้ที่มีอาการชักแบบไวต่อแสงเกิดอาการชักได้ ดูรายการเตือนเนื้อหาทั้งหมดได้ที่ {a=https://cutiesai.com/14dwy}คลิกที่นี่{/a}\n" if _is_thai() else "\"14 Days With You\" is a demo for an upcoming horror/romance game, and is intended to be played by those who are 18 and older. Themes will get darker as more \"Days\" are released. Player discretion is advised.\n\n{color=#9d64fd}{b}THIS DEMO INVOLVES:{/b}{/color} mild coarse language, horror, gore, and unsettling themes such as being stalked, violence, death, and murder. It also involves eye-straining text, screen shakes, and the potential to cause seizures for those with photosensitive epilepsy. For the full list of content warnings, please {a=https://cutiesai.com/14dwy}click here{/a}.\n"):
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
