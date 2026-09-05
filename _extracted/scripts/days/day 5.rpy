################################################################################
## DAY 5 YEHAWWWWWWW
################################################################################
label day5:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Currently playing Day 5',
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
    $ calendar_day = "05"
    $ skipday = "day6"

    $ update_ren = f"if lost, please return me to @{username_angel} >///<"
    $ update_moth = "I'M EXPLODING THE OCEAN WITH MY MIND!!!!!"
    $ update_violet = f"Hmm… looking for more MMOs to play. @{username_jae} any reccs?"
    $ update_elanor = "I hope everyone has a lovely day today! Mocha says \"meow\", hehe!"
    $ update_conan = "Remember to return your books on time."
    $ update_jae = "MAPLEEEE I WOULD GO TO WAR FOR YOU"
    $ update_leon = "Aaaaand… There's another crab in my bag lol"
    $ update_teo = "planning on going to the city today. who's coming?"
    if status_teo == False:
        $ update_olivia = "I DON'T WANT TO WORK TODAYYYYYYY"
    else:
        $ update_olivia = f"BATTING MY PRETTY AND DEMURE EYELASHES AT YOU @{username_teo}"
    $ update_kiara = "I wish I could bottle this sea breeze! It's just lovely :D"

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

    if d4_inviteren == True:
        $ ren_outfit = "normal"
        jump day5_renmorning
    else:
        $ ren_outfit = "normal"
        jump day5_alonemorning

################################################################################
## WAKING UP WITHOUT REN
################################################################################ 
label day5_alonemorning:
    scene angel_bedroom_day
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve

    n "Rather than the faint chirping of birds outside my window, it's the sound of something buzzing that rudely pulls me from my slumber."
    n "Muscle memory immediately kicks in, causing me to haphazardly throw my arm above my head and fumble around in search of the noise."
    n "When my hand lands on what I think is my phone, I groggily pull it closer to see what all the fuss is about. My boss' name flashes on the screen — causing me to awaken fully — and I unlock my phone to read his message."
    if status_teo == False:
        ct "Library closed 2day.. Police closed down the entire street. Unsure why . Will text U if more information becomes available. - [ch_conan]"
        y "…What?"
        n "[ch_conan]'s odd texting quirks aside, what did he mean the police closed down the entire street? Did that have anything to do with what was on the news last night?"
        n "That reminds me… I still needed to call [ch_elanor] and [ch_teo] to see if they were alright. I mean, it's been almost an entire day since I've heard any kind of reply from them."
        y "I'll try [ch_elanor] first."
        n "Not wasting any time, I find her name in my contacts list and press the call button… Only for it to immediately go to voicemail."
        n "Strange."
        y "…Maybe she's busy?"
        n "I hope she {b}at least{/b} received [ch_conan]'s text. I'd hate for her to show up bright and early to the library, only to find out that it's closed for the day."
        n "Speaking of texts… Maybe I should send one of my own, just in case."
        n "I type up a quick response before doing the same for [ch_teo]. And maybe it's because of what happened during our 'double date' yesterday, but I wasn't in the mood to try calling him for some reason."
        n "With that out of the way, I let out a tired sigh before haphazardly throwing my phone back onto the empty space near my bed."
    else:
        ct "Library will be closed 2day 4 pesticide spraying. Bookworms R back. U will get paid leave. - [ch_conan]"
        n "Well, that was relatively short and to the point — much like how [ch_conan] is always known to be. Though… He was never really the type to substitute letters with numbers."
        n "He was always more of the punctual type, I guess. Ah well. Maybe [ch_elanor] was giving him texting lessons again. Or perhaps his daughter, Alice? …Was she even old enough to text?"
        n "Before I can let my thoughts wander, I instead busy myself with drafting a response before haphazardly throwing my phone onto the empty space near my bed and letting out a sigh."
    n "Well… Now that I've got the day off, I wonder what should I do today?"
    play audio "audio/sfx/vibrate.ogg"
    n "But before I can decide on something, my phone goes off for what felt like the hundredth time this morning, and I fish around for it with another groan."
    n "Not bothering to look at the screen this time, I swipe my finger across the screen to answer the call."
    n "Wait—Call?!"
    play audio "audio/sfx/item.ogg"
    show mothphone happy at vcpos with easeinright
    m "Heeeeey there, sleepyhead! I've got something big to share with you!"
    show mothphone neutral at spop
    if d3_datestatus == False:
        m "Do you remember how I told you about that drawing raffle I won? Y'know, the other day when you were getting ready for that double date?"
        y "…Good morning to you too. And yeah, kinda."
        y "I {i}definitely{/i} remember you bringing it up, but I'm pretty sure you started gushing about recent AoG spoilers, like… five seconds later."
        show mothphone sad at spop
        m "…[damn!c], that {i}does{/i} sound like me. Whoops!"
        show mothphone smirk at spop
        m "Well, there's no harm in telling you again! No distractions this time, right?"
        n "With a tired laugh, I nod my head and give [ch_moth] a thumbs up."
        y "None at all."
    else:
        m "Do you remember how I told you about that drawing raffle I won? Y'know, the other day when you were at the manga store?"
        y "…Good morning to you too. And yeah, I do. But you got cut off near the end, though."
        y "I couldn't really make out what you were saying after our call disconnected."
        show mothphone sad at spop
        m "…I did? Weird. Maybe I'm remembering things differently again… [damn!c]."
        show mothphone smirk at spop
        m "Well, there's no harm in telling you again! You can hear me this time, right?"
        n "With a tired laugh, I nod my head and give [ch_moth] a thumbs up."
        y "Loud and clear."
    show mothphone neutral at spop
    m "Alright! drumroll, pleeeeease…"
    show mothphone happy at spop
    m "Guess who won a free trip to New Salvus! Me, that's who!"
    y "NO WAY?!" with vpunch
    show mothphone neutral at spop
    m "Yes way! I'm passing through Corland Bay right now, and I figured if you were still in the area, maybe we could—"
    y "Did you want to meet up?!"
    n "Knowing that this could potentially be the first time I meet [ch_moth] in person, I don't bother to hide my joy and excitement. Finally… After years and years of video calls and messaging each other online, we now had the chance to do it face to face."
    n "But before my thoughts can delve any further, [ch_moth] interrupts in a tone equally excited as mine."
    show mothphone sad at spop
    m "Would that be okay? I mean, the shuttle won't pick me up until tomorrow morning, so I haven't got much planned. A-And I wouldn't want to intrude on your plans or anything."
    show mothphone smirk at spop
    m "I know this is all so sudden and we've never actually met in person yet, or even {i}made{/i} any plans to…"
    y "Hey, it's fine! I could show you around the Bay; take you to the infamous beach from Attack On Giants—"
    show mothphone happy at spop
    m "SAY LESS." with vpunch
    show mothphone smirk at spop
    m "I'll be waiting for you… at our special place. Or whatever the meme is."
    show mothphone happy at spop
    m "Anyway! I'll be at the ferry terminal! But don't make me wait too long; watching the ocean makes me feel nauseous. Also… {i}I{/i} want to be the one who hangs up first. Byeeee!"
    show mothphone error at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5), vcpos
    n "Before I can get a word in, [ch_moth] flashes me a cheeky grin and ends the call."
    play audio "audio/sfx/item.ogg"
    hide mothphone with dissolve
    n "Letting out a puff of laughter at their antics, I eagerly get ready to start my day."

################################################################################
## VIOLETTTTTTAAAAAAAAAAAHHHHHHHHHHHHHHH
################################################################################ 
label day5_meetingviolet:
    scene oh_complex_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 2.0, 1.0)
    play audio "audio/sfx/door.ogg"

    n "Now appropriately dressed and prepared to face the day, I barely take two steps out of my apartment before the muffled sounds of chatter capture my attention."
    show violet happy at tleft
    show ren angry at tright
    play audio "audio/sfx/walking.ogg"
    play audio ["<silence 0.2>", "audio/sfx/heels alt.ogg"]
    with dissolve
    n "Glancing towards the {b}only{/b} functioning elevator on the far side of the hallway, I notice [ch_violet] and [ch_ren] in what seems to be an animated conversation — though it looks like my neighbour was the one doing most of the talking."
    show violet neutral at spop
    v "Oh, hello [ch_angel]! Good morning. Heading somewhere exciting today?"
    y "Ah, I'm just on my way to the ferry terminal—"
    show ren happy at spop
    r "Angel!"
    play audio "audio/sfx/sprinting.ogg"
    n "I can practically see sparkly particle effects appear around [ch_ren]'s face as he beams at me with a sunny smile. The next thing I know, he pivots away from [ch_violet], beelines towards me, and invades my personal space by curiously leaning closer."
    y "Uhh—? Hi?"
    y "And wow, isn't this an unlikely surprise."
    show ren neutral at spop
    r "O-Oh, yeah? I actually bumped into [ch_violet] this morning while on my walk."
    show ren smirk at spop
    if d1_inviteren == True:
        r "We started talking about you, and she mentioned wanting to see you."
    else:
        r "We started talking about you, and she mentioned something about being your neighbour."
    show violet sad at spop
    v "…I did?"
    show ren happy at spop
    r "Yeah! You also asked if I wanted to follow you upstairs to see if [ch_angel] was home, and well, here we are!"
    show violet angry at spop
    v "Oh? Hmm, I see. I could've sworn I went upstairs to check—{nw=0.4}"
    show violet sad at spop
    extend "No, never mind."
    n "[ch_violet] seems somewhat confused at the legitimacy of [ch_ren]'s words, but ultimately brushes it off with a shake of her head."
    n "Is… Everything alright with her?"
    show violet happy at spop
    v "Welp! I should probably let you both be on your way, then. Have fun, you two!"
    if d1_inviteren == True:
        show violet smirk at spop
        v "And remember! No funny business, you two!"
    else:
        pass
    show ren happy at center
    hide violet
    play audio "audio/sfx/heels.ogg"
    with easeoutleft
    n "Before either of us can muster a response, [ch_violet] swiftly turns on her heel and makes her way towards her apartment."
    n "A wave of concern washes over me as I notice how she ignores the potted plant by her door — normally, she'd give it a pet or even bring it inside on certain days — but [ch_ren]'s timid voice pulls me away from my thoughts and captures my attention."
    show ren neutral at spop
    r "So… You said something about visiting the ferry terminal earlier?"
    y "Oh, right. I was on my way to meet my online friend, actually."
    show ren smirk at spop
    r "Yeah? That sounds exciting."
    show ren sad at spop
    r "But… Is it really good practice to be meeting random strangers online?"
    n "His concern is almost palpable, and it strikes a chord within me. And although [ch_ren] {b}definitely{/b} had a valid point, [ch_moth] was no stranger. All five years of our friendship can attest to that."
    n "However, I did appreciate his concern nonetheless. In fact, it reminds me so much of Haruko and how he'd always look out for the safety of his friends—"
    n "All of a sudden, a mischievous thought crosses my mind…"
    n "One that involves [ch_moth]… And the real-life manifestation of Haruko."
    n "Ohhhh yeah, they'd {b}definitely{/b} freak out if they ever saw [ch_ren] in the flesh."
    n "With such an ingenious plan now firmly hatched in my mind, I turn to him with a faux-innocent glint in my eyes."
    y "[ch_ren]. {i}[ch_ren]ny-poo.{/i} My favourite pink-haired guy. Did you want to come along?"
    show ren flushed at spop
    r "Y-You want me to join? Yeah! Sure! Of course!"
    show ren happy at spop
    r "I even know the quickest route to the ferry! Y-You can count on me!"
    
    scene other_dark
    with dissolve
    n "…And that's how [ch_ren] and I find ourselves catching a ride to the promenade to meet [ch_moth]."
    jump day5_ferryscene

################################################################################
## WAKING UP WITH POOKIE BEAR
################################################################################ 
label day5_renmorning:
    scene angel_bedroom_day
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve
    play audio "audio/sfx/vibrate.ogg"
    n "Rather than the faint chirping of birds outside my window, it's the sound of something buzzing that rudely pulls me from my slumber."
    n "Muscle memory immediately kicks in, causing me to haphazardly throw my arm above my head and fumble around in search of the noise."
    n "When my hand lands on what I think is my phone, I groggily pull it closer to see what all the fuss is about. My boss' name flashes on the screen — causing me to awaken fully — and I unlock my phone to read his message."
    if status_teo == False:
        ct "Library closed 2day.. Police closed down the entire street. Unsure why . Will text U if more information becomes available. - [ch_conan]"
        y "…What?"
        n "[ch_conan]'s odd texting quirks aside, what did he mean the police closed down the entire street? Did that have anything to do with what was on the news last night?"
        n "That reminds me… I still needed to call [ch_elanor] and [ch_teo] to see if they were alright. I mean, it's been almost an entire day since I've heard any kind of reply from them."
        y "I'll try [ch_elanor] first."
        n "Not wasting any time, I find her name in my contacts list and press the call button… Only for it to immediately go to voicemail."
        n "Strange."
        y "…Maybe she's busy?"
        n "I hope she {b}at least{/b} received [ch_conan]'s text. I'd hate for her to show up bright and early to the library, only to find out that it's closed for the day."
        n "Speaking of texts… Maybe I should send one of my own, just in case."
        n "I type up a quick response before doing the same for [ch_teo]. And maybe it's because of what happened during our 'double date' yesterday, but I wasn't in the mood to try calling him for some reason."
        n "With that out of the way, I let out a tired sigh before haphazardly throwing my phone back onto the empty space near my bed."
    else:
        ct "Library will be closed 2day 4 pesticide spraying. Bookworms R back. U will get paid leave. - [ch_conan]"
        n "Well, that was relatively short and to the point — much like how [ch_conan] is always known to be. Though… He was never really the type to substitute letters with numbers."
        n "He was always more of the punctual type, I guess. Ah well. Maybe [ch_elanor] was giving him texting lessons again. Or perhaps his daughter, Alice? …Was she even old enough to text?"
        n "Before I can let my thoughts wander, I instead busy myself with drafting a response before haphazardly throwing my phone onto the empty space near my bed and letting out a sigh."
    n "Wait… Empty space?"
    n "That reminds me… What happened to [ch_ren]? The last thing I remember from last night was us snuggled up on the couch together."
    n "At that, my cheeks immediately grow warm at the thought. And without so much as thinking, I reach for my phone once more to check out the security camera app he installed."

    if relationship_ren == "crush":
        n "I guess it was a good purchase after all, seeing as I could use these cameras to spy on a certain pink-haired cutie — one who was {b}hopefully{/b} still in my apartment."
    else:
        n "I guess it was a good purchase after all, since I could use these cameras to check if [ch_ren] was still in my apartment."

    n "Looking for the app he installed on my phone, I open it up and navigate towards the camera in my living room."
    n "I see the telltale signs of my pillows and blankets on the couch, though what catches my interest is the fact that they were neatly stacked and put away… With no [ch_ren] in sight."
    n "Curious, I switch to a different camera to find him. He wasn't in my kitchen either, and not near my entryway. There was no point checking the camera in my bedroom since — well, I'm here already — which only left…"
    n "As soon as I check out the camera in my hallway, it's {b}then{/b} that I notice a familiar pair of blue jeans and a soft cardigan slumped against the wall. Was that [ch_ren]… Sitting outside of my door? What was he doing?"
    n "Perhaps a bit impulsively, I sit upright in bed and call out for him. And almost immediately, I hear the telltale signs of someone clambering around outside my bedroom."
    n "It's shortly followed by the faint sound of a throat clearing before a familiar patch of pink hair peeks through the gap in the door."
    play audio "audio/sfx/door.ogg"
    show ren flushed at cleft with easeinleft
    n "[ch_ren] peers in and sheepishly looks at me with a soft smile before he opens the door fully and invites himself inside."
    show ren flushed at spop
    r "G-Good morning, [ch_angel]! Did you sleep well? I—Um…"
    n "[ch_ren] looks like he wants to say something but instead chooses to clam up and stare at his feet. I almost want to reach out and ask him to look at me, but I hold back in favour of letting him take the initiative."
    n "Still, it doesn't stop me from calling out his name."
    y "[ch_ren]?"
    n "Almost immediately, [ch_ren]'s head whips up as he looks at me with wide eyes. There's a crooked smile on his face this time, and almost timidly, he shuffles on his feet as if deciding whether he can come closer."
    show ren smirk at spop
    r "You… Ah—Well, you asked me to stay last night."
    show ren neutral at spop
    r "B-But then you started mumbling about 'not having enough room for something', so I carried you to your bedroom instead, and…"
    show ren sad at spop
    r "{i}Then{/i} you asked me to join you in your bed, but then you said something about 'the grown-ups saying it'd be okay for me to stay', and I…"
    show ren blushing at spop
    r "W-Well, I didn't really know what to make of that, to be honest."
    n "…[shit!c], seriously?! Was I {b}really{/b} sleep-talking about something that happened when I was a child?!"
    show ren neutral at spop
    r "But I figured you really {i}did{/i} want me to stay, so I ended up camping out in your living room. So don't worry! Nobody came into your room."
    show ren flushed at spop
    r "B-Besides me, of course. Ahaha…"
    show ren blushing at spop
    r "And… I only {i}just{/i} woke up, actually!"
    y "Right…"
    show ren flushed at spop
    r "I-If you still want to, I can join you, and—Um… Actually, no… N-N-Never mind!"
    n "[ch_ren] looks like he'll combust on the spot if he talks any longer, and as if sharing the same thought, he clams up and awkwardly scratches his jaw. From that reaction alone, I have the slightest inclination as to what he wanted to ask me."
    n "Now that I think about it… Would it be such a bad idea?"

    $ choice_style = "box"
    menu:
        "Let him stay by the door":
            $ affection_ren -= 10
            n "I keep my mouth shut and let [ch_ren] linger a little longer by the door. He seems completely unfazed, though, if the way he casually leans against the doorframe and crosses his arms is any indication."
            n "It doesn't help that the sunlight from my window illuminates his relaxed demeanour in such an ethereal way, but the moment of peace shatters the second my phone goes off for what {b}feels{/b} like the hundredth time this morning."
            show ren blushing at bpop
            n "The sudden noise seems to startle [ch_ren] as well — so much so that he ends up knocking something off my dresser just as I press the answer button."
            play audio "audio/sfx/item.ogg"
            show mothphone happy at vcpos with easeinright
            m "Heeeeey! Morning sleepyhead! I've got something big to share with you!"
        "Invite [ch_ren] into bed":
            $ d5_invitebed = True
            $ affection_ren += 10
            y "Were you going to ask if you could join me in bed?"
            show ren blushing at bpop
            r "YES!" with hpunch
            show ren flushed at spop
            r "No, wait. I-I mean…"
            show ren neutral at spop
            r "…You don't mind? Because I don't mind standing here! Honest! You can't even notice the draft, and I don't mind the sunlight directly hitting my eyes at all—"
            y "Come here, [ch_ren]."
            play audio "audio/sfx/shoes alt.ogg"
            show ren flushed at tleft with easeinleft
            n "Almost like a puppy, he immediately makes a beeline towards me — but not before closing the door and waiting for me to lift the blankets up."
            n "…I suppose that's his way of making sure I really wanted him in my bed? Aw."
            play audio "audio/sfx/fabric.ogg"
            n "Not wasting another second, [ch_ren] joins me underneath the duvet and makes himself comfortable beside me."
            show ren neutral at spop
            r "H-Hi."
            if d1_sharebed == True:
                y "Hey. I feel like we've done this dance before."
                show ren smirk at spop
                r "Hehe~ Maybe once or twice. Your bed is just as warm as last time."
                y "That's usually what happens when someone sleeps in it."
            else:
                y "Hey, stranger."
                show ren smirk at spop
                r "Hehe~ Your bed is so warm."
                y "That's usually what happens when someone sleeps in it."
            n "I don't miss the way he pulls the blanket closer to his face with a warm smile."
            n "Funny, I sometimes do the same thing whenever I pull my clothes from the dryer. There's just something about the warmth and soothing scents that makes me feel happy — and it makes me wonder if [ch_ren] is feeling the same."
            n "Though admittedly, it {b}was{/b} a bit weird knowing that they're {b}my{/b} sheets and not his own, but… [ch_ren]'s eccentric nature had been growing on me these last few days. Somehow, this didn't really faze me anymore."
            show ren blushing at bpop
            n "[ch_ren], however, seems to have different thoughts. As if realising what he had just done, his eyes grow as wide as saucers before he whips his head in the opposite direction and feigns interest in the wall."
            n "There's a prominent blush spreading across his cheeks as he clears his throat and pulls the blanket down again."
            show ren flushed at spop
            r "U-Uh…"
            n "Before I can react, my phone goes off for what felt like the {b}hundredth{/b} time this morning, and I fish around for it once more with a groan. Not bothering to look at the screen this time, I swipe my finger across the screen to answer the call."
            n "Wait— Call?!"
            play audio "audio/sfx/item.ogg"
            show mothphone happy at vcpos with easeinright
            m "Heeeeey! Morning sleepyhead! I've got something big to share with you!"
    $ choice_style = "default"
    if d5_invitebed == True:
        show mothphone neutral at spop
        m "If it's not too much trouble, could you go to the ferry termi—Wait…"
        show mothphone flushed at spop
        m "WHO'S IN YOUR BED?! HELLOOOO! YES, YOU! I CAN SEE YOUR ARM!" with hpunch
    else:
        show mothphone neutral at spop
        m "If it's not too much trouble, could you go to the ferry termi—Wait…"
        show mothphone angry at spop
        m "What was that noise?"
        show mothphone flushed at spop
        m "OH MY GOD?! DO YOU HAVE SOMEONE IN YOUR BEDROOM?!" with hpunch
        show mothphone happy at spop
        m "[damn!c], [player_fl]! Let me see! Who is it? Whoooo?"
        show ren flushed at tleft with easeinleft
        n "Well, I doubt there's any point in keeping [ch_ren]'s presence a secret now. Giving him a small gesture, I beckon him closer to the edge of the bed and scoot over so that we can both fit in the frame."
        n "But before I properly introduce him to [ch_moth], I figure it'd be fun to tease them a little bit. Surely it won't hurt?"

    menu:
        "\"[ch_moth]… Haruko is finally real.\"":
            $ affection_moth += 1
            $ affection_jae += 1
            show mothphone sad at spop
            m "…What?"
            show mothphone blushing at spop
            m "WHAAAAAAAT?!" with vpunch
            show ren smirk at spop
            r "H-Hello. It's nice to meet you."
            if persistent.streamermode == True:
                show mothphone flushed at spop
                m "Oh my god? OH MY GOD?! HELLOOOO?!"
            else:
                show mothphone flushed at spop
                m "Oh my god? OH MY GOD?! WHAT THE FUCK, [player_fl]?!"
            show mothphone smirk at spop
            m "You {i}seriously{/i} weren't joking?! Wait… Is that actually the submissive and breedable guy you were—"
        "\"This is [ch_ren]. The guy I was telling you about.\"":
            $ affection_violet += 1
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            show ren neutral
            n "[ch_ren] doesn't seem to shy away when I tilt the camera towards his face — in fact, he only seems to lean closer to me before acknowledging [ch_moth] with a smile."
            show mothphone flushed at spop
            m "HUUUUUH?!" with vpunch
            show mothphone blushing at spop
            m "Since when did you become friends with the real-life version of Haruko?! And you didn't even tell me? Or… Wait—"
            show mothphone sad at spop
            m "I think you did? Is that the submissive and breedable guy you were—"
        "\"Are you talking about my body pillow?\"":
            $ affection_olivia += 1
            show mothphone smirk at spop
            m "Oh, veeeery funny, [player_fl]. I would've been the first to know if you bought a life-sized Haruko pillow."
            show mothphone neutral at spop
            m "{i}And{/i} I'd be the first to listen to you complain about the cost."
            y "Yeah, and then you'd ask me where I got it from."
            show mothphone happy at spop
            m "Exactly! So whose arm is that, [ch_angel]? Wait… That's not the submissive and breedable guy you were—"
        "\"It's none of your business.\"":
            $ affection_ren += 1
            $ affection_teo += 1
            show mothphone smirk at spop
            m "Actually, as your bestest friend ever, it's legally my business to know all about your romantic endeavours. {i}Especially{/i} when they're in your bedroom."
            show mothphone sad at spop
            m "Just like how you'd tell me about—Wait…"
            show mothphone flushed at spop
            m "That's not the submissive and breedable guy you were—"
        "{image=14NWY symbol} \"It's Mr Submissive and Breedable himself.\"" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
            call DLC_day5_bed from _call_DLC_day5_bed

    y "Okaaay, I think we should move on from this topic!"
    y "[ch_moth], this is [ch_ren]. [ch_ren], this is [ch_moth]."
    show mothphone happy at spop
    m "Nice to meet you, Mr. Submissive and—"
    y "[ch_moth]!"
    show ren sad at spop
    if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
        r "…I don't really understand how I—"
    else:
        r "…Wh-What does that mean?"
    show mothphone smirk at spop
    m "It's nothing, pookie bear. Don't you worry."
    show ren frown at spop
    r "…Pookie bear?"
    y "Please don't ask."
    show mothphone happy at spop
    m "No, no! Ask [them]! I'm having way too much fun with this. Hey, tell me… Does [ch_angel] make you wear Haruko's outfit too?"
    show ren flushed at spop
    r "Um—No. Not yet."
    show mothphone flushed at spop
    m "…{i}YET?!{/i} You've talked about this?" with hpunch
    show ren blushing at spop
    r "N-N-No! I just—Well, if [they] asked, I'm sure I wouldn't say no, and—"
    y "Alright! I think we're done here."
    y "[ch_moth]. Didn't you say you had something important to tell me?"
    show mothphone happy at spop
    if d3_datestatus == False:
        m "Oh, right! Remember how I told you about that drawing raffle I won? Y'know, the other day when you were getting ready for that double date?"
        y "Kinda… I definitely remember you bringing it up, but I'm pretty sure you started gushing about recent AoG spoilers, like… five seconds later."
        show mothphone sad at spop
        m "…[damn!c], that {i}does{/i} sound like me. Whoops!"
        show mothphone smirk at spop
        m "Well, there's no harm in telling you again! No distractions this time, right?"
        show ren smirk
        n "With a laugh, I nod my head while [ch_ren] gives a thumbs up from behind my shoulder. clearly, he's just as invested in our conversation."
        y "Aside from {i}pookie bear{/i} over here? No, none at all."
    else:
        m "Oh, right! Remember how I told you about that drawing raffle I won? Y'know, the other day when you were at the manga store?"
        y "Yeah, but you got cut off near the end, though. I couldn't really make out what you were saying after our call disconnected."
        show mothphone sad at spop
        m "…I did? Weird. Maybe I'm remembering things differently again… [damn!c]."
        show mothphone smirk at spop
        m "Well, there's no harm in telling you again! You can hear me this time, right?"
        show ren smirk
        n "With a laugh, I nod my head while [ch_ren] gives a thumbs up from behind my shoulder. clearly, he's just as invested in our conversation."
        y "Loud and clear."
    show mothphone smirk at spop
    m "Alright! drumroll, pleeeeease…"
    show mothphone happy at spop
    m "Guess who won a free trip to New Salvus! Me, that's who!"
    y "NO WAY?!" with hpunch
    play audio "audio/sfx/item.ogg"
    show ren sad at bpop
    n "I can feel [ch_ren] jolt in surprise from my sudden outburst before he settles back by my side. At that, I shoot him an apologetic smile — one that he returns with his own."
    show ren neutral
    show mothphone happy at spop
    m "Yes way! I'm passing through Corland Bay right now, and I figured if you were still in the area, maybe we could—"
    y "Did you want to meet up?!"
    n "Knowing that this could potentially be the first time I meet [ch_moth] in person, I don't bother to hide my joy and excitement. Finally… After years and years of video calls and messaging each other online, we now had the chance to do it face to face."
    n "But before my thoughts can delve any further, [ch_moth] interrupts in a tone equally excited as mine."
    show mothphone sad at spop
    m "Would that be okay? I mean, the shuttle won't pick me up until tomorrow morning, so I haven't got much planned. A-And I wouldn't want to intrude or anything."
    show mothphone neutral at spop
    m "I know this is all so sudden and we've never actually met in person yet, or even {i}made{/i} any plans to…"
    y "Hey, it's fine! I could show you around the Bay; take you to the infamous beach from Attack On Giants—"
    show mothphone blushing at spop
    m "SAY LESS." with hpunch
    show ren sad at spop
    r "U-Um…"
    n "It's then that I realise [ch_ren] is {b}still{/b} sitting next to me, peering over my shoulder while [ch_moth] and I converse. A wave of guilt washes over me, but [ch_moth] seems to step in before I can react."
    show mothphone happy at spop
    m "Oh, right! The iconic beach scene wouldn't be complete without Haruko, would it? You should bring him with you. I don't mind."
    show ren neutral at spop
    r "M-My name is [ch_ren]… But if it's really alright with [ch_angel] too, I wouldn't mind tagging along."
    y "Oh, right—You're a big fan of Attack on Giants too!"
    show ren happy at spop
    r "You remembered? H-Haaah… I mean—Yeah!"
    show ren smirk at spop
    r "I really like that anime, too! So I don't mind tagging along. If it's okay with you, of course."
    y "I'd love to have you with me."
    show ren blushing at spop
    r "L-L-L—?!" with vpunch
    n "[ch_ren] almost slams his head against the headboard with how quickly he straightens up, as [ch_moth] snickers at his reaction in the background."
    show mothphone flushed at spop
    m "Kiss, kiss, kiss!"
    y "I'll seriously hang up on you."
    n "[ch_moth]'s teasing calms down the moment I send them a faux glare. [ch_ren] seems to find amusement in my words as well, given how the corners of his lips pull into the faintest of smiles."
    if d5_invitebed == True:
        show mothphone smirk at spop
        m "Man, who knows what you two were getting up to in bed before I called?"
    else:
        show mothphone smirk at spop
        m "Man, if you two need some alone time, just say so."
    y "Goodbye. Don't ever call me again—"
    show mothphone happy at spop
    m "Hahaha, hold on!"
    show mothphone neutral at spop
    m "I'll be waiting for you guys at the ferry terminal! But don't make me wait too long; watching the ocean makes me feel nauseous. Also…"
    show mothphone happy at spop
    m "{i}I{/i} want to be the one who hangs up first. Byeeee!"
    show mothphone error at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5), vcpos
    n "Before I can get a word in, [ch_moth] flashes me a cheeky grin and ends the call."
    play audio "audio/sfx/item.ogg"
    hide mothphone with dissolve
    y "Well then… I guess it's breakfast to go?"
    show ren happy
    n "With a smile, [ch_ren] eagerly nods his head."

