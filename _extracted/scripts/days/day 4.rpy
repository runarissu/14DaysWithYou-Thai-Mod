################################################################################
## DAY 4!!!
################################################################################
label day4:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Currently playing Day 4',
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
    $ calendar_day = "04"
    $ skipday = "day5"

    $ update_ren = "ahhh you make me so happy!!! >_<"
    $ update_moth = "NO BC WHY ARE PLANES SO SCARY???? we should cancel all airlines immediately"
    $ update_violet = "I feel like it's going to rain soon..."
    $ update_elanor = "Good morning everyone! Let's make today another wonderful day!"
    $ update_conan = "I think, therefore I am."
    $ update_jae = "looking for a man to send me money"
    $ update_leon = f"@{username_angel} dont sleep in :P"
    $ update_teo = "anyone wanna keep me company later?"
    $ update_olivia = f"ME ME?ME, ME @{username_teo} ME,..ME ME MEMEM ME,ME HELLO ME @{username_teo}".upper()
    $ update_kiara = "Loving the scenery in #CorlandBay! I'm feeling super inspired right now! x"

    $ location_moth = "home"
    $ location_violet = "home"
    $ location_elanor = "home"
    $ location_ren = "home"
    $ location_conan = "home"
    $ location_jae = "home"
    $ location_leon = "home"
    $ location_teo = "home"
    $ location_olivia = "home"
    $ location_kiara = "home"

    call girlmath from _call_girlmath

################################################################################
## WAKEY WAKEY
################################################################################
label day4_morning:
    scene angel_bedroom_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 2.0, 1.0)

    n "Rainbow bandages. A red tunnel. Blue eyes. That's all I can seem to recall from my dream as the blaring {b}bzzt, bzzt, bzzt!{/b} of my alarm pulls me from my slumber."
    n "Almost groggily, I reach for my phone to turn it off and flop back into my bed. Curious, I glance at the screen to check the time — only to get blinded by the brightness of my wallpaper."
    y "Ugh…"
    n "Wincing at the bright screen that practically flashbangs me, I crack open one eye to read the numbers on the screen."
    n "{b}9:05AM.{/b} Ah, so it wasn't too early, then."
    n "I still had plenty of time to get ready for the day and possibly make some waffles for breakfast. The batter would expire soon anyway, and I didn't really feel like visiting the bakery this morning."
    n "With that plan in mind, I let out a sleepy groan and roll out of bed."

    if d3_wahooren:
        call DLC_day4_s1 from _call_DLC_day4_s1
    else:
        n "Muscle memory kicks in, and my immediate reaction is to open the blinds for some much-needed sunshine — but when I glance at my windows, they were already pulled back."
        n "…Sunlight had been pouring into my room for who knows how long, and I didn't even notice? And when did I open them? I swear I closed the blinds last night."
        n "In fact, I was confident I did — because there was {b}no way{/b} I'd be getting any sleep after finding out a potential stalker was creeping outside my window."
        n "Don't tell me someone broke in again…"
        n "I try not to focus on the twang of dread slowly building up inside the pit of my stomach. I wasn't about to get worked up again, and so early in the morning, too."

    n "Ugh. This was not what I needed to start my day with."
    n "Deciding not to dwell on it for now, I stand up and gradually work out the kinks in my body. No way was I going to let this ruin the outing I had planned with [ch_teo], [ch_elanor], and [ch_leon]."
    y "Oh, yeah. I almost forgot… We were supposed to go to the aquarium today."
    n "With that in mind, I make a mental note to dress appropriately as I walk over to my closet. Absentmindedly, I run my fingers across some of my clothes before pulling something [favourite_outfit] from the rack."
    n "My usual style has never let me down before, so I decide to stick with the theme and wear something similar. I pick out a few more matching pieces and accessories before giving them all a cursory glance."
    n "Feeling satisfied with the items I chose, I nod in approval before heading to the bathroom to change."

    scene angel_bathroom_day
    show peffect
    stop ambience fadeout 2.0
    play audio "audio/sfx/movement.ogg"
    with dissolve

    n "I doubt the hot water would work this early in the morning, so having a nice, refreshing shower was {b}definitely{/b} out of the question."
    n "Well, not that it really mattered. I still needed to buy some more shampoo anyway, and—"
    extend " Oh?"
    y "Strange…"
    n "Was my toothbrush holder always this solid black colour? I could've sworn it was grey…"
    n "Picking it up from the shelf, I give it a once-over. The Haruko print was still there, yet it somehow felt… heavier in my hands?"
    n "But then again, I don't exactly go around meticulously measuring how heavy my items are in the first place."
    n "Jeez, today was seriously a day of overthinking, huh? Well, whatever."
    n "Putting the holder back on the shelf, I focus my attention back on the reflection of myself in the mirror and give an appreciative nod."
    if hair_length == "bald":
        n "The outfit I chose looks perfect, and all I have left to decide on is how to style the finishing touches."
    else:
        n "The outfit I chose looks perfect, and once I put everything on, all I'd have left to decide on is how I should style my hair."
    if custom_angel == False:
        y "Hm… What should I do?"
        menu:
            "My hair is short":
                $ hair_length = "short"
                pass
            "My hair is mid-length":
                $ hair_length = "mid-length"
                pass
            "My hair is long":
                $ hair_length = "long"
                pass
            "I don't have hair":
                $ hair_length = "bald"
                jump day4_morningcont
        menu:
            "I also have straight hair":
                $ hair_texture = "straight"
                pass
            "I also have wavy hair":
                $ hair_texture = "wavy"
                pass
            "I also have curly hair":
                $ hair_texture = "curly"
                pass
            "I also have coily hair":
                $ hair_texture = "coily"
                pass
            "I also have braided hair":
                $ hair_texture = "braided"
                pass
            "I also have locs":
                $ hair_texture = "locs"
                pass
    elif hair_length != "bald" or hair_length != "hidden":
        n "Absentmindedly brushing a hand through my [hair_length], [hair_colour] hair, I try to come up with something that'll look good."
    else:
        pass

    label day4_morningcont:
    n "An idea comes to mind, and I immediately set to work."
    
    scene angel_lounge_day
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve
    if hair_length == "bald":
        n "An hour flies by, and I've somehow managed to change into my outfit and finish breakfast in record time."
    else:
        n "An hour flies by, and I've somehow managed to get dressed, style my hair, and finish breakfast in record time."
    n "With nothing else left to do, I decide I might as well kill time in my entryway by picking out which shoes to wear."
    n "But just as I stop in front of the shoe rack, something near the front door catches my eye."
    y "…A letter?"
    n "Odd. My door doesn't have a letterbox, so I usually have to visit the front desk to collect my mail — that is, if [ch_violet] doesn't bring it up for me."
    n "So what was this doing here?"
    play audio "audio/sfx/slide.ogg"
    n "Curiosity gets the better of me, and I find myself scooping up the letter and opening it. Inside was nothing more than a folded note written in red ink, and—"
    play ambience "audio/ambience/heartbeat.ogg" fadein 1 fadeout 1
    stop music fadeout 1

    if li_name == "Moth":
        n "Was that a photo of Moth?"
        y "…What the?"
    else:
        n "Was that a lock of [li_hair] hair?"
        y "…What the?"
        n "Did this… belong to [li_name]?"
    play audio "audio/sfx/paper.ogg"
    n "A chill runs down my spine once I realise what {b}exactly{/b} this item is, and I hesitantly scan the rest of the note for answers. It simply read:"
    if li_name == "Moth":
        npc "Not bad for a candid shot, huh? And don't bother warning them about this. I'll know."
    else:
        npc "I think [li_they] might need a new lock as well, don't you think? And don't bother warning [li_them] about this. I'll know."
    npc "Let's keep this between us, alright? It'll be our little secret."

    n "…What the hell? Was this somehow tied to that [asshole] who broke into my apartment a few days ago? Or was it someone else entirely?"
    stop ambience fadeout 2.0
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    n "Though admittedly, whoever this… {b}stalker{/b} was, they were honestly doing a pretty bad job at making their intentions clear. I mean, what exactly were they trying to accomplish by doing this?"
    n "Did they want me to stay away from [li_name] as well? Or just keep silent? What did they get out of blackmailing me like this? And why target [li_name] specifically? None of this made any sense."
    n "And now that I give it more thought, I still wasn't sure what they wanted from {b}me{/b}, either. Why go through all this trouble in the first place? It wasn't like I was doing anything wrong."
    y "Maybe moving back to the Bay wasn't a good idea after all…"
    n "I mean, I left the hardships and turmoil of the city behind for a reason."
    n "I wanted fresh air, new faces, and a more easygoing lifestyle — things I'd {b}never{/b} get in the city — and now it seems like history is only repeating itself once more."
    n "I thought I could live a peaceful life here with my new job and friends… And now I've somehow found myself in more trouble than I could ever ask for."
    n "And what's worse is that after denying my own paranoia for so long, {b}this{/b} was all it took to convince me that my potential intruder {b}really was{/b} real after all. [shit!c], maybe [ch_violet] was right."
    n "I remember brushing off her concerns because the idea of a stalker seemed so far-fetched to me — especially given Corland Bay's innocuous reputation — but now…? Ugh."

    if li_name == "[ch_violet]":
        n "Admittedly, a big part of me wanted to knock on [ch_violet]'s door and see if she was safe, but another part kept me rooted in place."
        n "…What my newfound stalker finds out? Or what if they were still lurking about outside after dropping off that letter—"
    elif li_name == "[ch_olivia]":
        n "And as awkward as our first encounter was, part of me still wanted to check in on [ch_olivia]; but another part kept me rooted in place. What if my stalker finds out? What if they were still lurking outside—"
    else:
        n "Admittedly, a big part of me wanted to see if [ch_violet] was still home, but another part kept me rooted in place. Would it be safe? What if the intruder was still lurking outside—"

    play audio "audio/sfx/vibrate.ogg"

    n "*{i}bzzt bzzt!{/i}*" with hpunch
    y "Ack!"
    n "Suddenly, my phone goes off and scares the living daylights out of me — so much so that I end up dropping it on the hardwood floor and clambering to pick it back up in a panic."
    y "[shit!c]! [shit!c], [shit], [shit]!"
    n "With shaking hands, I forgo looking for any dents and cracks in the screen as I try to discern the reason for the noise instead."
    n "The letter \"T\" shows up where the caller ID should be, alongside a suggestive contact photo of someone's abs that I don't remember taking — which could only mean one thing…"
    n "[ch_teo] was calling."
    n "It takes a few failed attempts, but I somehow manage to press the answer button and respond with a shaky tone."
    y "Um… H-Hello?"
    tcall "Well [damn], Doll. You sound like you just woke up. Not planning on sleeping in, are you?"

    if li_name == "[ch_teo]":
        n "Even if it {b}was{/b} just to tease me, hearing [ch_teo]'s smug voice honestly brought me a sense of comfort. It meant that he was safe after all, and I couldn't help but let out a sigh of relief at the thought."
        tcall "Aw, what? Did I take your breath away? That's real cute."
        n "Ugh. I take it all back."
        n "Still… Was it really okay for me to talk to him like this? Now that I think about it, I'd also have to spend the entire day with [ch_teo] as well."
        n "I guess it would be fine? It's not like the note told me otherwise."
        n "Heh, I suppose it's my stalker's fault for not being more thorough with their passive-aggressive letter for me. Maaaybe if they were more—"
        n "Ugh, no. What was I thinking? And where did this sudden burst of foolhardiness come from? I have to start taking this seriously, otherwise—"
        tcall "[damn!c], still speechless? Don't tell me you fell asleep after all."
    else:
        pass
    y "What? No, I—"
    tcall "Good. 'Cuz I'm outside your apartment right now."
    tcall "Your neighbourhood looks like [shit], by the way. Smells like it, too."
    y "Did you seriously call me just to make fun of where I live?"
    tcall "I called to tell you to hurry up. Unless you want to {i}walk{/i} to the aquarium. In fact, maybe I should just—"
    extend " Ah, [dammit]."
    tcall "{size=-6}Well, well, well. If it isn't little Miss Priss all by her lonesome—{/size} Oops, she looks mad."
    n "[ch_teo]'s voice practically oozes smugness as he taunts whoever it is he's talking to (most likely [ch_violet]), before I hear him adjust the phone and continue speaking."
    tcall "Oi, Dollface, hurry up, won't you?"
    n "He hangs up before I can mutter out a response."

    if li_name == "[ch_violet]":
        n "But did that mean… Was he talking about [ch_violet]? Was she safe?"
        n "Relief washes over me, and I never thought I'd be happy to hear {b}[ch_teo]{/b} talking about my neighbour, even if it were in an antagonistic manner. It meant that she really was safe after all, and I couldn't help but let out a sigh of relief at the thought."
        n "Still… Was it really okay for me to be going out in public like this? Now that I think about it, I'd eventually have to run into [ch_violet] again at some point."
        n "I guess it would be fine? It's not like the note told me otherwise."
        n "Heh, I suppose it's my stalker's fault for not being more thorough with their passive-aggressive letter for me. Maaaybe if they were more—"
        n "Ugh, no. What was I thinking? And where did this sudden burst of foolhardiness come from? I have to start taking this seriously, otherwise—"
        n "The faint sounds of a car horn pull me from my thoughts, and I'm reminded of the tall, green-haired annoyance I'm supposed to be hanging out with today."
        y "Ah, I shouldn't keep [ch_teo] waiting."
    else:
        pass
    n "But still… Knowing that [ch_teo] was downstairs {b}somehow{/b} gives me the confidence to leave the safety of my home — though not before committing the state of my apartment to memory and triple-checking my lock."
    n "I have half a mind to quickly snap photos of everything to see if anything was touched in my absence, but I doubt I'd have enough time. Still… If my stalker {b}does{/b} decide to come back again, I'd want to know."
    n "But now that I'm thinking about photos… this gives me the perfect opportunity to splurge on some security cameras. I'd been needing them for quite some time now, anyway."
    n "With all this talk of violent crimes, dead bodies, and murder happening on the news lately (and now this intruder), I figure it'd be better to be safe than sorry."
    n "So, deciding to let [ch_teo] suffer — even just a little bit — at the hands of [ch_violet], I pull out my phone to scroll through some home security bundles on sale as I make my way towards the lobby."

################################################################################
## LEON SCENE
################################################################################
label day4_leonarrival:
    scene other_dark
    play music "audio/bgm/Childhood Friend.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/movement.ogg"
    play audio ["<silence 1.8>", "audio/sfx/ignition.ogg"]
    play ambience "audio/ambience/driving.ogg" fadein 2.5 fadeout 1
    show peffect
    with GlitchDissolve

    $ location_moth = "home"
    $ location_violet = "work"
    $ location_elanor = "home"
    $ location_ren = "oh"
    $ location_conan = "work"
    $ location_jae = "city"
    $ location_leon = "aquarium"
    $ location_teo = "aquarium"
    $ location_olivia = "pier"
    $ location_kiara = "random"

    n "[ch_teo] ended up being uncharacteristically quiet throughout the drive, and if I were being honest, I appreciated the silence."
    n "It was definitely odd not having our typical playful banter, but it also wasn't something I needed first thing in the morning."
    n "He also doesn't seem in the mood to be disturbed, given how he clenches the wheel with one hand while the other supports his head against the window ledge like some angsty teen."
    n "So, I try to settle further into the (admittedly comfy) seat of his luxury car and focus my attention on the scenery as it passes by."

    n "It isn't long before the aquarium comes into view as [ch_teo] looks around for a decent place to park."
    n "We must've picked a busy day to visit, considering the amount of cars parked both outside {b}and{/b} in the reserved parking area — though [ch_teo] seemed to have somewhere in mind."
    y "Uhh…"
    n "I watch as he drives straight past a {b}very clearly{/b} labelled \"no go\" zone and pulls up into one of the empty spaces without so much as a reaction."
    scene beach_carpark_day
    show peffect
    stop ambience fadeout 2.0
    with GlitchDissolve
    n "He doesn't even wait for me to get out before he opens his door and walks to the front of the car — and not wanting to be left behind, I quickly follow suit."
    y "[ch_teo]?"
    n "I was about to question whether he was {b}allowed{/b} to park in the employee zone in the first place, but given how he shamelessly pulls down one of the warning signs and tosses it into a bush, I figured that was my answer."
    n "It doesn't take long before he's right by my side once more and ushers me towards the front entrance."
    
    scene beach_street_day
    show peffect
    play audio "audio/sfx/movement.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    with GlitchDissolve
    
    n "I almost stumble over my feet as [ch_teo] pulls me along — but not before almost bowling him over as he abruptly stops in front of me."
    play audio "audio/sfx/item.ogg"
    show teo smirk at spop, center with dissolve
    t "Heh. Look at that. Almost like a loyal dog, isn't he?"
    n "Glancing in the direction he was pointing, I see [ch_leon] sitting on one of the benches as he absentmindedly watches people go by."
    n "And once he catches sight of us, he immediately leaps to his feet and rushes over with a wave and a warm smile."

    if li_name == "[ch_leon]":
        n "Relief washes over me as I take in his relaxed and carefree disposition, and I never thought I'd be {b}happy{/b} to hear [ch_teo] casually tease my friend with our usual, playful banter."
        n "But… Seeing [ch_leon]… It meant that he really was safe after all, and I couldn't help but let out a sigh of relief at the thought."
        n "Still… Was it really okay for me to be out in public like this? Now that I think about it, I'd be spending the entire day with my childhood friend as well."
        n "I guess it would be fine? It's not like the note told me otherwise."
        n "Heh, I suppose it's my stalker's fault for not being more thorough with their passive-aggressive letter for me. Maaaybe if they were more—"
        n "Ugh, no. What was I thinking? And where did this sudden burst of foolhardiness come from? I have to start taking this seriously, otherwise—"
        show teo neutral at spop
        t "It's a good thing he doesn't bite."
        n "[ch_teo]'s voice pulls me from my thoughts, and I send him a playful eye roll in response. I doubt he takes any notice of it, though, since [ch_leon]'s arrival takes up all of our attention."
    else:
        show teo neutral at spop
        t "It's a good thing he doesn't bite."
        n "At that snarky comment, I nudge [ch_teo] with my elbow and send him an eye roll. I doubt he takes any notice of it, though, since [ch_leon]'s arrival takes up all of our attention."

    play audio "audio/sfx/shoes alt.ogg"
    play audio "audio/sfx/sprinting.ogg"
    show teo smirk at tleft with easeinright
    show leon happy at tright with dissolve

    show leon happy at bpop
    l "Heyo! You look good, Sunfish!"
    y "You're not so bad yourself, {i}oarfish.{/i}"
    show teo frown at spop
    t "…Hello? I'm here too."
    y "[ch_elanor] hasn't arrived yet?"
    n "Scoffing at our playful dismissal, [ch_teo] cracks a joint in his neck and crosses his tattooed arms. However, he doesn't seem to stray from his spot, which meant that he still had an interest in our conversation."
    n "At his almost childlike reaction, [ch_leon] shoots his friend a cheeky, lopsided smile before continuing."
    show leon neutral at spop
    l "I'm sure she's on her way. She said something about \"wanting to get her steps in\" in our group chat. Is that why she didn't want [ch_teo] picking her up?"
    show leon smirk at spop
    l "And actually… I dunno if you realised, but you guys were fifteen minutes early."
    y "Really? Pfft— No thanks to [ch_teo]'s speeding, I guess."
    y "And what about you? I'm guessing you had to walk all the way here, right?"
    show leon happy at spop
    l "Haha! There's nothing wrong with getting a bit of exercise in the morning! I'm sure [ch_elanor] would agree."
    show leon smirk at spop
    l "And I just got here, actually."
    show teo smirk at spop
    t "Really? 'Cuz it looked like you were sitting on that bench for a while."
    show leon blushing at spop
    l "I-I just sat down."
    y "Long enough to stretch your legs, huh?"
    show leon flushed at spop
    l "…Okay, yeah. So {i}maaaybe{/i} I {i}did{/i} arrive half an hour early."
    show leon happy at spop
    l "But I was excited! It's been a while since I've been to the aquarium."
    show teo neutral at spop
    t "Even {i}longer{/i} since you've seen Dollface over here, I bet."
    y "Huh?"
    show leon happy at spop
    l "Can ya blame me? We've been separated for {i}years{/i} — now we're finally reunited again. It must be fate…"
    show leon neutral at spop
    l "No… Destiny."
    n "Playing along with [ch_leon]'s dramatics, I lean against his side and clutch at the spot above my heart."
    y "It's written in the stars."
    play audio "audio/sfx/shoes alt.ogg"
    show teo frown at ffullyleft with easeinright
    show teo frown at spop
    t "You guys are genuinely so embarrassing."
    play audio "audio/sfx/walking.ogg"
    hide teo with easeoutleft
    show leon happy at center
    with easeinright
    n "Hearing [ch_teo] huff once more, [ch_leon] and I both watch as he tries to distance himself by looking at the posters on the wall."
    n "No doubt feigning interest in it; it wasn't like [ch_teo] really cared much for marine life. All his world revolved around was wealth and luxury, giant tech companies, and… probably starting fires."
    extend " Yeah, definitely starting fires."
    n "Though… For a guy who spent most of his time in the shadow of his father's legacy, I had to hand it to him — [ch_teo] {b}was{/b} seemingly more down to earth than other people I've met."
    n "He didn't have to spend time with us, but he did. And as much as he'd often joke about not wanting to affiliate himself with people outside his tax bracket, [ch_teo] sure seemed to like hanging out with [ch_jae], [ch_leon], and me."
    n "…I wonder, does he ever feel lonely?"
    n "Before my thoughts can delve any further, I feel a gentle nudge at my side. Looking to my left, I see [ch_leon] peering at me with a curious expression."
    show leon neutral at spop
    l "Y'know, I'm really glad you came. But… I'm also honestly surprised you agreed to this."
    y "Surprised? What do you mean?"
    show leon sad at spop
    l "Uhh… Well, you know… Is [ch_ren] okay with this?"
    y "[ch_ren]?"
    show leon neutral at spop
    l "The guy we met at the pier the other day. He said something about being your boyfriend?"

    #hide leon with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "[rh_o]\"Oh, right. My boyfriend.\"[rh_c]":
            $ affection_ren += 10
            $ rem_boyfriend = True
            show leon neutral with dissolve
            n "Whether or not it was because I wanted to stake my claim over [ch_ren] — or because he confidently declared himself as my boyfriend a few days ago — I couldn't help but let it slip."
            n "But [ch_leon] seems to pick up on the hesitance laced within my words, given how he inquisitively tilts his head and sends me a reassuring smile."
            show leon smirk at spop
            l "Haha, is it still a new thing for you? I'm sure calling someone your boyfriend must take some time to get used to. Take things at your own pace."
            n "It was… strange hearing this kind of advice from [ch_leon] — especially after practically lying to him — but I wasn't going to say anything."
            n "We've been friends for so long, yet the topic of dating had never seemed to come up between us — much less something more extreme like settling down or getting married."
            n "At that, I recall a fond memory from my youth."
            n "A younger version of ourselves greets me as they innocently play a game of pretend on the playground. I can see [ch_leon] in all his boyish charm as he promises to marry me from atop the slide — before he slides down it and runs to my side in glee."
            n "He seems all too happy to run circles around me while he shouts to the skies about \"protecting me from bad guys\", yet… Something else was missing from the scene… Something I couldn't fully remember."
            n "What was it?"
            show leon happy at spop
            l "—As long as he's chill with this, yeah? I wouldn't want any misunderstandings to happen."
            n "…Great, I had been spacing out again."
            n "Not wanting to offend [ch_leon] with my silence, I try to make sense of his words before coming up with a sufficient response of my own."
            y "Oh! Uh, yeah! He's fine with it!"
            extend " …Probably."
        "\"[ch_ren] isn't my boyfriend.\"":
            $ affection_ren -= 10
            show leon neutral with dissolve
            n "Oh yeah, I still needed to talk to [ch_ren] about that and clear up any potential misunderstandings with everyone — and [ch_leon] definitely seems like a good place to start."
            n "But before I can get a word in to explain, he beats me to it."
            show leon frown at spop
            l "He's not? Then what was that all about the other day? He sure looked all cosied up with you at the pier."
            y "I'm sure [ch_ren] only said that to get [ch_teo] off my back. He didn't really mean it."
            y "And I've been meaning to talk to him about that for a while now, actually."
            show leon sad at spop
            l "I see…"

    $ choice_style = "default"
    y "Besides! I only agreed to this outing because [ch_elanor] {i}genuinely{/i} seemed like she wanted to go."
    y "A-And it's not like this is a {i}\"date\"{/i} date anyway, so—"
    show leon neutral at spop
    l "Hey, don't sweat it, [ch_angel]. And no need to explain yourself either; I get what you're saying."
    show leon happy at spop
    l "I'm sure everyth—"
    n "[ch_leon] cuts himself off when he notices something behind me — and when I turn around to look — I see [ch_elanor] running up to the group with a flushed expression on her face."
    n "But as she draws near, she clumsily trips on a stray piece of cobble and tumbles forward."
    e "Ah!" with vpunch
    play audio "audio/sfx/shoes alt.ogg"
    play audio "audio/sfx/heels alt.ogg"
    show teo frown at tleft
    show elanor blushing at ffullyleft
    with easeinleft
    play audio "audio/sfx/item.ogg"
    show leon frown at bpop with hpunch
    play audio "audio/sfx/heels alt.ogg"
    play audio "audio/sfx/running.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show leon at fright with easeinleft
    n "Without thinking, I lurch forward to close the gap between us, but [ch_teo]'s muscular arm beats me to it." with vpunch
    n "Almost effortlessly, he reaches out to catch her — almost like those cliche romance movies — except… Not at all, because [ch_teo] was allergic to anything romantic."
    n "A fact that's emphasised by the look of pure {b}disdain{/b} on his face as he pulls my co-worker to her feet."
    n "[ch_elanor] seems to be blissfully enjoying every moment of it, though, seeing as she practically clutches onto his bicep while looking up with wide, sparkling eyes."
    n "In fact, I doubt she was even aware of our presence with how she stays rooted in [ch_teo]'s awkward embrace."
    show leon smirk at spop
    l "Looks like she really {i}fell{/i} for him, huh?"
    y "Pfft—! You're as bad as [ch_jae] with those puns."
    show leon happy at spop
    l "Haha! He's rubbing off on me. C'mon, let's go see if she's okay."

