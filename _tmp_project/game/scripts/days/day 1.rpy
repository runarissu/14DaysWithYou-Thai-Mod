################################################################################
## DAY 1 POGGERS
################################################################################
label day1:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Currently playing Day 1',
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
    $ calendar_day = "01"
    $ skipday = "day2"
    
    scene angel_lounge_day
    show peffect
    play music "audio/bgm/Afternoon Moment.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    with GlitchDissolve

    $ update_ren = "OH GOD OG GOD OHHHHH BOY OHH MY GOD OH BOY OHHH MY GO"
    $ update_moth = "in my housespouse era don't @ me"
    $ update_violet = "STOP INTERFERING WITH MY WALKS TEO!!! I SWEAR I'LL MACE YOU AGAIN!!!"
    $ update_elanor = "Good morning Corland Bay! :)"
    $ update_conan = "Treat your books with kindness."
    $ update_jae = "imagine paying to get into a club LOOOOOOLLLLLLLLL"
    $ update_leon = "…My wallet is crying orz /lh"
    $ update_teo = "#BTB spotted at the pier lol"
    $ update_olivia = "THE TITS ON THAT MAN??? HOLY MOLY"
    $ update_kiara = "Use the code \"creston20\" for 20% off your next item at my store!"

    if unlockable == "kitsune":
        n "\"And in other news; the remains of {b}yet another{/b} body has been found inside one of the tunnels in Mount Corland, making it a total of {b}four{/b} unidentifiable victims this past year. Authorities believe that—\""
    else:
        n "\"And in other news; the remains of {b}yet another{/b} body has been pulled out from Lake Bluemoss, making it a total of {b}four{/b} unidentifiable victims this past year. Authorities believe that—\""

    y "Ugh."
    n "Stifling a groan with the rim of my coffee cup, I fish around for the remote lodged between the cushions and turn off the TV."
    n "I wasn't about to let some morbid headline damper the start of my cheerful morning… Especially considering how today was going to be my first day at work after {b}finally{/b} getting that hard-earned promotion."
    n "I mean, sure, stacking and sorting through books at a library might not have been my dream job — or even my {b}first{/b} choice of places to work after moving back…"
    n "But the pay was nice, my co-workers were friendly, and the building was located within the perfect walking distance from my apartment."
    n "There was even this adorable little bakery along the way that served {b}the best{/b} shortcakes and croissants known to mankind, and the manager there always loved to hand out small freebies whenever I stopped by."
    n "It still beats living in the city, though. Honestly… I wasn't even sure why I left my home town in the first place."
    n "The fast-paced, hustle and bustle lifestyle of the city just {b}wasn't{/b} what I was longing for whenever I stared out of my window on sleepless nights, and the people there were always rude and indignant."
    n "It was nothing like Corland Bay, where everyone felt like a close-knit family, and the air smelled like the sea rather than pollution."
    n "And sure, the local crime rate might be getting out of hand as of late, and there might be fewer things for me to do here…"
    n "But my new job keeps me busy, and I prefer spending time alone at the beach over visiting shady bars with people I barely considered friends. In fact—"

    play audio "audio/sfx/vibrate.ogg"
    n "*{i}bzzt bzzt!{/i}*" with vpunch
    $ meet_moth = True
    $ unlock_help = True
    play audio "audio/sfx/item.ogg"
    n "Setting my mug onto the table, I reach into my pocket and pull out my phone. A notification from [ch_moth] — my online friend — pops up, so I tap on the screen to read their message."
    n "What greets me is an adorable sticker of some anime character giving a thumbs up, as well as a short message that says \"Good luck today!\" underneath."
    n "[ch_moth] had always been adamant about showing their {b}endless{/b} support for me — even after five years of friendship, cursed memes, and late night video calls."
    n "And even though I would never admit it out loud, I was truly grateful to have someone like them in my life."
    n "Pulling up the keyboard, I begin to type a response to their message."

    menu:
        "Say \"Thank you!\"":
            $ affection_moth += 1
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_leon += 1
            n "It really was considerate of them to send this message — especially considering our contrasting time zones — so I decided on sending back a quick '{i}Thank you{/i}!' in response."
            n "A grey chat bubble pops up just as I hit the send button, indicating that [ch_moth] was typing out another message."
        "Send back another sticker":
            $ affection_moth += 1
            $ affection_olivia += 1
            $ affection_kiara += 1
            n "When {b}did{/b} I download that pack of anime stickers…? Not that I was about to complain or anything. After all, they were free, charming, and included some of my favourite comfort characters."
            n "Without hesitating, I send back a sticker of some green-haired protagonist holding up a giant heart."
            n "A grey chat bubble pops up just as I hit the send button, indicating that [ch_moth] was typing out another message."
        "[rh_o]Reply later[rh_c]":
            $ affection_ren += 1
            $ affection_teo += 1
            n "Leaving people on read is my specialty, after all. As I reach for my discarded mug, I slip my phone back into my pocket, intending to reply to [ch_moth] later."
            n "That is until I heard it go off once more."
            n "…And then another three times."
            y "{i}*Sigh*{/i}… Alright, fine. Let me see what you said."
        "Send a meme with zero context":
            $ affection_moth += 1
            $ affection_violet += 1
            $ affection_jae += 1
            n "Without missing a beat, I open up the image gallery with practised fingers and send back a blurry picture of a worm in a bag of crisps with the word \"sexy\" written in glitter font."
            n "Not even {b}five{/b} seconds pass before [ch_moth] quips back with a response of their own; this time sending their own cryptic meme of a frog sitting on a slice of bread."
            y "Is that…"
            extend " {i}butter?{/i}"
            n "Before I can ask, a grey chat bubble pops up once more, indicating that [ch_moth] was {i}still{/i} typing another message."

    mt "btwww! did u see the latest AoG ep?? i heard Haruko got an outfit change!!!!"
    mt "spoil it for me. did he really change his hairstyle as well? or was it really just his sorcerer outfit?"
    mt "i can't call myself his spouse if i don't even know whether he changed his look or not :'("
    n "Attack on Giants — or \"AoG\", as [ch_moth] liked to call it — is a popular anime series that we recently became obsessed with, and Haruko is one of the main characters from the show."
    n "He's a sorcerer from the Shizuka clan, and is widely known for his shy, empathetic, and airheaded demeanour. And as of late, his unique hairstyle has become a trending topic within the anime community."
    n "Now that I'm thinking about it, what hairstyle {b}did{/b} Haruko have in the latest episode of AoG?"

    menu:
        "\"Haruko's hair is short now.\"":
            $ ren_hair = "short"
            mt "HE CUT IT SHORTTTTTT??? lets hold a funeral <3"
            mt "rest in rip to his luscious pink locks… gone but not forgotten :("
        "\"Haruko's hair is mid-length now.\"":
            $ ren_hair = "normal"
            mt "oh!!! so it's still relatively the same length then??? PHEW >.<"
            mt "i must've been looking at fake news or something…"
        "\"Haruko's hair is long now.\"":
            $ ren_hair = "long"
            $ ren_length = "blue"
            mt "HE GREW IT OUT????? i knew there was a 1 year timeskip BUT DAAANG!!!"
            mt "i'm bouncing off the walls rn!!!"
        "\"His hair is still the same.\"":
            $ ren_hair = "normal"
            mt "oh for real??? haruko never changed his hairstyle? i guess that makes sense lol"
            mt "i was probably looking at some fake news or something hahaha -.-;"

    mt "btw!!! i don't mean to change the subject, but…"
    mt "didn't you say last night that you were gonna head to work at 8am??"
    mt "cuz it's like… almost 9:30 where you are now rn ^^'"
    mt "right???? or am i just dumb and got the time zones mixed up again lol"
    n "Looking at the time displayed on my phone, I immediately let out a string of curses and leap to my feet."
    y "[shit!c]!"
    n "Grabbing the coat that I had carelessly strewn across the back of the sofa earlier, I quickly shrug it on before making a beeline towards the front door."
    n "Before I leave; however, I spare myself one final glance in the (poorly hung) mirror in the hallway."
    n "Hopefully, the outfit I chose was appropriate for my job."

    menu:
        #with dissolve
        "Something cutesy":
            $ affection_violet += 1
            $ affection_olivia += 1
            $ favourite_outfit = "cute"
            y "You can't go wrong with a bit of pastel, bows, and frills."
            n "Giving myself a small spin in the mirror, I admire how the soft fabric and patterns flow around me."
        "Something comfy":
            $ affection_elanor += 1
            $ affection_jae += 1
            $ favourite_outfit = "comfy"
            n "Oh, please. Climbing shelves and carrying stacks of books while wearing something stiff and uncomfortable? Yeah, no thanks."
            n "I pull the sleeves of my sweater down to smooth out all the folds and give myself an appreciative nod in the mirror."
        "Something alternative":
            $ affection_ren += 1
            $ ren_switch += 1
            $ favourite_outfit = "edgy"
            n "Okay, so {b}maybe{/b} my outfit might not match the vibes of the library… But hey, at least I'll look hot while stacking those books."
            n "Adjusting the black choker around my neck and re-adjusting the fishnet mesh, I give myself an appreciative nod in the mirror."
        "Something professional":
            $ affection_elanor += 1
            $ affection_conan += 1
            $ favourite_outfit = "professional"
            n "Perhaps it's because I'm still in my \"impress my colleagues\" phase, but sometimes it's best just to wear something appropriate for my job."
            n "Tugging at the ironed-out collar of my blazer, I give myself a small spin in the mirror to make sure that everything was in the right place."
        "Something trendy":
            $ affection_violet += 1
            $ affection_kiara += 1
            $ affection_teo += 1
            $ favourite_outfit = "trendy"
            n "Did this outfit cost me an arm and a leg to obtain? …Perhaps. But hey, if my pay check can cover it, then I should be able to wear it."
            n "Giving myself a small spin in the mirror, I admire how the eye-catching accessories move around me."
        "[rh_o]Something casual[rh_c]":
            $ affection_ren += 1
            $ affection_leon += 1
            $ affection_moth += 1
            $ favourite_outfit = "casual"
            n "Not seeing the point in getting overdressed for work, I settled for something more chill and laid back."
            n "Adjusting the strings and sleeves of my hoodie, I give myself an appreciative nod in the mirror."

    n "But enough of that! I can check myself out another time. Hastily, I smooth out the wrinkles and pick off any stray pieces of lint from my sleeves before I {b}finally{/b} head out the front door—"
    n "And almost catch my coat on the door handle in the process."

################################################################################
## MEET VIOLET SCENE
################################################################################ 
label day1_meetviolet:
    scene oh_complex_day
    play audio "audio/sfx/door.ogg"
    stop ambience fadeout 2.0
    show peffect
    with GlitchDissolve

    n "With a grumble, I tug at the fabric of my coat before slamming the door shut with a little bit {b}too much{/b} force than necessary."
    n "Even trying to insert my key came with a bit of a struggle, and I had to fight the urge to yell in frustration as I attempted to lock my door."
    y "Seriously… When will that lazy {i}bum{/i} of a landlord do something about this?"
    y "I swear I've complained about this at least {i}four{/i} times this month…"
    play audio "audio/sfx/heels alt.ogg"
    show  violet neutral at left with easeinleft
    show violet neutral at spop
    $ meet_violet = True
    v "Oh! Hey there [ch_angel]! Looking good!"
    n "My neighbour — [ch_violet] — practically beams at me while she fishes through her pockets for her own apartment key."
    n "Resting on her hip was {i}yet another{/i} potted plant, and I found myself wondering where she was going to put it this time."
    n "I was almost {b}entirely{/b} convinced that her whole apartment had been turned into a greenhouse at this point, considering how her balcony was practically filled to the brim with different kinds of plants, greenery, and other various kinds of flora."
    n "But I wasn't about to complain or anything. The fragrance that wafted in with the wind always smelled floral and earthy, and it did well to mask the smell of smoke and burnt food whenever I tried to cook."
    play audio "audio/sfx/heels.ogg"
    show  violet happy at center with easeinleft

    if favourite_outfit == "cute":
        v "Hey, your outfit is just my style! You look so cute!"
    elif favourite_outfit == "trendy":
        v "Hey, isn't your top from that high-end brand? I didn't know we had similar taste in fashion!"
    else:
        v "Love the shoes, by the way! The colour reeeeally compliments your aura this morning."

    show violet neutral at spop, center
    v "You'll have to let me peek inside your closet some day. I've been looking for some new inspiration lately."
    show violet blushing at spop, center
    v "Especially with winter right around the corner… Ahh, I'm getting excited just thinking about it! Oh—"
    show violet happy at spop, center
    extend " But back to you!"
    show screen reltutorial
    n "Her voice pulls me away from my thoughts, and I notice how the growing smile on her face doesn't seem to falter."
    n "Wow, [ch_violet] sure was extra chirpy this morning… I wonder if she'd let me borrow some of that energy?"
    n "In response, I shoot my neighbour a grin of my own, and it was apparently enough to brighten her mood {b}even more{/b} than it was already."

    #hide violet happy
    hide screen reltutorial with dissolve

    menu:
        #with dissolve
        "\"What exactly are you holding?\"":
            $ affection_violet += 1
            $ affection_jae += 1
            show violet blushing at bpop, center
            v "Oh, this? It {i}maaaaaay or may not{/i} be another plant I impulsively bought from work… Heehee, isn't she beautiful?"
            n "She briefly pulls away from her lock to gently pet the succulent plant. The look on her face is soft now, and I couldn't help but stare."
        "\"Is that {i}another{/i} plant?\"":
            $ affection_violet += 1
            $ affection_moth += 1
            $ affection_kiara += 1
            $ ren_decay += 1
            show violet blushing at bpop, center
            v "Hmm? {i}Oh!{/i} Yeah, this is Charlie! I'm thinking of putting her next to Whitney."
            n "Great, she names her plants."
        "\"It's nice to see you again!\"":
            $ affection_violet += 1
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_leon += 1
            show violet blushing at spop, center
            v "Yeah, it's nice to see you too! I'd usually still be at the flower shop at this time, so it's nice to finally be able to catch up with you like this — {i}especially{/i} when our schedules align!"
            show violet happy at spop, center
            v "Speaking of! You should stop by my place the next time you're free. I'd love to introduce you to this little guy's family."
        "[rh_o]\"Sorry, Vi, I'm in a rush.\"[rh_c]":
            $ affection_violet -= 1
            $ affection_teo += 1
            $ affection_olivia += 1
            $ affection_ren += 1
            show violet happy at spop, center
            v "That's okay, don't let me stop you!"
            n "She gives me a soft smile and waves her free hand before focusing her attention back on her door. That is, until she suddenly jolts as if she just remembered something and swivels on her heels to look at me once more."

    show  violet neutral at spop, center
    v "Oh, I almost forgot! I've been meaning to ask you this, but… When were you going to tell me that you were seeing someone?"
    y "{i}…Huh?{/i}"
    n "A knowing look pulls at her features as [ch_violet] continues to fiddle with the lock on her door."
    y "What are you talking about?"
    show  violet happy at spop, center
    v "{i}C'mooon!{/i} Don't act like you {i}didn't{/i} just have a guy over last night. I saw him leaving when I took Cathy out for a walk."
    n "I'd be more worried about my neighbour taking her plants — {b}named{/b} plants — out on a walk at night, but the thought of someone leaving my apartment seemed to set off {b}way more{/b} alarm bells."
    n "I give [ch_violet] a concerned look, and she picks up on it almost immediately."
    show  violet frown at spop, center
    v "…You don't remember? Don't tell me you were drunk or something!"
    n "With a huff, she gives up on trying to unlock her door (it seemed as though we both shared the same problem with our apartment locks) and places her potted plant on the ground before slowly making her way towards me."
    play audio "audio/sfx/item.ogg"
    show  violet sad z with dissolve
    v "Tall guy?"
    show violet sad z at spop, center
    extend " Wearing a dark slasher hoodie? "
    show violet sad z at spop, center
    if persistent.streamermode == True:
        extend "Really into alternative fashion with the crazy amount of belts and loops wrapped around his leg?"
    else:
        extend "Probably into either alt fashion {i}or{/i} bondage with the crazy amount of belts and loops wrapped around his leg?"
    show violet neutral z at spop, center
    v "Ring any bells?"
    y "Err… no? Last night I was just catching up on some tv shows and talking with my friend."
    y "No one came here, even if they did, I would've heard them. My place isn't really that big anyway."
    show  violet sad z at spop, center
    v "Really? But I was so sure it was your door…"
    n "A hand rests on her cheek in a thinking manner before she pouts up at me, seemingly giving in… for now."
    show  violet frown z at spop, center
    v "Well… alright then. Maybe it was somebody else's apartment? I mean, it's always so dark in these hallways at night. Honestly… What is our landlord doing?"
    show  violet neutral z at spop, center
    v "Would you mind if I check in with security downstairs later? It'd give me some peace of mind."
    y "Yeah, that's fine."
    show  violet smirk z at spop, center
    v "Alright then. Thank you, [ch_angel]."
    show  violet happy z at spop, center
    v "{i}Welp!{/i} I got some plants to water and some MMOs to raid in, so…"
    play audio "audio/sfx/heels alt.ogg"
    show  violet happy with dissolve
    n "[ch_violet] lets out one last huff before she picks up her plant (what did she name this one again?) and goes back to unlocking her door."
    play audio "audio/sfx/heels.ogg"
    show  violet happy at left with easeinleft
    show violet neutral at spop
    v "Good talk, I guess! Even if it {i}was{/i} kinda awkward, hee hee."
    y "Uh, yeah… Sure. See ya later, Vi."
    hide violet neutral with dissolve
    n "Slipping past my neighbour and into the cramped hallway, I quickly make for the stairs — when will they fix that broken elevator? — and break into a slight jog."
    n "Thankfully the weather was rather cool today, and the shoes I chose weren't going to leave me with blisters by the time I reached the library."