################################################################################
## MEETING MOTH AT THE FERRY TERMINAL YIPPEEEE
################################################################################ 
label day5_ferryscene:
    scene beach_beach_day
    play music "audio/bgm/Promise To Meet Again.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/beach.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 2.0, 1.0)

    $ location_moth = "pier"
    $ location_violet = "home"
    $ location_elanor = "home"
    $ location_ren = "pier"
    $ location_conan = "library"
    $ location_jae = "pier"
    $ location_leon = "random"
    $ location_teo = "random"
    $ location_olivia = "random"
    $ location_kiara = "bluemoss"

    n "The salty aroma of the sea is the first thing I notice before a large ferry boat comes into view."
    n "[ch_ren] becomes a temporary second thought the moment I realise {b}who{/b} might be on that ship, and I hurriedly make my way towards the dock where [ch_moth] is waiting."
    play audio "audio/sfx/sprinting.ogg"
    show moth smirk at center with dissolve
    show moth smirk at bpop
    m "[ch_angel]!" with vpunch
    y "[ch_moth]!"
    play audio "audio/sfx/shoes alt.ogg"
    show moth neutral z at spop
    if player == "Moth":
        m "It's youuuuu! You're actually real!" with vpunch
        y "Hahaha!"
    else:
        m "{size=+10}[ch_angel]!{/size}" with vpunch
        y "{size=+10}Moooooth!{/size}"
    show moth happy z at bpop
    play audio "audio/sfx/item.ogg"
    n "Almost immediately, [ch_moth] runs towards me with outstretched arms before pulling me into a warm hug."
    n "Their excitement is almost palpable as they laugh in my ear and give me the tightest squeeze I've ever experienced. They nearly swept me off my feet, too, had it not been for the potential safety hazards of swinging someone around on a slippery dock."
    show moth frown z at spop
    m "Man, I couldn't {i}wait{/i} to get off that thing! Never again am I going to ride on a ferry. Ever. {i}Everrrr.{/i}"
    show moth neutral z at spop
    m "But oh my God? You're actually here! You're real!"
    show moth blushing z at spop
    m "And you're taller than I expected, too! And woah… I love your outfit!"
    y "Heh, must be the shoes."
    show moth happy z at spop
    play audio "audio/sfx/shoes alt.ogg"
    show ren neutral at cleft with easeinleft
    m "I {i}have{/i} to get a similar pair of—"
    show moth flushed at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    play audio "audio/sfx/item.ogg"
    show moth flushed at center with dissolve
    play audio "audio/sfx/shoes alt.ogg"
    play audio ["<silence 0.2>", "audio/sfx/shoes alt.ogg"]
    show ren neutral at tleft
    show moth flushed at tright
    with easeinleft
    m "…!" with vpunch
    show moth flushed at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5), tright
    show ren sad
    m "HOLY [shit!u]! IS THAT—?!" with hpunch
    show moth blushing at spop
    m "You're joking. You're {i}actually{/i} joking. Is this real?"
    show moth flushed at spop
    m "No way {i}the{/i} real-life Haruko is standing before my eyes right now…"
    show ren neutral
    n "Following [ch_moth]'s gaze, I notice [ch_ren] sheepishly walk up to the both of us and stand by my side. He doesn't seem to greet [ch_moth] in any way, but just as I turn around to fully face him, [ch_ren] removes a hand from his pocket and gives a shy wave."
    n "Ah, I guess I've gotten so used to [ch_ren] being more forward around me that I almost forgot about his reserved side."
    show ren flushed at spop
    if d4_inviteren == True:
        r "I-It's nice to meet you! Again."
        show ren smirk at spop
        r "And… I get that a lot."
        show ren neutral at spop
        r "It… It must be my shoes as well."
        show moth blushing at spop
        m "Yeah… The shoes…"
        y "[ch_moth], you haven't even looked down yet."
        show moth flushed at spop
        m "Do I need to? Everything I need is riiiiight here in front of me, and—[shit!c]. Did I say that out loud?"
    else:
        r "I-It's nice to meet you! I'm… Um… [ch_ren]."
        show moth blushing at spop
        m "Hoooooooly—"
        show moth flushed at spop
        m "You even sound just like him! Wait, don't tell me… Do you {i}also{/i} whim—"
        show moth blushing at bpop
        m "[shit!c]. Did I say that out loud?"
    show moth smirk at spop
    m "Whatever, doesn't matter. You can't blame me when I've got {i}the{/i} real-life Haruko standing in front of me right now!"
    show moth flushed at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5), tright
    m "Where'd you get your hair done? Can you save me from a giant? Do you need a spouse?"
    show moth blushing at spop
    m "God, I've seen what you've done for others—"
    y "[ch_moth]!"
    n "I've never seen them so… animated before. It was almost hard to believe that this was the same [ch_moth] who'd always shy away from social situations."
    show moth neutral at spop
    m "Sorry! I'll try to tone it back. Keyword being 'try' here."
    show moth happy at spop
    m "But for real, though, thanks for coming out and meeting me like this. I know it's really last minute."
    y "Not at all. I had nothing planned for today anyway, and I'm glad [ch_ren] was willing to tag along."
    show ren happy at spop
    r "O-Of course! I like making you happy—"
    show moth flushed at spop
    m "Guh, he really is Haruko."
    show ren sad at spop
    r "Oh, uh—It's [ch_ren]. And I guess… Well, apart from the hair, I suppose it's just a major coincidence that Haruko and I happen to act the same."
    show ren smirk at spop
    r "It's one of the reasons why he's my favourite character, actually."
    n "It's hard to miss the way [ch_ren] looks at me when he mentions Haruko as his favourite, but it happens all too quickly that I fear it was just a trick of my imagination."
    show moth smirk at spop
    m "Yeah? I like him cuz he's hot."
    show moth blushing at spop
    m "Plus, he whimpers and pouts in the most cutest way whenever he's upset."
    show ren blushing at bpop
    n "I almost laugh at the way [ch_ren]'s eyes widen at [ch_moth]'s words."
    show moth smirk at spop
    m "Alsoooo~ Have you seen him in the latest episode? I swear, the animators knew what they were doing when they ripped his unifo—"
    y "Wait! I haven't seen it yet! Don't spoil it!"
    show moth sad at spop
    m "Oh? [shit!c], sorry, [player_fl]! My bad. But hey, if you've got the time, why don't we all watch it together later?"
    show ren happy at spop
    r "S-Sounds like fun! Don't you think, Angel?"
    n "I wasn't expecting [ch_ren] to join in, much less witness [ch_moth] be so… social with someone."
    n "But then again… Much like me, [ch_moth] has been {b}obsessed{/b} with Attack On Giants since it first came out, so it made sense for them to be able to gush about it without any restraint."
    n "Plus, it was nice to see [ch_moth] having fun, so who was I to put a stop to it?"
    show moth neutral at spop
    m "Speaking of… Did I tell you the reason I'm here in the first place?"
    show moth smirk at spop
    m "Well, y'know about that one anime convention being held in New Salvus? They were hosting this AOG art contest online, so naturally I joined… {i}aaaaand{/i} won!"
    show moth happy at spop
    m "So now I get to go to the convention for free, {i}and{/i} I get to have one-on-one time with all the voice actors!"
    show moth blushing at spop
    m "I mean, c'mon, I finally get the chance to talk to {i}the{/i} voice actor for Haruko? This is like a dream come true!"
    show moth flushed at spop
    m "…I wonder if I can get him to say he wants to marry me."
    y "Wait, why didn't I know about this?"
    show moth frown at spop
    m "Yeah… Now that you mention it, it {i}is{/i} kinda strange how you never said anything to me. You must be really busy with work, huh?"
    n "Work…? I guess you could say that."
    n "However, with everything that's been happening recently, I'm not entirely sure I can blame my distractions on my job. And I {b}love{/b} Attack On Giants… It's weird how I never got any recommendations or ads for the convention online."
    n "Huh, so much for personalised feeds."
    show moth happy at spop
    m "Well, don't worry about it too much! I'll be sure to buy you all the Haruko charms I can find. I mean, I still owe you, don't I?"
    show moth neutral at spop
    m "Besides! The convention isn't until tomorrow, and we've still got an entire day to kill. Didn't you once say you wanted to show me some of the sights here?"
    y "Aw, you remembered?"
    y "Well… Since we're all here already, why don't we start with the main beach? Oh, but…"
    y "You don't really like the water, do you? Maybe we can just—"
    show ren smirk at spop
    r "They don't?"
    show moth sad at spop
    m "Ahahaha… {i}Yeeeeeah.{/i} Though it's not really the water that gets to me! It's what's lurking beyond."
    show moth frown at spop
    m "Unknown creatures, ships and planes that go missing for no reason, endless depths that have yet to be explored…? Yeah, nope. Not for me."
    show moth neutral at spop
    m "Oh, and I almost drowned as a kid."
    y "WHAT?!" with vpunch
    show moth happy at spop
    m "Hahaha! Unfortunately for you, [player_fl], you'll need to unlock my level eighty friendship to hear that one."
    show moth neutral at spop
    m "Now! What did you say about a beach? After what happens in the latest episode, I hope I get to see Haruko's glorious butt imprint in the sand."
    show ren blushing at spop
    r "U-Um… Please don't look at me when you say that."

    if status_teo == False:
        jump day5_teodead
    else:
        pass

################################################################################
## MEETING JAE EXCEPT TEO IS ALIVE AND THRIVING
################################################################################ 
label day5_teoalive:
    scene beach_street_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/street.ogg" fadein 1 fadeout 1
    show peffect
    show ren neutral at tleft
    show moth frown  at tright
    play audio "audio/sfx/movement.ogg"
    play audio ["<silence 0.1>", "audio/sfx/movement.ogg"]
    with Fade(1.0, 2.0, 1.0)

    show moth frown at spop
    m "…Bit of a walk, huh?"
    y "From the ferry terminal? Yeah. It's not far from my place, though."
    show moth sad at spop
    m "Wait, for real? You live around here?"
    y "Mm! See that building over there? The tall one?"
    n "[ch_ren] quickly moves out of the way as [ch_moth] squints in the direction I'm pointing at. It takes them a moment, but their eyes finally land on one building in particular before they turn to me with a concerned look."
    show moth frown at spop
    m "…The one with the ratty sign that's about to fall off its hinges?"
    y "Uh. Yeah. That one."
    show moth flushed at spop
    m "Oh! It's… Um… Nice? N-Not too shabby! But [damn], it's really close to the beach, huh? I bet you'd get a good view of the ocean from up there."
    y "Actually, the main street blocks my—"
    play audio "audio/sfx/sprinting.ogg"
    show ren sad at cleft
    show moth flushed at center
    show jae happy at cright
    with easeinright
    j "[ch_angel]? And… Ron, right? Hey, hey, hey!" with vpunch
    n "A familiar voice calls out from somewhere behind us before [ch_jae] emerges from one of the buildings and jogs towards us with a bounce in his step."
    show ren frown at spop
    r "It's [ch_ren]…"
    show jae sad at spop
    j "Aw, [shit], sorry! So it's [ch_ren], huh?"
    show jae smirk at spop
    j "[ch_ren]. {i}Reeeen.{/i} [ch_ren]. Alright, stored that in my brain!"
    show jae sad at spop
    j "I could've sworn I heard [ch_leon] call you Ron, though…"
    if d1_inviteren == False:
        show jae smirk at bpop
        j "But it's nice to finally put the name to the face! You… weren't what I was expecting, to be honest."
    show jae happy at spop
    j "But that's not important right now! What are you guys doing out here so early? I thought you had work today, [ch_angel]."
    y "I've actually got the day off today."
    y "My boss said something about bookworms, I think? So I'm spending the day showing my friend [ch_moth] around Corland Bay. They're new here."
    show jae smirk at spop
    j "Now that you mention it… Yeah, your friend {i}does{/i} kinda have that touristy look about 'em."
    show jae happy at spop
    j "So your name is [ch_moth], huh? That's such a cool name! I'm Jae-Hyun! Feel free to call me [ch_jae], though."
    show jae smirk at spop
    j "That's so much easier to remember, huh?"
    show moth frown at spop
    m "…"
    show jae smirk at spop
    j "Though I totally won't blame you guys if you start calling me Joe, or something."
    show jae happy at bpop
    j "I mean, think about it! Ron and Joe… An unlikely duo on the hunt for more hair-dye… Haha!"
    show ren sad at spop
    r "H-Hair…dye?"
    show moth flushed at spop
    m "…"
    show jae frown at spop
    j "Yeesh, tough crowd today. Heh."
    show moth frown at spop
    m "…"
    n "Ah, right. I'd almost forgotten how shy [ch_moth] gets around people they don't know. Unlike talking to strangers online, there was no safety or comfort in having a screen to hide behind in real life."
    n "Part of me wonders if this might be the reason why they seem so out of place right now — but this isn't the time to ask, and I didn't want to make [ch_moth] feel any more uncomfortable than they already were."
    show jae neutral at spop
    j "Soooo… Were you guys heading to the beach, too? I heard the swell is going to be good today!"
    y "We are, actually. I wanted to show [ch_moth] the infamous Giant's Cove."
    show jae smirk at spop
    j "Niceee! Here's hoping there won't be too many tourists there today. It's still early, so maybe they're all—Oh, wait… Are you going dressed like that?"
    y "Like… What?"
    show jae happy at spop
    j "C'moooon, two of you are wearing jeans, and the other has two sweaters on! That's toootally not beach apparel."
    show jae neutral at spop
    j "If you want, I've got a spare pair of swim trunks in my bag that you can borrow for the da—"
    show ren happy at spop
    r "W-Why don't I buy us some swimsuits instead? There's a beach stand just over there."
    y "Oh, you don't have to. Besides, I don't think [ch_moth] would want to go too deep into the wa—"
    show ren neutral at spop
    r "It's fine, I won't be long!"
    play audio "audio/sfx/running.ogg"
    hide ren
    show moth frown at tleft
    show jae neutral at tright
    with easeoutleft
    n "Before I can respond, [ch_ren] is {b}already{/b} bounding towards the nearby stall to pick out some swimsuits, leaving me alone with [ch_moth] and [ch_jae]."
    y "Well, then…"
    show jae happy at spop
    j "Haha! He must be reeeeal excited about visiting the cove too, huh?"
    show jae smirk at spop
    j "Welp! If you guys wanna try out surfing later, come and find me! I'll be hanging out here all day."
    show jae neutral at spop
    j "[ch_teo] and [ch_leon] might even show up later if you wanna meet {i}even more{/i} of [ch_angel]'s totally cool and handsome friends."
    show moth neutral at spop
    m "…"
    n "I couldn't help but playfully roll my eyes at [ch_jae]'s antics."
    y "I think we'll pass. But… You're heading to the beach already?"
    show jae happy at spop
    j "Ohhh? You want me to stay? Aww shucks, [ch_angel]."
    y "Never mind. C'ya."
    play audio "audio/sfx/item.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show jae happy at cright with easeinleft
    n "With a gentle shove, I usher [ch_jae] in the direction of the beach with a smile. His boisterous laughter slowly fades off as he waves goodbye to [ch_moth] and me."
    show jae happy at bpop
    j "It's nice meeting ya, [ch_moth]! Tell [ch_ren] I said bye!"
    play audio "audio/sfx/sprinting.ogg"
    show moth neutral at center
    hide jae
    with easeoutright
    show moth flushed at spop
    m "…"
    show moth smirk at spop
    m "He's… Really nice."
    y "He is."
    jump day5_changingstalls

