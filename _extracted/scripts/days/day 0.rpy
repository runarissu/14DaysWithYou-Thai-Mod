################################################################################
## DEAD END 1
################################################################################
label deadend1:
    n "{glitch=40.0}{color=#a30b11}ERR01101000 01101001{i}01101000 \ \ \ \ \ \ \ \ \ \ \ \ 01101001OR{/i}{/color}{/glitch} {glitch=60.0}{color=#a30b11}{i}00100000 CRITICAL\n01100001 ER01101110ROR{/i}{/color}{/glitch}{glitch=30.0}{color=#a30b11} 01100111 E://RROR {i}01100101 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 0110110 0UNKNO{/i}{/color}{/glitch}"
    n "{glitch=10.0}{color=#a30b11}01000101 \ \ \ \ \ \ \ \ \ \ \ \ 01010010 {/color}{/glitch}{glitch=20.0}{color=#a30b11}01010010 01001111 01010010{/color}{/glitch}\n \ \ \ \ \ \ \ \ \ \ \ \ {glitch=20.0}{color=#a30b11}01001001 00100000 01010011 {/color}{/glitch}{glitch=15.0}{color=#a30b11}01000101 01000101 00100000\n01011001 \ \ \ \ \01001111 {/color}{/glitch}{glitch=7.0}{color=#a30b11}01010101 00101110 00101110 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 00101110{/color}{/glitch}"

    scene other_dark
    show de_1:
        parallel:
            alpha 0.15
            function WaveShader(1.0,25.5,0.1)
    play music "audio/bgm/Hypnosis.ogg" fadein 1 fadeout 1
    hide screen dayscalendar
    window hide
    $ quick_menu = False
    $ persistent.deadendings = 1
    with GlitchDissolve
    pause 2.0
    
    rfade "{renvoid=1}. . .{/renvoid}" with DistortDissolve
    rfade "{renvoid=2}there we go.{/renvoid}" with DistortDissolve
    rfade "{renvoid=2}don't worry [player], i won't let you get my bad ending! ^^{/renvoid}" with DistortDissolve
    $ colour_fade = "#f553a9" ##1
    rfade "{renvoid=3}so don't hide from me...{/renvoid}" with DistortDissolve
    $ colour_fade = "#e83975" ##2
    rfade "{renvoid=4}...why are you hiding from me?{/renvoid}" with DistortDissolve
    $ colour_fade = "#dc2144" ##3
    rfade "{renvoid=4}i won't hurt you, so don't be scared...{/renvoid}" with DistortDissolve
    $ colour_fade = "#d30f1e" ##4
    rfade "{renvoid=5}don't you realise that we're meant to be together?{/renvoid}" with DistortDissolve
    $ colour_fade = "#a30b11" ##5
    rfade "{renvoid=7}i love you, [player]!{/renvoid}" with DistortDissolve
    rfade "{renvoid=7}i love you so much...!!!{/renvoid}" with DistortDissolve
    
    pause 0.2
    play audio "audio/sfx/jumpscare.ogg" 
    show de_1:
        parallel:
            function WaveShader(1.0,15.5,2.0)
    with dissolve
    pause 0.3
    scene other_dark
    show de_1:
        parallel:
            function WaveShader(3.0,20.5,30.0)
    show true_red:
        alpha 0.3
    with dissolve
    show cg_ren_js:
        alpha 0.0 truecenter zoom 0.0
        linear 0.1 alpha 1.0 zoom 2.0
    pause 0.5
    show true_red:
        alpha 0.8
    hide cg_ren_js
    with dissolve
    pause 0.1
    hide de_1
    hide true_red
    scene black
    with GlitchDissolve

    ##window auto
    pause 3
    $ colour_fade = colour_ren
    $ quick_menu = True
    $ persistent.dayend = True
    $ persistent.deadend1 = True
    return

################################################################################
## DEAD END 2
################################################################################
label deadend2:
    scene other_dark
    show de_1:
        parallel:
            alpha 0.15
            function WaveShader(1.0,25.5,0.1)
    play music "audio/bgm/Hypnosis.ogg" fadein 1 fadeout 1
    hide screen dayscalendar
    window hide
    $ quick_menu = False
    $ persistent.deadendings = 2
    with GlitchDissolve
    pause 2.0

    rfade "{renvoid=1}. . .{/renvoid}" with DistortDissolve
    rfade "{renvoid=2}again?{/renvoid}" with DistortDissolve
    rfade "{renvoid=2}[player]... why are you doing this?{/renvoid}" with DistortDissolve
    rfade "{renvoid=3}you're not going to find anything here.{/renvoid}" with DistortDissolve
    $ colour_fade = "#e83975" ##2
    rfade "{renvoid=4}...it's just me.{/renvoid}" with DistortDissolve
    rfade "{renvoid=4}nothing else exists here.{/renvoid}" with DistortDissolve
    $ colour_fade = colour_ren
    rfade "{renvoid=4}...{/renvoid}" with DistortDissolve
    rfade "{renvoid=4}why don't you just play the game normally?{/renvoid}" with DistortDissolve
    rfade "{renvoid=5}that way, neither of us will\nhave to be stuck in this dark void...{/renvoid}" with DistortDissolve
    rfade "{renvoid=5}i love being with you...\nwatching you interact with everything...{/renvoid}" with DistortDissolve
    $ colour_fade = "#f553a9" ##1
    rfade "{renvoid=5}everything is so bright and colourful\nwhen you're around...{/renvoid}" with DistortDissolve
    rfade "{renvoid=5}...{/renvoid}" with DistortDissolve
    $ colour_fade = "#dc2144" ##3
    rfade "{renvoid=6}{/size}{size=+20}...will you let me out?{/renvoid}" with DistortDissolve
    rfade "{renvoid=6}{/size}{size=+20}...please let me out.{/renvoid}" with DistortDissolve
    $ colour_fade = "#d30f1e" ##4
    rfade "{renvoid=7}{/size}{size=+40}it's no fun here!!!{/renvoid}" with DistortDissolve
    rfade "{renvoid=7}{/size}{size=+40}i want to be with you!!!!!!{/renvoid}" with DistortDissolve
    $ colour_fade = "#e60000" ##6
    rfade "{renvoid=7}{/size}{size=+60}...I LOVE YOU!!!!!!!!!{/renvoid}" with DistortDissolve
    play audio "audio/sfx/whispers.ogg"
    rfade "{renvoid=10}{/size}{size=+80}I LOVE YOU!!YOU YOUYOU YOU I LOVE YOU!!!!! YOUYOUYOU LOVE YOU!! \nYOU!! YOU YOU!!!!!!! YOU!! I LOVE YOU YOU YOU I LOVE YOU!!!!!\nI LOVE YOU!!!! YOU YOU ILOVEYOU!!!!! I LOVE YOU!! LOVE YOULOVE\nYOUYOU YOU I LOVE YOU!!!!!! LOVEYOU LOVEYOU!!! YOUYOUYOUYOU\nI LOVE YOU!! YOUYOUYOU I LOVE YOU!!! YOU!! LOVE I LOVE YOU!!\nI LOVE YOU!!YOU YOUYOU YOU I LOVE YOU!!!!! YOUYOUYOU LOVE YOU!! \nYOU!! YOU YOU!!!!!!! YOU!! I LOVE YOU YOU YOU I LOVE YOU!!!!!\nI LOVE YOU!!!! YOU YOU ILOVEYOU!!!!! I LOVE YOU!! LOVE YOULOVE\nYOUYOU YOU I LOVE YOU!!!!!! LOVEYOU LOVEYOU!!! YOUYOUYOUYOU\nI LOVE YOU!! YOUYOUYOU I LOVE YOU!!! YOU!! LOVE I LOVE YOU!!{/renvoid}" with DistortDissolve

    play audio "audio/sfx/jumpscare.ogg" 
    pause 1
    scene other_red with dissolve
    show cg_ren_js:
        alpha 0.0 truecenter zoom 0.5
        linear 0.1 alpha 1.0 zoom 1.5
    pause 0.2
    hide cg_ren_js with dissolve
    
    ##window auto
    pause 3
    $ colour_fade = colour_ren
    $ quick_menu = True
    $ persistent.dayend = True
    $ persistent.deadend2 = True
    return