################################################################################
## MEET ELANOR
################################################################################
label day1_meetelanor:
    scene library_reception_day
    play music "audio/bgm/Refreshing Scent.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/library.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 1.0, 1.0)

    n "The smell of old paper, coffee, and soft incense floods my senses as I step through the library's glass doors."
    n "The melodic chimes alert the woman at the reception desk of my arrival, and I watch as she tucks a strand of stray blonde hair behind her ear as she turns around to greet me."
    y "Good morning, [ch_elanor]."
    play audio "audio/sfx/heels alt.ogg"
    show  elanor blushing at bpop, center with dissolve
    $ meet_elanor = True
    e "Oh!"
    n "She looks surprised for some reason before her expression morphs into a soft smile, and she beckons me closer with a nod of her head."
    n "[ch_elanor] is one of my co-workers here at Corland Bay Library, and one of the {b}very few{/b} people here who actually gets the work done."
    n "And although she's notorious for being rather scatterbrained, she more than makes up for it with her caring and doting attitude towards everyone."
    n "But her nurturing personality can get rather… overbearing at times, and I often find myself having to step away to get some breathing room."
    n "Nevertheless, she's charming to work with, and I appreciate her always looking out for me. After all, who knows what my sleeping schedule would've looked like without her help."
    show  elanor flushed at spop, center
    e "[ch_angel]! Just on time. I printed out your— Wait… {i}where did I—?{/i}"
    show  elanor sad
    n "Her expression turns into a slight panic as she spins on her heels, and I silently watch with amusement as she shuffles through the various books and stacks of papers lining her desk."
    show  elanor frown at spop, center
    e "Where did I leave it?"
    show  elanor blushing at spop, center
    e "Ah! Here it is!"
    play audio "audio/sfx/item.ogg"
    show  elanor blushing z with dissolve
    play audio "audio/sfx/paper.ogg"
    n "Spinning around once more, [ch_elanor] comes back and hands me a sheet of paper with the word \"SCHEDULE\" printed in big, bold letters. I take it from her grasp and give the sheet a once-over."
    n "Well, it looks like I'm going to be busy for the next few weeks… But I guess [ch_elanor] doesn't seem to share the same disdain as me, judging from the playful look plastered on her face."
    show  elanor happy z at spop, center
    e "{i}Sooooo?{/i} How does it feel to no longer be the one in charge of stacking books all day long?"
    show  elanor frown z at spop, center
    e "Although… You'll still have to work the front desk from time to time though. {i}Unfortunately{/i}."
    n "I offer a weak smile at her words before rounding the corner and placing my bag under the desk. And as I begin to pull out some of my belongings, the front door chimes again, letting everyone know that another patron has come in."
    play audio "audio/sfx/heels.ogg"
    hide elanor frown z with dissolve
    n "Figuring [ch_elanor] has it all covered, I leave the customer to her as I go back to preparing everything for the day."
    n "But as I turn around to check on her, I notice that she had {b}already{/b} finished greeting the customer and was on her way back to her own desk across from mine."
    n "As if sensing my gaze, she spins around in her office chair and flashes me a teasing grin."
    play audio "audio/sfx/heels alt.ogg"
    show  elanor smirk at spop, center
    e "Looks like {i}he's{/i} back again."
    n "[ch_elanor] gives a soft chuckle as she inclines her head in the direction of the person she was talking about."
    show  elanor neutral at spop, center
    e "You know, that new guy. I don't know when he started showing up here in the Bay, but he always comes in and rents out the books you recommend on the display window."
    show elanor happy at spop, center
    e "And if I didn't know any better, I'd say he has a little crush on you."

    if favourite_outfit == "professional":
        show elanor happy at spop, center
        e "Especially with that outfit! I don't know about him, but I think that blazer looks great on you!"
    elif favourite_outfit == "casual":
        show elanor happy at spop, center
        e "Especially with that outfit! Honestly, the laid-back look makes {i}me{/i} jealous. Maybe I shouldn't have worn heels today…"
    else:
        show elanor blushing at spop, center
        e "Especially with that outfit you've got on! It makes you look rather [gorgeous], so I can't really fault him for staring."
        show elanor neutral at spop, center
        e "Because he {i}was{/i} staring."
        show elanor happy at spop, center
        extend " {i}A lot{/i}."

    hide elanor with dissolve
    n "Snorting, I push [ch_elanor]'s office chair so that she's facing the other way and focus my attention {i}back{/i} to the papers in front of me."
    n "What was with everyone today? Always smiling, gossiping about other people, and meddling in business that wasn't their own."
    n "It was bad enough that I had to deal with a potential intruder — but I doubt my deadbeat landlord was going to do anything about it."
    n "I might need to buy a stronger lock on my way home from work… Maybe even some kind of alarm system. But would the stores still be open by then?"
    n "All of a sudden, I get pulled backwards as [ch_elanor] playfully wheels my chair around and leans over my shoulder to softly speak into my ear."
    play audio "audio/sfx/item.ogg"
    show  elanor happy z at bpop, center with dissolve
    e "Would you look at that… {i}Loverboy{/i} in aisle eight needs some help, it seems."
    n "She nods in the direction of the red light flashing above the bookshelves, signalling to the staff that someone in that row needed assistance."
    play audio "audio/sfx/walking.ogg"
    hide elanor happy z at bpop, with dissolve
    n "With a sigh, I reluctantly stand up and make my way over. I already knew for a fact that [ch_elanor] wasn't going to go help them herself, so I begrudgingly begin to make my way towards aisle eight alone."
    n "I knew better than to glance back at her, though, knowing fully well that my teasing co-worker would be sporting the {b}biggest{/b} grin on her face at my misfortune."