################################################################################
## OH EM GEE TEO IS DEAD?!?!! so anyways <3 live laugh jae-hyun <3
################################################################################ 
label day5_teodead:
    scene beach_street_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/street.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/movement.ogg"
    play audio ["<silence 0.6>", "audio/sfx/walking.ogg"]
    show ren happy at tleft
    show moth frown  at tright
    show peffect
    with Fade(1.0, 2.0, 1.0)

    n "The walk along the promenade is awfully quiet, and it has me wondering where the usual crowd of people are. Usually, I'd see [ch_jae] and [ch_teo] hanging around near the food kiosks, but today… No one seemed to be around."
    n "Did something happen? And why was nobody answering their phones? It'd surely been over a few hours by now, and [ch_elanor] has never been one to screen a text for that long."
    n "[ch_teo] too, for that matter — even {b}if{/b} he often finds enjoyment in ghosting others."
    y "It sure is quiet today…"
    y "Eh. At least we won't have to worry about fighting someone over a spot to put down our stuff."
    show ren neutral at spop
    r "That's true… A-Ah! But we can't go in the ocean wearing these outfits."
    show ren neutral at spop
    r "Here, why don't I buy some swimsuits for us? There's a beach apparel stand just over there."
    y "Oh, you don't have to. Besides, I was mostly joking. You already know [ch_moth] doesn't like the oc—"
    show ren neutral at spop
    r "It's fine, I won't be long!"
    play audio "audio/sfx/running.ogg"
    hide ren with easeoutleft
    n "Before I can respond, [ch_ren] is already bounding towards the nearby stall with a slight spring in his step."
    y "Well, then…"
    show moth neutral at spop
    m "Haha! It's fine, [player_fl]. You two can swim if you want. I don't mind sitting under a palm tree or two and catching up on some webcomics."
    y "Are you sure?"
    show moth neutral at spop
    m "Yeah! Besides, {i}now{/i} might be a good time to try and conquer my fears!"
    show moth angry at spop
    m "…Probably."
    show moth neutral at spop
    m "Y'know, I recently watched this anime where the main protagonist gets isekai'ed to an underwater city—"

################################################################################
## WE'RE GOING SWIMMING!!! (no we're not)
################################################################################ 
label day5_changingstalls:
    scene town_street_day
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve

    if status_teo == False:
        n "When [ch_ren] returns, he's got a bunch of bathing suits, towels, and a beach bag bundled up in his arms."
    else:
        n "In the end, I find myself listening to [ch_moth] lore-dump about an anime while we wait for [ch_ren] to return. And when he does, he comes back with a bunch of bathing suits, towels, and a beach bag bundled up in his arms."
    
    n "He wastes no time in handing me a swimsuit, and before I can tell what's happening, he's {b}already{/b} ushering me towards a changing stall and promising to watch the door from outside."
    
    scene other_dark
    play audio "audio/sfx/door.ogg"
    with GlitchDissolve
    n "A small part of my brain picks up on the fact that the swimsuit is in my {b}exact{/b} size, but I put it on the back-burner for now so I can focus on changing out of my regular clothes."
    n "When I look at all the items [ch_ren] got me, I notice that…"

    $ choice_style = "box"
    menu:
        "It shows parts of my skin":
            n "The design on the front somewhat resembles my [favourite_outfit] aesthetic, and it makes me wonder if that was the reason why [ch_ren] intentionally picked it out for me."
            if body == "feminine":
                n "However, another part of me wonders if he only picked this swimsuit because it shows off some of my curves."
            elif body == "masculine":
                n "However, another part of me wonders if he only picked this swimsuit because it shows off my build."
            else:
                n "However, another part of me wonders if he only picked this swimsuit because it shows off some of my legs."
            n "Heh, I know what you are, [ch_ren]."
        "It doesn't show any of my skin":
            n "The design on the front somewhat resembles my [favourite_outfit] aesthetic, and it makes me wonder if that was the reason why [ch_ren] intentionally picked it out for me."
            n "He also seems to understand that I don't normally show much of my skin in public, and {b}especially{/b} when it comes to wearing a swimsuit at the beach."
            n "And while it was greatly appreciated, it did come across as a bit… odd. I mean, how did he even know this about me? Did I mention it in passing at some point?"
            n "Eh, whatever. I'll make a mental note to ask him about this later."
    $ choice_style = "default"

    n "I can still hear [ch_moth] moving about in the stall next to me — alongside the rustling of fabric and a few expletives — so I take my time changing. But it doesn't take long before I'm fully dressed and ready to throw myself into the ocean."
    n "As if to kill time and give everyone else a few more minutes to get dressed, I stuff my regular clothes into my bag eeeeextra slowly and swing open the door—"
    n "Only to find [ch_ren] still waiting for me on the other side."
    
    scene town_street_day
    play audio "audio/sfx/door.ogg"
    show ren smirk at center
    with GlitchDissolve
    
    show ren smirk at spop
    r "All done? That was quick. Guess it's my turn now, huh?"
    n "It's then that I notice that there were only two stalls available… And that [ch_ren] really was taking his guarding job seriously."

    $ choice_style = "box"
    menu:
        "Let [ch_ren] join me in my stall":
            $ affection_ren += 10
            y "I'm actually… not quite done yet. Did you want to share my stall?"
            n "Almost immediately, [ch_ren]'s cheeks turn a bright shade of red as he practically chokes on his own spit."
            show ren blushing at spop
            r "Join you—?! A-A-Are you sure?" with vpunch
            show ren flushed at spop
            r "I can wait outside until you're done!"
            show ren blushing at spop
            extend " I don't mind!"
            show ren flushed at spop
            extend " Really!"
            show ren frown at spop
            r "Besides, that stall probably won't fit the both of us. W-We'd be—{i}I'd{/i} be… Um—"
            m "Oh, for Haruko's sake. Just use [their] stall!"
            show ren flushed
            n "[ch_moth]'s words catch us both off guard before [ch_ren] turns his gaze back towards me and pairs it with a sheepish smile."
            n "Figuring that his timidness was holding him back from taking the initiative, I move to the side and silently beckon him closer with a wave of my hand."
            scene other_dark
            play audio "audio/sfx/door.ogg"
            play audio "audio/sfx/shoes alt.ogg"
            play audio ["<silence 0.2>", "audio/sfx/shoes alt.ogg"]
            show ren flushed z
            with dissolve
            n "And almost shyly, [ch_ren] stumbles forward and tries his best to squeeze inside the stall without disrupting me, despite his large frame. As if to offer him some sort of comfort — and breathing room — I give [ch_ren] a reassuring smile and turn my back."
            y "Don't worry, I won't look."
            show ren blushing z at spop
            r "{size=-6}I-I wouldn't mind if you did…{/size}"
            y "Hm? What was that?"
            show ren happy z at spop
            r "Ah—! I said… I won't look either! S-So don't mind me!"
            if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
                call DLC_day5_stall from _call_DLC_day5_stall
            m "I can still hear you two, you know."
            y "Hiii, [ch_moth]."
            m "Yeah, yeah. Whatever. You guys better hurry up. I'm almost done here!"
        "Get out and let [ch_ren] use my stall":
            $ affection_ren -= 10
            if rem_boyfriend == True:
                y "All yours, babe."
                show ren flushed
                n "At my words, [ch_ren]'s cheeks immediately flush a deep red as he draws closer to me and almost trips over his own feet."
                show ren blushing at spop
                r "Y-Y-You are? All mine?"
                y "Yeah. You {i}are{/i} my boyfriend, aren't you? But… I was actually talking about the {i}stall{/i}, [ch_ren]."
                show ren lovesick at spop
                r "B-B-Boyfr—I mean… R-Right! Hahaha!~ The stall. Mine. Or…" with vpunch
                show ren blushing at spop
                r "Um—My turn. In the stall. {i}Me.{/i}"
            else:
                y "All yours, buddy."
                show ren blushing at spop
                r "…Y-Y-You are?"
                y "The {i}stall{/i}, [ch_ren]. It's all yours."
                show ren flushed at spop
                r "Oh. Right! H…Hahaha… The stall. Mine. I mean—My turn."
            n "It's almost endearing watching the way puffs his cheek and pouts at his fumble. [ch_ren] makes sure to keep direct eye contact with the ground instead of me as he passes by, but he turns around at the last minute and peers at me from behind the door."
            play audio "audio/sfx/shoes alt.ogg"
            show ren frown z with dissolve
            r "You— U-Um… You really {i}were{/i} talking about the stall, right? Actually—"
            show ren flushed z at bpop
            r "Never mind!" with vpunch
            play audio "audio/sfx/door.ogg"
            hide ren with dissolve
            n "Before I can respond, [ch_ren] slams the door shut and hides his flushed expression from me." with vpunch
            m "I can still hear you two, you know."
            y "Hiii, [ch_moth]."
            m "Yeah, yeah. Whatever. You guys better hurry up. I'm almost done here!"
    $ choice_style = "default"

################################################################################
## NOW WE'RE ACTUALLY SWIMMING (no we still are not)
################################################################################ 
label day5_covescene:
    scene beach_grove_day
    play music "audio/bgm/Promise To Meet Again.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/beach.ogg" fadein 1 fadeout 1
    show peffect
    $ ren_outfit = "swimwear"
    $ moth_outfit = "swimwear"
    with Fade(1.0, 2.0, 1.0)

    n "The walk to the beach is nothing short of eventful, and soon enough, we find ourselves at the entrance to the infamous Giant's Cove."
    n "[ch_moth] can barely contain their excitement as they take in the familiar scenery before them, and I don't miss the way they start to babble about the striking similarities between the beach scene from AoG and the current scene laid out before them."
    n "I've already visited this cove enough times for the excitement to wear off, but watching [ch_moth] have the time of their life right now only seems to hype me up even more."
    n "When I look back at [ch_ren] to see whether he was feeling the same, I find that he's already staring straight at me with a soft look in his eyes. He reaches a hand out to me, but just as he's about to say something, [ch_moth] cuts him off."
    show ren smirk at tleft
    show moth happy at tright
    with dissolve
    show moth happy at bpop
    m "They {i}actually{/i} built a monument for Attack on Giants here? That's sooo cool!"
    show moth flushed at spop
    m "Oh, we should take a photo to commemorate! Here!"
    y "Uh—"
    show ren frown
    play audio "audio/sfx/shoes alt.ogg"
    show moth happy at cright
    with easeinleft
    n "In a blur, [ch_moth] excitedly shoves their phone into [ch_ren]'s hands and tugs me towards the stone statue made in Haruko's likeness."
    n "One of their arms hooks over my shoulder to pull me closer to their side, and I can feel their smile grow the moment they press their cheek next to mine."
    n "[ch_ren], however, seems to have a bout of confusion as he takes in the scene in front of him — before he snaps out of his daze and lifts [ch_moth]'s phone to take a photo."
    play audio ["<silence 0.3>", "audio/sfx/camera.ogg", "<silence 0.5>", "audio/sfx/camera.ogg"]
    play audio "audio/sfx/camera.ogg"
    n "The camera flashes every time he takes a picture, but after the seventh flash, [ch_moth] decides that's enough and signals for their phone back."
    play audio "audio/sfx/shoes alt.ogg"
    show moth happy at tright with easeinright
    show moth smirk at spop
    m "Ooh, let's see the results!"
    n "When I peer over [ch_moth]'s shoulder, I see that the photos [ch_ren] took were… actually kind of {b}bad{/b}. Although the statue and I were perfectly in the frame, [ch_moth] seemed to be cut out entirely, with only the arm around my shoulders making the shot."
    show moth angry at spop
    m "Hey—What about me?"
    show ren smirk at spop
    r "Y-You're right there. See?"
    show moth frown at spop
    m "My arm, you mean."
    show ren neutral at spop
    r "Yeah."
    show moth sad at spop
    m "That doesn't count. Here, take another one."
    show ren frown at spop
    r "…"
    show ren angry
    play audio "audio/sfx/shoes alt.ogg"
    show moth happy at cright
    with easeinleft
    play audio ["<silence 0.3>", "audio/sfx/camera.ogg", "<silence 0.5>", "audio/sfx/camera.ogg"]
    n "This time, [ch_moth] curls their arm around my waist and leans closer to my side. I don't miss the way [ch_ren]'s eyes widen — nor the way he takes a second too long to take the photo — but I chalk it up to him being surprised at [ch_moth]'s sudden clinginess."

    if rem_boyfriend == True:
        n "Was he… jealous because we didn't have any pictures like these of our own?"
        n "Before I can think about it further, [ch_ren]'s voice grabs my attention."
    elif rem_touch == True:
        n "I mean, it makes sense, given how aversive I've been whenever I try to initiate any form of physical contact with [ch_ren]."
        n "I wasn't a big fan of it, but I knew that [ch_moth]'s intentions were harmless. But before I can think about it further, [ch_ren]'s voice grabs my attention."
    else:
        pass

    show ren at center
    show moth sad
    with easeinleft
    play audio "audio/sfx/shoes alt.ogg"
    show ren sad at spop
    r "There. Better?"
    n "When [ch_ren] hands the phone back to [ch_moth], they hunch over the screen and look over everything with a critical eye."
    n "It's almost comical watching them zoom in and out to scrutinise every little detail, but I figured it'd be best to leave them to their own devices once I see them open up a photo editing app."
    n "No doubt to cover our faces with AoG stickers before they share it in their family group chat to boast."
    play audio "audio/sfx/shoes alt.ogg"
    hide moth with easeoutright
    n "Turning to my side, I look at [ch_ren] with a teasing expression."
    y "What about you, buttercup?"
    show ren flushed at spop
    r "H-Huh?"
    y "Don't you want a photo to commemorate this moment as well?"
    n "Without waiting for a response, I playfully pull [ch_ren]'s phone from his pocket and aim it at my pink-haired companion."

    scene CG D5_BEACH
    hide screen dayscalendar
    show screen menuwu
    $ quick_menu = False
    $ persistent.cg_d5_beach = True
    with Fade(1.0, 1.0, 1.0)

    r "Ah!"
    n "[ch_ren] immediately covers part of his face with his hand — but quickly realises that he isn't wearing his thick cardigan, so the sleeves of his rash guard hardly do much to hide his growing embarrassment."
    n "He seems almost camera shy with the way he turns away from me with a soft blush on his cheeks, though he doesn't complain when I start to take a few pictures of my own."
    n "In fact, [ch_ren] appears to {b}revel{/b} in all the attention I'm giving him with the way he indulges in my request with a warm smile."
    n "Feeling a sudden surge of confidence, I reach out my hand expectantly and gesture for [ch_ren] to place his cheek against it."
    r "…!"
    n "He wastes no time in leaning down, pressing his face against my hand, and nuzzling into my touch. [ch_ren] {b}almost{/b} looks like a cute puppy like this, and I find myself taking a few more pictures to savour the tender moment."
    n "Though admittedly, the eye contact he's giving the camera feels a bit… {b}intimate{/b}, but I brush it aside for the sake of my rapid heartbeat."
    r "If I send these to you, will you make it your lockscree—"
    
    scene beach_grove_day
    show peffect
    $ quick_menu = True
    hide screen menuwu
    show screen dayscalendar
    show peffect
    show ren angry z
    with GlitchDissolve

    m "Haruko—I mean, [ch_ren]! Can you come here for a second?" with vpunch
    play audio "audio/sfx/shoes alt.ogg"
    show moth neutral at cright with easeinright
    show moth neutral at spop
    m "I need you to compare hairstyles with this statue. My brother thinks Haruko's hair isn't fluffy enough, but—"
    play audio "audio/sfx/item.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show ren sad with dissolve
    play audio "audio/sfx/fabric.ogg"
    play audio "audio/sfx/walking.ogg"
    show moth at tright with easeinright
    show ren at tright
    show moth:
        xalign 0.9
    with easeinleft
    n "I stifle my laughter at [ch_ren]'s confused look as [ch_moth] continues to rant while they tug him towards the Haruko statue. I look away the moment they ask him to start posing, and it's then that I realise I still have his phone in my hands."
    play audio "audio/sfx/vibrate.ogg"
    n "But just as I move to return it to its rightful owner, the screen immediately lights up and starts to vibrate."
    hide ren
    hide moth
    with dissolve
    n "Perhaps it's muscle memory kicking in from all the times my own phone would go off, but I find myself unconsciously lifting it up to look at the screen before realising what I had just done."

    if status_olivia == False and status_teo == False:
        npct "i understand why the offering wouldn't work with o, but did u REALLY need to fish out that—"
    elif status_olivia == False and status_teo == True:
        npct "that was you, right? that was ur offering it accepted yesterday? why? how???? she's not even the real o—"
    elif status_olivia == True and status_teo == False:
        npct "i'm guessing ur the reason it's placated again? also, GROSS dude. don't tell me u went back and fished out his—"
    else:
        npct "{b}{color=#a30b11}[[ {/color}{glitch=20.0}{color=#a30b11}{b}REDACTED{/b}{/color}{/glitch}{color=#a30b11} ]{/color}{/b} ? what did u do? everything is back to normal again and its WEIRD. who did you offer—"

    n "[shit!c], what exactly are you doing right now, [ch_angel]? I shouldn't be reading through someone else's private notifications like this. And yet…"
    n "I couldn't help but feel…"

    $ choice_style = "box"
    menu:
        "I feel weirded out, ask [ch_ren] to leave us alone":
            $ d5_inviteren = False
            $ ren_purity -= 1
            $ ren_decay += 1
            $ affection_ren -= 10
            $ persistent.d5_dismissren = True
            n "I couldn't shake off the feeling that something {b}just{/b} wasn't right."
            n "While the text ultimately seems harmless — and granted, I had barely any context to go off of — my instincts were telling me not to fall for it."
            n "With a resolute nod, I make my way towards the group and try to grab [ch_ren]'s attention."
            play audio "audio/sfx/walking.ogg"
            show ren happy at tleft
            show moth neutral at tright
            with dissolve
            show ren happy at bpop
            r "Angel! Ah, sorry, did you want to take more photos as well?"
            show ren neutral at spop
            r "Here, I'll move out of the way—"
            y "Actually, I was thinking of taking [ch_moth] back to the pier so I can finish up the rest of the tour. I wanted to return your phone first."
            show ren smirk at spop
            r "Oh, right. Thanks! Here, let me get my towel, and we can all go back to the—"
            y "Um… So I was thinking… Maybe it could just be me and [ch_moth]?"
            show ren sad at spop
            r "You… And [ch_moth]?"
            show ren frown at spop
            r "Don't you want me t'come along?"
            show ren sad at spop
            r "I-Is there something wrong? Did… D-Did I do something wrong?"
            y "N-No! Nothing is wrong. I just didn't realise that having {i}the{/i} real-life Haruko tagging along would be a bit too overwhelming for them."
            y "Once things settle down, maybe we can all meet up again?"
            n "That was a bald-faced lie, but I hope [ch_ren] won't see through it."
            show ren frown at spop
            r "…"
            show ren sad at spop
            r "You really don't want me—? I-I see."
            show ren smirk at spop
            r "Yeah…"
            show ren sad at spop
            extend " Sure…"
            show ren frown at spop
            extend " O-Okay."
            show ren smirk at spop
            r "I'll um—I guess I'll see you later, then? You have my number anyway! I'll… I'll only be a text away!"
            n "If only he knew."
        "I feel fine, hang out with [ch_ren] a little longer":
            $ d5_inviteren = True
            $ affection_ren += 10
            n "What was I thinking, reading private messages like this? [ch_ren] didn't deserve to have his privacy disregarded like this. With a resolute nod, I make my way towards the group and call for [ch_ren]'s attention."
            play audio "audio/sfx/walking.ogg"
            show ren happy at tleft
            show moth neutral at tright
            with dissolve
            show ren happy at bpop
            r "Angel! Ah, sorry, did you want to take more photos as well?"
            show ren neutral at spop
            r "Here, I'll move out of the way—"
            y "Actually, I was thinking about heading to the manga store to check out some of the new merch. Do you want to join us? Oh—And here's your phone."
            show ren smirk at spop
            r "Hehe, that sounds like a good idea! Here, I'll go get our bags while you finish taking your photos."
            show ren happy at spop
            r "Let me know when you're ready to go."
            play audio "audio/sfx/sprinting.ogg"
            hide ren
            show moth neutral at center
            with easeoutleft
            n "Almost like a puppy, [ch_ren] bounds off towards our belongings and starts to pack them up with a blissful smile on his face."
            show moth flushed at spop
            m "Man… He really is just like Haruko."
            show moth blushing at spop
            m "Gah! I want him to turn into a sticky hand just so I can repeatedly throw him against a wall over and over again."
            y "…Pfft! Your levels of cuteness aggression genuinely terrify me sometimes."
    $ choice_style = "default"