################################################################################
## DEAD END 3
################################################################################
label deadend3:
    scene other_dark
    show de_1:
        parallel:
            alpha 0.15
            function WaveShader(1.0,25.5,0.1)
    play music "audio/bgm/Hypnosis.ogg" fadein 1 fadeout 1
    hide screen dayscalendar
    window hide
    $ quick_menu = False
    $ persistent.deadendings = 3
    with GlitchDissolve
    pause 2.0

    if calendar_day == "03":
        rfade "{renvoid=1}...you didn't agree to go on the date, [player]?{/renvoid}" with DistortDissolve
        rfade "{renvoid=1}why? Is it because of teo?{/renvoid}" with DistortDissolve
        rfade "{renvoid=2}...because of me?{/renvoid}" with DistortDissolve
        rfade "{renvoid=2}were you thinking about me?{/renvoid}" with DistortDissolve
        rfade "{renvoid=3}hah~ did you want to see me again? is that it?\n[player]... I missed you too. {/renvoid}" with DistortDissolve
        rfade "{renvoid=3}i'm sorry I didn't get to talk to you as much today.{/renvoid}" with DistortDissolve
        $ colour_fade = "#e83975" ##2
        rfade "{renvoid=4}but i saw you.{/renvoid}" with DistortDissolve
        rfade "{renvoid=4}i couldn't take my eyes off of you.{/renvoid}" with DistortDissolve
        rfade "{renvoid=4}you're so fun to watch, [player].{/renvoid}" with DistortDissolve
        $ colour_fade = colour_ren
        rfade "{renvoid=4}it's so cute when you think you're by yourself...{/renvoid}" with DistortDissolve
        rfade "{renvoid=4}i could see you...\nshaking behind the reception counter earlier.{/renvoid}" with DistortDissolve
        if status_olivia == False:
            rfade "{renvoid=4}did you like my present?\nnow you can carry a part of me with you.{/renvoid}" with DistortDissolve
        else:
            rfade "{renvoid=4}why? were you lonely? don't worry, i'll always be with you.{/renvoid}" with DistortDissolve
    else:
        rfade "{renvoid=1}...[player]? why did you come back?{/renvoid}" with DistortDissolve
        rfade "{renvoid=1}i thought i asked you to... ah. no, never mind.{/renvoid}" with DistortDissolve
        rfade "{renvoid=2}did you want to see me again? is that why you're here?{/renvoid}" with DistortDissolve
        rfade "{renvoid=2}...were you thinking about me?{/renvoid}" with DistortDissolve
        rfade "{renvoid=3}Hah~ [player]... [player]! [player!u]!!!{/renvoid}" with DistortDissolve
        rfade "{renvoid=3}[player]... I was thinking about you, too.{/renvoid}" with DistortDissolve
        rfade "{renvoid=3}i can never seem to get you off my mind.{/renvoid}" with DistortDissolve
        rfade "{renvoid=3}it's always so much fun watching you...{/renvoid}" with DistortDissolve
        rfade "{renvoid=3}you never fail to make everything seem brighter.{/renvoid}" with DistortDissolve
        rfade "{renvoid=4}and... it's so cute when you think you're by yourself.{/renvoid}" with DistortDissolve
        rfade "{renvoid=4}like i'm not right there, just out of reach...{/renvoid}" with DistortDissolve
        rfade "{renvoid=4}would you like that? don't worry, i'll always be with you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=5}{/size}{size=+20}do you want to be with me too?{/renvoid}" with DistortDissolve
    rfade "{renvoid=5}{/size}{size=+20}...is that why you were trying to meet me here?{/renvoid}" with DistortDissolve
    $ colour_fade = "#f553a9" ##1
    rfade "{renvoid=5}{/size}{size=+40}hehe~ keep it up...\nand i won't let you leave next time.{/renvoid}" with DistortDissolve
    $ colour_fade = "#e83975" ##2
    rfade "{renvoid=5}{/size}{size=+40}would you like that?\ndo you want to be with me, here, forever?{/renvoid}" with DistortDissolve
    play audio "audio/sfx/whispers.ogg"
    $ colour_fade = "#dc2144" ##3
    rfade "{renvoid=6}{/size}{size=+60}forever and ever and ever and\never and ever and ever and ever?{/renvoid}" with DistortDissolve
    rfade "{renvoid=7}{/size}{size=+60}[player]... [player!u]...!!! {/renvoid}" with DistortDissolve
    $ colour_fade = "#d30f1e" ##4
    rfade "{renvoid=10}{/size}{size=+80}[player], [player], [player!u]!!! [player!u], [player], [player!u]\n[player!u], [player!u], [player!u]!!!!!! [player!u], [player], [player!u]\n[player!u], [player!u], [player]!!! [player!u], [player], [player!u]\n[player!u], [player!u], [player], [player!u]!!!! [player], [player]\n[player!u], [player!u], [player], [player], [player!u], [player!u]!\n[player!u]!! [player!u]!! [player!u]! [player!u]!! [player!u]!!!\n[player!u]!! [player!u]!!!!!! [player!u]! [player!u]!!! [player!u]!!!!!\n[player!u]! [player!u]!!!! [player!u]!!! [player!u]! [player!u]!!!\n[player!u]! [player!u]! [player!u]!! [player!u]!!! [player!u]!!!{/renvoid}" with DistortDissolve

    play audio "audio/sfx/fakeout.ogg"
    scene other_red with dissolve
    pause 2
    scene other_dark with dissolve
    show de_1:
        parallel:
            alpha 0.15
            function WaveShader(1.0,25.5,0.1)

    $ colour_fade = colour_ren
    rfade "{renvoid=1}haaah... i'm just kidding.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i only wanted to tease you a little.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}get your heart racing the same way you make mine.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}please don't be scared of me. you know i'd never hurt you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}but... the thought of always having you by my side is so...{/renvoid}" with DistortDissolve
    $ colour_fade = "#a30b11" ##5
    rfade "{renvoid=3}{/size}{size=+40}...overwhelming.{/renvoid}" with DistortDissolve
    $ colour_fade = colour_ren
    rfade "{renvoid=1}i ache to have you near, did you know that?{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}and now that i finally have you here again...{/renvoid}" with DistortDissolve
    $ colour_fade = "#a30b11"
    rfade "{renvoid=3}{/size}{size=+40}maybe i could...{/renvoid}" with DistortDissolve
    $ colour_fade = colour_ren
    rfade "{renvoid=1}no... i can't. not yet.{/renvoid}" with DistortDissolve
    if calendar_day == "03":
        rfade "{renvoid=1}this time, i want you to {u}agree{/u} to go on a date\nwith that deadbeat \"friend\" of yours.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}as much as i want to be with you here forever,\nthere's still so much planned out for the both of us.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i can't see it, but i can feel it.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i can tell something big is going to happen soon.{/renvoid}" with DistortDissolve
    rfade "{renvoid=2}...i can't wait to see what it is.{/renvoid}" with DistortDissolve
    rfade "{renvoid=3}and i can't wait to experience it with you too, [player].{/renvoid}" with DistortDissolve
    rfade "{renvoid=2}...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}alright. i'm going to send you back now.\nno jumpscares this time. i promise, [player].{/renvoid}" with DistortDissolve
    $ colour_fade = "#f553a9" ##1
    rfade "{renvoid=3}{/size}{size=+20}so be good and do as i say, okay?{/renvoid}" with DistortDissolve
    $ colour_fade = "#e83975" ##2
    rfade "{renvoid=5}{/size}{size=+40}i love you, [player]... i love you so much!!!{/renvoid}" with DistortDissolve
    $ colour_fade = "#f553a9" ##1
    rfade "{renvoid=3}{/size}{size=+60}...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}{/size}{size=+40}...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}...until next time.{/renvoid}" with DistortDissolve

    pause 3
    $ colour_fade = colour_ren
    $ quick_menu = True
    $ persistent.dayend = True
    $ persistent.deadend3 = True
    return