################################################################################
## MEET REN
################################################################################
label day1_meetren:
    scene library_isle_day
    show peffect
    play audio "audio/sfx/movement.ogg"
    with GlitchDissolve

    n "Ducking around the corner and into the aisle, I was immediately met with a broad backside that was covered by what had to be the {b}comfiest{/b} looking cardigan I'd ever seen."
    n "The person whom it belonged to, however, hadn't seemed to notice me yet, so I awkwardly clear my throat and absent-mindedly shift my weight from one foot to the other."
    y "{i}Ahem—!{/i}"

    scene CG D1_LIBRARY
    hide screen dayscalendar
    show screen menuwu
    $ quick_menu = False
    $ meet_ren = True
    $ persistent.cg_d1_library = True
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    with Fade(1.0, 1.0, 1.0)

    rpc "{size=+10}{i}…Ah—!{/i}{/size}" with vpunch
    n "He seems to jump at the sudden noise before sheepishly turning around to face me. Immediately, I was taken aback by his soft demeanour, doe-like eyes, and imposing height."
    n "So {i}this{/i} was the guy who always rented out my recommended books on the display window, huh? He definitely fit the aesthetic of a cosy literature-lover needing a good book."
    n "His pink hair also reminded me of Haruko, an anime character I had recently been obsessing over with [ch_moth] during our late-night video calls. In fact, even the overall cut and style appeared vaguely similar to his…"
    n "But then again, this hairstyle could've been trending right now or something, and I just so happened to be the last to know about it."
    n "But… Now that I {b}really{/b} had a good look at him — which proved difficult considering his towering height — this stranger also seemed to bear a near {b}picture-perfect{/b} resemblance to the male lead from this webcomic I was reading."
    n "It was called \"Always with you\", and it involved the main character meeting the love of [their] life at a—"

    scene library_isle_day
    $ quick_menu = True
    hide screen menuwu
    show screen dayscalendar
    show peffect
    show ren blushing at center
    with GlitchDissolve

    $ persistent.fact_mannerism1 = True

    n "As if noticing my spaced-out look, the stranger absent-mindedly scratches at his jaw while he waits for me to snap out of my thoughts. In fact, I had been so distracted that I didn't even realise that he had been muttering quietly to himself."

    if unlockable == "kitsune":
        show ren blushing at spop, center
        rpc "{size=-6}Okay, fox-feet… Make sure your ears aren't showing…{/size}"
    elif favourite_outfit == "edgy":
        show ren flushed at spop, center
        rpc "{size=-6}Woah… You look…{/size}"
        show ren sad at spop, center
        rpc "{size=-6}But I thought you preferred softer clothing…? That's why I…{/size}"
    elif favourite_outfit == "comfy":
        show ren happy at spop, center
        rpc "{size=-6}Heh, I knew you preferred softer-looking clothing. I made the right choice with this outfit.{/size}"
    else:
        show ren flushed at spop, center
        rpc "{size=-6}I-I wasn't expecting you to show up so soon…!{/size}"

    show ren smirk at spop, center
    rpc "{i}Ahem!{/i} Um… S-Sorry, I hope I'm not bothering you."
    show ren neutral at spop, center
    rpc "I was just looking for… Uhh…"
    n "His voice pulls me back to the present, and I hastily try to make sense of what was spilling from his cherry-tinted lips."
    n "Watching him struggle with his words would've made {b}anyone{/b} feel bad, so I offer him a reassuring smile in return and an encouraging nod of my head."
    n "At that, he takes a steady inhale of air before trying again."
    show  ren flushed at spop, center
    rpc "…I need some help. I-I'm looking for a specific book, you see, but…"
    
    $ persistent.fact_mannerism2 = True
    
    n "Aaaaaand… now he's playing with the ends of his sleeves."
    n "I felt the sudden urge to reach out and stop him — did I find the action annoying? Endearing? Relatable? who knows — but instead, I held back and waited for him to find the words to speak."
    n "But… {b}wow.{/b} Even his mannerisms were eerily similar to Haruko's."
    
    $ persistent.fact_tempermentshy = True
    
    n "The endearing awkwardness and sleeve-tugging gave me a sense of déjà vu, and it honestly felt like he walked straight out of the anime and into this very library."
    n "Man, [ch_moth] is gonna {b}freak{/b} when I tell them about this later."
    n "The stranger in front of me takes in another shaky inhale before he tries to speak once more; this time with a lot more confidence in his tone and a fire in his eye."
    show  ren frown at spop, center
    rpc "…Do you have any books on native flora? The best I've found are on generic wildlife, but nothing about Corland Bay's plants."
    show  ren sad at spop, center
    rpc "Or… Maybe I'm just in the wrong aisle?"
    n "He was looking for a book about the native flora? Perhaps I should introduce him to [ch_violet]…"
    n "Chuckling to myself at the thought, I stepped closer to the tall man and began scanning the contents of the shelf beside him."
    play audio "audio/sfx/item.ogg"
    show  ren flushed z with dissolve
    n "He almost seems to flinch at the sudden closeness between us, but showed no sign of moving away. In fact, he seemed to almost lean {b}closer{/b} and incline his head towards mine."
    n "And had I not been too preoccupied with finding that book, I would've noticed how his breath hitches in his throat as my scent floods his senses."
    y "No, you're definitely in the right aisle. Those kinds of books are just… more hidden, I guess."
    n "I step past him this time and make my way over to the lower part of the shelves. Absent-mindedly, I run a finger against the spines of each book until I come into contact with one book in particular."
    play audio "audio/sfx/slide.ogg"
    n "Then, bending over slightly, I pull the book from the shelf and give the cover a once-over before offering it to the man behind me."
    y "Is this what you're looking for?"
    show  ren blushing z at bpop, center
    n "Too preoccupied with the misplaced book on the bookshelf (who brings {i}cook books{/i} to the nature aisle?), I barely notice how his blue eyes trail across my form before landing on the book held out in my outstretched hand."
    n "…Was it just me, or… Did he have a certain glint in his eyes?"
    if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
        call DLC_day1_library from _call_DLC_day1_library
    n "Was this book {b}really{/b} that interesting? Or perhaps this tall stranger was just really into nature?"
    n "Well, not that it mattered, because he was already taking a tentative step forward and revealing more of his hands from the depths of his long sleeves."
    n "With shaky fingers, I watch as the stranger reaches out and takes it from my grasp. He flips through a few pages to take in its contents, before finally settling on the book with an affirmative nod."
    show  ren smirk z at spop, center
    rpc "Y-Yes! This was exactly what I was looking for! Thank you…"
    y "I'm glad."
    show  ren happy z at spop, center
    rpc "Haha, you're like an angel sent down from heaven or something. You're so helpful. {i}Kind,{/i} too."
    y "…What?"
    show  ren flushed z at bpop, center
    rpc "…W-What?"
    show  ren blushing z at spop, center
    rpc "Oh! I-I didn't— Did I say that out loud? I didn't mean to! Ugh, that must've been so weird… I'm so sorry!"
    n "He looked as though he was about to cry now, so I hastily threw up my hands in a comforting manner and shot him a reassuring smile."
    y "Hey, it's fine! No need to freak out. I just… I wasn't expecting someone to say that about me, is all."
    show  ren smirk z at spop, center
    rpc "R-Really? …Well, I think it's true for what it's worth."
    show ren flushed z at spop, center
    rpc "{size=-6}…You {i}really are{/i} like an angel.{/size}"
    y "Um… Thanks?"
    if player == "Angel":
        n "An {b}Angel{/b}, huh? I seriously doubt that was the reason why  I was given this name in the first place, but…"
        n "It was crazy how he was able to guess my name so easily."
    n "Figuring that was my cue to leave before things got awkward, I give him one last friendly smile and subtly glance back toward the front desk. But the eccentric man showed no signs of moving; instead, he just looked down at me expectantly."
    show ren neutral z
    n "Did he want to continue the conversation? It seemed unlikely as he didn't say anything. He simply…"
    extend " Stared at me."
    n "Awkwardly, I clear my throat for what had to be the millionth time today and gesture vaguely to the reception desk behind me."
    y "Well, if you don't need any more help, I should…"
    show  ren happy z at spop, center
    rpc "…"
    n "This is just getting weird now. Should I even {b}attempt{/b} to continue this conversation or just leave?"
    n "I mean, it would seem rude to just walk away abruptly — especially considering how he's (apparently) a regular patron in a library {b}I{/b} worked at — but he wasn't making much of an effort either. So what should I do?"
    
    #hide ren happy with dissolve
 
    menu:
        #with dissolve
        "[rh_o]Keep talking to him[rh_c]":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_kiara += 1
            $ affection_elanor += 1
            show ren neutral z with dissolve
            y "So…"
            extend " Do you come here often?"
            n "Seriously, [ch_angel]? That was the best you could come up with? [dammit!c]. Now he probably thinks {i}I'm{/i} the weird one."
            show ren happy z at bpop, center
            rpc "Haha! Yes, actually! I uh… I like visiting whenever I have some free time."
            rpc "Although I usually end up coming here just to hide away in a corner somewhere and look at {i}you—{/i}{nw=0.3}"
            show ren flushed z at bpop, center
            extend "{i}r{/i} book collection! Hahaha…" with vpunch
            rpc "Y-You have a lot of interesting books here. Lots and lots of… {i}books{/i}."
            y "Uh… Yeah? I mean, it {i}is{/i} a library after all."
            y "But… sure! Whatever you say, mister—"
        "Stare back at him":
            $ affection_ren += 1
            $ affection_olivia += 1
            $ affection_jae += 1
            show ren happy z with dissolve
            y "…"
            show ren neutral z at spop, center
            rpc "…"
            y "…"
            show ren flushed z at spop, center
            rpc "…"
            show ren flushed z at spop, center
            extend " Uh."
            show ren flushed z at spop, center
            extend " Y-You shouldn't stare at me like that…"
            show ren smirk z at spop, center
            rpc "{i}Especially{/i} when it's with a stranger you don't know."
        "Politely excuse yourself and leave":
            $ affection_ren -= 1
            $ affection_violet += 1
            $ affection_conan += 1
            $ affection_leon += 1
            show ren frown z with dissolve
            y "I should probably head back to the front desk now. Sorry, but I can't be away from it for too long. Unless I want to get fired or something."
            show ren flushed z at spop, center
            rpc "W-Wait! Uhh…"
            n "He seems almost hesitant for a moment before his hand shoots out."
            n "Most of it was covered by the sleeve of his cardigan, but it was close enough to my line of sight that I could make out the faint cuts and marks lining his fingers."
            n "…Were those burn marks?"
            show ren happy z at bpop, center
            $ persistent.fact_name = True
            r "My name is [ch_ren]! I-It was nice to meet you! And… Thank you for your help!"
            n "Oh? Was he introducing himself? In that case… I take his outstretched hand and give it a gentle shake."
            n "His breath seems to catch in his throat at the contact, but he disguises it by clearing his throat awkwardly."
            if player == "Ren":
                y "Oh? I'm {i}also{/i} [ch_angel]. What a coincidence."
                y "Anyway! It's nice to meet you too, [ch_ren], but I really {i}do{/i} need to go back and—"
            else:
                y "I'm [ch_angel]. It's nice to meet you too, but I really {i}do{/i} need to go back and—"
            jump reninterrupt
        "Lie and end the conversation":
            $ affection_ren -= 1
            $ affection_teo += 1
            show ren neutral z with dissolve
            y "Ah! I just remembered that I was supposed to go do an inventory check a couple of hours ago. So if you'll excuse me—"
            show gwitch
            show ren frown z at spop, center
            play audio "audio/sfx/glitch.ogg"
            rpc "{b}{color=#a30b11}01001100\ \ \ 01001001\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 01000001\ \ \ \ \ \ \ 01010010\ \ \ \ \ \ \ \ \ .\ \ \ \ \ \ \ \ \ .\ \ \ \ \ \ .{/color}{/b}"
            hide gwitch
            show ren sad z at spop
            rpc "No, you don't."
            y "…Huh?"
            show ren smirk z at spop, center
            rpc "…"
            n "What… just happened?"
            n "The eccentric man seems almost hesitant for a moment before his hand shoots out for a handshake."
            n "Most of it was covered by the sleeve of his cardigan, but it was close enough to my line of sight that I could make out the faint cuts and marks lining his fingers."
            n "…Were those burn marks?"
            show ren happy z at spop, center
            $ persistent.fact_name = True
            if player == "Ren":
                r "If you're busy then I'll let you go. But… Y-You should know, my name is {i}also{/i} [ch_ren]. And it was nice to meet {i}you{/i}, [ch_angel]! Thank you for your help."
            else:
                r "If you're busy then I'll let you go. But… My name is [ch_ren]. And it was nice to meet you, [ch_angel]. Thank you for your help."

            if player == "Angel":
                y "…How did you know my name?"
                n "Surely there was no way [ch_ren] was be able to guess my {b}real name{/b} from a silly little nickname he made up on the spot…"
            else:
                y "…How did you know my name?"
            n "And where did his timid persona go?"
            show ren neutral z at spop, center
            r "…Your name tag."
            n "As if to prove a point, [ch_ren] reaches out to gently flick the name tag that I somehow {b}forgot{/b} that I had put on this morning."
            y "Oh."
            show ren smirk z at spop, center
            r "…"
            n "Why does he keep looking at me like that?"
            jump reninterrupt

    y "Actually… Now that I think about it, you haven't told me your name yet."
    show  ren flushed z at spop, center
    rpc "Oh! Haha, I guess you're right."
    play audio "audio/sfx/glitch.ogg"
    show gwitch
    show  ren neutral z at bpop, center
    rpc "You can call me {b}{color=#a30b11}[[ REDACTED ]{/color}{/b} ."
    hide gwitch
    n "…What?"
    extend " It was like he said something, but his voice was delayed. Was that even his voice? Was he speaking English? It almost felt like something that came out of a dream."
    y "How did you do that…?"
    show  ren smirk z at spop, center
    rpc "Do what?"
    show ren happy z at spop, center
    $ persistent.fact_name = True
    extend " Anyway! You can just call me [ch_ren] if you'd like."
    show ren neutral z at spop, center

    if player == "Angel":
        r "Is it alright if I continue to call you \"Angel\"? It's such a unique name — in my personal opinion at least, haha~"
        n "Wait… Did he just guess my real name? Or was he just using \"angel\" as a nickname? And was he {b}really{/b} flirting with me right now?"
    elif player == "Ren":
        r "Is it alright if I call you Angel, instead? It might help, s-since we share the same name, and all."
        show ren smirk z at spop, center
        r "Plus… It really suits your helpful nature."
        n "What just happened? Was I just imagining things? And was he {b}seriously{/b} trying to flirt with me right now?"
    else:
        r "Is it alright if I call you [ch_angel]? Although… {i}Angel{/i} does suit you just as well — in my personal opinion at least, haha."
        n "Seriously, what just happened? Was I just imagining things? And was he {b}really{/b} flirting with me right now?"

    show  ren sad z at spop, center
    r "…Are you okay?"
    y "Uh— Y-Yeah, I think? But…"
    y "How did you know my name? I don't remember telling you."
    show  ren neutral z at spop, center
    r "Silly, it's on your name tag."
    n "As if to prove a point, [ch_ren] reaches out to gently flick the name tag that I somehow {b}forgot{/b} that I had put on this morning."
    y "Oh."
    if player == "Ren":
        show  ren smirk z at spop, center
        r "[ch_angel] {i}does{/i} suit you more than it suits me, though."
        show ren happy z at bpop, center
        r "{size=-6}Wow, we have so many similarities… Maybe it's a sign… Haah…{/size}"
    else:
        show  ren smirk z at spop, center
        r "[ch_angel] {i}is{/i} a cute name, though."
        show ren happy z at bpop, center
        r "{size=-6}And it's really, really, {i}reeeeeeally{/i} fun to say. Especially over and over again!{/size}"
    y "…{i}Right{/i}? Anyway—"

    label reninterrupt:
    show ren smirk z at spop, center
    r "Say, are you busy later? I'd love to thank you for helping me find this book."
    n "Seriously, what was up with this guy? One minute he's shy, and the next, he's bold. It was almost like he was putting up several fronts to see which one I responded to better…"
    y "Actually, I'll be busy this afternoon. I need to buy a new lock for my apartment."
    show  ren sad z at spop, center
    r "…A new lock? That doesn't sound good. Can I ask why?"
    n "I guess it wouldn't hurt to tell him… I mean, what was he going to do? Personally show up at my doorstep and test the new lock himself?"
    y "Apparently someone broke into my apartment last night, and I didn't notice. I don't think they stole anything, but still. It's {i}creepy.{/i}"
    y "I figured it's better to be safe than sorry, you know?"
    show  ren happy z at spop, center
    r "Yeah. But… It sounds like instead of a lock, you just need to jump the scumbag when they least expect it and {i}beat 'em up{/i} to teach them a lesson."
    show  ren smirk z at spop, center
    r "Stay up all night if you have to. Really get the edge on them."
    n "I couldn't help but let out a genuine chuckle at his suggestion. If I had to choose, then {b}this{/b} would have to be the side of him that I preferred. He seemed at ease, and his words weren't as forced or awkward."
    y "Yeah? And who's gonna be the one to beat the guy up at 3AM? Because last I checked, I'm not really the type to go around throwing punches at people I don't know. And {i}definitely{/i} not before the sun is up and shining."
    show  ren flushed z at spop, center
    r "…I could do it for you."
    y "You? But— I mean, we don't even know each other that well, and…"
    show  ren happy z at spop, center
    r "That's fine. I could tell you {i}aaaaaall{/i} about myself on the walk there."
    show  ren neutral z at spop, center
    r "My whole life story and everything. Where I was born, the school I went to, how many cute librarians I've met…"
    show  ren smirk z at spop, center
    r "Which happens to be {i}one,{/i} so far."
    n "Before I could even comment on his sudden confidence, [ch_ren] seems to pick up on my discomfort at his choice of words — if it even {i}was{/i} discomfort that I was feeling — and hastily backtracks."
    show  ren sad z at spop, center
    r "H-Hey… Or not. I was just messing around. I-I didn't mean to make you feel uncomfortable."
    n "There it was again; that subtle shift in his personality. But… Now that he mentioned it, would it {b}really{/b} hurt to invite him to my place for the night?"
    n "He definitely looked like he could handle himself in a fight (his contrasting outfit aside), so maybe it wasn't so bad of an idea?"

    #hide ren with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "[rh_o]Invite him over[rh_c]":
            $ affection_ren += 10
            $ d1_inviteren = True
            $ persistent.d1_inviteren = True
            y "Actually, you know what? {i}Would{/i} you mind coming over and staying the night? I'd feel a bit safer knowing someone else was around."
            show ren flushed z at spop, center
            r "O-Oh! You… You actually want me to come over?"
            show ren happy z at bpop, center
            r "I mean, yeah!"
            show ren neutral z at bpop, center
            extend " Sure!"
            show ren happy z at bpop, center
            extend " Definitely!"
            n "He seems a bit {b}too{/b} eager for this."
            y "If it's not too much trouble, I gu—"
        "Don't invite him over":
            $ affection_ren -= 10
            $ persistent.d1_dontinviteren = True
            y "Sorry, I just don't know you well enough for that."
            show ren sad z at spop, center
            r "N-No, I totally get it. I don't know why I suggested that in the first place…"
            show ren neutral z at spop, center
            n "…"
            n "Great. Now it's back to being awkward again."
            y "Well, anyway—"
    $ choice_style = "default"

    e "{size=-6}…Where [are] [they]? [ch_angel]?{/size} {i}Ah-!{/i}"
    play audio "audio/sfx/heels alt.ogg"
    play audio ["<silence .3>", "audio/sfx/shoes alt.ogg"]
    show ren angry z at spop, left:
        xalign 0.2
    show elanor happy z at spop, right:
        xalign 0.8
    with easeinright
    e "There you are!" with vpunch
    show elanor frown z at spop, right:
        xalign 0.8
    e "Someone at the front desk is looking for you, and— {i}Oh!{/i} Sorry, are you busy right now? I can—"
    n "…Impeccable timing as always, [ch_elanor]."
    y "—No, it's fine. I think everything is already handled here, right?"
    show  ren sad z at left:
        xalign 0.2
    show elanor blushing z at right:
        xalign 0.8
    n "I give the two of them a soft smile before making my way towards the reception desk. But as I pass by [ch_elanor], I gently clasp a hand on her shoulder and shoot her a playful look of my own."
    y "If you need more help, I'm sure [ch_elanor] here can assist you! She {i}loooooves{/i} helping others, right?"
    show  ren angry z
    n "And as I turn to leave, I barely miss the way [ch_ren]'s eyes zone in on my hand resting on [ch_elanor]'s shoulder."