################################################################################
## MAINT STREET SCENE
################################################################################ 
label day5_streetscene:
    scene beach_street_day
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/street.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/movement.ogg"
    play audio "audio/sfx/running.ogg"
    show peffect
    $ ren_outfit = "normal"
    $ moth_outfit = "normal"
    if d5_inviteren == False:
        show moth smirk at center
    else:
        show ren happy at tleft
        show moth smirk at tright
    with Fade(1.0, 2.0, 1.0)

    $ location_moth = "pier"
    $ location_violet = "home"
    $ location_elanor = "library"
    $ location_ren = "pier"
    $ location_conan = "library"
    $ location_jae = "pier"
    $ location_leon = "home"
    $ location_teo = "home"
    $ location_olivia = "work"
    $ location_kiara = "oh"

    if d5_inviteren == False and meter_gore >= 1 and ren_decay >=4:
        jump day5_streetscenealt
    elif status_olivia == False or status_teo == False:
        n "The moment we reach the main street, I immediately pick up on the lack of… well, noise. Aside from a lone cop car, there were hardly any other cars or people on the street, and most of the stores appeared to be closed."
        n "Weird. Was today a public holiday? I doubt it, considering I was initially supposed to work today."
    else:
        n "The sounds of lively chatter and vehicles driving by grow louder as we make our way towards the main street. Strange. Everything seems so busy and chaotic today. Was there some kind of event going on?"
        n "I doubt it, considering [ch_elanor] and I were both in charge of keeping the library's community board up to date. I would've known if there was an event happening."

    if d5_inviteren == False:
        play ambience "audio/ambience/heartbeat.ogg" fadein 1 fadeout 1
        play music "audio/bgm/The One Who Approaches.ogg" fadein 1 fadeout 1
        n "But before I can dwell on it any longer, I suddenly find myself being thrust forward and onto the road by an unknown force — before [ch_moth] reaches out a hand to pull me back."
        play audio "audio/sfx/item.ogg"
        play audio "audio/sfx/shoes alt.ogg"
        show true_red:
            alpha 0.3
        hide true_red with owie
        y "Oof—!" with vpunch
        play audio "audio/sfx/found you.ogg" 
        show killer at center behind moth with dissolve
        show moth frown at bpop with vpunch
        play audio "audio/sfx/shoes alt.ogg"
        show moth frown at tleft with easeinright
        show moth frown at cleft, bpop with easeinright
        n "I turn around to confront the offender, but I'm not able to get a good look at their face because of the mask and hoodie they're wearing."
        n "Despite that, they seem to exude something… {b}sinister{/b} with the way their shoulders hunch forward as their hands remain in their pocket."
        n "…What if they were hiding a knife in there?"
        play audio "audio/sfx/shoes alt.ogg"
        show moth frown with easeinright:
            xalign 0.02
        n "Any semblance of a retort dies on my tongue as I take a step back towards [ch_moth]. I can feel them reach for my arm, and with one more glance, I turn away and hurriedly pace down the street."
        play audio "audio/sfx/shoes alt.ogg"
        play audio "audio/sfx/sprinting.ogg"
        show moth frown at center
        hide killer
        with easeoutright
        stop ambience fadeout 2.0
        play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
        n "What the hell was that?"
        show moth angry at spop
        m "[ch_angel]? Hey, are you okay? What the hell was their problem?"
        show moth sad at spop
        m "I mean, c'moooon. How hard is it to look where you're going? That dude's a grade A [asshole]! {i}No{/i}… They're the S tier of [asshole]s!"
        n "[ch_moth]'s words of reassurance do little to comfort me, but I appreciate hearing them nonetheless. I just couldn't seem to shake off the eerie feeling or calm my rapid heartbeat after that sudden encounter."
        n "What if that was my stalker? The person who was—"
        show moth neutral at spop
        m "—Maybe we should head back to your place? I guess peak hour is starting soon since {i}everyone{/i} seems to be in such a hurry."
        y "Y-Yeah… Good idea."
        n "Whether or not [ch_moth] picks up on my hesitancy is lost on me. I don't want to worry them — let alone ruin what's supposed to be a fun day for them — so I try my best to mask my fears for their sake."
        n "Also, I won't lie… the thought of being within the safety of my own home is a genuinely comforting idea."
        n "Having [ch_moth] close by somehow seems to boost my confidence as well, and from that thought alone, I give a resolute nod and lead them towards my apartment."
        jump day5_branchingdeadend
    else:
        pass
    
    play ambience "audio/ambience/heartbeat.ogg" fadein 1 fadeout 1
    play music "audio/bgm/The One Who Approaches.ogg" fadein 1 fadeout 1
    n "But before I can dwell on it any longer, I suddenly find myself being thrust forward and onto the road by an unknown force — before [ch_ren] reaches out a hand to pull me back."
    
    play audio "audio/sfx/item.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show ren sad at bpop with easeinleft:
        xalign 0.25
    show true_red:
        alpha 0.3
    show moth angry at spop
    hide true_red with owie
    y "Ack!" with hpunch
    n "Once the initial shock wears off and I gather my bearings, I whip my head around to figure out what — or who — tried to push me."
    n "But it proves difficult with [ch_ren]'s large frame blocking my view, so I remove his hand from my shoulder and sidestep around him."
    
    play audio "audio/sfx/found you.ogg"
    show killer at center behind moth, ren with dissolve
    show moth frown at bpop with vpunch
    show moth frown at tright with easeinleft
    play audio "audio/sfx/shoes alt.ogg"
    show moth frown at cright, bpop with easeinleft
    
    n "When I do, I come face to face with a dark, hooded figure who doesn't even bother to acknowledge our existence."
    n "What the? This [asshole] {b}really{/b} tried to push me into oncoming traffic and walked off as if nothing had happened?! Wait…"
    n "Was this the person [ch_violet] was talking about? The tall build, the hooded jacket… The only thing that's missing is the crazy amount of belts on their leg."
    n "So this is my stalker?! I have half a mind to just… pull down their mask and hoodie to expose their identity, but I didn't want to cause a scene or make matters worse. [ch_ren], however, seems to have other plans."
    n "Before I can react, he surges towards the hooded stranger with a nasty scowl on his face."
    play audio "audio/sfx/item.ogg"
    show ren angry at tleft, bpop with easeinright
    if persistent.streamermode == True:
        r "What's your problem?" with hpunch
    else:
        r "The fuck's your problem?" with hpunch
    npc "…"
    show ren frown at spop
    r "Not even goin' to apologise?"
    play audio "audio/sfx/fabric.ogg"
    n "When no response comes, [ch_ren] reaches for their shoulder to get their attention. All it does is cause them to turn around slightly — before they shrug it off and break into a sprint."
    
    play audio "audio/sfx/shoes alt.ogg"
    play audio "audio/sfx/sprinting.ogg"
    hide killer with easeoutright
    show moth frown at bpop with hpunch
    show moth frown at tright with easeinleft
    stop ambience fadeout 2.0
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    
    n "Everything happens in a blur, and just as the smudge of black fades from my view, [ch_ren]'s pink hair replaces it as he gently grips my arms to ground me."
    show ren sad at spop
    r "A-Are you alright? Did they hurt you?"
    n "Concern and worry couldn't even {b}begin{/b} to describe the range of emotions present on his face. [ch_ren] peers even closer when I don't respond to his questioning, and in that moment, I find myself too stunned to speak."
    n "All of my attention goes towards the warmth radiating from his sudden closeness and the soft, blue eyes peering into mine with so much worry."
    n "I can feel [ch_ren]'s fingers press deeper into my shoulders — not enough to hurt me, but present enough to anchor me — as he pulls me even closer towards his chest."
    n "I feel safe being surrounded by his concerned presence, and it was nice to know that he cared so much for my well-being — so much so that he'd willingly pick a fight with some stranger for a simple apology."
    n "But the moment only lasts for so long before I realise that he's trying to get me to respond."
    show ren frown at spop
    r "—A-Angel? What's wrong?"
    show moth sad at spop
    m "You okay, [player_fl]? Do you know them or something?"
    y "N-No… And I'm fine. I just—They scared me, is all."
    y "This has never happened to me before."
    show ren sad at spop
    r "Y'sure you sure you're fine? You're still shaking."
    show moth angry at spop
    m "Want to sit down? Should I… Should I call the cops or something?"
    n "I can barely hear [ch_moth]'s words over the rapid sounds of my heart beating and the ringing in my ears."
    n "I wasn't able to see that person's face because of their mask, but their scent… I could recognise that smell anywhere. It was something unmistakably earthy and muddy, and it felt oddly familiar in some way."
    n "Before I can let my thoughts travel any further, I notice my friends are still staring at me with concerned looks. Not wanting them to worry, I mask my fear with a determined glint in my eye and try to ease the mood."
    y "M-Maybe we should head home instead."
    show ren frown at spop
    r "Sure, but… Are you {i}sure{/i} you're alright? You still seem a bit dazed, [ch_angel]."
    y "Yeah… I'm fine! We should probably get off the street, though. I suppose peak hour is starting soon."
    show moth angry at spop
    m "That might explain why they were in such a rush… Still, it wouldn't hurt to apologise for bumping into someone."
    show moth neutral at spop
    m "Well, whatever! You said you wanted to head home?"
    show ren neutral at spop
    r "[they!c] did. So… Where did you want to go, Angel? I-If you'd like, we can go to my apartment. It's not far from here."
    if d2_visitren == True or d4_visitren == True:
        show ren smirk at spop
        r "Ah, but you already know that, don't you? Hehe."
    else:
        pass
    show ren happy at spop
    r "Or… We can go back to your place if you prefer?"

    $ choice_style = "box"
    menu:
        "\"We should go to my place.\"":
            $ choice_style = "default"
            $ affection_ren -= 10
            y "My apartment might be best. It's not far from here either."
            n "Purely on the happenstance of that [asshole] being my stalker, I'm sure they wouldn't have the guts to try anything while I still had company over."
            n "And somehow… having [ch_moth] and [ch_ren] nearby seems to boost my confidence, so I boldly commit to my decision with a nod of my head."
            y "Is that fine with you guys?"
            show ren happy at spop
            r "Yeah! Of course! It's fine!"
            n "[ch_moth] still seems a bit peeved by the person who bumped into me, but they still nod their head at my question."
            y "Alright then, let's go."
            jump day5_angelapartmentbranch
        "\"We should go to [ch_ren]'s place.\"":
            $ choice_style = "default"
            $ affection_ren += 10
            $ ren_purity += 1
            n "Somehow, I felt a lot more comfortable going back to [ch_ren]'s apartment instead of my own."
            n "I don't want to risk [ch_moth]'s safety either, so I try my best to convince myself that this {b}really is{/b} a good idea after all. With a resolute nod of my head, I turn to [ch_ren] with a meek smile."
            y "Would it be alright if we go to your apartment?"
            show ren happy at spop
            r "Yes! Of course! It's totally fine! It's not far from here, anyway."
            n "[ch_moth] still seems a bit peeved by the person who bumped into me, but they still nod their head at my question."
            y "Alright then, let's go."
            jump day5_renapartmentbranch

################################################################################
## What do you MEAN he's a yandere that HURTS people????????? That's crazy!!!!!
################################################################################ 
label day5_streetscenealt:
    n "The moment [ch_moth] and I reach the main street, I immediately pick up on the lack of… well, noise. Aside from a lone cop car, there were hardly any other cars or people on the street, and most of the stores appeared to be closed."
    n "Weird. Was today a public holiday? I doubt it, considering I was initially supposed to work today."
    n "Suddenly, [ch_moth] comes to an abrupt stop in front of one of the only open stores on the street; a quaint, little gift shop just opposite of the icecream parlour."
    n "The storefront itself is warm and inviting, though with the limited amount of space and endless amount of clutter inside, it didn't seem to be designed to fit more than a few customers at a time."
    show moth neutral at spop
    m "Ooh! Do you mind if I check this store out real quick? I wanna get a few souvenirs for my family back home."
    y "Go for it."
    show moth happy at spop
    m "Thanks! I won't be long!"
    play audio "audio/sfx/running.ogg"
    hide moth with easeoutright
    n "Leaving my friend to do their own thing, I step away from the gift shop and take a moment to absorb the weird… eeriness of the scenery before me."
    n "It still made absolutely {b}no sense{/b} for most of the buildings to be closed for the day, nor the fact that there were barely any people out on the street. Did it have something to do with what had been on the news?"
    n "There's been a few murders happening recently — and to be fair, I probably {b}should{/b} be more concerned about them — but this kind of macabre stuff… It's normally unheard of, especially in Corland Bay."
    n "This little seaside town has always prided itself on how safe and close-knit everything is, so all this talk about murders and killings? It didn't make any sense."
    n "It's almost like I carried the worst parts of the city with me when I moved back."
    n "Ugh. What a depressing thought."
    stop music fadeout 7
    n "Shaking my head, I decide there's no point in dwelling over this — not when I have more pressing matters to focus on. I'm {b}supposed{/b} to be having fun with [ch_moth] today, and—"
    play ambience "audio/ambience/heartbeat.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/item.ogg"
    play audio ["<silence 0.7>", "audio/sfx/shoes alt.ogg"]
    show true_red:
        alpha 0.3
    hide true_red with owie
    y "Mmph—!" with vpunch
    
    play music "audio/bgm/The One Who Approaches.ogg" fadein 1 fadeout 1
    n "Without warning, a sturdy pair of hands clamp over my mouth and chest before I'm being dragged backwards. Panic surges through me like electricity, and my heart races as I struggle against the grip tightening around me."
    scene street_alleyway_night
    with dissolve
    n "Almost desperately, I try to fight back as I get pulled off the street and into a dark alleyway. A scream claws its way up my throat, but it dies on my tongue as the gloved hand holds my jaw closed and prevents any sound from coming out."
    n "What is happening?!" with vpunch
    stop ambience fadeout 2.0
    n "Without wasting a second, I…"

    $ choice_style = "box"
    menu:
        "Try to kick their legs":
            $ affection_ren -= 10
            $ ren_decay += 1
            $ persistent.d5_kickfigure = True
            n "While my upper half may be restrained, my legs sure weren't."
            n "With all the force I can muster, I swing my right leg into the air before hurling back into my assaulter's knee. A strained cry of pain comes from behind me before my entire world starts to spin."
            play audio "audio/sfx/plate.ogg"
            play audio "audio/sfx/shatter.ogg"
            play audio "audio/sfx/paper.ogg"
            play audio ["<silence 0.2>", "audio/sfx/glass.ogg"]
            scene other_dark with vpunch
            play audio "audio/sfx/paper.ogg"
            play audio ["<silence 0.2>", "audio/sfx/item.ogg"]
            n "In less than a second, I'm slammed against a large dumpster and thrown to the ground. The sounds of boxes crashing and glasses shattering are all I hear as I roll onto my side, only to feel something grab my ankles and drag me forwards."
            n "A shriek finally escapes me, and just as I try to kick my assaulter again, a flash of pink moves from above me."
            n "Was that…?"
            play audio ["<silence 0.3>", "audio/sfx/fabric.ogg"]
            play audio "audio/sfx/running.ogg"
            n "I watch in complete horror as [ch_ren] brandishes a broken glass bottle in one hand and jams it into the person's rib over and over and over again — with each thrust becoming more ruthless than the last."
        "Don't do anything":
            $ affection_ren += 10
            n "Doing something would ultimately make matters worse, so I purposefully remain still and let my assaulter drag me deeper into the alleyway."
            play audio "audio/sfx/plate.ogg"
            play audio "audio/sfx/shatter.ogg"
            play audio "audio/sfx/paper.ogg"
            play audio ["<silence 0.2>", "audio/sfx/glass.ogg"]
            scene other_dark with vpunch
            play audio "audio/sfx/paper.ogg"
            play audio ["<silence 0.2>", "audio/sfx/item.ogg"]
            n "In the chaos, they end up knocking over a cardboard box filled with empty bottles as they tumble to the floor with a loud clatter — before a large, gloved hand wraps itself around my neck and squeezes down on my windpipe."
            play audio "audio/sfx/item.ogg"
            y "Grk—!" with vpunch
            n "Their other hand moves along the exposed seams and pockets of my outfit as if to look for something, and it's then that I realise what exactly is happening…"
            n "But before I can react, a flash of pink moves from the corner of my eye."
            n "Was that…?"
            play audio ["<silence 0.3>", "audio/sfx/fabric.ogg"]
            play audio "audio/sfx/running.ogg"
            n "I watch in complete and utter horror as [ch_ren] shoves the person off of me, brandishes a broken glass bottle in one hand, and plunges it into their neck over and over and over again — with each thrust becoming more ruthless than the last."
    $ choice_style = "default"
    play audio ["<silence 0.4>", "audio/sfx/stab.ogg", "<silence 0.3>", "audio/sfx/stab.ogg"]
    play audio "audio/sfx/stab.ogg"
    play audio ["<silence 0.3>", "audio/sfx/splat.ogg", "<silence 0.5>", "audio/sfx/splat.ogg"]
    play audio ["<silence 0.5>", "audio/sfx/shatter.ogg"]
    n "The gruesome sounds of glass shards breaking, skin squelching, painful grunting, and blood dripping all blend together in this dank alleyway… yet I can't find it in me to look away."
    play audio ["<silence 0.2>", "audio/sfx/stab.ogg", "<silence 0.4>", "audio/sfx/stab.ogg"]
    play audio ["<silence 0.3>", "audio/sfx/splat.ogg", "<silence 0.3>", "audio/sfx/splat.ogg"]
    n "All I can do is watch in silence as [ch_ren] repeatedly stabs my assaulter without a single hint of remorse. His usual soft eyes are void of any emotion, and he doesn't relent until they go limp in his hold and slump to the ground with an audible thump."
    play audio [ "audio/sfx/bone alt.ogg", "<silence 0.4>", "audio/sfx/splat.ogg"]
    n "But even then, [ch_ren] doesn't stop. He lifts his leg and starts to kick them now — finding some kind of sick pleasure in watching their body recoil and hit the wall with each heavy blow."
    play audio ["<silence 0.9>", "audio/sfx/bone alt.ogg"]
    n "My blood goes cold the moment the dull sound of bones cracking reaches my ears, but my rapid heartbeat drowns it all out. And when [ch_ren] turns to me, there's an almost predatory look in his eyes that keeps me rooted in place."

    scene other_dark
    show CG D5_ALLEYWAY1
    play music "audio/bgm/Tears Of A Murderer.ogg" fadein 1 fadeout 1
    hide screen dayscalendar
    show screen menuwu
    $ quick_menu = False
    $ persistent.cg_d5_alleyway1 = True
    with Fade(1.0, 1.0, 1.0)

    n "His breathing is laboured and ragged, yet what intrigues me the most is the the way the corners of his lips twitch into an almost sickeningly sweet smile."
    show CG D5_ALLEYWAY2 with dissolve
    $ persistent.cg_d5_alleyway2 = True
    r "Hah… Haaah…"
    r "[player_fl]-[ch_angel]…"
    n "In an instant, he's forgoing his bloodied victim to reach for me. I can feel him cup my face with so much tenderness that it almost makes the moment feel… romantic."
    n "But the rough texture of [ch_ren]'s blood-soaked hands against my skin pulls me back to reality, and sends a noticeable shiver down my spine as he checks my body for any signs of damage."
    scene street_alleyway_night
    $ quick_menu = True
    hide screen menuwu
    show screen dayscalendar
    show peffectp
    with dissolve

    n "When his eyes meet mine, I…"

    $ choice_style = "box"
    menu:
        "Encourage [ch_ren]'s violent behaviour":
            $ choice_style = "default"
            $ d5_witnesskill = True
            $ angel_sanity += 1
            $ ren_purity -= 1
            $ ren_decay += 1
            $ ren_blood = True
            show ren lovesick z at center with dissolve
            y "Th-Thank you…"
            n "The initial shock still hasn't worn off yet, but at least I can feel my legs again. [ch_ren] must've taken notice, as he gently moves me towards the wall to lean against it, before he sinks down to the ground alongside me."
            show ren sad z at spop
            r "I-I saw what happened after your friend left you alone. Are you alright?"
            y "…Is {i}that{/i} person alright?"
            n "[ch_ren] glances over his shoulder towards the body he'd practically maimed."
            show ren neutral z at spop
            r "They're not dead, thankfully. Just… Unconscious."
            show ren sad z at spop
            r "But if you're feeling fine, we should get out of here before the cops come."
            y "…Shouldn't we tell them what happened? Isn't this a literal reportable offence?"
            show ren smirk z at spop
            r "That's… a good idea. B-But imagine all the trouble this would cause us—"
            show ren sad z at spop
            r "This might even jeopardise your job at the library, too. And… There's also your friend we need to consider."
            n "…Right, [ch_moth]. I shouldn't stress them out with all this. Traumatic experience or not, I still want their impression of Corland Bay to be a good one."
            y "You've got a point."
            if angel_sanity >= 3 and ren_decay >= 3:
                n "Before I can get lost in my thoughts, the sleeves of [ch_ren]'s cardigan come into view as he starts to wipe the blood from my face. There's a tender look in his eye, and I can't help but feel weak in the knees at the vulnerability of it all."
                show ren lovesick z
                n "In return, I reach out to smear some of the red on his cheek as well. [ch_ren] almost seems to {b}keen{/b} at my touch — but just as I bring my blood-stained finger towards his mouth for him to taste, he cuts me off."
            else:
                n "Before I can get lost in my thoughts, the sleeves of [ch_ren]'s cardigan come into view as he starts to wipe the blood from my face. There's a tender look in his eye, and I can't help but feel weak in the knees at the vulnerability of it all."
            show ren neutral z at spop
            r "Here, why don't I clean up this scene a bit? Make it look like a mugging attempt gone wrong."
            show ren smirk z at spop
            r "Because… that's what this was, {i}right?{/i}"
            y "Yeah… A mugging attempt…"
            show ren neutral z at spop
            r "And you'll go back to that bench, wait for your friend, and pretend this never happened, right?"
            y "…Sure. Y-Yeah, okay."
            show ren smirk z at spop
            r "Trust me, everything will be fine. I'll make sure nothing incriminating leads to us. All y'gotta do is act like nothing is wrong."
            show ren happy z at spop
            r "I know you can do that f'me. Can't you, [ch_angel]?"
            n "I can only offer him a meek nod."
            if rem_boyfriend == True and rem_touch == True:
                n "In return, [ch_ren] leans down and presses a deep kiss against my lips."
                show ren lovesick z at spop
                r "…Haaah~ You're always so good for me."
            else:
                show ren smirk z at spop
                r "…You're always so good f'me."
            jump day5_renapartmentbranch
        "Discourage [ch_ren]'s violent behaviour":
            $ choice_style = "default"
            $ ren_blood = True
            show ren lovesick z at center with dissolve
            if persistent.streamermode == True:
                y "…What the actual f—"
                y "What was that?! [ch_ren]!"
            else:
                y "…What the actual {i}fuck{/i} was that?! [ch_ren]!"
            show ren sad z at spop
            r "Are you alright? Did they hurt you?"
            n "Completely ignoring my words, [ch_ren] continues to caress my face as he peers down at me. But the sickening feeling of having someone else's blood against my skin makes my stomach churn, so I shove him off and stumble back."
            play audio "audio/sfx/item.ogg"
            play audio "audio/sfx/shoes alt.ogg"
            show ren sad with vpunch
            n "My eyes widen in horror when I almost trip over the lifeless body lying on the floor, and it's then that I realise…"
            y "[shit!c]—! Are they… dead? This can't be real…"
            y "[ch_ren], you just killed someone!"
            show ren angry at spop
            r "…They tried t'kill {i}you{/i}, [ch_angel]. They had it coming."
            y "That doesn't mean you should've shanked them to death!"
            show ren frown at spop
            r "I should've done {i}worse.{/i} I mean, you're practically shakin' like a leaf right now because of 'em."
            show ren angry at spop
            if persistent.streamermode == True:
                r "{size=-6}That piece of crap deserved it. We should leave 'em to rot here.{/size}"
            else:
                r "{size=-6}Fuckin' piece of shit deserved to die. I should've made 'em choke on glass.{/size}"
            show ren happy at spop
            r "Ah, b-but… Don't worry, you're safe now. I won't let anyone else hurt you."
            y "What?! You didn't save me from anything, you've just {i}incriminated{/i} me! You're…"
            y "You're a murderer!"
            show ren smirk at spop
            stop music fadeout 5
            r "…A murderer? Is that what you really think of me?"
            play music "audio/bgm/Lonely Doll.ogg" fadein 1 fadeout 1
            show ren lovesick at spop
            r "'Sides, I'm doing this for you! It's only fair! You've done the same for me, back when we were k—"
            y "I think I'm going to be sick."
            show ren lovesmile at spop
            r "Here, sit down. I'll go 'n get you some—"
            y "No! You've done enough! A-And—Don't touch me! Don't come near me!"
            show ren frown at spop
            r "A-Angel…"
            y "I said no!"
            show ren sad at spop
            r "[ch_angel]—"
            show ren angry at spop
            r "…"
            show ren sad at spop
            r "H-Hey, please be careful. You're… You're going to trip and hurt yourself if y-you keep—"
            if persistent.streamermode == True:
                n "Why, of all times, was [ch_ren] trying to act all shy and timid now?! What is wrong with him?!"
            else:
                n "Why, of all times, was [ch_ren] trying to be shy and timid now?! What the fuck is wrong with him?"
            show ren lovesick at spop
            r "Here, I-I can fix this… Don't worry, I can… I'll…"
            show ren sad
            y "You can't just bring someone back to life after stabbing them and watching them bleed out!"
            y "You can't stop the police from showing up at my doorstep!"
            y "You can't—Ugh! This was never supposed to happen! I left New Salvus to get {i}away{/i} from all of this, and—"
            n "My head starts to throb the more I raise my voice."
            n "He's insane. Everything about this situation is insane."
            hide ren with dissolve
            n "My legs feel like jelly as I slowly back away from [ch_ren]'s outstretched hands and the dead body lying on the floor. My back hits the wall, and I desperately clutch onto it in an attempt to steady myself."
            n "Unease settles within my chest as I watch [ch_ren] turn back towards the body and crouch down. And when he starts muttering something under his breath, a dizzying wave suddenly washes over me."
            n "Black clouds of smoke start to form and swirl around my feet in a mesmerising pattern, before my entire being is covered in it and it becomes all I see."
            n "It causes my head to feel lighter — and just when I think I'm {b}finally{/b} free from all the nausea and panic — [ch_ren]'s shadowed form reaches for me once more from within the fog and engulfs me."

    $ ren_blood = False
    jump day5_deadend