################################################################################
## AQUARIUM ENTRANCE
################################################################################
label day4_aquariumscene:
    scene other_dark
    play music "audio/bgm/After The Rain.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve

    n "As it turns out, [ch_elanor] {b}really was{/b} okay… Being cradled inside the arms of [ch_teo]."
    
    if li_name == "[ch_elanor]":
        n "Relief washes over me as I take in her gleeful disposition, and I never thought I'd be {b}happy{/b} to see her safe and sound in [ch_teo]'s embrace."
        n "But… Seeing [ch_elanor] so happy… It meant that my stalker didn't do anything to her, and I couldn't help but let out a comforting sigh at the thought."
        n "Still… Was it really okay for me to be out in public like this? Now that I think about it, I'd be spending the entire day by my co-worker's side."
        n "I guess it would be fine? It's not like the note told me otherwise."
        n "Heh, I suppose it's my stalker's fault for not being more thorough with their passive-aggressive letter for me. Maaaybe if they were more—"
        n "Ugh, no. What was I thinking? And where did this sudden burst of foolhardiness come from? I have to start taking this seriously, otherwise—"
        n "I get pulled from my thoughts the moment [ch_leon] gently nudges me forward, and I follow everyone inside as we wait in line to buy admission tickets."
    else:
        n "But the moment only lasts until [ch_leon] and I rejoin the group with a knowing smile on our faces. [ch_teo] aptly chooses not to say anything, and out of solidarity — or perhaps future blackmail — neither do we."
        n "And soon enough, we all found ourselves waiting in line to buy admission tickets."
        pass

    scene store_entrance_day
    show peffect
    show elanor happy at cleft
    show teo smirk at center
    show leon neutral at cright
    with dissolve

    n "[ch_elanor] happily takes photos of us while [ch_teo] scrolls through his phone, and [ch_leon] stands beside me to look at all the colourful fish in the small tanks."
    show elanor blushing at spop
    e "This is all rather exciting, don't you think?"
    show teo neutral at spop
    t "Really? It's just fish."
    show leon sad at spop
    l "Oi, c'mon mate. Show a bit more enthusiasm, yeah?"
    show teo frown at spop
    t "…"
    show teo neutral at spop
    t "If you love 'em that much, wait 'til you find out what's at the beach."
    show leon frown at spop
    l "I want to apologise in advance for him."
    show elanor neutral at spop
    e "N-No, it's fine! I'm sure [ch_teo] has other interests that excite him. Fish just aren't particularly one of them."
    show teo smirk at spop
    t "…Wanna know what makes me excited?"
    n "[ch_leon] and I both share a look before rolling our eyes."
    show teo happy at spop
    t "Breaking tail lights and slashing tyres."
    show elanor blushing at spop
    e "O-Oh—!"
    show elanor flushed at spop
    extend " Erm, wait… Slashing tyres? Isn't that illegal?"
    show teo smirk at spop
    t "Probably."
    show elanor sad at spop
    e "…"
    show teo neutral at spop
    t "I'm just messing with you, Princess. Loosen up a little."
    play audio "audio/sfx/vibrate.ogg"
    n "All too quickly, the light-hearted mood gets replaced with something serious as [ch_leon]'s phone starts buzzing."
    n "Recognition flashes across my childhood friend's face as he looks at the screen, before he awkwardly scratches at the back of his neck and points towards the entrance with his thumb."
    show leon sad at spop
    l "Sorry guys, gimmie a sec."
    play audio "audio/sfx/walking.ogg"
    show elanor neutral at tleft
    show teo at tright
    hide leon
    with easeoutright
    n "Without waiting for a response, [ch_leon] makes a beeline for the front door."
    n "After a few seconds, I see his figure emerge from outside the large windows, pacing back and forth on the sidewalk as he talks to someone on the phone."
    n "Judging by the solemn expression on his face, I can only guess that the call isn't a good one."
    n "…I sure hope everything is alright."
    n "Too caught up in [ch_leon]'s shift in demeanour, I barely notice how [ch_elanor]'s hand gently pushes [ch_teo] and I forward so they can speak to the clerk at the front desk."
    play audio "audio/sfx/shoes alt.ogg"
    play audio ["<silence .4>", "audio/sfx/heels alt.ogg"]
    show teo at center with easeinleft
    show elanor at cleft with easeinleft
    n "Broad, tattooed shoulders now block my view from the window, which causes me to shift my attention back to the present."
    n "But [ch_teo] doesn't seem to notice my lack of focus — or perhaps he just doesn't care — as he pulls out a black card from his wallet and leans over me to hand it to the woman behind the counter."
    n "He could've gone without the nonchalant, smug look on his face, but I wasn't about to say anything when he was {b}literally{/b} about to pay for my admission fee."
    n "But before I could (begrudgingly) thank him, [ch_elanor]'s excited voice cuts me off."
    show elanor happy at spop
    e "Ooh, do you suppose there will be shows today as well? I saw some advertised outside!"
    show teo smirk at spop
    t "Oh yeah? I wasn't paying much attention to them."
    show elanor blushing at spop
    e "Hehe, I hope there'll be penguins! Perhaps [ch_leon] would enjoy them."
    show teo neutral at spop
    t "What about me?"
    show elanor sad at spop
    e "You? Hm… I don't suppose you like sharks?"
    n "I can hear the clerk chime in with information on the latest hotspots and what shows were playing, but I shut it all out when I notice [ch_leon] standing idly near the doorway — still sporting that concerned look on his face."
    hide elanor
    hide teo
    with easeoutleft
    show leon frown with easeinright
    n "Without missing a beat, I make my way over to his side and spare him an empathetic glance."
    play audio "audio/sfx/item.ogg"
    show leon frown z with dissolve
    l "Ah… I'm real sorry about all that, [ch_angel]. But something's come up involving my mum at the hospital."
    y "Oh no. Is everything okay?"
    show leon neutral z at spop
    l "Yeah nah, Mum's fine! It's just some important paperwork I need to fill out on her behalf. Y'know, since Dad is still working abroad and all."
    show leon sad z at spop
    l "I'm so sorry, but I really gotta go. I'll try to come back as soon as I'm—"
    y "Hey, don't sweat it, [ch_leon]. Focus on your mother first."
    show leon neutral z
    n "I don't miss the way his entire demeanour softens at my concern. [ch_leon] looks as though he wants to say something serious but holds himself back at the very last second."
    n "As if to compensate, I end up filling the silence instead."
    y "I'm sure I can survive third-wheeling [ch_teo] and [ch_elanor]'s date alone."
    show leon happy z at spop
    l "Jeez, I really owe ya one."
    show leon neutral z at spop
    extend " Actually? You know what? Here."
    n "Before I can refuse, [ch_leon] shoves a stack of small bills into my palm and closes his hands around it."
    y "Hey— You don't have to. Besides, [ch_teo] already paid for everything just now—"
    show leon smirk z at spop
    l "Nah, I won't be hearing anything from you!"
    show leon happy z at spop
    l "If you won't accept it, then spend it all on something for {i}me{/i} instead, yeah? Go to town in the souvenir shop!"
    show leon neutral z at spop
    l "See if they have any sunfish merch in there."
    y "…Alright. Thank you, [ch_leon]."
    show leon happy z at spop
    l "No worries, darl'. But I really gotta go now, though. I'll tell Mum you said hi!"
    play audio "audio/sfx/shoes alt.ogg"
    show leon neutral with dissolve
    n "[ch_leon] turns on his heel before I have the chance to respond, so he completely misses me waving him off."
    play audio "audio/sfx/item.ogg"
    show leon frown with vpunch
    n "In his rush, he almost knocks someone over — but he quickly helps them regain their footing and apologises before speeding off once more."
    play audio "audio/sfx/sprinting.ogg"
    hide leon with easeoutright
    y "Man, I sure hope everything is okay with his mother."
    n "But before I can dwell on it any longer, the sweet melody of [ch_elanor]'s laughter pulls me from my thoughts and I turn back towards the group."

    scene aquarium_tunnel_day
    show peffect
    play audio "audio/sfx/movement.ogg"
    play ambience "audio/ambience/underwater.ogg" fadein 1 fadeout 1
    show teo happy at center
    show elanor happy at ffullyleft
    with GlitchDissolve

    n "I notice that [ch_teo] and [ch_elanor] are now standing by the entrance — which also happened to double as a {b}massive{/b} underwater tunnel — all while pointing to a school of fish swimming over their heads."
    n "When [ch_elanor] notices my presence, she happily waves me over before her attention shifts towards the door behind me, no doubt expecting to see [ch_leon] walk back in and join us."
    n "It made sense considering how they missed his departure — but she snaps out of her curious daze the moment [ch_teo] brushes a hand against her back to move her out of the way of a family passing by."
    play audio "audio/sfx/heels alt.ogg"
    show elanor blushing at tleft with easeinleft
    n "But what truly {b}shocks{/b} me is that he doesn't seem to move his hand. Instead, [ch_teo] leaves it there as he steps closer and blocks my co-worker from my view."
    show teo neutral
    n "He meets my gaze with an intense, unreadable expression, and I can't help but look away."
    
    hide teo
    hide elanor
    with dissolve

    n "…What was that all about?"
    n "Suddenly, the moment felt too personal for my liking; almost as if I shouldn't be looking at something so intimate."
    n "Turning away, I decide to channel my interest into picking out a roadmap from the brochure stand instead. If [ch_teo] and [ch_elanor] were planning on getting cosy with each other, I needed to plan my escape route."
    n "But before I move away, I notice a lone aquarium tank off to the side."

    scene aquarium_tank_day
    show peffect
    with dissolve

    n "It was far enough from the eyes of the people still waiting in the queue, but still close enough to the entrance to entice any passers-by to come in and take a look."
    n "Inside were countless amounts of colourful fish, coral, and other sea crustaceans; and I couldn't help but look in awe of some of the bright marine life as they float about in the water."
    n "If only [ch_leon] could join us… I could almost hear his laughter at some of the sunfish-like creatures that swim by."
    n "Keeping the rest of the group in sight, I stray slightly to the right for a better vantage point."
    n "A group of neon tetra fish zip past and my eyes follow them as they swim around. They easily stand out against the bright orange and green corals; and {b}especially{/b} the pink and blue—"
    n "Wait… Pink and blue?"

    scene CG D4_AQUARIUM
    hide screen dayscalendar
    show screen menuwu
    $ quick_menu = False
    $ persistent.cg_d4_aquarium = True
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    with Fade(1.0, 1.0, 1.0)

    n "Peering closer to the glass, I catch sight of a familiar face on the other side of the tank."
    n "[ch_ren] doesn't seem to notice me yet, seemingly far too entranced by the brightly-coloured creatures as they swim by."
    n "His soft eyes follow some of the smaller fish as they dart across the tank before swapping over to the group of guppies swimming past."
    n "Suddenly, our eyes meet the moment the fish split up, and I watch as [ch_ren]'s expression morphs from surprise into a sickeningly sweet look. He tries to say something, but his words come out inaudible due to the glass separating us."
    n "As if realising, [ch_ren] {b}instead{/b} points to one of the fish off to the side before resting his hand on the glass and mouthing something else."
    n "I still can't fully understand what he was trying to say — that is, until my eyes land on what he was pointing at. Catching me off guard, I watch in awe as a lone fish swims between us and captures both of our attention."
    n "Was that… an angelfish?"
    n "The fond memory from our time at the pier comes to mind, and I find myself thinking back to when [ch_ren] affectionately gave me that nickname."
    n "And had I known any better, I would've assumed that he was thinking about the same thing — given the way his eyes crinkle and soften as the fish's scales shimmer underneath the artificial light."
    n "Too absorbed in how picturesque this all looked, I completely miss [ch_ren]'s swift departure — that is, until he's rounding the corner of the fish tank and taking his place by my side."

    scene aquarium_tank_day
    play music "audio/bgm/After The Rain.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/walking.ogg"
    $ quick_menu = True
    hide screen menuwu
    show screen dayscalendar
    show peffect
    show ren flushed z at center
    with dissolve

    r "H-Hi, [ch_angel]…"
    y "Oh! Hey you. Fancy meeting you here."
    n "The first thing I notice is how [ch_ren] is tugging at his sleeves again, though he doesn't seem to shy away from my close proximity — nor seem to mind it as much."
    y "Those fish were pretty neat, huh?"
    show ren smirk z at spop
    r "Y-Yeah… I couldn't take my eyes off of y—{nw=0.3}"
    show ren blushing z at bpop
    extend " {i}them.{/i}"
    show ren flushed z at spop
    r "Hey, did you spot the angelfish swimming by?"

    #hide ren with dissolve

    menu:
        #with dissolve
        "\"I was busy looking at the sunfish.\"":
            $ affection_leon += 1
            $ affection_elanor += 1
            show ren sad z with dissolve
            show ren sad z at spop
            r "…Sunfish? There were sunfish as well? I-I didn't even notice… Sorry."
            n "I watch as [ch_ren] awkwardly scratches his jaw before he turns to me with a lopsided smile and a sparkle in his eyes."
            show ren smirk z at spop
            r "You know, I don't think I've ever seen a sunfish from the front."
            y "Haha, really? Actually… You know what? I don't think I have, either."
            y "I guess they'd look a bit silly, huh? Oh— that reminds me! I should've taken some photos!"
            show ren neutral z at spop
            r "Photos? …What for?"
            y "So I can show them to [ch_leon] later! I'm sure he'd find them {i}hilarious{/i}."
            show ren frown z at spop
            r "…"
            show ren sad z at spop
            r "{size=-6}It doesn't bother you knowing that he calls you a sunfish?{/size}"
            y "Hm? Sorry, what was that?"
            show ren flushed z at bpop
            r "N-N-Nothing!"
            n "[ch_ren] immediately whips his head around — and almost smacks it into the glass in the process — as he feigns interest in the fish once more."
            n "Though I can tell he was genuinely feeling embarrassed with how bright his cheeks are. It was honestly… cute."
            n "Still, now that [ch_ren] was right in front of me, I couldn't help but wonder {b}why{/b} he was here in the first place."
        "\"…The what? Clownfish?\"":
            $ ren_switch += 1
            $ affection_teo += 1
            $ affection_jae += 1
            $ affection_olivia += 1
            show ren smirk z with dissolve
            show ren smirk z at spop
            r "Heh, clownfish? Wait… Isn't there a popular movie about one?"
            show ren sad z at spop
            r "Ahhh— what was the name of it? Minding Nino? …Blinding Screamo?"
            y "Are you talking about \"Finding Emo\"? Man, I haven't seen that movie in ages!"
            show ren flushed z at spop
            r "Yeah? M-Me too! We could… We could watch it together sometime."
            show ren blushing z at spop
            r "O-O-Only if you want to, of course!"
            y "Oh? I'd be down for that. I'm pretty sure I've forgotten the entire plot of the movie, anyway."
            show ren smirk z at spop
            r "Hmm… Probably something about finding emos."
            y "Yeah? Well, if you find one, let me know!"
            show ren frown z at spop
            r "…"
            show ren sad z at spop
            r "{size=-6}Is that… your type? Emos?{/size}"
            y "Hm? Sorry, what was that?"
            show ren flushed z at bpop
            r "N-N-Nothing!"
            n "[ch_ren] immediately whips his head around — and almost smacks it into the glass in the process — as he feigns interest in the fish once more."
            n "Though I can tell he was genuinely feeling embarrassed with how bright his cheeks are. It was honestly… cute."
            n "Still, now that [ch_ren] was right in front of me, I couldn't help but wonder {b}why{/b} he was here in the first place."
        "[rh_o]\"I did. It was so captivating.\"[rh_c]":
            $ affection_ren += 1
            $ affection_conan += 1
            $ affection_kiara += 1
            show ren flushed z with dissolve
            show ren flushed z at spop
            r "You—{nw=0.3}"
            show ren blushing z at bpop
            extend "{i}it{/i} was, huh? I couldn't stop looking as well."
            y "Yeah! I didn't even know they could be that colour!"
            y "Actually… This might sound cheesy, but after you mentioned the angelfish… It reminded me of our date by the pier. Remember?"
            show ren happy z at spop
            r "How could I forget? It's one of my most treasured memories. Top {i}three{/i}, in fact."
            n "Not wanting to let this opportunity pass, I decide to tease [ch_ren] a bit."
            y "Pfft— Oh, please… Top three?"
            show ren flushed z at spop
            r "D-Don't laugh! If you get to be cheesy, why can't I?"
            y "Well, in that case… If {i}you{/i} get to give me a cheesy nickname like \"Angelfish\", why can't I?"
            show ren blushing z at spop
            r "Wait, y-you want to… give me a nickname?"
            y "C'mon, it's only fair!"
            y "Though to be honest, I don't really know any pink-coloured fish… [dammit!c]."
            show ren neutral z at spop
            r "Oh yeah? That's too bad."
            y "Hey! Don't think you can get away that easily, {i}Buttercup{/i}. I'll think of something better… {i}eventually{/i}."
            show ren smirk z at spop
            r "Eventually?"
            y "Eventually."
            n "At that, [ch_ren] lets out a puff of laughter before returning his attention to the tank once more. He doesn't seem to stray from my side though, and it's then that I realise… What {b}was{/b} he doing at the aquarium at the first place?"
            n "Without missing a beat, I take a step closer and voice my thoughts."
        "\"I was staring at the sharks.\"":
            $ affection_violet += 1
            $ affection_moth += 1
            show ren smirk z with dissolve
            show ren smirk z at spop
            r "Sharks, huh? They did look kind of cool, didn't they?"
            y "Oh? A shark enthusiast, are we?"
            show ren neutral z at spop
            r "Haha! No, they're a bit too scary for my liking."
            show ren sad z at spop
            r "Plus… I don't think Haruko likes them all that much, either."
            show ren happy z at spop
            r "Say, have you seen the latest episode of AoG yet? Haruko {i}finally{/i} visits the sea for the first t—"
            y "Ah! [ch_ren]! Don't spoil it!"
            y "I was going to watch it later when I have some free time."
            show ren flushed z at spop
            r "O-Oh! Sorry…"
            show ren sad z at spop
            r "You're, um… You're not really missing out on much, though."
            show ren neutral z at spop
            r "It's another one of those boring beach episodes — but I wouldn't mind watching it again."
            y "I see. In that case, maybe we could watch it together sometime?"
            show ren blushing z
            n "[ch_ren]'s response is almost comical; he immediately straightens his posture with such an exaggerated motion that I find it hard not to laugh."
            show ren flushed z at bpop
            r "Y-Y-You want to—!"
            show ren blushing z at spop
            extend" With me?!"
            show ren flushed z at spop
            extend " J-Just the two of us?"
            y "Sure. Unless you know someone else who might be interested?"
            show ren blushing z at bpop
            r "{size=+6}No!{/size}" with vpunch
            n "I watch as [ch_ren]'s cheeks flush a deep shade of red before he whips his head around — and almost smacks it into the glass in the process — as he feigns interest in the fish once more."
            n "Though I can tell he was genuinely feeling embarrassed with how bright his cheeks are. It was honestly… cute."
            n "Still, now that [ch_ren] was right in front of me, I couldn't help but wonder {b}why{/b} he was here in the first place."
    
    y "You know… I wasn't expecting to run into you here."
    show ren sad z at spop
    r "O-Oh, really?"
    y "Yeah. No offence, but you don't really seem like an aquarium guy."
    show ren smirk z at spop
    r "Hehe, is that so?"
    show ren neutral z at spop
    r "I-I didn't have any plans for today, so I figured I'd do a bit of under-the-sea sightseeing to pass the time."
    show ren happy z at spop
    r "Plus… I-I finished the book you recommended the other week. The one about the underwater city?"
    show ren flushed z at spop
    r "I guess it inspired me to come here."
    y "Really?!" with vpunch
    extend " Did you like it? What did you think about it?"
    show ren happy z at spop
    r "I enjoyed it! Especially the part where—"
    show ren smirk z at spop
    r "Oh? S-Say… Look at that."
    n "[ch_ren] isn't shy about how he leans over my shoulder to point at something outside my peripheral vision."
    n "I follow his finger, and between the driftwood and coral, I spot [ch_elanor] and [ch_teo] standing awfully close together."
    n "I don't miss the way [ch_teo] sizes up [ch_ren] — even from a distance — before he tears his gaze away from us with an inaudible scoff."
    n "A surprised sound escapes the back of my throat as I watch [ch_teo] unabashedly run a hand down my co-worker's side — but what truly shocks me is the way [ch_elanor] boldly grabs his arm and loops her hand around it."
    y "No way…"
    show ren frown z at spop
    r "That's—! U-Um…"
    n "Wow. I honestly didn't know she had it in her."
    n "And while her confidence shocked me, it also sparked a bout of curiosity inside of me as well. Even though we all established that this {b}wasn't{/b} an actual date, [ch_elanor] still wanted to treat like one?"
    n "But now that I really think about it, isn't this similar to the date I shared with [ch_ren] at the pier as well?"
    n "The next thing I know, I find my mind wandering to all the times I held [ch_ren]'s hand as we walked along the boardwalk. And right now, it looked all too tempting with how it was casually resting against the glass."
    n "I could easily fit the palm of my hand in his, and I'm sure he wouldn't mind in the slightest if I were to reach out right now and—"
    n "No! C'mon, [ch_angel], what were you thinking?!"
    extend " Althooooough…"
    n "Come to think of it… Wasn't {b}I{/b} the one who initiated most of the hand-holding during the moments we spent together?"
    n "Maybe he'd be okay with it after all. Should I…?"
    
    #hide ren with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "Move your hand away":
            $ affection_ren -= 10
            show ren smirk z with dissolve
            n "[damn!c]. Why was I so fixated on holding his hand all of a sudden?"
            n "Shaking my head to dismiss these thoughts, I pull my hand away and try to play it cool. [ch_ren] doesn't seem to notice my slight change in demeanour — though if he did, he had the decency not to say anything."
            n "Not that he could, however, considering how [ch_elanor]'s voice breaks the silence and captures our attention."
        "[rh_o]Hold [ch_ren]'s hand[rh_c]":
            $ affection_ren += 10
            $ rem_touch = True
            show ren flushed z with dissolve
            n "Before I can talk myself out of it, I reach out and slip my fingers between [ch_ren]'s palm and the glass of the tank."
            n "His skin feels uncharacteristically coarse and rough against my own — but before I can question it — I brush against something cold and metallic instead."
            n "Daring a curious peek, I look down and notice a golden ring on one of his fingers."
            n "In fact, it appeared to look vaguely similar to the one around his neck… But as soon as I open my mouth to ask, [ch_ren] casually slips his fingers between my own to entwine them."
            show ren smirk z
            n "He gives me a soft smile — almost as if he knew this was going to happen — before [ch_elanor]'s voice pulls me back to the present."

    $ choice_style = "default"

