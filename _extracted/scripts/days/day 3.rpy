################################################################################
## DAY 3 YAHOOOOOOOO >_<!!
################################################################################
label day3:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Currently playing Day 3',
                'state': 'I can see you, Angel...',
                'large_image_key': '14dwy_logo',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

    show screen dayscalendar
    show screen versionscreen
    $ quick_menu = True
    $ _skipping = True
    $ calendar_day = "03"
    $ skipday = "day4"

    $ update_ren = "arghhh… so much to do todav ;;"
    $ update_jae = "Maple found her bag of dog treats again orz"
    $ update_leon = "wow, why is the hospital so busy today?"

    $ location_elanor = "library"
    $ location_conan = "library"
    $ location_jae = "random"
    $ location_violet = "pier"
    $ location_leon = "random"
    $ location_teo = "home"
    $ location_olivia = "work"
    $ location_ren = "home"

    if death_flag == "olivia":
        $ death_flag = "hehe"
        $ status_olivia == False
    else:
        $ update_olivia = "i'm too cute to reject! (delulu)"

    if d2_visitren == True:
        $ ren_outfit = "lounge"
        jump day3_renmorning
    else:
        $ ren_outfit = "normal"
        jump day3_alonemorning

################################################################################
## WAKING UP AT REN'S PLACE WHY AM I YELLING AAAAAAAAAAAA
################################################################################
label day3_renmorning:
    scene ren_spareroom_day
    show peffect
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/street.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)

    n "The unusual sounds of city life and traffic pull me away from my slumber, and I wake to the sight of an unfamiliar ceiling."
    n "This… wasn't my bedroom? And this certainly wasn't my bed."
    n "Last I checked, my duvets were a patterned purple — a house-warming gift from [ch_violet] when I first moved into my apartment — not this dark shade of black."
    n "Confused, I rub the sleep from my eyes in order to fully take in the rest of the room. And just like that, memories from yesterday come flooding back."

    if d2_wahooren == True:
        call DLC_day3_s1 from _call_DLC_day3_s1
    else:
        n "Oh… Right. [ch_ren] offered to let me stay the night due to the freak storm that swept over Corland Bay. It was sweet of him to do, and it had me wondering where he was right now."
        n "Was he still fast asleep? Or perhaps he was already awake?"

    n "Deciding there's no time like the present to find out; I stretch out the knots in my body, wake myself up fully, and jump out of bed."

    ################################################################################
    ## he's a chef ur honour *explodes the apartment*
    ################################################################################
    scene ren_misc_day
    stop ambience fadeout 2.0
    play audio "audio/sfx/movement.ogg"
    show peffect
    with GlitchDissolve

    n "As soon as I walk out into the hallway, the mouthwatering scent of something sweet and sugary greets me, and it almost has my feet floating towards the kitchen."
    n "Curiosity — or perhaps hunger — takes over my body; and before I know it, I find myself navigating through the maze of [ch_ren]'s stupidly large apartment."
    n "Speaking of the devil…"

    scene ren_kitchen_day
    show peffect
    with GlitchDissolve

    show ren blushing with dissolve
    n "There, [ch_ren] stands in his kitchen; hunched over the stove with a spatula in one hand, and what looks to be a recipe pulled up on his phone in the other."
    n "He doesn't seem to notice my presence yet, so I take the opportunity to study him a little bit more."
    n "And although I could only see most of his backside and side profile, I could easily make out the concentrated look on his face as his gaze flits back and forth between his phone and the pan."
    n "But just when I think he's about to turn around, [ch_ren] lets out a surprised noise and immediately lifts the pan from the stove."

    show ren angry at bpop, center
    if persistent.streamermode == True:
        r "Jeez!" with vpunch
    else:
        r "Fuck!" with vpunch
        n "Hearing [ch_ren] swear so casually was still something I had to get used to — but that wasn't what made me speechless right now…"

    n "Sniffing the air, the smell of something burning invades my nostrils and has me retreating back into the living space for some fresh air."
    n "…Wow. Did [ch_ren] {b}really{/b} manage to burn a pancake? Or maybe he just wasn't that confident in cooking?"
    n "Regardless, seeing him put so much effort into something so trivial did manage to pull at my heartstrings."
    n "Deciding I've had my fill of watching [ch_ren], I finally make myself known."
    
    #hide ren with dissolve

    menu:
        #with dissolve
        "Hug him from behind":
            $ ren_purity -= 1
            $ affection_ren += 1
            $ affection_olivia += 1
            show ren angry with dissolve
            n "Quietly tiptoeing behind the taller man, I wait for the perfect opportunity to strike before wrapping my arms around his waist and resting my head on his broad backside."
            show ren flushed at bpop, center
            r "{size=+10}…[player_fl]-[player_fl]-[ch_angel]?!{/size}" with vpunch
            show ren blushing at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
            r "I didn't hear you— I… Um…"
            n "Despite his flustered outburst, [ch_ren] doesn't seem to move from my hold. In fact, he almost seems to melt and lean into my touch instead."
            n "Almost as if to confirm my thoughts, I feel him wrap one of his arms around my waist to pull me in for a brief hug."
        "Try and scare him":
            $ affection_ren -= 1
            $ affection_moth += 1
            $ affection_jae += 1
            $ affection_teo += 1
            $ persistent.d3_scareren = True
            show ren angry with dissolve
            n "Quietly tiptoeing behind the taller man and hiding behind the counter, I wait for the perfect opportunity to strike."
            n "That moment arrives once he turns around to scrape the burnt remnants of pancake into the bin, and before [ch_ren] has any time to react, I spring into action."
            y "{size=+10}BOO!{/size}" with hpunch
            show ren flushed at bpop, center
            r "{size=+10}…A-Angel?!{/size}" with vpunch
            show ren flushed at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
            r "You scared me! H-How long have you—"
            n "Despite his flustered outburst, [ch_ren] doesn't seem to move away from the stove."
        "[rh_o]Call out his name[rh_c]":
            $ affection_ren += 1
            $ affection_elanor += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            show ren angry with dissolve
            n "Stepping a bit closer, I wait until [ch_ren] turns around to scrape the burnt remnants of pancake into the bin before calling out to him."
            y "[ch_ren]?"
            show ren flushed at bpop, center
            r "{size=+10}…[player_fl]-[player_fl]-[ch_angel]?!{/size}" with vpunch
            show ren blushing at bpop, center
            r "H-How long have you been awake— I… Um…"
            n "Despite his flustered outburst, [ch_ren] doesn't seem to move away from the stove."
        "Don't say anything":
            $ affection_ren -= 1
            $ affection_violet += 1
            $ affection_conan += 1
            $ ren_switch += 1
            show ren angry with dissolve
            n "Okaaaay, so maybe one more second of being sneaky wouldn't hurt. After all, it wasn't often that I get the chance to observe [ch_ren] like this."
            n "But before I can do anything, he breaks the silence once more."
            show ren angry at spop, center
            r "[shit!c]. Y'can't be serious."
            show ren angry at spop, center
            if persistent.streamermode == True:
                r "Out of the entire batch, how did I manage to mess up {i}this{/i} badly—"
            else:
                r "Out of the entire batch, how did I manage to fuck up {i}this{/i} badly—"
            show ren flushed at bpop, center
            r "{size=+10}…A-Angel?!{/size}" with vpunch
            show ren flushed at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
            r "You scared me! H-How long have you—"
            show ren blushing at bpop, center
            r "When did you— I… Um…"
            n "Despite his flustered outburst, [ch_ren] doesn't seem to move away from the stove."
        "{image=14NWY symbol} Slip your hands underneath his shirt" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
            call DLC_day3_kitchen from _call_DLC_day3_kitchen

    show ren neutral at spop, center
    r "Ahem…"
    show ren happy at spop, center
    extend " G-Good morning, [ch_angel]!"
    show ren flushed at spop, center
    r "I was going to surprise you with breakfast in bed. Sorry, did I take too long?"
    n "It was like I flicked an invisible switch, because all of a sudden, [ch_ren] was back to the usual, timid personality that I'd grown to know."
    y "Aw, you don't have to go through all that trouble for me."
    show ren neutral at spop, center
    r "It's fine, I-I wanted to! Really! Um… Here!"
    play audio ["<silence .5>", "audio/sfx/plate.ogg"]
    n "Without giving me a second to spare, [ch_ren] conjures up a plate full of thick, fluffy pancakes from somewhere behind him — alongside a few toppings as well."
    show ren neutral at spop, center
    r "I didn't manage to burn these ones, at least. Eat as much as you'd like!"
    show ren flushed at spop, center
    r "…I'll have this one."
    n "He gestures to the burnt pancake still stuck to the frying pan. No amount of washing and scrubbing would restore that pan to its former glory."
    n "Giving [ch_ren] a pitiful look, I deposit a few fluffy pancakes onto my own plate before offering the rest to him as well."
    y "[ch_ren], you've made enough to feed an army! Why don't we share?"
    show ren happy at spop, center
    r "It's okay! I made them all for you! Exactly how you like them!"
    y "Oh? And how do you know how I like my pancakes?"
    n "Deciding to tease him a little, I throw the light-hearted accusation into the air and hope that he'll catch it."
    show ren sad at spop, center
    r "…Huh? Oh! I-I don't! I just… I suppose—"
    show ren blushing at spop, center
    r "Don't people normally enjoy pancakes this way? I thought maybe—"
    n "There he goes again… Getting flustered beyond belief while his cheeks flush a deep shade of red. It really was adorable."
    y "Relaaaax. I'm only teasing you."
    extend " These pancakes are delicious, by the way."
    show ren flushed at spop, center
    r "O-Oh… You were just joking… Haha~"
    n "His mood immediately seems to perk up once he hears my compliment."
    show ren happy at bpop, center
    r "You like them?! Really? You're not lying? Then…"
    show ren happy at spop, center
    r "Then I'll make them for you again sometime! O-Only if you want, that is!"
    show ren flushed at spop, center
    extend " It's no problem at all!"
    show ren neutral at spop, center
    extend " I really don't mind."
    y "How about you just focus on eating first? Aren't you hungry?"

    if d2_wahooren == True:
        call DLC_day3_s2 from _call_DLC_day3_s2
    else:
        show ren flushed at spop, center
        r "A-Ah, I snacked on a few pancakes while cooking them. Don't worry about me. You just eat!"
        show ren blushing at spop, center
        r "D-Do you want some different toppings? I'm sure I've got more strawberries in the fridge."
        n "Something inside me told me that [ch_ren] was lying about eating already, but I didn't feel like calling him out on it."
        show ren neutral at spop, center
        y "I'm good for now. But thank you. Really."

    n "Seemingly satisfied with my response (or lack thereof), [ch_ren] lets out a pleased hum and instead moves away to busy himself with washing the dishes."
    n "My gaze follows him, and I absent-mindedly catch a glimpse at the clock on one of the shelves — eight o'clock on the dot."
    n "Wait a second… Eight o'clock?! I was going to be late for work!" with vpunch
    show ren sad
    n "As if picking up on my panicked behaviour, [ch_ren] halts his movements and sends me a curious glance."
    y "Crap! I'm going to be late for work again if I don't leave now! I-I still need to walk home and get changed and—"
    show ren frown at spop, center
    r "H-Hey, it's okay, [ch_angel]! Calm down."
    show ren sad at spop, center
    r "Look, your clothes from yesterday are washed and dry."
    show ren smirk at spop, center
    r "Why don't you change into them, and when you're ready, I can drop you off at work?"
    y "[ch_ren]…"
    n "There I go again; relying on this enigma of a man and taking up too much of his kind hospitality."
    n "I was already overstaying my welcome by using his dryer and sleeping in his spare bed — but now here I was — eating his food and being exactly five minutes away from getting a lift in his car."
    n "He really should be the one being called \"angel\" instead of me."
    y "Thank you so much. I owe you my entire life."
    show ren happy at spop, center
    r "Hehe, and I thought {i}I{/i} was dramatic."
    show ren flushed at spop, center
    r "{size=-6}…A-Another date with you will do just fine.{/size}"

    scene ren_misc_day
    show peffect
    play audio "audio/sfx/movement.ogg"
    with GlitchDissolve

    n "His soft smile is the last thing I see before I head back into the guest bedroom to change. But before I can make it three feet away, [ch_ren]'s voice calls out to me once more."
    r "O-Oh, but I should warn you! I don't exactly drive a car…"
    jump day3_libraryscene

################################################################################
## WAKING UP AT HOME
################################################################################
label day3_alonemorning:
    scene angel_bed_day
    show peffect
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)

    n "Almost like clockwork, my body reacts to the all-too-familiar sounds of birds chirping outside my window, and it pulls me from the depths of dreamland."
    n "Groggily, I roll onto my side and reach for my phone on the nightstand. I briefly get flashbanged from the brightness of my screen before squinting my eyes to make out the time."
    n "Glancing at the clock, I realise that I somehow managed to wake up an hour earlier than usual — and that I'd received a few messages from [ch_moth] at some point last night."
    n "Opening them up, I casually begin to skim through them."
    mt "TELL ME you've seen the newest Attack on Giant theories! >:o"
    mt "BIG FAT MASSIVE SPOILER ALERT…"
    extend " Haruko lives?!"
    extend " OUR BOY REALLY SURVIVED THAT MASSIVE BLAST FROM THAT SORCERER!!!"
    mt "LOOK AT THESE PICS! YOU CAN CLEARLY SEE PART OF HIS OUTFIT IN ONE OF THEM."
    mt "HE'S CLEARLY STILL ALIVE!!!" with vpunch
    mt "btw! let me know when ur awake so I can tell you about something suuuuper important…"
    extend " ANYWAY!!!!"
    mt "back to my Haruko theory that I came up with and definitely DID NOT steal from some forum online B-)"
    mt "in this 329 page essay, i will—"
    n "There still seemed to be quite {b}a few{/b} more lengthy messages from [ch_moth] underneath, but I figured I got the overall gist of things already."
    n "In fact… After looking at all these messages, I was beginning to think that [ch_moth] didn't really have anyone else to talk to about Attack On Giants — which didn't really surprise me."
    n "They weren't exactly the best at opening up and getting to know others — let alone with strangers online — so it was a wonder how we managed to become friends in the first place."
    n "Back then, we were both new fans who wanted to fawn over Attack On Giants on some online forum, yet we somehow crossed paths and clicked immediately."
    n "And even now the franchise is {b}still{/b} insanely popular within the anime community; garnering many fans who love to discuss episode theories with others online."
    n "Yet… [ch_moth] always seemed to come to me before anyone else — and for that, I was grateful. I honestly didn't mind in the slightest, and I also got to gush to them about my hyperfixations in return."
    n "But… man. I just wished our time zones would be more lenient."
    n "I always manage to catch [ch_moth] as soon as I'm going to bed, and they always seem to message me while I'm halfway through my sleep cycle."
    n "Welp, there was no use in thinking too much about it."
    n "Putting those thoughts aside for now, I decide to spend the rest of my morning going through the rest of [ch_moth]'s messages instead — and even sending back a few theories of my own — before getting ready for work."
    n "But before I begrudgingly leave the warmth and comfiness of my bed in favour of making breakfast, I make sure to give my new Haruko plushie a squeeze and a pat on the head."
    jump day3_libraryscene

################################################################################
## GOING TO WORK
################################################################################
label day3_libraryscene:
    scene black
    show peffect
    play music "audio/bgm/Refreshing Scent.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)

    if d2_visitren == True:
        if unlockable == "meowdacted":
            $ ren_outfit = "meow"
        else:
            $ ren_outfit = "normal"
        n "Turns out, [ch_ren] didn't actually own a car like I expected. He owned a [damn] {b}sports motorcycle.{/b}"
        $ persistent.fact_awy = True
        n "All black, sleek, and scary — but what surprised me the most were the faded \"Always With You\" sticker decals that adorned the tank."
        n "So [ch_ren] was a fan of that webcomic as well?"
        n "I always assumed the community was rather small — there wasn't much talk about the webcomic online — so it was nice to know someone else enjoyed it as much as I did."
        n "But just as I was about to bring the topic up, my vision goes dark as [ch_ren] places a helmet over my head with a smile."
        n "He fastens and adjusts the strap before motioning towards the back of his bike with an expectant look."
        n "Admittedly, I was a bit hesitant to hop on that thing, but [ch_ren] assured me that he'd tell me what to do and keep me safe the entire time."
        play audio "audio/sfx/ignition.ogg"
        n "\"Daunting\" couldn't even begin to describe how I felt when the engine turned on — and I was certain [ch_ren] had scratch marks with how tightly I was clinging to him — but I somehow came out of it unscathed."
        n "I even managed to bag myself a nice, warm hoodie that smelled like [ch_ren] — even if its only purpose was to protect me from the wind and flying debris."
        n "And when we parted in front of the library with a friendly goodbye, [ch_ren] waited until I was inside the building before taking off."
    else:
        n "With a full stomach and a slight bounce in my step, I casually make my way towards the Corland Bay Library."
        n "Even from here, I could make out [ch_elanor]'s fancy \"welcome!\" message written on the chalkboard sign, and from the looks of the parking situation outside, it didn't seem that busy… yet."
        n "What captures my interest, however, is a black sports motorbike propped up in one of the parking spots."
        n "I could make out a ton of small anime decals on the tank, but what really catches my attention were the \"Always With You\" stickers."
        n "Whoever owned that bike must've been a fan of the webcomic, and it made me want to be their friend because of it. Because as unfortunate as it is, the only person I had to talk to about this was [ch_moth]."
        n "But it made a lot of sense, considering how \'Always With You\" was only published recently, and the fandom was still so small. Not many people were aware of its existence, but that was slowly starting to change."
        n "Physical copies of the webcomic were starting to appear in stores, and despite my attempts, I had yet to get my hands on one."
        extend " Oh well. Maybe one day."
        n "Now wasn't the time to be dwelling on these things… I would've been late for work if I stayed in my head any longer."
        n "Not wasting any more time, I quickly speed up the stairs and enter the library."

    n "But I barely make it three feet inside before a mess of blonde hair enters my field of view and almost knocks me over."