################################################################################
## ANGEL AND THEIR RAGGEDY APARTMENT TYPE BEAT
################################################################################ 
label day5_angelapartmentbranch:
    scene other_dark
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 2.0, 1.0)

    $ location_moth = "oh"
    $ location_ren = "oh"

    n "I'm not sure who exactly suggested it, but once we settle into my apartment, we all find ourselves huddled in the kitchen with a recipe pulled up on [ch_ren]'s phone."
    n "It was by some miracle that we had all the necessary ingredients in my pantry, though the only thing missing was a tablespoon of sugar."
    n "Yeah, one single tablespoon."

    scene angel_kitchen_day
    show peffect
    show moth angry at tleft
    show ren frown at tright
    with GlitchDissolve
    
    show moth angry at spop
    m "It's fine. I doubt it'd taste any different whether or not we add sugar."
    show ren sad at spop
    r "B-But the recipe calls for sugar."
    show moth smirk at spop
    m "I'm sure the recipe will continue to live a long and prosperous life without it."
    show ren frown at spop
    r "Didn't you read the chef's family story? The sugar is mandatory."
    show moth happy at spop
    m "I honestly skipped over it."
    n "[ch_ren] genuinely looks heartbroken at the prospect of [ch_moth] skipping past the long-winded story about how the recipe had been passed down from generation to generation. And I had to admit, the sight {b}was{/b} kind of funny."
    n "But the bickering could only go on for so long before it started to become something more serious."
    show moth smirk at spop
    m "It's fine, [ch_ren]. Besides, we'd only waste time going to the store just to buy some."
    show ren sad at spop
    r "I can get some delivered here. A-And what if [ch_angel] needs sugar for something else later? [they!c]'d have to go out of [their] way to buy it."
    show ren neutral at spop
    r "We'd save more time by doing it now."
    show moth frown at spop
    m "But we'd {i}still{/i} have to wait. And it's just a tablespoon."
    show ren angry at spop
    r "It's {i}not{/i} just a ta—"
    y "Alright! Look, we shouldn't be arguing over this."
    n "Once I speak up, the two of them immediately pipe down. I catch a glimpse of [ch_moth] rolling their eyes at [ch_ren]'s reaction — which was to stiffen his lip, pick at his jaw, and look down at his feet."
    show moth sad at spop
    m "Well then, what do you think we should do?"
    show ren sad at spop
    r "D-Don't make [ch_angel] decide."
    show moth frown at spop
    m "Why not? It's not like you're going to agree with me, right?"
    show ren frown at spop
    r "…"
    show ren sad at spop
    r "I still think—"
    y "It's okay, I don't mind."
    n "Whether or not that was true, it was too late for me to take it back. What should I do…?"

    menu:
        "Continue without any sugar":
            $ affection_ren -= 1
            $ affection_moth += 1
            $ affection_jae += 1
            $ affection_olivia += 1
            y "[ch_moth] is right. I don't think we need sugar that badly."
            show ren sad at spop
            r "I-If you say so…"
            show moth happy at spop
            m "Hey. You can still order it if you want. We just don't need to use it right now."
            show ren neutral at spop
            r "If Angel says no, it's fine."
            show moth smirk at spop
            m "And what if [ch_angel] said yes?"
            show ren happy at spop
            r "I'd buy it! In bulk! [they!c]'d never have to worry about buying sugar ever again!"
            show moth angry at spop
            m "…Free will exists, you know."
        "Ask [ch_ren] to do an online delivery":
            $ affection_ren += 1
            $ affection_moth -= 1
            $ affection_conan += 1
            $ ren_purity += 1
            show ren happy at bpop
            r "Y-Yeah! Sure! Of course!"
            show moth angry at spop
            m "…"
            show moth sad at spop
            m "Well, alright. I suppose it {i}might{/i} make a difference after all."
            show moth happy at spop
            m "I've been watching this new cooking anime recently, and I learned that—"
            show moth flushed at bpop
            m "O-Oi! [ch_angel] only asked for sugar; you don't need to buy any [favourite_snack]s!"
            show ren sad at spop
            r "It says here that you'll save more if you spend over fifty dollars… And the shipping becomes free, as well."
            show moth frown at spop
            m "That's a load of bull[shit] to get you to spend more! Here, let me see."
            n "In the end, the two ended up curating an entirely new grocery list for me — which made their entire argument about waiting kind of redundant."
        "Suggest asking your neighbours":
            $ affection_violet += 1
            $ affection_elanor += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            show moth happy at spop
            m "Oh! Good idea! Man, why didn't we think of that?"
            show ren neutral at spop
            r "I-I can go ask if you'd like."
            y "It's fine. I'll quickly pop over to [ch_violet]'s place and see if she has any sugar. You guys keep working on the main dish. I'll be just a few minutes!"
            show ren frown at spop
            r "W-Wait!"
            scene other_dark
            play audio "audio/sfx/movement.ogg"
            with dissolve
            m "{size=-6}Now that [player_fl] is gone, did [they] ever ask you to wear Haruko's cooking outfit?{/size}"
            r "{size=-6}What? …[player_fl]-[ch_angel]! Please come back!{/size}"
            n "Chuckling at their interaction, I make my way towards [ch_violet]'s door."
            jump day5_visitviolet
        "Don't say anything":
            $ affection_teo += 1
            show ren frown at spop
            r "S-See? You shouldn't have made [them] choose. It's okay, we can just… we'll continue without any sugar."
            show ren sad at spop
            r "I'm sorry for being so pushy, Angel."
            show moth angry at spop
            m "…"
            show moth frown at spop
            m "I'm sorry too."
            show moth sad at spop
            m "I'm so used to living in a rowdy household; sometimes I {i}need{/i} to be firm on making the final decisions. Otherwise, my siblings will just continue to argue and yell at each other."
            show ren sad at spop
            r "…"
            show moth smirk at spop
            m "Heh, judging by that reaction, I'm guessing it's the same for you, too?"
            show ren flushed at spop
            r "N-No, actually. I wasn't allowed to talk back to anyone in my family. If I did, I'd have to—"
            show ren frown at spop
            r "Um… I-I'd have to…"
            show ren blushing at spop
            r "…Apologise! Y-Yeah, they'd always… My parents would always make me say sorry for raising my voice."
            show ren sad at spop
            r "That's all."
            show moth angry at spop
            m "Oh? Well then, that's… Uhh—"
            show moth sad at spop
            m "Maybe we should move on to something else?"

################################################################################
## YOU GOTTA DO DA COOKING BY THE BOOK YOU KNOW YOU CAN'T BE LAZ
################################################################################ 
label day5_angelcooking:
    scene other_dark
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve

    $ cam_feed = False

    n "With everything settled, we all go back to making dinner."

    if d2_visitren == True:
        n "Admittedly, I was a little wary of letting [ch_ren] watch the stove — considering how he'd once burnt an entire pan of pancakes — yet he seems to be doing well so far."
    else:
        n "Admittedly, I was a little wary of letting [ch_ren] watch the stove — considering how distracted he was with something on his phone — yet he seems to be doing well so far."

    n "[ch_moth], however, is all too happy to wash the dishes, which leaves me in charge of dumping the remaining vegetables into the pan while [ch_ren] stirs."

    scene angel_kitchen_day
    show ren smirk at center
    show moth neutral at cright
    with dissolve

    show ren smirk at spop
    r "You know, [player_fl]… If you were a vegetable, you'd be a cute-cumber."
    show moth happy at spop
    m "Criiinge."
    y "Well, if you were a potato, you'd be a sweet one."
    show ren blushing at spop
    r "…!"
    show ren flushed at spop
    r "Y-You think I'm sweet? H…Haaah~ Hahaha…"
    show moth smirk at spop
    m "Eugh! You two are acting like an old married couple now. Grooooss."
    show moth happy at spop
    m "Can we go back to the conversation about [ch_ren] not knowing the difference between a cucumber and zucchini?"
    show moth smirk at spop
    m "Because it's kinda funny watching him—"
    show ren lovesick at spop
    r "{size=-6}M-M-M-Married…{/size}"
    n "It's like he didn't hear a word [ch_moth] said."
    show ren flushed at spop
    r "We really look like we're married—?"
    y "…Uhh, [ch_ren]? Your hand is getting awfully close to the flame."
    play audio "audio/sfx/glass.ogg"
    show moth angry
    show ren angry at bpop with vpunch
    show moth angry with easeinright:
        xalign 1.0
    r "Huh? Ah—[shit!c]! I didn't notice."
    y "You… didn't notice?"
    n "Now that I'm here thinking about it, [ch_ren] {b}did{/b} have quite a number of strange markings littering parts of his hands. Some look like deep cuts, while others closely resemble inflamed blemishes and burn marks."
    n "…Did something happen to him in the past? Was that why he wasn't able to feel the heat coming from the stove?"
    n "Before I can ask, [ch_ren] seems to notice my inquisitive gaze fixated on his hands and beats me to the punch."
    
    show ren smirk at spop
    if d1_inviteren == True:
        r "Curious? I once said that I'd tell you about my entire life story, didn't I?"
        show ren neutral at spop
        r "All y'have to do is ask, Angel."
    else:
        r "Curious? I don't mind telling you. I don't like keeping secrets from you anyway."
        show ren neutral at spop
        r "All you need to do is ask me, Angel."
    
    y "…"
    n "Was he really being genuine right now? If so…"
    y "Alright then. How'd you get those burn marks?"
    n "There's a flash of… {b}something{/b} in [ch_ren]'s blue eyes as he steps closer and fills the space between us."
    play audio "audio/sfx/item.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show ren neutral z
    hide moth
    with dissolve
    n "He effortlessly cages me in between his chest and the flat surface behind me, before he leans down and lowers his voice to a hushed whisper that sends a shiver down my spine."
    show ren blushing z at spop
    r "You'll have to keep this secret between you and me, okay? It's… pretty embarrassing."
    show ren smirk z at spop
    r "And no telling your friend, either."
    n "Nodding my head, I try my best to focus on [ch_ren]'s words — and ignore the way his unique scent floods my senses and has me unconsciously leaning closer for more."
    
    ## Hello gaslighting and manipulating king <3
    show ren neutral z at spop
    if li_name == "[ch_leon]":
        r "Well… When I was a kid, I went camping with my mom. It was our first time doing something like this, so we didn't have much experience."
        show ren sad z at spop
        r "I guess kid me wanted to prove just how reliable and capable he could be, so I volunteered to start the campfire while my mom pitched the tent."
    elif li_name == "[ch_violet]":
        r "Well… When I was a kid, I went camping with my sister. It was our first time doing something like this, so we didn't have much experience."
        show ren sad z at spop
        r "I guess kid me wanted to prove just how reliable and capable he could be, so I volunteered to start the campfire while my sister pitched the tent."
    elif li_name == "[ch_moth]":
        r "Well… When I was a kid, I went camping with my family. It was our first time doing something like this, so we didn't have much experience."
        show ren sad z at spop
        r "I guess kid me wanted to prove just how reliable and capable he could be, so I volunteered to start the campfire while everyone else pitched the tent."
    else:
        r "Well… When I was a kid, I went camping with some friends from school. It was our first time doing something like this, so we didn't have much experience."
        show ren sad z at spop
        r "I guess kid me wanted to prove just how reliable and capable he could be, so I volunteered to start the campfire while my friends pitched the tent."
    
    show ren frown z at spop
    r "Biiiig mistake."
    show ren sad z at spop
    r "The fire got waaay out of hand, and before I knew it, the only thing I could feel was the flames scorching my skin and this {i}horrible{/i}, burning sensation tearing me up."
    show ren frown z at spop
    r "The heat ended up marring most of my arms and I suffered a lot of nerve damage from it — and now it's left me practically unable to feel most things."
    show ren angry z at spop
    r "And… What's worse is that my nerves continue to deteriorate with each passing day, no matter how hard I try to prevent it from happening."
    show ren sad z at spop
    r "It's reached a point where I can barely feel anything at all."
    n "As if to prove a point, I hear [ch_ren]'s hand grip the counter by my side — almost alarmingly tight."
    show ren smirk z at spop
    r "But… I guess that's why I always like touching you."
    show ren sad z at spop
    r "It's sad, isn't it? Someone who can hardly discern things by touch no matter how hard they try, yet {i}always{/i} yearning to see just how much they can still feel…"
    show ren smirk z at spop
    r "I want to experience everything I can before it all goes away… And {i}you{/i} make it possible."
    n "Wow. After hearing all of that, it makes me want to…"

    menu:
        "Reach for his hand":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_elanor += 1
            show ren flushed z
            n "As if testing [ch_ren]'s words, I silently reach for his hand on the counter and grasp it tightly in my own. His own eyes widen in surprise before I feel a puff of air against the shell of my ear."
            n "When I glance up, I notice the way [ch_ren]'s gaze seems fixated on the way our fingers are laced together, as his expression shifts into an almost wistful smile that tugs at the corners of his lips."
            n "But before I can open my mouth to speak, the soft and intimate moment is abruptly interrupted — leaving my words unvoiced and hanging in the air between us."
        "Reach for his face":
            $ affection_ren += 10
            $ affection_conan += 1
            $ affection_jae += 1
            $ affection_kiara += 1
            $ ren_purity += 1
            n "He can hardly feel anything in his hands anymore, right? So that means…"
            show ren flushed z
            n "Without a second thought, I reach for [ch_ren]'s face and gently cup his cheek. My thumb runs across his soft skin, and it's then that I notice all the faint freckles and blemishes that litter his face."
            n "Part of me wants to trace them, but I hold back for now."
            y "It's much better like this, right? This way, you can feel {i}everything.{/i}"
            n "His own eyes widen at my words before I feel him nuzzle his face closer into my hands. An almost pitiful smile pulls at his lips — and had I paid a tiny bit more attention, I would've noticed the tears forming in the corner of his eyes as well."
            n "But before I can open my mouth to speak, the soft and intimate moment is abruptly interrupted — leaving my words unvoiced and hanging in the air between us."
        "Reach for his chest":
            $ affection_ren += 5
            $ affection_moth += 1
            $ affection_teo += 1
            $ affection_olivia += 1
            show ren flushed z
            n "Without a second thought, my hands reach out and settle on [ch_ren]'s broad chest. I can feel his heartbeat quicken underneath my touch, and it has me wondering if my own is doing the same."
            y "Feelings are stored here, in the heart — not the hands."
            n "As cliche as it was, [ch_ren] seems to take it with the utmost sincerity. His own eyes widen at my words before I feel him take another step closer, with the only thing preventing us from being chest to chest being my hands."
            n "An almost pitiful smile pulls at [ch_ren]'s lips — and had I paid a tiny bit more attention, I would've noticed the tears forming in the corner of his eyes as well."
            n "But before I can open my mouth to speak, the soft and intimate moment is abruptly interrupted — leaving my words unvoiced and hanging in the air between us."
        "Don't move at all":
            $ affection_leon += 1
            $ ren_decay += 1
            n "Despite [ch_ren]'s words, I choose not to move at all; instead, I remain firmly in place as he continues to peer down at me with half-lidded eyes."
            y "I'm… Sorry to hear that, [ch_ren]."
            show ren smirk z at spop
            r "It's fine. You wanted to know, and I don't mind telling you."
            show ren sad z at spop
            r "Besides, I hate keeping things from you. I like being close to you. And… I'd like it if you'd do the same with m—"
            n "Before [ch_ren] can finish his sentence, the soft and intimate moment is abruptly interrupted — leaving his words unvoiced and hanging in the air between us."
        "{image=14NWY symbol} Reach for his belt" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
            call DLC_day5_kitchen from _call_DLC_day5_kitchen

    play audio "audio/sfx/plate.ogg"
    play audio ["<silence 0.2>", "audio/sfx/glass.ogg"]
    m "Dude! Watch what you're cooking!" with vpunch
    jump day5_angelsleeping