################################################################################
## FILLER SCENE HEHEHEHEHEHE
################################################################################
label day4_fillerscene:
    scene aquarium_tunnel_day
    show peffect
    show ren angry at cleft
    show teo smirk at cright
    show elanor sad at center
    with dissolve

    show elanor neutral at spop
    e "[ch_angel]! There you are!" with vpunch
    show elanor sad at spop
    e "Why didn't you say anything earlier, [ch_teo]?"
    show teo frown at spop
    t "…"
    show teo angry at spop
    t "Where'd Pretty Boy run off to? Princess over here said he had to leave earlier."
    show teo smirk at spop
    t "And [damn], if it isn't Buttercup."
    show ren frown at spop
    r "…I-It's [ch_ren], actually."
    n "Ugh. Not this again. Before the two can have the chance to butt heads, I carefully step in and interrupt."
    y "Ah, something came up at the hospital so [ch_leon] had to go."
    show elanor frown at spop
    e "Oh dear. I hope everything is okay."
    y "He assured me that everything's fine, so I wouldn't stress too much about it."
    n "I watch as [ch_elanor] shuffles on her feet in contemplation before noticing the item still grasped carefully in her hands."
    show elanor blushing at spop
    e "That's a relief. But— {i}Oh!{/i}"
    show elanor sad at spop
    extend " What do you suppose we should do with his ticket, then? Shall I ask for a refund?"
    show teo neutral at spop
    t "S'fine. That's like loose change to me. I'll make it back in forty-five seconds."
    show elanor neutral at spop
    e "Still… We shouldn't let it go to waste… Oh, I know!"
    n "[ch_elanor]'s expression shifts from revelation to something more cheeky as she turns to me with a small, knowing grin. She leans close enough to whisper — but doesn't seem all that quiet about it."
    show elanor smirk at spop
    e "Here, why don't we give the ticket to your loverboy?"
    show teo neutral at spop
    t "Loverboy? You've gotta be joking."
    show elanor happy at spop
    e "Hehe! Should I tell you {i}aaaall{/i} about how our lovely [ch_angel] has a secret admirer? And how he often rents out [their] books from the li—"
    play audio "audio/sfx/item.ogg"
    y "{size=+6}[ch_elanor]!{/size}" with vpunch
    show ren sad at spop
    r "I-I feel like I'm missing some context here…"
    n "Almost hastily, I snatch the ticket from [ch_elanor]'s hands and usher [ch_ren] inside the tunnel — {b}away{/b} from my gossipy co-worker and [ch_teo]'s smug grin."

    scene other_dark
    play music "audio/bgm/Summer And Guitars.ogg" fadein 1 fadeout 1
    stop ambience fadeout 2.0
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/running.ogg"
    show peffect
    with GlitchDissolve

    n "I hardly notice the time passing with all the fun I'm having, and before I know it, almost two hours go by in a blur."
    n "I'd initially been so fixated on being a third wheel that I completely forgot about the exciting things people could do at the aquarium."
    n "[ch_elanor] seemed all too happy to snap pictures of everything; ranging from [ch_ren] and I petting some stingrays, [ch_teo] getting splashed by a seal, and all the giant sea creatures that swam around in the overhead tanks."

    scene aquarium_foodcourt_day
    show peffect
    show ren happy at center
    with dissolve

    n "By the time I noticed my feet starting to hurt, we had all made it to the small food court conveniently placed at the end of the main attractions."
    n "[ch_elanor] used this as an opportunity to use the restroom while [ch_teo] wandered off to who-knows-where, so [ch_ren] and I were left to look for a place for us all to sit down and rest."
    n "But we didn't get far before the light sounds of footsteps drew closer once more."
    
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/heels alt.ogg"
    play audio "audio/sfx/sprinting.ogg"
    show ren frown at cleft
    show teo neutral at cright
    show elanor neutral at center
    with easeinright

    show elanor happy at spop
    e "[ch_angel]! [ch_ren]! There you are."
    show elanor neutral at spop
    e "Sorry for the wait! I ran into [ch_teo] earlier while he was talking to one of the tour guides."
    show teo frown at spop
    t "He's a… friend, and {i}I{/i} wanted to talk to him. You didn't need to wait for me."
    show elanor blushing at spop
    e "O-Oh? But you said you were lost and needed help with something urgent?"
    show teo smirk at spop
    t "Aw, c'mon Princess, no need to act coy. Surely people say the same thing to you at the library, right?"
    show elanor sad at spop
    e "Well, yes, I suppose they do… but I don't see what that has to do with me waiting for you."
    show elanor frown at spop
    e "Or acting coy, for that matter…"
    show teo neutral at spop
    t "…"
    show teo smirk at spop
    t "You're adorable when you're clueless."
    show elanor flushed at spop
    e "E-Erm!"
    show elanor neutral at spop
    e "Ahem! Anyway! Are either of you hungry yet? It's past noon, and I'm worried [ch_teo] won't put his pride aside and admit that he's hungry."
    show teo angry at spop
    t "Excuse me?"
    show elanor smirk at spop
    e "Oh? Am I wrong? I could've sworn I heard your stomach growling earlier."
    show teo frown at spop
    t "…Tch."
    show elanor happy at spop
    e "Hehe! Now who's acting coy?"
    n "First of all, when did they reunite without me noticing? And secondly… Was [ch_teo]… Embarrassed?"
    n "There was no way I was going to let this opportunity pass."
    y "Aww, is the big baby hungry? Didn't eat breakfast this morning, did you?"
    show ren frown
    show teo smirk at spop
    t "…I did. Unlike you, I can afford to eat whenever I want."
    n "Though it came out blunt and harsh, I knew [ch_teo] was only joking."
    show elanor neutral at spop
    e "Hmm… Then why don't I go and get us all something to eat? Any preferences? Allergies I should be made aware of?"
    show teo neutral at spop
    t "Aw. Why do you care, Princess? You plotting to kill me or something?"
    show elanor happy at spop
    e "It's only natural to worry about the health of others! I wouldn't want to give you something you're allergic to!"
    show elanor neutral at spop
    e "Besides, everyone deserves to be cared for."
    show teo flushed at spop
    t "…"
    show teo frown at spop
    extend "{size=-6}You're weird.{/size}"
    show elanor happy at spop
    e "What was that?"
    show teo angry at spop
    t "—I said wasabi. I'm allergic to wasabi."
    show ren neutral at spop
    r "…Wasabi, huh?"
    show elanor smirk at spop
    e "I see! And what about you lot? Any preferences?"
    show ren happy at spop
    r "…D-Do you think they have any [favourite_snack]s? I've been having a really bad craving for it recently."
    y "Then in that case, I'll have a—"
    show elanor sad
    n "Before I can voice my preferences, [ch_teo] cuts me off by pulling out his wallet and handing it to my co-worker. [ch_elanor] takes it from him without complaint, but pairs it with a curious look and a slight tilt of their head."
    show teo smirk at spop
    show ren angry
    t "Get whatever. I need to have a word with Dollface over here."
    y "Uh—?"
    play audio "audio/sfx/heels alt.ogg"
    play audio "audio/sfx/item.ogg"
    play audio ["<silence .4>", "audio/sfx/shoes alt.ogg"]
    hide elanor with dissolve
    show ren at tleft
    show teo at tright
    with easeinleft
    n "I don't get the chance to fully respond before [ch_teo] directs me towards the opening of the food court. But I barely get three steps away before I feel a gentle tug at my sleeve."
    show ren sad
    n "Curious, I glance back, only to find [ch_ren] sporting a pout on his soft features."
    show teo neutral at spop
    t "Relax, Buttercup. You'll get [them] back in one piece."
    n "Now that I think about it, it {b}was{/b} kind of out of the blue for [ch_teo] to be acting like this. I mean, since when did he ever want to talk about something serious?"
    n "With that revelation in mind, I offer [ch_ren] a reassuring look and give his arm a comforting squeeze."
    y "I'm sure it'll only be a few minutes."
    show ren sad at spop
    r "…O-Oh."
    n "His eyes flicker between me and [ch_teo] a few times before it lands on my hand still resting on his arm, and he lets out an inaudible sigh."
    show ren frown at spop
    r "O-Okay. I'll… I'll wait for you here."
    show teo angry at spop
    t "No, stay where Princess can see you. Unless you want her to freak out and think we ditched."
    y "Her name is [ch_elanor], you know."
    show teo smirk at spop
    t "Wow. Amazing. Whatever. C'mon, let's go."
    n "Without another word, [ch_teo] nudges me in the right direction — leaving [ch_ren] all alone and confused."

################################################################################
## TEO IS UP TO HIS BS AGAIN
################################################################################
label day4_teocloset:
    scene aquarium_hallway_day
    show peffect
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show teo smirk z
    with Fade(1.0, 1.0, 1.0)

    $ location_ren = "aquarium"
    $ location_elanor = "aquarium"
    
    n "Following closely behind, [ch_teo] leads me to a quiet corner near the food court before turning around and boxing me in with his large arms."
    n "He casually leans his weight to one side before finally speaking."
    show teo neutral z at spop
    t "Hey. So I've got this fun idea."
    y "…Seriously?! I thought you wanted to talk about something urgent!"
    show teo angry z at spop
    t "[damn!c], could you be a little less loud about it? And as a matter of fact; {i}yes{/i}, I do."
    y "No. You always say, 'I've got an idea', and it turns out to be something illegal like trespassing or vandalism!"
    show teo frown z at spop
    t "Isn't that the whole {i}point{/i} of an idea?"
    n "…He was not serious."
    y "We are not about to discuss the logistics behind—"
    show teo neutral z at spop
    t "Look, it's serious. I need you to help me make Ellie or whatever jealous."
    show teo frown z at spop
    t "She's getting a bit too clingy for my taste. And it might even get Buttercup to ease up on all that juvenile, puppy love [shit]."
    show teo neutral z at spop
    t "You seriously don't think he's being too clingy? He's practically glued himself to your side the entire day."

    if relationship_teo == "exboyfriend":
        y "Oh, please. You're one to talk. You {i}always{/i} used to do this to me back when we were dating!"
        y "Remember all those parties you invited me to? Back when we both used to live in the city?"
        y "You always left me by myself so you could go mess around with other people!"
        y "At one point, I had to ask [ch_jae] to take me home because you didn't come back!"
        show teo angry z at spop
        t "…You're not seriously bringing this up again, are you?"
        show teo frown z at spop
        t "Who do you think {i}asked{/i} [ch_jae] to pick you up in the first place?"
        show teo angry z at spop
        t "And I know you. You always hated getting in trouble with the law. Why would I bring you along and get you involved in that [shit]?"
        show teo sad z at spop
        t "Plus, I'd appreciate if you didn't lump all my interests into just \"messing around\". Is that seriously what you think of me?"
        show teo frown z at spop
        t "Am I just some serial cheating sleazebag to you?"
        y "Well, no… But—"
        show teo neutral z at spop
        t "And like I've told you a million times, Doll, we were never dating. You came to that conclusion by yourself."
        y "Excuse me?!"
        show teo frown z at spop
        t "I mean, when have I ever said we were exclusive?"
        y "…"
        show teo angry z at spop
        t "At what point did I ever call you my [partner]?"
        show teo frown z at spop
        t "Every time you asked me what we were, I told you it was just something casual. Nothing more."
        show teo sad z at spop
        t "Sure, you got special treatment — but that's only cuz I saw you as a friend instead of someone I can just screw around with."
        show teo frown z at spop
        t "You don't see me goin' after [ch_jae] or [ch_leon] for the same reason, do you?"
        y "…I guess. But still—"
        show teo sad z at spop
        t "For what it's worth, I'm sorry for giving you the wrong impression. But you knew from the [damn] start that I wouldn't be down for {i}those{/i} kinds of relationships."
        show teo neutral z at spop
        t "I told you this from the very beginning, Dollface; but whatever we had going on between us, it was never meant to be something serious."
        show teo frown z at spop
        t "{i}You{/i} were the one who got too attached and clingy."
        show teo angry z at spop
        t "And now the same [damn] thing is happening all over again with that blonde friend of yours."
    else:
        y "…What? Don't you think that's kind of a roundabout idea? How would this even benefit—"
        show teo smirk z at spop    
        t "Trust me, this is for my own benefit — not yours."

    show teo angry z at spop
    t "Little Miss Princess over there is treating me like I'm a [damn] child who needs to be supervised all the time, and I can't even tell if she's interested in me or not."
    show teo frown z at spop
    t "Plus, you're not exactly j—{nw=0.3}"
    show teo neutral z at spop
    extend " No, never mind."
    show teo smirk z at spop
    t "Either my idea works out and this gathering gets more… {i}interesting{/i}, or she realises I'm not the type to be babied and backs off."
    n "While I had to jump through hoops and hurdles to understand it, [ch_teo] {b}did{/b} have a point. But everything about his idea still felt wrong."
    y "Regardless if I agree or not; if [ch_elanor] saw us flirting, wouldn't she just assume that you're not interested in her at all?"
    y "Besides, I'd never betray her like that."
    show teo neutral z at spop
    t "…Who said anything about flirting?"
    show teo smirk z at spop
    t "[shit!c], you really {i}are{/i} into me, aren't ya? Can't say I'm flattered, Doll."
    y "Excuse me?"
    show teo happy z at spop
    t "All I was gonna do was ignore her for a bit — make them think {i}you're{/i} more entertaining or something."
    show teo smirk z at spop
    t "I mean, it almost worked with that tour guide from earlier…"
    show teo neutral z at spop
    t "But if you wanna cling to my arm too, by all means [gorgeous], go ahead."
    if relationship_teo == "exboyfriend":
        show teo smirk z at spop
        t "Just try not to get attached again this time."
    else:
        pass
    y "You're so insufferable."
    show teo smirk z at spop
    t "So, is it a yes or a no?"
    y "I still don't know what you want me to do exactly."
    n "[ch_teo]'s gaze shifts to something behind me before a light ignites in his eyes as he sends me a sly smirk."
    show teo neutral z at spop
    t "Just follow my lead."
    n "I barely have any time to process his words before [ch_teo] places a hand on the small of my back and pulls me closer to his side."
    n "His voice is louder than usual, and it's {b}then{/b} when I notice [ch_elanor] and [ch_ren] slowly coming into view."
    show teo happy z at bpop
    t "{size=+6}See that storeroom over there? Looks like it's unlocked.{/size}"
    show teo neutral z at spop
    t "{size=+6}Wanna go… check it out?{/size}"
    y "What are you—"

    if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
        call DLC_day4_s2 from _call_DLC_day4_s2
    else:
        show teo smirk z at spop
        t "C'mon Doll. You're really not interested in having a bit of fun? Loosen up a little."

    play audio "audio/sfx/vibrate.ogg"

    n "All of a sudden, I feel my phone vibrate in my pocket. But just as I move to pull it out, [ch_teo] gives me a pointed look and I find myself stalling."

    #hide teo with dissolve

    menu:
        #with dissolve
        "Follow [ch_teo] inside the storeroom":
            $ affection_teo += 1
            $ affection_olivia += 1
            $ affection_jae += 1
            show teo happy z at spop, center with dissolve
            n "With a wink, he leans closer and whispers against the shell of my ear."
            show teo smirk z at spop
            t "Smart choice, Doll."
            n "One of [ch_teo]'s large hands rests atop the one holding my phone, before he uses it to gently tug me along and shuts the door behind us."
        "Refuse and stay where you are":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_violet += 1
            $ affection_leon += 1
            $ d4_altroute = True
            show teo frown z at spop, center with dissolve
            n "At that, he peers at me with a bored expression before rolling his eyes."
            show teo neutral z at spop
            t "Aw, don't be like that."
            jump day4_closetbranch
        "Wait for [ch_elanor] to return":
            $ affection_elanor += 1
            $ affection_kiara += 1
            $ affection_conan += 1
            show teo frown z at spop, center with dissolve
            n "Just as [ch_elanor] looks in our direction, [ch_teo] blocks my view with his body."
            show teo neutral z at spop
            t "Perfect timing."
            n "And just like that, [ch_teo] casually throws an arm over my shoulder to usher me into the closet, before he shuts the door behind us with an audible click."
        "[rh_o]Wait for [ch_ren] to notice you[rh_c]":
            $ affection_ren += 1
            show teo frown z at spop, center with dissolve
            n "The moment [ch_ren] notices my alarmed expression, he immediately starts to make a beeline towards [ch_teo] and I."
            n "But just as he gets cut off by a large family passing by, [ch_teo]'s body covers him from my view."
            show teo neutral z at spop
            t "Looks like we gotta hurry this up."
            n "Without warning, [ch_teo] gently tugs me along by the sleeve of my jacket and shuts the door behind us with an audible click."
    