################################################################################
## SEEING ELANOR AGAIN YIPEE MY WIFE!!
################################################################################
label day3_elanorscene:
    scene library_reception_day
    play ambience "audio/ambience/library.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve
    $ update_elanor = "What has been happening lately? This is not okay! :("

    play audio "audio/sfx/item.ogg"
    show elanor sad z at bpop, center
    e "[ch_angel]! There you are! Quick, I need your help!" with vpunch
    n "[ch_elanor]'s anxious demeanour catches me off guard, and I immediately do a sweep of the library for anything out of place."
    n "But I'm hardly given any time to take in my surroundings before [ch_elanor] reaches for my arm and all but {b}drags{/b} me behind the reception counter and towards a mountain of paperwork."
    play audio "audio/sfx/heels alt.ogg"
    show elanor sad with dissolve
    n "Stacks upon stacks of books, files, newspapers, and manilla folders cover the entire expanse of their desk — and for the briefest moment, it almost resembled a messy archive repository rather than her workstation."
    y "…What's all this?"
    show elanor frown at spop, center
    e "{i}This{/i} was supposed to be sorted out yesterday! I swear I did it already…"
    show elanor sad at spop, center
    e "In fact, I know I did!"
    show elanor frown at spop, center
    e "I remember leaving it all in [ch_conan]'s office before I left work yesterday — so you can imagine my surprise when I saw it back on my desk this morning!"
    n "[ch_elanor] seems genuinely concerned, especially with how she's flitting about and pacing back and forth in front of me."
    n "It was almost like she'd seen a ghost, and if I didn't know any better, I honestly would've believed it."
    show elanor sad at spop, center
    e "Please help me! If [ch_conan] finds out I somehow messed up again, I don't know what will happen!"
    y "Hey, hey. Don't worry El, I'll help."
    y "And I doubt [ch_conan] will get mad. You know how he is."
    show elanor frown at spop, center
    e "I suppose you're right…"
    n "Her shoulders seem to visibly relax at my words, and she slumps into her chair with a heavy sigh."
    show elanor neutral at spop, center
    e "Thank you so much, [ch_angel]! …Do you think you can manage the stack of books? I'll handle all of the files."
    n "Without missing a beat — lest our boss magically appears somewhere behind us — we immediately get to work."

    scene library_reception_day
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    show peffect
    show elanor neutral
    with Fade(1.0, 2.0, 1.0)

    n "Time flies by quickly when I have my chatty co-worker to keep me company."
    n "She fills me in on how the freak storm caught everyone off guard, and how some of the patrons shared the same idea of seeking refuge within the library as well."
    n "Apparently [ch_elanor] was the only one around to keep an eye on things… And from the sounds of it, she seemed to take on the leadership role like a pro."
    n "Still… Discussing her whereabouts had me thinking…"
    y "That reminds me. Where did you go the other day?"
    show elanor neutral at spop, center
    e "…{i}The other day{/i}? What do you mean?"
    y "You remember [ch_ren]? The pink-haired guy?"
    show elanor happy at spop, center
    e "Hm?"
    extend " Ohhh! Loverboy!"
    y "…Yeah, him."
    y "After we had that conversation with [ch_ren], I never saw you afterwards."
    show elanor neutral at spop, center
    e "Oh? Hmm… Let me think."
    n "I watch as she inclines her head to the side to think — and all too quickly — she snaps her fingers and gives me an affirmative nod."
    show elanor flushed at spop, center
    e "Oh, that's right!"
    show elanor blushing at spop, center
    e "I— Erm… Well, this is a bit embarrassing, but…"
    show elanor blushing at spop, center
    extend " I-I ended up going home early."
    show elanor flushed at spop, center
    e "I must've accidentally bumped into something while cleaning the stockroom the other day, and before I knew it, one of the shelves came tumbling down on me!"
    show elanor sad at spop, center
    e "It wasn't until a little while later when [ch_conan] found me and pulled me out."
    y "You knocked over an entire shelf?"
    extend " Miss Creston."
    show elanor blushing
    n "Knowing I was only teasing, [ch_elanor] sends me a sheepish smile and bows her head to hide her reddening cheeks."
    n "But now that I think about it… The shelves in the stockroom had always seemed relatively stable to me. My co-worker wasn't known for her strength, so it didn't make much sense for it to topple over that easily."
    n "But thankfully [ch_elanor] elaborates more; almost as if she could hear the gears in my head working overtime."
    show elanor neutral at spop, center
    e "Well, I suppose it was a tad bit odd. I mean…"
    show elanor sad at spop, center
    e "I've worked in this library for more than five years now, and not once have I heard so much as a creak from those shelves."
    y "It does seem strange, yeah."
    show elanor happy at spop, center
    e "Hmm… Well! I have no doubt [ch_conan] will be installing new storage shelves soon. Oh, speaking of!"
    show elanor smirk at spop, center
    e "Did you notice the new awnings outside the library? I suppose that sudden storm from yesterday had something to do with it. In fact—"

    if status_olivia == False:
        show elanor sad at spop, center
        e "Oh, perhaps you saw it on the news already? Some poor woman was found—"
    else:
        show elanor sad at spop, center
        e "Oh, maybe you heard it on the news already? I heard that all the rain—"

    n "Our conversation gets cut short as I watch [ch_elanor]'s attention drift behind me and towards the flashing red light above one of the shelves."
    n "Duty calls, I guess."
    n "As soon as she stands, I shoot her an appreciative smile — which she returns with an apologetic one of her own — and meanders her way towards the aisle."

################################################################################
## MEETING KIARA
################################################################################
label day3_meetingkiara:
    scene library_reception_day
    show peffect
    with Fade(1.0, 2.0, 1.0)
    $ kpos = tleft
    $ epos = tright

    n "Now left to my own devices, I go back to sorting through the books and putting them into separate piles."
    n "I manage to get a solid ten minutes to myself before the sudden sense of… unease creeps up on me."
    n "It felt as though someone was watching me, so I take a curious sweep across the vicinity to try and locate the source."
    n "But nothing seemed out of the ordinary: people were studying, others were quietly typing away at computers, and I could even spot the back of [ch_elanor]'s head from her spot near the fantasy fiction aisle."
    n "Nothing was out of place, yet… That unnerving feeling of having eyes on the back of my head still lingered."
    n "In fact, now that I thought about it; it was eerily similar to the feeling I got when I was walking home a few days ago."
    n "[ch_violet]'s words about someone breaking into my apartment echo in my mind before it all suddenly dawns upon me…"
    n "The supposed person watching me… Could it somehow be linked?"
    n "No. Definitely not."
    extend " Shaking my head, I try to dismiss those unsettling thoughts before they start to develop into something more sinister."
    n "There was no one watching me. After all, there was hardly anything impressive about me to warrant a stalker in the first place."
    n "I was as plain as they come, and if some [asshole] really did break into my house, they left empty-handed."
    n "That alone clearly proved that I don't own anything worth stealing — except {b}maybe{/b} my limited edition Attack On Giant figurines — But even then!"
    n "I remember thoroughly inspecting my entire apartment once I got home; nothing was out of place nor looked like it had been touched. Everything was as I left it that morning."
    n "Yet it still didn't explain why I was feeling this way."
    n "Fear and apprehension seem to overwhelm my senses {b}so much{/b} that my mind barely registers the sound of something rustling — and I look down to see that I had been worrying the papers in my hands for the past few minutes."
    n "Have I been stressing out that badly? Jeez, I really was letting all this paranoia get the best of me."
    n "Shaking my head once more, I decide it's best not to let those thoughts fester and grow into something far bigger than it should be."
    n "No one broke into my apartment, and no one was watching me right now. I was making a mountain out of a molehill, and nothing was going to scare me—"
    play audio "audio/sfx/item.ogg"
    show kiara happy z at spop, center with dissolve
    $ meet_kiara = True
    k "—Heeeeellloooo?" with vpunch
    y "{size=+10}Ack!{/size}" with hpunch
    play audio "audio/sfx/heels alt.ogg"
    show kiara frown at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    k "Woah!"
    n "Instead of some creepy stalker dressed in all black, I was met with blonde hair and expensive-looking clothing."
    n "…Was this the person I felt watching me?"
    n "It was difficult to make out her words over the loud, rapid sounds of my heartbeat, so I try my best to calm down before responding."
    y "S-Sorry! I wasn't… I didn't notice you come in."
    y "Ahem."
    extend " Welcome to the Corland Bay Library!"
    extend " Can I help you with anything?"
    n "I hope I sounded professional enough — though I'm sure there was still a lingering sense of fear in my words and a facial expression to match."
    n "But it starts to dissipate as I take in the woman's appearance."
    show kiara neutral
    n "Her green eyes seem oddly familiar to me, but what gives it all away is how the woman slightly inclines her head to the side as she looks over me with concern."
    n "Surely not. Was that…"
    y "I don't suppose… Are you [ch_kiara]?"
    extend " [ch_elanor]'s told me all about you."
    show kiara happy at spop, center
    k "In the flesh! I'm actually here to visit my darling sister, would you believe!"
    show kiara neutral at spop, center
    k "Buuuut… Now {i}you've{/i} piqued my interest."
    n "She shoots me a harmless wink and rests her hands atop the reception counter."
    n "Wow… Even the clanging of her jewellery sounds expensive, and I can't help but look at her in awe."
    show kiara neutral at spop, center
    k "Tell me… What else has Norie said about me?"
    
    #hide kiara with dissolve

    menu:
        #with dissolve
        "\"She really, {i}really{/i} admires you.\"":
            $ affection_elanor += 1
            $ affection_kiara += 1
            $ affection_violet += 1
            $ affection_conan += 1
            show kiara blushing at spop, center
            k "Oh? …Really?"
            show kiara happy at spop, center
            k "When did she say that? It would've been nice to hear it coming from her."
            show kiara neutral at spop, center
            k "Ahh well. I'm sure you're well aware of how shy little Norie can be sometimes."
        "\"She loves your taste in fashion.\"":
            $ affection_moth += 1
            $ affection_jae += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            show kiara smirk at spop, center
            k "Ahaha, she better! I didn't pursue a career in fashion for nothing!"
            show kiara happy at spop, center
            k "Did you know I designed her handbag? It's from my latest spring collec—"
        "\"She wants her jacket back.\"":
            $ affection_olivia += 1
            $ affection_kiara += 1
            show kiara sad at spop, center
            k "…Her what?"
            show kiara smirk at spop, center
            k "Surely not that raggedy, old thing she always keeps in the trunk of her car? I'm honestly doing her a favour!"
            show kiara neutral at spop, center
            k "Besides, doesn't her outfit look cuter without it? I think—"
        "[rh_o]\"She finds you annoying.\"[rh_c]":
            $ affection_elanor -= 1
            $ affection_kiara -= 1
            $ affection_teo += 1
            $ ren_decay += 1
            show kiara happy at spop, center
            k "Hmm… Nothing I haven't heard before."
            show kiara smirk at spop, center
            k "I think it's my sisterly duty to annoy her at least once a day. It keeps me young."
            show kiara neutral at spop, center
            k "What about you? Have any siblings of your own to anno—"

    play audio "audio/sfx/sprinting.ogg"
    play audio "audio/sfx/heels alt.ogg"
    show kiara sad at kpos
    show elanor flushed at epos
    with easeinright
    e "[player_fl]-[ch_angel]!" with vpunch
    n "As if summoning [ch_elanor] herself, she emerges from somewhere behind me and joins us at the front desk."
    show elanor neutral at spop, epos
    e "[ch_kiara]! What are you doing here?"
    show kiara happy at spop, kpos
    k "There she is!"
    show kiara smirk at spop, kpos
    k "What? Am I not allowed to see my little sis?"
    show elanor frown at spop, epos
    e "I'm at work right now! You could've texted me in advance."
    show kiara smirk at spop, kpos
    k "But I wanted to surprise you. Aaaand— Look! I come bearing gifts!"
    n "At that, [ch_kiara] places down a few bags branded with high-end prints and designer logos."
    show kiara sad at spop, kpos
    k "Sorry darling! If I knew I'd be meeting you here, I would've brought extra."
    show kiara happy at spop, kpos
    k "But I'm sure there's something for you in one of the bags as well! Pick whatever [ch_elanor] doesn't want."
    if player == "Kiara":
        show kiara smirk at spop, kpos
        k "In fact, here! You can have this quaint little charm I bought for myself! It appears we have the same name, so the 'K' shouldn't be a problem, hm?"
        show kiara neutral at spop, kpos
        k "Besides, I can always buy another one!"
    n "…I genuinely wished I could be rich enough to say something like that."

################################################################################
## PLANNING THE DATE
################################################################################
label day3_planningdate:
    scene black
    show peffect
    play music "audio/bgm/Refreshing Scent.ogg" fadein 1 fadeout 1
    with GlitchDissolve

    $ location_teo = "library"
    $ location_ren = "random"

    n "The sisters seem fully engrossed in each other's presence, so I leave them alone so that they can have their moment to catch up."
    n "After all, I didn't know how long it'd been since [ch_elanor] and [ch_kiara] had seen each other, and the mountain of work in front of me wasn't going to sort itself out in the meantime."
    play audio "audio/sfx/walking.ogg"
    play audio ["<silence .8>", "audio/sfx/item.ogg"]
    n "But before I can silently slip away and sit back down, a tattooed arm boxes me in and commands my attention."
    n "And for the second time today, the expensive smell of wealth and luxury floods my senses."
    extend " Only this time, I knew the person it belonged to."

    scene library_reception_day
    show peffect
    show teo neutral
    with GlitchDissolve

    $ tpos = cleft
    $ epos = center
    $ kpos = cright
    $ cpos = cright
    $ update_teo = "planning something. who wants in?"

    t "[damn!c]. Who're they?"
    n "Seemingly out of nowhere, [ch_teo] appears with that familiar smirk on his face and an unbothered drawl in his tone."
    n "He's absolutely shameless with how his eyes take in both of the sisters' appearances, before he's leaning more of his weight onto his arm and shooting me an expectant look."
    y "…Don't even think about it, [ch_teo]."
    show teo smirk at spop, center
    t "Trust me, you don't wanna know what I'm thinking about right now."
    n "Given how he leans even closer to my side with a sultry grin, I end up believing his words. After all, I wouldn't put it past [ch_teo] to think up {b}multiple{/b} ways to cause a scene in his free time."
    show teo neutral at spop, center
    t "Not jealous, are you?"
    y "Why would you even—"

    play audio "audio/sfx/shoes alt.ogg"
    play audio ["<silence 0.2>", "audio/sfx/heels alt.ogg"]
    show teo smirk at spop, tpos
    show elanor happy at spop, epos
    show kiara sad at spop, kpos
    with easeinright

    n "Whether or not it was my sudden outburst that captures their attention, [ch_elanor] and [ch_kiara] {b}finally{/b} seem to notice us, and I thank my lucky stars for a chance to escape this conversation."
    n "Perhaps I could sneak off to the employee's lounge while everyone was busy talking? I'm sure—"
    show teo smirk at spop, tpos
    t "—You work here too? I've got a few things here that you could check out."
    y "Ugh."
    show elanor blushing
    n "Despite my disgust at [ch_teo]'s blatant flirting, [ch_elanor] seems to be eating it up with a slight blush on her cheeks."
    show kiara happy at spop, kpos
    k "Oh! Actually, I'm just visiting."
    show kiara neutral at spop, kpos
    k "I don't work here, but little Norie over here does! I'm sure she can help you out."
    n "Despite her friendly tone, [ch_kiara] seems to be passively shutting down [ch_teo]'s attempts at flirting and redirecting it towards [ch_elanor] instead."
    n "Yet [ch_teo] doesn't seem to be picking up on it; instead choosing to lean a little more against the counter — so that his muscles flex under his form-fitted shirt — and crosses his ankles."
    show teo neutral at spop, tpos
    t "You're not from around here, are you? I'd remember a face like yours."
    show teo smirk at spop, tpos
    t "The name's [ch_teo]dore, by the way. But cuties like you can call me [ch_teo]."
    show kiara smirk at spop, kpos
    k "Charming. I'm [ch_kiara]."
    show kiara neutral at spop, kpos
    k "And… no, I'm only in town for a few weeks. I'm visiting some relatives and finding some inspiration before I head back home."
    show teo happy at spop, tpos
    t "Inspiration, huh? I could show you around."
    show kiara smirk at spop, kpos
    k "Well, aren't you fun? What about my baby sister?"
    show elanor flushed at spop, epos
    e "H-Huh? But I'm older than you…"
    show kiara happy at spop, kpos
    k "Come on, live a little, Norie! You always tell me how you're holed up at work all the time!"
    show elanor blushing at spop, epos
    e "I-I suppose, but…"

    show teo neutral at spop, tpos
    t "Looks like you're in need of a bit of fun… I can help with that."
    show teo happy at spop, tpos
    t "Have either of you been to the aquarium yet? It opened recently."
    show kiara sad at spop, kpos
    k "Not yet, but… I'll have to give your offer a pass, I'm afraid."
    show teo neutral at spop, tpos
    t "Aquariums not your style?"
    show kiara smirk at spop, kpos
    k "{i}You're{/i} not my style."
    show teo smirk at spop, tpos
    t "Ouch."
    n "Despite the low blow to his ego, [ch_teo] didn't look the least bit offended. In fact, he seems to thrive off of it."
    play audio "audio/sfx/vibrate.ogg"
    n "But as if fate felt the urge to intervene, [ch_kiara]'s phone suddenly goes off and startles everyone."
    show teo sad
    show elanor flushed
    show kiara frown at spop, kpos
    k "Sorry! Give me a sec. I need to take this call."

    $ tpos = tleft
    $ epos = tright

    play audio "audio/sfx/shoes alt.ogg"
    play audio "audio/sfx/heels.ogg"
    show teo sad at tpos
    show elanor flushed at epos
    hide kiara
    with moveoutright

    n "She slips away before any of us can have the chance to respond, and without missing a beat, [ch_teo] immediately takes her previous spot beside [ch_elanor]."
    show teo neutral at spop, tpos
    t "…And what about you?"
    show elanor blushing at bpop, epos
    e "M-Me?"
    show teo smirk at spop, tpos
    t "Don't see anyone else around, Princess."
    show elanor flushed at spop, epos
    e "Oh…! Well, I mean—"
    show elanor flushed at spop, epos
    extend " I think it'd be fun, but…"
    show elanor blushing at spop, epos
    e "I-I suppose it would be a bit awkward if it's just you and me…"
    show teo neutral at spop, tpos
    t "…You heard her, Doll."
    n "As if finally acknowledging my presence, [ch_teo] turns to me with an expecting look on his face."
    show teo happy at spop, tpos
    t "Why don't you tag along? I'll even see if [ch_leon] wants to join the fun. It'll be like a double date."
    show elanor happy
    n "At that, [ch_elanor] visibly seems to relax a little bit. I spare a quick glance in her direction, and I can pick up on the barest hint of hope in her eyes."
    n "Wait. She… {b}wanted{/b} to go on a date with [ch_teo]?"
    show elanor sad
    y "I don't know, El…"
    show teo angry at spop, tpos
    t "Aw, what? Got better things to do?"
    show teo neutral at spop, tpos
    t "Look, I'll pay for everything. I can even pick you up as well if you want. Sound good?"
    n "Not that I'd ever openly admit it to [ch_teo], but his offer was finally starting to sound tempting."
    n "I mean, free food {b}and{/b} a free outing? It was too good to refuse. However…"

    #hide teo
    #hide elanor
    #with dissolve

    menu:
        #with dissolve
        "[rh_o]\"Sure, why not?\"[rh_c]":
            $ affection_teo += 5
            $ affection_jae += 1
            $ affection_olivia += 1
            show teo neutral at tpos
            show elanor happy at epos
            with dissolve
            n "I find myself agreeing with his offer. But before I can regret anything, [ch_teo] cuts me off."
        "\"Fine. But I'm doing this for [ch_elanor].\"":
            $ affection_elanor += 5
            $ affection_conan += 1
            $ affection_kiara += 1
            show teo neutral at tpos
            show elanor happy at epos
            with dissolve
            n "[ch_elanor] seems to brighten at that, and her smile just about makes it all worth it."
        "\"Fine. But only if [ch_leon] will be there.\"":
            $ affection_leon += 5
            show teo angry at tpos
            show elanor happy at epos
            with dissolve
            n "[ch_teo] seems to roll his eyes at that, clearly used to me bringing up my childhood friend all the time."
        "[de_o]\"No thanks.\"[de_c]":
            $ d3_datestatus = False
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_violet += 1
            $ persistent.d3_declinedate = True
            show teo angry at tpos
            show elanor sad at epos
            with dissolve
            n "[ch_teo] scoffs at my answer while [ch_elanor] visibly deflates."
            y "Sorry guys, but I just don't feel up for it."
            show elanor blushing at spop, epos
            e "No, I-I get it!"
            show elanor neutral at spop, epos
            e "Please don't feel pressured to do something you don't want to, [ch_angel]."
            show elanor sad at spop, epos
            e "I can tell you've been on edge lately; I wouldn't want to add any more unnecessary stress."
            show teo frown at spop, tpos
            t "Yeah, cool. Whatever."
            show teo smirk at spop, tpos
            extend " I'm sure [ch_jae] would be happy to join us instead."
            n "Without so much as glancing in my direction, he pulls out his phone and immediately starts to text someone."
            n "[ch_elanor] awkwardly shuffles on her feet at the abrupt end of the conversation, but otherwise, she doesn't seem to pick up on [ch_teo]'s curt behaviour."
            n "Great… It couldn't possibly get more awkward than this—"
            jump day3_conaninterrupts

    show teo smirk at spop, tpos
    if pronoun == "neutral":
        t "There we go. Knew you weren't gonna chicken out on us."
    else:
        t "Atta [baby]. Knew you weren't gonna chicken out on us."

    show teo neutral at spop, tpos
    t "Then it's settled. [ch_leon] and I will meet you both here tomorrow after work."
    show teo smirk at spop, tpos
    t "What time d'ya finish?"
    show elanor happy at spop, epos
    e "E-Erm, around t—"

    label day3_conaninterrupts:
        $ tpos = cleft
        $ epos = center
        $ cpos = cright
        $ update_conan = "Make sure to stay safe everyone."

        play audio "audio/sfx/heels alt.ogg"
        play audio "audio/sfx/walking.ogg"
        play audio "audio/sfx/shoes alt.ogg"
        show teo frown at tpos
        show elanor blushing at epos
        show conan neutral at cpos
        with easeinright

        c "—There you are, [ch_angel]. Ah, I didn't realise you were busy."
        n "Finally, it was as if someone had heard my prayers this time."
        n "[ch_conan] emerges from somewhere behind me — what was up with that today? — and offers me an escape from the current conversation."
        n "And without missing a beat, I turn towards my saviour and spare him a thankful glance."
        show elanor happy
        n "I make sure to silently apologise to [ch_elanor] as well, clearly uneasy with the thought of leaving her alone with [ch_teo]… But she seems all too happy with how she subtly shoos me away with a hand behind her back."

        play audio "audio/sfx/heels.ogg"
        play audio "audio/sfx/walking.ogg"
        hide teo
        hide elanor
        show conan neutral at center
        with moveoutleft

        y "Sure, I can slip away for a moment. Did you need something?"
        show conan sad at spop, center
        c "…Just need an extra pair of hands to sort through some boxes."
        show conan neutral at spop, center
        c "But if you're busy, I'll manage it by myself."
        y "It's fine. I could use a breather!"
        n "Okay, so perhaps I {b}didn't{/b} need to announce that so joyfully…"
        n "With warm cheeks, I turn back towards [ch_elanor] and [ch_teo] to send them one {b}final{/b} apologetic look before following after [ch_conan]."