################################################################################
## MEET CONAN
################################################################################
label day1_meetconan:
    scene library_lounge_day
    play music "audio/bgm/Refreshing Scent.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 1.0, 1.0)

    n "Hours seem to pass by in a blur, and soon enough, I find myself resting up in the employees' lounge. My mind drifts back to the guy from earlier, and I couldn't help but wonder what happened to him afterwards."
    n "Did he rent out the book I offered? What about my recommended novel of the week? [ch_ren] surely was… {b}strange{/b} to say the least, but I had to admit that he {b}did{/b} seem kind of cute with his oversized cardigan and timid demeanour."
    n "He still gave me off-putting vibes, though — especially with his ever-changing personality. And if I had to be completely honest, that 'shy and timid' persona that he displayed felt rather… {b}forced{/b} to me."
    n "It was almost as if he saw it on TV or something and wanted to try it out himself — and I just happened to be one of his first victims. But who was I to call him out for it? That was his business if he wanted to act all shy and demure."
    play audio "audio/sfx/walking.ogg"
    show  conan frown with dissolve
    $ meet_conan = True
    c "…[ch_angel]? Everything alright? It's not often I find you in here at this time."
    n "[ch_conan], my boss, startles me as he suddenly appears in the entranceway."
    n "Everyone saw him as some kind of blessing to this institution, because the moment he showed up, all forms of trouble seemed to disappear overnight."
    n "Those low-life teens started causing chaos elsewhere, and the rumoured gangs became few and far between."
    n "At first I thought that he might've been linked with these criminals because of his intimidating gaze and facial scars, but then I got to know him better and found out that he held a massive soft spot for those dear to him."
    n "Though, much like [ch_elanor], [ch_conan] felt more like a father figure with how much he fretted over his staff and their well-being."
    n "I mean, he {b}literally{/b} installed a new air-conditioner and water dispenser last week because one of his employees fainted due to heatstroke…"
    n "It wasn't anything {b}too major{/b}, but it was nice to know that our boss was considerate enough about the people he hired. I doubt I could say the same about my old job in the city."
    n "[ch_conan] was also nice to chat to whenever I went on my breaks, and would always encourage me to take as much time as I needed before I returned to my desk."
    n "But after realising that I had (once again) been spacing out, I pull myself away from my thoughts and turn to offer my boss an acknowledging smile."
    y "Yeah, I'm fine. Just… taking a short break. I'll be back out there soon."
    show  conan neutral at spop, center
    c "Take as long as you need. Don't overwork yourself."
    n "He seems hesitant to leave — if the way he was shifting from one foot to the other was any indication. He shoots me a concerned look before opening his mouth, only to close it once more in contemplation."
    show  conan sad at spop, center
    c "…Have you seen [ch_elanor]? I asked her to come see me regarding the unsorted novels in the storeroom, but she's yet to show up."
    y "[ch_elanor]? Last I saw her, she was talking to one of our patrons in aisle eight. Maybe she's still there?"
    show  conan neutral at spop, center
    c "Hm. I'll have to check again then… Thank you."
    play audio "audio/sfx/walking.ogg"
    hide conan with dissolve
    n "And with that, he disappeared just as quietly as he came."
    n "But… that was odd. It wasn't like [ch_elanor] to suddenly go missing. Was she still occupied with [ch_ren]? It'd been a while, so I figured she would've finished helping him and left by now."
    n "Oh well, I'm sure she'll turn up sooner or later. [ch_ren] didn't seem much like a talkative person, anyway."
    n "Jeez, why did my thoughts keep returning to that eccentric man?"

    scene library_reception_day
    show peffect
    with GlitchDissolve

    n "Deciding that I wasn't going to waste my time thinking about any more pink-haired guys — my beloved Haruko aside — I get up from the lounge and meander my way back towards the front desk again."
    n "But once I arrive, I immediately notice that my chatty co-worker was {b}still{/b} nowhere to be found."
    n "It was just like my boss had said; [ch_elanor] wasn't anywhere to be seen, and it wasn't like her to leave the reception desk unattended for so long."
    n "Maybe she managed to knock over a pile of books again and was busy cleaning it up? It certainly wouldn't be anything out of the ordinary for her."
    y "Well, whatever. I'm sure she'll turn up again soon."
    play audio "audio/sfx/paper.ogg"
    n "The impact from me plopping down into my office chair causes some of the papers around me to rustle — and a bright, pink sticky note fluttering around captures my attention."
    n "Assuming it was left here by [ch_elanor], I peel the folded note off my computer screen and read it."

    if d1_inviteren == True:
        n "{b}\"Angel!\"{/b}"
        n "Unfolding it read the following:"
        n "{b}\"I'll wait for you after work. But if you change your mind about our deal, just keep walking. I'll take the hint, don't worry! ^^\"{/b}"
        n "{b}\"— that stuttering guy from aisle 8 <3\"{/b}"
        n "The stuttering guy from aisle eight? I couldn't help but crack a smile at the name [ch_ren] chose for himself."
    else:
        n "{b}\"You can throw this away if you want.\"{/b}"
        n "Unfolding it read the following:"
        n "{b}\"(xx)xxx-xxx-xxx\"{/b}"
        n "{b}\"— that stuttering guy from aisle 8 <3\"{/b}"
        n "Did [ch_ren] leave this note? And was that his number? I had to admit, he really was a persistent fellow."

    n "And before I could allow [ch_elanor] the chance to manifest behind me and to tease me to kingdom come, I pocket the note and go back to sorting through the stack of returned books left on the desk."

################################################################################
## MEET LEON / MEET JAE
################################################################################
label day1_meetjaeleon:
    scene oh_street_night
    play music "audio/bgm/Childhood Friend.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/street.ogg" fadein 1 fadeout 1
    show ceffect
    with Fade(1.0, 1.0, 1.0)

    if d1_inviteren == True:
        $ rpos = cleft
        $ jpos = center
        $ lpos = cright
    else:
        $ rpos = center
        $ jpos = tleft
        $ lpos = tright

    if d1_inviteren == True:
        n "True to his word, I catch a glimpse of [ch_ren] patiently waiting for me on one of the benches as I pack up for the day and leave the library."
        n "From afar, he looks like an oversized puppy waiting for his owner to return from work, and admittedly, I find it rather cute. Especially with how his figurative tail starts to wag upon my arrival."
        n "[ch_ren] seems all too happy to see me, but before I can even call him out on it, he offers me a bottle of water that (I assumed) he bought from one of the convenience stores down the street."
        play audio "audio/sfx/shoes alt.ogg"
        show ren happy at bpop, center with dissolve
        r "You sure worked hard today! Now you can finally rest, huh?"
        n "He's looking down at me again with a glimmer of expectancy in his eyes, so I hesitantly take the bottled water from his grasp and give him an affirmative nod of my head."
        y "Th-Thanks…"
        show ren neutral at bpop, center
        r "Mm, no problem!"
        show ren smirk at spop, center
        r "D-Did you wanna head off now, or do you wanna rest for a bit? I mean, you {i}were{/i} standing a lot today…"
        show ren sad
        n "He seems almost lost in his thoughts now, and I wonder how he knew what I'd been doing all day. After all, I figured he would've left after he found that book, but… maybe he stayed a bit longer to read it?"
        y "Oh no, I'm fine. But… Do you think we could make a quick detour on the way? I still need to—"
        play audio "audio/sfx/shoes alt.ogg"
        show ren angry at bpop, rpos
    else:
        n "While walking home from work, I couldn't shake off the feeling of someone watching me from behind. Yet every time I turned around, no one was there."
        play audio "audio/sfx/other world.ogg"
        n "It felt like a pair of eyes were on me and watching my every move, which was strange, considering how I'd never noticed this when I first started walking to and from my workplace."
        n "Maybe I was just imagining things? Or maybe I was just too tired?"
        n "Rolling my eyes at my own paranoia, I continue on my walk. But I didn't make it that far before—"

    if d1_inviteren == True and unlockable == "sunpup":
        jump monsterpupeasteregg

    play audio "audio/sfx/running.ogg"
    show jae happy at jpos
    with easeinright
    $ meet_jae = True

    j "[ch_angel]!" with hpunch

    if d1_inviteren == True:
        show ren angry at rpos

    show jae happy at jpos
    play audio "audio/sfx/walking.ogg"
    show leon neutral at lpos
    with easeinright
    $ meet_leon = True

    l "Heyo!~" with hpunch
    n "Ah… I could recognise those boisterous voices anywhere."
    n "The first one belonged to Jae-Hyun — or simply just [ch_jae] — a guy I had met at university. He sat next to me during the first few days of orientation, and even offered to lend me his phone charger when my battery started to run out."
    n "He's a fun guy to be around, though his extroverted and energetic personality was often hard to keep up with."
    n "But [ch_leon] — the other guy awkwardly hanging off of [ch_jae]'s arm — was a different story. We'd practically known each other since we were babies, but he moved away from Corland Bay when we were still in elementary school."
    n "I wasn't sure when he moved back to the Bay, but it was great knowing I'd be able to see him again."
    n "I just wished I could find the time to hang out with him just like we used to. But I was always busy with work and he was always busy playing volleyball and taking care of his sick mother in the hospital."
    n "Before I knew it, I was being pulled out of my thoughts by [ch_jae]'s bubbly laughter."

    show jae frown at spop, jpos
    j "Hey hey! Still with us?"
    show leon happy at spop, lpos
    l "Hey, [ch_angel]. Finally finished with work?"

    label meet_jaeleon:
        if d1_inviteren == True:
            show leon neutral at spop, lpos
            l "Oh? And who's this?"
            show ren neutral at cleft
            if player == "Ren" or player == "Leon" or player == "Jae":
                y "This is {i}also{/i} [ch_ren]. We actually met at work today—"
            else:
                y "This is [ch_ren]. We actually met at work today—"
            n "Uh, maybe it wasn't a good idea to tell [ch_leon] — the human personification of overprotective — that I had just met the man today. What would he think if he found out I was bringing home a complete stranger?"
            y "He uhh… He usually rents out my recommended books at the library. Anyway!"
            y "[ch_leon], [ch_jae]… This is [ch_ren]."
            y "[ch_ren], this is [ch_leon] and [ch_jae]. Unfortunately, these guys are my friends."
            show leon happy at spop, lpos
            l "It's truly unfortunate to know a handsome bloke such as myself."
            n "[ch_leon] dramatically clutches the spot above his heart as he leans further into [ch_jae]'s shoulder."
            show jae happy at bpop, jpos
            j "So, you're [ch_ren]? Are you new here? I like to think I know everyone here in the Bay, but it seems you've proven me wrong!"
            show ren sad at spop, rpos
            r "Um… Y-Yeah… I recently moved here a couple of months ago…"
            show leon neutral at spop, lpos
            l "Oh, same as [ch_angel]? I'm pretty sure [they] moved back here like… what? Two months ago, right?"
            n "[ch_leon] looks at me for confirmation, and I meekly nod my head. Strange how I've only been back here for two months, and I've yet to find enough time to catch up with all my friends."
            show ren flushed at bpop, rpos
            r "O-Oh, hahaha! What a coincidence…"
            show jae smirk at bpop, jpos
            j "Anyway! Talking about moving is boring! Do you wanna come hang with us?"
            show ren frown at rpos
            show jae happy at jpos
            n "I hardly notice the way [ch_ren] gets shoved to the side by [ch_jae] — intentionally or not — nor could I make out the scowl on his face as soon as the excitable man leans a little too close into my personal bubble."

        show jae happy at bpop, jpos
        j "We were just about to head over to Club Shoreline! Do ya wanna come? I'm sure [ch_leon] wouldn't mind paying for you as well!"
        show leon frown at spop, lpos
        l "Oi! I don't mind paying for [them], but who said anything about paying for you?"
        show jae smirk at bpop, jpos
        j "I did, just now! Thaaaanks [ch_leon], you're the best!~"
        n "I don't miss the way [ch_leon] rolls his eyes at [ch_jae]'s antics before settling his gaze on me once more."
        show leon neutral at spop, lpos
        l "Do ya wanna tag along? I really don't mind paying if you do."

        if d1_inviteren == True:
            y "Sorry guys, I've actually already made plans."
            show leon smirk at spop, lpos
            l "And do these plans have anything to do with this lanky fellow?"
            show ren sad at spop, rpos
            r "{size=-6}…My name is [ch_ren].{/size}"
            y "Actually, yeah… I promised I'd hang out with him today."
            show jae neutral at bpop, jpos
            j "Aww, he can come clubbing with us too! The more the merrier!"
            show ren frown at spop, rpos
            r "…I-I'd rather not."
            y "Sorry, maybe another time. I'm kinda drained from work anyway, so…"
        else:
            y "Sorry guys, as much as I'd love to, I'm kinda drained from work… Maybe another time, though."

        show leon neutral at spop, lpos
        l "Hey, no worries, darl'. Just make sure you take it easy when you get back home, yeah?"
        n "He shoots me a considerate smile before throwing an arm over [ch_jae]'s shoulder."
        show leon happy at bpop, lpos
        l "Well then! If you'll excuse us, I gotta find a way to get this knucklehead to cover his own entry fees. We can all catch up another time, okay?"

        if d1_inviteren == True:
            show leon smirk at spop, lpos
            l "And if you need help with anything, just give me a ring, yeah? I'll watch my phone like a hawk tonight!"
            show leon happy at bpop, lpos
            l "It was nice catching up with ya again, darl'! And nice meeting you too, Ron!"
            play audio "audio/sfx/movement.ogg"
            play audio "audio/sfx/sprinting.ogg"
            hide jae
            hide leon
            with moveoutleft
            n "As they leave, I notice the way [ch_leon] looks [ch_ren] up and down, almost as if he was sizing him up. But [ch_jae] — like always — ignores the mood and thumps [ch_leon] in the back to encourage him to walk faster."
        else:
            play audio "audio/sfx/movement.ogg"
            play audio "audio/sfx/sprinting.ogg"
            hide jae
            hide leon
            with moveoutright

        n "I watch as they both throw a carefree wave over their shoulders as they both head off in the direction of the nightclub a few blocks down the street."

        if d1_inviteren == True:
            y "So… That wasn't awkward at all…"
            play audio "audio/sfx/shoes alt.ogg"
            show ren frown at center with easeinleft
            n "I turn to look at [ch_ren], but his eyes seem to be fixated on the two retreating figures. He doesn't seem to snap out of it, so I gently call out his name again."
            show ren happy at bpop, center
            r "O-Oh! Sorry! Do you wanna… Do you wanna head back home now?"
            n "In the end, we made a quick detour to the local locksmith before heading back to my apartment."
            jump day1_inviteren
        else:
            n "It was nice to see them again, especially since I had been so occupied with moving back home and settling in."
            n "It didn't feel like that long, but two months was a long time, and I somehow couldn't find a single chance to hang out with either of them yet."
            n "Oh well, there's always next time."
            n "Putting those thoughts to rest, I start making my way back home once more."
            jump day1_rejectren