################################################################################
## VISITING VIOLET MY WIFE MY LOVE MY BABYGIRL
################################################################################ 
label day5_visitviolet:
    scene oh_complex_night
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/movement.ogg"
    show peffect
    with GlitchDissolve

    $ persistent.d5_visitviolet = True
    $ cam_feed = True
    $ cam_chance = renpy.random.randint(7,10)
    $ cam_display = renpy.random.choice(cam_list)

    n "As soon as the cursive 'welcome!' mat comes into view, I clear my throat and gently knock on [ch_violet]'s door — making sure to avoid the hanging ivy near the peephole."
    n "It barely takes five seconds before I hear the sound of feet shuffling and my neighbour's head appearing from behind the door."
    play audio "audio/sfx/door.ogg"
    show violet happy at center with dissolve
    show violet happy at spop
    v "Oh, [ch_angel]! Hello! Now isn't this a surprise, hm?"
    y "Hey Vi. I'm sorry to bother you. I was just wondering…"
    y "You don't happen to have some extra sugar I could borrow, do you?"
    show violet neutral at spop
    v "…Sugar? Well, of course! I was {i}just{/i} using some to bake a batch of blueberry cookies the other day."
    show violet happy at spop
    v "Here, I'll be just a moment!"
    play audio "audio/sfx/heels alt.ogg"
    hide violet with dissolve
    n "Before I can respond, [ch_violet] goes back into her apartment — but leaves the door open for me to peer inside. Once more, I'm hit with the calming aroma of lavender and herbs, though the smell of something luxurious is new."
    n "Leaning closer, I pick up on the faint sounds of chatter in the background as well, and it has me wondering… Did [ch_violet] have a guest over?"
    n "Curiosity washes over me, and it's {b}then{/b} that I notice a pair of high-end heels by the door. Were those [ch_kiara]'s shoes?"
    n "They looked an awful lot like…"
    n "I don't have time to wonder for long, however, as [ch_violet] soon returns with a small container full of sugar."
    show violet happy at center with dissolve
    play audio "audio/sfx/heels alt.ogg"
    show violet happy at bpop
    v "Here we go! Is this enough? Or would you like some more?"
    y "Oh, no, this is fine. Thanks, [ch_violet]."
    show violet sad at spop
    v "No problem. Feel free to stop by anytime! You're always welcome here—Oh?"
    n "She follows my gaze towards the pair of heels, and almost shyly, she retreats behind the door with a sheepish smile."
    show violet flushed at spop
    v "Ah! An… Old friend of mine is in town for a while. Her name's [ch_kiara]. We're…"
    show violet blushing at spop
    v "We're catching up and reminiscing about old times together."
    y "[ch_kiara]? You mean… [ch_elanor]'s sister?"
    y "I didn't know you two knew each other! Or that you guys were friends."
    show violet neutral at spop
    v "Hehe! Yes, well, it's… quite a bit more complicated than that, actually."
    n "The faint blush on her cheeks says everything. I have half a mind to tease her, but I ultimately go against it, considering how she literally just let me borrow some of her sugar. Still…"

    menu:
        "Encourage [ch_violet]'s crush":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_violet += 1
            $ affection_jae += 1
            $ affection_kiara += 1
            $ purplebrown = True
            y "A bit more complicated than just friends, huh?"
            y "Does that mean you're planning on giving [ch_kiara] some 'sugar' later, as well?"
            show violet flushed at spop
            v "…"
            show violet blushing at spop
            v "[player_fl]-[player_fl]-[ch_angel]! What are you sugges—"
            k "{size=-6}…Everything alright there, [ch_violet] dear?{/size}"
            n "[ch_kiara]'s concerned voice can be heard somewhere deeper in [ch_violet]'s apartment as she shoots me an incredulous look, though it only gets softened by the red blooming on her cheeks."
            show violet sad at spop
            v "O-Oh, no! Everything's fine! I'm just saying goodbye!"
            k "{size=-6}Well, alright then…{/size}"
            n "Taking the hint, I let out a snort and turn towards my door."
            y "Alright, alright. I'll stop now. Thanks for the sugar, Vi. And…"
            y "No funny business, you two."
            show violet flushed at bpop
            v "…!"
            n "With a wink, I give my neighbour two thumbs up and head back to my own apartment across the hall."
            jump day5_angelcooking
        "Discourage [ch_violet]'s crush":
            $ affection_violet -= 5
            $ affection_teo += 1
            $ affection_kiara -= 5
            y "Oof, maybe it's best to avoid anything 'complicated'."
            y "That normally doesn't lead to anything good, no matter how much time and effort you put into it."
            show violet sad at spop
            v "…You really think so?"
            show violet frown at spop
            v "Mm, perhaps you're right. I mean, maybe it's why things didn't work out the {i}first{/i} time."
            show violet sad at spop
            v "You see, [ch_kiara] wanted more structure in our relationship and valued her career over almost everything else… Including me."
            show violet neutral at spop
            v "Meanwhile, all {i}I{/i} wanted was to go with the flow of life and see where it would take us."
            show violet sad at spop
            v "I suppose… We clashed too much? But it's been years, and we've both changed since then. Or, at least, I think so."
            show violet frown at spop
            v "But… Maybe you have a point. If it was messy and complicated back then, it might still be the same now. Ah—"
            show violet flushed at spop
            v "Apologies! I must be boring you with my musings. Ahem…"
            show violet happy at spop
            v "Thank you for talking to me tonight, [ch_angel]! I hope whatever you're cooking ends up scrumptious!"
            show violet neutral at spop
            v "Save me and Agatha a bite or two if you want! We're always happy to be your personal taste testers."
            show violet frown at spop
            v "Unless… {i}You're{/i} the one who keeps burning everything and setting off the fire alarm?"
            n "I almost choke on my own spit at her words."
            y "Oh, uh… Yeah! Sure can! And… Sorry if I overstepped in any way."
            show violet smirk at spop
            v "No, I think this is what I needed to hear. Admittedly, I've been deliberating over this for far too long. I'm glad that I can finally make up my mind."
            show violet happy at spop
            v "Oh! But here I go again, talking your ear off. I'll let you go now. Toodles!"
            n "With an awkward puff of laughter, I bid my neighbour goodbye and head back to my own apartment."
            jump day5_angelcooking
        "Ask [ch_violet] what she thinks":
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            y "Complicated? What do you mean?"
            show violet smirk at spop
            v "Oh? Are you trying to be sneaky and peek into my love life? Hehe!"
            show violet neutral at spop
            v "Well, all I'll say is that [ch_kiara] and I have given this whole… 'relationship' thing a try several times, but it never ends up working out."
            show violet sad at spop
            v "Oh, but it's never her fault things end so badly! I promise!"
            show violet frown at spop
            v "Though… I suppose it's also why I always want to keep giving 'us' another go."
            show violet neutral at spop
            v "She never makes me feel as though I should stop giving her any more chances, and…"
            show violet sad at spop
            v "I never really know when to put my foot down and say that enough is enough."
            show violet smirk at spop
            v "Hm… I suppose I've got a bit of thinking to do tonight, huh? Ah—"
            show violet neutral at spop
            v "I must be boring you with my ramblings, aren't I? Sorry! I'll let you go now."
            show violet happy at spop
            v "I hope whatever you're cooking ends up scrumptious! Save me and Agatha bite or two if you want! We're always happy to be your personal taste testers."
            show violet sad at spop
            v "Unless… You're the one who keeps burning everything and setting off the fire alarm?"
            n "I almost choke on my own spit at her words."
            y "Oh, uh… Yeah! Sure can! And… Sorry if I overstepped in any way."
            show violet smirk at spop
            v "No, I think this is what I needed to hear. Admittedly, I've been deliberating over this for far too long. I'm glad that I can finally make up my mind."
            show violet happy at spop
            v "Oh! But here I go again, talking your ear off. I'll let you go now. Toodles!"
            n "With an awkward puff of laughter, I bid my neighbour goodbye and head back to my own apartment."
            jump day5_angelcooking
        "Don't say anything":
            $ affection_ren += 1
            $ affection_olivia += 1
            show violet sad at spop
            v "Ahem… So! If that's all you needed…"
            y "Right! Yeah, thanks for the sugar, Vi. I'll make sure to bring over some leftovers to repay you."
            show violet happy at spop
            v "Oh, don't you worry about that! Though… I'm always happy to be your personal taste tester."
            show violet smirk at spop
            v "Unless, of course, {i}you're{/i} the one who keeps burning everything and setting off the fire alarm?"
            n "I almost choke on my own spit at her words."
            y "C-Couldn't be me! Anyway! Thanks again. I'll head off now."
            show violet smirk at spop
            v "Mm! Toodles!"
            n "With a smile, I give my neighbour one final wave and head back to my own apartment."
            jump day5_angelcooking

################################################################################
## HONK SHOOO HONK SHOO HONK SHOOOOOOO
################################################################################ 
label day5_angelsleeping:
    scene other_dark
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 2.0, 1.0)

    $ location_moth = "oh"
    $ location_violet = "home"
    $ location_elanor = "home"
    $ location_ren = "oh"
    $ location_conan = "home"
    $ location_jae = "home"
    $ location_leon = "home"
    $ location_teo = "home"
    $ location_olivia = "home"
    $ location_kiara = "oh"
    
    n "Although dinner ended up being a little toasty, it does little to sour the rest of our evening — despite the slight pout that lingers on [ch_ren]'s features."
    n "We decide to eat in the living room so that we could watch AoG, and eventually we blaze through fourteen episodes — and even a few MeTube theory videos — before the events of the day slowly started to catch up to us."
    scene angel_lounge_night
    with GlitchDissolve
    n "[ch_moth] was the first to let out a yawn, and eventually, the rest of us fell victim to it. I didn't want to leave the warmth of my blankets, but {b}someone{/b} needed to turn my couch into a temporary bed for [ch_moth] to sleep on."
    n "Looking back at them, I see that they're already halfway to dreamland, given the way their head was awkwardly thrown over the seat of the recliner with drool peeking out from the corner of their lip."
    scene angel_bedroom_night
    play audio "audio/sfx/walking.ogg"
    with dissolve
    n "Getting up as quietly as I can, I silently tip-toe towards my bedroom to retrieve a few spare pillows and a blanket. But what I didn't expect was for [ch_ren] to follow close behind."
    n "His presence practically startles me, and it takes all my willpower not to yell out in surprise."
    n "Had he always been so stealthy?! You'd think that with his large and lanky frame, he'd be a little more… noisy, right?"
    n "As if noticing how quiet I've suddenly become, [ch_ren] offers to fill the silence."
    play audio "audio/sfx/shoes alt.ogg"
    show ren flushed at center with dissolve
    show ren flushed at bpop
    r "S-Sorry, I just wanted to see if you needed any help."
    show ren neutral at spop
    r "Here, I can carry these for you and help your friend get set up."
    show ren sad at spop
    r "Did you want to get changed in the meantime? Sleeping in that might be a little uncomfortable."
    y "Oh. Sure, thanks. But…"
    n "I can easily distinguish the concern in his voice, but my thoughts were elsewhere at the moment. I can't believe it took me this long to realise, but… Where was [ch_ren] going to sleep?"

    if rem_boyfriend == True:
        n "Would he mind sharing the bed with me? I mean, we've both been really adamant about [ch_ren] being my boyfriend, and he's shown no complaints up until this point… Would he mind?"
        n "Deciding I won't get my answer by simply thinking about it, I turn my attention back to [ch_ren] once more."
        y "Did you want to sleep with me tonight?"
        show ren blushing at bpop
        r "S-S-S-Sleep with y—!" with hpunch
        show ren flushed at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
        r "You mean… Like… {i}Y-You know{/i}… Or did you mean—"
        if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
            call DLC_day5_s1 from _call_DLC_day5_s1
        else:
            pass
        y "I was talking about sharing a bed with me, you dork."
        show ren flushed at spop
        r "…Oh. Ohhhh! Right. Yeah. {i}Yesss.{/i} Th-That's fine! I don't mind."
        show ren sad at spop
        r "But what about you? Are you really okay with that?"
        
        $ choice_style = "box"
        menu:
            "Share a bed with [ch_ren]":
                $ update_ren = f"WE'RE OFFICIALLY DATING!!!! I HAVE THE BEST {partner} EVER!!!!!!".upper()
                $ affection_ren += 10
                $ d5_sharebed = True
                y "Yeah. Why wouldn't I be? You're my boyfriend, aren't you?"
                show ren lovesick at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
                r "YES!" with vpunch
                show ren blushing at spop
                r "A-Ahem… Y-Y-Yes."
                show ren flushed at spop
                r "I should… I'll go bring this to your friend and come right back."
                y "Okay."
                show ren neutral at spop
                r "But just to make sure… You {i}really{/i} want me to share a bed with you?"
                y "Yes, [ch_ren]."
                show ren happy at spop
                r "And I'm really, really, {i}reeeeally{/i} your boyfriend?"
                y "{i}Yes{/i}, [ch_ren]."
                show ren flushed at spop
                r "Really? You promise?"
                y "Hurry up before I change my mind."
                play audio "audio/sfx/sprinting.ogg"
                hide ren with easeoutleft
                n "At that, [ch_ren] practically teleports out of my room and sprints down the hallway."
            "Let [ch_ren] sleep outside":
                $ affection_ren -= 10
                $ d5_sharebed = False
                y "On second thought… Maybe it'd be better for you to sleep on the recliner. I wouldn't want to accidentally kick you in my sleep."
                show ren happy at spop
                r "O-Oh! Haha, that's fine. And I wouldn't really mind if you did…"
                show ren flushed at spop
                r "{i}Kick me{/i}, I mean. I probably wouldn't even notice."
                y "Thanks for being so understanding. And sorry for being so wishy-washy."
                show ren sad at spop
                r "No, I get it. Today's been a lot for you, huh? Especially because of that weirdo from earlier."
                y "Yeah…"
                show ren neutral at spop
                r "I 'spose you want to go to bed early, then? In that case, I'll let you get changed and bring these pillows to your friend before settling in myself."
                show ren smirk at spop
                r "Goodnight, [ch_angel]."
                y "Goodnight, [ch_ren]."
        $ choice_style = "default"
    else:
        y "What about you, [ch_ren]?"
        show ren neutral at spop
        r "…Me?"
        y "Yeah. Where do you want to sleep? Unless… Were you planning on going home instead?"
        n "Admittedly, I somehow feel safer whenever [ch_ren]'s around. His presence never fails to bring me peace of mind, and a small part of me finds itself hoping that he'd choose to stay."
        n "But if he did… There weren't many places for him to seep. Y'know, aside from my bed and the floor—"
        n "As if reading my thoughts, [ch_ren] perks up and beats me to a response."
        show ren happy at bpop
        r "I-I don't mind taking over the recliner! If that's okay with you, of course. Otherwise, I'm perfectly happy to sleep on the floor."
        show ren lovesick at spop
        r "Or the carpet outside your room, even—"
        y "But… Wouldn't the recliner be uncomfortable?"
        show ren happy at spop
        r "It's fine! Besides, I've slept in worse places. Sometimes I don't even sleep at all."
        y "What?"
        show ren neutral at spop
        r "N-Nothing! Don't worry about it! A-Anyway, I should let you get dressed now."
        show ren smirk at spop
        r "G-Goodnight, [ch_angel]!"
        y "Right… G'night, [ch_ren]."

################################################################################
## Eepy (Day 5 ending — Angel's apartment)
################################################################################
label day5_angeleepy:
    scene angel_bed_night
    show peffect
    with Fade(1.0, 2.0, 1.0)
    play audio "audio/sfx/item.ogg"
    if d5_sharebed == True and rem_touch == False:
        n "Settling into bed, I let out a deep sigh and sink deeper into my pillow. [ch_ren] joined me earlier, after he'd given [ch_moth] some of my spare pillows and blankets — and soon enough, he was pulling aside my duvet and getting comfortable."
        n "He made sure to leave ample space between us, though it was hard to ignore his presence when he was {b}literally{/b} right there beside me."
        n "[ch_ren] was close enough that I could feel the steady rise and fall of his chest from behind me — signalling that he'd already fallen asleep — and yet, I found it… oddly soothing, somehow."
        n "It was so soothing, in fact, that it almost had me dozing off as well."
        n "Yet… For some reason, my mind didn't seem to get the memo."
    elif d5_sharebed == True and rem_touch == True:
        n "Settling into bed, I let out a deep sigh and sink deeper into my pillow. [ch_ren] joined me earlier after he'd stripped himself of his outer cardigan and belt — though I figured the jeans must've been comfortable enough for him to sleep in."
        n "But it wasn't like I had any spare clothes that would fit his large and lanky frame, and there was {b}no way{/b} I was going to ask him to take his pants off."
        n "[ch_ren], however, didn't seem to mind sleeping in denim, as he paid them no mind the moment he joined me under the covers and pulled me closer towards his body."
        n "I was so close that I could feel his chest slowly rise and fall against my backside — signalling that he'd already fallen asleep — and I found it… oddly soothing, somehow. It was so soothing, in fact, that it almost had me dozing off as well."
        n "Yet… For some reason, my mind didn't seem to get the memo."
    else:
        n "Settling into bed, I let out a deep sigh and sink deeper into my pillow."

    n "Today had been an eventful day, to say the least, but despite everything, I was glad that [ch_moth] seemed to enjoy themself. All I wanted was for them to have a fun and memorable experience here in Corland Bay, much like I did all those years ago."
    n "Nothing could replace those fond memories of me exploring the wonders of the town on my own as a child, even going as far as Lake Bluemoss before an adult would find me and tell me it was time to go home."
    n "Thinking back on that memory… Wasn't there someone else with me?"
    n "I remember… leaving the playground to venture deeper into the woods — far enough that I could see the actual lake itself — and there would always be someone waiting there for me."
    n "Was it… [ch_leon]? It was him, right? I honestly couldn't remember anyone else from my childhood."

    if d4_inviteren == True:
        n "But… what about the child with the pigtails and colourful bandages all over their body? Was that [ch_leon]? Somehow, that didn't feel right."
    else:
        pass

    n "Well, all this thinking wasn't doing me any good. I had to be up early if I wanted to catch up with [ch_moth] before they left. Sighing once more, I turn on my side and try to count sheep."
    n "Eventually, it works, as I soon find myself falling into a deep, comforting slumber."
    
    jump day5_ending_good