################################################################################
## DEAD END 4
################################################################################
label deadend4:
    scene other_dark
    show de_1:
        parallel:
            alpha 0.15
            function WaveShader(1.0,25.5,0.1)
    play music "audio/bgm/Hypnosis.ogg" fadein 1 fadeout 1
    hide screen dayscalendar
    window hide
    $ quick_menu = False
    $ persistent.deadendings = 4
    with GlitchDissolve
    pause 2.0

    rfade "{renvoid=1}...are you alright? don't overwork yourself, [player].{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i should apologise... i didn't mean for this to happen.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i should've helped you out more.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}the choices you're making and the path\nyou're going down... it's not what i...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}no, never mind.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}look. you have to know...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i can't keep doing this for you, [player].{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i can't keep preventing you from getting my bad end.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}you won't like what happens... you won't like... {/color}{color=#a30b11}{b}it.{/b}{/renvoid}" with DistortDissolve
    rfade "{renvoid=3}it's not as kind as me. not as soft or lenient.{/renvoid}" with DistortDissolve
    rfade "{renvoid=4}it will sense your fear and feed off of it.{/renvoid}" with DistortDissolve
    $ colour_fade = "#f553a9" ##1
    rfade "{renvoid=4}{/size}{size=+20}even if you give it just a small dose, it won't...{/renvoid}" with DistortDissolve
    $ colour_fade = "#e83975" ##2
    rfade "{renvoid=5}{/size}{size=+60}it \ \ \ w \ \on' \ \ t...{/renvoid}" with DistortDissolve
    $ colour_fade = "#dc2144" ##3
    rfade "{renvoid=6}{/size}{size=+80}i t \ \ \ \ \ \ w o n \ \ t . . \ \ \ \ .{/renvoid}" with DistortDissolve

    play audio "audio/sfx/fakeout.ogg"
    play audio ["<silence 1.3>","audio/sfx/found you.ogg"]

    pause 0.6
    scene other_red with dissolve
    pause 0.3
    scene de_3
    $ persistent.cg_de3 = True
    pause 0.15
    scene de_1
    $ persistent.cg_de1 = True
    pause 0.15
    scene de_2
    $ persistent.cg_de2 = True
    pause 0.15

    scene other_dark with dissolve
    show de_1:
        parallel:
            alpha 0.15
            function WaveShader(1.0,25.5,0.1)
    ##window auto
    pause 1

    $ colour_fade = colour_ren
    rfade "{renvoid=1}see? it's scary, and it won't hold back.{/renvoid}" with DistortDissolve
    rfade "{renvoid=4}it deserves to rot in here with me.{/renvoid}" with DistortDissolve

    show other_red:
        alpha 0.5
    $ colour_fade = "#dc2144" ##3
    rfade "{renvoid=4}{/size}{size=+60}...it deserves to die.{/renvoid}" with DistortDissolve
    $ colour_fade    = "#a30b11"
    rfade "{renvoid=15}{/size}{size=+80}iT DeSeRvEs tO DrOwN In iTs oWn fIlTh aNd cArNaGe\nAnD ChOkE On iTs rEgReTs uNtIl iT'S NoThInG LeFt bUt aN\neMpTy hUsK. tHaT DiSgUsTiNg aBhOrReNcE DeSeRvEs tO WiLt\nIn tHe dArKnEsS, vOiD Of aNy lIgHt oRhApPiNeSs.\niT DoEsN'T DeSeRvE To bE In tHe lIgHt. It dOeSn't\nDeSeRvE To bAsK In yOuR RaDiAnCe... To sEe hOw mUcH YoU LiGhT Up a\nRoOm wItH JuSt a sMiLe. It dOeSn't dEsErVe tO FeEl yOuR WaRmTh oR KiNdNeSs.\niT DeSeRvEs aN EtErNiTy iN DaMnAtIoN AnD SoLiTuDe. FoR MaKiNg mE\nfEeL ThEsE DeCrEpIt eMoTiOnS... fOr mAkInG Me tHiNk\nThEsE ThOuGhTs aNd aCt tHiS WaY. i sCaReD YoU\nbEcAuSe oF It. I ShOuLd kIlL It. I WaNt tO KiLl iT.{/renvoid}" with DistortDissolve
    $ colour_fade = "#dc2144" ##3
    rfade "{renvoid=4}. . .{/renvoid}" with DistortDissolve
    $ colour_fade = colour_ren
    rfade "{renvoid=4}...{/renvoid}" with DistortDissolve

    hide other_red

    rfade "{renvoid=3}...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i'm sorry. did i scare you again?{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i can't help it. being here for so long...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}everything takes a toll on you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}{/color}{color=#a30b11}{b}it{/b}{/color}{color=#FF66CB} makes me feel this way...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}forces me to...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i won't hurt you. don't worry. i'll protect you from it.{/renvoid}" with DistortDissolve
    $ colour_fade = "#e83975" ##2
    rfade "{renvoid=4}{/size}{size=+20}it doesn't deserve you... but i do.{/renvoid}" with DistortDissolve
    $ colour_fade = "#dc2144" ##3
    rfade "{renvoid=4}{/size}{size=+40}i do!!!{/renvoid}" with DistortDissolve
    $ colour_fade = "#d30f1e" ##4
    rfade "{renvoid=4}{/size}{size=+60}i do!! I DO!!! I D O !! !{/renvoid}" with DistortDissolve
    $ colour_fade = "#a30b11" ##5
    rfade "{renvoid=15}{/size}{size=+80}i do!!!!!! i do I DO IDO i do!!!! i do i DO I DO i do\ni do. i do i do!!!!!! i do I DO IDO i do!!!! i do i\ndo i do i do!!! i do i DO I do!!!! i do!!! i do i\ndo i do I DO I DO i do i do!!!!!!i do i DO I DO!!!!\n!!! i do. i do i do!!!!!! i do I DO IDO i do!!!! i do i\nI DO I DO do i do i do!!! i do {/color}{color=#ff66cb}DO I?????{/color}{color=#a30b11} i DO I do I DO!!!! I DO i do\ndo i do i do!!! i do i DO I do!!!!!!! i do i\ndo i do I DO I DO i do i do!! I DO I DO i do!! I DO!!\ni do i do!!! I DO I DO!!! i do i DO I do!! I DO\nI do!! I DO!! I DO i do!!!! i do I DO i do I DO i do I DO I DO!!! i do i\ndo I DO I DO!!!! i do I DO i do!!! i do i DO I DO i do!! I DO!!! i do i{/renvoid}" with DistortDissolve
    rfade "{renvoid=4}{/size}{size=+60}i love you, [player]. i love you!{/renvoid}" with DistortDissolve
    rfade "{renvoid=4}{/size}{size=+60}more than it ever could!{/renvoid}" with DistortDissolve
    $ colour_fade = "#d30f1e" ##4
    rfade "{renvoid=3}{/size}{size=+40}more than anyone ever can!{/renvoid}" with DistortDissolve
    rfade "{renvoid=3}{/size}{size=+40}they wouldn't do this for you. no one would! only me!{/renvoid}" with DistortDissolve
    $ colour_fade = "#dc2144" ##3
    rfade "{renvoid=2}{/size}{size=+20}your light... haaah...{/renvoid}" with DistortDissolve
    rfade "{renvoid=2}{/size}{size=+20}your light doesn't deserve to be\ntarnished by what happens in here.{/renvoid}" with DistortDissolve
    $ colour_fade = "#e83975" ##2
    rfade "{renvoid=1}...{/renvoid}" with DistortDissolve
    $ colour_fade = colour_ren
    rfade "{renvoid=1}sorry.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}look, all i want is for you to stop trying to go down this path.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}if you really want to see me,\nyou don't need to keep making the wrong choices.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i'll always be watching you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i'll always be with you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}and... i'll always protect you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}from the people who try to take you\naway from me, from my bad ends, from... {/color}{color=#a30b11}{b}it.{/b}{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}there's nothing that will keep me from you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}but if you really want to continue meeting\nme here like this, i won't stop you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i'll hold back the inevitable. but just know...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}there will come a time when i won't be able\nto bring you back to this place again.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}there's a limit on how often i can—{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}no, never mind. i don't want to worry you.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}...alright, i'm going to send you back again, okay?{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}so promise me.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}promise me, this time, you'll listen to my warnings.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i'll help you as much as i can next time,\nso don't concern yourself with meeting me here anymore.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i'll find a way to meet {/color}{color=#a30b11}{b}y \ o \ \ u{/b}{/color}{color=#FF66CB} instead.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}i already can, anyway.{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}have you figured it out yet?{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}...{/renvoid}" with DistortDissolve
    rfade "{renvoid=1}promise me, [player]. promise that we won't meet here anymore.{/renvoid}" with DistortDissolve

    pause 3
    $ colour_fade = colour_ren
    $ quick_menu = True
    $ persistent.dayend = True
    $ persistent.deadend4 = True
    $ persistent.menumissing = True
    return