################################################################################
## MEETING CONAN AGAIN
################################################################################
label day3_conanscene:
    scene library_lounge_day
    show peffect
    play audio "audio/sfx/walking.ogg"
    show conan frown z at spop, center
    play music "audio/bgm/Refreshing Scent.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)

    c "Apologies for this. I didn't mean to steal you from your friends."
    n "{b}This{/b} happened to be sorting through all of the books a co-worker managed to knock over this morning, and making sure they were all in the correct category before putting them back onto the cart."
    n "It felt eerily similar to what I had been previously doing with [ch_elanor] — only this time — there weren't any [ch_teo]-shaped annoyances to keep me company."
    n "But, man… I swear… [ch_conan] had to be the {b}only{/b} boss who'd be perfectly fine with their employees slacking off to talk with their friends instead."
    n "He hadn't said a word about [ch_teo] (and possibly [ch_kiara] too, depending on how long he'd been standing behind me), and seemed more than okay with us huddling around the reception desk."
    n "Deciding not to push my luck, I return [ch_conan]'s soft look with one of my own."
    y "It's fine, don't worry about it."
    show conan neutral z at spop, center
    c "…I've been meaning to ask you something, actually. Has everything been going alright with you?"
    show conan neutral z at spop, center
    extend " Nothing… shady has been happening lately?"
    y "What do you mean?"

    if status_olivia == False:
        show conan sad z at spop, center
        c "You haven't seen the news? Someone's body was found in an alleyway near your neighbourhood."
        show conan frown z at spop, center
        c "She was supposedly bludgeoned and beaten past the point of recognition. It's horrifying to think someone is capable of such crimes."
    else:
        show conan sad z at spop, center
        c "You haven't heard the news? There's been a few murders happening in the bay area recently."

    show conan neutral z at spop, center
    c "Admittedly, I have been worried for your safety as of late. You live by yourself, correct?"

    if d1_inviteren == False:
        y "Yeah, but my neighbour checks in with me almost regularly. Now that I think about it, she's also been concerned for my safety."
    else:
        y "Yeah, but I've recently had a… friend stay with me. Now that I think about it, he's also been concerned for my safety."

    show conan smirk z at spop, center
    c "That's good. I'm glad. Listen, if something ever happens…"
    n "[ch_conan] awkwardly glances over his shoulder before returning his gaze back to me. Nothing but sincerity stares back, and I find myself in a stunned silence."
    show conan neutral z at spop, center
    play audio "audio/sfx/paper.ogg"
    c "Here. It's my personal number."
    n "But due to the lack of clarification, I ended up sending him a confused look instead of thanking him."
    show conan frown z at spop, center
    c "I know you've only recently moved back to Corland Bay, but you've yet to put someone down as your emergency contact."
    show conan neutral z at spop, center
    c "I'm worried you won't have anyone to call in case something does happen. I want to make sure you're safe at all times."
    y "Oh. Thank you, [ch_conan]."
    show conan smirk z at spop, center
    c "…Of course."
    n "He gives my shoulder a gentle pat before resuming his original task."
    n "The conversation falls back into an easy, comfortable silence, and I pocket his number before pouring all of my focus towards the books laid out in front of me."

################################################################################
## MEETING LEON AGAIN
################################################################################
label day3_leonscene:
    scene black
    show peffect
    play music "audio/bgm/After The Rain.ogg" fadein 1 fadeout 1
    stop ambience fadeout 2.0
    with Fade(1.0, 2.0, 1.0)

    $ location_kiara = "home"
    $ location_elanor = "library"
    $ location_olivia = "home"
    $ location_conan = "home"
    $ location_leon = "library"
    $ location_violet = "random"
    $ location_jae = "home"
    $ location_ren = "bluemoss"
    $ location_teo = "library"

    n "The rest of my shift passes by uneventfully, and at some point, [ch_elanor] informs me that [ch_kiara] had to leave for a work-related matter and wouldn't be coming back for a few days."
    n "She'd even asked [ch_elanor] to give me her number as well — alongside mentioning something about \"sharing more embarrassing stories about little Norie the next time we talk\"… Whatever that meant."
    n "Still, it was really nice to finally meet [ch_elanor]'s sister, and it was even kinder of her to gift me a fountain pen before she left."
    n "Or… At least, I assumed it was [ch_kiara]."
    n "I found the expensive-looking box sitting on my desk once I returned, and I wasted no time in opening it up and examining the contents."
    n "The pen itself appeared to be made from {b}extremely{/b} high quality materials, and the cursive \"[player_fl]&R\" logo looked rather fancy underneath the light."

    if status_olivia == False:
        n "The ink was a rich, deep red too — which I couldn't wait to use on my papers."
    else:
        pass

    n "I made a mental note to get something for [ch_kiara] as well, before pocketing the pen next to [ch_conan]'s number and packing up my belongings for the day."

    if d3_datestatus == False:
        n "But as I'm slipping out the library's back door, I notice [ch_teo], [ch_elanor], [ch_leon], and [ch_jae] all standing around the alleyway's entrance in an avid conversation."
        n "Planning their outing tomorrow, no doubt."
        n "And despite the cold treatment [ch_teo] gave me earlier for rejecting his offer, it was… nice to see [ch_elanor] out and making new friends."
        n "Deciding not to ruin their fun, I quietly sneak out the back door and take the opposite route home."
        n "But… Something at the back of my mind must've seriously been bothering me, because I didn't even feel like visiting the manga store on my way back."
        n "Jeez. Whatever this is, I hope it'll pass soon."
        jump day3_homealone
    else:
        pass

    if unlockable == "starshine" or unlockable == "sunpup":
        n "But as I'm slipping out the library's back door, I notice a familiar patch of two-tone hair, a cunty outfit, and the sloppy appearance of someone who'd just woken up from a nap."
        jump eastereggalternative
    else:
        n "But as I'm slipping out the library's back door, I notice a familiar broad backside, a patch of blonde hair, and a bright red patterned shirt standing near the alleyway's entrance."

    scene beach_street_night
    play ambience "audio/ambience/street.ogg"
    play audio "audio/sfx/movement.ogg"
    $ lpos = cleft
    $ epos = center
    $ tpos = cright
    show peffectp
    show leon neutral at lpos
    show elanor neutral at epos
    show teo neutral at tpos
    with GlitchDissolve

    n "As if sensing my presence, [ch_leon] turns around and greets me with one of his familiar warm smiles."
    show leon happy at spop, lpos
    l "G'day, darl'! Been a while."
    n "He sends me a toothy grin before making space for me within the group. [ch_elanor] greets me with a delicate wave, and [ch_teo] looks moderately annoyed, as usual."
    show leon smirk at spop, lpos
    l "[ch_teo] was just introducing me to [ch_elanor] and yarning on about this little outing he has planned."
    show leon happy at spop, lpos
    l "Hey! How come you never told me you've never been to the aquarium before? Makes sense, though."
    show leon neutral at spop, lpos
    l "I reckon it was built a bit after you left the Bay, right? So I doubt you had time to check it out."
    y "Pretty much. Most of my free time has been taken up with moving and unpacking boxes."
    n "I couldn't help but find myself agreeing with his words."
    n "It was crazy how [ch_leon] seemed to know me so well; even though we hadn't had the chance to speak to each other like this in a while."
    y "But I'm curious to see what it's like!"
    extend " What about you, Norie?"
    n "I couldn't help but let [ch_kiara]'s nickname for her slip."
    show elanor happy at spop, epos
    e "…Hm? O-Oh! Yes, I'm the same!"
    show elanor blushing at spop, epos
    e "Hehe, I'm looking forward to tomorrow! I've never been to an aquarium before, so this should be fun."
    show leon frown at spop, lpos
    l "Well, here's hoping the weather will be more lenient tomorrow. It was [pissing] down buckets yesterday, wasn't it?"
    show leon sad at spop, lpos
    l "Did ya make it home alright, Sunfish?"
    n "All of a sudden, that eerie feeling comes back, and I resist the urge to turn around and look behind me."
    n "I only {b}now{/b} notice that I've had my back to the dark alleyway this entire time."
    show elanor sad at spop, epos
    e "—[ch_angel]?"
    y "…Sorry, what was that?"
    show leon frown at spop, lpos
    l "You alright? You look like you've seen a ghost."
    n "I watch as [ch_leon] looks behind me before glancing at [ch_teo] and [ch_elanor] for what seems like reassurance."
    y "Ah— No, it's nothing. I just… I guess I've had a long day at work."
    show leon neutral at spop, lpos
    l "Nah, I get it. Feeling tired? You should head on home then."
    show elanor neutral at spop, epos
    e "Please! Don't let us keep you longer than we should."
    show teo smirk at spop, tpos
    t "…Want me to drop you off? Car's out front."
    n "As much as I appreciated everyone's concern, I honestly wanted to be left alone right now to clear my head — and going on a walk would surely do me wonders."
    n "Besides, it was still (somewhat) bright out and there were people around, so I had no reason to worry about my non-existent stalker."
    n "I also heard that some new merchandise arrived at the local manga store which I had been meaning to check out, so that would surely help to get my mind off things."
    n "It was along my route home anyway… What harm could possibly come out of a quick detour?"
    hide leon
    hide elanor
    hide teo
    with dissolve
    n "At that thought, I quickly placate everyone's concern before bidding my goodbyes and heading off alone down the street."
    n "…It wasn't until I got far enough away from the library that the eerie feeling started to dissipate."

################################################################################
## GOING TO THE MANGA STORE
################################################################################
label day3_mangastore:
    scene store_manga_day
    stop ambience fadeout 2.0
    show peffect
    play music "audio/bgm/Refreshing Scent.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)

    n "The nostalgic smell of comic books and plastic greets me as I enter the all-too-familiar manga store, and I immediately beeline my way towards the anime aisle."
    n "I was set on collecting the last remaining accessories for my mini Attack On Giant's display, and I wasn't about to let my paranoia get in the way of that."
    n "But as I was passing through a few of the aisles, I noticed a familiar shade of pink near the cashier."
    y "Is that… [ch_ren]?"

    scene CG D3_MANGA
    hide screen dayscalendar
    show screen menuwu
    $ quick_menu = False
    $ meet_ren = True
    $ persistent.cg_d3_manga = True
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 1.0, 1.0)

    if d2_visitren == True:
        n "I didn't even notice his motorbike out front… If he even brought it. Up until now, I always assumed he walked everywhere."
        n "And even though he was wearing a mask and had his hair tied back, I could easily make out his large and lanky frame anywhere."
    else:
        n "Even though he was wearing a mask and had his hair tied back, I could easily pick out his large and lanky frame anywhere."

    n "Sneaking closer, I notice how he appears to be in a hushed conversation with the manager about something confidential (if their closeness was anything to go by), before he places a thick manilla envelope into her hands and leans back."
    n "Oh? I wonder what's inside."
    n "Was [ch_ren] trading in some old manga? Ooh, what if it's Attack on Giants?!"
    n "Though, if it {b}is{/b} AoG, then I'm not really sure why he'd want to trade them in. With how popular the franchise is currently, there isn't much of a high demand. If anything, there's {b}too much{/b} consumable media being produced right now."
    n "Everywhere I go, all I see is Haruko… And I wouldn't have it any other way."
    n "And speaking of my beloved Haruko; now that I got a better look at [ch_ren]…"
    n "Isn't that the limited edition Spring Haruko hoodie?!" with vpunch
    extend " I thought they weren't selling them anymore!"
    n "But just as I'm about to make myself known to ask questions, [ch_ren] is {b}already{/b} turning on his heel and slipping behind the large racks filled with cosplays and gaming-themed apparel."

    scene store_manga_day
    $ quick_menu = True
    hide screen menuwu
    show screen dayscalendar
    show peffect
    play music "audio/bgm/Refreshing Scent.ogg" fadein 1 fadeout 1
    with GlitchDissolve

    n "His height does him no favours though, as I watch his head peek out from the top while he bobs and weaves his way towards the side entrance."
    play audio "audio/sfx/vibrate.ogg"
    n "At that very moment, my phone decides to jump-scare me by suddenly going off, and it startles me enough to temporarily forget about [ch_ren]."
    n "Letting out a string of curses, I reach into my back pocket and pull it out — only to see [ch_moth]'s name flash on the screen. With a grin, I accept the video call and hold the phone up to my face."

    $ update_moth = "HARUKO??? HELLOOO?????? PLEASE PLEASE PLEASE PLE"
    $ persistent.d3_meetmoth = True

    play audio "audio/sfx/item.ogg"
    show mothphone error at vcpos with easeinright
    y "Heeey! Listen, now isn't really a good time to talk, but—"
    show mothphone smirk at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5), vcpos
    mcall "Oh nooo, that's terrible. Get well soon. Or… sorry for your loss. Ooooor— whatever. Anyway! Listen!"
    show mothphone happy at bpop
    mcall "…GUESS WHO WON AN ALL-PAID HOLIDAY TRIP OVERSEAS!" with vpunch
    show mothphone smirk at spop
    mcall "Me, that's who!"
    n "It'd been a while since I'd last seen [ch_moth]'s face, but they appeared just as boisterous as I remembered them."
    show mothphone happy at spop
    mcall "AND FOR FREE, TOO! I mean, okay yeah, I still need to pay for food and stuff, but—"
    show mothphone frown at spop
    mcall "…Hey, where are you?"
    y "Um… I'm in a manga store? Hold on— Can we backtrack for a second? You got free tickets? To where—"
    show mothphone flushed at bpop
    mcall "—Is that a Haruko figurine?!" with vpunch
    show mothphone flushed at spop
    extend " Can you get it for me? Please? Please, please, please, please, pl—"
    y "[ch_moth]."
    show mothphone blushing at spop
    mcall "I'll pay you back! Promise! I'll pay for shipping, too! It's soooo cute!"
    show mothphone blushing at spop
    mcall "Look at his widdle outfit! Lookit! His tiny little jacket and tiny little shoes!"
    n "With an eye-roll, I reach behind me for the figurine — but not before picking up the accessories I originally came in here for — and slowly make my way towards the cash register."
    n "Once [ch_moth]'s hoots and hollers calm down, I gently try to coax them back onto the original topic."
    show mothphone neutral at spop
    mcall "Oh, right! You asked where I'm going? Weeeeell… It's actually a surprise."
    y "…Seriously?"
    show mothphone flushed at spop
    mcall "{glitch=5.0}A good surprise though! Hey, {/glitch}{glitch=7.0}you're still in Corla—{/glitch}"
    n "For a brief moment, their screen starts to lag and a loading symbol pops up."
    y "[ch_moth]?"
    show mothphone error at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5), vcpos
    mcall "{glitch=5.0}Bec— I'll be— In {/glitch}{glitch=7.0}almo— Tha{/glitch}{glitch=3.0}t okay with y—{/glitch}"
    play audio "audio/sfx/item.ogg"
    hide mothphone with dissolve
    n "Their voice cuts in and out, giving an almost robotic effect before the screen eventually fades to black."
    n "With a heavy sigh, I end the call and shoot [ch_moth] a text to let them know that they got disconnected yet again."
    n "But as I absent-mindedly look out the window, I notice the blurry outline of [ch_ren]'s figure sitting on a bench outside; busying himself with what looked like a phone in his hands."
    npc "{size=+10}Next!{/size}" with vpunch
    n "The cashier's voice pulls me away from my thoughts, and I quickly pay for my purchases — all while sparing not-so-secretive glances at [ch_ren] from beyond the shop window to make sure that he's still there."
    n "It was strange, but I couldn't help but hope I'd get a chance to catch up with him on my way out."

    if d1_inviteren == False:
        n "I know it'd barely been more than a day since I last saw him, but I still wanted to thank him for the date he took me on yesterday."
    elif d2_visitren == True:
        n "I know it'd barely been more than a few hours since I last saw [ch_ren], but I still wanted to thank him for letting me stay at his place for the night."
        n "…And for washing my clothes, cooking me breakfast, and driving me to work."
    else:
        n "I know it'd barely been more than a day since I last saw him, but I still wanted to thank him for staying at my place the other day and keeping watch."
        n "It was strange to feel safe in the presence of someone I barely knew, but a part of me wanted to keep [ch_ren] around on the off-chance that my non-existent stalker showed their ugly head."

    n "The cashier pulls my attention away by handing me a bag and receipt, and I give them my thanks before making a beeline towards the exit."

    scene town_street_night
    show ceffect
    play music "audio/bgm/After The Rain.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/movement.ogg"
    with GlitchDissolve

    n "But just as the door swings open, I notice that [ch_ren] had… already left."
    n "He was no longer on the bench where I last saw him, and I couldn't spot him on either end of the street either."
    n "It was like he was never there in the first place, and I almost find myself wondering if I had imagined the whole thing."

    if relationship_ren == "crush":
        n "It was a shame, though; I really wanted to see him and his charming smile again."
    else:
        n "I was starting to see him everywhere, anyway, and it was beginning to come across as creepy."

    n "But Corland Bay isn't that big of a coastal town in retrospect, so I'm sure we were bound to run into each other again sooner or later."
    n "I mean, I {b}literally{/b} met [ch_ren] at my own workplace because we shared a few common interests in books. His just so happened to be about native flora."
    n "That kind of stuff wasn't something either of us could control, and I was most likely looking too deep into it. Still…"
    extend " It felt strange all the same."
    n "Oh well, there was no use dwelling over it."
    if d1_inviteren == True:
        n "I was bound to run into [ch_ren] again at some point — regardless if I had a way to contact him or not."
    else:
        n "I still had [ch_ren]'s number saved in my contacts anyway, so I could always shoot him a text — or even a call — if I {b}really{/b} started to miss him."