################################################################################
## Uh Oh :D
################################################################################ 
label day5_branchingdeadend:
    scene other_dark
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    show peffectp
    with Fade(1.0, 2.0, 1.0)

    $ cam_feed = True
    $ cam_chance = renpy.random.randint(7,10)
    $ cam_display = renpy.random.choice(cam_list)

    n "Admittedly, even after we'd made it back to my apartment, I still couldn't shake off the sense of fear still lingering inside me."
    n "I felt terrible for dismissing [ch_moth]'s concern for the nth time tonight, and even more so when I shut down their request to watch the latest Attack on Giant episode together."
    n "I honestly couldn't get myself in the mood to do so, and whether or not [ch_moth] picked up on it, they chose not to say anything."
    n "Instead, they offered to head straight to bed so that they could wake up early and spend the morning with me before they had to leave."
    n "It made me smile to know that [ch_moth] still wanted to spend more time with me, so with a promise to do so, I helped prepare my couch for them to sleep on and make my way towards my bedroom."

    scene angel_bedroom_night
    show peffectp
    with GlitchDissolve

    n "Perhaps out of habit — or was it fear? — I triple-check to make sure that my window is locked tight and that my bedroom door is shut completely."
    n "I'd already quadruple-checked that the front door was locked before I turned in for the night, so with a satisfied hum, I crawl into bed and try to get comfortable."
    n "Though sleep proves to be difficult given recent events, so I resort to counting the faint ticking of the clock to help me drift away to dreamland."
    n "Twelve… Thirteen… Fourteen…"
    
    scene other_dark
    with dissolve

    n "Soon enough, everything starts to fade, and I feel the cold embrace of sleep wash over me."
    
    stop music fadeout 5
    play audio ["<silence 2.5>", "audio/sfx/jumpscare.ogg"]
    play audio ["<silence 2>", "audio/sfx/shatter.ogg"]
    scene angel_bedroom_night with Fade(1.0, 2.0, 1.0)
    show true_red with vpunch:
        alpha 0.3
    hide true_red with owie
    play ambience "audio/ambience/heartbeat.ogg" fadein 1 fadeout 1

    n "All of a sudden, a blood-curdling scream rattles the walls and pulls me from my slumber."

    if persistent.streamermode == True:
        n "What the—? Was that… [ch_moth]?"
        n "[shit!c]. What {b}was{/b} that?"
        n "Don't tell me it's the creep from earlier?!"
    else:
        n "What the fuck? Was that… [ch_moth]? …The creep from earlier?!"
        n "[shit!c]. What the fuck. What the actual fuck."
    
    play music "audio/bgm/Lonely Doll.ogg" fadein 1 fadeout 1
    stop ambience fadeout 2.0

    n "Panic takes hold of my body, and I find myself frozen in place. The logical part of my brain tells me to reach for my phone — to check the cameras and look for any signs of danger — but I can't seem to move."
    n "My body runs cold as I sit in my bed, and no matter how many times I reassure myself that the footsteps outside are just [ch_moth], I can't seem to convince my brain otherwise."
    y "[shit!c]. [shit!c], [shit], [shit]!"
    n "The faint glow of the hallway light seeps in from underneath my door, but it soon fades away the moment a shadowy figure appears. I somehow find the strength to turn away, yet when I brace myself for the worst to happen…"
    n "Nothing comes."
    n "Instead, there's just an eerie silence and a sense of dread hanging in the air."
    n "I know I should probably scream, yell, throw something — {b}anything{/b} that would make enough noise to alert my neighbours — yet I can't seem to get any of my limbs to move, no matter how hard I try."
    n "My body betrays me as it stays rooted in place, and all I can do is lay as still as a statue and hope that this is all some kind of [fucked] up nightmare."
    n "What I would give to just wake up and see my friends again… To see [li_name] again — and even [ch_ren]. If he were here right now…"
    n "[shit!c]! If only I'd asked him to stay…"
    n "Why did I turn him away? All because of some stupid text message?"
    n "Even more palpable silence passes, and just when I begin to think this was all in my head—"
    
    if status_teo == False or status_olivia == False:
        scene angel_bedroom_night at fadetint
        play audio "audio/sfx/glitch.ogg"
        play audio "audio/sfx/cold breath.ogg"
        show gwitch
        show other_dark:
            alpha 0.5
        show de_1 at fadetint:
            parallel:
                alpha 0.2
                function WaveShader(1.0,30,0.01)
        if status_olivia == False:
            show ghost_olivia:
                alpha 0.5
                zoom 2.5
                yalign 0.5
                xpos -150
                function WaveShader(5.0,15.0,0.03)
        if status_teo == False:
            show ghost_teo at fadetint:
                alpha 0.3
                xalign 0.8
                function WaveShader(2.0,3.0,0.05)
        with GlitchDissolve
        n "From the corner of my eye, I {b}swear{/b} I can see some kind of ghastly apparition begin to form by the foot of my bed."
        n "Tendrils of smoke seem to rise from the floor and wrap around my form, before it envelops me in a dark haze and renders me unable to move or make a sound. All I can hear is the loud thumps of my heartbeat, before—"
        n "In the blink of an eye, the other-worldly mass manifests closer to me, and it's then that I notice the eerie sounds spilling out from the darkness."
        n "It's a macabre amalgamation of bones cracking, flesh bending in ways it shouldn't, unnerving crying, and the muffled pleas and shouts for help."
        gh "EA╳MS M╳S PT╳╳T RU╳NK W╳PNT╳╳╳E"
        n "Upon hearing that, a bloodied, severed hand emerges from within the dark abyss and hovers above my face — and I let out a pitiful sob the moment a drop of blood lands on my cheek."
        n "The hand reaches for the blanket below my chin in an attempt to peel it back, and I muster all my strength to keep it cocooned around me. It was my last line of defence, and I wasn't about to have my final source of safety ripped away from me."
        scene other_dark
        with dissolve
        n "Not wanting to look and see how the spectral form would respond, I squeeze my eyes shut and {b}try{/b} to bury my face in the pillow."
        n "But the eerie sound of water running and reeds rattling in the wind draw my attention, and I crack open an eye to see…"
    else:
        play audio "audio/sfx/bone.ogg"
        play audio "audio/sfx/shatter.ogg"
        n "{size=+6}*BANG BANG BANG*{/size}" with vpunch
        y "[shit!c]!" with vpunch
        n "I can feel the tears start to swell up in my eyes as I grip the edges of my blanket."
        n "The doorknob jiggles, taunting me with the thought of the door being unlocked — but the final nail in the coffin is the eerie squeak coming from the hinges and filling the silence."
        n "Heavy footsteps make their way towards the bed, and the moment I feel the weight of something sink down onto the mattress, I let out a silent sob."
        n "I can feel the intruder place their hand on my blanket before they peel it back, and I muster all my strength to keep it cocooned around me. It was my last line of defence, and I wasn't about to have my final source of safety ripped away from me."
        scene other_dark
        with dissolve
        n "Not wanting to look and see how my killer would respond, I squeeze my eyes shut and bury my face in the pillow."
        n "But the sound of my window opening draws my attention, and I crack open an eye to see…"
    
    scene angel_bedroom_night
    with dissolve
    n "Nothing."
    n "Before I can make sense of what I just witnessed, the world around me starts to go blurry."
    n "But even as I lose consciousness, I don't miss the faint shape of something large disappearing from the corner of my eye, along with the lingering smell of old paper, something muddy, and the foul stench of blood."

    $ cam_feed = False

    jump day5_deadend

################################################################################
## REN AND THEIR BIG ASS PENTHOUSE WITH MARBLE FLOORING TYPE BEAT
################################################################################ 
label day5_renapartmentbranch:
    scene sh_complex_night
    play music "audio/bgm/Summer Memories.ogg" fadein 1 fadeout 1
    show peffectp
    with Fade(1.0, 2.0, 1.0)

    $ ren_blood = False
    $ persistent.d5_visitren = True
    $ persistent.fact_residence = True
    $ location_moth = "sh"
    $ location_violet = "home"
    $ location_elanor = "home"
    $ location_ren = "home"
    $ location_conan = "home"
    $ location_jae = "home"
    $ location_leon = "home"
    $ location_teo = "random"
    $ location_olivia = "random"
    $ location_kiara = "oh"

    if d5_witnesskill == True:
        n "In the end, [ch_ren] ended up accompanying [ch_moth] and me to his apartment. He talked about creating some kind of alibi as a precaution, but I trusted him enough to take care of any loose ends."
        n "No matter which way I look at it, this was just a robbery attempt that went sideways, plain and simple."
        n "The thought alone brings me some semblance of comfort, if not for the fact that it {b}also{/b} meant I'd be down a stalker as well."
        n "…If that was even my stalker in the first place."
        n "There was something about that assailant that felt… {b}different{/b}, somehow. Like it wasn't the same person who broke into my apartment all those days ago."
        n "Ugh."
        n "Before I can start making yet another mountain out of a molehill, [ch_moth]'s carefree antics pull me from my thoughts."
    elif d2_visitren == True or d4_visitren == True:
        n "Soon, we all arrive at [ch_ren]'s apartment."
        n "The elevator ride to his floor is just as slow and tacky as last time, yet [ch_moth] doesn't seem to mind it in the slightest. In fact, they seem to be wholly engrossed with their surroundings — much like I had been the very first time I visited [ch_ren]'s place."
        n "Stepping inside, I notice that my slippers from last time were waiting by the door, and the sight alone sends a wave of appreciation through my body."
        n "Did [ch_ren] leave them out for me?"
        n "As cheesy as it sounds, it almost feels like coming home to my own apartment."
        n "But it's [ch_moth]'s awestruck voice that pulls me back to the present, and I watch in silence as they take in the scene before them. Funny, was this how {b}I{/b} looked when I first arrived here?"
    else:
        n "Soon, we all arrive at [ch_ren]'s apartment complex in record time."
        n "I guess he {b}really{/b} wasn't lying when he said it wasn't far… But judging from the pristine interior and fully-functioning elevators, his building seemed to be in {b}far better{/b} shape compared to my apartment."
        n "The elevator ride could've been a little less awkward though, if it weren't for the slow ascend and tacky music…"
        n "Or for the fact that I could feel [ch_ren] staring holes through the back of my head."
        n "But it's [ch_moth]'s awestruck voice that pulls me back to the present, and I watch in silence as they take in the scene before them once the automatic doors open."

    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/running.ogg"
    show ren neutral at tleft
    show moth flushed at tright
    with dissolve
    show moth flushed at bpop
    m "Oh. My. God."
    show moth blushing at bpop
    m "WHAT KIND OF ENTRYWAY IS THIS?! And… Is that… marble flooring?! Dude, you can afford {i}this{/i} much marble?" with hpunch
    show ren sad at spop
    r "I didn't buy it… I-It came with the apartment."
    show ren neutral at spop
    r "And so did the rest of the furniture. Or… Most of it."
    show moth smirk at spop
    m "That's a whooooole lotta marble!"

    if d2_visitren == True or d4_visitren == True:
        if d5_witnesskill == True:
            y "…Y-Yeah, I literally said the same thing!"
            n "Wow, real believable, [ch_angel]. At least {b}try{/b} to sound less… spacey."
            n "Ugh. Even [ch_ren] is doing a better job than me. I just need to suck it up and at least {b}try{/b} to look happy. For [ch_moth]'s sake."
        else:
            y "I literally said the same thing!"
        show moth flushed at spop
        m "Right?! Look at all of this!"
        show ren sad at spop
        r "…It's just marble?"
    else:
        pass
    show moth blushing at spop
    m "Jeez, I guess I skipped the episode where Haruko became a millionaire."
    show ren frown at spop
    r "Like I said… I'm {i}not{/i} Haruko, I'm Re—"

    if d2_visitren == True or d4_visitren == True:
        show moth flushed at bpop
        m "Are those Ducci slippers?! Since when could you afford those?"
        y "Hm? …These? They belong to [ch_ren]. He let me borrow them the first time I came here."
        y "Oh, are there any spare slippers for [ch_moth], too?"
        show ren frown at spop
        r "…"
        show ren smirk at spop
        r "I'll have a look."
        show moth angry at bpop
        m "YOU HAVE MORE THAN ONE PAIR?!" with hpunch
        show moth sad at spop
        m "[shit!c], sorry. I probably shouldn't be so loud, huh."
        if d4_visitren == True:
            y "You're fine. [ch_ren] doesn't have any neighbours—Or, at least, he {i}didn't{/i} until recently… I think? What was with all that smoke yesterday?"
        else:
            y "You're fine. [ch_ren] doesn't have any neighbours—Or, at least, he {i}didn't{/i} until recently… I think?"

        show moth smirk at spop
        m "Heh, sure sounds like you're really used to living here, huh? So, when are you moving in?"
        y "O-Oh, uhh—No. No, I—"
    else:
        show moth flushed at bpop
        m "Are those Ducci slippers?!" with hpunch
        show moth smirk at spop
        m "I hate to admit it, [ch_angel], but your beloved Haruko is literally living the dream life right now. So, when are you moving in?"
        n "[ch_ren] seems to perk up at that."
        y "M-Move in? No, I—"

    if rem_boyfriend == True:
        n "Now that I think about it… the idea {b}is{/b} rather tempting. [ch_ren] already seems fine with the idea of being my boyfriend; surely he'd enjoy being my roommate, too."
        n "But before I can get carried away with these fantasies, I remind myself {b}why{/b} I'm purposefully trying to distance myself from [ch_ren] in the first place."
        n "I didn't want him to get involved with my personal problems, nor did I want to give my stalker any more ammunition to use against me."
        n "In fact—"
    else:
        pass

    show moth happy at bpop
    m "—I mean, look at all this space! If you won't live here, I will!"
    show moth neutral at spop
    m "How many rooms are there? How many kitchens does this place have? Is there a cinema room? Ooh, what about—"
    show ren neutral at spop
    r "Here. Try 'n see if these fit you."
    play audio "audio/sfx/item.ogg"
    n "[ch_ren]'s voice cuts [ch_moth] off as he throws a pair of shoes onto the ground."
    show moth smirk at spop
    m "Oh, they're a little tight around the toes… Buuuut comfy!"
    show ren sad at spop
    r "That's too bad. I don't have any other sizes."
    y "You know, they look like they might fit {i}me{/i} better, actually… Here, wanna swap?"
    n "[ch_moth]'s slippers {b}definitely{/b} appear smaller than the pair I'm currently wearing, but they didn't look too uncomfortable."
    n "That much is evident when we swap, and [ch_moth] seems to be feeling all the more better in a larger pair of slippers — if their wide, appreciative smile was anything to go by."
    show moth neutral at spop
    m "You don't mind?"
    y "Not at all."
    show ren happy at spop
    r "Actually… M-Maybe I {i}do{/i} have another pair that'll fit you better, [player_fl]! Here, I'll go and check again—"
    y "It's cool, [ch_ren]. Don't worry about it."
    show ren sad at spop
    r "…"