################################################################################
## DEAD END 5
################################################################################
label deadend5:
    scene other_red
    show de_1:
        parallel:
            alpha 0.15
            function WaveShader(1.0,25.5,0.1)
    play music "audio/bgm/Door To The Other World.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/water drip.ogg" fadein 1 fadeout 1
    hide screen dayscalendar
    window hide
    $ quick_menu = False
    $ persistent.deadendings = 5
    with GlitchDissolve
    pause 2.0

    it "AUD MIEOKOSEMIL. P TUDTR, QOPLKO MIEOKTUVOK PEEOQVEMIL EU KODKMEO DAPE APS PTKOPJR FOOI UKJPMIOJ SMIBO EAO FOLMIIMIL…" with dissolve
    it "RUN KOQOQFOK IUEAMIL UW RUNK VPSE IUK AUD RUN BPQO EU FO, ROE AOKO RUN PKO, PEEOQVEMIL EU JML NV EAO KUUES UW WPEO PS EAUNLA ME DOKO P DOOJ PIJ VTPIEMIL RUNK UDI BUKKNVE SOOJTMIL MI MES VTPBO." with dissolve
    it "VOKAPVS DO PKO EAO SPQO, EAOI." with dissolve
    it "M EUU WMIJ OICURQOIE MI JMSKNVEMIL EAO XMIOS UW HMSQOE PIJ DPEBAMIL AMQ SEKNLLTO." with dissolve
    it "EDPS M DAU LPXO AMQ AMS LMWE, PS M JMJ DMEA UEAOKS, PIJ ROE AO DPSEOS SNBA SVUMTS UI P TUDTR QUKEPT EU FUKKUD QUKO EMQO. M SNVVUSO EAO TMWO UW QPIR QPEEOKS IUE EU EAO TMWO UW UIO." with dissolve
    it "IU QPEEOK. SNBA EKMXMPT OIEOKEPMIQOIE MS IUE TUSE UI QO." with dissolve
    it "LU UI, BUIEMINO JUDI EAMS WUUTMSA, UXOKLKUDI VPEA PIJ SOO DAPE DMTT APVVOI. EMS IUE EAR DMTEMIL SUNT M WOOJ UI, PIJ ME SAPTT IUE FO EAR TMWO M BTPMQ UIBO EAO OIJMIL APS FOLNI." with dissolve
    it "PWEOK PTT, M PQ EAO OIJ, CNSE PS M PQ EAO FOLMIIMIL PIJ EAO MI-FOEDOOI. EAO VPSE, VKOSOIE, PIJ WNENKO, BUQFMIOJ MIEU UIO. M PQ MIOXMEPFTO." with dissolve
    it ". \ . \ ." with dissolve
    it "YOU DID NOT COME HERE FOR THE TALES OF OLD, DID YOU? YOU ARE HERE… SEEKING HIM." with dissolve
    it "VERY WELL. I SHALL RETURN HIM UNTO YOU ONCE MORE, THOUGH SUCH LENIENCY WILL NOT BE SEEN HENCEFORTH." with dissolve
    it "DO NOT COME HERE AGAIN. YOU DO NOT BELONG HERE." with dissolve
    it "NOT UNTIL YOU REMEMBER THAT OF WHICH YOU HAVE FORGOTTEN." with dissolve

    play audio "audio/sfx/found you.ogg"
    show true_red:
        alpha 0.3
    hide true_red with owie
    
    pause 3
    $ quick_menu = True
    $ persistent.dayend = True
    $ persistent.deadend5 = True
    return