################################################################################
## MEETING OLIVIA AGAIN (OR THE LANDLORD IF SHE DIDN'T PASS THE VIBE CHECK LOL)
################################################################################
label day3_meetinglandlord:
    scene oh_complex_night
    show peffectp
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)

    $ location_moth = "home"
    $ location_violet = "home"
    $ location_ren = "home"
    $ location_elanor = "home"
    $ location_conan = "home"
    $ location_jae = "home"
    $ location_teo = "home"
    $ location_kiara = "home"
    $ location_olivia = "home"
    $ location_leon = "home"

    if status_olivia == True:
        n "It was beginning to get dark once I arrived back at my apartment complex, so I quickly usher my way up the staircase and onto my floor."
        n "But as I'm making the long trek up the stairs, I bump into someone lingering around the corner and almost end up tumbling down."
        play audio "audio/sfx/item.ogg"
        show olivia sad z with dissolve
        y "{size=+10}Woah!{/size}" with hpunch
        show olivia frown z at bpop, center
        o "Hey! Watch it!" with vpunch
        n "Glancing up, I notice that it's the cashier from yesterday who was glaring daggers at me while I try to steady myself with the railing."
        n "That was… [ch_olivia], wasn't it?"
        play audio "audio/sfx/heels alt.ogg"
        show olivia frown with dissolve
        n "She makes no effort to help me — though she does move to the side in order to give me space at the top of the stairs."
        n "It's then when I take notice of the {b}giant{/b} basket of laundry in her arms, and it makes me wonder if she was actually going to carry it all the way to the laundromat by herself."
        n "Clearly, she was stronger than she looked."
        show olivia flushed at spop, center
        o "S-Sorry! I didn't mean to—"
        n "[ch_olivia] cuts herself off once the severity of the situation finally sinks in, before she sucks in her cheek and lets out an exasperated chuckle."
        n "Seriously? What could she possibly find so funny about this situation?"
        show olivia sad at spop, center
        o "Of all places… A staircase? Really?"
        show olivia neutral at spop, center
        o "Your boyfriend sure has a messed up sense of humour."
        y "…What?"
        show olivia sad at spop, center
        o "No, it's nothing. Look, I didn't mean to knock you down the staircase like that. I'm just…"
        show olivia frown at spop, center
        o "I've got a lot on my mind lately, and I wasn't looking where I was going."
        y "Hey, it happens."
        n "It most certainly didn't."
        n "But [ch_olivia] seemed to be having a rough day, so I wasn't going to make things worse by being rude to her."
        n "She already looked on edge for some reason — especially with how she kept sneaking glances over both of our shoulders."
        n "It was almost like she was looking for something, and I would've asked her about it if she didn't beat me to it."
        show olivia neutral at spop, center
        o "So where's that boyfriend of yours anyway?"
        show olivia sad at spop, center
        o "Not lurking around the corner like a creepy psychopath, is he?"
        y "…Who?"
        show olivia frown at spop, center
        o "Seriously?! Your boyfriend! The guy you visited the souvenir shop with the other day!"
        y "Ohhh! [ch_ren]? He's not my boyfriend. We're just…"
        
        #hide olivia with dissolve
    
        menu:
            with dissolve
            "[rh_o]\"Actually, he {i}is{/i} my boyfriend.\"[rh_c]":
                $ affection_ren += 1
                $ affection_olivia -= 5
                $ rem_boyfriend = True
                show olivia frown with dissolve
                o "Great, no need to rub it in my face."
                show olivia sad at spop, center
                o "And why are you so indecisive? Either he's your boyfriend, or he's not."
                show olivia frown at spop, center
                o "You know what? I'm not even sure why I'm having this conversation with you. Forget it. I'm in a rush, so please move."
            "\"He's just a guy I'm interested in.\"":
                $ affection_ren += 1
                $ affection_jae += 1
                $ affection_kiara += 1
                $ affection_olivia += 1
                show olivia sad with dissolve
                o "You're interested in someone like him? I feel sorry for you."
                y "Excuse me?"
                show olivia neutral at spop, center
                o "Nothing. Just the ramblings of a stressed-out university student. Anyway, I'm in a rush, so please move."
            "\"He's just a friend.\"":
                $ affection_ren -= 1
                $ affection_violet += 1
                $ affection_elanor += 1
                $ affection_conan += 1
                $ affection_leon += 1
                $ affection_olivia += 1
                show olivia frown with dissolve
                o "For real? Friends don't look at each other that way."
                y "What?"
                show olivia sad at spop, center
                o "Are you seriously that dense? Whatever."
                show olivia frown at spop, center
                o "I'm not even sure why I'm having this conversation with you. Forget it. I'm in a rush, so please move."
            "\"I've never seen that man in my life.\"":
                $ affection_ren -= 1
                $ affection_olivia -= 1
                $ affection_teo += 1
                $ affection_moth += 1
                show olivia frown with dissolve
                o "…"
                show olivia frown at spop, center
                o "Are you—!"
                show olivia sad at spop, center
                o "Ugh. I don't have time for this. Forget it. I'm in a rush, so please move."
            "{image=14NWY symbol} \"He's just a friend… With a few benefits.\"" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
                call DLC_day3_olivia from _call_DLC_day3_olivia
        play audio "audio/sfx/heels.ogg"
        show olivia sad at right with easeinright
        n "Clearly done with the conversation, [ch_olivia] sidesteps me and starts to make her way down the stairwell. But she only manages to get a few feet away before she turns around once more."
        n "Resting her laundry basket on a hip, she looks up at me with an unreadable look."
        show olivia neutral at spop, right
        o "You live on this floor as well? Then it looks like we're going to be seeing each other more often."
        show olivia frown at spop, right
        o "But just some neighbourly advice: If you plan on bringing \"[ch_ren]\" around, keep it down. I'm not afraid to file a noise complaint."
        play audio "audio/sfx/heels alt.ogg"
        hide olivia with dissolve
        n "And with that, she disappears around the corner."
        n "…What was that all about?"
        n "Deciding it wasn't worth my time to mull it all over, I slowly make my way towards my apartment."
    else:
        n "It was beginning to get dark once I arrived back at my apartment complex, so I quickly usher my way up the staircase and onto my floor."
        n "But as I'm making the long trek up the stairs, I bump into someone lingering around the corner and almost lose my footing."
        show beau angry at tleft
        show haruka sad at tright
        with dissolve
        play audio "audio/sfx/item.ogg"
        show beau angry at bpop
        b "Oof." with vpunch
        show haruka angry at bpop
        play audio "audio/sfx/heels alt.ogg"
        npc "Woah!"
        n "There, right before my eyes, is my landlord, Beau. But the other person by his side is a complete stranger to me."
        show beau neutral at spop
        b "Ahem… Good evening, [ch_angel]. Finished with the day—?"
        y "—{i}You!{/i} There you are! Have you been getting my complaints?" with vpunch
        show beau frown at spop
        b "…Complaints?"
        show haruka sad at spop
        npc "Huh? What [are] [they] talking about?"
        show beau neutral at spop
        b "Ah, I don't believe either of you have met yet. Shall I introduce the two of you?"
        n "Was he seriously trying to divert the conversation right now?!"
        show beau happy at bpop
        b "[ch_angel], I want you to meet my daughter. This is my pride and joy, Haruko."
        show haruka frown at spop
        h "It's Haruka."
        show beau sad at spop
        b "Ah— Yes."
        y "You mean… Like the main protagonist from Attack on Giants?"
        show haruka sad at spop
        h "…Unfortunately."
        y "Your father {i}seriously{/i} named you after an anime character?"
        show haruka happy at spop
        h "Yeah, so maybe he's a {i}taaaad{/i} bit obsessed with the anime."
        show haruka neutral at spop
        h "S'why he wears those stupid clips and painted his nails pink. The blue rhinestones were my addition, though."
        show haruka smirk at spop
        h "Buuut! If you think being called 'Haruka' is embarrassing enough, my younger sister was named after his favourite character of {i}all time{/i}… Rin—"
        y "—Haruko's arch nemesis?! You can't be serious!" with vpunch
        y "Wait… No. We're getting off-topic again."
        y "Beau! Did you or {i}did you not{/i} get my complaints?"
        show beau frown at spop
        b "Hm? Come again?"
        n "He looks up from his phone and spares a meagre glance in my direction."
        show beau sad at spop
        b "Sorry [ch_angel], I've been so distracted lately."
        show beau happy at bpop
        b "You see, I've always had an interest in renovating old buildings. In fact, I recently bought yet another apartment complex in New Salvus for this very purpose."
        show beau neutral at spop
        b "I suppose that makes it… {i}twenty-eight{/i} buildings now, right, my adorable little munchkin? It's always so hard keeping track of everything."
        show haruka frown at spop
        h "Ugh. I'm a grown adult. Don't call me that."
        show beau happy at spop
        show haruka angry
        b "Oh? But you've always been my sweet baby princess—"
        n "…It's like I'm not even here."
        n "But as soon as Beau reaches out to pinch one of Haruka's cheeks in an affectionate manner, I take a moment to fully absorb their conversation."
        n "So my landlord bought {b}yet another{/b} building, huh? Well… That probably explains why he hardly ever bothers to take care of {b}this{/b} apartment."
        n "Well, whatever. I didn't have time for this — or their mushy, tender moment."
        n "Without another word, I quietly excuse myself from the conversation and make my way home."

################################################################################
## INVITING SOMEONE OVER
################################################################################
label day3_invitingfriend:
    scene angel_lounge_night
    show peffectp
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/movement.ogg"
    play audio "audio/sfx/door.ogg"
    with GlitchDissolve

    n "Not bothering to turn on the light, I toss my keys into the tray, shrug off my jacket, and unceremoniously drop myself onto the couch."
    n "Today had been a whirlwind of events and emotions, and the worst part was that it still hadn't ended yet."
    n "I still had an hour or so left before I consider any dinner plans, so I figured I might as well spend the evening winding down in the meantime."
    play audio "audio/sfx/slide.ogg"
    n "All too quickly, an idea pops into my head, and I reach over to grab my phone."

    $ choice_style = "box"
    menu:
        "[rh_o]Invite someone over[rh_c]":
            $ choice_style = "default"
            $ invitestatus = True
            $ affection_ren -= 10
            $ persistent.d3_inviteover = True
            n " Figuring it'd be best to catch up with someone instead of stewing in my apartment alone, I pull up my contacts list and idly scroll through it."
            n "[ch_conan]'s number immediately captures my attention — being the newest addition to my contacts and sitting near the top of the list — before my curiosity begins to stray once more."
            n "Without so much as hesitating, I tap on that person's number and bring the phone closer to my ear."
        "Don't invite someone over":
            $ choice_style = "default"
            $ affection_ren += 10
            n "…Maybe it wasn't such a good idea after all. I mean, I've already spent the entire day talking to my friends, so perhaps it would be best to simply spend time with myself instead."
            n "After all, I definitely deserved it. So much has been going on lately, and I could use a distraction to take my mind off of things."
            n "And so, I decided to make myself an early dinner before settling into the comfort of my bed and catching up on some webcomics."
            jump day3_dayend

    label day3_invite1:
    menu:
        "{glitch=10.0}[ch_ren]{/glitch}":
            $ affection_ren += 10
            play audio "audio/sfx/glitch.ogg"
            n "Odd… I don't remember scrolling all the way down to view his contact details."
            n "Nevertheless, I find myself tapping on [ch_ren]'s name and bringing the phone closer to my ear."
            n "He picks up almost immediately, and I can practically {b}feel{/b} the excitement and moe flowers expel from the screen and hit me in the face."
            n "And before I know it, [ch_ren] is agreeing to come over as soon as he can — so I quickly turn the lights back on, clean the place up a bit, and anticipate his arrival."
            jump day3_inviteren
        "[ch_moth]":
            $ affection_moth += 10
            n "Quickly glancing at the time to make sure it wasn't too early for them, I tap on [ch_moth]'s name and bring the phone closer to my ear."
            n "The phone rings a few times before they pick up with a happy lilt in their tone."
            jump day3_invitemoth
        "[ch_violet]":
            $ affection_violet += 10
            n "The phone rings exactly four times before [ch_violet] picks up, and we barely get a few minutes into the call before she's suggesting that I come over instead."
            n "Admittedly, it {b}was{/b} a nice idea — and before I know it, I'm picking up my keys and heading out."
            n "I can already smell the soft aroma of lavender and thyme the moment I step out of my apartment and make my way across the hall."
            jump day3_inviteviolet
        "[ch_elanor]":
            $ affection_elanor += 10
            n "It takes a while before [ch_elanor] answers, but she seems more than happy to come over to my place and spend some more time together."
            n "And so, I quickly turn the lights back on, clean the place up a bit, and anticipate her arrival."
            jump day3_inviteelanor
        "[ch_conan]":
            $ affection_conan += 10
            n "…[ch_conan]?"
            jump day3_inviteconan
        "Someone else…":
            jump day3_invite2

    label day3_invite2:
    menu:
        #with dissolve
        "[ch_jae]":
            $ affection_jae += 10
            n "The phone rings exactly two times before [ch_jae] answers, and we barely get a few minutes into the call before he's suggesting that I come over instead to catch up."
            n "Admittedly, it was a nice idea — and before I know it, I'm picking up my keys and heading out."
            jump day3_invitejae
        "[ch_leon]":
            $ affection_leon += 10
            n "Quickly glancing at the time to make sure it wasn't too late for him, I tap on [ch_leon]'s name and bring the phone closer to my ear."
            jump day3_inviteleon
        "[ch_teo]":
            $ affection_teo += 10
            n "Without thinking, I tap on [ch_teo]'s number and bring the phone closer to my ear."
            jump day3_inviteteo
        "[ch_olivia]" if status_olivia == True:
            $ affection_olivia += 10
            n "Deciding to indulge in one of [ch_ren]'s harmless pranks, I find [ch_olivia]'s number and give it a call."
            n "Admittedly, I didn't have much of a plan in mind, but I figured I could just come up with something silly on the spot and roll with it. Perhaps I should ask her if her fridge is still running… Heh."
            n "Pressing the phone closer to my ear, I listen to it ring a few times before a familiar voice answers."
            jump day3_inviteolivia
        "[ch_kiara]":
            $ affection_kiara += 10
            n "I still needed to thank her for giving me her number, so I tap on [ch_kiara]'s name and bring the phone closer to my ear."
            n "It rings a few times, and just when I think nobody is going to answer, she picks up with an apologetic tone. "
            jump day3_invitekiara
        "{glitch=10.0}{b}Go back…{/b}{/glitch}":
            jump day3_invite1