################################################################################
## Snuggling on couch or whateva
################################################################################
label day5_rencouch:
    scene ren_lounge_day
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show peffect
    with GlitchDissolve

    if d2_visitren == True or d4_visitren == True:
        n "As we make our way into the living room, [ch_moth] suggests ordering takeout so that we can eat while catching up on the recent episodes of Attack On Giant."
    else:
        n "As we make our way into the living room, I couldn't help but take in my surroundings in awe."
        n "Did [ch_ren] seriously live in a place like this? It was honestly hard to imagine, given how humble he came across. And… Was this even an apartment? Surely a penthouse would've made more sense."
        n "The living room is just as ostentatious as the entryway, though I couldn't help but feel like it lacked any form of life. It just didn't seem like someone actually lived here."
        n "The furniture was gaudy yet tasteless, there was hardly any personal decoration or colours, and there was nothing that really screamed '[ch_ren]' to me."
        n "There were no personal touches, photos, items, hobbies, {b}nothing{/b}. Just tacky furniture and the bland smell of something sterile."
        n "If I was being honest, it gave off the same vibe as a dentist's clinic or a hospital."
        n "But I suppose it made sense, considering how [ch_ren] is still in the process of moving in. I mean, he {b}did{/b} say something similar earlier, didn't he?"
        n "Not that I had much time to ponder, however, as [ch_moth] suddenly throws an arm over my shoulder and pulls me away from my thoughts."
        n "The next thing I know, they're suggesting we order some takeout so that we can chow down on something while catching up on the recent episodes of Attack On Giant."

    n "It's almost comedic watching [ch_ren] and [ch_moth] huddle over a phone to look through the menu, and I nearly end up letting a laugh slip through when they start bickering over the meal deals {b}not{/b} actually being that good of a deal."

    scene ren_loungeroom_day
    play audio "audio/sfx/walking.ogg"
    show peffect
    with dissolve
    n "Leaving the two of them to their own devices, I plop onto the couch with a sigh and absentmindedly clutch one of the throw pillows."

    if d2_visitren == True or d4_visitren == True:
        n "Odd… I swear I have the exact same cushions on my couch back at home. Did [ch_ren] and I always have the same taste in decor?"
        n "And… Since when did [ch_ren] start decorating his apartment? Last I checked, everything in here came pre-furnished — tacky decor and all."
    else:
        n "Odd… I swear I have the exact same cushions on my couch back at home. Did [ch_ren] and I have the same taste in decor?"

    n "Before I can get too deep in my thoughts, [ch_moth] and [ch_ren] join me on the couch once more to fill me in on what they ordered — and what they got for me as well."
    n "[ch_moth] seems all too happy to talk about the fried rice dish they ordered — before rambling on about how most fast-food joints never usually have it in stock — all while [ch_ren] gets his television set up for us."
    n "The next thing I know, we're almost two episodes deep until our food arrives."
    n "It takes another three more before we're all finished with our meals, and soon enough, [ch_moth] is relaxing on the floor with a bunch of pillows surrounding them while [ch_ren] and I remain on the couch."
    show moth happy at tleft
    show ren neutral at tright
    with dissolve
    show moth happy at bpop
    m "Here we goooo! It's finally beach episode time!"
    show moth neutral at spop
    m "You guys {i}have{/i} to see the outfit the animators put him in. It wasn't in the manga, but I still think it's cool."
    show moth flushed at spop
    m "Wait… We should turn the lights off for maximum effect!"

    scene ren_loungeroom_night
    show peffectp
    show moth flushed at tleft
    show ren neutral at tright
    play audio "audio/sfx/shoes alt.ogg"
    with dissolve
    n "[ch_moth]'s voice fills the silence as they get up, flick off the light switch, and start to pump themselves up for the opening song — yet my mind can't help but wander towards today's events."
    if d5_witnesskill == True:
        n "I still couldn't shake off the traumatic encounter from earlier, or the fact that I may {b}potentially{/b} still have a stalker who won't leave me alone." 
    else:
        n "I still couldn't shake off the encounter from earlier, or the fact that I {b}now{/b} had solid proof of a stalker who wouldn't leave me alone."
    n "Still… Going to [ch_ren]'s place was {b}definitely{/b} a smart idea. There's an entire team of security personnel down in the reception, and you need a specific keycard to make it past the first floor."
    n "Now knowing this, I wouldn't have to worry about [ch_moth]'s safety as much. And for some reason… Well, I don't know why, but I always seem to feel a lot better whenever [ch_ren] is around."
    n "Speaking of…"
    play audio "audio/sfx/fabric.ogg"
    hide moth
    show ren neutral at center
    with easeoutleft
    show ren neutral z at center with dissolve
    n "I cast a sneaky glance in [ch_ren]'s direction, only to find him sprawled out on the couch. He'd offered to share his blanket earlier (after I offered mine to [ch_moth]), and I couldn't help but notice how much of it he'd given to me."
    n "In fact, only half of his leg was covered — and with winter right around the corner — I was worried he was too shy to admit that he was feeling cold."
    n "Without thinking, I lean over and gently drape a portion of the blanket across [ch_ren]'s lap in an attempt to offer him some warmth."
    n "But as I do, my hand inadvertently brushes against the back of his, and it's then that I notice just how cold his skin feels."
    n "A surge of concern washes over me, and I have half a mind to reach out to grasp his hands in my own — but [ch_ren]'s immediate reaction keeps me rooted in place."
    n "Almost unashamedly, his gaze shifts towards me before he sends me a curious look. And when he finally speaks, his voice is barely above a whisper, almost getting drowned out by the noise coming from the television."
    show ren smirk z at spop
    r "It's okay, Angel. Y'can have it."
    y "I'm not the one with frozen hands."

    if rem_boyfriend == True:
        y "What kind of [person] would I be if I let my boyfriend's hands go cold?"
        n "Not giving [ch_ren] any time to respond, I reach out and gently cup his freezing hands in my own."
    else:
        n "As if to prove a point, I reach out and gently poke one of his cold knuckles."
    show ren flushed z at bpop
    r "…!"
    show ren sad z at spop
    r "B-But… Your hands are cold, too!"
    m "[ch_ren], shh!" with hpunch
    n "We both glance in [ch_moth]'s direction for any signs of disruptions, but they seem far too engrossed with whatever is happening on the television to fully turn around."
    show ren frown z at spop
    r "You're cold… I should've noticed earlier. Here, I'll go turn up the heater."
    y "No, it's okay. Here, why don't we…"

    menu:
        "Snuggle up together":
            $ affection_ren += 1
            $ affection_olivia += 1
            $ d5_cuddleren = True
            y "[ch_elanor] once told me it's more efficient to stay warm by sharing body heat. Why don't we sit a bit closer?"
            show ren blushing z at bpop
            r "C-C-Closer—?!"
            show ren flushed z at bpop
            r "Yeah! S-Sure! Okay!" with hpunch
            m "{size=-6}Seriously, [ch_ren]! Quiet{/size}!"
            n "Without missing a beat, I throw the blanket over our shoulders and scoot closer to [ch_ren] until my arms and thighs are brushed up against his."
            n "But [ch_ren] takes it a step further by pulling my legs over his lap and resting one of his hands over my knee to prevent them from falling. And just as I dare to take a glance in his direction, [ch_moth] chooses {b}now{/b} of all times to turn around to talk to us."
            m "{size=-6}Fiiiinally! We get to see Haruko!{/size}"
            n "I doubt they realised what [ch_ren] and I were currently doing in the dark."
            n "In fact, [ch_moth] seems all too engrossed with the TV as Haruko's grand entrance flashes on the screen — yet I couldn't help but let my mind wander towards [ch_ren]."
            n "Being this close to him, I can practically feel the warmth radiate from his body — yet all I can focus on is the way his thumb rubs small circles on my knee while his other hand plays with the loose material of my bottoms."
            n "Almost daringly, I sneak a glance in his direction, only to find him staring at me with a gentle expression in return."
            show ren neutral z at spop
            r "I thought you wanted to watch the beach episode?"
            y "I-I am."
            show ren smirk z at spop
            r "The TV is that way."
            n "With a teasing smile, [ch_ren] points towards the television — though the look in his eyes practically challenges me to look away."
            m "{size=-6}Okaaaay, here we go! We're going to the beach now!{/size}"
        "Ask to change the temperature":
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_jae += 1
            $ ren_purity += 1
            y "Actually—[ch_ren], do you mind changing the temperature?"
            show ren neutral z at spop
            r "Oh… Y-Yeah! Of course! I'll do it now. Be right back."
            play audio "audio/sfx/sprinting.ogg"
            hide ren with easeoutright
            show moth smirk at cleft with easeinleft
            n "At that, [ch_ren] gets up from the couch and meanders down the hallway — almost stiffly, like his limbs didn't know how to bend — leaving [ch_moth] to face me with a knowing look in their eyes."
            show moth happy at spop
            m "Any particular reason why his ears are beet red?"
            y "I have the faintest idea what you're talking about."
            show moth smirk at spop
            m "Don't think I didn't notice the way he fixed his pants once he stood up."
            y "Jeez [ch_moth]!"
            n "Without missing a beat, I throw a pillow in their general direction with a laugh, and they easily dodge it by leaning to the side."
            play audio "audio/sfx/walking.ogg"
            play audio ["<silence 1.3>", "audio/sfx/item.ogg"]
            hide moth with easeoutleft
            show ren neutral z at center with easeinright
            n "However, our antics quickly die down once [ch_ren] returns, resulting in [ch_moth] giving me one last smirk before turning their attention back to the TV."
            m "{size=-6}Okaaaay, here we go! We're going to the beach now!{/size}"
        "Take back the blanket":
            $ affection_moth += 1
            $ affection_teo += 1
            $ affection_kiara += 1
            play audio "audio/sfx/fabric.ogg"
            n "Okay… so maybe an explanation would've been nice, but I pull back the blanket without another word and bundle myself up in it once more."
            n "[ch_ren] only seems to find amusement in my actions — given the way his lips split into a grin as he lets out a puff of laughter — before he offers me the pillow he'd been hugging as well."
            show ren smirk z at spop
            r "Comfy? I can tamper with the thermostat too, if y'want. Or get you some more blankets."
            y "Th-This is fine."
            show ren neutral z at spop
            r "Y'sure? 'Cuz it kinda looks like you wanna build a blanket fort right now."
            y "Any more snarky responses from you, and I swear I'm taking these blankets home with me."
            show ren smirk z at spop
            r "Didn't know you moonlight as a burglar, lov—"
            m "{size=-6}Here we go! We're going to the beach now!{/size}"
            n "Impeccable timing, [ch_moth]…"
        "Tell [ch_ren] that you're fine":
            $ affection_violet += 1
            $ affection_leon += 1
            y "Let's just continue watching. I'm fine."
            n "[ch_ren] doesn't seem satisfied with my answer, however, given the way he immediately begins to pout in my peripheral vision."
            n "This {b}almost{/b} feels like a guilty pet owner trying to eat food in front of their dog, and I had half a mind to glance back in [ch_ren]'s direction and say something. But before I can even turn my head, he breaks the silence."
            show ren happy z at spop
            r "Do you… Do you want to wear my cardigan—"
            m "{size=-6}Oh, it's time! Here we go, we're fiiiinally going to the beach now!{/size}"
            n "Impeccable timing, [ch_moth]…"

    n "There, on the television in all its glory, is the iconic Giant's Cove we visited earlier today… And [ch_moth] can barely contain their excitement."
    m "{size=-6}Oh my god! Look! There's that massive rock arch we saw! [damn!c], they really did take a whole lot of inspiration from Corland Bay.{/size}"
    n "They're not shy with the way they languidly flop over on the carpet and pull one of the cushions to their chest to get more comfortable."
    n "But the moment is fleeting, as Haruko soon appears on the screen in a magical, pink flurry. Almost instantly, [ch_moth] rolls onto their stomach instead, kicking their legs and practically melting over the sight of Haruko in a swimsuit."
    m "HIS MUSCLES! LOOK! {size=-6}Ugh, I yearn to lick the crevices of his—{/size}" with vpunch
    show ren flushed z at spop
    r "Ooookay."
    n "Suppressing a laugh, I glance at [ch_ren], who seems to be sporting a worried — yet just as flushed — look on his features."
    show ren smirk z at spop
    r "…And here I thought {i}your{/i} fondness for Haruko was unmatched."
    y "Those are some big words coming from someone who's rocking the same hairstyle as him."
    show ren blushing z at spop
    r "Wha—?!"
    show ren flushed z at spop
    r "What does that mean?"
    m "{size=-6}Heyyyy! What are you two whispering about over there?{/size}"

    $ choice_style = "box"
    menu:
        "{image=14NWY symbol alt} Reach for [ch_ren] underneath the blanket" if dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou == True and persistent.streamermode == False:
            $ choice_style = "default"
            show ren happy z at spop
            r "We're just wondering if Haruko's outfit is going to—"
            show ren blushing z at bpop
            extend "U-U-U-Um…!" with vpunch
            n "The sudden urge to tease [ch_ren] washes over me once more, and before I can stop myself, I trail my hands up his leg — getting increasingly close to the front of his jeans with every inch."
            n "[ch_ren] practically chokes on his spit the moment my hand lands on his upper thigh as one of his own moves to circle my wrist. And just when I think he's about to move my hand away, he instead lets it rest there."
            n "Stealing a quick glance in his direction, I can't help but let out a teasing puff of laughter at {b}just{/b} how red his cheeks have become."
            n "But in my moment of weakness, [ch_ren] unexpectedly turns it into an opportunity to wrap his arms around my waist and pull me directly onto his lap."
            n "…Where did this sudden burst of confidence come from?"
            n "As I shift to get comfortable, I can feel the telltale shape of his hard-on pressing against my thigh, which brings me back to my initial plan of trying to make [ch_ren] flustered."
            n "Well, look how that turned out."
            show ren smirk z at spop
            r "Didn't think I'd let you get away with that, did you? And we can't have your friend seeing me in this state."
            show ren neutral z at spop
            r "Guess you'll just have to finish what you've started, hm?"
            n "I can practically {b}feel{/b} [ch_ren]'s smile against the shell of my ear as he leans down to whisper in a hushed tone."
            n "The low and husky vibration from his voice alone sends a shiver down my spine — as well as sparking a bout of excitement in the pit of my stomach and making me want even more."
            n "Without thinking, I unconsciously find myself reaching for [ch_ren]'s forearm to steady myself as my eyelids flutter shut."
            if nsfw_position == "top" or nsfw_position == "vers":
                call dlc_14nwy_d5_t1 from _call_dlc_14nwy_d5_t1
            else:
                jump day5_wahooscene
        "Move closer to [ch_ren]" if dlc_14nightswithyou_scenes == False or persistent.dlc_14nightswithyou == False or persistent.streamermode == True:
            $ affection_ren += 1
            $ choice_style = "default"
            show ren happy z at spop
            r "We're just wondering if Haruko's outfit is going to—"
            show ren blushing z at bpop
            extend "A-A-A-Angel?!" with hpunch
            n "Deciding to see just how far I can take things, I practically situate myself in [ch_ren]'s lap without another word. And judging by his outburst, I know I don't need to turn around to see how red his cheeks are."
            if rem_boyfriend == True:
                m "{size=-6}Jeez! You just can't seem to keep your hands off your boyfriend, huh?{/size}"
                m "{size=-6}Though if I had a partner who vaguely looked like Haruko, I'd probably be the same…{/size}"
                m "{size=-6}Yeah. I'd do the exact same, actually.{/size}"
            else:
                m "{size=-6}His outfit? It hasn't—Woah! I didn't know you guys were that close.{/size}"
            m "{size=-6}Well, whatever. You two can get all cosy over there, just try not to hit me with your feet.{/size}"
            show ren smirk z
            n "I can feel [ch_ren]'s legs move from under me — almost as if he wanted to go through with [ch_moth]'s threat — before he ultimately reconsiders. Instead, he wraps his arms around my waist and nuzzles his head into the crook of my neck."
            show ren neutral z at spop
            r "This is just… Trying to keep warm, right?"
            y "Is it working?"
            show ren smirk z at spop
            r "Hm… I think y'need to be closer."
            y "I don't think that's physically possible, [ch_ren]."
            n "It was true; I was basically ensnared by his lanky limbs, with barely any room left to move around."
            n "With the way [ch_ren]'s arms were circled around my waist and how his thighs cage my own on either side, I could do very little except sit there and {b}try{/b} to focus on the screen."
        "Answer [ch_moth]'s question":
            $ choice_style = "default"
            $ d5_cuddleren = False
            y "Uh— We're just…"
            show ren smirk z at spop
            r "[player_fl] and I were talking about Haruko's new outfit."
            m "{size=-6}Oh? Without me?!{/size}"
            play audio "audio/sfx/running.ogg"
            play audio ["<silence 0.7>", "audio/sfx/fabric.ogg"]
            show moth happy at cleft with easeinleft
            n "Without another word, [ch_moth] gets up from the floor — pillows and all — and joins [ch_ren] and me on the couch. I barely catch a glimpse of [ch_ren]'s pouty expression before [ch_moth] throws their blanket over my lap and huddles closer to me."
            show moth happy at bpop
            m "Wait, I gotta show y'all this really cool fan art someone made! It's based on episode twenty—"

################################################################################
## RELAXING AT HOME PART 2 ELECTRIC BOOGALOO
################################################################################ 
label day5_renevening:
    if d5_wahooren == True:
        call DLC_day5_s2 from _call_DLC_day5_s2
    else:
        scene other_dark
        play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
        show peffectp
        with Fade(1.0, 2.0, 1.0)
        n "In the end, we all blazed through the latest episode of Attack on Giant — and even a few MeTube theory videos — before the events of the day slowly started to catch up to us."
        n "[ch_moth] was the first to let out a yawn, and eventually, the rest of us fell victim to it as well."

        if d5_cuddleren == True:
            n "I didn't want to leave the warmth of [ch_ren]'s body, but the thought of a comfy bed with plenty of leg room was calling my name."
        else:
            n "I didn't want to leave the warmth of the fluffy blankets, but the thought of a comfy bed with plenty of leg room was calling my name."
        n "And before I know it, [ch_ren] is {b}already{/b} showing us to our rooms with a bright smile on his face — before he leaves [ch_moth] and I alone to decompress."
    n "As I step into my own room, I notice that it's just as gaudy and extravagant as the rest of the apartment; furnished with the most ornate decor and bold colour choices I've ever seen."
    n "But just when I think it couldn't get any worse, I survey the rest of the room and come face to face with the most unfortunate revelation…"
    n "It didn't come with its own bathroom."
    y "[dammit!c]."

    scene ren_hallway_night
    show peffectp
    play audio "audio/sfx/door.ogg"
    play audio "audio/sfx/walking.ogg"
    with GlitchDissolve
    n "With a grumble, I step back into the dark hallway — borrowed toothbrush and clothes in hand — and prepare myself for the inevitability of getting lost in [ch_ren]'s endless maze of an apartment."
    n "All of this… For a single bathroom…"
    n "I have no doubt that this place has {b}at least{/b} four restrooms, but the chances of me finding even one seems laughable. Stumbling around yet another corner, I come across [ch_moth] — hunched in front of a door with a frown on their face."
    y "[ch_moth]?"
    show moth angry at center with dissolve
    play audio "audio/sfx/shoes alt.ogg"
    show moth angry at bpop
    m "WOAH!"
    y "Heh, sorry. Were you looking for the restroom, too?"
    show moth neutral at spop
    m "Nah, my room has a private ensuite. I'm actually looking for something else."
    n "…A private {b}what{/b}? Where was mine?"
    show moth smirk at spop
    m "Heh. I'm looking for [ch_ren]'s cosplay room."
    y "His…?"
    y "Wait, hold on a sec. Are you… Snooping? Pfft— [ch_moth]!"
    show moth flushed at bpop
    m "Shhh! And I'm {i}not{/i} snooping. I'm just… Trying to find where he keeps all of his Attack On Giants merch."
    show moth smirk at spop
    m "I'm sure a small peek won't hurt."
    n "I watch as [ch_moth] reaches for the door once more, only to be met with an audible click and a stiff handle."
    show moth sad at spop
    m "Oh? [damn!c]. Locked."
    y "Well, what did you expect?"
    show moth frown at spop
    m "Hmph. Maybe he has a spare key somewhere?"
    y "You're not seriously still thinking of going through his stuff?!"
    if d2_visitren == True or d4_visitren == True:
        y "And never mind that! This place doesn't use physical keys, anyway. You have to use a keycard to access everything. [ch_ren] explained it to me a while ago."
        show moth happy at spop
        m "Soooo… Does that mean you have one?"
        y "I'm {i}not{/i} going to snoop through his stuff."
        show moth smirk at spop
        m "You won't… But what if I do?"
    else:
        y "Besides, that door doesn't look like it uses regular keys."
        show moth sad at spop
        m "Yeeeeeah, you're right. Oh! What about that keycard [ch_ren] gave you earlier?"
        y "…Keycard?"
        n "Was [ch_moth] talking about the weird plastic card [ch_ren] pressed into my hands before he left? I assumed it was only used to unlock the front door — which, to be fair, {b}was{/b} a rather odd thing to give me."
        n "But if this… {b}keycard{/b} can be used to unlock other rooms in his apartment, then maybe it wasn't so odd after all."
        n "Well, whatever. It's not like I'm planning on using it to help [ch_moth] snoop though [ch_ren]'s belongings without his knowledge. At that, I make my intentions known."
        y "There's no point. I left his keycard back in my room. And besides, if the door's locked, it's probably for a reason. We shouldn't go in there."
        show moth smirk at spop
        m "You might not want to… But what if {i}I{/i} do?"
    
    y "[ch_moth]."
    show moth smirk at spop
    m "{i}[ch_angel].{/i}"
    show moth happy at spop
    m "C'moooooon! What if he's one of the lucky people who got Haruko's limited-edition sword? You're seriously not interested? Even the slightest bit?"
    n "Okay, so maybe I was just a little, tiny, miiinuscule bit curious — but that spark of interest didn't justify breaking into a locked room without the other person's knowledge."
    n "And while it technically wouldn't be breaking in if I used a keycard to unlock the door, [ch_ren] still trusted me enough to give me one. Not [ch_moth] — {b}me{/b}."

    if d4_snooping == True:
        n "Besides, I already did my own snooping yesterday, and look where that got me."
    else:
        pass
    y "Look. Instead of breaking in, why don't you go and ask [ch_ren] first? I'm sure he wouldn't mind giving you the full tour of his collection — {i}if{/i} he even has one."
    show moth frown at spop
    m "You've got a point… Man, why didn't I think about that?"
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/item.ogg"
    show moth flushed at tleft
    show ren smirk at tright
    with easeinright
    show moth flushed at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5):
        xalign 0.3
    show ren smirk at spop
    r "—Think about what?"
    n "All of a sudden, [ch_ren] appears from behind one of the dark hallways and scares the living [shit] out of us."
    show moth neutral at bpop
    m "Woah! Uh… {i}Heeeeey{/i} pookie wookie! We were just…"
    y "[ch_moth] wanted to look at your Haruko collection."
    show moth flushed at spop
    m "Wha—?! Hey!" with hpunch
    show ren sad at spop
    r "M-My…? In {i}that{/i} room? Why would I—Oh!"
    show ren blushing at spop
    r "Ah… Well, this is a bit embarrassing, but… That room isn't… it's not finished yet. It's a mess."

    if d2_snooping == True:
        n "Oh, that's right. I completely forgot about [ch_ren]'s storage room. But wait… Was {b}this{/b} the same room from the last time I came here? I could've sworn it was closer to the foyer."
        n "Man, this place really is too big and confusing than it needs to be."
    else:
        n "A mess? What was he talking about?"
        pass

    show ren flushed at spop
    r "—Once it's more… presentable, I'll be sure to invite you back and give you the full tour!"
    show moth angry at spop
    m "Right… Sorry."
    show moth frown at spop
    m "…"
    show ren neutral at spop
    r "There's nothing to be sorry about."
    n "Ugh, he truly is the real-life embodiment of Haruko. And… Wait. Didn't he have a line similar to that in the manga?"
    show moth happy
    n "[ch_moth] must've been on the same wavelength as me since their mood {b}immediately{/b} shifts from embarrassment to excitement, before they shoot me a look as if to say 'you heard that too, right?!'."
    n "But before I can respond, [ch_ren] cuts me off with a timid laugh."
    show ren happy at spop
    r "A-Anyway! Was there anything else you needed?"
    show moth smirk at spop
    if d5_wahooren == True:
        call DLC_day5_s3 from _call_DLC_day5_s3
    else:
        m "[player_fl] was looking for the bathroom earlier. [they!c] needed to pee {i}soooo{/i} badly."
    y "Hey!" with hpunch
    show moth happy at spop
    m "Oh, but calling me out for wanting to see his Haruko collection was fine, huh? Pff—Hahaha!"
    show ren neutral at spop
    r "The bathroom…? Of course! It's just down the hall, near the kitchen. Here, I can show you."
    show ren happy at bpop
    r "F-Follow me!"
    n "Leaving [ch_moth] to their own devices, I quickly catch up to [ch_ren] and follow him down the hallway."

################################################################################
## we sleepin we snorin (Day 5 ending — [ch_ren]'s apartment)
################################################################################ 
label day5_reneepy:
    scene ren_spareroom_night
    play ambience "audio/ambience/night.ogg" fadein 1 fadeout 1
    show peffectp
    with Fade(1.0, 2.0, 1.0)

    $ cam_feed = True
    $ cam_chance = renpy.random.randint(7,10)
    $ cam_display = renpy.random.choice(cam_list)

    n "Soon enough, the events of the day slowly catches up and leaves me feeling tired and drained. Man, today had been a lot, huh?"
    n "But just as I settle into bed, I hear a faint knock coming from the door. Was it… [ch_ren]? I let out a faint 'Come in!' and wait for my visitor to emerge."
    n "To my surprise, it's [ch_moth] that appears from behind the door with a sheepish smile on their face."
    play audio "audio/sfx/door.ogg"
    show moth blushing at center with dissolve
    show moth blushing at spop
    m "Hey… I didn't wake you, did I? Sorry… I just find it hard to fall asleep when everything is quiet."
    show moth neutral at spop
    m "I'm used to my younger siblings bickering in the room next door, or hearing someone playing video games downstairs. Do you mind if I…"
    show moth frown at spop
    m "Um— Can I chill with you for a while? I promise I'll sleep in my own bed later."
    n "Without missing a beat, I lift the covers and pat the spot next to me. And with a relieved smile, [ch_moth] crawls into the bed and lets out a faint hum once they sink into the mattress."
    play audio "audio/sfx/item.ogg"
    show moth z neutral with dissolve
    n "They seem content lying on their back, so I do the same and look up at the ceiling. The silence that follows is momentary, seeing as [ch_moth] soon speaks once more — only this time, their voice is much softer than before."
    show moth smirk z at spop
    m "…Thanks for today, [player_fl]."
    show moth neutral z at spop
    m "No one's really gone out of their way to make me feel so… included? …Seen? Haha, I'm not really sure what word I'm trying to look for. But…"
    show moth happy z at spop
    m "I really appreciate everything you've done."
    show moth blushing z at spop
    if persistent.streamermode == True:
        if status_teo == True:
            m "You of all people know that I don't have many friends — and I've probably been a jerk to [ch_jae] earlier — but I want you to know that I think he's really cool! I just…"
        else:
            m "I mean, you of all people know that I don't have many friends. I just…"   
    else:
        if status_teo == True:
            m "You of all people know that I don't have many friends — and I've probably been an ass to [ch_jae] earlier — but I want you to know that I think he's really cool! I just…"
        else:
            m "I mean, you of all people know that I don't have many friends. I just…"
    show moth frown z at spop
    m "I have trouble talking to people. But I'm glad I could get along with you and [ch_ren] this easily."
    y "Oh yeah, you didn't seem to have any trouble talking with [ch_ren]."
    show moth smirk z at spop
    m "Heh, probably because his personality reminds me so much of Haruko."
    show moth neutral z at spop
    m "Though… I didn't think the whole 'light academia' fashion would suit him, but weirdly enough, it kinda does?"
    y "Honestly? It's like [ch_ren] walked straight out of my dreams or something. I mean, he's practically a walking amalgamation of all of my recent interests."
    show moth happy z at spop
    m "Must be all the manifesting you've been doing in our DMs."
    y "Oh, please—manifesting? I think {i}you're{/i} the one who's been doing that."
    y "I mean, you always ask for Haruko to be real, and look what happened."
    show moth flushed z at spop
    m "Hahaha! Truuue, but I distinctly recall asking for him to be my husband as well. I guess whoever was listening missed that part."
    y "Manifest harder."
    show moth happy z
    n "[ch_moth] can't seem to contain their laughter at my words, and they end up clamping a hand over their mouth to silence their sounds — lest they wake up [ch_ren]."
    n "The corners of their eyes crinkle as they turn to look at me with a smile, and I find myself mirroring their expression."
    show moth smirk z at spop
    m "…Goodnight, [ch_angel]. Thanks for today."
    y "Night, [ch_moth]."
    hide moth with dissolve
    n "At that, they roll onto their back once more and pull the covers up to their chin. The silence returns once more, and I'm left to stew in my own thoughts."
    n "Today had honestly been a lot of fun. Plus, it was nice to know that [ch_moth] enjoyed themself this much. I have no doubt that I'll be sad once they leave for the city tomorrow, but I didn't want to ruin this moment with my sappy feelings."
    n "With one last smile, I turn on my side and slowly drift off to sleep."

    $ cam_feed = False

    jump day5_ending_good

################################################################################
## EEUUUGHGHGUEGHEUSGH
################################################################################
label day5_ending_good:
    ## ! Fix this for day 6
    $ ending_demo = "obtained"
    $ persistent.d5_ending_gooding = True
    jump pathpoint

label day5_deadend:
    $ persistent.deadendings += 1
    $ persistent.deadend5 = True
    $ persistent.d5_badending = True
    jump pathpoint