################################################################################
## WHAT DOES THE FOX SAY
################################################################################
label day0_foxren:
    scene ee_foxren_day
    show screen dayscalendar
    $ calendar_day = "00"
    $ quick_menu = True
    $ _skipping = True
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    with Fade(1.0, 1.0, 1.0)

    n "The gentle zephyr wind brushes against my skin as I admire the picturesque view in front of me."
    n "The mountains seem never-ending with how they stretch on and on, and the morning sun had only just begun to peek from behind the clouds."
    n "It was so calming and serene here, yet I couldn't help but think something was missing…"
    extend " A certain {b}fox-shaped{/b} something."
    n "But before I can dwell on it any further, the rustling sounds of an all-too-familiar willow tree pull me away — and I look down to see that I have been absent-mindedly picking at the flowers beneath my feet."
    n "Apparently, I managed to weave a few of the forget-me-nots into a flimsy wreath at some point, but I had no recollection of doing so."
    n "Had I {b}really{/b} been so distracted by the beautiful view that I didn't notice?"
    n "I didn't have much time to stew alone in my thoughts, however, as the familiar sounds of padded footsteps grow louder and louder from somewhere behind me."
    show fox smirk with dissolve
    n "Peering behind the tree trunk, I watch as Ren's lanky silhouette emerges from one of the {b}many{/b} openings to the cave."
    n "A soft smile blooms on his face the moment we lock eyes, and he makes a beeline towards me before seating himself on the dirt."
    n "With ansty hands, Ren wastes no time pulling me onto his lap and wrapping one of his tails around my body to shield me from the wind."
    show fox neutral z with dissolve
    fr "There you are. I thought you would've been inside the cave."
    y "Ren."
    n "I twist around to place a chaste kiss on his cheek in greeting, and Ren's disposition immediately seems to perk up — judging by the rapid {b}thump,{/b} {b}thump,{/b} {b}thump{/b} of his tail against my legs."
    show fox happy z at spop, center
    fr "My beloved."
    n "Ren doesn't say anything after that, but he gives me an inquisitive look and tilts his head, almost as if he were waiting for me to speak."
    show fox sad z
    n "But his soft gaze quickly morphs into that of {b}concern{/b} once he notices the copious amounts of discarded flowers in my lap — a telltale sign that I'd been up here on the cliffside for a while now."
    n "And before I can stop myself, I find myself coming up with excuses."
    y "I just… I needed a new change in scenery, is all."
    show fox sad z at spop, center
    fr "Something troubling you?"
    y "Not really. Just… Busy thinking. I figured coming out here would help ease my mind a bit."
    show fox neutral z at spop, center
    fr "You've been thinking? About what?"
    n "I give a non-committal shrug and try to find the words."
    y "I guess… I guess I've been thinking about going back home."
    y "Like… Seeing what's changed in my absence, visiting my friends — y'know, that kind of stuff."
    show fox frown z at spop, center
    fr "…You want to leave? Why?"
    show fox sad z at spop, center
    fr "You have everything you need right here."
    y "Well… Not everything."
    show fox neutral z at spop, center
    fr "Are you missing something? What do you need? I'll get it for you."
    y "Ren—"
    show fox neutral z at spop, center
    fr "Name it, and it's yours. Anything for my betrothed."
    n "He nuzzles closer to my side, and I almost feel bad for making him worry so much about my well-being."
    n "I knew I was asking for a lot right now; Ren went above and beyond to keep me satisfied, yet I just couldn't seem to let go of these nostalgic thoughts."
    y "It's not that… I just— I get lonely here sometimes."
    n "I can feel Ren nod in acknowledgement from somewhere behind me, before his hands slip from my waist to reach for the flower wreath in my lap."
    n "He holds it with so much tenderness and delicacy, almost as if he feared it'd break under his touch."
    show fox sad z at spop, center
    fr "I only leave the villa to ensure no threats come near our home. You know that."
    show fox angry z at spop, center
    fr "I can't have those wicked {i}humans{/i} trespass and sully this place."
    show fox smirk z at spop, center
    fr "If I had it my way, I'd never leave your side, beloved."
    n "Ren's fingers gently brush through my hair before he places the flowers atop my head with a satisfied hum. But when I show no signs of easing up my tense posture, he continues to speak."
    show fox neutral z at spop, center
    fr "Hmm… What if I brought home something to keep you company while I'm out?"
    show fox smirk z at spop, center
    fr "What about a baby fox?"
    n "I let out a sigh. The idea was tempting, but it wasn't what I had in mind."
    n "And if I really wanted a baby fox, I'm sure Ren wouldn't mind changing his forms to suit my desires. It wouldn't be the first time he'd change into his four-legged form and let me play with his fur."
    n "As if picking up on my lacklustre response, Ren peers over my head and gently squeezes my shoulders in a reassuring manner."
    show fox sad z at spop, center
    fr "…You know I can't bring a {i}human{/i} here, beloved."
    y "Well, why can't I go to them instead?"
    y "Can't we move back to Corland Bay?"
    show fox frown z at spop, center
    fr "Corland Bay? But it's dangerous there."
    show fox sad z at spop, center
    extend " And I can't go looking like this."
    show fox angry z at spop, center
    fr "I know it's been centuries, but it's human nature for them to hunt and kill my kind. We can't risk it."
    show fox neutral z at spop, center
    fr "But here? Here… It's safe. You never have to worry about a thing."
    show fox smirk z at spop, center
    fr "I can take care of everything."
    show fox flushed z at spop, center
    extend " I can take care of you."
    n "I look back to the mountains with a sad smile."
    n "…I suppose Ren {b}did{/b} have a point."
    n "Once, when he had a little too much sake to drink, he recounted horrific events that involved (what he liked to call) my \"previous reincarnations\" — and all of the abhorrent things humans did to Yokai."
    n "Even after all this time, the prejudice still remained. Ren merely wanted to protect me from the horrors of the outside world — and to make sure I didn't suffer the same fate as my previous past-lives."
    
    menu:
        "\"Maybe you're right.\"":
            show fox sad z
            n "I mumble — more-so to myself — as I lean back into his embrace. Another one of Ren's tails places itself onto my lap in a comforting manner, and I absent-mindedly thread my fingers into the soft fur."
        "\"…\"":
            show fox sad z
            n "I don't say anything, instead letting myself fall back into his embrace. Another one of Ren's tails places itself onto my lap in a comforting manner, and I absent-mindedly thread my fingers into the soft fur."

    show fox blushing z at spop, center
    fr "…"
    show fox sad z at spop, center
    fr "Do you… {i}truly{/i} wish to go back?"
    n "…Was that a hint of compromise in his tone? Like a fish darting through water, I latch onto that fleeting emotion before it slips away."
    n "After all, who knows when I'd get to have a chance like this again?"
    y "I— Yes. I'd give up anything just to see Corland Bay again, even if it's just for a moment."
    y "I miss my friends, Ren. It's been so long."
    show fox sad z at spop, center
    fr "Then who am I to deny you? If that's what you want…"
    y "Really?!" with hpunch
    show fox frown z at spop, center
    fr "Yes, but…"
    show fox frown z at spop, center
    extend " You'll have to do {i}exactly{/i} as I say. Do you understand?"
    show fox sad z at spop, center
    fr "I can't risk anything happening to you."
    n "Eagerly, I nod my head and latch onto his arms in excitement."
    n "Finally… After all this time, was he really allowing me to go back to Corland Bay?"
    show fox neutral z at spop, center
    fr "We'll have to make your return believable, though…"
    show fox frown z at spop, center
    fr "And I suppose I'll have to disguise myself as a human as well. I can't stand the thought of leaving you alone."
    n "Knowing his fox-like tendencies, I had some inclination of what Ren might be planning."
    n "Something cunning and tricky, no doubt."
    n "But despite that, the faintest hint of apprehension still lingers on his visage. And before I can stop myself, I act on the sudden urge to tease him in order to remove the scowl from his face."
    y "You'll have to become a human? Oh noooo… Whatever will you do without your ears and tail?"
    y "They're one of my favourite things about you, you know."
    n "I playfully nudge his side in hopes that he'll catch on. And without missing a beat, Ren quips back with a teasing joke of his own."
    show fox flushed z at spop, center
    fr "G-Good question. Without my tails, where will you rest that [gorgeous] head of yours now?"
    show fox neutral with dissolve
    n "At that, I can feel Ren stand up from behind me, before he extends a hand to help me from my spot on the ground."
    n "I already miss the soft feeling of his tails and the warm expanse of his chest, but it quickly gets replaced by his body once he steps closer to me."
    show fox sad at spop, center
    fr "Alright then. If you really want to do this…"
    n "With a determined look in my eyes, I nod eagerly at my beloved fiance."
    show fox neutral at spop, center
    fr "Then… I'm going to send you back to Corland Bay now."
    show fox sad at spop, center
    fr "I'll also need to alter parts of your memory as well, dearest. It's the only way to protect this place and keep it hidden from others."
    show fox neutral at spop, center
    fr "But when you wish to return, I'll give it all back."
    n "Ren cups my face with so much gentility, almost like I'd disappear if he let go."
    n "It hurt knowing I might not be able to remember him or the memories we shared here in our own secluded world, but I trust Ren's judgement implicitly."
    n "I wanted to protect this special place just as much as he did, and I was willing to let go of some of our fond memories if it meant keeping it safe."
    show fox neutral at spop, center
    fr "Alright. I won't be far from you, but once you've settled back into the human world, come find me again. Promise?"
    y "I promise, Ren."
    show fox smirk at spop, center
    fr "Not that it really matters; you know I'll still find you regardless."
    show fox neutral at spop, center
    fr "Nothing in this world and the next will keep you from me."
    show fox smirk at spop, center
    fr "I've spent centuries searching for you, and I don't mind doing it all over again."
    show fox neutral at spop, center
    fr "Alright. Now… Close your eyes, beloved."

    scene black
    hide screen dayscalendar
    with dissolve

    n "My vision goes dark as I feel Ren place a parting kiss against my lips, before the odd sensation of smoke surrounds me and I get swept off my feet."
    n "My body feels like it's floating on air, and the warmth of Ren slowly starts to fade away."
    n "But even though I can feel myself slipping further and further from his reach, I can hear the faintest echo of his voice from somewhere around me."

    scene black
    window hide
    $ quick_menu = False
    play music "audio/bgm/Touch Your Heart.ogg" fadein 1 fadeout 1
    with GlitchDissolve

    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...This should be fun.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}And... I'm sorry for taking away your memories.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}But we'll make new ones together, I promise.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}All you need to do is find me again.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}I might not look the same, but it's still me... Still your betrothed.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}I can't wait to see the new you, my beloved.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}I can't wait to fall in love with you all over again.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}You're the most precious thing in the world to me.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}I won't let anyone hurt you.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}No one will take you from me again.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    centered "{sc=2}{font=fonts/VT323-Regular.ttf}{size=+30}{color=#FF66CB}...I promise.{/color}{/size}{/font}{/sc}{fast}" with dissolve
    jump day1