################################################################################
## STORAGE ROOM SCENE
################################################################################
label day4_storeroomscene:
    scene storage_night
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show peffectp
    with Fade(1.0, 2.0, 1.0)
    
    play audio "audio/sfx/door.ogg"

    n "Darkness envelopes the both of us as I strain to make out the sound of [ch_teo]'s shuffling in order to pinpoint where he is."
    n "Ugh. I seriously can't believe he roped me into doing this—"
    t "This is my side. Don't cross that line."
    y "…What line?"
    t "The line I just drew with my fingers."
    y "[ch_teo], I can barely see anything in here!"
    n "Well… {b}almost{/b}. Even in my corner of the dark room, I can still make out the faint shape of boxes on the shelves, alongside a dirty mop and cleaning supplies that [ch_teo] made sure to put me near."
    n "[shit!c], I hope I wasn't standing in anything."
    if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
        call DLC_day4_teo from _call_DLC_day4_teo
    n "But just as I pull out my phone to use the flashlight and check, bright overhead lights flood the confined space as [ch_ren] and [ch_elanor]'s concerned faces appear from behind the door."

    play audio "audio/sfx/door.ogg"

    scene aquarium_hallway_day
    show peffect
    show ren angry at center
    show elanor flushed at tleft
    show teo smirk at tright
    with dissolve

    t "Well, that was quick."

    play audio "audio/sfx/shoes alt.ogg"
    play audio "audio/sfx/item.ogg"
    with hpunch
    play audio "audio/sfx/running.ogg"
    play audio "audio/sfx/heels alt.ogg"
    show teo frown at bpop, cright
    show elanor sad at bpop, cleft
    with easeoutleft
    show ren angry z at center with dissolve
    
    n "[ch_ren] wastes no time in shoving past [ch_teo] to reach for me, only to take his place by my side and pull me into his chest. Because of this, I could hardly see [ch_elanor]'s (or [ch_teo]'s) reaction."
    show ren frown z at spop
    r "Couldn't you talk to [them] outside?"
    n "I can practically hear the venom dripping from [ch_ren]'s tone as he harshly glares at [ch_teo] from over his shoulder."
    show ren sad z at spop
    r "…Who goes into storerooms \"just to talk\" anyway?"
    show teo smirk at spop
    t "Talk about clingy. Well, whatever. I got what I wanted."

    play audio "audio/sfx/shoes alt.ogg"
    show teo smirk at tleft zorder 1
    show ren sad z at center zorder 3
    show elanor at cleft zorder 2
    with easeinright

    n "I follow [ch_teo]'s gaze as he takes in [ch_elanor]'s flushed expression before he throws an arm over her shoulder, takes the bag of food from their grasp, and guides her out of the closet."
    n "I can hear him mumble something about how adorable she looks with a pouting expression as the door shuts behind them."
    
    play audio "audio/sfx/heels.ogg"
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/door.ogg"
    hide elanor
    hide teo
    with easeoutleft

    scene storage_night
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    show peffectp
    show ren sad z
    with GlitchDissolve

    n "Nothing but silence is left in their wake, and it's then that I notice that [ch_ren] is {b}still{/b} in the closet with me — peering down with an unreadable expression."
    show ren frown z at spop
    r "…Did he hurt you? Do anything strange?"
    y "No, [ch_teo] was just—"
    n "Odd, I couldn't help but feel the need to explain myself."
    y "He just wanted a way to make [ch_elanor] jealous, so he suggested going into this closet with him."
    y "I swear, nothing happened."
    show ren sad z at spop
    r "…"
    show ren frown z at spop
    r "…Do you like him?"
    y "W-What?"
    show ren angry z at spop
    r "Do you like [ch_teo]?"
    show ren sad z at spop
    r "{size=-6}Why else would you agree to… to…{/size}"
    n "Clarifying who he was talking about still didn't lessen the confusion bubbling in my brain, and I can hear [ch_ren]'s grasp tighten around the shelf behind me as he tries to find the words to say."
    n "His breath comes out staggered now, and his gaze isn't any less intense."
    y "No, I— Actually…"

    #hide ren with dissolve

    menu:
        #with dissolve
        "\"Actually, I {i}do{/i} like [ch_teo].\"":
            $ affection_teo += 1
            $ affection_jae += 1
            $ affection_leon += 1
            $ affection_olivia += 1
            show ren angry z with dissolve
            n "Something akin to hatred flashes in [ch_ren]'s eyes before he closes them and rests his forehead against my own."
            n "But the action was fast fleeting as his head eventually drops into the crook of my neck instead, and his hands remain against the shelf behind me."
            show ren frown z at spop
            r "I see…"
            show ren sad z at spop
            r "[fuck!c]. What does he have that I don't?"
        "\"I think I like [ch_elanor] more.\"":
            $ affection_conan += 1
            $ affection_elanor += 1
            $ affection_kiara += 1
            show ren angry z with dissolve
            n "Something akin to rage flashes in [ch_ren]'s eyes before he closes them and rests his forehead against my own."
            n "Though his head soon drops into the crook of my neck instead as his hands remain against the shelf behind me — effortlessly caging me in and preventing me from running away."
            show ren frown z at spop
            r "I see…"
            show ren sad z at spop
            r "[fuck!c]. What does she have that I don't?"
        "[rh_o]\"I like you the most, [ch_ren].\"[rh_c]":
            $ affection_ren += 1
            $ affection_moth += 1
            show ren flushed z with dissolve
            n "[ch_ren] lets out a shaky breath as his composure practically melts in front of me."
            n "His cheeks flush a deep red, and he looks down with intense, lovestruck eyes before he closes them and rests his forehead against my own."
            n "But the action was fast fleeting as his head eventually drops into the crook of my neck instead, and his hands remain against the shelf behind me."
            show ren blushing z at spop
            r "Me…? Y'really like me the most?"
            show ren flushed z at spop
            r "H-Haaah… [fuck!c]. Sorry, I need a second."
        "\"I couldn't care less about [ch_teo].\"":
            $ affection_ren += 1
            $ affection_violet += 1
            $ affection_teo -= 1
            show ren neutral z with dissolve
            n "A foreign emotion sparks within [ch_ren]'s eyes before he closes them and rests his forehead against my own."
            n "Though his head soon drops into the crook of my neck instead as his hands remain against the shelf behind me — effortlessly caging me in and preventing me from running away."
            show ren sad z at spop
            r "Right…? There's something wrong with him."
            show ren frown z at spop
            r "[fuck!c]. The thought of you and [ch_teo] together? I— S-Sorry, I need a second."
        "{image=14NWY symbol} \"You're all I think about, [ch_ren].\"" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
            call DLC_day4_ren from _call_DLC_day4_ren

    y "[ch_ren]?"
    n "He doesn't seem to respond; instead, he simply stays rooted in place while his breath fans against my shoulder."
    n "I can almost hear the wooden shelf creak as his grip tightens — before he pulls back with a determined glint in his eyes."
    show ren sad z at spop
    r "As long as [ch_teo] didn't do anything to you… Then…"
    y "And if he did?"
    show ren neutral z at spop
    r "…"
    stop music fadeout 1
    show ren smirk z at spop
    r "I'd kill him."
    n "It was like the room got cold all of a sudden. There's an unsettling look on [ch_ren]'s face before it quickly morphs into his usual, soft expression."
    n "Was I just imagining things?"
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    show ren happy z at spop
    r "Just kidding."
    n "…Something tells me he wasn't really joking around."
    show ren sad z at spop
    r "Um… A-Angel? Are you okay?"
    n "Was that really [ch_ren] just now?"

    #hide ren with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "Encourage his dark behaviour":
            show ren sad z at center with dissolve
            $ ren_purity -= 1
            $ ren_decay += 1
            $ angel_sanity += 1
            $ death_flag = "teo"
            y "You know what? Maybe you should've."
            y "I can't really stand people who do whatever they please for their own selfish reasons."
            n "I glare at the floor as I recount how [ch_teo] had been treating me lately — like I was something expendable to throw away once he had his fun."
            n "Besides, wasn't that what he essentially did? Once [ch_elanor] came in, he didn't look twice before leaving with her."
            show ren frown z at spop
            r "You… Y-You'd be okay with that? With [ch_teo]… dead?"
            y "Yes."
            show ren sad z at spop
            r "Really? …Y'sure?"
            y "I'm sure."
            n "He stares at me with wide eyes, and it almost makes me regret saying anything in the first place."
            n "I don't really know what just came over me, but still…"
            n "Some decrepit and morbid part of me genuinely {b}did{/b} believe that [ch_teo] would've been better off at the bottom of Lake Bluemoss."
            n "I never really let it get to me, but I've honestly had it up to here with people like him. Those hedonistic individuals who only care about themselves and never the well-being of those around them."
            n "Perhaps it was why I moved away from the city in the first place: to escape people like [ch_teo]. In some messed up way, at least it brought me closer to someone as understanding and considerate as [ch_ren]."
            n "Speaking of, I dare a glance towards my pink-haired companion, only to find him staring back at me with a soft smile. He leans in close this time — as if he wanted to whisper something for only me to hear."
            show ren smirk z at spop
            r "Well. If I ever need to hide a body, I'll know who to call now."
            y "No way you're getting me involved with your crimes!"
            show ren happy z at spop
            r "No? But I think it's a genius idea. They'd never suspect the cute librarian."
            n "Now that the mood had lightened, I give [ch_ren] a playful shove and roll my eyes."
        "Dissuade his dark behaviour":
            $ ren_purity += 1
            $ ren_decay -= 1
            show ren sad z at center with dissolve
            y "[ch_ren]? That was really messed up."
            y "You shouldn't joke around like that. Especially when it involves my friends."
            show ren sad z at bpop
            r "I-I was only kidding, Angel. Really! I wouldn't actually do something like that."
            n "His blue eyes widen at that, and I can tell from his expression that [ch_ren] really was being sincere in this moment."
            show ren frown z at spop
            r "Sorry. It was a stupid thing to say. I won't ever do it again, promise."
            y "Cross your heart?"
            show ren happy z at spop
            r "And hope to di—"
            show ren sad z at spop
            extend " Uh…! No, I mean—"
            show ren frown z at spop
            extend " Wait—!"
            show ren blushing z at spop
            r "Ugh… I-I really need to start thinking before I speak…"
            n "I was partially to blame for setting [ch_ren] up like that, so I let him know by rolling my eyes and sending him a reassuring smile."

    $ choice_style = "default"
    y "Well, now that {i}that's{/i} all sorted, I think we should leave this dingy storage closet by now, don't you?"
    y "I mean, we've been in here for a while."
    extend " And Norie has our food."
    show ren flushed z at spop
    r "I-I suppose we {i}should{/i} leave. But…"
    show ren smirk z at spop
    r "I guess there's something sort of… comforting about this closet. Or maybe it's just you."
    y "Huh?"
    show ren flushed z at spop
    r "Being this close to you… I like it."
    n "Where was this coming from? Suddenly, I can hear [ch_ren]'s arms shift from beside me and move towards my face instead."
    n "His fingertips hover close to my cheek, and for a brief moment, I almost find myself wanting to lean into his touch to feel his warmth."
    n "But he pulls away at the very last second and instead rests his hands by his side once more."
    y "…[ch_ren]?"
    show ren sad z at spop
    r "I don't want to be a hypocrite."
    play audio "audio/sfx/shoes alt.ogg"
    show ren sad with dissolve
    n "He sends me yet another soft smile before stepping back and awkwardly tugging on the end of his sleeve."
    n "…A hypocrite? What did he mean by that? Confused, I press him for answers."
    y "What do you mean?"
    show ren frown at spop
    r "I came in here thinking [ch_teo] was putting moves on you to get a rise out of me."
    show ren sad at spop
    r "If I'm being honest… Part of me wants to think that he's still outside, waiting for us to leave."
    show ren neutral at spop
    r "I kind of… I-I want to… to…"
    n "He covers his mouth with his hand as he awkwardly shifts his weight from one foot to the other. [ch_ren] almost looks like he's weighing his options, and I can't tell if it's a winning or losing battle in his mind."
    n "All I can do is offer him a reassuring look to let him know he can speak more freely with me."
    n "I mean, we {b}did{/b} just have a heart-to-heart about the appropriateness of murder a few minutes ago."
    show ren flushed at spop
    r "I kind of… Want to… Make him jealous, too."
    y "…Oh?"
    show ren blushing at spop
    r "I mean… {i}I'm{/i} supposed to be paired up with you today — Not him. He has no business trying t'take you from me."
    show ren smirk at spop
    r "Not like he could, anyway."
    n "His words remind me of the day at the pier — when that pushy cashier kept trying to flirt with [ch_ren]."
    n "I won't lie and say that I {b}hadn't{/b} been affected by it — it's hard not to be when being with [ch_ren] had been the most exciting thing as of late — but I still had so many things I needed to discuss with him."
    n "What better place to start than here?"
    y "About that… Remember our time by the boardwalk the other day?"
    show ren flushed at spop
    r "O-Our date by the pier?"
    y "Yeah. And how that cashier tried to… Well, I'm not really sure {i}what{/i} she was trying. But she seemed real cosy with you."
    show ren frown at spop
    r "…Cosy? Did it come across that way? I-I thought I made my intentions with her clear…"
    n "The confusion must've been written all over my face as [ch_ren] takes it upon himself to elaborate further."
    
    if angel_sanity >= 1:
        show ren flushed at spop
        r "I um… I maaay have threatened to push her down the staircase…"
        show ren blushing at spop
        r "I-I wouldn't really do it, though!"
        y "…What? You really tried to threaten her?"
        show ren sad at spop
        r "Y-Yes… But only because she tried to take me away from you! I'd never want to make you upset… Or leave your side, for that matter."
        show ren angry at spop
        r "We were having fun together and she had to come along and {i}ruin{/i} it."
        if status_olivia == False:
            show ren angry at spop
            r "{size=-6}Making you upset like that… That clingy leech had it coming.{/size}"
            show ren neutral at spop
            r "B-Besides! Whatever she had to show me downstairs probably wouldn't have been that interesting, anyway."
        else:
            show ren neutral at spop
            r "Besides, whatever she had to show me downstairs probably wouldn't have been that interesting, anyway."
    else:
        show ren sad at spop
        r "I told her I wasn't interested in… whatever she had to show me downstairs."
        y "…You did?"
        show ren happy at spop
        r "Yeah! I did! I promise!"
        y "That was all you said?"
        show ren sad at spop
        r "…Um—! Y-Yes. More or less."
        show ren angry at spop
        r "But I guess she didn't really like that answer, huh? I'm sorry for not telling you sooner."
    n "I let out a deep sigh and weigh [ch_ren]'s words. Was he really telling me the truth?"
    show ren sad at spop
    r "I swear. I'm not interested in her, Angel."
    show ren neutral at spop
    r "In fact… I'm not really interested in {i}anyone{/i} who isn't you."
    show ren smirk at spop
    r "I guess I haven't been really forward enough with you, huh? In that case…"
    play audio "audio/sfx/item.ogg"
    show ren smirk z with dissolve
    n "I watch as [ch_ren] takes a tentative step towards me and reaches an arm out. But before I can feel the cool touch of his hand on my cheek, he seems to… hesitate."
    n "But when I take my own step closer and lean my head into his hand, [ch_ren]'s demeanour seems to melt instantly. He sends me a soft smile before fully committing to cupping my cheek."
    show ren neutral z at spop
    r "Believe me when I say my only interest is in {i}you{/i}, [ch_angel]."
    show ren flushed z at spop
    r "No one could possibly sway me from you."
    show ren smirk z at spop
    r "I-I'm yours completely… {i}All of me.{/i} And more."
    n "[ch_ren]'s gaze is almost intense as he peers down at me. Sincerity manifests on his face {b}and{/b} in his words, and I find myself slowly believing it."
    show ren smirk z at spop
    r "Y'don't need to feel the same way right now, but… So long as you believe me. That's all I ask. And…"
    n "His gaze drops to his feet, and the hand that was once caressing my face now moves to cover his mouth instead. Perhaps it was a trick of the eye, but I could've sworn I saw [ch_ren] gently inhale."
    show ren blushing z at spop
    r "{size=-6}Maybe… Don't look at anyone else who isn't me, too.{/size}"
    y "What was that?"
    show ren flushed z at spop
    r "N-N-Nothing! Just… Wondering if Mr. wasabi hair is still outside this door."
    y "Pffft— Wasabi hair?!"
    y "Why don't you go check then, {i}Buttercup{/i}? I'll wait here."
    show ren happy z at spop
    r "No, I like being here with you instead."
    n "[ch_ren] takes yet {b}another{/b} step closer — we're practically chest to chest at this point — until I could feel the warmth radiate from his body and bring me comfort."
    show ren neutral z at spop
    r "No one compares to you."
    show ren smirk z at spop
    r "I could bask in your company for as long as you let me. I'd never tire of you."
    y "O-Oh."
    show ren neutral z at spop
    r "Was that too much? I figured I'd be more honest and open with you to avoid any more misunderstandings, but I can dial it back."
    show ren blushing z at spop
    r "Or… N-Not do it {i}at all{/i}, if you prefer—"
    y "I don't mind it, [ch_ren]. I just— I wasn't expecting it, I guess."
    y "Normally, you're more… reserved? Almost like Har—"
    show ren happy z at spop
    r "—Like Haruko, right? Haha~ What a coincidence, huh?"
    y "Heh, I suppose. He's my favourite character for a reason, you know."
    show ren neutral z at spop
    r "And is it winning me any points?"
    y "We'll see."
    n "I can feel [ch_ren]'s breath ghost against the shell of my ear as he lets out a puff of laughter."
    show ren flushed z at spop
    r "…Can't believe I'm getting jealous over an anime character."
    y "Hey, now. Unlike Haruko, you're real. I can touch you."
    show ren blushing z
    n "[ch_ren]'s face seems to immediately flush at that."
    y "Besides, imagine how [ch_teo] must be feeling right now. We've been in here for {i}how{/i} long?"
    show ren sad z at spop
    r "Y-You know, I didn't think you'd be on board with making him jealous."
    y "Really?"
    show ren smirk z at spop
    r "Yeah… But if you're still up for it…?"
    n "There's a mischievous glint in [ch_ren]'s eyes, making him look younger and more youthful than he normally appears."
    n "What harm could a little prank do? I {b}did{/b} want to get back at [ch_teo] for making me go through with this in the first place, and admittedly, I was enjoying my time with [ch_ren] in the closet."
    n "I wouldn't have had this much-needed conversation otherwise, nor would I have gotten any clarity if I'd kept pondering over it endlessly. With a lopsided smile of my own, I come to a decision."

    #hide ren with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "{image=14NWY symbol alt} Try and make [ch_teo] jealous" if dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou == True and persistent.streamermode == False:
            $ choice_style = "default"
            show ren smirk z at center with dissolve
            y "Actually… I think I have something different in mind."
            show ren flushed z at bpop
            r "O-O-Oh?"
            n "With a sudden surge of confidence, I take a step closer to [ch_ren] and reach for his waist. He peers down at me with wide, curious eyes — and even goes as far as letting me guide him into a corner before closing the distance once more."
            n "Soon enough, his hands reach out for me to draw me closer to his warmth."
            n "And while it was hard to see in this dark room, it was easy to make out the feather-like touch of [ch_ren]'s fingers as they glide across my skin."
            show ren smirk z
            n "He cups my face with such love and tenderness that it {b}almost{/b} makes me believe I gave him the wrong idea about staying in this closet… that is, until he brings me closer to his own in order to kiss me."
            n "It starts off slow and gentle, almost as if he wanted to take his time with me. There's so much gentility in his affections that it pulls a dreamy sigh from my lips — one which he eagerly devours with every press of his mouth against my own."
            n "Far too swept up in the moment, I barely notice [ch_ren]'s hands trailing down my body until I feel the slight press of his fingers against my sides as he brings me closer to his body."
            n "But before they start to slip between the folds of my clothing in search of skin to caress, I pull away and send the pink-haired man an impish look."
            show ren flushed z at spop
            r "Angel?"
            n "[ch_ren]'s voice seems to have lost its usual soft and timid demeanour, instead being replaced with something coarse and baritone as he looks down at me with half-lidded eyes."
            n "The smile I give him in return is anything {b}but{/b} innocent as I drop to my knees and trail my hands up and down his thighs."
            n "At that, [ch_ren] seems to get the hint almost immediately — if the noise he lets out is any indication — as his hands scramble to seek purchase on the shelf behind him."
            jump day4_wahooscene
        "[rh_o]Stay with [ch_ren] a little longer[rh_c]" if dlc_14nightswithyou_scenes == False or persistent.dlc_14nightswithyou == False or persistent.streamermode == True:
            $ choice_style = "default"
            $ affection_ren += 1
            $ affection_teo -= 1
            show ren happy z at center with dissolve
            y "I'm sure we could spend a few more minutes inside this closet."
            y "We could really sell it if you let me tussle your hair a bit."
            show ren smirk z at spop
            r "Hahaha! Only if you turn your jacket inside out, too. Though… Something tells me [ch_teo] would see right through it."
            y "Yeeeah, I guess he'd be all too familiar with this sort of thing, huh? Hey, have you heard?"
            n "Deciding that if we were going to spend a bit longer inside this closet, I might as well have fun with it. Without missing a beat, [ch_ren] leans closer to me and lowers his head so I can whisper into his ear."
            y "One time, [ch_teo] got caught fraternising with the Mayor's son at some club. Apparently, he left with the wrong tie and belt."
            show ren happy z at spop
            r "Seriously?!"
            y "Yeah! It was all over the news!"
            show ren neutral z at spop
            r "Wow… I must've missed it. I-I don't… usually watch TV."
            y "Oh? And what {i}do{/i} you do?"
            show ren smirk z at spop
            r "I rent good books and chat up [gorgeous] librarians, of course."
            y "And do you normally chat them up in dark closets as well?"
            show ren neutral z at spop
            r "Only one."
            y "…So far."
            show ren happy z at spop
            r "Pfft— So far. I'm hoping it will stay that way."
            n "The smile [ch_ren] sends me somehow makes the closet feel so much brighter."
            jump day4_leavingstoreroom
        "Leave the storage closet":
            $ choice_style = "default"
            $ affection_teo += 1
            $ affection_elanor += 1
            show ren neutral z at center with dissolve
            y "Actually, maybe we should just get out of this closet and face him like adults."
            show ren sad z at spop
            r "Yeah… It's probably for the best."
            y "We wouldn't want to keep [ch_elanor] waiting, either."
            show ren frown z at spop
            r "Y-Yeah. We definitely wouldn't want that."
            n "I can see the dejected look briefly take hold of his expression before [ch_ren] turns on his heels and offers a hand to guide me out of the dark room."
            n "But before he opens the closet door, I place a quick peck on his cheek before stepping out with a grin."
            jump day4_leavingstoreroom

################################################################################
## LEAVING THE CLOSET
################################################################################
label day4_leavingstoreroom:
    scene aquarium_hallway_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 2.0, 1.0)

    $ location_moth = "home"
    $ location_violet = "bluemoss"
    $ location_elanor = "pier"
    $ location_ren = "home"
    $ location_conan = "random"
    $ location_jae = "street"
    $ location_leon = "home"
    $ location_teo = "pier"
    $ location_olivia = "random"
    $ location_kiara = "pier"

    play audio "audio/sfx/door.ogg"
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"

    n "As soon as [ch_ren] and I exit the storeroom, the first thing we notice is that [ch_teo], [ch_elanor], {b}and{/b} our food were nowhere in sight."
    n "Well, I guess the resident arsonist really got what he wanted after all… And for some reason, [ch_ren] seems just as bummed about the situation too."

    play audio "audio/sfx/shoes alt.ogg"
    show ren sad at center with dissolve
    r "…They really just left?"
    y "I guess so. Which kinda sucks because [ch_teo] was my ride home."
    show ren happy at spop
    r "Oh? I-I can drop you off if you want!"
    show ren neutral at spop
    r "Or… We could go to my place? It's not far, and we still have some time to kill."
    n "All of a sudden, the chilling thought of a potential stalker lurking about returns, and I will the unsettling feeling in my stomach to calm down."
    n "Perhaps going home {b}wouldn't{/b} be the best idea right now — especially if someone might still be there waiting for me."
    n "[ch_ren]'s innocent offer lingers in my mind, and I find myself feeling more and more inclined to take him up on it as the seconds pass."
    n "I mean, I definitely {b}would{/b} feel much better if I had someone else around in the off-chance that something were to happen."

    if d3_inviteren == True:
        n "Plus, [ch_ren] {b}did{/b} once offer to let me stay at his place if something ever went wrong."
        n "And some part of me felt almost… safe in his presence."
    elif d1_inviteren == True:
        n "Plus, [ch_ren] {b}did{/b} offer to help out with my intruder situation a few days ago."
        n "And some part of me felt almost… safe in his presence."
    else:
        n "Plus, I {b}did{/b} feel safe in [ch_ren]'s presence."

    n "Still, I didn't want to concern him with my troubles — let alone potentially put his well-being at risk."
    n "I also didn't want anything to happen to [li_name] by revealing too much to [ch_ren]… So maybe it {b}would{/b} be best to keep quiet about my problem and accept his offer. And if I change my mind, I'm sure [ch_ren] would be kind enough to bring me home."
    n "So, with a forced smile, I peer up at [ch_ren] with a determined look and give him my answer."
    y "S-Sounds good to me!"