################################################################################
## INVITE REN SCENE
################################################################################
label day1_inviteren:
    scene oh_complex_night
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    stop ambience fadeout 2.0
    show peffectp
    show ren neutral
    with Fade(1.0, 1.0, 1.0)
    $ location_ren = "oh"

    y "So, this is my place… You'll have to excuse the mess; I wasn't expecting to have anyone over."
    show  ren happy at spop, center
    r "Hey, don't worry about it. I know you're not a messy person."
    show ren flushed at spop, center
    extend " I mean—"
    extend " From what I can tell, y-you don't really seem like the type…"
    y "Yeah? Well… I hope you can still keep that image of me {i}after{/i} you see the state of my place."
    show  ren happy at spop, center
    n "His soft laughter echoes down the hallway and almost drowns out the sound of my neighbour opening her door."

    play audio "audio/sfx/door.ogg"
    play audio "audio/sfx/heels.ogg"

    show ren angry at spop, center
    show violet blushing at spop with easeinleft
    v "Oh!"
    show  ren neutral
    n "[ch_violet] almost seems embarrassed as she jumps behind her door, clearly not expecting someone to be around at this time. But she brushes it off with a soft smile and steps outside."

    play audio "audio/sfx/heels alt.ogg"
    play audio "audio/sfx/walking.ogg"
    show  violet happy at spop, tleft
    show ren neutral at spop, tright
    with easeinleft
    v "Hello again, [ch_angel]! We seem to be bumping into each other a lot today, huh? {i}Oh—{/i} Who's this?"
    n "Um… How do I explain to my neighbour that [ch_ren] {b}wasn't{/b} some guy I had just met at work today?"
    n "I'm certain she'd chew me out for bringing home a complete stranger, but still… He didn't exactly seem like the type to murder me in my sleep."
    n "In fact, he seemed more like the type of guy to ask me to return his order because he asked for no pickles or something."
    y "Err, this is—"
    show  ren angry at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5), tright
    r "I'm [ch_ren]."
    n "Immediately, his large frame blocks my view as he steps in front of my neighbour and me — almost as if he wanted to put as much distance between us as possible."
    n "One of his hands shoots out from inside his pocket, and he gruffly offers it to [ch_violet] for her to shake."
    n "Concerned about his abrupt actions, I sidestep him and look up to gauge his expression."
    show  ren happy at spop, tright
    r "…"
    show  ren neutral at spop, tright
    r "I'm a friend of [ch_angel]'s."
    show  violet sad at spop, tleft
    v "I… See. I haven't seen you around before, though. Are you new to the area?"
    y "Relax, Vi. He's not a serial killer or anything."
    n "At least… I sure hope he wasn't. And why did I feel the sudden urge to defend him? It wasn't like I could confidently say that he was some 'holy being' that flew down from heaven, or something."
    n "Maybe {b}he{/b} was the one who needed to be called 'angel' instead…? Ah well, it didn't really matter."
    y "{i}Really.{/i} [ch_ren] actually offered to stay at my place for the night in case that creep decides to come back."
    show  violet blushing at spop, tleft
    v "Oh! Well… I mean… He certainly has the height for it."
    show  ren happy at spop, tright
    r "Haha, I get that a lot…"
    show ren neutral at spop, tright
    r "But don't worry, [they] [are] safe in my hands."
    show  violet neutral at spop, tleft
    v "Well… alright then. A friend of [ch_angel] is a friend of mine."
    show violet frown at spop, tleft
    extend " But I have my eye on you, Mr. totally-{i}not{/i}-a-serial-killer!"
    n "She \"whispers\" the next part to [ch_ren] under her breath, but clearly had the intention of letting me hear it all as well."
    show  violet angry at spop, tleft
    v "Just remember that I know what you look like now — so don't complain if you see your face plastered all over milk cartons soon enough!"
    show  violet happy at spop, tleft
    show ren flushed at tright
    v "Welp, alriiiighty then! Enjoy your night! And no funny business, you two."
    show violet happy at spop, tleft
    v "I'm off for my walk now. Toodles!"

    play audio "audio/sfx/heels.ogg"
    hide violet with moveoutleft
    play audio "audio/sfx/shoes alt.ogg"
    show ren flushed at spop, center with easeinleft
    r "Uh…"
    y "Ignore her. {i}Please.{/i}"
    show  ren happy at spop, center
    r "Alright."
    r "…"
    show  ren neutral at spop, center
    r "…"
    show ren smirk at spop, center
    r "…Okay, but I gotta ask… Was she holding a potted plant? …On a {i}walk?{/i}"
    y "{i}…Yes.{/i} She was."

    scene angel_lounge_night
    play audio "audio/sfx/door.ogg"
    play audio "audio/sfx/movement.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show peffectp
    with GlitchDissolve
    n "Dropping my keys into the bowl, I shrug out of my coat and drape it over one of the chairs near the entrance."
    y "{i}Welp{/i}… Make yourself at home!"
    show  ren sad with dissolve
    n "Turning to [ch_ren], I watch as he awkwardly shuffles about in the hallway, almost uncertain if he should come inside or not. He moves to take off his shoes, and I watch in awe as he neatly stacks them next to the umbrella rack."
    show  ren flushed at bpop, center
    r "Oh— Are you the type to leave your shoes on at home? S-Sorry! I'll—"
    y "No, no, you're fine!"
    hide ren with dissolve
    n "Ugh, he really was adorable. But now that he was here… I wasn't quite sure what to do next."
    n "Usually, I'd pop on a TV show or some anime while I chow down on some takeaway food — or even just talk with [ch_moth] until some unreasonable hour in the morning — But now that I had company over, I wasn't quite sure what to do."
    n "I didn't even know what [ch_ren] liked to do in his free time…"
    
    play audio "audio/sfx/item.ogg"
    show  ren happy z at bpop, center with dissolve
    n "Turning to face the pink-haired man once more, I almost jump back in fright. {b}Clearly{/b}, I wasn't expecting him to get so close to me while I was lost in thought."
    n "I could almost feel the heat radiating from his large frame and feel the small puffs of air leave his nostrils as he shyly leans down to look at me."
    y "Oh! Um— So…!"
    n "Breathe, [ch_angel], breathe."
    y "Was there anything you wanted to do, {i}oooor…?{/i} Because I usually just…"
    n "[dammit!c], it was hard to think straight when he was standing so close to me and wafting his {b}stupidly{/b} strong scent of mint and fresh linen in my direction."
    n "Why was I even so attentive to the way [ch_ren] smelled? Wow, I'm beginning to sound like a creep."
    show  ren neutral z at spop, center
    r "Nah, I don't really have anything I need to do. You can just go about your normal routine if you want, and I'll try not to get in your way."
    show  ren smirk z at spop, center
    r "Or you can just put me in a corner somewhere and pretend I'm not there. Whatever works for you!"
    y "No offence, but you take up much more room than you think. So I doubt that would work."
    show  ren happy z at spop, center
    r "Haha, touché."
    n "Once again, I found myself being drawn in by his soft laughter, and I couldn't help but chuckle along with him. Was it always this easy talking to him? It was like we were childhood friends reminiscing about old times or something."
    n "Except the only one making it awkward now was me."
    show  ren neutral z
    n "Glancing back at [ch_ren], I notice how he's {b}still{/b} looking at me with those expectant eyes of his as he looms over me in the entryway."
    n "He obviously didn't want to do something I'd be uncomfortable with, and he couldn't really suggest anything since this wasn't his home. So, I guess the choice was up to me after all."

    menu:
        "Watch some television":
            $ ren_switch += 1
            $ affection_ren += 1
            $ affection_leon += 1
            $ affection_olivia += 1
            $ affection_kiara += 1
            show ren neutral z
            y "Well then… I usually just watch TV while I get ready for bed. Do you wanna watch something to pass some time?"
            show ren happy z at spop, center
            r "Sounds great to me!"
        "[rh_o]Make a late-night snack[rh_c]":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_violet += 1
            $ affection_jae += 1
            $ d1_makesnack = True
            show ren neutral z
            y "Are you hungry? I think I've got some leftover takeaway still in the fridge that I can heat up. Or we can raid my pantry for some snacks if you prefer."
            show ren neutral z at spop, center
            r "I-Is that okay? I don't want to be a bother."
            y "Not at all. I'm feeling a bit peckish anyway."
            show ren happy z at spop, center
            r "Well, alright then!"
        "Suggest getting ready for bed":
            $ affection_ren += 1
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_teo += 1
            show ren neutral z
            y "It's getting rather late, isn't it? Did you just want to get ready for bed? I can show you the bathroom while I get the air mattress out."
            show ren flushed z at spop, center
            r "I-It's fine! I don't want to be a bother. I can just… sleep on the floor or something. I don't mind, honest!"
            y "Hey, don't worry about it. It's not a bother at all. Besides, I have timber flooring. I'll just be two seconds!"
            n "I turn and make a beeline for my closet before he can respond."
            hide ren with dissolve
            jump sleeping
        "[de_o]Ask him to leave[de_c]":
            show ren neutral z
            n "No matter how I look at it, [ch_ren] {b}really was{/b} some random stranger that I'd impulsively invited to my house, and I couldn't help but feel a bit uneasy with the situation."
            n "Plus, even [ch_violet] herself had suspicions of him. That alone should've been enough of a warning sign."
            n "Turning to [ch_ren] once more, I offer him a sympathetic smile before gesturing towards the door."
            y "Actually… Maybe this wasn't a good idea after all. We just don't know each other that well, and I—"
            show ren sad z at spop, center
            r "Oh, n-no! I get it. I'm sorry if I made you uncomfortable. I'll just—"
            n "I watch as he almost trips over his own shoes at the doorway."
            show ren blushing at spop, center with dissolve
            r "Well… I'll be going then. But if something happens or you change your mind… Um… H-Here's my number!"
            n "Quicker than I anticipated, [ch_ren] reaches into his pocket to shove a crumpled up, pink sticky note into my hand."
            y "Oh! Uhh, Okay. Yeah. Thanks [ch_ren]."
            show ren happy at bpop, center
            r "Y-Yeah! No problem! …Bye!"
            n "He doesn't seem to move from his spot in front of my door, that is, until I tilt my head and offer him a confused look."
            hide ren with dissolve
            n "And just like that, [ch_ren]'s body seems to move like it's on auto-pilot as he makes his way towards the staircase without so much as a glance behind him."
            scene angel_bed_night
            show peffectp
            with Fade(1.0, 1.0, 1.0)
            n "As I started getting ready for bed, I decide to quickly video call [ch_moth] to tell them about what had happened today."
            jump mothaltintro

    hide ren with dissolve

    if d1_makesnack == True:
        n "Settling onto the couch with some microwaved food and snacks, [ch_ren] and I then decided on something to watch."
    else:
        n "Once we were both seated and comfortable on the couch, I picked up the remote and decided on something to watch."

    n "There wasn't much on at this time besides some B-list horror flick — and to my surprise, I find out that [ch_ren] actually {b}liked{/b} those kinds of movies."
    n "Or, at least, he {b}seems{/b} to enjoy it with the way he was hunched over in his seat, gaze intently staring at the screen as a hunt sequence begins."

    play music "audio/bgm/The One Who Approaches.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/heartbeat.ogg" fadein 1 fadeout 1

    n "But I suppose I could understand the intrigue; seeing as once I glanced back at the television, I found myself completely {b}enraptured{/b} by the suspense and overall chilling atmosphere of it all."
    n "The killer was chasing down his victim now, and I watch with bated breath as he stalks his way towards the door, cutting off the glow of light from underneath the door frame."
    n "Almost smugly — like he knew exactly where his victim was hiding — the masked killer knocks on the door before letting himself in."
    n "He walks with heavy footsteps towards the edge of the bed before {b}ever-so-slowly{/b} bending down,"
    extend " lifting the quilt up,"
    extend " raising his axe, and—"

    stop music fadeout 1
    play audio "audio/sfx/found you.ogg"
    show glitch_1:
        parallel:
            function WaveShader(20.0,10.0,0.8)
    show ren angry at bpop, center
    with vpunch
    hide glitch_1

    r "{size=+10}AH!{/size}" with vpunch
    y "{size=+10}WAH!{/size}" with hpunch

    n "It wasn't the jump scare that got me — but rather, [ch_ren]'s abrupt yelp. Clenching my shirt where my rapid heartbeat thrummed against my chest, I spare a glance at the lanky man with fleeting anger in my eyes."

    stop ambience fadeout 2.0
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1

    show ren sad at spop, center
    r "S-Sorry! I wasn't… I really didn't think a cheap jump scare like that would get me, ahaha…"
    y "And here I thought you enjoyed watching these kinds of films."
    show  ren flushed at spop, center
    r "I-I do… I just… I guess I wasn't paying much attention at the time."
    y "I see."
    n "I {b}didn't{/b}, in fact, see."
    show  ren neutral at spop, center
    r "We can change the movie if you'd like. You don't have to watch it because of me. I know you prefer watching anime, anyway."
    y "Nah, I don't mind watching some scary movie if yo—"
    extend " Huh? How did you know I liked watching anime?"
    n "That \"side\" of me wasn't something I'd go around telling strangers, and I'd certainly remember if I told it to [ch_ren]."
    show  ren sad at spop, center
    r "Oh! Uh…"
    show  ren blushing at spop, center
    r "I uh… I saw one of your posters on your wall when we came in. {i}Attack on Giants{/i}, or something, I think?"
    n "Oh… {b}right.{/b} I forgot that I'd hung that up when I first moved into my apartment. But I'm surprised that he noticed it from all the way in the lounge room."
    n "But… Shouldn't it be dark by now in that hallway? It's not like there were any windows to let in the moonlight, and I hadn't turned the light on yet."
    show  ren flushed at spop, center
    r "I actually like that anime too. I've recently started watching it because… Well, I thought it looked interesting."
    n "{b}HE{/b} watches Attack on Giant?! Well… now that I thought about it, it made a lot of sense. He {b}definitely{/b} gave off Haruko vibes, and his oddly specific hairstyle and timid personality were proof of that."
    n "Then again… It really might've been a coincidence after all. But there was no harm in asking, right?"
    y "…Is that why you styled your hair like that? Because it honestly reminds me of one of the characters from it. He's… one of my {i}favourite{/i} characters, actually. Do you know him? Haruko? He's the sorcerer who—"
    n "C'mon [ch_angel], tone it down — this wasn't [ch_moth] you were gushing to. No one needed to see this cringy side of you. Although… Looking at [ch_ren], he {b}did{/b} seem to be interested in what I had to say."
    n "But then again, he was probably just being nice."
    y "…Ah, maybe it {i}is{/i} just a trending haircut or something. Sorry."
    show  ren happy at bpop, center
    r "Haha, I like Haruko too! He's very timid and sweet, isn't he? I guess that's why he's a fan favourite, huh?"
    show ren neutral at spop, center
    r "…"
    show  ren smirk at spop, center
    r "D'you normally go for guys like him?"
    n "There's that switch in personality again. Was he always like this? I was beginning to think that it was {b}more{/b} than just an act he was putting on."
    show  ren smirk at bpop, center
    r "He's your type, right?"
    y "Actually…"
    n "I get a weird sense of déjà vu from his words, and I find myself thinking back to the time when [ch_moth] asked me that {b}very same{/b} question."
    n "And now that I thought about it… [ch_ren] {b}definitely{/b} fit the description I gave them. He had Haruko's looks and personality, but also liked to dress in that cosy, soft academia aesthetic that I liked."
    n "…But my interests were ever-changing and dependant on my hyperfixations, so I couldn't say for certain what my current type was."
    n "As if noticing my far-off stare, [ch_ren] breaks the silence by talking once more."
    show  ren flushed at spop, center
    r "O-Oh, but you asked about my hair, right? I guess it {i}does{/i} have something to do with Haruko but at the same time…"
    show ren smirk at spop, center
    extend " {i}not really{/i}."
    show  ren happy at spop, center
    r "I chose this hairstyle because of… {i}other{/i} reasons."
    n "Well, that certainly was ominous."
    n "But before I could ask, I watch as [ch_ren] subtly tries to mask a yawn by turning his head to the side while covering his mouth. It was endearing how he tried to pass it off as though he was simply looking around the room, but I knew better."
    y "…Tired? I can go get your bed set up now if you'd like. Just give me a second to pull out the air mattress."
    show  ren flushed at spop, center
    r "I-It's fine! I don't want to be a bother. I can just sleep on the floor or something. I really don't mind, {i}honest!{/i}"
    y "Uh… But I have timber flooring…? Seriously, don't worry about it. I'll just be two seconds!"
    hide ren with dissolve
    play audio "audio/sfx/fabric.ogg"
    n "I get up from my spot on the couch and make a beeline for my closet before he can respond."

    label sleeping:
        play audio "audio/sfx/walking.ogg"
        n "And yet, I barely got three meters away before I could hear the heavy, tell-tale footsteps of [ch_ren] following close behind me once more — almost like a lost puppy."
        n "It was honestly… kind of cute?"
        n "Shaking my head to dismiss those thoughts, I pull out my trusty air mattress from the closet and begin setting it up in the lounge room."
        n "…"
        n "…That is, until I found out that it had a massive, gaping hole on the side."
        n "Those [damn] rats! I swear, if I had the chance to move apartments, I'd take it in a heartbeat. But until then, I'll continue to send complaint after complaint to that good-for-nothing landlord."
        show  ren flushed at spop, center with dissolve
        r "R-Really… I don't mind sleeping on the floor."
        y "And like I said, I have uncomfortable timber flooring. Unless…"
        hide ren with dissolve

        menu:
            with dissolve
            "[rh_o]\"You could share my bed.\"[rh_c]":
                $ d1_sharebed = True
                $ affection_ren += 1
                $ affection_moth += 1
                $ affection_teo += 1
                $ affection_olivia += 1
                $ affection_kiara += 1
                show ren flushed with dissolve
                n "Wow, did I really just suggest that? And where did I suddenly get so much confidence from?"
                n "At that, I can feel my entire face flush, and I could barely spare a glance at [ch_ren] to notice that he was sporting a similar demeanour."
                show ren blushing at bpop, center
                r "Y-Your…? Oh! Uhh…"
                y "Sorry! I don't know why I—"
                show ren flushed at spop, center
                r "N-No! I don't mind! It's just… Is that {i}really{/i} okay with you?"
                show ren flushed at spop, center
                r "I don't want to make you uncomfortable by invading your personal space, and I {i}really{/i} don't mind sleeping on the floor."
                y "No, it's fine. I'm the one who asked you to do this favour in the first place, so I owe you."
                jump sleepingbed
            "\"You could sleep on my couch.\"":
                $ affection_conan += 1
                $ affection_violet += 1
                $ affection_elanor += 1
                $ affection_leon += 1
                $ persistent.d1_sleepoutside = True
                show ren flushed with dissolve
                n "…Why didn't I think of that sooner?"
                n "But noooo, I just {b}had{/b} to go and embarrass myself by attempting to blow up an air mattress, only to find out that it had holes in it because of {b}rats{/b}."
                n "I'm going to be known as the rat [baby] now. I'll never be able to show my face—"
                show ren neutral at spop, center
                r "Y-Yeah, the couch is fine. But I really don't mind sleeping on the floor. Honest!"
                n "Oh. He doesn't seem phased about the rats after all."
                y "No, it's okay. I'm the one who asked you to do this favour in the first place, so I owe you."
                jump sleepingfloor
            "\"My hallway has carpet.\"":
                show ren flushed with dissolve
                n "…Seriously?! Why did I say it like that?"
                y "Err— What I mean is… Wouldn't it be comfier if you slept on the carpet instead of wood? Because the hallway outside my bedroom has carpet."
                show ren blushing at spop, center
                r "Well, yeah, but… Is that {i}really{/i} okay with you? I don't want to make you uncomfortable by invading your personal space, and I {i}really{/i} don't mind sleeping on the floor."
                y "No, it's fine. I'm the one who asked you to do this favour in the first place, so I owe you."
                jump sleepingfloor
            "\"Maybe if I stack some blankets on the floor…\"":
                $ ren_decay += 1
                show ren flushed with dissolve
                n "Really, [ch_angel]? Did I seriously just suggest putting some blankets on the {b}floor{/b}? Even after I asked him to come here in the first place?"
                n "I can't believe I was about to take advantage of his kindness like that."
                show ren happy at spop, center
                r "That's fine!"
                y "…It's really not, though."
                show ren neutral at spop, center
                r "But it is. As I said, I don't mind, and I don't want to invade your personal space or make you uncomfortable."
                show ren smirk at spop, center
                r "Besides, won't you feel safer knowing I'll be right outside your door? If anyone {i}does{/i} decide to break in again, they'd have to go through me first."
                y "I guess… but still."
                show ren happy at spop, center
                r "No buts! Now, will this corner suffice?"
                y "You were serious about being put in a corner?!"
                n "It was surprising how he managed to get me laughing again."
                jump sleepingfloor

    label sleepingfloor:
        scene angel_bed_night
        show peffectp
        with GlitchDissolve

        n "After setting up some blankets and extra pillows from my room, I showed [ch_ren] the way to the bathroom in case he needed to go and bid him goodnight."
        n "It was like my feet were on autopilot as I returned to my bedroom."
        n "Silently shutting the door, I awkwardly looked around my room as if {b}I{/b} was the guest in my own house."
        n "It didn't feel awkward per se, but knowing that I had brought home a complete stranger still didn't sit right with me."
        n "But still… [ch_ren] showed no signs of wanting to murder me in my sleep, and [ch_violet] {b}did{/b} meet him before he came inside…"
        n "So maybe this {b}wasn't{/b} so much of a bad idea after all."
        n "I somehow felt {b}safe{/b} in his presence, and even though we had just met, I felt like I could trust [ch_ren] enough to leave him unattended in my lounge room."
        n "With that thought in mind, I slowly slipped underneath the covers of my bedsheets and eventually began to drift off."
        n "…"
        n "So… {i}[ch_ren]{/i}, huh? I wonder what tomorrow will bring."

        jump day1_ending_good

    label sleepingbed:
        scene angel_bed_night
        show peffectp
        with GlitchDissolve

        n "After showing [ch_ren] to the bathroom to freshen up and changing into my own pyjamas in the laundry room, I met him in the middle, and we both made our way to my bedroom."
        n "I didn't bother flicking on the light, knowing fully well that I'd be busy ignoring his presence next to mine by pretending to be asleep. So instead, I awkwardly lead him in before turning to face him in the darkness."
        y "You can just… pick whichever side you prefer."
        show  ren blushing at bpop, center with dissolve
        r "Y-You first…"
        show  ren flushed at spop, center
        r "Oh, but maybe I should be the one closest to the door? J-Just in case…?"
        n "He really didn't need to be so considerate, but nevertheless, I took my side on the left and slowly slipped underneath the sheets."
        n "It must've looked forced, but I awkwardly pat the empty space next to me and shoot [ch_ren] a crooked smile. He slowly makes his way over and joins me underneath the covers—"
        n "And before he could even say anything, I slam down a pillow between us."
        play audio "audio/sfx/item.ogg"
        n "{size=+5}*THUMP*{/size}" with vpunch

        hide ren with dissolve

        y "Just in case I roll over or something! I'm… known to be a cuddler in my sleep."
        r "Oh! Hahaha! That's… That's fine. I'm the same, I think."
        y "You think?"
        r "I mean, no one's told me yet, but… I've woken up to my limbs tangled around my pillow more times than I can count."
        y "…I see."
        r "Y-Yeah…"
        n "Great, now it's awkward again. But being this close to [ch_ren], I could smell his scent once more, and it felt almost… {b}comforting{/b}. I had to fight the urge to roll over onto my side and face him — or rather, the pillow — once more."
        n "The bed dips as [ch_ren] moves around to get comfortable, and I find myself wondering what he might be looking at right now. Was it my ceiling? The pillow between us? Or was he laying on his side and facing the wardrobe?"
        n "{b}Why{/b} was I so concerned in the first place? Sure, I suppose I {b}did{/b} find him rather interesting, but that didn't really explain why I wanted to look at his face one more time."
        n "Did I want to get closer to him? Or was I just curious about what that stranger was currently doing in my bed?"

    
        menu:
            with dissolve
            "Call out to him":
                $ affection_ren += 1
                $ affection_kiara += 1
                y "…[ch_ren]?"
                show ren neutral at spop, center with dissolve
                r "Hm?"
                n "His response is almost immediate, and it felt as though he was waiting with bated breath for me to talk. The bed dips under his weight before his crown of pink hair comes into view, and I silently stare back at him in the dark."
                n "There seemed to be some unspoken tension between us, and I had to fight the urge to act upon it."
            "Say goodnight":
                $ affection_elanor += 1
                $ affection_conan += 1
                $ affection_leon += 1
                n "Maybe it was just me feeling this way? Stifling the urge to reach out to him, I roll onto my side and spare the pink-haired man one last glance."
                label saygoodnight:
                y "Goodnight, [ch_ren]."
                show ren neutral with dissolve
                r "G-Goodnight [ch_angel]. Sweet dreams. I'll… I'll stay up a bit longer just in case anything happens."
                show ren smirk at spop, center
                r "So don't worry about a thing and just get some sleep, okay? No one's gonna break in on my watch."
                show ren neutral at spop, center
                r "…I'll see you in the morning."
                hide ren with dissolve
                if first_kiss == True:
                    n "The fleeting touch of his hand still lingers on my cheek as I find myself drifting off into a blissful sleep."
                else:
                    n "With his protective presence and soft voice still in my mind, I soon found myself drifting off into a blissful sleep."
                jump day1_ending_good
            "[rh_o]Move the pillow[rh_c]":
                $ affection_ren += 1
                $ affection_moth += 1
                $ affection_jae += 1
                $ affection_olivia += 1
                play audio "audio/sfx/fabric.ogg"
                n "Before I can stop myself, my hand reaches out to move the pillow from between us. I was immediately met with soft blue eyes, which I could see widen in surprise even in the darkness of the room."
                show ren flushed at bpop, center with dissolve
                r "…H-Hi."
                y "Hey…"
                n "Talk about awkward."
                n "Without realising it, I discard the pillow somewhere behind me as I continue to stare deeply into [ch_ren]'s eyes. There seemed to be some unspoken tension between us, and I had to fight the urge to act upon it."
            "Don't say anything":
                $ affection_violet += 1
                $ affection_teo += 1
                label saynothing:
                r "Oh…A-Are you going to sleep already?"
                y "…"
                r "S-Sorry. Um… G-Goodnight, [ch_angel]. Sweet dreams. I'll… I'll stay up a bit longer just in case anything happens."
                show ren smirk at spop, center
                r "So don't worry about a thing and just get some sleep, okay? No one's gonna break in on my watch."
                show ren neutral at spop, center
                r "…I'll see you in the morning."
                hide ren with dissolve
                n "With his protective presence and soft voice still in my mind, I soon found myself drifting off into a blissful sleep."
                jump day1_ending_good

        n "What exactly was I feeling? And why did I want to find out?"
        hide ren with dissolve

    
        menu:
            with dissolve
            "[rh_o]Lean over and kiss him[rh_c]":
                $ affection_ren += 1
                $ first_kiss = True
                show ren flushed with dissolve
                n "Before I could think, I find myself leaning over and drawing my face closer to his. [ch_ren] seems to be on the same wavelength as me, as I feel his warm breath fan against my cheeks as his own face draws near to close the distance."
                n "One of my hands shoots out to rest against his chest, and before I could stop myself, I leaned in the rest of the way."
                hide ren
                show other_dark with dissolve
                show peffectp
                n "Almost immediately, I was met with a pair of soft lips and the taste of cherry on my mouth. My eyelids flutter shut at the sensation, and I let [ch_ren]'s overwhelming presence engulf my entire being."
                n "The smell of fresh mint, masculine deodorant, and something that was so wholly '[ch_ren]' flooded my senses, and I felt myself becoming intoxicated by it all."
                n "It was like two pieces of a puzzle slotting together with how perfectly our lips seemed to meld with each other, and I couldn't pull myself away."
                n "One of his hands rises up to cup my cheek, and I find myself keening softly as [ch_ren] tilts his head to deepen the kiss."
                n "He takes my bottom lip into his own and gently bites down before his tongue joins in, curiously prodding against my lips as if to test the waters."
                n "When I meet him halfway with my own, he seems to have {b}finally{/b} found the reassurance he needed before deepening the kiss {b}even more{/b}."
                n "His other hand rests on my waist before gently pulling me closer, clearly not wanting any distance between us."
                n "So [ch_ren] wanted this just as much as I did? I could feel just how eager he was as he kissed me with more desperation and fervour than anything I'd ever experienced in my life."
                n "But we could only go on for so long before one of us needed air, and that someone happened to be me."
                n "When I pull away, [ch_ren] practically {b}whines{/b} at the loss of contact, and I watch with slight amusement as his lips unconsciously follow to seek out mine once more before his eyes flutter open."
                hide other_dark with dissolve
                show ren flushed at spop, center
                n "A beat passes as we just… stare at each other; taking in the moment and to process what had just occurred."
            "Hastily backtrack":
                show ren neutral with dissolve
                y "A-Actually, never mind. Sorry."
                show ren smirk at spop, center
                r "Ah… You don't have to apologise. If anything, {i}I{/i} should be the one apologising to {i}you{/i}…"
                show ren sad at spop, center
                r "I'm sorry if I'm making you uncomfortable. I can… I can still sleep outside if you prefer."
                y "…No, you're fine. {i}really{/i}. A-Anyway… We should get some sleep, yeah?"
                hide ren with dissolve
                n "I turn on my side to face the window, but not before casting a final glance in [ch_ren]'s direction one last time."
                jump saygoodnight
            "Say goodnight":
                show ren flushed with dissolve
                y "Oh, um-! I guess… I just wanted to say g'night, is all."
                show ren neutral at spop, center
                r "Ah! I-I see… G-Goodnight then, [ch_angel]."
                show ren smirk at spop, center
                r "I'll… I'll stay up a bit longer just in case anything happens. So don't worry about a thing and just get some sleep, okay? No one's gonna break in on my watch."
                show ren neutral at spop, center
                r "…I'll see you in the morning."
                hide ren with dissolve
                n "With his protective presence and soft voice still lingering in my mind, I find myself drifting off into a blissful sleep."
                jump day1_ending_good
            "Go to sleep":
                n "Content with seeing his face one last time, I lean back into my pillow and slowly flutter my eyelids shut."
                jump saynothing

        r "…"
        n "His hands are still on me, and it was only then when I noticed that he was tracing faint stars on my cheek with his thumb."
        show  ren smirk at spop, center
        r "…Did that really just happen?"
        n "His voice is soft. So soft that I could barely make out what he was saying. He's staring at me with so much overwhelming {b}adoration{/b} in his eyes that I couldn't help but look away."

        if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True:
            n "…And that was when I saw just how {b}hard{/b} that kiss affected him."
            n "As if noticing what I was staring at, [ch_ren] lets out an awkward sound and shifts so that his lower half is obscured by the blankets once more."
            show  ren blushing at bpop, center
            r "S-Sorry! I- Uhh… You're just really hard to… resist."
            show  ren flushed at bpop, center
            r "N-Not that I'd want to resist you or anything! I just- Well- Umm…!"
            show  ren blushing at spop, center
            r "…I guess what I'm trying to say is that… I… {i}I want you.{/i}"
            n "Taken aback by his sudden boldness, I had to allow myself a moment to collect my thoughts."
            hide ren with dissolve
        else:
            n "…And that was when I saw just how much that kiss affected him."
            n "As if noticing how red his cheeks had gotten, [ch_ren] lets out an awkward sound and timidly turns his face away from mine."
            show  ren blushing at bpop, center
            r "S-Sorry, [ch_angel]! I- Uhh… It's just that… Kissing you felt really nice. I-I didn't want to stop."
            show  ren flushed at bpop, center
            r "N-Not that I would've {i}kept going{/i} if you told me to stop! I just- Well- Umm…!"
            show  ren blushing at spop, center
            r "…I guess what I'm trying to say is that… I… I'd really like to kiss you again. If you want to."
            n "Taken aback by his sudden boldness, I had to allow myself a moment to collect my thoughts."

        $ choice_style = "box"
        menu:
            with dissolve
            "{image=14NWY symbol alt} \"I want you too.\"" if dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou == True and persistent.streamermode == False:
                show ren flushed at bpop, center
                r "Y-You do?"
                show ren blushing at spop, center
                r "Th-Then…"
                show ren neutral at spop, center
                r "Then… tell me clearly what you want from me."
                $ choice_style = "default"
                jump day1_wahooscene
            "[rh_o]\"Sorry, what was that?\"[rh_c]" if dlc_14nightswithyou_scenes == False or persistent.dlc_14nightswithyou == False or persistent.streamermode == True:
                $ affection_ren += 1
                show ren flushed at spop, center
                r "Oh! U-Umm… Nothing! Forget I said anything!"
                show ren blushing at spop, center
                r "Sorry, you probably want to sleep now, right?"
                show ren blushing at spop, center
                r "I'll let you… I'll let you do that."
                show ren flushed at spop, center
                r "Goodnight, [ch_angel]!"
                hide ren with dissolve
                n "Giving him a weak reply (could he even hear me?), I awkwardly turn over onto my side and settle back into bed. As [ch_ren] does the same, I feel the mattress shift once more, and a heavy silence lingers in the air."
                n "Maybe he fell asleep already? Deciding to push my luck and break the silence once more, I whisper to [ch_ren] one final time."
                $ choice_style = "default"
                jump saygoodnight
            "\"Maybe we should go to bed now.\"":
                $ affection_violet += 1
                label nowahoo:
                show ren flushed at spop, center
                r "Oh! Ah- Y-Yeah, okay."
                show ren blushing at spop, center
                r "Sorry, I hope I didn't make things awkward?"
                y "Not at all. It's just… We don't really know each other that well yet."
                show ren flushed at spop, center
                r "…I see. Y-Yeah, that makes sense."
                y "But… we could get to know each other in the morning? Maybe over breakfast?"
                show ren happy at spop, center
                r "Y-Yeah, I'd like that."
                hide ren with dissolve
                n "Giving him a faint nod (could he even see it in the dark?), I awkwardly turn over onto my side and settle back into bed. As [ch_ren] does the same, I feel the mattress shift once more, and a heavy silence lingers in the air."
                n "Maybe he fell asleep already? Deciding to push my luck and break the silence once more, I whisper to [ch_ren] one final time."
                $ choice_style = "default"
                jump saygoodnight