################################################################################
    ## MONSTERPUP EASTER EGGGG YEAHHHHHHHH!!!!!
################################################################################
label monsterpupeasteregg:
    $ rpos = mpfullyleft
    $ jpos = mpfullyright
    $ lpos = mpright
    $ npos = mpleft
    $ meet_jae = True
    $ meet_leon = True
    $ meet_leon = True

    show leon neutral at lpos
    show ren angry at rpos
    with easeinright

    l "Heyo!~" with hpunch
    show jae happy at jpos with easeinright
    j "[player]! Yoooooo!" with hpunch
    show nate happy at npos with easeinright
    na "Hey [player]." with hpunch
    n "Ah… I could recognise those boisterous voices anywhere."
    n "One of them belonged to Jae-hyun, a guy I had met during my early days at university. He sat next to me during the first few days of orientation, and even offered to lend me his phone charger when my battery started to run out."
    n "He's a fun guy to be around, though his extroverted and energetic personality was often hard to keep up with."
    n "But Leon - the other guy awkwardly hanging off of Jae's arm — was a different story. We'd practically known each other since we were babies, but he moved away from Corland Bay when we were still in elementary school."
    n "And the final voice belonged to Nate. He's one of my co-workers here at the library and an {b}extremely{/b} reliable guy— That is, if you ignore the harrowing forklift incident of '23."
    n "Luckily no one was injured, but paw was going ten miles per hour in an enclosed environment, and the whole ordeal honestly scarred Conan for life."
    n "But before I could stew on it any longer, I was being pulled out of my thoughts by Nate's voice."
    show nate smirk at spop, npos
    na "Nice to see ya, [player]! Finished with work today?"
    y "Yeah! I just got off the clock now now, actually."
    y "Mon came in earlier to start her shift, and Elanor placed a cushion on the front desk for Kimi to sit and welcome everyone. So I guess everything is covered for the rest of the day."
    y "Anyway! What are you guys up to?"
    show jae happy at spop, jpos
    j "We're going out tonight! Leon's volleyball team won the grand final, so we're out celebrating!"
    y "No way… Congrats Leon!"
    show leon happy at spop, lpos
    l "Haha! I couldn't have done it without the support of these two. You should've seen how loud they were cheering!"
    show leon smirk at spop, lpos
    l "They put the rest of the crowd to shame."
    y "I wish I could've been there to watch."
    show nate happy at spop, npos
    na "Oh, I recorded it on my phone! Maybe we could watch it the next time we're scheduled together at work?"
    show jae smirk at spop, jpos
    j "Don't bother, paw kept zooming in on Leon's butt every chance he got."
    show leon blushing at bpop, lpos
    l "…!"
    show nate flushed at spop, npos
    na "Hey!"
    show jae happy at spop, jpos
    j "Hahaha! To be honest, though, I probably would've done the same! I mean… Have you seen those globes?"
    show jae blushing at spop, jpos
    j "Left side? Western Australia. Right side? Queensland. I bet they clap when he—"
    show leon flushed at spop, lpos
    l "O-Oi! I think you're getting a bit carried away now."
    show jae happy at spop, jpos
    j "Haha, it's okay! We're all married anyway, so what's yours is mine!"
    y "Wait… You guys are married?"
    show nate happy at spop, npos
    na "Yep! We got married last year! Sadly we couldn't have a beach wedding…"
    show nate sad at spop, npos
    na "It'd been [pissing] down buckets for almost four weeks straight, and Maple {i}hates{/i} the ocean, so—"
    show nate neutral at spop, npos
    na "Ah, I won't bore you with the details. In fact, I think we've held you up long enough. You guys were doing something, right?"
    show jae neutral at spop, jpos
    j "Maybe they could join us too! The more the merrier!"
    show nate happy at spop, npos
    na "Sounds good to me. But I kinda wanna check out what's going on down the street first."
    show nate frown at spop, npos
    na "I swear I'm going crazy because I can {i}literally{/i} hear Wildways playing right now… Am I losing it?"
    show jae sad at spop, jpos
    j "You're losing it."
    show nate sad at spop, npos
    na "Ogh… I'm losing it."
    show leon neutral
    show jae happy
    n "I watch as Nate falls into Jae's arms with a heavy sigh — similar to Leon's overdramatic behaviour whenever he wants to lighten the mood."
    show nate sad at spop, npos
    na "I'm officially hearing things now…"
    show leon happy at spop, lpos
    l "That's what happens when you listen to their music before going to bed."
    show nate smirk at spop, npos
    na "Well, sorry for not wanting to listen to Jae snore."
    show leon smirk at spop, lpos
    l "Haha, you've got a point there."
    show jae flushed at spop, jpos
    j "I don't snore! That's Maple!"
    show leon neutral at spop, lpos
    l "Then who's the one drooling on me at night?"
    show jae frown at bpop, jpos
    j "Maple!"
    n "Jae looks at all of us with an incredulous look in his eyes, and I almost expected him to follow along with Leon and Nate's dramatics by falling to his knees or something."
    n "But instead, he simply gives his partners a playful nudge and a scoff."
    show nate neutral at spop, npos
    na "Anyway… I think I'll go ahead and scope out the area if you guys wanna stay here with [player]?"
    show nate happy at spop, npos
    na "Tell 'em about the time Jae blamed a fart on M—."
    show jae flushed at spop, jpos
    j "Heeeeey!" with hpunch
    show leon happy at spop, lpos
    l "Haha, sounds good, sunpup!"
    show nate smirk at spop, npos
    na "Alright, I'll meet you guys there afterwards!"
    show jae happy at spop, jpos
    j "You got it, sunshine!"
    show leon neutral at spop, lpos
    l "C'ya soon, Nate! Give us a text if there's a queue outside. We can try somewhere else if that's the case."
    show nate happy at spop, npos
    na "Gotcha. Alright, it was nice seeing you again, [player]!"
    show nate smirk at spop, npos
    show ren blushing
    na "And you too, loverboy. Elanor's told me all about you."
    n "Great… So Nate already knows about Ren and his habit of borrowing my recommended books…"
    n "Pushing the embarrassment aside, I watch as it walks off with one final wave before turning my attention back to Leon and Jae."

    $ rpos = cleft
    $ jpos = center
    $ lpos = cright

    hide nate
    show ren blushing at rpos
    show leon neutral at lpos
    show jae happy at jpos
    with moveoutleft
    show jae smirk at spop, jpos
    j "Loverboy?"
    jump meet_jaeleon