################################################################################
## GOING HOME SCENE
################################################################################
label day4_visitren:
    scene beach_carpark_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    show peffect
    show ren neutral at center
    with Fade(1.0, 1.0, 1.0)

    $ update_ren = "baby u are my ANGELLLLLLLLLLLLLL"
    $ update_elanor = "After a long day, I think it's time for some wine. ;)"
    $ update_jae = "*blows a kiss to the sky* for maple"
    $ update_teo = "found something even better to do tonight"
    $ update_olivia = "all men do is lie"

    n "The walk to the parking lot was slow and uneventful, but I didn't seem to mind. I was having fun with [ch_ren] as we playfully nudged each other along the sidewalk, and the banter we shared helped brighten my mood."
    n "Eventually, though, things started to wind down, and I found myself trying to fill the silence."
    y "So… [ch_teo] and [ch_elanor], huh?"
    n "Somehow, the conversation keeps falling back to the pair, and I just couldn't understand why."
    n "It wasn't like I was actively trying to think about them. Though… Maybe I just needed to wrack my brain around it for the thought to leave my mind."
    n "A sideward glance in [ch_ren]'s direction shows that he genuinely {b}was{/b} considering my question — if the pursed lip and head tilt were anything to go by — and I couldn't help but chuckle."
    show ren neutral at spop
    r "It sure is a weird combo now that I think about it, b-but… Well, if it works?"
    y "That's true, I suppose. It's just hard to imagine Norie with someone like [ch_teo]."
    show ren sad at spop
    r "…D'you think it's impossible? Being with someone who's not your type?"
    y "I guess it depends on the person…"
    show ren smirk at spop
    r "I see."
    y "What about you, [ch_ren]? Think you could be with someone who might not be your type?"
    show ren frown at spop
    r "No, absolutely not."
    n "His response is immediate, and it has me turning my head in my pink-haired companion's direction."
    show ren smirk at spop
    r "I mean, {i}you're{/i} my type. Why would I want to be with someone who isn't you?"
    show ren flushed at spop
    r "Oh, b-but this isn't about me, right? You asked about [ch_elanor] and [ch_teo]."
    y "…Yeah."
    show ren neutral at spop
    r "Well, do you think they should be a couple?"
    n "I choose to ignore the way [ch_ren] evades my initial question. But I won't lie; his own musings {b}does{/b} leave me pondering."
    n "…Did I think my friend and co-worker would be a good couple?"
    n "Hypothetically, of course. I was well aware of the fact that {b}the{/b} [ch_teo]dore Alvarado would never settle down with anyone."
    n "But still. If anyone would be able to get [ch_teo] to change his ways, I'm sure [ch_elanor] could do it. She just has a certain… charm about her that makes everyone want to be a better person."
    n "I had no doubt that even people like [ch_teo] wouldn't be immune to it."

    #hide ren with dissolve

    menu:
        #with dissolve
        "[rh_o]\"Yes, they would be cute together.\"[rh_c]":
            $ affection_ren += 1
            $ affection_jae += 1
            $ affection_elanor += 1
            $ affection_teo += 1
            $ greenyellow = True
            show ren happy at center with dissolve
            r "Yeah, that's what I was thinking too."
            show ren angry at spop
            r "{size=-6}Maybe then it'd stop 'em from looking at you with hearts in their eyes.{/size}"
            y "What was that?"
            show ren flushed at spop
            r "O-O-Oh! I said, \"Doesn't [ch_elanor] look like she has hearts in her eyes\"? Y-You know… For [ch_teo]."
            y "Looking deeply into Norie's eyes, are we?"
            show ren sad at spop
            r "No!"
            show ren frown at spop
            extend " I would never!"
            show ren sad at spop
            extend " Why would I even—!"
            y "I'm just teasing you, [ch_ren]."
            show ren flushed at spop
            r "Oh…! Ahaha…"
        "\"No, they're not good for each other.\"":
            $ affection_elanor -= 1
            $ affection_teo -= 1
            $ affection_violet += 1
            show ren neutral at center with dissolve
            r "Hm, I see. Well then, I guess we should let fate do its thing, right? We shouldn't interfere."
            y "You believe in fate?"
            show ren smirk at spop
            r "It led me to you."
            y "Jeeeeez, you're so cheesy!"
        "\"I'm not really sure, to be honest.\"":
            $ affection_leon += 1
            $ affection_kiara += 1
            $ affection_olivia += 1
            show ren sad at center with dissolve
            r "Yeah, it's hard to tell with those two, isn't it?"
            show ren neutral at spop
            r "Maybe it's best if we leave it up to destiny."
            y "You know, you sound an awful lot like [ch_leon]."
            show ren frown at spop
            r "…"
        "\"It's not my place to decide.\"":
            $ affection_ren += 1
            $ affection_conan += 1
            $ affection_moth += 1
            show ren sad at center with dissolve
            r "Y-You're right. We shouldn't meddle in other people's affairs."
            y "I didn't know you were such a stickler for rules."
            show ren smirk at spop
            r "Haha~ Should I try acting more like [ch_teo], then?"
            y "Oh, please don't. One of him is enough."
            y "And besides… I like you the way you are."
            show ren flushed at spop
            r "…"

    show ren neutral
    n "Soon enough, our conversation comes to a halt when a sleek, black sports bike comes into view."
    
    if d2_visitren == True:
        n "So [ch_ren] brought his bike again, huh? Part of me still expected someone like him to just… walk everywhere if I was being honest."
    else:
        n "And as I draw closer, I notice a few faded \"Always With You\" sticker decals that adorned the tank."
        n "Did [ch_ren] really own this motorbike? And was he a fan of the webcomic as well?"
        n "I always assumed the community was rather small — there wasn't much talk about the webcomic online — so it was nice to know someone else enjoyed it as much as I did."
        n "But just as I was about to bring the topic up, [ch_ren] blocks my view as he turns to me with an embarrassed smile."

    show ren sad at spop
    r "If I had known I'd be bringing you home, I would've brought my car instead."
    show ren neutral at spop
    r "But I, um… I recently loaned it to a friend, actually."
    y "Oh, really?"
    show ren sad at spop
    r "Yeah, he's out of town though… I doubt I'll be getting it back anytime soon."
    show ren happy at spop
    r "A-A-Anyway!"
    n "[ch_ren] retrieves a spare helmet from the side of his motorbike and turns to me once more."
    
    if d2_visitren == True:
        n "All too familiar with this routine, I let him slip the helmet on and secure it tightly. I still wasn't used to riding his bike, but I put the fear aside for the prospect of {b}more{/b} free food and a warm home."
    else:
        n "With a nervous glance, I let him slip the helmet on and secure it tightly. I'd never been on his motorbike before, but I put the fear aside for the prospect of {b}more{/b} free food and a warm home."

    scene other_dark
    play music "audio/bgm/After The Rain.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve

    n "Somehow, we managed to make it to [ch_ren]'s apartment complex in record time. I guess he really wasn't lying when he said it wasn't that far."
    n "And unlike [ch_teo], [ch_ren] {b}lawfully{/b} parks his bike in the designated area before guiding me towards the elevator with a spring in his step."
    n "Tacky music plays as we slowly ascend to the upper levels, though [ch_ren] only makes it even more awkward by staring at the back of my head the entire time."
    n "I can practically feel his eyes on me even as I try to ignore them, so I offer him a forced grin while we both wait for the elevator doors to open."

    scene sh_complex_night
    show peffect
    show ren neutral at center
    with dissolve

    $ persistent.fact_residence = True

    if d2_visitren == True:
        n "Once they do, I let out a sigh of relief."
        n "The same gaudy interior greets us, and I still find myself trying to process how [ch_ren] could afford such a lavish place."
    else:
        n "Once they do, I was immediately met with a grandiose corridor and large, spacious doors — and I found myself wondering how much it'd cost to live in a luxurious place like this."
        n "[damn!c]. Did [ch_ren] really live here?"
    
    play audio "audio/sfx/item.ogg"
    n "Too lost in thought, I aimlessly follow behind my pink-haired companion as he leads me towards his door — before bumping into his backside when he abruptly stops in his tracks."
    show ren frown
    n "Concerned at his odd and sudden reaction, I glance up only to find him staring intently at the floor."
    n "Following [ch_ren]'s gaze, I notice the lights coming from beneath the cracks of one of the doors. And weirdly enough, the faintest hint of black smoke seems to be emerging from there as well."
    n "Smoke? …Did they burn their food or something?"
    n "Confused, I look to [ch_ren] to see if he has any better ideas."
    y "Is there something wrong?"
    show ren flushed at spop
    r "Hm? Oh! No! I-I just…"
    show ren sad at spop
    r "I didn't realise someone had… moved in. I thought I was the only one who lived on this floor."
    y "Not a fan of sharing, are we?"
    show ren smirk at spop
    r "Not… particularly."
    show ren frown at spop
    r "{size=-6}Still… I guess everything should be fine as long as I don't—{/size}{nw=0.3}"
    show ren neutral at spop
    extend " never mind."
    n "Before I can question it, [ch_ren] continues walking until we arrive at our destination."
    n "Watching him dig through his pockets for his keycard only reminds me to check my phone — but when I reach for it, I notice that my own pockets are empty."
    n "A wave of realisation hits me as the panic slowly starts to creep in."
    y "Oh, shoot!"
    show ren sad at spop
    r "Hm?"
    n "In my flustered state, I barely notice [ch_ren] turning to me with a curious look on his face."
    y "Ugh. I think I left my phone back at the aquarium!"
    show ren frown at spop
    r "Are you sure?"

    if d4_wahooren == True:
        call DLC_day4_s3 from _call_DLC_day4_s3
    else:
        y "Yeah… I'm pretty sure I placed it on the shelf when [ch_teo] pulled me into that closet earlier."
        show ren angry
        n "[ch_ren] seems to bristle at that."

    show ren neutral at spop
    r "H-Hey, don't worry. I'll go back and get it. The aquarium should still be open, anyway."
    y "I'm so sorry about this."
    n "[ch_ren] unlocks the door and gestures for me to go inside."
    show ren happy at spop
    r "Don't worry about it, [ch_angel]. Here, make yourself at home! I'll be back before you know it."
    n "[ch_ren] doesn't give me a chance to say goodbye before he's speeding off towards the direction of the elevator. Leaving me to my own devices, I awkwardly step inside his apartment and take everything in."

################################################################################
## ANGEL GOES SNOOPIN LMAO
################################################################################
label day4_snooping:
    scene ren_lounge_night
    show peffect
    play audio "audio/sfx/door.ogg"
    with GlitchDissolve

    if d2_visitren == False:
        play audio "audio/sfx/walking.ogg"
        n "I venture further into the entryway — leaving the grandiose corridor and large, spacious doors behind me."
        y "Woah…"
        n "Did [ch_ren] seriously live in a place like this? It was hard to imagine as I awkwardly stand at the entrance to his foyer in shock."
        n "Yes. {b}Foyer{/b}. He had a whole [damn] foyer in his apartment."
        n "Was this even an apartment? Surely a penthouse would've made more sense."
        n "Feeling nosey, I shut the door and meander my way further into his home. And soon enough, I find myself in [ch_ren]'s spacious lounge room."
        n "Aside from the hallway, the rest of the lights were off — but I could still make out most of the dark shapes within the room with ease."
        n "It was just as ostentatious as the rest of his house, though I couldn't help but feel like it lacked any form of life."
        n "It just didn't seem like someone actually lived here."
        n "The furniture was gaudy yet tasteless, there was hardly any personal decoration or colours, and there was nothing that really screamed '[ch_ren]' to me."
        n "There were no personal touches, photos, items, hobbies, {b}nothing{/b}. Just tacky furniture and the bland smell of something sterile."
        n "If I was being honest, it gave off the same vibe as a dentist's clinic or a hospital."
        n "But as I look closer, I soon find myself eating my words. It's {b}then{/b} when I notice a large desk pressed against one of the corners in the room; tucked and hidden away from view."
    else:
        n "Everything looks the same as the last time I was here — down to the cold, marble flooring and gaudy furniture scattered about the place."
        n "And although I didn't notice it last time, the mirror in his entryway looked very similar to mine. The only difference was that {b}his{/b} was hung up correctly."
        y "Heh, cute."
        n "Well. At least now I know what mine will look like once I put in the effort to fix it. But until then, it's going to stay crookedly placed on my wall and forever taunt me."
        play audio "audio/sfx/walking.ogg"
        n "Saving that mental note for later, I recall my steps towards [ch_ren]'s spacious lounge and take everything in."
        n "Yep, still the same grandiose furniture, sterile smell, and—"
        extend " Wait a second."
        y "Oh?"
        n "Looking closer, It's {b}then{/b} when I notice a large desk pressed against one of the corners in the room; tucked and hidden away from view."
        n "It didn't look brand new — though I don't recall looking in that spot the {b}last{/b} time I was here, either. The desk could've been here since the beginning for all I know."

    n "I can't help the twang of curiosity that hits me as I draw closer towards it. And with the desk now close enough to see, I can easily make out the shape of some kind of art station — as well as [ch_ren]'s laptop still open to the side."
    n "Papers were scattered all over the rest of the table, and another tentative step closer brings its contents into view. Were they… Rough drafts for a webcomic?"
    n "I had an inkling [ch_ren] would be into them — given his interest in AoG — but I had no idea he {b}created{/b} a few of his own."
    n "One book in particular, however, piques my interest with its unique cover (though it might've just been the book-lover in me). It was thick and worn out, yet it looked like it was well taken care of."
    n "I notice some kind of smudge marks — possibly red paint — stain the front of the cover; as well as some sort of circular, indented notch right in the center."
    y "Does something go inside here?"
    n "The contraption is foreign to me, and whatever fit inside must've been how you unlock it. But as I turn the book in my hand, I notice that the latch was {b}already{/b} detached — and a few loose pages spill out onto the desk."
    play audio "audio/sfx/paper.ogg"
    play audio ["<silence 0.2>", "audio/sfx/slide.ogg"]
    play audio ["<silence 0.4>", "audio/sfx/fabric.ogg"]
    y "Ack!"
    n "With a panicked cry, I quickly scoop the papers back up and open the book to stuff them back inside."
    $ persistent.fact_awy = True
    n "But as I do so, something else catches my eye. Weren't these… sketches from \"Always With You?\""
    n "I could easily make out the male lead's hairstyle anywhere — after all, it was similar to [ch_ren]'s (or rather, Haruko's) — yet this one had a contrasting shade of black instead of pink."
    y "Maybe another character, then?"
    n "Strange… I don't remember seeing any similar black-haired characters in the webcomic."
    n "Still, the likeness of the art style was insane. And \"Always With You\" was the {b}only{/b} webcomic published by the anonymous author — their debut into the online industry was a huge success because of it."
    y "Soooo… Fan art?"
    n "It was oddly cute to think that [ch_ren] might've made his own self-insert character, though if {b}I{/b} were any better at art, I probably would've done the same."
    n "Curiosity once again gets the better of me (or was it my hyperfixations?), and I was half tempted to peek through the rest of the book to learn more."
    n "…Should I?"

    menu:
        "Investigate the drawings":
            $ affection_ren -= 5
            $ affection_moth += 1
            $ affection_olivia += 1
            $ affection_kiara += 1
            $ d4_snooping = True
            $ d4_gloomy = True
            $ persistent.d4_snooparound = True
            n "I can't resist the urge to flip through the pages, and when I do, my suspicions are confirmed."
            n "There, right in front of my eyes, were the all too familiar characters from \"Always With You\", yet something about them felt almost… uncanny."
            n "They didn't look {b}exactly{/b} like the actual characters from the webcomic, though I could sense a certain familiarity from them."
            n "And upon closer inspection, most of the drawings were of the main character and [their] love interest doing various, lovey-dovey things together — though other drawings were depicted as rather ominous and gloomy."
            n "Which was ironic, considering that the male lead was usually referred to as \"Gloomy\" by the narrator. He was often withdrawn and greatly preferred to lurk in the shadows instead of interacting with others, so the name really fit."
            n "But still… Seeing my beloved Gloomy in some of these drawings — surrounded by hundreds of creepy eyes, harsh scribbles, and more of that deep, red ink — it honestly made me feel… {b}bad{/b} for him."
            if persistent.deadend1 == True:
                n "Why was he often being drawn in a dark room with nothing in it? And… Why did it look so familiar?"
            else:
                n "Why was he often being drawn in a dark room with nothing in it? Almost like an endless void with no exit in sight?"
            n "Figuring I'd seen enough — or perhaps I just didn't want to see one of my comfort characters so… {b}alone{/b} — I tear my eyes away from the pages and close the book."
            play audio "audio/sfx/glass.ogg"
            n "When I do, I make sure to shut the latch properly and place it back on the table. But as I do so, I accidentally knock over one of the ink bottles, which stains the desk a deep shade of black."
        "Look at the weird lock":
            $ affection_ren -= 5
            $ affection_elanor += 1
            $ affection_conan += 1
            $ d4_snooping = True
            $ persistent.d4_snooparound = True
            n "Glancing at the book still in my hands, I check out the lock one more time."
            n "Yet no matter how many times I turn and angle the book differently, I still can't figure out how the mechanism works. It didn't look like a normal key would fit in it, and I didn't see any space to insert one in the first place."
            n "All it had was a small indent in the center and room underneath to insert the latch. But upon further inspection… Wouldn't a ring fit in there?"
            n "It had just enough space for one — and it definitely fit the circular shape — though I don't think I'd ever heard of a lock that could be opened with a ring."
            y "Pfft, maybe I should invest in one for my own apartment."
            n "Figuring it isn't my place to snoop any further, I tear my eyes away from the front cover and close the book."
            play audio "audio/sfx/glass.ogg"
            n "When I do, I make sure to shut the latch properly this time and place it back on the table. But as I do so, I accidentally knock over one of the ink bottles, which stains the desk a deep shade of black."
        "Check out the desk":
            $ affection_ren -= 5
            $ affection_moth += 1
            $ affection_jae += 1
            $ affection_teo += 1
            $ d4_snooping = True
            $ persistent.d4_snooparound = True
            n "Holding the book to my chest for now, I glance at the desk once more. The papers were still there, alongside [ch_ren]'s laptop that was {b}still{/b} surprisingly on — despite not being plugged into a power socket."
            n "Admittedly, it did pique my interest."
            y "Why would [ch_ren] leave his laptop unattended?"
            n "As if getting a response, a message pops up on the screen and startles me."
            if status_olivia == False:
                npct "u sure she's gone for real this time? we cant risk…… u know. after what happened last time"
                npct "it's like its following us >:("
                npct "and just a suggestion but mybe try burning that other thing too? i dont want any chanses"
                npct "chances* ??? idk"
            else:
                npct "u sure that was o? what is she doing here? didn't we… u know?"
                npct "and don't tell me ur still keeping contact with that thing?"
                npct "u know whats going to happen if u do"
                npct "dont make it mad ren."
            npct "look. i'll see if i can visit and help u out as well. need 2 return ur boring piece of junk anyway"
            npct "{b}{color=#6ff}[[ {/color}{glitch=20.0}{color=#6ff}{b}ERROR{/b}{/color}{/glitch}{color=#6ff} ]{/color}{/b} didn't like it :("
            npct "well, whtever."
            npct "don't do anything stupid in the meantime {b}{color=#a30b11}[[ {/color}{glitch=20.0}{color=#a30b11}{b}REDACTED{/b}{/color}{/glitch}{color=#a30b11} ]{/color}{/b} "
            n "All of a sudden, the app closes itself and shows me [ch_ren]'s cluttered desktop. And out of the corner of my eye, I swear I see the red light of his webcam turn on for a split second."
            n "[fuck!c], I shouldn't have been looking through [ch_ren]'s personal messages without his permission. What kind of creep does that, anyway?"
            n "Almost ashamed, I step away from the laptop — but not before realising the item still grasped in my hands."
            y "Oh."
            play audio "audio/sfx/glass.ogg"
            n "Closing the book, I make sure to shut the latch properly and place it back on the table. But as I do so, I accidentally knock over one of the ink bottles, which stains the desk a deep shade of black."
            pass
        "[rh_o]Let [ch_ren] have his privacy[rh_c]":
            $ affection_ren += 1
            $ affection_violet += 1
            $ affection_leon += 1
            n "What was I thinking? I wasn't about to invade someone's personal space like that. [ch_ren] had been nothing but respectful with me, so it wasn't right to simply rummage through his stuff."
            n "With a resolute nod, I step away from the laptop — but not before realising the item still grasped in my hands."
            y "Oh."
            play audio "audio/sfx/glass.ogg"
            n "Closing the book, I make sure to shut the latch properly and place it back on the table. But as I do so, I accidentally knock over one of the ink bottles, which stains the desk a deep shade of black."
    
    y "Ah! [shit!c]!"
    if d2_visitren == False:
        n "I frantically skitter about to look for some paper towels, and eventually find myself in front of (what I assumed were) one of [ch_ren]'s gaudy bathrooms."
        scene ren_bathroom_day
        show peffect
        play audio "audio/sfx/movement.ogg"
        with GlitchDissolve

        y "Woah…"
        n "Even his restroom looked expensive… I was afraid of touching anything, fearing I'd accidentally break it and end up paying for it."
        $ persistent.fact_cosmetics = True
        n "Glancing around again, I noticed how his countertop seemed to be void of any dental care, hairbrushes, and skincare products — though a few bottles of concealer and an opened box of hair dye sat in the corner near the sink."
        n "Well, I guess that answers my burning question on whether or not he naturally had pink hair…"
        n "But now it made me wonder; if [ch_ren] {b}does{/b} dye his hair, then what was his natural hair colour?"
        n "There were still so many things I didn't know about that soft-looking guy, and I was beginning to question whether coming here was a good idea or not."
        n "With a sigh, I decide not to waste any more time thinking about irrelevant things and instead turn my attention back to the mission at hand — which was finding something to dry the ink with."
        n "It takes me a moment of contemplation, but I eventually settle on a roll of toilet paper before rushing back to the living room. And by some miracle, it easily lifts the mark from the desk — though it only seems to transfer onto my skin instead."
    else:
        n "I frantically skitter about to look for some paper towels, and eventually settle on some toilet paper from [ch_ren]'s bathroom. By some miracle, it easily lifts the mark from the desk — though it only seems to transfer onto my skin instead."
    y "Ugh! Great, just when I thought it couldn't get any worse."

    scene other_dark
    show peffectp
    play ambience "audio/ambience/shower.ogg" fadein 1 fadeout 1
    with Fade(1.0, 2.0, 1.0)

    n "It takes a solid minute or two of scrubbing until I'm satisfied. And once I'm sure no stains are left on the table, I haphazardly throw the toilet paper into the trash can and wash my hands in the kitchen sink."
    n "That alone takes another five minutes of scrubbing and rinsing, but I somehow managed to lift all the ink from my skin and wash it down the drain."
    n "After all this, I {b}definitely{/b} learned my lesson not to snoop ever again."
    stop ambience fadeout 2.0
    n "With an embarrassed sigh, I plop myself on the couch and let out a groan. A small part of me knew [ch_ren] wouldn't get upset over something so small, but still…"

    if d4_snooping == True:
        n "I didn't want him to know that I was snooping through his things — much less trying to learn more about his personal hobbies and interests."
    else:
        n "I didn't want him to know that I had been casually looking at things in his apartment without him knowing."

    n "The queasy feeling in the pit of my stomach only seems to worsen at that, and I contemplate running away from such a confronting scene and locking myself at home for the rest of my life."
    n "Forget my phone. I could always buy a new one — I'm sure I still had my spare one still lying around in a box collecting dust somewhere."
    n "Sure, the screen was cracked, but it'd still get the job done."
    n "Still… I couldn't help but feel like I was making a mountain out of a molehill. And there was the looming threat of a potential stalker waiting for me to come home."
    n "Maybe it was best if I stayed here after all."
    n "With that thought in mind, I settle further into [ch_ren]'s plush couch and anxiously await his return."

    scene ren_loungeroom_night
    show peffectp
    with GlitchDissolve

    n "I can hear the faint ticking of a clock from somewhere in this endless maze of an apartment, alongside the occasional humming of the central heater he turned on before he left."
    if d2_visitren == True:
        n "So he finally figured out how it worked?"
    else:
        pass
    n "Aside from that, the silence is almost deafening — and I have half a mind to reach for the remote and turn on the television."
    n "Surely it wouldn't hurt? I mean, [ch_ren] {b}did{/b} say I could make myself at home… You know, potential snooping aside."
    n "Ugh… Perhaps it was to get rid of the guilty feeling forming in my stomach, but I quickly find myself shaking my head to dismiss those thoughts and reaching for the remote on the table."