################################################################################
## DIDN'T INVITE REN
################################################################################
label day1_rejectren:
    scene angel_bedroom_night
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    stop ambience fadeout 2.0
    show peffectp
    with Fade(1.0, 1.0, 1.0)

    $ location_elanor = "home"
    $ location_conan = "home"
    $ location_ren = "home"
    $ location_jae = "home"
    $ location_leon = "home"

    n "Back at home, the sounds of my microwave meal and the television filled the silence as I told [ch_moth] about my day."

    label mothaltintro:
        play audio "audio/sfx/item.ogg"
        show mothphone bg at vcpos with easeinright
        n "Like always, their webcam is pointed towards the ceiling with only half of their face in the frame. But I knew it was probably because they hadn't cleaned their room in a while."
        n "At that thought, I glance towards the growing pile of laundry in my basket and make a mental note to take care of it on my next day off."
        n "But now that I was looking at it…"

        if persistent.streamermode == True:
            n "When did I leave it looking so messy…? And since when did I leave last week's load on top?"
        else:
            n "When did I leave it looking so messy…? And since when did I leave my underwear exposed?"
        show mothphone bg at spop
        mcall "Helloooooo? Earth to [ch_angel]? You good?"
        y "…Hm? Sorry, what were you talking about?"
        show mothphone bg at spop
        mcall "I was asking you about that dude from earlier. Like, I seriously can't believe he gave you his number."
        y "Yeah… I'm surprised too."
        show mothphone bg at spop
        mcall "Yeah, no kidding! My guy {i}literally{/i} couldn't even stutter out a complete sentence, yet he was able to shoot his shot like that?"

        show mothphone bg at spop
        if persistent.streamermode == True:
            mcall "…Wow, maybe his… {i}y'know{/i} really is big."
            y "Jeez [ch_moth]!"
        else:
            mcall "…damn, maybe his dick really is big."
            y "M-M-[ch_moth]!"

        show mothphone bg at spop
        mcall "Whaaat? I'm just saying! But you'll let me know, right? If it really is big?"
        y "I'm hanging up on you."

        if d1_inviteren == True:
            jump mothaltending

        show mothphone bg at spop
        mcall "Haha! Okay, okay! I'm just kidding! But for real though, did you text him back yet?"
        y "…Err, no. I thought you were supposed to make them wait a day or something? I don't want to seem too eager."
        show mothphone bg at spop
        mcall "So you're saying you're eager?"

        show mothphone bg at bpop
        mcall "*ahem*… {size=+5}Attention everyone! [they!c] [are] eager as hell!{/size}" with vpunch

        show mothphone bg at bpop
        mcall "{size=+10}And for a guy who doesn't even know how to grow a backbone!{/size}" with vpunch
        y "Ugh, I'm not saying {i}anything!{/i} But your neighbours will if you keep shouting like that!"
        show mothphone bg at spop
        mcall "Yeah, yeah. Okay. Look! If it were me, I'd text him back as soon as possible. Maybe even give him a call instead if his voice was as {i}\"submissive and breedable\"{/i} as you said it was."
        y "I literally never said that?!"
        show mothphone bg at spop
        mcall "If that's what you wanna believe!"
        n "[dammit!c], their laughter was contagious."
        show mothphone bg at spop
        mcall "Why are you still talking to me anyway? Go call up your precious little Haruko 2.0. I got some webcomics I need to catch up on anyway."
        y "Oh, speaking of webcomics; did you read the latest chapter for Always Wi—"
        show mothphone error at spop
        mcall "Alright, I'm hanging up now. Cya [ch_angel]!"
        hide mothphone with easeoutright
        n "With a sigh, I watch the green call button turn red. [ch_moth] had always been terrible towards my impulse control, but I adored them either way."

        scene angel_bed_night 
        show peffectp
        with GlitchDissolve

        n "Spinning around in my chair, I glance over at my phone charging on the nightstand and decide to listen to [ch_moth]'s words after all."
        n "Plopping onto my bed, I scoop my phone up and unlock it. I navigate the messages app easily and open up a new contact to enter [ch_ren]'s details."
        n "Moments seem to pass as I blankly stare at his number on the screen, and before I could let myself stall any longer, I finally decide on what I should do."

    
        menu:
            with dissolve
            "Send him a text":
                $ affection_moth += 1
                $ affection_conan += 1
                $ affection_teo += 1
                $ affection_kiara += 1
                $ affection_olivia += 1
                n "So what if it was almost eleven at night? Before I can give myself time to rethink, I shoot [ch_ren] a short text explaining who this was and ask if he enjoyed his book."
                y "There, that should do it."
                jump day1_textren
            "Call him instead":
                $ affection_ren += 1
                $ affection_moth += 1
                $ affection_violet += 1
                $ affection_elanor += 1
                $ affection_jae += 1
                $ affection_leon += 1
                n "Deciding to give [ch_ren] a call instead, I tap on his contact info and press the green button without a second thought."
                n "Silently hoping that he'd still be awake at this time, I bring my phone closer to my ear and listen to the dial tone."
                jump day1_callren
            "[de_o]Wait until tomorrow[de_c]":
                n "Putting my phone down, I decided to stick to what I know best and just text him in the morning instead. "
                jump day1_deadendstart
            "[de_o]Block his number[de_c]":
                $ persistent.d1_blocknumber = True
                n "Still sitting in the contacts app, my finger hovers over the block button before I finally decide to press it."
                n "While [ch_ren] ultimately seemed harmless, his odd and timid behaviour rubbed me off the wrong way."
                n "Plus, I wasn't entirely convinced that he {b}wasn't{/b} the same person [ch_violet] saw last night. Sure, their appearances didn't match up at all, but it never hurt to be cautious."
                jump day1_deadendstart

        label mothaltending:
            show mothphone bg at spop
        mcall "Okay, okaaaaay I'm sorry! But still… You don't think he was some creep or something? I mean, who just… {i}agrees{/i} to go to some strangers house?"
        n "Thankfully, [ch_moth] had the decency to {b}not{/b} comment on me impulsively inviting [ch_ren] over in the first place."
        y "You think? Vi had some suspicions about him as well."
        show mothphone bg at spop
        mcall "Yeah? That's real sus. And you said he had pink hair like Haruko? That's like… Anime rule number one."
        show mothphone bg at bpop
        mcall "Never trust a guy with pink hair!"
        show mothphone error at spop
        show gwitch
        mcall "{glitch=1.0}I'm sure there's something real fuck{i}ed \ \ \ \ \ \ \ \ \ \ \ \ u{/i}{/glitch}{glitch=60.0}{i}p\n \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ abo\ \ \ \ \ ut hi\ \ m…{/i}{/glitch}"
        hide gwitch with dissolve
        y "…Hello? [ch_moth]? You're breaking up."
        y "[ch_moth]?"
        play audio "audio/sfx/item.ogg"
        hide mothphone with easeoutright
        n "I watch as the green call button suddenly turns red, and wonder if their wi-fi got cut off again. Or maybe one of their siblings were streaming a movie?"
        n "Oh well. I can always ring them back in the morning. It's not like I had anything really important to tell them."

        jump day1_deadendstart