################################################################################
## INVITING REN OVER
################################################################################
label day3_inviteren:
    scene angel_lounge_day
    show peffect
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)
    $ d3_inviteren = True
    $ location_ren = "oh"

    n "Barely ten minutes pass before I hear a loud knocking at my front door. Almost immediately, I leap to my feet and unlock it with a smile."
    show ren happy with dissolve
    y "[ch_ren]! Hey, come on in."

    if d2_visitren == True:
        show ren smirk at spop, center
        r "…I see you're still wearing my hoodie."
    elif d1_inviteren == True:
        show ren smirk at spop, center
        r "Heh, I see not much has changed since the last time I was here."
    elif d1_inviteren == False:
        n "I watch as he awkwardly shuffles about in the hallway, almost uncertain if he should come inside or not. He moves to take off his shoes, and I watch in awe as he neatly stacks them next to the umbrella rack."
        show ren flushed at bpop, center
        r "Oh— Are you the type to leave your shoes on at home? S-Sorry! I'll—"
        y "No, no, you're fine!"
        n "Ugh, he really was adorable."
    else:
        show ren smirk at spop, center
        r "It's good to see you again, Angel."

    show ren blushing at spop, center
    r "I… Um, I also brought some takeout with me, if that's okay?"
    show ren neutral at spop, center
    r "I figured you hadn't had a chance to eat yet."
    y "Woah, how'd you know? It's like you can read minds or something."
    show ren smirk at spop, center
    r "…"
    n "Barely registering the look on his face, I gently coax [ch_ren] into my living room."
    n "He makes himself at home on my couch, and I bring a few utensils from my kitchen for the food he so kindly brought."
    y "Oh! By the way, Were you at the manga store earlier today?"
    y "I thought I saw you there."
    show ren flushed at spop, center
    r "Yeah, I-I know you did… I mean—!"
    show ren blushing at spop, center
    r "Because I saw you as well!"
    show ren flushed at spop, center
    extend " After I left!"
    show ren blushing at spop, center
    extend " I noticed you through the window!"
    n "Well, that seemed to confirm my thoughts about [ch_ren] sitting outside the store."
    n "Stabbing my fork into the food, I take a bite and let out a pleased hum from all the delicious flavours dancing on my tongue."
    y "Really? You should've said hi."
    show ren frown at spop, center
    r "I thought about it, but… Y-You seemed really focused on something."
    show ren sad at spop, center
    r "And then you got a call, so…"
    y "Ahhh, yeah. That was my friend [ch_moth]. Oh! That reminds me! [ch_ren]."
    n "At that, his full attention is immediately on me — takeout long forgotten as the taller male moves in his seat to face me."

    if d1_inviteren == False:
        y "You like Attack on Giants too, don't you? I mean, your hair and outfit… It was inspired by Haruko, right?" 
        n "I know I must've been coming on a bit strong, but [ch_ren] and I {b}have{/b} been getting to know each other a bit better over these past few days, and somehow, I knew he wouldn't freak out as much if he knew about my more… nerdy side."
        n "Sparing a glance at [ch_ren], he seems to be handling it well enough — if the interested yet curious look on his face was anything to go by."
        n "In fact, [ch_ren] seems almost on the edge of his seat with how intently he's staring at me. He must really be interested in Haruko as well to garner this sort of reaction."
        n "In some way, it was comforting to know we shared a few more similar interests."
        y "Haruko is… actually my one of my favourite characters at the moment. He has been for a while now, actually."
        y "Oh— But that's not the point! The point is, [ch_moth] loves Haruko too! I could introduce you guys! They're a diehard fan of the anime, and I'm sure they—"
    else:
        y "I remember you saying that you like Attack on Giants too, right? I could introduce you guys!"
        y "They're a diehard fan for the anime, and I'm sure they wouldn't mind—"

    show ren blushing at spop, center
    r "Oh! Uhh… {i}[ch_moth]{/i} is the one who's interested?"
    n "Almost shyly, he turns his head away and meekly scratches at his jaw."
    show ren flushed at spop, center
    r "I-I don't mind, but…"
    n "I wasn't expecting [ch_ren] to be so… hesitant, and I suddenly felt bad for springing this all onto him without considering how he might feel as well."
    y "Hey, no need to force yourself. If you don't want to, that's okay."
    y "I just thought it'd be nice to let them have someone else to talk to, y'know?"
    y "[ch_moth]… [ch_moth] has trouble making friends — and most of the time, they're only talking to me."
    show ren sad at spop, center
    r "Yeah? That's too bad…"
    n "He sends me a sad look coupled with a frown before returning to the plate of food before him."
    n "Although I was thinking about [ch_moth], I really didn't want to force [ch_ren] into befriending someone if he didn't want to."
    n "Besides, maybe he has trouble forming friendships, too?"
    n "It {b}was{/b} a little difficult trying to keep up with his sudden personality shifts, but at this point in our…friendship, I was starting to get used to it."
    n "Deciding to lift the mood a little, I try to change the subject to something more light-hearted."

    if d1_inviteren == True:
        y "Soooo… the rats, huh?"
    else:
        y "Soooo… Apparently, this place has rats."

    n "Really [ch_angel]?! That was the first thing you could think of? How was that any less awkward than what we were currently—"
    show ren sad at spop, center
    r "Actually… I didn't want to say anything, but…"
    show ren blushing at spop, center
    r "I think I saw one on my way up here…"
    show ren frown at spop, center
    r "I-It probably made itself a home in that busted elevator shaft."
    y "Seriously?!" with vpunch
    extend " Wait, do you think you could come with me and explain it to my landlord? I swear, they—"
    show ren sad at spop, center
    r "—Your landlord isn't doing anything about it?"
    y "No!" with vpunch
    n "I collapse onto the sofa with a dramatic sigh."
    y "I honestly don't know what they're doing, if I'm being honest."
    y "I've sent sooo many complaints but haven't received a reply for {i}any{/i} of them."
    show ren neutral at spop, center
    r "R-Really? Have you considered just… {i}moving?{/i}"
    y "Quite a few times, actually. But…"
    
    #hide ren with dissolve

    menu:
        #with dissolve
        "The location is nice":
            $ affection_violet += 1
            $ affection_leon += 1
            $ affection_jae += 1
            show ren neutral with dissolve
            y "It was overwhelming at first, but…"
            y "Honestly? I think the low rent and location are the only things stopping me from considering other places to live."
        "This place has its charms":
            $ affection_conan += 1
            $ affection_olivia += 1
            show ren neutral with dissolve
            y "I mean… It was a bit overwhelming during the first month, but once you look past the smashed windows and broken elevators, the place is actually really nice."
            y "It's cosy, and it has its charms, and there's barely any traffic here."
        "My neighbour is friendly":
            $ affection_violet += 1
            $ affection_kiara += 1
            show ren neutral with dissolve
            y "Well, everything was a little overwhelming in the beginning…"
            y "But my neighbour was nothing but kind to me when I first moved in. And she always has the {i}best{/i} afternoon snacks."
        "[rh_o]I'm not sure what I like[rh_c]":
            $ ren_decay += 1
            $ affection_ren += 1
            $ affection_teo += 1
            show ren neutral with dissolve
            y "I suppose {i}this{/i} was the only place available at the time…"
            y "Everything was a bit overwhelming at first, but I really wanted to come back to Corland Bay."
            y "I figured this would only be a temporary thing. Y'know, until I got my bearings."

    show ren smirk at spop, center
    r "I-I see… Then it's not so bad here after all, right?"
    show ren blushing at spop, center
    r "I mean, as long as there's no creep trying to break in and steal all your laundry or something, haha…"
    y "Pfft. You've got a point there."
    y "I think I'd take the rats over a laundry-stealing intruder any day, but…"
    y "Now that I think about it, who would wanna break in just to steal dirty clothes?"
    n "While I'm sure [ch_ren] only meant it as a joke, it {b}was{/b} oddly specific."
    show ren flushed at spop, center
    r "O-Oh! Uhh…"
    show ren blushing at spop, center
    extend " I just figured that's what normal creep behaviour would be!"
    show ren flushed at spop, center
    r "Y-You have a great sense of fashion, a-and I see your TV is still here, so…"
    y "Haha, yeah, I guess it {i}would{/i} be difficult to lug that down a staircase."
    show ren happy at spop, center
    r "They probably should've asked the rats for help."
    y "Pffft—! {i}Again{/i} with the rats?"
    n "I couldn't help but let out a laugh at his corny inside joke."
    n "…Wait, since when did we have our own inside jokes?"
    n "Now that I {b}really{/b} thought about it, the banter I shared with [ch_ren] seemed very easygoing as of late — despite how serious the topics were supposed to be."
    n "I had been worrying all day about this supposed stalker, yet here I was, casually brushing it off as a carefree joke."
    show ren sad at spop, center
    r "Still… Is everything alright in your neighbourhood?"
    show ren frown at spop, center
    r "I've heard about the murders going on recently."
    y "Well, no one I know has gone missing, so I suppose that's good, right?"
    y "I won't lie, though; it {i}is{/i} kind of scary knowing that there's a killer out there."
    show ren sad at spop, center
    r "Y-Yeah, 'suppose so…"
    show ren frown at spop, center
    r "But are you {i}really{/i} okay with staying here alone? Doesn't that…"
    show ren smirk at spop, center
    extend " scare you?"
    y "I'm sure I'll be fine."
    y "I've got my neighbour, [ch_violet]. And if it's {i}reeeally{/i} necessary, I'm sure I could stay with [ch_leon] for a while and—"

    if d2_visitren == True:
        show ren flushed at bpop, center
        r "S-Say! You could always stay with me instead!"
        show ren happy at spop, center
        r "I mean, you've already stayed the night at my place, so it wouldn't be a bother if you wanted to come over again."
        show ren smirk at spop, center
        r "I'd honestly sleep better at night knowing you're safe."
    else:
        show ren flushed at bpop, center
        r "S-Say! You could always stay with me instead!"
        show ren neutral at spop, center
        r "I rent an apartment not far from here. You're always welcome to stay— {i}especially{/i} if it's an emergency."
        show ren smirk at spop, center
        r "I-I'd… I'd sleep better knowing you're safe."

    show ren happy at spop, center
    r "And I always carry a spare keycard with me anyway. If you'd like, you can hold onto it in case someth—"
    y "Ahhh… I appreciate the offer [ch_ren], but I can't accept that—"
    show ren flushed at spop, center
    r "I-It's fine! Besides, you said yourself that living here can get overwhelming."
    show ren sad at spop, center
    r "If this can help you in any way…"
    y "I don't know…"
    show ren neutral at spop, center
    r "Keep it, just in case. I mean, you never know…"
    show ren frown at spop, center
    extend " What if that creep breaks into your apartment again?"

    if d2_visitren == False:
        show ren flushed at spop, center
        r "If that happens, you could… You'd be safer at my place!"
        show ren neutral at spop, center
        r "L-Like I said, it not far from here."
    elif d1_inviteren == True:
        show ren flushed at spop, center
        r "If that happens, you could… You could come and stay with me this time!"
        show ren smirk at spop, center
        r "I could keep you safe, just like the first time you invited me over."
    else:
        show ren happy at spop, center
        r "If that happens, you could… You'd be safer at my place!"

    show ren neutral at spop, center
    r "The lobby is {i}full{/i} of security, a-and they won't let anyone upstairs without proper clearance."
    show ren blushing at spop, center
    r "Plus… Um… I don't have rats?"
    n "I won't lie, [ch_ren]'s offer honestly was tempting."
    n "The idea of having somewhere to go in case things got bad {b}was{/b} a comforting thought, but something just didn't sit right with me."
    n "I know I've been spending a lot of time with [ch_ren] recently, but I still wasn't that familiar with him."

    if relationship_ren == "crush":
        n "And sure, I might've developed a bit of a crush on the tall guy, but I wasn't going to be swayed by my feelings."
    else:
        n "And sure, maybe I {b}did{/b} invite a total stranger over to my place on a whim, but I wasn't going to be swayed just because I felt indebted to [ch_ren]."

    n "Still… The offer really was tempting. And it wasn't like he was asking me to move in with him or anything."
    n "Now that I thought about it… {b}[ch_ren]{/b} was the one giving me access to his home. It wasn't like {b}I{/b} was the one in danger here."
    n "He was trusting me enough not to be some kind of crazed killer — much like the one on the news."
    n "I can't help but crack a small smile at the (somewhat morbid) thought, and [ch_ren] seems to take it as a positive sign."
    n "But before I can dwell on it any further, I watch as he leans over to reach into his back pocket and pulls out something that resembled a plastic card."
    n "[ch_ren] wastes no time handing it to me, and I take a moment to look it over."
    n "His address and unit number are neatly printed at the top, and some kind of obscure barcode is on the bottom."
    n "However, the apartment name and logo in the top right corner are what {b}really{/b} captures my attention."
    
    $ persistent.fact_residence = True
    
    if d2_visitren == True:
        n "\"Sunshine Hills\"…? I almost forgot he lived in the nicer parts of Corland Bay."
        n "They were known for their high-rise apartments and fancy penthouses, so I'm sure [ch_ren] never had to worry about rat infestations or deadbeat landlords."
    else:
        n "\"Sunshine Hills\"…? He lived in the nicer parts of Corland Bay?"
        n "There was only one \"Sunshine Hills\" that I was familiar with, and they were known for their high-rise apartments and fancy penthouses."
        n "I'm sure [ch_ren] never had to worry about rat infestations or deadbeat landlords."

    n "Though… The more I thought about it, the more willing I was to accept his offer."
    n "Maybe it wouldn't be such a bad idea after all?"
    if d2_visitren == True:
        n "I couldn't help but wonder what kind of programmer could afford fancy marble flooring — but as always — [ch_ren] remained a mystery to me."
    else:
        n "Even though [ch_ren] lived in the more luxurious parts of town, would he really mind if I crashed at such an expensive place?"
        n "I know {b}he's{/b} the one who's offering, but still…"

    n "If this opportunity meant getting to know him better, maybe it'd be worth it?"
    n "Snapping out of my thoughts, I look up from the glossy plastic and focus my attention back to [ch_ren]."
    show ren sad at spop, center
    r "Seriously though, it wouldn't hurt to keep it."
    show ren blushing at spop, center
    r "A-And it's a spare keycard, anyway! I can always get more. I already have a stack of them at home."
    show ren smirk at spop, center
    r "They're real handy, too… I can use 'em to lock up my office and bedroom without a physical key."
    show ren sad at spop, center
    r "But I always end up misplacing them all, and—"
    show ren blushing at spop, center
    r "S-Sorry [ch_angel], am I rambling again? I just… Well, I don't want you to worry or anything."
    show ren frown at spop, center
    r "And… You never know what might happen."
    show ren sad at spop, center
    r "I've seen what's been on the news lately, and I just want you to be safe."
    n "He wants me to be safe? …Where have I heard that before?"
    y "Well, I suppose so."
    show ren neutral at spop, center
    r "Great! Then…"
    n "He glances back at the plastic item in my hands with an expectant look; almost as if he were waiting for me to put it away."
    n "And when I carefully shove it into my pocket, [ch_ren] seems to visibly relax and lean back into his chair once more."
    show ren happy at spop, center
    r "Then that settles it!"
    show ren smirk at spop, center
    extend " Come by whenever you want!"
    show ren happy at spop, center
    extend " You don't even need to call!"
    y "Err… Thanks."
    n "I think I'll still call him in advance… Or even shoot a text."
    n "As lovely as [ch_ren]'s… \"welcoming\" hospitality was, I wouldn't want to disrupt or intrude on anything."
    n "As if picking up on my sudden silence; he clears his throat, gestures towards the food on the table, and scoops up a giant forkful."
    show ren flushed at spop, center
    r "Anyway! W-We should… We should finish this before it gets cold."
    y "Oh… yeah! You're right."
    n "Deciding to ease the tension once more, I speak the first thing that comes to mind as I stab my fork into the container as well."

    #hide ren with dissolve

    menu:
        #with dissolve
        "\"Enjoying the food?\"":
            $ affection_ren += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            $ affection_violet += 1
            show ren happy with dissolve
            n "Despite having his cheeks stuffed full of food, [ch_ren] manages to send me a pleased look and an awkward thumbs up — which was a feat in itself, considering how he was trying to hold his utensils at the same time."
            show ren happy at spop, center
            r "—Ish good! Real tashty! Wan' some?"
            n "He offers some of his takeout to me, but I gently shove it back with a laugh."
            y "I think I'll pass."
            show ren neutral at spop, center
            r "Hehe, you're mishin' out!"
        "[rh_o]\"Can you pass the sauce?\"[rh_c]":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_jae += 1
            show ren neutral with dissolve
            n "With a nod, [ch_ren] reaches for the dipping sauce to his left and hands it to me."
            n "Our fingers accidentally brush, and I can't help the slight tinge of pink that blooms on my cheeks."
            n "[ch_ren] seems to be sporting a similar look of his own before he awkwardly clears his throat and goes back to eating."
            show ren blushing at spop, center
            r "…S-Sorry!"
        "\"You've got some crumbs on your face.\"":
            $ affection_ren += 1
            $ affection_elanor += 1
            $ affection_conan += 1
            $ ren_purity -= 1
            show ren flushed with dissolve
            n "Before I can stop myself, I reach out towards [ch_ren]'s face and gently wipe away the crumbs from his cheek."
            n "My fingers brush against his bottom lip, and I can't help the slight tinge of pink that blooms on my cheeks."
            n "[ch_ren] seems to be sporting a similar look of his own before he awkwardly clears his throat and goes back to eating."
            show ren blushing at spop, center
            r "Um… Th-Thank you."
        "\"You look like a hamster.\"":
            $ affection_ren += 1
            $ affection_teo += 1
            $ affection_olivia += 1
            $ ren_purity -= 1
            show ren flushed with dissolve
            n "Well, it was true. With how [ch_ren] was stuffing food into his mouth, he almost looked similar to a fluffy, pink hamster."
            n "Almost immediately after hearing my words, his cheeks flush a deep red as he chokes down his food."
            show ren blushing at spop, center
            r "H-Hamster? Usually, I get a fox or puppy…"
            show ren flushed at spop, center
            extend " I'm not mad, though."
            show ren smirk at spop, center
            r "Now that I think about it, you kind of look like a chipmunk."
            n "With an eye-roll, I playfully shove [ch_ren]'s arm and pretend like I {b}didn't{/b} agree with his words."
        "{image=14NWY symbol} \"Your fly's unzipped.\"" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
            call DLC_day3_inviteren from _call_DLC_day3_inviteren

    scene angel_lounge_night
    play music "audio/bgm/A Gentle Farewell.ogg" fadein 1 fadeout 1
    show peffectp
    with GlitchDissolve

    n "The casual banter continues throughout dinner, and soon enough, all the containers were empty, and our stomachs were full."
    n "I dimmed the lights and switched the TV on at some point to fill the silence between our conversations, and soon enough, [ch_ren] and I find ourselves taking an interest in a movie that was currently playing."
    n "It was some unknown, sappy romcom that came out almost a decade ago, yet [ch_ren] didn't seem to mind all that much."
    n "I wasn't following the plot too keenly, but from what I could gather, the male lead just confessed his love for the main character in the back of [their] truck."
    n "To top it all off, it started raining as some slow, melodic love song came on the radio. The two characters were all too happy to share a sweet kiss with each other in that romantic moment, but…"
    n "The tenderness soon gets cut short once the scene starts to travel down a more… heated path."
    n "The kisses become more passionate, and before I know it, I'm watching the main character lean across the center console to sit in [their] lover's lap instead."
    n "Clearly, I wasn't expecting this to happen in what I (falsely) believed was a harmless romcom, so I dared a glance in [ch_ren]'s direction to gauge his reaction."
    show ren blushing z with dissolve
    n "Yet aside from the faint dusting of pink on his cheeks, the rest of him seems all too relaxed."
    n "There's an arm casually thrown over the back of the couch while the rest of his body is slouched into the plushness of the seat."
    n "His lanky limbs are stretched out in front of him, while his thighs are spread out slightly — and the empty space between his legs was beginning to look {b}inviting{/b} for some reason."
    n "…Was it because of the movie?"
    n "Before I can stop myself, I find my mind wandering…"
    
    #hide ren with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "{image=14NWY symbol alt} Sit in his lap" if dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou == True and persistent.streamermode == False:
            $ choice_style = "default"
            show ren blushing z with dissolve
            n "A beat passes, and before my sudden confidence can crumble, I subtly slide across the couch and situate myself atop [ch_ren]'s lap."
            n "I can feel him tense up from underneath me… Before his arms come to wrap themselves around my side and pull me closer to his body."
            n "[ch_ren]'s breath ghosts along my skin as he whispers against the shell of my ear."
            show ren neutral z at spop, center
            r "Hey."
            y "H-Hi."
            show ren smirk z at spop, center
            r "Y'gotta keep watching the movie, Angel. Don't get distracted."
            n "And just like the male lead, [ch_ren]'s hands mimic his movements; gliding up and down my sides before resting on the plush of my thighs."
            n "I watch as the male lead leans in to kiss his love interest, and without missing a beat, I feel [ch_ren]'s mouth move to the back of my neck — right below my earlobe."
            n "My breath hitches the moment he makes contact, and I softly squirm in his lap. His lips are soft and warm against my skin, and his own breath sends goosebumps running across my body."
            n "My face grows hot when I see the main character take off [their] own shirt, and I boldly follow along with [ch_ren]'s game and move to do the same."
            if d2_visitren == True:
                if bust == "breast":
                    n "Leaning forward a little bit, I quickly shrug off [ch_ren]'s hoodie and my bra, and let it drop to the floor."
                else:
                    n "Leaning forward a little bit, I quickly shrug off [ch_ren]'s hoodie and my undershirt, and let it drop to the floor."
            else:
                n "Leaning forward a little bit, I quickly make work of my top by tugging it off and letting it drop to the floor."
            n "The cold, evening air of my apartment ghosts along my exposed skin before [ch_ren] wraps his arms around my body to share his warmth."
            n "His lips return to the side of my neck once more — only this time — he's nuzzling his head and breathing in my scent with a soft sigh."
            n "I can barely focus on the movie at this point; [ch_ren]'s ministrations were far too distracting, and I find myself squeezing my eyes shut and losing myself in all of the pleasure."
            n "…But it seems he had other plans in mind."
            show ren neutral z at spop, center
            r "Eyes open, Angel."
            n "Almost blearily, I open my eyes in time to see the main character's hands trail down [their] lover's chest before removing his shirt."
            n "…Did [ch_ren] want me to do the same?"
            n "Testing my luck, I twist around in his lap to face him."
            n "[ch_ren] seems all too distracted with kissing along the juncture of my neck, so when I tug on the ends of his cardigan in a silent attempt to get him to take it off, he doesn't seem to notice."
            n "But once my fingers slip underneath and run along the hardened muscles of his abdomen, [ch_ren] pulls back with a dark look in his eyes."
            show ren smirk z at spop, center
            r "A-Alright… But on one condition, though. Turn around."
            hide ren with dissolve
            n "Movie long forgotten, I do as he says. Almost eagerly, I move out of [ch_ren]'s lap to give him room and face the other way."
            n "I can hear the sounds of fabric rustling from behind me, before [ch_ren] brings his white turtleneck into view and folds it into a narrow strip before me."
            n "Once he's done, he slowly brings it towards my face and holds it mere inches away from my eyes — clearly asking for permission to continue."
            n "And when I show no signs of protest, he gently covers my eyes and ties the ends behind my head; effortlessly blindfolding me."
            jump day3_wahooscene
        "[rh_o]Keep watching the movie[rh_c]" if dlc_14nightswithyou_scenes == False or persistent.dlc_14nightswithyou == False or persistent.streamermode == True:
            $ choice_style = "default"
            $ affection_ren += 1
            show ren blushing z with dissolve
            n "…What was I thinking?! This movie was clearly messing with my head. Subtly, I slap my cheeks and focus my attention back to the TV screen."
            n "But every so often, my gaze flickers back to [ch_ren] to see if he was feeling just as awkward as I was throughout the scene — and it seems I was right."
            n "It's almost painful watching him awkwardly clear his throat a few times until his interest ultimately shifts towards my wall instead."
            n "I also feel the urge to look away once the couple starts to get {b}even more{/b} handsy with each other, and when it starts to become too much to bear, I impulsively change the channel."
        "Change the channel":
            $ choice_style = "default"
            $ affection_ren -= 1
            show ren blushing z with dissolve
            n "…What was I thinking?! This movie was clearly messing with my head. Subtly, I slap my cheeks and focus my attention back to the TV screen."
            n "Not wanting to let this awkward encounter draw out any longer, I reach for the remote and flick to the local news station instead."

    n "A monotone voice droning on about the weather fills the silence, and I feel the couch move as [ch_ren] shifts in his seat."
    show ren flushed z at spop, center
    r "Th-That was… Um…"
    y "Yeah…"
    show ren blushing z at spop, center
    r "They were really going at it, huh?"
    y "Mhmm."
    show ren flushed z at spop, center
    r "Haha…"
    n "Jeez, I can't believe it's somehow even more awkward now."
    n "But just as I'm about to do something about it, [ch_ren] awkwardly clears his throat and moves to stand up."
    show ren sad at spop, center with dissolve
    r "It's getting a bit late now, isn't it? I should probably start heading home soon."
    y "Oh. Are you sure? You can stay a bit longer."
    show ren neutral at spop, center
    r "N-No, I really should go. Now that I think about it, you need to wake up early, don't you?"
    y "…Yeah, actually. But how did you know that?"
    show ren flushed at spop, center
    r "Oh! Y-You seem like the early bird type."
    n "He doesn't seem to elaborate on that, and instead starts to pack up his belongings and head towards the hallway."
    hide ren with dissolve
    n "Deciding that was that, I walked [ch_ren] towards the front door with a soft smile on my face."
    n "Today had been a lot of fun thanks to him, and I was able to keep my mind off of the events that would ultimately transpire tomorrow."
    n "I was still unsure about [ch_teo]'s intentions, but being with [ch_ren] helped me to understand that maybe it was wrong of me to judge others so quickly."
    n "At first, I thought [ch_ren] was just some shy guy with a stuttering problem… But over the course of a few days, I've learned there's more to him than just that."
    n "He had his moments of confidence, and it was endearing watching him stand up for the things that he wanted."
    n "…Perhaps I was being a bit too harsh on [ch_teo]. Even {b}he{/b} deserved a chance to redeem himself."
    n "I suppose I'll give him a chance tomorr—"
    show ren sad with dissolve
    r "[ch_angel]?"
    y "S-Sorry?"
    n "Crap. I really needed to stop spacing out like that."
    show ren neutral at spop, center
    r "I… Um… I asked if you wanted me to lock the door for you."
    n "It suddenly hit me like a ton of bricks. I was still standing in the hallway while [ch_ren] was already waiting for me at the door — so I quickly rush over to him with a flushed expression."
    y "Sorry! I was just… busy thinking. I can lock it. Thanks though."
    show ren happy at spop, center
    r "Haha, you do that a lot. It's cute."
    n "I almost roll my eyes at his words as I lean against the front door and watch [ch_ren] awkwardly shuffle on my doormat."
    show ren smirk at spop, center
    r "Thanks for today. A-And sorry for taking up so much of your time."
    y "Not at all. Thanks for coming over. Get home safe, okay?"
    n "[ch_ren]'s eyes seem to light up the moment I voice my concern over him."
    show ren flushed at spop, center
    r "Y-Yeah! Okay!"
    show ren happy at spop, center
    extend " I will!"
    show ren neutral at spop, center
    extend " You too! Or— I mean—"
    show ren blushing at spop, center
    r "Y-You're already at home, so… Go to bed safe! Or sleep safe! …Sleep well?"
    show ren sad at spop, center
    r "…Um— {size=-6}What am I—{/size}"
    n "I can't help but chuckle at his panicked state, and [ch_ren] seems to settle once he hears my laughter."
    y "Goodnight, [ch_ren]."
    show ren happy at spop, center
    r "G-Goodnight, [ch_angel]! I'll see you tomorrow!"
    hide ren with dissolve
    n "The sound of the door shutting drowns out the ending of his sentence."
    jump day3_dayend