################################################################################
## TELEVISION OUTCOME
################################################################################
label day4_televisionscene:
    if death_flag == "teo":
        $ death_flag = "hehe"
        $ status_teo = False
        $ persistent.d4_killteo = True
    else:
        pass

    n "Flicking through the channels, I land on one in particular. And although the signal was weak, I could discern the picture of some news reporter in a blazer that looked far too flimsy to keep her warm."
    n "She's droning on about the local happenings in Corland Bay before a familiar backdrop comes on the screen and captures my full attention."
    y "Oh?"

    if status_teo == False:
        play music "audio/bgm/Lonely Doll.ogg" fadein 1 fadeout 1
        n "The entrance to the aquarium appears on the television as ambulance lights flash and sirens go off in the background."
        n "There's a sombre expression on the reporter's face as she communicates with her counterpart who is currently at the location."
        npc "—ictim's body has just been found— *crrk!* —mauled and ripped apart— *crrk!* —in one of the shark tanks."
        npc "Authorities have confirmed that it {i}is{/i} the body of— *crrk!* —Cristian— *crrk!* —do's son and sole heir to the corporate giant— *crrk!* —Tech marketing."
        npc "—Also believe that— *crrk!* —was a self-inflicted accident."
        npc "Here on the scene with us, we have the Mayor's chairman and the mother of the victim, Kaori Alv— *crrk! *— to talk about—"
        play ambience "audio/ambience/heartbeat.ogg" fadein 1 fadeout 1
        n "The TV turns to static, and I quickly reach for the remote to find another channel. Another news show pops up; this time showing a grainy, black and white recording of CCTV footage taken from the aquarium."
        n "And though it's hard to make out, the footage depicts a person pacing around on the wooden decks until the upper half of their body is just out of frame."
        n "The rest of their body was still in view, though; being illuminated by their phone screen as they fiddled with it. Then, all of a sudden, the person immediately drops it — almost as if it was too hot to touch — and takes a step back."
        n "They must've lost their footing or something, as they end up tumbling into the tank and submerging themselves underwater."
        n "The footage cuts out shortly after, seemingly too inappropriate to air on live television, as noted by the reporter."
        y "…"
        n "I let out a breath I hadn't known I'd been holding and let reality sink in. I was just at that aquarium… I looked at those sharks with everyone just hours prior."
        n "Everything felt all too surreal in this moment, and I suddenly wished I had my phone to text [ch_elanor] and [ch_teo] to see if they saw the news."
        n "With my heartbeat still hammering loudly in my chest, I end up unconsciously turning the television off to avoid hearing about {b}more{/b} heavy topics."
        stop ambience fadeout 2.0
        play music "audio/bgm/After The Rain.ogg" fadein 1 fadeout 1
    elif greenyellow == True:
        n "It looked like the upscale restaurant where [ch_conan] and my other co-workers held my welcoming party. Everything still looks the same, except the main thing that holds my interest are the two people sitting in a quiet corner of the room."
        n "No way… I could easily make out the blonde patch of [ch_elanor]'s head, but what surprised me was the fact that {b}[ch_teo]{/b} was there as well."
        n "In fact, he seemed all too happy to be in [ch_elanor]'s company, given how he was casually leaning into his chair with a lazy smirk on his face. Was he… Enjoying himself?"
        n "But more importantly… Were they still on a date?!"
        y "That's not possible…"
        n "[ch_teo] and [ch_elanor]? {b}[ch_teo]?{/b} Mr Non-comital himself? I was certain today's outing had only been for his enjoyment. Yet… Why did he genuinely look happy to be on a date with [ch_elanor]?"
        n "Slapping my hands against my cheeks, I bring myself to my senses. I was so caught up on [ch_teo] that I almost forgot another major factor: [ch_elanor]."
        n "She's the most sweetest, caring person I know; and she could make just about {b}anyone{/b} soften up to her. I wouldn't put it past [ch_teo] to realise that and possibly open up as well. But still, it certainly wasn't what I was expecting — and so soon, too."
        n "The news reporter soon returns and continues on about some planned renovations happening at that restaurant — right before it switches to a pre-recorded broadcast about a recent murder in the city."
        n "The mere mention of New Salvus had me curling in with disgust, and I had half a mind to change the channel or turn the TV off altogether."
    else:
        n "It looked like the upscale restaurant where [ch_conan] and my other co-workers held my welcoming party. Everything still looks the same, except the main thing that holds my interest are the two people sitting in a quiet corner of the room."
        n "Oh? Was that [ch_elanor] and… [ch_kiara]?"
        n "They seemed to be enjoying each other's company, given how they were both smiling and laughing at each other's jokes."
        n "Today's outing aside, it sure was good to see [ch_elanor] having fun outside of our workplace. I hardly ever see her outside of the library, so it was nice to know that she was enjoying herself."
        n "The news reporter soon returns and continues on about some planned renovations happening at that restaurant — right before it switches to a pre-recorded broadcast about a recent murder in the city."
        n "The mere mention of New Salvus had me curling in with disgust, and I had half a mind to change the channel or turn the TV off altogether."

    n "Seeing all of this recent talk of gore and murder on TV, it makes me feel…"

    $ choice_style = "box"
    menu:
        "I enjoy seeing it":
            $ meter_gore += 1
            $ angel_sanity += 1
            $ ren_decay += 1
            $ ren_purity -= 1
            n "I guess some morbid part of me honestly {b}liked{/b} hearing about all these sickening topics on the news."
            n "Though… It made sense considering how I'd been all but encompassed by it while living in the city. Everywhere I went, I was surrounded by petty crimes, selfish [asshole]s who called themselves my friends, and even the stench of death."
            n "I always thought moving to Corland Bay would give me a break from it — after all, everyone always says nothing bad happens here — but I guess I was wrong."
        "I feel sick just hearing about it":
            $ meter_gore += 0
            $ angel_sanity -= 1
            $ ren_decay -= 1
            $ ren_purity += 1
            n "Thinking about all of this gory violence and death… It makes me feel uneasy."
            n "In fact, it was one of the reasons why I left the city in the first place. Prior to moving to Corland Bay, I had always been surrounded by petty crimes, selfish [asshole]s who called themselves my friends, and even the stench of death."
            n "Moving here had been a good decision at the start, but now… I'm not so sure. Everyone would always say that nothing bad ever happens in the Bay, but after recent events? It was slowly becoming untrue."
            y "Ugh…"

    $ choice_style = "default"
    n "But I suppose it wasn't all bad. I have supportive friends now, an amazing boss and co-worker, and a timid library patron who goes to great lengths to keep me safe."
    n "Man… I guess I never truly appreciated [ch_ren]'s thoughtfulness until this moment."
    n "He's done so much for me these past few days, and not once has he asked for anything in return."
    n "And as if manifesting him with my thoughts, I hear the telltale sounds of the front door unlocking before [ch_ren] shuffles inside and flicks on all the lights."

################################################################################
## REN'S APARTMENT PART 2 ELECTRIC BOOGALOO
################################################################################
label day4_renreturns:
    scene ren_lounge_day
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve

    play audio "audio/sfx/door.ogg"
    play audio "audio/sfx/walking.ogg"
    n "In one of his hands is my beloved phone — alongside a bag of delicious-smelling takeout and an angelfish plushie peeking out from another."
    n "And almost like a puppy, [ch_ren] immediately makes his way over to me — still perched on the couch — before depositing the toy in my hands."

    if status_teo == False:
        play audio "audio/sfx/shoes alt.ogg"
        show ren sad z at center with dissolve
        r "[player_fl]-[ch_angel]? …Were you sitting in here without any lights? S-Sorry, I should've turned them on before I left."
        show ren happy z at spop
        r "But, um— I brought some food with me! I figured you might be hungry."
        show ren flushed z at spop
        r "…I-I don't really have much food in the pantry right now."
        show ren sad z at spop
        r "Also— Well…"
        n "[ch_ren] looks as though he has something deeply serious he wants to say, and I had some kind of inclination as to what it might be."
        show ren sad z at spop
        r "Something happened at the aquarium, [ch_angel]. You might want to…"
        show ren frown z at spop
        r "Actually, m-maybe we should move this conversation to the kitchen?"
        y "…I already know, [ch_ren]."
        show ren sad z at spop
        r "You do? About—"
        y "Yeah. I saw on the news. So it's true, then? Someone really did die?"
        show ren frown z at spop
        r "I-I didn't really stick around to find out once the first cop car pulled up. But…"
        show ren sad z at spop
        r "I don't know… Something doesn't add up."
        y "What do you mean?"
        n "[ch_ren] looks conflicted with what he wants to say."
        show ren sad z at spop
        r "I passed by that shark tank when I went to retrieve your phone, and I…"
        show ren frown z at spop
        r "Well, I didn't exactly stop to look, but I-I didn't see any dead bodies in there…"
        if angel_sanity >= 1:
            show ren sad z at spop
            r "Look, I-I know we said some incriminating things today, but I swear—"
            show ren sad z at bpop
            extend " It wasn't serious, and I— Angel, I would never— I-I…"
        elif angel_sanity == 0:
            show ren sad z at spop
            r "Look, I-I know I said some incriminating things today, but I swear—"
            show ren sad z at spop
            extend " I didn't— Angel, I would never— I-I…"
        else:
            pass
        n "I could tell that [ch_ren] was taking this {b}hard{/b} with how he wouldn't meet my gaze and his shoulders seemed to shake."
        show ren frown z at spop
        if ren_decay >= 1:
            r "I wasn't the one who killed him."
        else:
            r "I wasn't the one who killed them."
        y "It's okay, I believe you."
        show ren sad z at spop
        r "Y-You do?"
        n "It was like a weight was taken off of his shoulders. And without thinking, I find myself stepping closer to bring [ch_ren] into a comforting hug."
        y "I know you, [ch_ren]. You'd never hurt a fly."
        y "And I saw what happened on TV. They {i}fell{/i} into that tank. The reporters say it was a self-inflicted accident."
        show ren flushed z at spop
        r "Man, you really are an angel…"
        n "I can feel his hands clench around the back of my shirt before he pulls away with a forlorn expression. He attempts to put on a smile for my sake, though I could see right through it."
        show ren smirk z at spop
        r "Here, why don't we eat something to get our minds off this."
        show ren sad z at spop
        r "A-Are you feeling up to it? I know this might be… a lot for you to stomach right now."
        y "Yeah… Some food might be nice."
        show ren happy z at spop
        r "Great! Let me get some plates so we can eat, then."
    else:
        play audio "audio/sfx/shoes alt.ogg"
        show ren sad z at center with dissolve
        r "[player_fl]-[ch_angel]? …Were you sitting in here without any lights? S-Sorry, I should've turned them on before I left."
        show ren happy z at spop
        r "But, um— I brought some food with me! I figured you might be hungry."
        show ren flushed z at spop
        r "I-I don't really have much food in the pantry right now… Heh."
        y "Oh, that's fine! Thanks for being so considerate."
        show ren happy z at spop
        r "Yeah! I mean- No problem! It's nothing!"
        show ren flushed z at spop
        r "Uh… Let me get some plates, and we can eat, then."
    play audio "audio/sfx/shoes alt.ogg"
    show ren neutral at center with dissolve
    play audio "audio/sfx/walking.ogg"
    hide ren with easeoutright
    n "As [ch_ren] lifts himself from the back of the sofa, he makes sure to hand my cell phone back to me as well before heading off towards the kitchen."
    n "Now reunited with my beloved phone once more, I unlock it and check for any notifications."
    n "One update in particular lets me know that the security camera I ordered had been successfully delivered, and that alone makes me feel safe enough to return to my apartment; should I change my mind about staying here."
    n "With a satisfied hum, I quickly pocket my phone — lest I lose it again — and follow [ch_ren] into the kitchen."

    scene ren_kitchen_day
    show peffect
    play audio "audio/sfx/movement.ogg"
    show ren neutral at center
    with GlitchDissolve

    n "I watch as he turns on all the lights in there as well before he places the takeout on the countertop—"
    extend " and stops to sniff the air."
    n "Uh-oh."
    show ren sad at spop
    r "…What's that smell?"
    n "Oh, [shit]. I almost forgot about the ink I hastily threw away in the trash! In retrospect, I probably should've flushed it down the toilet or something instead."
    y "Oh! About that. I, um…"

    #hide ren with dissolve

    menu:
        #with dissolve
        "[rh_o]Be honest[rh_c]":
            $ affection_ren += 1
            $ affection_violet += 1
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_leon += 1
            show ren sad at center with dissolve
            n "I figure it'd be best if I simply come clean."
            n "After all, [ch_ren] didn't deserve to be lied to — much less have a guest he {b}trusted{/b} snoop through his belongings while he was away."
            n "Man, if only I could say the same thing about my stalker."
            n "Before I can dwell on it any further, [ch_ren]'s worried look pulls me from my thoughts and back to the present."
            n "Welp, here goes nothing."
        "Tell a white lie":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_jae += 1
            $ affection_kiara += 1
            show ren sad at center with dissolve
            y "Oh? Right, I noticed something funky-smelling as well."
            y "I must've stepped in something bad earlier… Sorry."
            show ren happy at spop
            r "Oh? I-I-It's okay! Don't worry about it."
            show ren flushed at spop
            r "Actually, you know what? I don't think I can smell anything weird at all!"
            n "[ch_ren]…"
            show ren happy at spop
            r "Yep, everything smells perfectly normal to me!"
            n "I watch in horror as his carefree smile fades the moment he opens the trashcan to throw away some rubbish."
            show ren sad
            n "I'm certain he notices the inky toilet paper sitting at the top of the pile, and it feels like an eternity before [ch_ren]'s gaze moves from the trash to land on me instead."
            n "He {b}still{/b} doesn't seem to react though, and before my guilty conscience can eat me alive, [ch_ren]'s voice breaks the silence."
            show ren flushed at spop
            r "Ah… Haha~ I guess I forgot to take out the trash this morning, too."
            show ren happy at spop
            r "S-Sorry you had to put up with that strong smell."
            n "…What? He must've known. Surely. He had every reason to call me out on my lie, yet… He didn't."
            n "Instead, [ch_ren] seemed to take on the blame with yet another carefree smile."
            n "Ah, forget it; maybe it was some form of righteousness, but I find myself confessing the truth."
        "Lie to him":
            $ affection_ren -= 1
            $ affection_teo += 1
            $ affection_olivia += 1
            show ren sad at center with dissolve
            y "Y-Yeah! I noticed that smell too when I first came in."
            y "I'm not really sure what it was."
            show ren flushed at spop
            r "Oh? M-Maybe I left a window open…"
            show ren frown at spop
            r "Or maybe it's the heating system? This is the first time I turned it on; maybe there's something funky in one of the vents."
            n "He glances up at the ceiling as if to inspect it, and I find myself following suit to make my fib seem believable."
            y "Yeah, m-maybe!"
            show ren sad
            n "But as [ch_ren] moves to throw away some discarded plastic left on the counter, his eyes catch sight of the inky paper sitting at the top of the rubbish."
            n "[shit!c]."
            n "He {b}still{/b} doesn't seem to react though, and before my guilty conscience can eat me alive, [ch_ren]'s voice breaks the silence."
            show ren flushed at spop
            r "Ah… Haha~ I guess I forgot to take out the trash this morning."
            show ren happy at spop
            r "Sorry you had to put up with that strong smell."
            n "…What? He must've known. Surely. He had every reason to call me out on my lie, yet… He didn't."
            n "Instead, [ch_ren] seemed to take the blame with a carefree smile."
            n "Ah, forget it; maybe it was some form of righteousness, but I find myself confessing the truth."
        "Don't say anything":
            $ affection_ren -= 1
            show ren sad at center with dissolve
            n "Figuring it's the best thing to do in this situation, I immediately clam up and inspect the threads of my shirt instead."
            n "Though it does me no favours as [ch_ren] {b}immediately{/b} picks up on my strange behaviour with a tilt of his head."
            show ren sad at spop
            r "[ch_angel!c]?"
            n "As he moves closer to my side, he casually opens the trashcan to discard some rubbish — only to notice the inky toilet paper sitting at the top."
            show ren sad
            n "I watch in horror as he takes in the sight before him, and I will the ground to open up and swallow me whole."
            y "I-I can explain—"
            show ren flushed at spop
            r "Ah… Haha~ I guess I forgot to take out the trash this morning."
            show ren happy at spop
            r "Sorry you had to put up with that strong smell."
            n "…What? He must've known. Surely. He had every reason to call me out on my lie, yet… He didn't."
            n "Instead, [ch_ren] seemed to take the blame with a carefree smile."
            n "Ah, forget it; maybe it was some form of righteousness, but I find myself confessing the truth."
        "{image=14NWY symbol} Distract him with a kiss" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
            call DLC_day4_renapartment from _call_DLC_day4_renapartment

    y "…I accidentally spilled some of your ink earlier."
    show ren sad at spop
    r "You… {i}What?{/i}"
    n "Everything now long forgotten; [ch_ren] rounds the corner within seconds and peers down at me with soft eyes."
    play audio "audio/sfx/item.ogg"
    show ren frown z at spop with dissolve
    r "Are you okay? It didn't stain you, did it?"
    show ren sad z at spop
    r "…Let me see?"
    n "He was still concerned about me? I watch as [ch_ren] reveals more of his hands from within the sleeves of his cardigan to hold and inspect my own."
    n "His blue eyes are full of concern as I feel the rough pads of his thumbs caress my skin. Once again, I'm reminded of the ring on his finger, and I can't help but ask…"
    y "That ring… It must be special to you, huh?"
    show ren sad z at spop
    r "My…ring?"
    n "[ch_ren] follows my gaze to his hand before awkwardly pulling away and scratching at his jaw."
    show ren flushed z at spop
    r "Y-Yes! It's… Um… It's a ring I made when I was younger!"
    show ren blushing z at spop
    r "I'm surprised you noticed it…"
    show ren neutral z at spop
    r "This ring… It means a lot to me. I don't know what I'd do if I lost it."
    y "It's very pretty."
    y "What about the one around your neck?"
    show ren flushed z at spop
    r "That's—!"
    n "[ch_ren] clams up the moment I meekly reach out to touch it, and he stares down at me with wide, cautious eyes."
    n "His own fingers wrap around my wrist — though he makes no effort to remove my hand from his necklace. In fact, he only seems to hold them in place as he peers at me."
    n "Feigning confidence, I run my fingers across the cold metal of his ring and take in all the small details."
    n "Much like the ring on [ch_ren]'s finger, the one around his neck also had a handmade feel to it — if the faint scratches and chips were anything to go by — though the craftsmanship was no less impressive."
    n "There also seems to be some kind of inscription inside the ring, but it was difficult for me to read due to the glare coming from the kitchen light."
    n "Part of me wants to pull it closer to get a better view, though I doubt it'd be a good idea to yank [ch_ren] down by his necklace — especially considering how he was {b}already{/b} hunching over enough as it is."
    n "Still, I couldn't stop my budding curiosity from putting one of my fingers inside the ring to see if it'd fit."
    n "And almost immediately, [ch_ren] stumbles forward as his fingers gently squeeze my wrists."
    show ren smirk z at spop
    r "D-Do you… D'you wanna try it on—"
    play audio "audio/sfx/thunder.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show ren frown at bpop with dissolve
    show ren frown with vpunch
    n "Before [ch_ren] can speak, a loud booming sound erupts from outside the apartment and startles the both of us."
    n "Man, was it {b}seriously{/b} about to start raining again?!"
    y "You're joking…"
    n "With a sigh, I abruptly pull away and glance out one of the large ceiling-to-floor windows. Dark clouds were rolling in from the distance, though there weren't any telltale signs of rain — yet."
    n "Though… The ominous black smoke was new. I didn't know the condensation got this bad — we weren't even that high up for fog to appear."
    n "Was this some kind of sign?"
    n "Still… It wouldn't do to be stuck waiting out yet {b}another{/b} storm again, so I glance in [ch_ren]'s direction and offer a sympathetic smile."
    y "Maybe I should head home before it starts raining."

    #hide ren with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "[rh_o]Go home[rh_c]":
            $ choice_style = "default"
            $ affection_ren += 10
            $ persistent.d4_visitangel = True
            show ren neutral at center with dissolve
            n "Yeah, It's probably best for me to go home before that storm gets any worse. I still had to go back to work tomorrow anyway."
            y "Thanks for today, but I should probably start heading back now."
            show ren happy at spop
            r "O-Oh, it's really no problem!"
            show ren neutral at spop
            r "Here, why don't I put your food in another bag and drop you off?"
            y "Are you sure? I don't want to be a bother…"
            show ren smirk at spop
            r "You'd never be a bother to me."
            n "Tapping the table, [ch_ren] pushes himself up and sets off to find something to put my takeout in."
            n "…What did I do to deserve someone as kind as [ch_ren]?"
            n "With a smile of my own, I get up from the stool and slowly make my way towards the entrance once more — but not before throwing [ch_ren] one final compliment."
            y "It's great that I can rely on you for anything."
            show ren flushed at spop
            r "…"
            show ren lovesick at spop
            r "{size=-6}H-Haaah… Hahah~{/size}"
            show ren happy at bpop
            r "I-I mean—! Of course."
            jump day4_gohome
        "[de_o]Stay the night[de_c]":
            $ choice_style = "default"
            show ren sad at center with dissolve
            n "It's probably best for me to just wait out this storm somewhere safe. If [ch_ren] was willing, I wouldn't mind spending the night here."
            y "Actually… Would it be okay if I crash at your place tonight?"
            n "His gaze was still on the black smoke outside the window, and it took a gentle nudge and the mention of his name to get [ch_ren]'s attention once more."
            show ren sad at spop
            r "…Why is it—? I-I haven't done any—"
            show ren frown at spop
            r "O-Oh, um…"
            show ren happy at spop
            r "I mean— Yes! Of course! It's no problem!"
            show ren neutral at spop
            r "I'll, uhh… I'll go get your stuff set up right now. Here, go ahead and start eating while I go… prepare your room."
            y "Thanks, [ch_ren]."
            y "It's great that I can rely on you for anything."
            show ren flushed at spop
            r "…"
            show ren lovesick at spop
            r "{size=-6}H-Haaah… Hahah~{/size}"
            show ren blushing at bpop
            r "I mean—! Y-Yeah, 'course! Y'can rely on me to… t'keep you safe."
            n "His cheeks immediately flush at my words, but I could tell that something was {b}still{/b} troubling him."
            n "Though before I get the chance to ask, he's {b}already{/b} leaving the kitchen and meandering down the hallway."

            play audio "audio/sfx/walking.ogg"
            hide ren with easeoutleft

    scene ren_lounge_day
    show peffect
    with dissolve
    show ren blushing at center with easeinright

    n "But just as [ch_ren] passes by the couch, I notice how his gaze shifts to his little art station hidden in the corner of the lounge room. He casts a curious glance in my direction before taking a step towards it."
    show ren sad at spop
    r "Did you… Was that where you spilled the ink?"
    y "Sorry. I-I didn't mean to."
    y "And it wasn't like I was going through your stuff! I only looked at the table, I promise."
    show ren frown at spop
    r "I-I see… So that explains why it's—"
    show ren neutral
    n "With an unreadable expression, [ch_ren] switches from looking impassive to determined in a matter of seconds."
    play audio "audio/sfx/paper.ogg"
    n "He reaches for something on the table — though it was hard to see what it was from where I was sitting in the kitchen."
    show ren neutral at spop
    r "You keep on eating. I'll join you shortly."
    n "And with that, he disappears into the darkness of his apartment."

    scene ren_kitchen_day
    show peffect
    with dissolve

    n "Deciding there's no use in overthinking his eccentric reactions (or dwelling over the fact that I got caught red-handed for being nosy), I pick up a fork and begin to dig in to my food."
    n "The taste of something both sweet {b}and{/b} savoury floods my tastebuds, and I let out a pleased hum."
    n "Man, was takeout {b}always{/b} this good? It only takes three more modest bites before I practically scarf down my meal. The flavour was immaculate, and I made a mental note to ask [ch_ren] what exactly he ordered the moment he returns."
    n "But now that I think about it… It'd been a while since he left, and [ch_ren] still hasn't come back yet."
    n "It'd surely been more than twenty minutes by now, and his food was starting to grow cold."
    n "…Was he really mad after all? Or maybe he needed help?"
    n "Whether or not it was the guilt still ebbing and flowing inside of me, I put my food aside and try to locate the eccentric guy in his stupidly large apartment."

    if persistent.imgdistortion == True:
        scene ren_misc_night
    else:
        scene ren_misc_night:
            parallel:
                function WaveShader(1.0,7.0,0.05)
    play music "audio/bgm/Lonely Doll.ogg" fadein 1 fadeout 1
    show peffect
    with dissolve

    n "But as I tiptoe down the hallway, the very same black smoke from earlier rolls out from underneath one of the doors — making my mind grow fuzzy and my legs feel like jelly."
    y "Wh-What the—?"
    n "Confused and slightly dazed, I lean against the wall for support and weakly call out [ch_ren]'s name."
    n "…What was happening to me?"
    n "A lurching feeling settles within the pit of my stomach, and just before I topple over; strong, scarred arms reach out and catch me."

    jump day4_deadend