################################################################################
## TEXT REN
################################################################################
label day1_textren:
    play audio "audio/sfx/footsteps.ogg" volume 1.5

    n "The response is almost immediate as my phone screen lights up in my hand, and I quickly open up my message app again to check."
    rt "hiii [ch_angel]! yes i'm reading thru it rn. so far it's rlly good! exactly what i was expecting ^^"
    n "Gah, even the way he typed seemed adorable."
    rt "hope this isn't weird or anything, but i was kinda hoping you'd text back >.< and i'm glad u did! so… thank u!"

    menu:
        #with dissolve
        "\"That is kinda weird, ngl\"":
            $ affection_ren -= 1
            $ affection_violet += 1
            $ ren_decay += 1
            rt "ah it is? sorry! i didn't mean to make u uncomfortable! u can just… delete my number if u'd like"
            rt "actually before u do… i was wonderinf if u were free tomorrow? i still wanted to thank u for helping me find that book"
        "\"Yeah np! Thanks for leaving your number!\"":
            $ affection_ren += 1
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            rt "oh!! yeah no worries!"
            n "He seems to take his time with the next response, judging from how the grey typing bubble flashes on the bottom of the screen."
            rt "i'm glad u didn't throw it away >.<"
            rt "actually… i was wonderinf if u were free tomorrow? i still wanted to thank u for helping me find that book"
        "\"Wait! Look at this meme I found real quick\"":
            $ affection_moth += 1
            $ affection_jae += 1
            $ affection_olivia += 1
            n "Without thinking, I send [ch_ren] one of the memes I had recently saved to my camera roll."
            n "And it barely takes him 10 seconds to reply, sending back a laughing Haruko sticker and a heart."
            y "Oh? {i}He{/i} knows about Attack on Giant?"
            n "Before I know it, my phone is buzzing in my hands once more."
            rt "hehe >w< that's v funny!"
            rt "can i save it??"
            rt "i saved it lol"
            rt "btw i was wonderinf if u were free tomorrow? i still wanted to thank u for helping me find that book"
        "Don't say anything":
            $ affection_ren -= 1
            $ affection_teo += 1
            $ ren_decay += 1
            n "I place my phone back on the nightstand and start getting myself comfortable in bed—"
            extend " before it goes off again {b}just{/b} as I slip under the covers."
            n "Groaning, I pick up my phone once more."
            rt "did u fall asleep alrdy? i guess it is pretty late"
            rt "actually… i was wonderinf if u were free tomorrow? i still wanted to thank u for helping me find that book"
        "{image=14NWY symbol} \"what are you wearing rn? ;)\"" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
            call DLC_day1_text from _call_DLC_day1_text

    n "Wow, was he serious?"

    menu:
        "\"What do you mean?\"":
            $ affection_violet += 1
            $ affection_conan += 1
            $ affection_leon += 1
            $ affection_teo += 1
            $ affection_kiara += 1
            n "He seems undecided on what to say as the grey typing bubble keeps flashing on the screen. What seems like minutes pass before he finally settles on a response."
            rt "um!! like… a date >///< if that's ok with u!"
        "\"Like a date?\"":
            $ affection_ren += 1
            $ affection_elanor += 1
            n "He seems undecided on what to say as the grey typing bubble keeps flashing on the screen. What seems like minutes pass before he finally settles on a response."
            rt "um yeah! like a date!! >///< if that's ok with u!"
        "Send him an obscure meme":
            $ affection_moth += 1
            $ affection_jae += 1
            $ affection_olivia += 1
            n "[ch_ren], you poor, ignorant fool. You fell right into my trap."
            n "Opening up my camera roll, I send him a blurry picture of a horse staring out at the ocean."
            rt "ohhhh? what is that? hahaha :3"
            rt "where do u find these memes lol"
            rt "anyway! were u free tomorrow?"
        "[de_o]Don't reply to him[de_c]":
            n "Man, he really was persistent."
            rt "[ch_angel]? are u still there??"
            n "Yeah, no. I wasn't going to respond to him after all."
            n "Minutes seem to pass as I blankly stare at my phone to watch his pitiful attempts at getting me to respond."
            rt "i can tell ur not sleeping, but… i can take a hint."
            rt "Sorry for bothering you. You can delete my number now if you'd like."
            rt "Goodnight, [ch_angel]. And make sure you close your window before you go to sleep. You wouldn't want anyone breaking in again, right? :)"
            n "…What? How did he know it was open? Or maybe it was just common for people to not close their windows at night? Well, whatever. I wasn't about to ask him anyway."
            jump day1_deadendstart

    rt "i can pick u up at ur place tomorrow and we can go visit the pier or something? hehe :D"
    rt "only if ur interested ofc!! we can just do whatever u want instead if u prefer ^^ i dont mind!!"
    n "So he wanted to go on a date? Well… It wasn't like I had anything planned for tomorrow; it was my day off, after all. Maybe it wouldn't be so bad?"
    n "Besides, I can't even remember the last time I went out with someone — let alone a date."
    n "Yeah, maybe going on a date with him wouldn't be such a bad idea. Besides, [ch_ren] didn't seem {b}that bad{/b} of a guy. I could even use this as an opportunity to get to know him better. He certainly seemed interesting."
    n "With that thought in mind, I quickly texted him back with my address and preferred time. Hardly a moment passes before I get a response."
    rt "ok sweet!! i'll pick u up @ around 11am then! aaaaa i can't wait!"
    rt "o!! i just saw the time >_< it's getting pretty late now huh? i should let u get some sleep"
    rt "sorry for keeping you up so late [ch_angel]!!"
    rt "goodnight! and thnx again for all ur help!! <3"
    n "After sending him a goodnight text of my own, I place my phone down and crawl into bed. Well… today definitely didn't turn out the way I was expecting it to, but… At least I scored a date with a cute guy!"
    n "With his sweet words in mind, I began to drift off."
    n "So… {i}[ch_ren]{/i}, huh? I wonder what tomorrow will bring."

    jump day1_ending_good