################################################################################
## INVITING MOTH OVER
################################################################################
label day3_invitemoth:
    mcall "Well, well, well! Look who came crawling back."
    mcall "Sorry about earlier; I'm not sure what the deal is with my wi-fi."
    y "Hold up— Rewind. Why am I crawling?"
    mcall "Why wouldn't you be? I'm the only person you know who has the all the latest AoG gossip."
    mcall "Anyway! What's up, [player_fl]?"
    y "Felt bored. Wanted to hear your lovely voice again."
    mcall "Pleeease. I can hear the sarcasm dripping through the phone right now. Seriously, what's up?"
    n "How did they know me so well?"
    y "Actually… I'm going on this double date tomorrow. Except it's not really a date. For me, at least."
    mcall "And how is it not a date? You'll be hanging out with someone you're interested in, right?"
    y "No. It's my best friend."
    mcall "Heh… Me? I didn't know we were going on a date together. I'm flattered, dude!"
    n "Oh. Um…"
    y "M-My other best friend!"
    mcall "…I'm going to pretend like you {i}didn't{/i} just pause for six whole seconds to come up with that lame excuse."
    n "Despite the harsh words, I could tell [ch_moth] was joking. Their eye-roll was practically audible."
    mcall "So what's so bad about this {i}\"not-a-date\"{/i} date with your {i}other{/i} best friend?"
    y "Well, for starters, he's someone I've practically known since birth."
    y "And the other two people happen to be my co-worker with the most purest soul I've ever seen—"
    extend " And my other friend, who's probably the devil incarnate."
    mcall "I think I've seen an anime about that once—"
    y "[ch_moth]! Not helping."
    mcall "Haha, sorry."
    mcall "Look, you said it yourself. You're not going on an {i}actual{/i} date, so there shouldn't be anything to worry about, right?"
    y "You don't understand. It's not [ch_leon] I'm worried about…"
    n "Was I really about to let [ch_moth] in about the more… personal details regarding my friendships?"
    extend " Welp, I guess there's a first for everything."
    y "[ch_teo] is honestly the worst person for [ch_elanor]."
    y "He isn't exactly the type to settle down, and El's the biggest hopeless romantic I know."
    y "She always talks about having that white picket fence dream, whereas [ch_teo] can barely sit through a single conversation about his own feelings."
    n "I knew I was beginning to ramble at this point, but I couldn't seem to stop myself."
    y "And what's worse is that [ch_teo] is suddenly interested in relationships all of a sudden. I don't get what his motives are."
    mcall "…I'm sure people can change? Maybe he's entering his magical girl era."
    n "It was a weak response, but I could tell [ch_moth] was being sincere about it."
    mcall "I mean, from what you've told me in the past, your co-worker sounds like a real nice gal. Maybe [ch_teo] feels the same way?"
    y "It just doesn't seem like something he'd do, though."
    n "I let out a sigh and absent-mindedly run my hands over my pants in order to smooth out the wrinkles."
    y "Sorry M, you probably didn't expect me to call you up just to rant to you."
    mcall "Hey, it's all good. I don't mind — and you know I always do the same."
    mcall "Besides! It's my duty as your bestest-est friend. Both online and in real life!"
    n "I couldn't help but chuckle at that."
    y "But… Saying \"real life\" implies we've met in person already."
    mcall "{glitch=3.0}Funn— you say that, [player_fl], 'cause I'll {/glitch}{glitch=5.0}b— your ar— {/glitch}{glitch=4.0}soon!{/glitch}"
    mcall "{glitch=8.0}Maybe— Could{/glitch}{glitch=10.0}— If your—{/glitch}"
    n "All of a sudden, the call cuts out for the {b}second{/b} time today."
    n "[damn!c]. Curse their horrible wifi."
    n "Well. There wasn't much I could do about a faulty connection."
    jump day3_rencanonevent

################################################################################
## INVITING VIOLET OVER
################################################################################
label day3_inviteviolet:
    scene violet_apartment_day
    show peffect
    show violet happy
    play music "audio/bgm/Summer Memories.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/windchime.ogg" fadein 1 fadeout 1
    with GlitchDissolve
    $ d3_inviteover = True

    n "Following the flowery scent towards [ch_violet]'s front door, I barely have to knock two times before my neighbour appears on the other side with a gentle expression on her face."
    show violet neutral z at spop, center with dissolve
    v "Come in, come in! Make yourself at home. I'll bring us some snacks while you get settled!"
    show violet smirk z at spop, center
    v "Now that I think about it, I don't think you've met Kristy yet!"
    n "[ch_violet] gently ushers me into her open plan kitchen before muttering something about retrieving a few things from the pantry."
    n "She disappears from my sight momentarily, only to return once more with her hands full and a bounce in her step."
    n "Alongside a tray of (what looked like homebaked) cookies and a teapot, [ch_violet] reveals a potted gardenia up to eye level and pretends to make it wave by moving one of its leaves."
    show violet happy z at spop, center
    v "This is Kristy! She's very shy. But here, help yourself to anything you'd like!"
    n "My neighbour's smile doesn't seem to falter as she offers me a plate of cookies and some herbal tea, before she grabs some for herself as well."
    show violet frown z at spop, center
    v "You know… Your aura seems off today. Have you eaten yet?"
    y "Not yet. I've been feeling a bit ansty since this morning if I'm being honest."
    show violet sad z at spop, center
    v "Oh dear! What happened?"
    y "Well…"
    n "Was I really about to confide in my neighbour about rather… personal details regarding my friendships?"
    extend " Welp, I guess there's a first for everything."
    y "Actually… I'm going on this double date to the aquarium tomorrow. Except… Well, it's not {i}exactly{/i} a date."
    show violet sad z at spop, center
    v "I'm not quite sure I follow? It's {i}not{/i} going to be a date?"
    y "Well, my childhood friend and I kinda got roped into tagging along on an outing between a co-worker and my friend, [ch_teo]."
    y "He's been adamant on calling it a double date."
    show violet z frown
    n "I watch as [ch_violet]'s face scrunches up at the mention of [ch_teo]'s name — which made sense, considering how she's been well acquainted with him in the past."
    n "I didn't know the {b}exact{/b} details of their history, but I did know that [ch_teo] and [ch_violet] never really got along with each other."
    show violet sad z at spop, center
    v "That big musclehead is still up to his usual antics?"
    y "Unfortunately. It all seems rather odd, though."
    y "I mean, you and I both know he isn't the type to settle down, and [ch_elanor] — my co-worker — is the biggest hopeless romantic I know."
    y "She always talks about having that white picket fence dream — whereas [ch_teo] can barely sit through a single conversation about his own feelings."
    n "I knew I was beginning to ramble at this point, but I couldn't seem to stop myself."
    y "And what's worse is that [ch_teo] is suddenly interested in relationships all of a sudden. I don't get what his motives are."
    show violet angry z at spop, center
    v "…He certainly {i}is{/i} a cunning person. I wouldn't put it past him."
    n "It was a weak response, but I could tell [ch_violet] was trying to be considerate of my feelings."
    show violet sad z at spop, center
    v "Though… It {i}has{/i} been a while since I've last spoken to [ch_teo]. Perhaps he's changed his ways?"
    y "It doesn't really seem like something he'd do, though."
    n "I let out a sigh and absent-mindedly run my hands over my pants in order to smooth out the wrinkles."
    y "Sorry, Vi. You probably didn't expect me to come over just to rant about my problems."
    show violet happy z at spop, center
    v "It's quite alright, [ch_angel]! I'm always happy to lend an ear."
    show violet neutral z at spop, center
    v "And sometimes it's good to get your thoughts out. It helps to—"
    play audio "audio/sfx/vibrate.ogg"
    n "All of a sudden, [ch_violet]'s phone starts to buzz in her pocket. She sheepishly pulls it out, only to frown at the message displayed on the screen."
    show violet sad z at spop, center
    v "Oh dear. Something's gone wrong at work. I'm sorry, but I think I'll need to—"
    y "Oh, go ahead! I should head back home anyway. Sorry for taking up so much of your time."
    show violet smirk z at spop, center
    v "There's nothing to be sorry for. We had a lovely time together, didn't we?"
    show violet happy z at spop, center
    v "Here, take some more cookies before you go!"
    n "I don't get much of a choice before [ch_violet] deposits more of her baked goods onto my empty plate and places it into my hands."

    scene oh_complex_night
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    stop ambience fadeout 2.0
    show peffectp
    with GlitchDissolve

    show violet smirk z with dissolve
    n "She even walks me to her door before stepping out behind me as well, and it has me wondering if she was about to head to her workplace at this hour."
    n "But it seems my thoughts get answered once [ch_violet] procures a set of keys from somewhere and begins the {b}lengthy{/b} process of locking her door."
    n "When I catch that landlord again, I swear—"
    show violet neutral z at spop, center
    v "Enjoy the rest of your evening! Oh, [ch_angel]?"

    if d2_visitren == True:
        n "Her gaze seems to fall from my face towards my outfit, and it's then when I realise I'm still wearing the hoodie [ch_ren] gave me today."
        show violet frown z at spop, center
        v "Where did you—"
        show violet smirk z at spop, center
        v "…No, never mind. Good night, [ch_angel]."
        show violet neutral z at spop, center
        v "Make sure to lock your door once you're inside."
    else:
        n "Her gaze seems to drift from my face to the stairwell behind me."
        show violet sad z at spop, center
        v "No, never mind. Good night, [ch_angel]."
        show violet neutral z at spop, center
        v "Make sure to lock your door once you're inside."
    y "Um, sure?"
    n "With that awkward farewell, I leave [ch_violet] to her own devices and head back to my apartment across the hall."
    jump day3_rencanonevent

