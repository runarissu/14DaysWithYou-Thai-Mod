label unlockables:
    $ unlockable = unlockable.lower()
    if unlockable == "starshine":
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}[player]...?{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Teo's been looking for you...{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...He won't be for long.{/color}{/size}{/font}{/sc}{fast}" with dissolve
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day1
    if unlockable == "sunpup":
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}[player]...?{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Jae and Leon have been asking about you...{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...Not if I can help it.{/color}{/size}{/font}{/sc}{fast}" with dissolve
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day1
    if unlockable == "froggydacted":
        $ froggy_switch = True
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Woag?{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Wadda hell!!!!{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Who turned me into a froggy png???{/color}{/size}{/font}{/sc}{fast}" with dissolve
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day1
    if unlockable == "meowdacted":
        $ ren_outfit = "meow"
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}bea? is that you?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}haaah~ i've missed you, beatrix!{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}i've missed you so, so, so, so, so, so much!{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}i hope you don't mind, but while\nyou were gone, i... well...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}i may have borrowed one of your jackets...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}sorry. but it smells just like you,\nand i've missed you so much.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}and when i wear it...\nit feels like you're hugging me.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}it's like you're here with me.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}please don't leave me alone again...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}but now that you're back, i should\nlet you play the game, huh?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}alright then. in that case...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}i can't wait to show you\nhow much i've missed you, angel ^^{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day1
    if unlockable == "kitsune":
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Is it...?{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Is it really you?{/color}{/size}{/font}{/sc}{fast}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...I finally found you again, my beloved...{/color}{/size}{/font}{/sc}{fast}" 
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day0_foxren
    if unlockable == "sleeeeepybug":
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Oh? Hello again, [player].{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Are you here to record me? If so...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Hello to all of [player]'s friends on the internet! ^^{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Make sure you're nice and comfy for us, okay?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Maybe even get yourself a tasty drink to enjoy.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...Hey. Why don't we drink it together? That's what couples do, right?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=4}{font=fonts/VT323-Regular.ttf}{size=+33}{color=#f553a9}H-Haaaah... ^^{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=6}{font=fonts/VT323-Regular.ttf}{size=+35}{color=#d30f1e}...Would you like that, [player]?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=3}{font=fonts/VT323-Regular.ttf}{size=+33}{color=#f553a9}Ahem. I should probably calm down now.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Alright. Have fun playing my game, angel!{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...Until next time.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day1
    if unlockable == "espoirduvide":
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Oh? I've missed you, Espoir.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Are you going to record me again? In that case...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Hello internet! ^^{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}Make sure you subscribe to Espoir's channel for me, okay?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}That way, you'll be able to see me more often!{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...And I'll be able to see you, too...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=3}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}So don't hide from me ^^{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=4}{font=fonts/VT323-Regular.ttf}{size=+33}{color=#f553a9}...Why are you hiding from me?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=7}{font=fonts/VT323-Regular.ttf}{size=+35}{color=#d30f1e}Are you scared of me?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=8}{font=fonts/VT323-Regular.ttf}{size=+40}{color=#a30b11}...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...Haha, just kidding~! Have fun, angel!{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day1
    if unlockable == "helloyinny":
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}[player]? i've missed you. are you here to record me again?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}hehe~ make sure to capture my good side, then.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}oh! and hello to all of your internet friends as well ^^{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}thank you for watching [player]'s videos\nand taking such good care of [them].{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}i'd say something inspiring like,\n\"subscribing will grant you extra luck on your gacha pulls!\" but...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}i don't want you falling for any dark-haired characters...\nbesides me, of course.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=3}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}in fact, i've got another \"Blade\" i can show you later... ^^{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=4}{font=fonts/VT323-Regular.ttf}{size=+33}{color=#f553a9}heh... i'm just kidding.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=3}{font=fonts/VT323-Regular.ttf}{size=+40}{color=#f553a9}...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}alright, i'll let you go now.\ni hope you have fun playing, angel!{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day1
    if unlockable == "epykslion":
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}oh? [player]? are you going to record me again?{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}well then... I'll have to make sure you get my good side.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}not you, though. you always look... perfect.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}even if your glasses are slightly askew right now, hehe~{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}i can see you, you know? ^^{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...oh, as well as all your subscribers\nwho are currently watching us right now.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=3}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}i guess we're not alone now, huh? in that case...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=4}{font=fonts/VT323-Regular.ttf}{size=+33}{color=#f553a9}thank you for showing all your love and support for my [player].{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=8}{font=fonts/VT323-Regular.ttf}{size=+40}{color=#a30b11}but don't worry... i'll take it from here...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=4}{font=fonts/VT323-Regular.ttf}{size=+33}{color=#f553a9}...{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}I can't wait to show how much I've missed you, angel.{/color}{/size}{/font}{/sc}{fast}{p=3}" with dissolve
        pause 0.5
        scene black with GlitchDissolve
        pause 3.0
        jump day1