################################################################################
## CALL REN
################################################################################
label day1_callren:
    play audio "audio/sfx/footsteps.ogg" volume 1.5

    n "*ring*… *ring*… *ring*…"
    n "It barely rings three times before he picks up, and he seems almost… flustered and out of breath."
    rcall "H-Hello? This… This is [ch_angel], right?"

    menu:
        "\"It is! Thanks for leaving your number\"":
            $ affection_ren += 1
            $ affection_elanor += 1
            $ affection_jae += 1
            $ affection_kiara += 1
            $ affection_olivia += 1
            rcall "O-Oh, yeah! No worries, hahaha! Thanks for… uh, thanks for calling! Wow… your voice sounds just as lovely on the phone."
            y "Oh, uh… Thank you?"
            rcall "Wait, no, that's not what I—… I-I didn't mean to— …Sorry, I wasn't thinking when I said that."
        "\"It is, but… How did you know?\"":
            $ affection_violet += 1
            $ affection_leon += 1
            rcall "Ah-! I mean, I wasn't really expecting anyone to ring, so I kind of just… assumed."
            extend " Not that many people ring me anyway, haha."
            rcall "…Sorry, did I make it weird?"
        "\"Sorry, I know it's late.\"":
            $ affection_conan += 1
            $ affection_moth += 1
            rcall "No! I-It's fine! I'm normally still awake at this time anyway. I usually like to watch some things before I fall asleep."
            rcall "Sometimes it keeps me up until the morning, but I don't really mind. I feel at ease when I get to look at y—"
            extend " {b}{i}stuff.{/i}{/b}"
            y "Oh, really? Like… movies or something? What do you normally like to watch? Maybe I've seen it!"
            rcall "…Movies? Why would I— {b}OH.{/b} Y-Yeah! It's some niche film you might not have heard about… M-Maybe we could watch it together sometime."
            rcall "Sorry, I made it awkward again, didn't I?"
        "\"…\"":
            $ affection_teo += 1
            $ ren_decay += 1
            rcall "…Hello? Are you there? I-I don't think I can hear you…"
            rcall "Did you meant to call me? …Hello?"
            y "…"
            rcall "Hellooooooooo! Are you there?"
            n "Deciding to put him out of his misery, I finally speak up."
            y "Hey [ch_ren]…"
            rcall "Oh, [ch_angel]! S-Sorry! I couldn't hear you earlier. I guess there must be something wrong with my phone, aha."
            rcall "Sorry… {i}Again{/i}."
        "{image=14NWY symbol} \"…What are you wearing?\"" if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
            call DLC_day1_call from _call_DLC_day1_call

    y "It's okay, don't worry about it. "
    n "He's really been apologising a lot today — I almost feel bad for him."
    rcall "Actually… I'm surprised you called. I honestly expected you to throw away my note, to be honest."
    rcall "I hope you didn't find it creepy or anything. Your… {i}workmate{/i} seemed like the type to tease you if I handed it to her instead, so I figured that leaving it on your desktop would've been the wiser choice."
    rcall "But then I was worried she might come back and find it before you did, so I considered putting it in your bag instead. But then I thought—"
    rcall "I guess I'm rambling now, aren't I? Sorry!"
    rcall "A-Anyway, I also wanted to know if… Well— If you were free tomorrow? I still wanted to thank you for helping me find that book."
    n "…Oh? Was he asking me out on a date? Or was I reading too deep into his words? He must've taken my silence as confusion, however, as he immediately begins to backtrack on his words."
    rcall "I-I guess I'm asking you out on a date, haha! We could… We could go visit the pier, or the beach, or this café I know… Honestly, we could do whatever you'd like! I don't mind at all."
    y "Well…"
    n "So he wanted to go on a date? Well… It wasn't like I had anything planned for tomorrow; it was my day off, after all. Maybe it wouldn't be so bad?"
    n "Besides, I can't even remember the last time I went out with someone — let alone a date."
    n "Yeah, maybe going on a date with him wouldn't be such a bad idea. Besides, [ch_ren] didn't seem {b}that bad{/b} of a guy. I could even use this as an opportunity to get to know him better. He certainly seemed interesting."
    y "Sure, why not? It sounds like it'd be fun. And I haven't visited the pier in a while."
    rcall "Y-You really want to go on a date?!"
    rcall "I-I mean, yeah! Cool! …Would it be alright if I pick you up around eleven, then?"
    y "Yeah, sure."
    n "Wow, he really seemed eager. I hope I didn't make the wrong choice by agreeing to this."
    rcall "A-Alright then, yeah! Great!"
    n "He was perhaps a bit {b}too{/b} eager."
    rcall "…A-Anyway, it's getting late now, isn't it? I'm sure I've already taken up too much of your time. I'll… I'll let you go to sleep, then."

    menu:
        "\"But I wanted to talk with you more…\"":
            $ affection_ren += 1
            $ affection_elanor += 1
            $ affection_olivia += 1
            rcall "{size=+10}A-A-Ah! Really?!{/size}" with vpunch
            extend " Me… Me too! But… you need to sleep, don't you? I won't be greedy. Can I… {i}err,{/i} would it be okay if I called you tomorrow?"
            y "Sure, we can talk more about our date then."
            rcall "O-Okay, yeah! Sweet! I mean—"
            rcall "Ugh, I'll just… I'll let you go to sleep before I embarrass myself {i}further{/i}."
            rcall "Goodnight [ch_angel]. Sweet dreams."
        "\"Can we talk again tomorrow?\"":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_jae += 1
            n "The sound of a muffled squeak erupts from his end before [ch_ren] clears his throat once more."
            rcall "{size=+10}Y-Yes please!{/size}" with vpunch
            rcall "I mean, now that I have your number as well, would it be okay if I called {i}you{/i}?"
            y "Sure, we can talk more about our date then."
            rcall "I'd love that… Wait, no— I mean—"
            rcall "Ugh, I'll just… I'll let you go to sleep before I embarrass myself {i}further{/i}."
            rcall "Goodnight [ch_angel]. Sweet dreams."
        "\"Okay then, goodnight.\"":
            $ affection_violet += 1
            $ affection_conan += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            $ affection_teo += 1
            rcall "G-Goodnight!"
            n "He sounds almost {i}chipper{/i} at the sound of my voice, but I decide against questioning it. He really was a rather eccentric person."
            rcall "…Can I… Can I still call you tomorrow, [ch_angel]? Or— No, never mind! Goodnight!"
            n "He hangs up before I can even respond."
        "[de_o]Blatantly ignore him[de_c]":
            $ ren_decay += 1
            n "Deciding not to respond, I keep my mouth shut and listen to [ch_ren] awkwardly fumble on the other side of the line."
            rcall "…Angel? Are you still there?"
            rcall "Ah— Don't tell my my phone isn't working again… Here, why don't I try calling you back and—"
            n "Before [ch_ren] could finish his sentence, I impulsively hang up the phone with a sigh."
            y "You sure like to talk a lot, huh?"
            jump day1_deadendstart

    n "Placing my phone on the nightstand, I begin to slip into my bed and pull the covers over my body."
    n "A beat passes before [ch_ren]'s soft, breathy voice enters my mind, and I slowly find myself getting lulled to sleep with it."
    n "So… {i}[ch_ren]{/i}, huh? I wonder what you have planned for us tomorrow."

    jump day1_ending_good

################################################################################
## UHH OHHHH
################################################################################
label day1_deadendstart:
    scene other_dark
    play music "audio/bgm/Notice Me.ogg" fadein 1 fadeout 1
    with GlitchDissolve

    n "I climb into bed with the thought of the supposed intruder still heavy on my mind, but I eventually put it to rest by remembering the heavy duty lock I bought and installed earlier."
    n "There's no way anyone could break in now, and even if they did, I could rely on my neighbour to hear."
    n "Often, I'd hear [ch_violet] gaming away on her computer until the early hours of the morning, so I felt safe knowing that she'd be around if something went wrong. "
    n "…"
    n "…Even if I couldn't hear her right now."
    n "…"
    y "Oh well. I'm sure everyone takes gaming breaks every so often."
    n "Snuggling deeper into the warmth of my blankets, my eyes began to feel heavy as I slowly lulled myself into dreamland."
    
    play audio "audio/sfx/static.ogg"
    stop music fadeout 1

    n "Because of this, I miss\ \ \ {color=#a30b11}{size=-6}01100001{/size}{/color}\ \ \ \ \ {color=#a30b11}{size=-6}01101110{/size}{/color}\ \ \ \ \ the sounds of foot\ \ \ \ \ {color=#a30b11}{size=-6}01100111{/size}{/color}\ \ \ steps creeping\ \ \ \ \ \ \ {color=#a30b11}{size=-6}01100101{/size}{/color} \ \ \ \ \ down the hall\ \ \ \ \ \ \ \ \ \ \ \ {color=#a30b11}{size=-6}01101100{/size}{/color}\ \ way {color=#a30b11}\ \ \ .\ \ \ \ \ \ \ \ \ \ \ .\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ .{/color}"

    jump day1_deadend

################################################################################
## EEUUUGHGHGUEGHEUSGH
################################################################################
label day1_ending_good:
    $ ending_good = "obtained"
    $ persistent.d1_ending_gooding = True
    jump pathpoint

label day1_deadend:
    $ persistent.deadendings += 1
    $ persistent.deadend1 = True
    $ persistent.d1_badending = True
    jump pathpoint