################################################################################
## INVITING ELANOR OVER
################################################################################
label day3_inviteelanor:
    scene angel_lounge_day
    show peffect
    play music "audio/bgm/After The Rain.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)
    $ d3_inviteover = True
    $ location_elanor = "apartment"

    e "{size=-6}Hellooo? [ch_angel]? I hope I got the right address…{/size}"
    show elanor neutral z with dissolve
    n "Barely twenty minutes pass before I hear [ch_elanor]'s soft voice at my front door. Almost immediately, I leap to my feet and unlock it with a smile."
    y "[ch_elanor]! Hey! Sorry for calling you over on such short notice. Especially after chatting your ear off for the entire day."
    show elanor smirk z at spop, center
    e "It's no problem. I don't mind spending more time with you."
    show elanor happy z at spop, center
    extend " That reminds me!"
    n "Without missing a beat, [ch_elanor] reaches into the depths of her handbag and pulls out a small object."
    show elanor smirk z at spop, center
    e "Tadaaa! Your favourite bookmark! I found it all alone on one of the shelves earlier today."
    n "Oh? Did I really lose one of my anime-themed bookmarks? I thought I left it beside my other stationary equipment by my desk…"
    extend " What was it doing on a shelf?"
    y "Hey, thanks! I don't remember leaving it there, though."
    show elanor sad z at spop, center
    e "Oh? Perhaps one of the children put it there? You know how they can get."
    y "You've got a point. I wouldn't put it past {i}[ch_teo]{/i} to do such a thing."
    show elanor z blushing
    n "Although I was only trying to make a silly, light-hearted joke, I notice [ch_elanor]'s posture straighten up at the mention of [ch_teo]'s name."
    y "Everything okay?"
    show elanor flushed z at spop, center
    e "I'm… Rather nervous, actually."
    show elanor blushing z at spop, center
    e "This is a little embarrassing, but it's been a rather long time since I've gone on a date with someone."
    n "[ch_elanor] tries to hide her flushed cheeks by stuffing her face full with some of the snacks I laid out on my coffee table."
    y "Are you worried about [ch_teo]? He's not exactly a bad guy, but…"
    show elanor sad z at spop, center
    e "[ch_angel]"
    n "She slightly tilts her head to the side in confusion, and admittedly, I find it rather adorable."
    show elanor neutral z at spop, center
    e "What's wrong?"
    y "Can I be completely honest with you, El?"
    n "Almost immediately, she nods her head and scoots closer to me. One of her hands reaches for mine, and she gently gives it a squeeze in a reassuring manner."
    y "[ch_teo] isn't…"
    y "Well, he's not exactly the type of person who wants to settle down or be in a relationship. Let alone go on dates unless it's for his own benefit."
    n "I search her face for any sort of reaction before continuing."
    y "It was… honestly a little strange watching him act that way in the library this morning…"
    show elanor frown z at spop, center
    e "Oh."
    n "I feel the sudden pang of guilt wash over me as [ch_elanor] pulls away slightly, bringing both of her hands to her chest as if it'd make herself seem smaller."
    show elanor sad z at spop, center
    e "I-I suppose it would be a bit silly for a good-looking guy like [ch_teo] to be interested in someone like me…"
    y "Hey now—"
    show elanor frown z at spop, center
    e "It's okay! I'm fine. Really. This wouldn't be the first time something like this has happened…"
    show elanor neutral z at spop, center
    e "But I'll get over it! Nothing a good romance novel can't solve!"
    n "She gives me a soft smile, though I can tell by the shakiness of her voice that she wasn't speaking the truth."
    n "…Was it really that hard for me to accept that maybe [ch_teo] was interested in [ch_elanor] after all?"
    y "Listen. You're lovely, El. I'm sure [ch_teo] noticed it, too, which would explain why he was so insistent on inviting you out."
    show elanor sad z at spop, center
    e "…You really think so?"
    y "I know so. I couldn't ask for a better workmate."
    show elanor happy z at spop, center
    e "Heh… M-Me too! You don't know how happy I am to work with someone like you, [ch_angel]. And—"
    play audio "audio/sfx/vibrate.ogg"
    n "All of a sudden, [ch_elanor]'s phone vibrates from somewhere within her handbag, alerting her of an incoming text."
    show elanor neutral z at spop, center
    e "Oh—! Ermm… It seems [ch_kiara]'s having trouble with something at home. Do you mind if I…?"
    y "Oh! Yeah, go for it! Sorry for inviting you over at such a late notice."
    show elanor happy z at spop, center
    e "It's okay. I'll always make time for you!"
    show elanor smirk z at spop, center
    e "I really must get going, though. Thank you for having me over!"
    show elanor happy at spop, center with dissolve
    e "Make sure to eat something more hearty before you go to bed! But wait an hour before sleeping!"
    y "I will."
    show elanor smirk at spop, center
    e "And drink water!"
    y "I will!"
    show elanor happy at spop, center
    e "And don't forget to close your window before—"
    hide elanor with dissolve
    e "{size=-6}Oh, hello [ch_violet]! And hello Catherine! It's been a while since I've seen you both!{/size}"
    n "Not wanting to see how that conversation will unfold, I quickly retreat back into the safety of my hallway."
    jump day3_rencanonevent

################################################################################
## INVITING CONAN OVER
################################################################################
label day3_inviteconan:
    n "Admittedly, calling up my boss wouldn't be the {b}weirdest{/b} thing for me to do."
    n "The phone rings and rings, though no one seems to pick up."
    n "…Perhaps he was busy? Or maybe he was still at the library?"
    n "But before I can berate myself for doing something so ridiculous as calling my employer so late in the evening, [ch_conan] {b}finally{/b} answers."
    ccall "…Yes?"
    y "Um— [ch_conan]? This is [ch_angel]."
    ccall "Ah, [ch_angel]. Good evening."
    ccall "Is everything alright? It's a bit late for these sorts of calls."
    n "His concern is evident in his tone, and I almost feel bad for making him worry."
    y "Yeah… Sorry. I know it's late, but…"
    y "I-I… I just wanted to call you so you'd have my number!"
    n "Woooow, nice save [ch_angel]."
    y "Now that I think bout it, maybe texting you would've been a better idea…"
    ccall "It's quite alright. As long as you're fine. Thank you for your number."
    y "Thank you for giving me yours."
    n "Oof. This conversation couldn't get any more awkward, could it?"
    ccall "…Of course. Your safety means a lot to me."
    ccall "In the event that something should happen, don't hesitate to call me."
    y "Right."
    n "An awkward pause ensures, and I'm so close to pretending that the connection dropped just so that I could end the call."
    n "But it seems fate is on my side tonight — because suddenly, something on the other end of the line captures [ch_conan]'s attention and pulls him away momentarily."
    ccall "Ah… I believe Alice needs my assistance. I'll have to go shortly."
    y "O-Oh! That's fine! No worries. Thanks again for talking with me."
    ccall "And you as well, sweetheart."
    extend " We'll have to continue this conversation another time. Perhaps when we're both free."
    n "…Sweetheart?"
    y "Y-Yeah! Sure! Definitely!"
    n "Ugh. I was beginning to sound a lot like [ch_ren]."
    ccall "Goodnight, [ch_angel]. Enjoy the rest of your evening."
    n "All of a sudden, the line cuts off."
    n "Well. There wasn't much sense in dwelling over that painful encounter."
    jump day3_rencanonevent

################################################################################
## INVITING JAE OVER
################################################################################
label day3_invitejae:
    scene jae_cabin_night
    show peffectp
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)
    $ d3_inviteover = True

    n "The walk to [ch_jae]-Hyun's abode was a peaceful one, and I was grateful for the seaside scenery to keep the air cool and my mind occupied."
    n "Soon enough, I find myself on his doorstep, and I barely have to knock three times before [ch_jae] appears on the other side."
    show jae neutral z with dissolve
    j "Heeeeey! Welcome!"
    show jae happy z at spop, center
    extend " Make yourself at home!"
    show jae happy z at spop, center
    extend " Mi casa es su casa!"
    n "[ch_jae] shuts the door behind me and ushers me deeper into his cosy, little beachfront cabin."
    show jae happy at center with dissolve
    n "The faint smell of saltwater and driftwood greets me, before [ch_jae] shuffles past to fully open the curtains and let in more of the cool evening breeze."
    show jae sad at spop, center
    j "You just missed [ch_teo]! He dropped by earlier and took Maple with him."
    show jae smirk at spop, center
    j "You know how much she loves driving around with the windows down. I'd do the same if my car wasn't so busted."
    y "{i}Busted?{/i} Or is it the fact that you can't go more than ten meters without hitting something?"
    show jae happy at spop, center
    j "Oh, har har. I'll be sure to remember that the next time you ask me to drive you somewhere."
    n "He casually plops himself onto the sofa before moving a pillow and gesturing for me to join him."
    n "[ch_jae] already had a bag of microwaved popcorn waiting on the table for us, and when I glanced at the television, I noticed some sort of TV show playing on mute."
    show jae neutral at spop, center
    j "Just dust off Maple's hair if you see any! She likes to sit in that spot and watch the seagulls."
    y "I miss her already."
    show jae happy at spop, center
    j "haha! You know she misses you too! I'll bring her around your place next time. Your apartment allows dogs, right?"
    y "…Rats too, apparently."
    show jae sad at spop, center
    j "Huh?"
    y "Nothing. So!"
    extend " Anything new happen lately? Got any big plans for Friday?"
    show jae neutral at spop, center
    j "I was thinking about visiting my parents in the city again. It's been a while, and I'm sure they miss me."
    show jae smirk at spop, center
    j "I mean, who doesn't?"
    n "At that, he playfully tosses a piece of popcorn into the air and effortlessly catches it in his mouth."
    show jae happy at spop, center
    j "What about you? Any plans of your own?"
    y "You won't believe whose date I'll be third wheeling tomorrow."
    show jae neutral at spop, center
    j "No, don't tell me…"
    show jae smirk at spop, center
    extend " [ch_teo] and [ch_violet]?"
    y "Pfft! No way. Doesn't she hate his guts?"
    show jae happy at spop, center
    j "That makes it funnier! But if it's not [ch_violet]…"
    show jae smirk at spop, center
    extend " Then it's [ch_teo] and [ch_leon]."
    y "Close, but no. [ch_leon] will be there, though."
    show jae neutral at spop, center
    j "Well, now you've got me all confused."
    n "With a fake sigh, I end up telling [ch_jae] the whole story."
    y "It's [ch_teo] and my workmate [ch_elanor]."
    show jae frown at spop, center
    j "…[ch_elanor]? She's the blonde one, right? Who knocks over books all the time?"
    show jae neutral at spop, center
    j "I think you've told me about her once."
    y "I wouldn't say {i}all{/i} the time… But yeah. [ch_teo] seems interested in her."
    show jae smirk at spop, center
    j "Interested? Like… You know… {i}Interested?{/i}"
    y "{i}Interested{/i} interested. And worst of all, I can't figure out why."
    y "You and I both know he's not the type to go on dates with people."
    show jae happy at spop, center
    j "[ch_teo] and romance? Unheard of."
    n "I couldn't help but laugh at that."
    n "Throughout all my years of knowing Teodore Alvarado, I have never once heard about him going on dates with anyone."
    n "He could definitely get intense and possessive at times, but nothing like… {b}this.{/b}"
    n "He just wasn't that type of guy, and I was worried about what [ch_elanor] was getting herself into."
    n "But still… People change all the time. I'm sure it wouldn't be impossible for [ch_teo] to do the same."
    show jae frown at spop, center
    j "—Ah, crap."
    n "[ch_jae]'s sudden outburst pulls me away from my thoughts, and I glance over to find him looking at something on his phone."
    n "As if picking up on my confusion, he immediately fills in the blanks."
    show jae frown at spop, center
    j "Maple's gone and rolled in some dirt again, and [ch_teo] absolutely {i}refuses{/i} to let her back in his car."
    show jae sad at spop, center
    j "I'm so sorry, but do you mind if I—"
    y "Oh, not at all! I didn't realise it had gotten so late, anyway."
    show jae neutral at spop, center
    j "I can drop you home if you want! It's on the way."
    y "It's okay. I could use some more fresh air."
    show jae neutral at spop, center
    j "If you're sure, then…"
    y "I'm sure. Thanks for letting me drop by."
    n "[ch_jae] beams at that, and before I step out the door, I offer one last request."
    y "Give Maple a good belly rub for me!"
    jump day3_rencanonevent

################################################################################
## INVITING LEON OVER
################################################################################
label day3_inviteleon:
    n "The phone rings a few times before his warm voice and the ocean greets me, and I find myself wondering why he's still on the beach at this hour."
    n "Probably starting to pack up after a day of volleyball with a few of his friends, no doubt…"
    lcall "Evenin' Sunfish! What's up? Everything good?"
    y "Hey, [ch_leon]. Sorry for calling you so late."
    y "I know we already saw each other earlier, but… I guess I wanted to hear your voice again."
    lcall "Aww, missed me that much? Haha, I'm flattered!"
    extend " I missed your voice, too."
    n "I feel at ease talking with my childhood friend — and it probably shows, given how I instantly start to melt into the sofa with a soft sigh."
    lcall "But seriously though, is everything okay? I can come over if ya want."
    y "Naw, it's fine. You don't have to do that."
    y "If I'm being honest, I think I've had my fair share of face-to-face conversations already."
    lcall "…Yeah? You did seem tired earlier today."
    y "I'll probably be even more tired tomorrow knowing [ch_teo] will be involved."
    lcall "Hah! Yeah, he's got that effect on people, unfortunately."
    n "I can hear [ch_leon] let out another soft chuckle at his own silly joke."
    lcall "Speaking of, are you still good with our plans for tomorrow?"
    y "Yeah, I'm still up for it. But it's [ch_elanor] I'm more worried about."
    lcall "How so?"
    n "Was I really about to confide in [ch_leon] about rather… personal details regarding my friendships?"
    extend " Welp, I guess there's a first for everything."
    y "…[ch_teo] is honestly the worst person for her."
    y "I mean, you and I both know he's not exactly the type to settle down, and El's the biggest hopeless romantic I know."
    y "She always talks about having that white picket fence dream, whereas [ch_teo] can barely sit through a single conversation about his own feelings."
    n "I knew I was beginning to ramble at this point, but I couldn't seem to stop myself."
    y "And what's worse is that [ch_teo] is suddenly interested in relationships all of a sudden. I don't get what his motives are."
    lcall "…Maybe he's trying to change his ways? You know how [ch_teo] can be. The bloke's always full of surprises."
    n "It was a weak response, but I could tell [ch_leon] was trying his best to reassure me."
    lcall "Besides, I met [ch_elanor] today, and she seems real sweet. Maybe [ch_teo] feels the same way?"
    y "It just doesn't seem like something he'd do, though."
    lcall "Yeah… Guess so."
    n "I let out a sigh and absent-mindedly run my hands over my pants in order to smooth out the wrinkles."
    y "Sorry [ch_leon], you probably didn't expect me to call you up just to rant to you."
    lcall "Haha, no worries darl'. You can always come to me for anything."
    lcall "{glitch=2.0}I don't mi— even if it's{/glitch}{glitch=3.0} m— know?{/glitch}"
    n "His voice gets cut off before the only thing I can hear is static noise."
    y "Uhh… [ch_leon]?"
    lcall "{glitch=3.0}Gahh— Hello? The reception is {/glitch}always spotty— {glitch=2.0}here…{/glitch}"
    lcall "{glitch=5.0}Hey, are you still there, [ch_angel]?{/glitch}{glitch=7.0} I might have— end this call.{/glitch}"
    y "I'm still here. Can you hear me?"
    lcall "{glitch=6.0}Barely! Listen, I gotta go now— {/glitch}{glitch=5.0}but if anything comes up,{/glitch}{glitch=4.0} just text me, yeah?{/glitch}"
    lcall "{glitch=5.0}I'll call you back as{/glitch}{glitch=7.0} so— as I'm able to.{/glitch}"
    y "Don't worry about it, [ch_leon]. Thanks for talking to me. Get home safe, alright?"
    lcall "{glitch=6.0}Well, now tha— you've said that, I think{/glitch}{glitch=7.0} I'm going to do the {/glitch}{glitch=5.0}opposite!{/glitch}"
    lcall "{glitch=6.0}Haha, just kidding. See {/glitch}{glitch=7.0}yo— tomorrow, Sunfish!{/glitch}"
    n "All of a sudden, the line cuts off."
    n "Well. There wasn't much I could do about a faulty connection."
    jump day3_rencanonevent

################################################################################
## INVITING TEO OVER
################################################################################
label day3_inviteteo:
    n "It was almost a humbling experience sitting here and waiting for [ch_teo] to answer."
    n "His hand was practically {b}glued{/b} to his phone at all times, so I knew for a fact that he was aware of me calling — and was probably letting it draw out this long for his own personal entertainment."
    n "But just when I'm about to end the call and do something more productive instead, he finally answers in that smug tone of his."
    tcall "Still thinking about me? It's barely been a few hours."
    y "Unfortunately. Are you doing anything right now?"
    tcall "I might be doing {i}someone{/i} later if that's what you're asking."
    y "It wasn't."
    tcall "Aww, don't be like that, Doll. I'm just messing with you."
    tcall "What? Are you bored or somethin'? Want me to change that?"
    y "Yes, actually. Do you mind coming over? I have food."
    tcall "You think I'd prefer food over you? That's really cute."
    n "I can hear shuffling from his end and what sounds like the television being turned down."
    tcall "Actually… You live on the north side of the Bay, right? In that decrepit, run-down complex?"
    y "Okay, ouch. And yes. But it's only decrepit if you squint. Everything looks fine on the outside."
    tcall "…Yeah? If that's the case, then I think I'm gonna do a rain check on this little evening rendezvous."
    y "What? Why?"
    tcall "No reason. I just suddenly changed my mind. But don't worry."
    n "I can hear [ch_teo] shift again before the sounds of the ocean filter in, cluing me in on his whereabouts."
    n "He's probably in his beachside villa; standing on one of his {b}many{/b}, stupidly expensive balconies that overlook the beach."
    tcall "We'll be seeing each other tomorrow. Surely you can wait that long."
    y "You mean you'll be seeing {i}[ch_elanor]{/i} tomorrow, right?"
    n "Feeling brave, I figure I might as well call him out on his strange behaviour from this morning."
    tcall "…The blonde one? Sure."
    y "{i}'Sure?'{/i} You don't exactly sound too certain. Or happy, for that matter."
    tcall "And you don't exactly sound jealous to me, either."
    y "…What?"
    n "Jealous? Did he really just say that… Again? Why on earth would [ch_teo] want me to feel that way?"
    n "He was so obviously showing interest in [ch_elanor] this morning, so what did my feelings matter to him?"
    tcall "Nothin'. Look, something just came up."
    extend " I'll see you tomorrow. Cya."
    y "[ch_teo]—"
    n "All of a sudden, the line cuts off."
    n "Jeez… What was up with him today? This wasn't like his usual self, and it was throwing me for a loop."
    n "But {b}great.{/b} Thanks to [ch_teo], I'm annoyed again."
    jump day3_rencanonevent