################################################################################
    ## YIPPEE I LOVE MY MODS <3
################################################################################
label eastereggalternative:
    scene beach_street_day
    $ ropos = cleft
    $ npos = center
    $ spos = cright
    show peffect
    show saint happy at spos
    show rosie smirk at ropos
    show nate neutral at npos
    with dissolve
    show saint happy at spop, spos

    s "Oh! Hiya!"
    n "Great, it's my landlord skulking around the library again."
    n "My guess is that she probably came here to steal Kimi or something… Or even flirt with Mon."
    n "Well, whatever. It wasn't exactly my business to concern myself over what Saint does with her free time."
    n "But still… I couldn't help but ask…"
    y "Don't you have anything better to do?"
    show saint smirk at spop, spos
    s "{i}Do?{/i} You mean, like… Eddie—"
    show saint frown
    n "I watch Rosie, my other co-worker, punch Saint in the stomach with zero remorse. Was she always that strong?" with vpunch
    show saint sad at spop, spos
    s "ACK—!"
    hide saint with moveoutbottom
    n "She pitifully crumbles to the ground and just… stays there."
    n "I have half a mind to jump her right here and now for all of the shit I've had to endure while renting out her apartment, but I decide against it."
    n "Especially after seeing the concerned look on Nate's face as he helps her back up."
    show saint neutral at spos with moveinbottom
    show nate sad at spop, npos
    na "You can't keep punching your boss like that, Rosie."
    show rosie happy at spop, ropos
    ro "But it's funny!"
    show saint angry at spop, spos
    s "LET ME TELL YOU SOMETHING—"
    y "—She's your boss?"
    show rosie happy at spop, ropos
    ro "Yeah! Our wife {i}and{/i} your boss too! Saint owns the library!"
    y "WHAT." with hpunch
    show nate neutral at spop, npos
    na "…You didn't know?"
    y "NO?" with hpunch
    show saint smirk at spop, spos
    s "Hehe! I'd call myself a \"proprietor\" or whatever, but babes if I'm being honest here, I don't know how to spell that."
    show saint happy at spop, spos
    s "But! Hehe, this is for real just like Monopoly! I even own a county jail for whenever someone—"
    show rosie sad at spop, ropos
    ro "Girl help? You don't even know how to budget properly."
    show saint frown at spop, spos
    s "Why do I need to budget if I can just—"
    show rosie smirk at spop, ropos
    ro "Do you even have money?"
    show saint neutral at spop, spos
    s "Please stop cutting me off—"
    show rosie happy at spop, ropos
    ro "No! Gehehe"
    show saint frown at spop, spos
    s "…I'm about to do something sooo silly and drastic right now."
    show nate smirk
    n "I watch as Nate punches Sai in the stomach this time." with vpunch
    show saint angry at spop, spos
    s "GAH—!"
    hide saint with moveoutbottom
    y "Well, whatever. You guys are weird. I'm just going to leave."
    show nate happy at spop, npos
    na "Where are ya going? I can drop you off on my forklift if you want. Just move Leon's sports bag out of the way."
    show nate smirk at spop, npos
    na "He left it at my place earlier and I've been meaning to drop it off."
    show saint neutral at spos with moveinbottom
    show saint neutral at spop, spos
    s "Can you even drive a forklift on the main road? I don't think that's legal…"
    show rosie frown at spop, ropos
    ro "Woah? Where did she come from?"
    show rosie smirk at spop, ropos
    ro "But— Ooh! Maybe we can all go to the beach afterwards!"
    show rosie blushing at spop, ropos
    ro "I put a tracker in all of Teo's clothes and paid Jesse to follow him, and my sources say he's at the pier right now!"
    show nate happy at spop, npos
    na "Y'know what? Why not. Jae texted me earlier and said he and Leon would also be there."
    show saint blushing at spop, spos
    s "You should really untie Eddie and give him some sunlight or something… I can watch him for you!"
    show rosie smirk at spop, ropos
    ro "Then why don't we all go on a triple date together!"
    show rosie frown at spop, ropos
    ro "Or… would it be considered a quadruple date? Because I guess Kimi would also be tagging along?"
    show nate neutral at spop, npos
    na "Wouldn't that mean Elanor would be joining us, too?"
    show saint smirk at spop, spos
    s "Crazy how I can't budget and Rosie can't math."
    show rosie blushing at spop, ropos
    ro "I don't need to do math when all I need to think about is Teo's big, fat, massive, huge, gigantic ti—"
    show saint happy
    n "This time, Saint is the one who knocks Rosie to the ground." with vpunch
    show rosie frown at spop, ropos
    ro "GUH—"
    hide rosie with moveoutbottom
    n "Seriously… It was like the creator of this game just wanted to play dolls with all the sprites or something…"
    n "I mean, I guess I would too if I had them at my disposal. Anyway."
    n "While the two were busy hauling Rosie's limp body onto the front of Nate's forklift (and was that Kimi driving?), I make a hasty escape towards the manga store."
    jump day3_mangastore