################################################################################
## REN TAKING ANGEL HOME SCENE
################################################################################
label day4_gohome:
    scene oh_complex_night
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/shoes alt.ogg"
    play audio "audio/sfx/movement.ogg"
    show peffectp
    show ren neutral at center
    with Fade(1.0, 2.0, 1.0)

    $ location_moth = "home"
    $ location_violet = "home"
    $ location_elanor = "home"
    $ location_ren = "home"
    $ location_conan = "home"
    $ location_jae = "home"
    $ location_leon = "home"
    $ location_teo = "home"
    $ location_olivia = "home"
    $ location_kiara = "home"

    n "The ride back to my place was nothing short of ominous. The looming clouds on the horizon made the scenery seem dark and eerie, but thankfully [ch_ren] and his pastel-coloured hair were there to brighten things up."
    n "He even offered to walk me to my door, and what greeted the both of us was a single package on top of my doormat."
    n "Panic flashes through me at the thought of it being another \"gift\" from my supposed stalker, but then I remembered the purchase I made this morning and the notification I received on my phone."
    n "Ah, that must be my security cameras."
    n "Deftly picking it up, I put it under an arm as I fish for my keys in one of my pockets. I can sense [ch_ren]'s eyes on me — or rather, my package — but even as I glance in his direction, I can tell that he's trying to hold himself back from asking."
    n "…Surely there wouldn't be any harm in telling him?"
    
    label day4_gohomebranch:
    y "Oh, I bought a security system this morning. B-Because of how shady this neighbourhood is."
    y "I figured it'd be a good idea to be safer than sorry."
    show ren sad at spop
    r "…That creep didn't come back, did they?"
    play audio "audio/sfx/item.ogg"
    n "Without thinking, I drop my keys and slap a hand over [ch_ren]'s mouth before cautiously looking over my shoulder." with vpunch
    show ren flushed at bpop
    r "Mmph!"
    n "Ugh, what was I doing?! I was getting worked up and acting paranoid again."
    n "With an embarrassed look, I turn back to apologise to [ch_ren] — only to find his cheeks a deep red and a hand wrapped around my wrist."
    n "When did he…?"
    show ren smirk at spop
    r "…"
    n "Quickly withdrawing my hand, I squeak out an apology before picking up my keys and turning back to my door. I still didn't want to get [ch_ren] involved with my problems, but I honestly didn't want to risk being alone tonight, either."
    play audio "audio/sfx/item.ogg"
    show ren sad z at spop with dissolve
    n "Too lost in my own world; I barely notice [ch_ren] coming closer — nor his hand covering my keys to steady my fidgeting."
    show ren smirk z at spop
    r "Do y'want some help?"
    n "He must've seen the look of confusion on my face since he continues talking."
    play audio "audio/sfx/shoes alt.ogg"
    if d2_visitren == True:
        show ren flushed at bpop with dissolve
        r "S-S-Setting up your cameras, I mean! Self-taught programmer, remember?"
    else:
        show ren flushed at bpop with dissolve
        r "S-S-Setting up your cameras, I mean! I'm pretty good with tech."
        show ren neutral at spop
        $ persistent.fact_job = True
        r "I guess you could say I'm a… programmer, of sorts."
    
    show ren happy at spop
    r "I'm sure I can figure it all out. Plus, it'd save you having to call someone to install them."
    n "He {b}did{/b} have a point. And… I'd honestly feel safer if I weren't alone tonight. Still, I'd been spending so much time with [ch_ren] lately, and I didn't want him to get fed up with me and my presence."
    n "…Would it be a good idea?"

    #hide ren with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "[rh_o]Accept and let him stay the night[rh_c]":
            $ choice_style = "default"
            $ affection_ren += 1
            show ren happy at center with dissolve
            n "Maybe it would be a good idea after all."
            jump day4_acceptoffer
        "Decline and say goodnight":
            $ choice_style = "default"
            $ affection_ren -= 1
            show ren neutral at center with dissolve
            n "No, I didn't want to risk it."
            jump day4_declineoffer

################################################################################
## ACCEPT
################################################################################
label day4_acceptoffer:
    $ d4_inviteren = True
    $ unlock_security = True
    y "…Would you mind?"
    n "I probably look pathetic with how I barely make any eye contact; instead choosing to stare at my door rather than [ch_ren]. But he doesn't seem to mind — or perhaps he simply chooses not to comment on it."
    show ren smirk at spop
    r "I'd be happy to, Angel."
    n "With a smile, I open the door and let [ch_ren] inside."

    scene angel_lounge_night
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/door.ogg"
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show peffectp
    with fade

    if d2_visitren == True:
        show ren smirk at spop, center with dissolve
        r "…Y'know, I think we have the same mirror."
        y "Oh?"
    elif d1_inviteren == True:
        show ren smirk at spop, center with dissolve
        r "Still okay f'me to leave my shoes here?"
        y "Yeah! Go ahead."
    elif d1_inviteren == False:
        n "I watch as he awkwardly shuffles about in the hallway, almost uncertain if he should come inside or not. He moves to take off his shoes, and I watch in awe as he neatly stacks them next to the umbrella rack."
        show ren flushed at bpop, center with dissolve
        r "Oh— Are you the type to leave your shoes on at home? S-Sorry! I'll—"
        y "No, no, you're fine!"
        n "Ugh, he really was adorable."
    else:
        show ren smirk at spop, center with dissolve
        r "It's really nice spending time like this with you, Angel."
        n "Haha, where's all this coming from?"
        n "I-I'm just feeling sentimental, I guess."
    
    n "Putting the small talk aside for a moment, I usher the pink-haired person into my living room and situate ourselves on the couch."
    n "[ch_ren] wastes no time in opening my package, placing all the bits and pieces on the table, and setting off to work — though every so often he'd sneak a peek in my direction whenever he thinks I'm not looking."
    n "…Did he want something?"
    
    if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
        call DLC_day4_angelapartment from _call_DLC_day4_angelapartment
    else:
        n "Raising a brow, I send him a silent question."

    if d3_inviteren == False:
        show ren flushed at bpop, center
        r "I don't mean to pry into your personal life, but…"
        show ren sad at spop, center
        r "Y-You know, you're always welcome to stay at my apartment."

        if d2_visitren == True:
            show ren happy at spop, center
            r "I mean, you've already stayed the night at my place, so it wouldn't be a bother if you wanted to come over again."
        else:
            show ren neutral at spop, center
            r "I mean, you've seen my place already. And you're always welcome to stay— {i}especially{/i} if it's an emergency."

        show ren smirk at spop, center
        r "I'd honestly sleep better at night knowing you're safe."
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

        if d1_inviteren == True:
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
        n "…Rats? Where was this coming from?"
        n "I won't lie though, [ch_ren]'s offer honestly was tempting."
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
        n "But before I can dwell on it any further, I watch as he leans over to reach into his back pocket and pulls out something that resembles a plastic card."
        n "[ch_ren] wastes no time handing it to me, and I take a moment to look it over."
        n "His address and unit number are neatly printed at the top, and some kind of obscure barcode is on the bottom."
        n "However, the apartment name and logo in the top right corner are what {b}really{/b} captures my attention."
        n "\"Sunshine Hills\"…? I almost forgot he lived in the nicer parts of Corland Bay."
        n "They were known for their high-rise apartments and fancy penthouses, so I'm sure [ch_ren] never had to worry about rat infestations or deadbeat landlords."
        n "Though… The more I thought about it, the more willing I was to accept his offer."
        n "Maybe it wouldn't be such a bad idea after all?"
        n "I couldn't help but wonder what kind of programmer could afford fancy marble flooring — but as always — [ch_ren] remained a mystery to me."
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
        r "After seeing what's been on the news lately, I just want you to be safe."
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
        n "As if picking up on my sudden silence, he clears his throat and gestures towards the items still laid out on the table in front of us."
        show ren flushed at spop, center
        r "Anyway! W-We should… {i}I{/i} should finish setting up your cameras."
        y "Oh… yeah! You're right."
        n "He goes quiet after that."
        n "Picking up the manual, [ch_ren] tries to busy himself with learning how to connect the cameras to my Wi-Fi — before tossing it aside and doing it {b}his{/b} own way."
    else:
        show ren flushed at bpop, center
        r "I-I don't mean to pry into your personal life, but…"
        show ren sad at spop, center
        r "You know, you're always welcome to stay at my apartment."
        y "[ch_ren], I've seen where you live. I doubt I could afford rent."
        show ren happy at spop
        r "You could stay for free! I don't mind at all!"
        show ren neutral at spop
        r "And I-I'm more than capable of covering your cost."
        show ren happy at spop
        r "I'd make a really good roommate, too! I always clean up after myself, and I wouldn't mind doing the same for you as well."
        show ren neutral at spop
        r "O-Only if you'd be fine with it, though."
        show ren flushed at spop
        r "And… I can cook as well! Laundry, cleaning, repairing things around the house… Uhh… Yardwork? I can do it all for you! Really!"
        y "Wait… you have a yard?"
        y "Man, they can really fit a lot into those upscale apartments, huh?"
        show ren blushing at spop
        r "Well, no… I don't…"
        show ren happy at spop
        r "B-But I always did the gardening and used a lawn mower {i}a lot{/i} when I was younger. I'm sure I can figure it all out again."
        show ren flushed at spop
        r "Not that I'd need to, though! Like you said… No yard, haha…"
        y "Pfft! No offence [ch_ren], but I can't imagine someone like you mowing grass."
        y "Was that your first job as a teen?"
        show ren neutral at spop
        r "Before that, actually."
        y "Huh? Before that? You mean… as a child?"
        show ren sad at spop
        r "…Maybe a bit younger?"
        y "Younger?!"
        show ren blushing at spop
        r "I mean— J-Just kidding! Yeah, it… it {i}was{/i} my first job as a teenager! Hahaha!"
        show ren flushed at spop
        r "A-Anyway, the point is, I'd be happy to let you stay at my place."
        y "…Oh? Well, I really appreciate the offer [ch_ren], but I gotta tough this one out on my own."
        show ren sad at spop
        r "O-Oh! …If you say so."
        n "He goes quiet after that."
        show ren neutral
        n "Picking up the manual, [ch_ren] tries to busy himself with learning how to connect the cameras to my Wi-Fi — before tossing it aside and doing it {b}his{/b} own way."

    n "Deciding not to get in the way, I curl up on the couch with my food and simply observe him."
    n "I won't lie; watching [ch_ren]'s hands deftly connect cables and unscrew plates was kind of attractive, but I wasn't about to say anything."
    n "And soon enough, the events of the evening slowly draw out as I start to feel the telltale signs of weariness take hold of me."
    n "I try my best to muffle my yawn before I glance up at the clock on my wall to read the time. Just past midnight."
    n "[damn!c], I hadn't realised we'd been at this for so long."
    show ren smirk at spop
    r "Tired?"
    n "[ch_ren]'s voice startles me, and I glance back to see that he had already put down the cameras and was reclining in his seat to fully look at me."
    y "Kinda. It's been a long day."
    show ren neutral at spop
    r "Y-You can head to bed if you want. I'll set this all up and lock up once I'm done."
    y "You're still going to go home after this?"
    show ren blushing at spop
    r "…Y-You want me to stay?"
    n "Did I? Strange. Perhaps it was because we'd been spending so much time together, but I'd somehow grown fond of [ch_ren]'s presence."
    n "It was… comforting to have him near — though I wasn't about to tell that to him. So, with an affirmative nod, I make the decision."
    y "Yeah. I do."
    show ren flushed at spop
    r "{i}Oh.{/i}"
    n "[ch_ren]'s grin practically reaches his ears as he laughs to himself."
    show ren happy at bpop
    r "Okay!"
    show ren neutral at bpop
    extend " Sure!"
    show ren happy at bpop
    extend " No problem!"
    n "I can't help but playfully roll my eyes at his enthusiasm."
    y "Well then. Why don't I get some pillows and blankets and we can camp out here for the night?"
    show ren happy at spop
    r "Haha, just like a sleepover?"
    y "Sure."
    n "His toothy grin reminds me of my childhood days — back when I'd beg all the adults to let some of my friends from school stay the night."
    n "With all of us wrapped up in patterned blankets, I'd cuddle up on the couch with everyone until we'd all fell asleep. But it wasn't [ch_leon] who came to mind. It was…"
    n "Someone else?"
    n "Their face was blurry, but I could make out tufts of black hair from within the blankets surrounding us… and the same toothy grin [ch_ren] was giving me."
    show ren sad
    n "But when I focus my attention back on him, I notice that the smile is gone, and he's instead looking at me with a confused look on his face."
    n "Ah, I must've been spacing out again."
    y "S-Sorry! I'll, uhh— I'll go get those pillows now."
    show ren happy at spop
    r "Let me know if you need any help!"
    n "[ch_ren]'s response gets drowned out as I flee into the hallway."

    scene other_dark
    play music "audio/bgm/Touch Your Heart.ogg" fadein 1 fadeout 1
    show peffectp
    with GlitchDissolve

    n "It took a while, but [ch_ren] managed to set the cameras up and hook it all up to an app on my phone — all while I made myself comfortable on the couch."
    n "He explained how to use it, but if I were being honest, I started to nod off once he started geeking out about the different kinds of alarm buttons."
    n "Before I know it, my head falls onto his shoulder with a soft thump, and I feel [ch_ren]'s body shake as he lets out a faint laugh. Something moves from the chair next to him before a warm duvet is wrapped around my shoulders."

    if hair_texture == "bald" or hair_texture == "braided":
        n "I can feel [ch_ren] pull me to his side before we both fall backwards onto the couch. His chest softens the blow, and with one of his hands gently tracing over the back of my neck, I slowly start to drift off."
    else:
        n "I can feel [ch_ren] pull me to his side before we both fall backwards onto the couch. His chest softens the blow, and with one of his hands gently threading through my hair, I slowly start to drift off."
    
    n "Nostalgia greets me once more, and before my consciousness fades away, I try to chase after the foggy memory that had been plaguing my brain as of late."
    n "Those three kids laughing and playing together near a lake… Who were they?"
    n "And who was the one that stayed right by my side even after everyone else went home?"
    n "Almost desperately, I try and recall their face — or any of their defining features, really. At this point, I'd take anything."
    n "But it's all for naught when I feel [ch_ren]'s lips fall to the crown on my head to place a chaste kiss."
    r "Sleep well, [ch_angel]."
    n "With his comforting voice in my mind, I slowly start to slip away."

    jump day4_ending_good

################################################################################
## DECLINE
################################################################################
label day4_declineoffer:
    y "I really appreciate the offer, [ch_ren], but I gotta tough this one out on my own."
    show ren flushed at spop
    r "O-Oh! …If you say so."
    n "His concern for my well-being is evident, but I didn't want to get him involved. This was {b}my{/b} problem, and I would handle it all on my own."
    n "Still, part of me knew I wouldn't hesitate to call him if something went wrong."
    n "After spending so much time with [ch_ren], I'd grown to appreciate his company. Something about him felt so… comforting to me."
    if d4_altroute == True:
        y "A-Anyway! You should probably head home before the storm comes. Thanks for dropping off my phone— and for the food."
    else:
        y "A-Anyway! You should probably head home before the storm comes. Thanks for dropping me off— and for the food."
    n "I make sure to lift up the bag full of takeaway for him to see."
    show ren flushed at spop
    r "Of course! Thanks for… Um… Paying for my ticket?"
    y "You can thank [ch_teo] for that."
    show ren happy at spop
    r "Haha~ I think I'll pass."
    n "[ch_ren]'s face playfully scrunches up at the mere mention of [ch_teo], and I find myself letting out a small chuckle before unlocking my front door and stepping into my apartment."
    y "Well, I should probably go get this camera set up and head to bed. Stay safe on your drive back."

    if d3_inviteren == True:
        show ren flushed at spop
        r "Y-You too! Or— Well, you're not driving anywhere, so… Dream safe!"
        show ren blushing at spop
        r "Ah-! I mean… Drive sleep!"
        show ren sad at spop
        extend " Stay well?"
        show ren flushed at spop
        r "Ugh, I {i}still{/i} can't get this right…"
        y "Pfft. Goodnight, [ch_ren]."
    else:
        show ren smirk at spop
        r "I will! Sleep well, Angel."
        y "You too! Goodnight, [ch_ren]."
    
    hide ren with dissolve
    n "I send him off with a smile before closing the door."
    
    scene angel_bedroom_night
    $ unlock_security = True
    play music "audio/bgm/Touch Your Heart.ogg" fadein 1 fadeout 1
    show peffectp
    with GlitchDissolve
    
    n "It takes me a while and countless online video tutorials, but I somehow managed to set up the security cameras and connect them to an app on my phone without {b}too much{/b} trouble."
    n "It would alert me of any unusual activity and movements when I'm not home, and I felt immensely safer because of it."
    n "Though I still had faith that my new lock {b}hadn't{/b} been tampered with since I got it, considering how the letter had been shoved underneath the door rather than being placed on something as conspicuous as a table."
    n "…If I had found it on my bedside table instead, I definitely would've felt true fear."
    n "Ugh. I was getting worked up again."
    n "If I continued to think about this any more than I should, I swear I would start to go crazy."

    scene angel_bed_night
    show peffectp
    with dissolve

    play audio "audio/sfx/item.ogg"
    n "Deciding that this was a problem for future me, I lock myself in my bedroom and hide within the safety of my duvet."
    n "A faint glow emits from my phone as I check to make sure I have all the angles in my apartment covered. Satisfied with my handiwork, I lay back on my bed and idly zoom in and out with one of the camera screens until I grow bored."
    n "I doubt I'd be able to fall asleep quickly, but it wouldn't hurt to try."
    n "Besides, I had to be up bright and early for work tomorrow."
    n "With that thought in mind; I lock my phone, shove it under one of my pillows, and will myself to fall asleep."
    n "…"
    n "Nostalgia greets me like an old friend, and before my consciousness fades away, I try to chase after the foggy memory that had been plaguing my brain as of late."
    n "Those three kids laughing and playing together near a lake… Who were they?"
    n "And who was the one that stayed right by my side even after everyone else went home?"
    n "Almost desperately, I try and recall their face — or any of their defining features, really. At this point, I'd take anything."
    n "The faintest recollection of pudgy cheeks, twin pigtails, and a frowning expression swirls in my mind, but it slips away the moment I drift further into dreamland."

    jump day4_ending_good