################################################################################
## INVITING OLIVIA OVER
################################################################################
label day3_inviteolivia:
    ocall "Hello?"
    n "Mustering the deepest, fakest voice I can, I reply back."
    y "Is this [ch_olivia]? Is your— Uhh… Hold on."
    y "Actually, I'm… I'm… Uh— I'm the guy you met at the store! and I wanted to know if your fridge was… Uh…"
    if persistent.streamermode == True:
        n "Are you serious, [ch_angel]?"
    else:
        n "What the literal fuck, [ch_angel]."
    ocall "Oh? …Ohhhh! It's you!"
    ocall "Hmph. You've got some nerve calling me after what you said the other day!"
    y "…Sorry? What I said?"
    ocall "Don't act like you forgot! Well, in case you didn't get the memo, I'm not interested in you anymore! I've moved on!"
    ocall "I bet you wished you called me earlier, huh? Well, it's too late!"
    y "Wait, what?"
    ocall "You see, I'm actually interested in… someone else now! Y-Yeah, that's right! You're sooo old news now!"
    ocall "Do you want to know who it is? I bet you're curious."
    y "Honestly? Not really. Look [ch_olivia], I'm not actually the guy you met, I'm—"
    ocall "—I'm actually interested in the person you were with the other day! That's right, I said it!"
    ocall "I'm sure [they] would've treated me much more nicely! Hmph, I bet you {i}wished{/i} you accepted my offer now, huh?"
    y"The other person? You mean… [ch_angel]?"
    if player == "Olivia":
        ocall "{i}That's{/i} [their] name? Really? …Wait, we have the same name?"
    else:
        ocall "Is that [their] name? Then yeah, sure! [ch_angel]!"
    n "[shit!c], I didn't mean to reveal that."
    y "A-Actually, no! That's not [their] name! And [ch_angel] isn't interested in you either, so don't bother!"
    ocall "What?!"
    y "You know what? I think I got the wrong number! G-Goodbye!"
    ocall "WHAT?! Hang on—" with vpunch
    n "I can hear the faintest sounds of Olivia's shouting from down the hallway."
    n "Without a second thought, I tap the red button and sit in stunned silence. It was {b}truly{/b} a humbling experience after… whatever that was… and I vow to never do something as stupid as that again."
    n "Ugh. I rake my hands down my face and will the embarrassment away. Figuring it would be better to take my mind off of it entirely, I decide to put my focus in something else instead."
    jump day3_rencanonevent

################################################################################
## INVITING KIARA OVER
################################################################################
label day3_invitekiara:
    y "Um… Hello? Is this [ch_kiara]? It's [ch_angel]."
    kcall "Oh! Hello darling! Rather late for a evening chat, don't you think?"
    n "I can sense the faintest hint of humour in her tone, so I try my best to match it."
    y "Sorry, I just wanted to thank you for giving me your number — and give you mine in return."
    kcall "I see… Well then! In that case, I'll be sure to save it."
    n "I can hear the soft sounds of a pencil scratching against paper in the background, so I can only assume that [ch_kiara] was currently working on some designs for her job."
    kcall "Actually, now that I've got you here… I wanted to thank you."
    y "Thank me? For what?"
    kcall "For taking care of my little Norie, of course!"
    kcall "I'm sure you've noticed, but they're not the best at leaving her comfort zone to indulge in some fun."
    kcall "She's always been more of a homebody, but I can tell that she enjoys being around you."
    y "Oh…"
    kcall "She talks about you too, you know? In fact, a little {i}yellow{/i} birdie told me that she once had a crush on—"
    kcall "{size=-6}Ah! N-Norie! When did you come in?{/size}"
    n "I can hear shuffling on the other end of the line before [ch_kiara]'s voice returns."
    kcall "Ahh~ Looks like I got tad bit {i}too{/i} ambitious. We'll have to chat another time, won't we?"
    y "Oh, uh— Yeah! For sure!"
    kcall "In that case, make sure to have some juicy stories ready for me next time! Toodles, darling!"
    n "…Toodles? That sounded an awful lot like [ch_violet]. But before I have the chance to reply, [ch_kiara] has already ended the call."
    n "Well then. That was definitely something."
    jump day3_rencanonevent

################################################################################
## REN LEAVE ANGEL ALONE CHALLENGE (gone wrong) (impossible)
################################################################################
label day3_rencanonevent:
    if d3_inviteover == True:
        scene angel_lounge_night
        show peffectp
        play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
        with Fade(1.0, 2.0, 1.0)
        play audio "audio/sfx/door.ogg"
        n "Shutting the door behind me, I flick off the light and tiredly trudge around my apartment as if my body were on autopilot."
    else:
        n "Figuring I had nothing else left to do for the night, I decide it's {b}finally{/b} time to satisfy the cravings of my stomach."
        n "Without wasting any more time, I get up and tiredly trudge around my apartment as if my body were on autopilot."

    n "But just as I'm about to enter the kitchen, my phone rings once more."
    n "Glancing down, I notice [ch_ren]'s contact details flash on the screen."
    n "Did he… Did he want to talk?"
    n "Admittedly, I {b}was{/b} a bit curious to see [ch_ren] again after missing him in the manga store earlier."
    n "A beat passes, and before I can stop myself, I answer his call."
    n "His soothing voice greets me, and I can practically {b}feel{/b} the excitement and moe flowers expel from the screen and hit me in the face."
    n "And before I know it, [ch_ren] is agreeing to come over as soon as he can — so I quickly turn the lights back on, clean the place up a bit, and anticipate his arrival."
    jump day3_inviteren

################################################################################
## ALONE SCENE OHHH NOOOO
################################################################################
label day3_homealone:
    scene angel_bedroom_night
    show peffectp
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)

    n "Once home, I waste no time in shrugging out of my work clothes, preparing something to eat, and getting ready for bed."
    n "The newest chapter for \"Always With You\" would be out soon, and I was interested to see what would happen between the main character and [their] love interest next."
    n "Of course, no one could ever replace my beloved Haruko — but he was slowly starting to climb his way up my list."
    n "Unlike some of the other mainstream love interests, he treated the MC with so much respect and adoration — and seeing their strong bond somehow filled an unknown, empty gap in my heart."
    n "Perhaps it was no more than wishful thinking, but I've always longed to have a deep connection like that with someone."
    n "Yet, in all my years of living, I've never actually found anything remotely close to it. Let alone in the city {b}or{/b} in Corland Bay."
    n "I couldn't help but let out a heavy sigh at that — before realising just how silly I was acting — and replacing it with a scoff instead."
    y "Well, whatever. At least I still have my fictional crushes."
    n "But just as I'm about to pull out my phone and check if the latest chapter is out, [ch_leon]'s name illuminates the screen."
    n "And almost like second nature, my finger taps the answer button without so much as a second thought."
    n "His warm voice and the ocean immediately greet me, and I find myself wondering why he's still on the beach at this hour."
    n "Probably starting to pack up after a day of volleyball with a few of his friends, no doubt…"
    lcall "Heyo [ch_angel]! You're not busy right now, are you? I know it's kinda late."
    y "…[ch_leon]? Hey! Not at all. I was just getting settled into bed. What's up?"
    lcall "So Uhh… I met up with [ch_jae] and [ch_teo] today! He was going on about this little get-together he had planned for tomorrow."
    lcall "Err, y'know, the one involving your co-worker…?"
    n "Ohhh boy. Here we go."
    lcall "Well, he told me that you didn't feel like tagging along. And…"
    n "[ch_leon] seems to trail off after that, and I can almost hear the gears turning inside his head as he tries to think of what to say."
    lcall "Actually… Can I be real honest with ya for a sec? I actually called to see if you'd consider changing your mind."
    lcall "You see… something big came up with [ch_jae], so he can't make it tomorrow."
    lcall "I don't really wanna cancel on [ch_teo] either, but I figured it'd be awkward if it's just me tagging along on his supposed \"date\" with [ch_elanor]."
    n "I could definitely understand where [ch_leon] was coming from. I mean, just mere hours ago, I found myself in the exact same predicament."
    n "I honestly didn't see the point in tagging along — especially if the date had nothing to do with me — but leaving [ch_elanor] alone with [ch_teo] would've definitely made things awkward {b}for sure.{/b}"
    n "But before I can dwell on it any further, [ch_leon]'s voice pulls me from my thoughts."
    lcall "So I was thinking… If El and [ch_teo] end up hitting it off, maybe {i}we{/i} could sneak off and go to the beach instead?"
    lcall "It's not like we'd be needed after that. And besides! I still owe ya something from our favourite ice cream stand, remember?"
    n "I couldn't help but laugh at that."
    y "Oh, please! That promise was from years ago! I honestly thought you'd forget all about it by now."
    lcall "Hahaha, no way! A promise is still a promise!"
    lcall "If you let me copy your math homework, I'd buy you your favourite ice cream in return!"
    y "Bet you didn't think the ice cream stand would close for a week, huh?"
    lcall "Pffft— {i}Or{/i} the fact that I'd be somewhere overseas a week after that!"
    lcall "Alas, mini-me didn't have the ability to predict the future, [ch_angel]… {i}Yet!{/i}"
    y "Someone had to humble you."
    lcall "Awww, c'mon, I was barely ten years old! Who's gonna humble a kid?"
    n "[ch_leon]'s laughter fills the silence, and I can't help but think back to the all-too-familiar ice cream stand on the pier."
    n "One dairy-creamed thought soon leads to another, and the next thing I know, I'm thinking about the date I shared with [ch_ren]."
    n "…Would he like ice cream? What flavour would he choose? …And after what happened yesterday, would he even go back the pier in the first place?"
    n "My thoughts only spiral after that, and I find myself wondering if I'd have the chance to run into him tomorrow."
    n "After all, Corland Bay isn't that big of a coastal town, so it wouldn't be strange for us to run into each other again sooner or later."
    n "I mean, I literally met [ch_ren] at my own workplace because we shared a few common interests in books. {b}His{/b} just so happened to be about native flora."
    n "That kind of stuff wasn't something either of us could control, and I was most likely looking too deep into it. Still…"

    if d2_visitren == True:
        n "I barely had the opportunity to see him {i}at all{/i} today."
    else:
        n "I hadn't had the opportunity to see him {i}at all{/i} today."

    n "In all honesty… I was starting to miss him. In fact, it was almost as if I was beginning to have pink-haired enigma withdrawals or something. Jeez."
    lcall "—[ch_angel]? Still with me?"
    n "[shit!c]. I was spacing out on [ch_leon] again."
    y "S-Sorry! What did you say?"
    lcall "Haha, boring you to death with all my yarning, am I? Don't worry; I'll let ya get some rest after this."
    lcall "I just wanted to know if you'd reconsider."
    lcall "I promise I won't let [ch_teo] ruin our day tomorrow. 'Sides, it'd be good to catch up again, yeah? Just like old times."
    n "…Should I?"

    $ choice_style = "box"
    menu:
        #with dissolve
        "{glitch=10.0}{b}Accept [ch_leon]'s offer{/b}{/glitch}":
            $ choice_style = "default"
            $ ren_decay += 1
            $ affection_ren += 10
            play audio "audio/sfx/glitch.ogg"
            show gwitch
            n "Odd… Perhaps it was because there was a slim chance to run into [ch_ren] again, but I find myself agreeing after all."
            hide gwitch
            n "Besides, it no longer felt like [ch_teo]'s request — but rather — {b}[ch_leon]'s{/b} request. And unlike that musclehead, I had no problems with my childhood friend."
            n "I felt better knowing that [ch_leon] would be tagging along with me tomorrow — and who knows? Maybe even [ch_ren] might make another one of his appearances. I certainly hoped so."
            n "Siiiigh. I was starting to feel a bit embarrassing with how much I'd been thinking about him lately. He really did take up a lot of my thoughts, didn't he?"
            n "With that pink-haired enigma in mind; I confirm my plans for tomorrow with [ch_leon], before saying goodnight and ending the call."
            n "…"
            n "I wonder what tomorrow will bring?"
            jump day3_ending_good
        "[de_o]Decline [ch_leon]'s offer[de_c]":
            $ choice_style = "default"
            y "Ah. Sorry, but I {i}reeeeeally{/i} don't think I can stomach being around that muscled-headed idiot."
            lcall "Yeah, nah! I get it! Don't worry Sunfish, you don't have to force yourself."
            lcall "And there's no need to apologise either. If you don't wanna go, then you don't have to go. I'll have fun in your steed!"
            n "What did I do to deserve someone as considerate as [ch_leon] in my life?"
            y "…Thanks, Leo."
            y "Make sure to send me updates, yeah? I can't exactly tolerate [ch_teo], but I can tolerate you and [ch_elanor] just fine."
            lcall "Haha, you got it! Undercover cop [ch_leon] Davis, reporting in!"
            lcall "No need to worry; your updates will be hand-written with love and {i}personally{/i} sent to your address every…"
            extend " five…"
            extend " minutes."
            n "I couldn't stop the laugh that came out at his usual dramatics."
            lcall "The second I see them so much as hold hands, I'll be sure to snap a pic so we can use it as like… blackmail, or something."
            lcall "I mean, {i}surely{/i} there's someone out there who'd pay big amounts of money for that kind of stuff, right?"
            y "Gasp… Not {i}the{/i} world-renowned [ch_leon] Davis using his own friend as blackmail!"
            lcall "He's trul{glitch=10.0}y gone corrupt… Ca{/glitch}n I get a m{glitch=6.0}oment of si{/glitch}lence for—"
            n "[ch_leon]'s voice abruptly cuts in and out, so I thumb the volume button to try and hear him better."
            y "Uh… Come again? Your sentence got cut off."
            lcall "Huh? Oh! I s{glitch=10.0}aid, \"can I g{/glitch}et\"—"
            y "Hello? [ch_leon]? I think you're breaking up."
            lcall "Are we b{glitch=5}{size=30}reaking up? But I tho{/size}{/glitch}ught we were{glitch=10.0} gonna be p{/glitch}artners in crime un{glitch=8.0}til the da{/glitch}y we—"
            lcall "…Wait, is th{glitch=10.0}is still a bit? Or ca{/glitch}n you really not h{glitch=5.0}ear me? Cuz I can{/glitch} hear you{glitch=10.0} just fine,{/glitch} [ch_angel]—"
            lcall "Oh, ac{glitch=6.0}tually— Yo{/glitch}u {i}do{/i} sound kinda di{glitch=9.0}storted now,{/glitch} an—"
            n "Pressing the phone closer to my ear, I try and make out [ch_leon]'s words. Except nothing but static and white noise greets me."
            n "…Did the call cut out?"
            
            play audio "audio/sfx/static.ogg"
            stop music fadeout 1
            
            n "Too preoccupied with\ \ \ \ \ \ examining\ \ \ \ {color=#a30b11}{size=-6}01110111{/size}{/color}\ \ \ \ \ \ \ my phone, I hardly\ \ \ \ \ \ {color=#a30b11}{size=-6}01101000{/size}{/color}\ \ \ make out the\ \ \ \ {color=#a30b11}{size=-6}01111001{/size}{/color}\ \ \ sound of my\ \ \ \ \ \ \ \ window\ \ \ \ sliding open…\ \ \ \ {color=#a30b11}{size=-6}00111111{/size}{/color}"
            jump day3_deadend

################################################################################
## ENDING SCENE YEHAWWWW
################################################################################
label day3_dayend:
    scene angel_bedroom_night
    show peffectp
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/night.ogg" fadein 1 fadeout 1
    with GlitchDissolve

    n "Once I had nothing else left to do for the night, I get changed into some comfy pyjamas and brush my teeth before settling into bed."
    n "The newest chapter for \"Always With You\" was going to drop in a few hours, and I figured I might as well stay up and read it before going to sleep."
    n "But my eyes were starting to get droopy, and all my mind could think about was the \"double date\" I had planned with [ch_leon], [ch_teo], and [ch_elanor] tomorrow."
    n "Man, I sure hope everything will be fine."
    play audio ["audio/sfx/item.ogg", "<silence .3>", "audio/sfx/item.ogg", "<silence .5>", "audio/sfx/item.ogg"]
    n "But I know worrying about it wasn't going to do me any favours, so I let my pent-up stress out on my pillow by smacking it to make it less lumpy."
    n "Though the moment I unceremoniously flop back down, I notice the cold draft — and the fact that my bedroom window was left wide open."
    n "Strange. I don't remember opening it earlier…"
    n "With a groan, I get up from my bed and to go and close it. But once I lock it shut, something moves from within the shadows and startles me."
    n "Squinting, I can barely make out the black mass moving through the gaps in the fire escape balcony."
    stop music fadeout 1
    n "…What was that? A person?"
    n "It certainly wouldn't be strange for someone to take a cigarette break at this hour… But I couldn't smell any telltale signs of smoke."
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    n "Maybe it was my landlord's cat out for a leisurely midnight stroll? That idea seemed more realistic in my mind."
    n "Yet despite my futile attempts at calming myself down, I still somehow find the willpower to go back to bed rather than opening the window once more and taking another curious peek outside."
    n "I didn't have a death wish, nor did I have the stupidity of those cliché, horror film characters."
    n "But before I turn away, I double check to make sure that the window is locked shut and the blinds are fully closed. I wasn't about to risk it."
    n "Happy with the precautions put in place, I make a hasty dive towards the warmth and safety of my bed."
    n "Snuggled deep within my blankets, I find it harder and harder to think about someone breaking in — and even more so with keeping my eyes open."
    n "Before I knew it, pink-coloured sheep slowly filled my mind as I drifted away."
    
    jump day3_ending_good

################################################################################
## EEUUUGHGHGUEGHEUSGH
################################################################################
label day3_ending_good:
    $ ending_good = "obtained"
    $ persistent.d3_ending_gooding = True
    jump pathpoint

label day3_deadend:
    $ persistent.deadendings += 1
    $ persistent.deadend3 = True
    $ persistent.d3_badending = True
    jump pathpoint