################################################################################
## BRANCH SPLIT
################################################################################
label day4_closetbranch:
    y "C'mon [ch_teo], this is a stupid idea."
    show teo frown z at spop
    t "Stupid? You're joking."
    y "Look. As much as I want to help you out, I don't really think this is going to accomplish… well, anything."
    y "Besides, it doesn't seem fair to [ch_elanor] either."
    show teo angry z at spop
    t "…"
    show teo sad z at spop
    t "Is that what you really think?"
    show teo frown z at spop
    t "Fine, whatever. I should've asked Buttercup to help me instead."
    show teo angry z at spop
    t "…Got anything else to add? If not, let's head back."
    n "Without another word, [ch_teo] drops his hand and walks away — leaving me to trail behind."

    scene aquarium_foodcourt_day
    show peffect
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show ren frown at cleft
    show teo frown at cright
    show elanor happy at center
    with Fade(1.0, 1.0, 1.0)

    show elanor happy at spop
    e "There you two are! Enjoy your little chat?"
    show teo angry at spop
    t "…Sure."
    show elanor sad at spop
    e "Is… Everything alright?"
    show teo frown at spop
    t "Just peachy."
    n "[ch_teo] shoots a wry glance in my direction as if to say, \"See? I told you so\", but I brush it off with a sigh."
    show elanor frown at spop
    e "[ch_teo]? [ch_angel]?"
    show ren sad at spop
    r "Um…"
    n "While [ch_elanor] shuffles awkwardly on the balls of her feet, [ch_ren] nudges my side and leans closer."
    show ren neutral at spop
    r "Are you alright, Angel? D-Did [ch_teo] do anything to you?"
    y "No, I'm fine. Don't worry about it."
    show ren sad at spop
    r "Y'sure? Because if he did…"
    y "Hm?"
    show ren smirk at spop
    r "…No, never mind."
    n "At that, [ch_ren] takes a step back and looks at my co-worker with a bright smile."
    show ren happy at bpop
    r "S-So! About that food…?"
    show elanor happy at spop
    e "Oh, that's right! Thank you for reminding me, [ch_ren]."
    show elanor neutral at spop
    e "Here! I'm sure we'll all start to feel better again once we've had something to eat. I hope you like adobo as much as me."
    show teo neutral at spop
    t "…Adobo? Is that foreign?"
    show elanor happy at spop
    e "Why, yes! It's a dish that mainly features chicken and rice, which I figured would be beneficial for you — given your build, and all."
    show teo smirk at spop
    t "Interested in my body, are you?"
    show elanor flushed at spop
    e "{size=+6}N-No!{/size}" with vpunch
    show elanor sad at spop
    e "Erm— Well… {i}Yes{/i}, technically. But only because I'm concerned about your dietary requirements. You look like the type of person who takes care of their health."
    show elanor happy at spop
    e "And my sister — [ch_kiara] — she was the one who introduced this dish to me while she was travelling abroad. I really think you'll enjoy the taste."
    show elanor neutral at spop
    e "It's one of her top ten favourite foods!"
    show teo frown at spop
    t "…Your sister again? Really?"
    show teo angry at spop
    t "Ugh. Sure. Whatever you say, Princess. Hand it over."
    n "With a groan, I knock my elbow against [ch_teo]'s arm. Yet all it does is make him give me {b}yet another{/b} one of those pointed looks."
    show elanor smirk at spop
    e "Erm— A-Anyway! Here, [ch_angel]! I bought you the same thing as [ch_ren]. I hope that's okay with you."
    show elanor happy at spop
    e "He was telling me aaaaall about how much you enjoy [favourite_snack]s earlier."
    show ren angry
    n "But before I can take the takeaway bag from her grasp, [ch_elanor] loops her arm in mine and tugs me away from the group."
    n "There's a cheeky grin on her face, which could only mean one thing…"
    show elanor smirk at spop
    e "Buuuut first… What did you two have to talk about?"
    n "…And there it was."
    n "Once my gossipy co-worker got started, there was no holding her back."
    y "Uhh… Nothing important. [ch_teo] just needed some… help with something."
    show elanor neutral at spop
    e "Oh? Is everything alright now?"
    n "I watch as [ch_elanor] peers over my shoulder to look at [ch_teo]—"
    extend " who was still within earshot. [shit!c]."
    show elanor sad at spop
    e "Does he still need help? I can go and find another staff member if you—"
    show teo angry at spop
    t "Forget it. This is starting to get real annoying now."
    show elanor sad at spop
    e "…Oh."
    y "[ch_teo]!"
    show ren sad at spop
    r "U-Um—"
    show teo frown at spop
    t "Move."
    play audio "audio/sfx/shoes alt.ogg"
    show teo behind elanor at tleft with easeinleft
    show ren angry at bpop with hpunch
    hide teo with easeoutleft
    show ren at tleft
    show elanor at tright
    with easeinright
    n "[ch_teo] doesn't wait for a response as he shoulders past [ch_ren] and makes his way towards one of the exits."
    show elanor frown at spop
    e "Did I say something wrong?"
    y "No, Norie—"
    show elanor sad at spop
    e "Perhaps I should go and apologise…"
    y "No. You didn't do anything wrong. Here, {i}I'll{/i} go and talk to him. You stay here with [ch_ren]."
    show elanor frown at spop
    e "Wait—"
    show ren frown at spop
    r "Y-You don't have to, [ch_angel]…"
    n "Before I can follow after [ch_teo], I feel someone tug at the sleeve of my jacket."
    y "…[ch_ren]?"
    show ren sad at spop
    r "You don't have to go after [ch_teo]. Just leave him."
    y "Maybe you're right… But I know [ch_teo] better than everyone else here, and I know he's only going to sulk and be a pain about it for the next few days."
    y "It's probably best if I do something about it now, otherwise we'll just suffer for it later. You guys {i}reeeally{/i} don't want to see a mopey [ch_teo]."
    show ren happy at spop
    r "Here, I'll come with you then—"
    show ren sad
    y "No, it's okay. You stay here and enjoy the rest of the day with [ch_elanor]."
    y "Besides, didn't you two hit it off back at the library? I'm sure she won't mind, right El?"
    show elanor flushed at spop
    e "Oh— R-Right!"
    show elanor happy at spop
    e "I do hope I didn't bore you to death with all my talk about native flowers."
    show ren frown at spop
    r "…What? I mean— N-No! Nope! Not at all. But…"
    show ren sad at spop
    r "Angel, did it really look like that to you? Because—"
    n "Before [ch_ren] can finish his sentence, my eyes wander towards [ch_teo]'s figure slipping through a crowd of people as he pulls out his phone. And before I realise it, my feet start to move on autopilot as I chase after him."
    y "Sorry, but I really need to— Ack, he's already gone! Uh…"
    y "I'll be back! Promise!"
    
    scene other_dark
    play audio "audio/sfx/sprinting.ogg"
    show peffectp
    with GlitchDissolve

    n "Now leaving the two of them behind, I make my way towards the opening of the food court and through the seemingly endless maze of fishtanks."
    n "Pushing open the heavy doors to back entrance, I aimlessly peer down the alleyway in search for my grumpy (and perhaps even childish) friend."
    n "My instincts tell me to head towards the hustle and bustle of the main street, but as I round the corner, I bump into someone's chest."

    scene beach_street_day
    show peffect
    show leon sad z
    play ambience "audio/ambience/street.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/walking.ogg"
    with fade

    play audio "audio/sfx/item.ogg"
    play audio ["<silence 0.2>", "audio/sfx/shoes alt.ogg"]
    show leon sad at bpop with vpunch
    l "Woah, sorry! Guess I wasn't looking where— Wait… [ch_angel]?"
    y "[ch_leon]?! What are you doing here?"
    y "I-I was just about to g—"
    show leon neutral at spop
    l "Go after [ch_teo]? Haha, it might be best to let him cool off a bit, yeah?"
    show leon frown at spop
    l "I just saw him sulk off in that direction. Plus, he seemed kinda… off in the group chat."
    y "Yeah, I figured he'd message you guys."
    show leon happy at spop
    l "Well actually… He messaged [ch_jae], who then messaged me — but he sent it to the wrong chat — so now… Here I am!"
    show leon neutral at spop
    l "I was on my way back from the hospital, anyway. I figured I'd pop in and see what was up."
    y "Well, I guess now you know…"
    show leon happy at spop
    l "Pffft, yeah, I suppose!"
    show leon neutral at spop
    l "But… Look. Seeing as [ch_jae]'s aware of everything now, maybe it's best to let {i}him{/i} handle [ch_teo], yeah?"
    y "You think so?"
    n "[ch_leon] gives me a non-comital shrug of his shoulders before gesturing for me to follow him."
    show leon smirk at spop
    l "It might help diffuse the situation. I mean, [ch_jae] has known him since elementary school. If he's able to put up with [ch_teo] for {i}that{/i} long, then I'm sure he'll be better help than us."
    y "Maybe you're right…"
    show leon neutral at spop
    l "Still not convinced? If you still want to go and talk to [ch_teo], we can. I don't mind tagging along and—"
    y "No, it's just… I can't help but feel like this is all somehow my fault."
    y "I mean, I {i}know{/i} it's not, but…"
    show leon sad at spop
    l "You know how [ch_teo] can get. Especially when he's told not to do something."
    y "Yeah, but I can't help but wonder if I could've been nicer about it… More kinder? I didn't think he'd react this way when I told him not to—"
    show leon neutral at spop
    l "Nah, I think this is what [ch_teo] needs."
    show leon sad at spop
    l "He doesn't show it, but he's always been coddled by everyone — even his parents. And all those people he hangs out with in the city? I can almost see where he gets his mindset from."
    show leon frown at spop
    l "[ch_teo] never used to be like this, y'know? Back when we were younger."
    show leon sad at spop
    l "But… I guess this is what happens when you've been denied genuine attention for most of your life."
    show leon frown at spop
    l "He doesn't know how to handle someone telling him \"no\" whenever he does something crazy, but it's not entirely his fault."
    show leon sad at spop
    l "Aside from his… questionable friends, [ch_teo] also grew up with distant parents. Whenever he wanted affection from them, he'd often have to do something brash just to get their attention."
    show leon frown at spop
    l "But it never lasted long. They'd just throw money in his direction and eventually ignore him again. It's pretty sad, honestly."
    show leon neutral at spop
    l "I think… All he wants is for someone to actually acknowledge him for who he is — not how he acts."
    show leon sad at spop
    l "I'm sure you've noticed it, right? Everyone wants him for his money, looks, and popularity. I doubt he's got any {i}real{/i} friends. Y'know, aside from us."
    show leon happy at spop
    l "Oh— And [ch_jae], of course."
    show leon frown at spop
    l "Outside of our friend group, I doubt [ch_teo] surrounds himself with genuine, good-hearted people. I bet his mates from the city don't even have his best interests at heart."
    show leon smirk at spop
    l "But! Mushy rant aside; I'm glad you were able to be his voice of reason. After everything he's been through, he needs someone like you."
    show leon happy at spop
    l "Someone who'll stop him from doing things he'll regret later, and to keep him in line whenever he says something insensitive. A true friend."
    n "Wow… I honestly didn't know that about [ch_teo]… Or that [ch_leon] thought of me that way. I didn't even know how to respond."
    n "Though I guess I didn't need to, considering how [ch_leon] continued to talk."
    show leon neutral at spop
    l "But enough about him! [ch_jae]'s on his way back from the city now, so we should leave Mr Moody to him. Besides…"
    n "With a grin, [ch_leon] tosses an arm over my shoulder and pulls me onto the street."
    show leon happy at spop
    l "I wanna spend some time with you! I think it's long overdue, yeah? I mean, I never even got to go on that aquarium date with you guys…"
    y "Oh no… How dreadful!"
    show leon smirk at spop
    l "It's truly a heartbreaking thought… I don't think I'll be able to go on…"
    show leon sad at spop
    l "My heart yearns to be by your side, but alas… T'was not meant to be…"
    y "Pfft— Alright, let's go, theatre kid."
    show leon happy at spop
    l "Hahaha, what gave it away?"
    n "With a playful eye-roll, I nudge my childhood friend with my hip to get him moving again. But what takes me by surprise is how he casually grabs my hand in his and leads me down the street."
    play audio "audio/sfx/item.ogg"
    show leon happy z with dissolve
    n "This almost feels like old times; back when we used to run hand-in-hand towards our favourite playground after school."
    n "I wonder… Was [ch_leon] thinking the same thing as me?"
    n "But when I glance upwards to check, I instead take notice of the destination my companion was leading me towards. After all, the massive umbrella made it hard to miss."
    n "A soft smile pulls at my features from the nostalgic sight before me, and I give [ch_leon]'s hand a gentle squeeze to let him know about my excitement."
    n "I can feel him do the same to my hand in return — which only makes my grin grow even wider."
    y "An ice cream stand, huh?"
    show leon neutral z at spop
    l "Yeah! It's been a while since we've visited one of these, hasn't it?"
    y "That's true. I wonder if they still sell all those wacky flavours."
    show leon happy z at spop
    l "Hahaha! Did you just call my favourite flavour \"wacky\"? I can't believe it."
    y "Why, I would never!"
    show leon smirk z at spop
    l "Oh really? Do you even remember what it is?"
    y "Duh! It's…"

    hide leon with dissolve
    menu:
        "\"Vanilla!\"":
            show leon happy z with dissolve
            l "Haha, vanilla? I think that's a safe option, don't you?"
            y "I could've sworn I've seen you eat vanilla ice cream before!"
            show leon neutral z at spop
            l "Well, you're not wrong… You can't go wrong with vanilla! But… No, it's not my favourite."
            y "And what {i}is{/i} your favourite ice cream flavour?"
            show leon happy z at spop
            l "You'll wanna write this one down, but it's — drumroll please — neeeeapolitan!"
            show leon smirk z at spop
            l "Anyway, that doesn't matter right now 'cuz it's {i}your{/i} turn."
            y "…Huh? My turn? Oh!"
            y "Are you going to guess my favourite now?"
        "[rh_o]\"Mint choc-chip.\"[rh_c]":
            show leon happy z with dissolve
            l "Pfft! Mint choc-chip? You're pulling my leg!"
            y "…Wait, it's not?! I swear I've seen you eat it before."
            show leon smirk z at spop
            l "Nah. I only ate it because one of our old classmates didn't like ice cream. I didn't want her to feel bad about wasting food."
            show leon neutral z at spop
            l "But that's not the point. Because now it's {i}your{/i} turn!"
            y "…Huh? My turn?"
            y "Oh! Are you going to guess my favourite flavour now?"
        "\"…Neapolitan?\"":
            show leon happy z with dissolve
            l "You got it!"
            show leon neutral z at spop
            l "See? I knew you'd remember it! I never doubted you for a second, darl'."
            y "How could I forget? The only reason it's your favourite is because it's like… three flavours in one."
            show leon happy z at spop
            l "Exactly. And all for the same price as one, too!"
            y "That's kind of like… cheating, isn't it?"
            show leon smirk z at spop
            l "Oh yeah? That sounds more like jealousy to me."
            y "Oh please!"
            show leon neutral z at spop
            l "Don't worry, I wouldn't mind sharing my ice cream with you. Germs, too."
            y "Ew, gross!"
            show leon happy z at spop
            l "Gross?! Hahaha!"
            show leon smirk z at spop
            l "Anyway… Now it's {i}your{/i} turn."
            y "Huh? Oh!"
            y "Are you going to guess?"
        "\"I don't remember.\"":
            show leon happy z with dissolve
            l "Haha! That's okay, we were just kids at the time. I don't blame you for not remembering."
            y "Well, it might be a little late for this question now, but… What {i}is{/i} your favourite flavour, [ch_leon]?"
            show leon neutral z at spop
            l "Oh? Curious, are we? In that case…"
            show leon smirk z at spop
            l "You'll wanna write this one down, but it's — drumroll please — neeeeapolitan!"
            show leon neutral z at spop
            y "Not that {i}my{/i} favourite flavour matters right now though, 'cuz it's {i}your{/i} turn."
            y "…Huh? My turn? Oh!"
            y "Are you going to guess my favourite now?"

    show leon happy z at spop
    l "'Course I am! It's only fair. And also because… I remember your favourite flavour too."
    y "Is that so?"
    show leon neutral z at spop
    l "I mean, as long as it hasn't changed over the years."
    y "No, it's still the same."
    show leon smirk z at spop
    l "Then…"
    n "There was no way he was going to guess it correctly. But now that I think about it… What {b}is{/b} my favourite ice-cream flavour? I should probably have one in mind before he guesses…"
    hide leon with dissolve
    
    $ input_prompt = "What is my favourite flavour?"
    call screen screenput with dissolve
    if input_answer == "answer":
        $ favourite_icecream = "vanilla"
    else:
        $ favourite_icecream = input_answer
    $ input_answer = "answer"
    
    show leon happy z with dissolve
    n "But just as I think of my answer, [ch_leon] speaks it into existence with a knowing, toothy grin."
    n "The ringing of his laughter drowns out the ending of his response, but I heard him clear as day."
    y "How did you—?!"
    show leon neutral z at spop
    l "Sunfish, I think it's time I told you… I'm… a mind reader."
    y "Woah? What number am I thinking of right now?"
    show leon sad z at spop
    l "Uhh… Four? No, sixty? …Four point sixty?"
    y "Haha, what? That's such a specific number."
    show leon smirk z at spop
    l "Yeah? Well, that's how much we owe this fine gentleman."
    n "With a smile, he gestures towards the person who served us the ice cream. Not wanting to make the people in line wait any longer, I fish out the loose change [ch_leon] gave me earlier and pay for our desserts."
    n "Seemingly satisfied, we make our way down the footpath to find somewhere to sit and eat."

    scene beach_park_day
    play music "audio/bgm/Childhood Friend.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show peffect
    with Fade(1.0, 2.0, 1.0)

    $ persistent.d4_icecream = True

    n "Eventually, [ch_leon] leads me to a nearby park where we plop down on one of the benches and kick up our feet."
    n "We spend a long while just… chatting and catching each other up on all the things that happened in our lives during our time apart. And soon enough, all of our ice-cream is gone and the sun was slowly beginning to set."
    n "A comfortable silence blankets the both of us as [ch_leon] casually throws his arms behind his head and closes his eyes. He seems at peace like this; almost as if the stress of his day-to-day life had been stripped away."
    n "But even with [ch_leon]'s eyes closed… I couldn't help but feel like someone — or something — was watching me."
    n "An eerie feeling washes over me, and I cast a hesitant glance over my shoulder to spot anything out of place."
    n "Nothing but the gentle rustle of foliage in the wind greets me, and yet… I still couldn't seem to shake off the lingering feeling of something hiding behind one of the bushes."
    n "What if it was my…?"
    n "Ugh. Just as I was {b}finally{/b} starting to relax and unwind again, I went and ruined it all by getting worked up once more."
    n "Quietly slapping my cheeks, I try to expel those thoughts from my mind. But the sound I made must've been louder than it felt — because [ch_leon]'s golden eyes soon blink open to look in my direction."
    show leon flushed z with dissolve
    show leon flushed z at spop
    l "Heh, sorry. I almost dozed off there!"
    show leon neutral z at spop
    l "It's so peaceful out here, I could probably fall aslee—"
    show leon sad z at spop
    l "Woah? Check that out."
    n "I follow [ch_leon]'s finger towards the sky, only to notice ominous, dark clouds rolling in from the distance."
    n "You're kidding… Was it seriously about to start raining again?!"
    n "But now that I look closer… Do clouds normally get that dark? Even from afar, it almost looks like black smoke enveloping some of the taller buildings in the heart of Corland Bay."
    n "It almost seemed… unnatural."
    n "All too quickly, the soft timbre of [ch_leon]'s voice cuts through my thoughts."
    show leon sad z at spop
    l "As fun as today has been, we should probably head back before it starts [pissing] down buckets, yeah? Here, I'll walk ya home."
    play audio ["<silence 1.6>", "audio/sfx/thunder.ogg"]
    n "He offers a hand to help me up from the bench, and just as I take it, I hear a twig snapping from somewhere behind me. But before I can react, the muted sound of thunder cuts me off."
    y "Thanks [ch_leon], but your place is in the opposite direction, isn't it? I wouldn't want to make you walk all the way back."
    show leon neutral z at spop
    l "Nah, it'll be fine. I don't mind walking."
    y "What if it starts raining?"
    show leon happy z at spop
    l "A little rain never hurt anyone!"
    y "Something tells me it won't be a little bit of rain…"
    show leon frown z at spop
    l "Actually… Yeah, you may be right."
    y "Gasp… Me? Being right?"
    show leon happy z at spop
    l "Could it be…?! What date is it? Is there a blue moon?!"
    y "Haha! Knock it off."
    show leon smirk z at spop
    l "Heh."
    show leon sad z at spop
    l "But… Hey. Are you sure you don't want me to walk ya home?"
    y "I'm sure. Besides, I could use some alone time. The past few days have been hectic, to say the least."
    show leon neutral z at spop
    l "Yeah? Well, so long as you don't stress yourself out or anything. If you need to vent, you know who to call."
    y "[ch_teo]?"
    show leon happy z at spop
    l "Hahaha!"

    scene oh_complex_night
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    stop ambience fadeout 2.0
    show peffectp
    with Fade(1.0, 1.0, 1.0)

    $ location_moth = "home"
    $ location_violet = "home"
    $ location_elanor = "home"
    $ location_ren = "oh"
    $ location_conan = "home"
    $ location_jae = "pier"
    $ location_leon = "home"
    $ location_teo = "pier"
    $ location_olivia = "home"
    $ location_kiara = "home"

    n "Despite saying that I'd be perfectly fine walking home on my own, [ch_leon] ended up accompanying me to the entrance of my apartment complex before {b}finally{/b} parting ways."
    n "It was… nice being able to catch up with him like this, and I genuinely find myself wondering if we could do it again in the future."
    n "But as I make my way towards my door, my eyes wander towards the small box sitting atop my doormat."
    y "…What the?"
    n "Panic flashes through me at the thought of it being another \"gift\" from my supposed stalker, but then I remembered the purchase I made this morning."
    n "Ah, that must be my security cameras."
    stop music fadeout 4
    n "Deftly picking it up, I put it under an arm as I fish for my keys in one of my pockets. But as I do so, I barely make out the sound of something behind me."
    play music "audio/bgm/Lonely Doll.ogg" fadein 1 fadeout 1
    n "Muffled footsteps echo from somewhere down the stairwell, indicating that someone was there — and that they were getting close."
    n "The thought alone sends a surge of panic through my body as I tense up."
    n "Was that…?"
    n "I desperately try to ignore the sudden dread of anxiety building up as my hand fumbles to unlock the door. Just a few more twists and clicks of my key before—"
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/item.ogg"
    show ren happy z at center, spop with dissolve
    r "{size=-6}A-Angel! I'm glad I caught you—{/size}{nw=0.4}"
    play audio "audio/sfx/shoes alt.ogg"
    show ren frown at bpop with hpunch
    y "{size=+6}[ch_ren]?!{/size}" with vpunch
    y "Jeez! You almost gave me a heart attack!"
    show ren sad at spop
    r "Huh? Oh— S-Sorry!"
    y "It's… It's fine. Um… What are you doing here?"
    if d1_inviteren == False and d3_inviteren == False:
        y "And— Wait. How did you know I live on this floor?"
        show ren flushed at spop
        r "A-Ah! {size=-6}I saw you…{/size} Um… I saw your landlord earlier, and they told me what floor you were on."
        y "They did what?! Ugh."
        n "It was always one thing after the other, huh? First it was my newfound stalker, and now my landlord was just handing out my personal information without a care in the world."
        n "What if it {b}wasn't{/b} [ch_ren] asking for me? What if it was my…"
        n "No. Stop it, [ch_angel]. I shouldn't be thinking about that, lest I start to manifest my worries into existence."
    else:
        pass
    n "Steeling my nerves, I try to calm down my rapid heartbeat and meet [ch_ren]'s gaze. There's a flicker of worry in his eyes, but it all fades away the moment he takes a step closer to me."
    show ren smirk at spop
    r "I don't suppose you're missing something, are you?"
    y "Huh?"
    n "I try to recount all the things I've been carrying around today. But when nothing of note comes to mind, [ch_ren] shoots me a bright smile and pulls something from behind his back."
    n "It was…"
    y "Oh! My phone! And… Our food from earlier?"
    show ren happy at spop
    r "Hehe~ I figured you didn't have dinner yet. I, um… I also added something extra in there as well."
    n "As if realising how suspicious his words sounded, [ch_ren]'s cheeks immediately flush a deep red as he backtracks and stutters out a response."
    show ren flushed at bpop
    r "A-A-A dessert! It's a dessert! I bought it on the way here! Y-You don't have to eat it, though."
    y "Oh?"
    n "Peering into the bag {b}still{/b} being held tightly in [ch_ren]'s grasp, I notice the food, an adorable angelfish plushie, and…"
    n "Was that a small cup of [favourite_icecream] ice cream sitting on top?"
    n "Before I can snoop any further, his soft voice interrupts my train of thoughts."
    show ren neutral at spop
    r "Actually… Your co-worker seemed really worried about you, too. She wanted to be the one to drop these off, but…"
    show ren smirk at spop
    r "Something came up."
    show ren sad at spop
    r "As for your phone, you left it near the storage closet. Here— {i}Oh.{/i}"
    n "As if noticing my current predicament, [ch_ren] looks at my occupied arms before giving me another soft smile."
    show ren neutral at spop
    r "It'd be nice to have more hands sometimes, huh? Need some help?"
    y "It's fine, I think I got it—"
    n "Just when I think my door is unlocked, I somehow lose my grip around the parcel in my hands. But luckily, [ch_ren] catches it just in time before handing it — and everything else — back to me."
    show ren frown at spop
    r "S-Say! That sure is heavy, huh! Um…"
    n "With how obvious [ch_ren]'s gaze was, I could tell that he wanted to ask what was inside it. Surely there wouldn't be anything wrong with telling him?"

    jump day4_gohomebranch

################################################################################
## EEUUUGHGHGUEGHEUSGH
################################################################################
label day4_ending_good:
    $ ending_good = "obtained"
    $ persistent.d4_ending_gooding = True
    jump pathpoint

label day4_deadend:
    $ persistent.deadendings += 1
    $ persistent.deadend4 = True
    $ persistent.d4_badending = True
    jump pathpoint