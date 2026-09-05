################################################################################
## DAY 2 HEHEHEHEHEHE
################################################################################
label day2:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Currently playing Day 2',
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
    $ calendar_day = "02"
    $ skipday = "day3"
    
    $ update_elanor = "Haha, I'm not me without my coffee! :P"
    $ update_conan = "Is anyone missing a wallet? Come find me @ CBL reception."
    $ update_violet = "No, violets are NOT blue :o"
    $ update_moth = "NEW AOG EPISODE JUST DROPPED!!!!!! DON'T TALK TO ME RN"
    
    $ location_elanor = "library"
    $ location_conan = "library"

    if d1_wahooren == True:
        $ ren_outfit = "nakey"
        jump day2_wahoomorning
    elif d1_sharebed == True and d1_wahooren == False:
        jump day2_sharedmorning
    elif d1_sharebed == False and d1_inviteren == True:
        jump day2_neutralmorning
    elif d1_inviteren == False:
        jump day2_alonemorning
    else:
        jump day2_alonemorning

################################################################################
## DID MORE THAN SHARE A BED LMAO
################################################################################
label day2_wahoomorning:
    scene angel_bed_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    show peffect
    with fade

    n "The sounds of birds chirping outside pull me from my slumber, as streaks of sunlight peak through the blinds of my window and cast a warm glow across my skin."
    n "I wanted nothing more than to reach out and close the blinds, but something — or rather, someone — seemed to be stopping me."
    show ren smirk z with dissolve
    n "A familiar pair of white sleeves are wrapped securely around my waist, so I turn around, only to find [ch_ren] staring intently at me from his side of the bed."
    n "Oh. Right. I forgot that we…"
    n "Heat rises to my cheeks as the memories from last night come rushing back, and I sheepishly try to hide my reddening face in the pillows."
    n "But [ch_ren] only seems to find amusement in my state of embarrassment with how his eyes crinkle while he lightly chuckles underneath the morning light."
    n "He looked far too pretty in the sunlight for a man who'd surely woken up no more than five minutes ago, and I had to fight the urge to take a picture of him to commit the scene to memory."
    n "Ugh. On second thought, that would've been far too creepy…"
    n "But I couldn't help myself from stealing one more peek at his soft demeanour before covering my face again."
    n "And without warning, [ch_ren] pulls me closer before he nuzzles his head into the crook of my neck and inhales deeply."
    n "His sudden act of affection startled me, to say the least, and despite the events that unfolded last night, he seemed {b}far too{/b} comfortable to be acting this familiar and cuddly with me."
    n "How was he acting so carefree after what we had done? It was like he thought that waking up to each other like this was completely normal to him."
    show ren neutral z at spop, center
    r "Mornin'…"
    n "Admittedly, his sleepy voice sounded rather pleasant when he spoke it so close to my ear — but I had other, more pressing issues to concern myself over."
    n "I just… didn't know how to casually broach the topic with him yet."
    n "[ch_ren], however, doesn't seem to {b}want{/b} to acknowledge the heavy air between us, and instead feels more than content with snuggling up to me and tickling my neck with his breath."
    n "So, to try and put some distance between us, I push against his chest and attempt to strike up a conversation."
    y "Good morning, sleepyhead. How long have you been awake?"
    show ren smirk z at spop, center
    r "Long enough to find out that you drool in your sleep."
    y "…"
    y "I do?!"
    show ren happy z at spop, center
    r "Nah, I'm just kiddin'."
    n "His laughter ghosts across my cheek as he nuzzles his face into my neck once more, and his hands glide across my back to draw me impossibly close to his body."
    n "Close enough until both of our bodies are pressed against each other, and I could feel the all-too-familiar warmth radiating from his skin. The sensation sends a shiver up my spine, and I only hope [ch_ren] didn't notice it."
    y "Um… Are you hungry? I can make us breakfast if you want."
    show ren neutral z at spop, center
    r "…Mm. Can't we stay here instead?"
    y "As much as I'd love to sleep in, I don't want to waste the day."
    show ren smirk z at spop, center
    r "…But I do. And y'very warm."
    y "And you're getting a bit {i}too{/i} clingy."
    n "While I meant it light-heartedly, I don't think [ch_ren] took it the same way, judging from the low whine that emits from the back of his throat and the deep sigh he releases into my skin."
    n "It takes him a moment before he finally detaches himself from me, and even from my spot on the bed, I could see the soft pout he was sporting."
    show ren sad with dissolve
    n "And without a care in the world, [ch_ren] sits up from his side on the bed and lets out a lengthy, drawn-out yawn — not acknowledging the blanket falling from his body and exposing his lower half to my eyes."
    n "Almost sheepishly, I avert my gaze and wait until he was done."
    show ren neutral at spop, center
    r "Y'know… We could go to that café near the pier for breakfast. The one that recently opened up?"
    y "You mean the Driftwood Café? I didn't know it was open to the public yet."
    show ren smirk at spop, center
    r "If y'want, we could go have a look."
    show ren blushing at spop, center
    extend " …Like a date?"
    show ren smirk at spop, center
    r "B-B-Besides, you said it yourself that you didn't want to waste the day."
    show ren happy at bpop, center
    r "Besides, what better way to start it than by going on a {i}niiice{/i} morning walk!"
    n "He sends me a cheeky smile, but I can tell by his sarcastic tone that the last thing he wants to do is to get out of bed."
    n "But seeing him act so casual and lively… It makes me wonder what had happened to his shy persona from yesterday."
    n "Was he more comfortable around me now? I certainly would assume so after how… {b}intimate{/b} we got last night. Of course, I still needed to talk to him about that, but [ch_ren] seemed almost adamant about avoiding the topic altogether."
    n "Well. I suppose we'll cross that bridge when we get there. The thought of good food was much more tempting."
    show ren flushed at spop, center
    r "Uh— W-Wait, where did I…?"
    n "Glancing over at [ch_ren] once more, I notice how he almost seems flustered as he looks around the room before lifting up the sheets and the pillows around him."
    n "He sends me a sheepish smile when our eye briefly meets before he goes back to searching for… whatever it was he was looking for on the floor."
    n "And I almost get rolled over when he tries to hoist the blanket around his waist and rise from the bed."
    show ren blushing at spop, center
    r "I-I don't suppose… Do you know where my pants are?"
    play audio "audio/sfx/item.ogg"
    n "Rolling my eyes, I toss him a pillow to cover up with before groaning into my arm."

    jump day2_pierdate

################################################################################
## SHARED A BED MORNING
################################################################################
label day2_sharedmorning:
    scene angel_bedroom_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 1.0, 1.0)

    n "The sounds of birds chirping happily outside pull me from my slumber, as the streaks of sunlight peak through the blinds of my window and cast a warm glow across my skin."
    n "Groggily, I turn on my side and smush my head into the pillow to block out the light — only to hear the faint sounds of tapping to my left."
    n "Cracking one eye open, I was surprised by the scene in front of me."
    n "[ch_ren] was already awake, perched up against the headboard as he idly scrolled through his phone."
    n "It seems he was waiting for me to wake up, judging by how he immediately puts his phone down as soon as we make eye contact and sends me a soft smile."
    n "Almost sheepishly, I shoot him an awkward smile of my own before covering my face with a pillow once more."
    n "Had [ch_ren] been watching me sleep? I hope I wasn't drooling."
    show ren neutral z at spop, center with dissolve
    r "Mornin', Angel."
    n "His voice pulls me from my thoughts, and I couldn't help but notice just how {b}attractive{/b} he sounded in the morning."
    n "His gruff, sleepy tone was rather pleasant to hear, and I found myself wanting to continue the conversation."
    n "Lifting my head from the safety of my pillow, I was greeted with [ch_ren]'s soft demeanour once more."
    y "I'd appreciate it if you weren't so chipper this early in the morning."
    show ren smirk z at spop, center
    r "You'd be this chipper too if you realised that you {i}weren't{/i} murdered in your sleep last night."
    show ren neutral z at spop, center
    r "Which can only mean one thing…"
    show ren happy z at spop, center
    extend " That creepy guy didn't come back to your apartment last night!"
    n "He seems almost smug as he leans closer to me, and it was then when I realised {b}just{/b} how pretty he looked underneath the morning light coming from my window."
    n "It wasn't fair that he got to look so ethereal and glowing this early in the day, and I wasn't sure if I wanted to praise his looks or throw a pillow at his head."
    n "[ch_ren] doesn't seem to pick up on my speechless nature though, as he continues to beam down at me with such a soft look."
    n "And I found myself wanting to look away in fear of making things even more awkward."
    show ren smirk z at spop, center
    r "I guess I did a good job, huh?"
    n "He's a bit {b}too{/b} smug."
    show ren neutral z at bpop, center
    r "If you ever need my services again, I'd be more than happy to oblige. F-For free, of course!"
    y "…You're really talkative in the mornings, aren't you?"
    show ren happy z at spop, center
    r "I can't help it. I got t'wake up next to a {i}real{/i} cutie this morning."
    y "Oh— Uhh…"
    n "As if noticing how close he was to me — or maybe realising that he dropped his usual stutter — [ch_ren] immediately pulls back and turns his head away."
    show ren flushed z at spop, center
    r "A-A-Anyway! Now that you're awake… Did you… Would you like to go out for breakfast? I think that café near the pier is open now."
    show ren happy z at spop, center
    r "We could go check it out… Like a date…? B-B-But only if you want to!"
    n "Why did he suddenly switch again? I figured we'd at least be a tiny bit closer, especially considering that we shared a bed, but… Maybe I was wrong?"
    y "You mean the Driftwood Café? I didn't even know it was open to the public yet."
    show ren smirk z at spop, center
    r "Really? Well, what better way to find out than by… {i}finding out{/i}, I guess? Heh."
    n "I roll my eyes at his lame attempt at a joke before groaning into my pillow."
    n "Did he seriously want to go out for breakfast {b}this{/b} early in the morning? Man, he was seriously a trooper."
    n "With a sigh, I reluctantly sit up and stretch my limbs. From that action alone, it was like I could feel [ch_ren]'s eyes on me…"
    show ren blushing z at center
    n "But as soon as I turned my head, he was already staring holes into the blanket with a blush on his cheeks."
    n "Shaking my head to dismiss those thoughts, I let all of my joints pop before breaking the silence once more."
    y "So… Driftwood Café?"

    jump day2_pierdate

################################################################################
## NEUTRAL MORNING YAHOOOOOOO
################################################################################
label day2_neutralmorning:
    scene angel_bedroom_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 1.0, 1.0)

    n "Waking up to the sounds of birds chirping outside and the sunlight filtering through my blinds, I groggily rub my eyes before absent-mindedly staring at the ceiling for a few moments."
    n "A lot had occurred last night, and I still needed to process most of it."
    n "But the main thing that plagued my mind was the stranger I let into my apartment last night. Was he still here?"
    n "Slipping out of bed, I smooth out the wrinkles in my pyjamas to make myself look presentable before heading out into the hallway."

    scene angel_lounge_day
    show peffect
    with dissolve

    n "I don't have to make it that far before I catch the familiar glimpse of pink in my vision, and I walk out to see [ch_ren] already awake and neatly stacking his pillows and blanket away."
    show ren neutral at spop, center with dissolve
    r "M-Morning, Angel! Sleep well? I don't think anyone came by last night, but…"
    y "…But?"
    show ren sad at spop, center
    r "Your neighbour… She's kind of loud, isn't she?"
    n "Ah. [ch_ren] must've heard her gaming away on her computer at 2am, like usual."
    n "As if to apologise on her behalf, I offer [ch_ren] a sympathetic smile before coming to help him move the pillows back into their rightful spot."
    y "Yeah… Sorry about that. I usually don't mind since I'm also awake at that time, but… I forgot that you'd be able to hear [ch_violet] from here as well."
    show ren happy at bpop, center
    r "O-Oh! It's no trouble! I just… It was odd to hear at first. She doesn't really give off that vibe, you know?"
    y "Yeah, I get what you're saying. She isn't really the type to—"
    show ren blushing at bpop, center
    r "*GROWL*" with vpunch
    n "Apparently, [ch_ren]'s stomach wanted to join in the conversation."
    n "Sheepishly, he covers his mouth with the sleeve of his sweater and turns away."
    n "But… Now that I was up close, I could make out the faint, dark circles under his eyes and immediately started to feel bad."
    n "So he was hungry {b}and{/b} he didn't get much sleep last night? I must've been a terrible host."
    n "I had to make up for this somehow."
    show ren flushed at spop, center
    r "S-Sorry! I don't know why it made that noise— I'm not hungry or anything…!"
    y "Here, why don't I make us something to eat?"
    show ren blushing at spop, center
    r "Oh! It's okay! Don't worry about it! I wouldn't want to be a bother, anyway…"
    show ren neutral at spop, center
    r "Actually, why don't we go out for breakfast instead? I think that café by the pier is open to the public now."
    show ren happy at bpop, center
    r "W-We should… We should check it out!"
    n "A new café? Was he talking about the Driftwood café? I wasn't even aware that it was open to the public yet."
    n "Still… Taking him out for breakfast was the least I could do to show my gratitude."
    n "After all, [ch_ren] {b}did{/b} make sure that no creeps broke into my apartment again, and he did it all without expecting anything in return."
    y "Uhh— Yeah, sure. Let me get dressed then. I'll just be two seconds!"
    show ren happy at bpop, center
    r "Sure! Okay! T-Take your time! I'll just… I'll wait here."
    n "Leaving [ch_ren] unattended yet again, I quickly duck back into my bedroom to change out of my pyjamas."

    jump day2_pierdate

################################################################################
## ALONE MORNING WE STAN
################################################################################
label day2_alonemorning:
    scene angel_bedroom_day
    play music "audio/bgm/On The Way Home.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/morning.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 1.0, 1.0)

    n "Waking up to the sounds of birds chirping outside and the sunlight filtering through my blinds, I groggily rub my eyes before absent-mindedly staring at the ceiling for a few moments."
    n "A lot had occurred last night, and I still needed to process most of it."
    n "But the main thing that plagued my mind was the date I had planned today with [ch_ren], the guy I had met at the library yesterday."
    n "Reaching over my nightstand to grab my phone, I casually check the time — only to realise that I still had a few more hours to kill."
    n "Not only that, but I {b}also{/b} apparently received a text message from [ch_moth] at some point last night."
    n "At a glance, it appeared as though they were just ranting about the newest update for \"Always With You\" again, though I hadn't read the latest chapter yet to know all the details."
    n "Nevertheless, I read through their wall of text and memes with avid curiosity, and even send back a few of my own."
    n "Before I knew it, hours seemed to pass by in a blur."
    n "Glancing back at the time on my phone once more, I notice that it went from being eight o'clock to half past ten."
    y "…Half past ten?!"
    n "My date with [ch_ren] was supposed to be in half an hour!"
    n "I quickly let [ch_moth] know that I had to dip from the conversation, before throwing my phone onto the mattress and sprinting towards the bathroom."

    play audio "audio/sfx/vibrate.ogg"

    n "But just as I grab a fresh towel and a change of clothes from my wardrobe, my phone buzzes once more."
    n "Assuming it was {b}yet another{/b} text from [ch_moth], I pick it up and put in my passcode. But what awaited me was a message from none other than [ch_ren]."
    rt "hi hiii! ^^ gm angel! i hope i didn't wakr u up!"
    rt "wake*"
    rt "gah this is so embarrassing knowing ur a librarian >//< i swear i can spell lol"
    rt "hehe anyway!! i just wanted to confirm whether or not u were still on for our date today??"
    rt "becaus we can meet up at the beach walk if you are! it's not far from this new café i want to check out :D"
    n "[ch_ren]'s messages brought a smile to my face for some reason, and I assumed it was because he seemed {b}just{/b} as enthusiastic as I was for today."
    n "I send back my own affirmative text alongside a smiling Haruko sticker, before going back to my bathroom and getting ready for the day."

    jump day2_pierdate

################################################################################
## PIER DATE BRANCH
################################################################################
label day2_pierdate:
    scene beach_street_day
    play music "audio/bgm/Summer Memories.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/street.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 1.0, 1.0)

    if unlockable == "meowdacted":
        $ ren_outfit = "meow"
    else:
        $ ren_outfit = "normal"
    $ update_ren = "i'm so excited for today hehe >w<"
    $ location_ren = "pier"
    $ location_jae = "pier"
    $ location_leon = "pier"
    $ location_teo = "pier"
    $ location_violet = "random"

    if d1_inviteren == True:
        n "In the end, [ch_ren] and I decided to walk to the café together — considering how the weather was perfect and it wasn't that far from my apartment."
    else:
        n "In the end, I {b}did{/b} end up meeting [ch_ren] halfway via the boardwalk, and we decided to walk to this recently opened café together for lunch."
        n "It wasn't far from my apartment anyway, and I figured I could do with a bit of exercise."

    show ren flushed with dissolve
    n "Turning to my side, I notice how the pink-haired man tries to not-so-subtly sneak side glances towards me."
    n "The arm at his side practically {b}itches{/b} to reach out — and if I knew any better, I would've assumed he wanted to hold my hand."
    n "But instead, he simply tucks his hands into his pockets and shoots me yet another soft smile."
    show ren happy at spop, center
    r "The weather's really nice today, huh?"
    n "Back to small talk, it seems."
    y "Sure is. If I had known it'd be this nice and sunny, I would've suggested spending the day at the beach instead."

    if unlockable == "kitsune":
        show ren smirk at spop, center
        r "Yeah? …Not a big fan of caves, are you?"
        y "Caves? That's a bit specific…"
        show ren flushed at spop, center
        y "H-Huh? Never mind!"
    else:
        show ren sad at spop, center
        r "Y-Yeah?"
        y "Yeah. We could go for a swim, or maybe even check out the rock pools! It's been a while since I've been there."
        show ren happy at spop, center
        r "O-Oh-! That {i}does{/i} sound fun—"

    $ rpos = tleft
    $ lpos = tright
    $ update_leon = "…It's not his wallet. -_-'"
    $ update_jae = "yea htats MY WALLET!! @{}".format(username_conan.upper())

    play audio "audio/sfx/shoes alt.ogg"
    play audio "audio/sfx/sprinting.ogg"
    show ren frown at rpos
    show leon happy at lpos
    with easeinright

    l "[ch_angel]!" with vpunch
    n "At the sound of my name being called, I turn on my heels, only to find [ch_leon] running up to me with a sports bag full of what I assumed to be his volleyball gear."
    show leon smirk at spop, lpos
    l "Heyooo, Sunfish!~ It's good to see you out and about this early!"
    show leon happy at spop, lpos
    l "I was just on my way to the beach to meet up with [ch_jae] and [ch_teo]. Did ya wanna tag along?"

    if d1_inviteren == True:
        show leon neutral at spop, lpos
        l "And hey! It's Ron, right? Nice to see you again, buddy."
        y "Oh, it's {i}[ch_ren]{/i}, actually—"
    else:
        show leon neutral at spop, lpos
        l "And hey! Who's this? I don't think we met before, mate."
        show leon happy at spop, lpos
        l "The name's [ch_leon]. [ch_angel]'s {i}beeeestest{/i} friend in the whole wild world, yeah?"
        n "I playfully roll my eyes at [ch_leon]'s words and give him a slow, reluctant nod."
        y "Keep telling yourself that. But this is my friend [ch_ren]. We actually met—"

    show ren sad at spop, rpos
    r "—{i}Sunfish?{/i}"
    y "Huh? Oh, yeah…"
    y "\'Sunfish\' is the cheesy nickname [ch_leon] gave me when we were kids. I don't really get it either, to be honest."

    if d1_inviteren == True:
        show leon smirk at spop, lpos
        l "Soooo… {i}Sunfish{/i} and {i}[ch_ren]{/i}, was it? Sorry about that, bud! I'm not too good with names. Faces too, sometimes."
        show leon neutral at spop, lpos
        l "But hey! It's good to see you both again! Doing anything exciting today? If not, you can tag along with me and—"
    else:
        show leon smirk at spop, lpos
        l "Soooo… {i}Sunfish{/i} and {i}[ch_ren]{/i}, was it? Nice to meet ya. I hope we can get along and become good friends too."
        show leon neutral at spop, lpos
        l "Actually… Hey! If you're both free right now, why don't we go down to the beach? I can introduce you to [ch_jae] and—"

    show ren happy at bpop, rpos
    r "—{i}Angelfish{/i} and I were about to go on a date, actually."
    y "Angelfish?"

    if unlockable == "kitsune":
        n "…This cunning guy sure loved to use nicknames, huh?"

    show leon frown at spop, lpos
    l "A date?"
    n "I don't miss the way [ch_ren] suddenly pulls my arm closer to his side, nor the way he clings onto me as though I'd suddenly disappear."
    show leon smirk at spop, lpos
    l "You're going on dates again, darl'? Good for you!"
    show leon happy at spop, lpos
    l "I'm glad to see that you're coming out of ya shell again!"
    show leon neutral at spop, lpos
    l "Take good care of [them] for me, won't ya, bud?"
    show ren frown at spop, rpos
    r "{size=-6}…What do you think I've been doin' ever since you moved away?{/size}"
    n "Like me, [ch_leon] barely seems to notice [ch_ren]'s mumbling as he rests an arm over my shoulder and starts tugging me in the direction of the beach."
    n "[ch_ren], on the other hand, still latches onto my arm but doesn't seem to move."
    show leon smirk at spop, lpos
    l "I can't believe my little sunfish is out there in the dating scene again… I feel like a proud father…"
    y "Oh please, we're basically the same age!"
    show leon happy at bpop, lpos
    l "I feel like a proud, {i}adoptive{/i} father…"
    n "[ch_leon] pretends to wipe a tear away from his eyes as he leans further into my shoulder, and it was only then that I noticed [ch_ren] wasn't following us."
    n "Turning around, I reach out to grab {b}his{/b} hand instead to tug him along."
    show ren happy at rpos
    n "He immediately seems to perk up at the action and entwines his fingers with mine before falling into step."
    show leon sad at spop, lpos
    l "…"
    y "Alright, as fun as it is to catch up with my proud, {i}adoptive{/i} father who's the same age as me — which makes things kind of weird — [ch_ren] and I {i}do{/i} need to get going."
    show leon happy at bpop, lpos
    l "Oh. Yeah, 'course. I didn't mean to take up so much of your time!"
    n "He unhooks his arm from around my shoulder and inclines his head towards the beach one more time."
    show leon smirk at spop, lpos
    l "But my offer still stands! If you wanna catch up some more, I'll be down at the beach with—"

    if unlockable == "starshine":
        show leon happy at spop, lpos
        l "Oh, speak of the devil! Isn't that him over there?"
        n "Following [ch_leon]'s gaze, I barely make out [ch_teo]'s familiar figure leaning against the side of his car — with one of my other co-workers pressed against his chest."
        n "She seems all too happy to be there, and their close proximity makes it seem like they were winding down after going on a date together."
        n "But now that I looked closer… That was Rosie, right? The one in charge of the upstairs bar in the library?"
        n "Yes, there's an upstairs bar. No, we don't serve alcohol. It's just milk."
        n "I'm genuinely concerned about the well-being of my co-workers."
        n "Also… The implication that all the Discord mods are {b}also{/b} library employees is kinda funny, if I'm being honest."
        n "Next thing you know, I'll start seeing Pup or Shalls hanging around the Bay."
        n "But all too quickly, a surprised gasp pulls me from my thoughts, and I look up to see the couple approaching the three of us."

        $ tpos = ffullyright
        $ ropos = fright
        $ rpos = ffullyleft
        $ lpos = fleft

        show ren angry at rpos
        show leon frown at lpos
        show teo smirk at tpos
        show rosie neutral at ropos
        with moveinright
        $ meet_teo = True

        n "[ch_teo] isn't subtle with how he nudges [ch_leon] out of the way, nor does he seem to remove his hand from Rosie's waist."
        n "In fact, he seems to {b}revel{/b} in the way my face scrunches up at his blatant display of PDA."
        show rosie happy at bpop, ropos
        ro "Oh! hiiii [ch_angel]!"
        show rosie sad at bpop, ropos
        ro "Not at the library today? I heard Jesse set fire to one of the shelves again…"
        y "No, Chii and [ch_elanor] are working today. But I'm sure they can handle it."
        y "What I'm more concerned about is {i}why{/i} you're standing so close to that ugly raccoon. He probably has rabies."
        show rosie blushing at spop, ropos
        ro "Gehee~ You know [ch_teo]? He's my booooyfriend!"
        show rosie happy at spop, ropos
        ro "And the mother of our six pups — but that's an inside joke for another easter egg."
        y "Sorry, what? Wait…"
        extend " You're dating [ch_teo]?!" with vpunch
        show teo frown at spop, tpos
        t "…We're not dating."
        show rosie smirk at spop, ropos
        ro "Don't listen to him, he's just shy! We're actually married, and I'm {i}literally{/i} best friends with his nanny."
        show rosie neutral at spop, ropos
        ro "We {i}always{/i} catch up on the weekends, and I show her our wedding videos while she shows me all his baby photos!"
        show leon sad at spop, lpos
        l "Guys… I think she's delusional…"
        show ren frown at spop, rpos
        r "Y-Yeah…"
        show rosie happy at spop, ropos
        ro "—Do you want to see the baby photo of him butt-naked on a beach? I'm sure it's saved on my phone somewhere…"
        y "Seriously?! You're not embarrassed being with a guy like [ch_teo]?"
        show rosie smirk at spop, ropos
        ro "Honestly? No."
        show rosie blushing at spop, ropos
        ro "The only thing I'm embarrassed about is how I'm {i}literally{/i} the only one serving cunt right now."
        show rosie happy at spop, ropos
        ro "Like… [ch_leon]'s got the spirit, but shawty those chinos are {i}not{/i} the vibe."
        show rosie sad at spop, ropos
        ro "And why is everyone dressed like it's winter? We live next to the BEACH."
        y "So true. It's like the person who created this game forgot that tropical locations exist."
        y "I don't think she even knows what season we're in right now."
        show rosie frown at spop, ropos
        ro "Right? This is so lame."
        show rosie happy at spop, ropos
        ro "You know what? I think I'm going to go buy everyone new fits! Targetcore is sooo old, where are the girlies wearing Hello Kitty Y2K?"
        show rosie sad at spop, ropos
        show teo neutral
        ro "Baaaabes…"
        n "I watch as Rosie gives [ch_teo] her best puppy eyes as she clings to his side."
        n "A beat passes before he lets out a sigh, digs into his back pocket for his wallet, and hands it to her."
        show rosie happy
        show teo smirk at spop, tpos
        t "Can't say no to my star girl."
        show teo neutral at spop, tpos
        t "Fine. Buy whatever you want."
        show teo frown at spop, tpos
        t "And try not to crash my car this time."
        show rosie neutral at spop, ropos
        ro "Yippeee! Thanks pookie!"
        show teo flushed at spop, tpos
        t "Yeah, whatever."
        n "Despite the harshness in his tone, [ch_teo] gives her a soft kiss on her forehead before letting her go."

        $ rpos = cleft
        $ lpos = center
        $ tpos = cright
        hide rosie
        show ren frown at rpos
        show leon sad at lpos
        show teo flushed at tpos
        with moveoutright

        n "Btw hello Rosie, this is your subconscious speaking directly to you right now."
        n "In exchange for [ch_teo] blushing, I'm expecting Eddie on my doorstep by 3pm. Oiled up and gift-wrapped."
        n "Anyway!! Back to da storyline."
        n "Once Rosie drives off in [ch_teo]'s expensive-looking car, [ch_ren] and [ch_leon] {b}finally{/b} make themselves known once more."
        n "But that {b}annoying rat{/b} seems to have other things in mind."
        n "As soon as [ch_ren] takes a step closer, [ch_teo] takes it upon himself to \"casually\" shove him to the side with one of his muscular arms."

        jump day2_teocont
    else:
        pass

    $ rpos = cleft
    $ lpos = center
    $ tpos = cright

    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show ren angry at spop, rpos
    show leon neutral at spop, lpos
    show teo neutral at spop, tpos
    with easeinright
    $ meet_teo = True

    t "Oi!" with hpunch
    show leon smirk at spop, lpos
    l "Speak of the devil…"
    n "Almost like he appeared from thin air, Teodore — or rather, [ch_teo] — emerges from somewhere behind [ch_leon] and makes his way towards the three of us."
    n "Though unlike most of my friends here in Corland Bay, I actually met [ch_teo] in the city a few years ago; back when I used to live there. In fact, it was through our mutual friend [ch_jae]."
    n "Apparently, they'd both known each other since the beginning of middle school. But even after graduating and moving on to university, the pair were still practically inseparable."
    n "According to [ch_jae], [ch_teo] would always show up at campus to pay him a visit — though if I were being honest — I'm sure [ch_teo] only did it to antagonise some of the students and staff there."
    n "It {b}definitely{/b} wasn't out of the ordinary for him to do something like that. Plus… It offered me a lot more insight into the whole \"assertive yet nonchalant\" attitude he often liked to put on."
    n "The first time I'd ever witnessed it was when [ch_teo] found me sitting alone at a café. I still remember sitting there slack-jawed as he practically shoved my laptop bag to the side… before he sat down and took a sip of my drink like it was his own."
    n "The satisfied grin from seeing my displeasure said everything — and had he not offered to buy me another drink — I'm almost certain I would've told [ch_teo] to get lost and bother someone else."
    n "But before I can reminisce any further, I hear the sounds of [ch_teo]'s footsteps drawing closer and it pulls me back to the present."
    n "I watch as he walks up to us with a confident stride — before he purposefully bumps into [ch_ren] with the sole purpose of sending him tumbling into the metal railing behind him."

    label day2_teocont:
    n "But luckily [ch_ren] manages to catch his footing at the last second, sending [ch_teo] an annoyed scowl of his own."
    show teo smirk at spop, tpos
    t "Aw [shit], sorry about that. I'm not sure how I missed such a brightly-coloured children's mascot."
    show leon frown at spop, lpos
    l "Alright, there's no need for that here."
    n "Despite [ch_leon]'s tone, [ch_teo] barely pays the shorter male any mind — seemingly {b}far more{/b} interested in [ch_ren] instead."
    show teo neutral at spop, tpos
    t "Let me guess, you're dressed up as Benny the Buttercup? My four year old cousin would {i}loooove{/i} you."
    show leon sad at spop, lpos
    l "Oi, knock it off, mate."
    show ren frown at spop, rpos
    r "What's your problem?"
    show teo smirk at spop, tpos
    t "Dunno. What's yours?"
    n "I could practically {b}feel{/b} the tension between the two grow, so I decided to step in."
    y "Uh— Maybe you should introduce each other first before you try glaring each other to death?"
    y "[ch_teo], this is [ch_ren]. He's my… Well…"
    show ren happy at bpop, rpos
    r "I'm [their] boyfriend."
    n "Well… that was certainly one way to put it. Especially {b}without{/b} bringing it up with me beforehand."

    if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
        call DLC_day2_s1 from _call_DLC_day2_s1

    n "At his words, I shoot [ch_ren] a confused glance — but the determined look on his face had me biting back my words."
    y "Uhh… Okay? Anyway, this is [ch_teo]. He's—"
    n "…Wait, how should I introduce him to [ch_ren]?"

    #hide ren
    #hide teo
    #hide leon
    #with dissolve

    menu:
        #with dissolve
        "\"He's a friend from the city.\"":
            $ affection_leon += 1
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_jae += 1
            $ affection_teo += 1
            show ren frown at rpos
            show leon happy at lpos
            show teo happy at tpos
            with dissolve
            t "Aw, you consider us friends? That's real cute, Doll."
            y "…Are we {i}not{/i} friends? You always used to show up and sit next to me whenever I'd visit that café near campus."
            y "Which was weird, because I never told {i}anyone{/i} where I was going."
            show teo neutral at spop, tpos
            t "Oh? Maybe I wanted to say hi before visiting Goldie. It's on my route to his university, you know."
            n "So he wanted to spend time with me before visiting [ch_jae]? How… uncharacteristically thoughtful of him."
            show ren angry
            show teo smirk at spop, tpos
            t "…Or maybe I was bored and wanted to see what someone with a lower-class income does in [their] free time."
            if persistent.streamermode == True:
                n "Well then. Never mind."
            else:
                n "Never fucking mind."
            show teo neutral at spop, tpos
            t "Just kidding, Doll. 'Sides, you're a bit {i}too{/i} boring for my taste. I doubt you'd even be worth hiring a private investigator."
        "\"He's my ex-boyfriend.\"":
            $ affection_ren -= 1
            $ affection_teo -= 1
            $ relationship_teo = "exboyfriend"
            show ren frown at rpos
            show leon neutral at lpos
            show teo smirk at tpos
            with dissolve
            t "Yeah, I don't like to date people outside of my tax bracket."
            show teo frown at spop, tpos
            t "And don't get it twisted, Doll; we were never exclusive. I never even brought up the concept of dating when I was with you."
            y "Oh, that explains why you were fine with cheating on me."
            show leon frown at spop, lpos
            l "…Wait, what? I thought you guys were just friends?"
            show ren frown at spop, rpos
            r "{size=-6}…What a complete [asshole].{/size}"
            show teo angry at spop, tpos
            t "Excuse me? It's not cheating if I was never your boyfriend."
            show leon sad at spop, lpos
            l "Alright! Why don't we change the subject—"
            y "I'm sorry, you {i}weren't{/i} my boyfriend? Then why would you ask me not to see other people?"
            show teo smirk at spop, tpos
            t "You think I'd want to share you with others and let them have what's mine?"
            n "Before I can step forward and knock some sense into that idiot, [ch_ren] seems to beat me to it."
            n "He grabs the other male by the collar of his shirt, but [ch_teo] only looks on with a lazy smirk."
            if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
                call DLC_day2_s2 from _call_DLC_day2_s2
            else:
                show ren angry at bpop, rpos
                r "What's your problem?"
        "\"He's just a fling.\"":
            $ relationship_teo = "fling"
            $ affection_teo += 1
            $ affection_olivia += 1
            $ ren_decay += 1
            show ren frown at rpos
            show leon neutral at lpos
            show teo smirk at tpos
            with dissolve
            t "Just a fling? I'm pretty sure you hit my line up more than once."
            show leon frown at spop, lpos
            l "…Wait, what? I thought you guys were just friends?"
            show teo happy at spop, tpos
            t "Yeah, we're friends. Friends who were reeeeal close… Right, Doll?"
            show ren frown at spop, rpos
            r "…"
            show teo smirk at spop, tpos
            t "Aw. And what's wrong with your face, {i}Buttercup{/i}?"
            show ren angry at spop, rpos
            r "What did you just call me?"
        "[rh_o]\"I've never seen this man in my life.\"[rh_c]":
            $ affection_teo += 1
            $ affection_moth += 1
            $ affection_violet += 1
            $ affection_kiara += 1
            show ren neutral at rpos
            show leon frown at lpos
            show teo happy at tpos
            with dissolve
            t "And I've never seen this [person] in my life either."
            show leon sad at spop, lpos
            l "You guys are hilarious."
            n "With a sigh, I try my best to clear the air of any confusion."
            y "Alright, [ch_teo]'s just a friend I made back in the city—"
            show teo smirk at spop, tpos
            t "—You wanna know what's {i}hilarious?{/i} Buttercup's outfit over here."
            show ren angry at spop, rpos
            r "…What did you just call me?"

    show leon angry at bpop, lpos
    l "Okay, enough!"
    show leon sad at spop, lpos
    l "Look, why don't we just drop this, yeah?"
    show leon frown at spop, lpos
    l "You really need to stop trying to pick fights with everyone, mate."
    show teo smirk at spop, tpos
    t "Aw, don't get your panties in a twist. I seriously doubt Buttercup's capable of harming a fly — let alone able to throw a decent punch."
    show ren frown at spop, rpos
    r "…You can drop the nickname."
    show teo angry at spop, tpos
    t "Nah. But I think Dollface over here should drop you instead."
    show teo smirk at spop, tpos
    t "'Sides, the nickname is kinda cute. Matches your style pretty well, don't you think, {i}Buttercup?{/i}"
    show ren angry at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5), rpos
    n "I could see [ch_ren]'s hand clench into a fist as he advances towards [ch_teo], but thankfully [ch_leon] steps in once more."
    show ren frown at rpos
    show leon frown at spop, lpos
    l "Seriously! Why don't we all cool off, yeah? I think we're getting a bit too heated."
    show leon sad at spop, lpos
    l "Look, {i}we're{/i} gonna head down the beach."
    show teo frown at tpos
    n "I don't miss the way [ch_leon] sends [ch_teo] a sharp glare."
    show leon neutral at spop, lpos
    l "Are you sure you don't want to join us, [ch_angel]? I promise to make sure that [ch_teo] stays on his best behaviour."
    y "Sorry [ch_leon], but I've already made plans with [ch_ren]."
    y "And I seriously doubt they'll be able to get along. You know how [ch_teo] can get."
    show leon smirk at spop, lpos
    l "Yeah, you've got a point there. Well… Alright then."
    n "He leans closer to me — almost as if he didn't want the other two eavesdropping."
    show leon neutral at spop, lpos
    l "If anything happens, I'll be in the area. Just come find me, okay?"
    y "I will. Thanks, [ch_leon]."
    n "I give his arm a soft squeeze and turn my attention back to [ch_ren]."
    show ren sad at rpos
    n "But by the way he looks at us, I can only assume that he didn't like how close I was standing to my childhood friend."
    n "Though that could've also been because [ch_teo] was still around. And honestly? I couldn't blame him."
    n "Regardless, I reach for his hand once more and tug him toward the café — making a point of ignoring [ch_teo]'s crass words as we went along."
    show ren happy at bpop, rpos
    n "I barely notice how [ch_ren]'s mood {b}immediately{/b} changes when my attention is back on him, and he follows along like a lost puppy."

################################################################################
## CAFE DATE BRANCH
################################################################################
label day2_cafedate:
    scene store_cafe_day
    play music "audio/bgm/Refreshing Scent.ogg" fadein 1 fadeout 1
    play ambience "audio/ambience/cafe.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 1.0, 1.0)

    n "We eventually arrive at the Driftwood Café, and the smell of fresh pastries and brewed coffee flood my senses as it wafts through the open windows."
    n "And just as I had thought, the café looked as though it had only recently opened — though it didn't seem as busy or crowded as I anticipated."
    n "Pulling me from my thoughts, [ch_ren] ushers me into one of the empty tables before he goes off to make an order with a pleased look on his face."
    n "It was a bit strange how he didn't want to look at the menu first, but I chalked it up to him wanting to surprise me."
    play audio "audio/sfx/item.ogg"
    show ren sad z with dissolve
    n "He's barely gone for five minutes before he returns once more, taking a seat in front of me with a huff."
    n "A comfortable silence washes over us, and I watch as he absent-mindedly fiddles with the ends of his hair."
    n "Was he still concerned about what [ch_teo] said about his appearance earlier? Maybe it'd be a good idea to take his mind off of it."
    y "Hey [ch_ren]?"
    show ren happy z
    n "Almost immediately, he perks up with wide eyes."
    y "How do you manage to keep your hair so fluffy? It always looks so good."
    n "[ch_ren] seems to flush instantly at my words, and he sheepishly ducks his head lower to hide his reddening cheeks."
    show ren blushing z at spop, center
    r "…You like it?"
    show ren flushed z at bpop, center
    r "I uh— I usually just angle a blow dryer below my chin and blast the heat… And it just stays like that afterwards…"
    y "Oh! So you don't need to use any products or anything?"
    show ren blushing z at spop, center
    r "N-Not really…"
    n "Just when I thought he got over his timid personality, it slowly came crawling back. Was this {b}really{/b} who he was?"
    n "[ch_ren] must've taken my silence as a lack of response, seeing as he tries striking up another conversation."
    show ren happy z at bpop, center
    r "…So! Work's going good for you, huh? Finally got that promotion?"
    y "Ah— Yeah, I did! I was honestly surprised when I first got my promotion, considering how I've only moved back here recently."
    y "But [ch_elanor]'s been really helpful by showing me the ropes and—"
    y "Wait, how did you know I got promoted?"
    show ren blushing z at spop, center
    r "Oh! Y-Your co-worker told me all about it yesterday after you left…"
    show ren happy z at spop, center
    r "[ch_elanor], right? She seemed really proud of you."
    show ren neutral z at spop, center
    r "A-Anyway! What were you saying about her showing you the ropes?"
    n "I barely noticed how he managed to change the conversation back to me, as I recounted all the times [ch_elanor] helped me through my first week of working at the library."
    n "It eventually reached the point where it felt like I had been talking for hours, and it wasn't until something caught my eye did I {b}finally{/b} stop."

    menu:
        "[rh_o]\"Aww, look at that cute puppy!\"[rh_c]":
            $ affection_ren += 1
            $ affection_jae += 1
            $ affection_violet += 1
            $ affection_leon += 1
            $ ren_purity += 1
            show ren neutral z at spop, center
            r "…Hm?"
            n "[ch_ren] glances out the window and follows my line of sight where a small pomeranian sat, idling chewing the laces of its owner's shoes."
            show ren happy z at spop, center
            r "Haha, yeah! That is a pretty dog, but…"
            show ren smirk z at spop, center
            r "I think you're cuter. Nothing could compare to y—"
        "\"That goth style is pretty cool.\"":
            $ affection_moth += 1
            $ affection_olivia += 1
            $ affection_kiara += 1
            $ ren_switch += 1
            show ren blushing z at spop, center
            r "G-Goth style?"
            n "He {b}also{/b} glances out the window and follows my line of sight before landing on the person walking by."
            n "They were decked out head to toe with heavy makeup, platform boots, and clothing you'd only find in stores like Not Tropic."
            n "[ch_ren]'s eyes seem to follow their form until they're out of sight, and the impassive look on his face made me curious."
            show ren neutral z at spop, center
            r "Yeah… it {i}is{/i} kinda cool! D-Do… Do you like that kind of style?"
            show ren sad z at spop, center
            r "Because I always thought you preferred something softer a—"
        "\"You've got something in your hair.\"":
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_ren += 1
            show ren blushing z at spop, center
            r "…H-Huh?"
            n "At my words, [ch_ren] seems almost bashful as he sheepishly starts picking at the strands of his pink hair."
            n "But he seems to miss the small piece of fluff, no matter how many times he tugs at his roots."
            y "Here, let me."
            n "Stifling a laugh, I reach over the table to pluck the offending item out of his hair."
            n "[ch_ren] only seems to lean closer into my touch while his cheeks flush a light shade of red, and just as I pull the piece of fluff out—"
        "\"Sorry, what were you saying?\"":
            $ affection_ren -= 1
            $ affection_teo += 1
            $ ren_decay += 1
            show ren happy z at spop, center
            r "…Mm? Oh! We were talking about your favourite webcomics."
            show ren smirk z at spop, center
            r "Y-You mentioned having a collection of them back in your apartment, and I guess I got curious…"
            n "Did I say that? And were we really still talking about myself?"
            n "Surely I would've moved on to a different topic by now…"
            y "Uhh, well, I've actually been reading this new webcomic lately. It's called 'Always with Y'—"

    npc "{size=+6}Order twenty-five!{/size}" with vpunch

    show ren neutral z at spop, center
    r "Oh, that's us! Wait right here. I'll be right back."
    hide ren with dissolve
    n "Before I could get a word in, [ch_ren] was jumping out of his seat and meandering his way towards the kiosk."
    n "It really was a sight to behold, seeing [ch_ren] tower over most of the other customers who were waiting in line."
    n "Even the cashier herself — who seemed to be {b}at least{/b} six feet tall — had to crane her neck upwards just to look at him."
    show ren neutral z at spop, center with dissolve
    n "But before I could blink twice, [ch_ren] was already on his way back with a large tray full of delicious food."
    n "He seats himself back in his original spot with a pleased smile, and begins to lay out the dishes in front of me."
    y "Oh! This is…"

    menu:
        "A delicious looking scone":
            $ favourite_snack = "scone"
            $ affection_elanor += 1
            $ affection_kiara += 1
            $ affection_conan += 1
            play audio "audio/sfx/plate.ogg"
            show ren neutral z with dissolve
            n "A delicious-looking scone sits next to my beverage, and I almost heard my stomach rumble at the sight."
        "A chocolate croissant":
            $ affection_leon += 1
            $ affection_moth += 1
            $ favourite_snack = "croissant"
            play audio "audio/sfx/plate.ogg"
            show ren neutral z with dissolve
            n "A croissant with chocolate filling sits next to my beverage, and I almost heard my stomach rumble at the sight."
        "[rh_o]A big slice of cake[rh_c]":
            $ affection_ren += 1
            $ affection_olivia += 1
            $ favourite_snack = "cake"
            play audio "audio/sfx/plate.ogg"
            show ren neutral z with dissolve
            n "A generous slice of cake sits next to my beverage, and I almost hear my stomach rumble at the sight."
        "A sugary cookie":
            $ affection_violet += 1
            $ affection_jae += 1
            $ affection_teo += 1
            $ favourite_snack = "cookie"
            play audio "audio/sfx/plate.ogg"
            show ren neutral z with dissolve
            n "A scrumptious cookie sits next to my beverage, and I almost heard my stomach rumble at the sight."

    n "…How did [ch_ren] know that this was my favourite thing to order?"
    n "Granted, it wasn't like I've been to the Driftwood Café before, but this was usually what I'd order at any other café."
    n "It was honestly like he could read my mind."
    n "And what was {b}even more{/b} mind-boggling was that he didn't even need to look at the menu beforehand."
    n "It was like he just… knew."
    show ren happy z at spop, center
    r "…"
    show ren smirk z at spop, center
    r "Don't forget your drink."
    n "[ch_ren] shoots me another gentle smile of his before placing my drink before me."
    y "No way—"
    n "The drink he placed in front of me… It was…"
    
    #hide ren with dissolve

    menu:
        #with dissolve
        "A double venti organic chocolate brownie caramel frappuccino extra hot with one inch foam, non fat" if unlockable == "Ballsac":
            play audio "audio/sfx/glass.ogg"
            show ren smirk z with dissolve
            y "A double venti organic chocolate brownie caramel frappuccino extra hot with one inch foam, non fat?!"
            y "Omg [ch_ren]…… You shouldn't have"
            show ren neutral z at spop, center
            r "…"
            show ren happy z at spop, center
            r "literally what the fuck dawg"
        "[rh_o]A cup of coffee[rh_c]" if player != "Ballsac":
            $ favourite_drink = "coffee"
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_ren += 1
            play audio "audio/sfx/glass.ogg"
            show ren smirk z with dissolve
            n "I could tell by the scent that he ordered me a cup of steaming coffee."
            n "Just like what I'd normally have in the mornings in order to smoothly make it through the day."
        "A steaming latte":
            $ favourite_drink = "latte"
            $ affection_violet += 1
            $ affection_kiara += 1
            play audio "audio/sfx/glass.ogg"
            show ren smirk z with dissolve
            n "I could tell by that scent that he ordered me a nice, warm latte."
            n "Just like the ones I usually bring on my way to work sometimes."
        "A can of soda":
            $ favourite_drink = "soda"
            $ affection_moth += 1
            $ affection_leon += 1
            $ affection_olivia += 1
            play audio "audio/sfx/glass.ogg"
            show ren smirk z with dissolve
            n "The fizzy drink was certainly appealing, especially considering that it was my favourite flavour."
            n "Just like the ones I usually buy on my way to work sometimes."
        "A fruity smoothie":
            $ favourite_drink = "smoothie"
            $ affection_jae += 1
            $ affection_teo += 1
            play audio "audio/sfx/glass.ogg"
            show ren smirk z with dissolve
            n "The inviting aroma of fruit floods my senses, and that alone was what assured me that [ch_ren] ordered my favourite smoothie."
            n "Just like the ones I usually bring on my way to work sometimes."

    show ren blushing z at spop, center
    r "I-I hope this is okay! Unfortunately, this café doesn't really have much to offer, judging from the menu I saw online."
    n "Ah. So that's how he knew what to order."
    show ren sad z at spop, center
    r "I even tried asking for napkins earlier, but I don't think they heard me…"
    show ren frown z at spop, center
    r "M-Maybe I should try again?"
    n "I almost felt bad for him, but I also felt grateful for ordering me something that I'd normally eat at a café."
    n "[ch_ren] makes sure everything is on the table before putting the tray aside, and it was {b}then{/b} when I noticed what he'd ordered himself."

    if unlockable == "kitsune":
        n "On his plate sat a chicken sandwich, alongside a cup of coffee that was an {b}alarming{/b} shade of black."
    else:
        $ persistent.fact_food = True
        $ persistent.fact_drink = True ## I didn't realise it was only one sentence (so this variable isn't really needed) but fuck it we ball
        n "On his plate sat a strawberry sweet roll, alongside a cup of coffee that was an {b}alarming{/b} shade of black."

    n "He seems to pick up on my inquisitive stare — if the innocent tilt of his head was anything to go by."
    show ren happy z at spop, center
    r "…Do you want my meal instead? We can swap if you want! I-I don't mind…"
    n "This was supposed to be a date, right? Deciding to tease him a little, I shoot [ch_ren] a sly grin."
    y "That's okay, but you could offer me a bite instead."
    show ren blushing z
    n "[ch_ren] almost seems to combust on the spot as his cheeks turn red, and he almost chokes on his own spit."
    n "He looks down at his food before glancing back at me, only to look down once more to scoop up a bite-sized piece of his food."
    n "I watch as [ch_ren]'s cheeks turn a deep shade of red while he brings his fork closer to me — and not wanting to be seen as a coward, I lean in to take a bite."
    n "His eyes widen almost immediately, and he seems hyper-focused on the way my mouth wraps around the fork before I lick my lips and let out a pleased hum."
    show ren flushed z at spop, center
    r "…"
    y "Mmm, it's yummy! Try some."
    n "The pink-haired man seems to have an awkwardly long staring contest with his own fork, before he scoops up {b}yet another{/b} small piece and takes a bite."
    if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
        call DLC_day2_cafe from _call_DLC_day2_cafe
    else:
        n "[ch_ren]'s cheeks are still scarlet red and he seems almost fidgety with how his leg keeps bouncing under the table, so I decide to take pity on him and not tease him for it."
    n "With a knowing smile, I start digging into my own meal with a pleased hum."

################################################################################
## MEETING OLIVIA SCENE
################################################################################
label day2_meetolivia:
    scene black
    play music "audio/bgm/Start Of The Day.ogg" fadein 1 fadeout 1
    stop ambience fadeout 2.0
    with Fade(1.0, 1.0, 1.0)

    n "Eventually, we ended up finishing our meals and decided to do a bit of window shopping to pass the time."
    n "I had nothing else to do today, and [ch_ren] seemed {b}insistent{/b} on spending the rest of his time with me, so I agreed."
    n "We passed by a few clothing stores, ice-cream stands, surfboard rentals, and many other interesting buildings, though nothing really caught my interest."
    n "But just as I thought I'd lost all hope, one store in particular catches my eye."

    scene store_souvenir_day 
    show peffect
    show ren neutral z
    with GlitchDissolve

    n "In one of the display windows, I spot this cute little rabbit plushie in the style of Haruko's likeness."
    n "I mean, it even came with his limited edition sorcerer outfit and everything!"
    n "I couldn't believe they were selling these things {b}here{/b}, of all places — and at such a cheap price, too."
    play audio "audio/sfx/heels.ogg"
    show olivia neutral at right with easeinright
    $ meet_olivia = True
    n "[ch_ren] seems to take notice of what I was not-so-subtly gawking at — but before we could enter the store, the cashier walks in front of the display stand and blocks our view."
    n "She drops a box of miscellaneous items at her feet and begins stocking the shelf next to the plushies, before she finally notices us standing by the window."
    show olivia happy at right
    n "I don't miss the way her eyes widen at [ch_ren] — obviously taking an immediate liking to him — and almost shamelessly pushes a strand of hair behind her ears before giving him a small wave."
    n "Sneaking a glance at the taller man beside me, I notice how [ch_ren] wasn't even paying any attention to her — instead keeping himself busy by scratching at his jaw and kicking at the stray cobblestone rocks by his feet."
    n "But the cashier seemed adamant about getting [ch_ren]'s attention, considering how she felt the need to abandon her spot by the shelves and make her way towards us."
    show ren frown z
    play audio "audio/sfx/heels.ogg"
    show olivia happy z at spop with dissolve:
        xalign 0.8
    o "Hi there! Welcome to Seaside Trinkets! My name is [ch_olivia]. Can I help you with anything?"
    y "Oh no, we're just looking around. But thanks for—"
    show olivia neutral z at spop,
    o "—We recently got some new beach-wear merchandise if you're interested in checking them out!"
    n "…Was she seriously ignoring me?"
    show olivia sad z at spop
    o "Oh! You kind of look like someone I know! Have we met before? Maybe we went to the same school!"
    play audio "audio/sfx/walking.ogg"
    show ren frown z at spop with ease:
        xalign 0.2
    r "…M-Me? I don't think so."
    show olivia smirk z at spop
    o "Really? I definitely would've remembered a face like yours."
    play audio "audio/sfx/heels.ogg"
    show olivia neutral z at spop with ease:
        xalign 0.5
    o "Actually, now that I've got a good look at you…"
    n "I watch as she shamelessly takes in [ch_ren]'s appearance before crossing her arms over her chest and leaning back."
    show olivia happy z at spop
    o "You also remind me of one of those characters from a cartoon that's been gaining a ton of traction here!"
    show olivia neutral z at spop
    o "Apparently, one of the locations from that show is based on Corland Bay's main beach."
    play audio "audio/sfx/shoes alt.ogg"
    show ren neutral z at spop with ease:
        xalign 0.1
    r "Are you talking about Attack on Giant?"
    show olivia happy z at spop
    o "Is that the name of it? Then yeah!"
    show olivia sad z at spop
    o "I don't really know much about those cartoons, but our company recently started selling some stuff for it to entice the tourists."
    show olivia smirk z at spop
    o "Do you want to come inside and take a look?"
    play audio "audio/sfx/heels alt.ogg"
    show olivia happy z at spop with ease:
        xalign 0.3
    o "Actually… Do you want my number as well? Here!"
    show ren frown z at spop
    r "…You had this prepared?"
    show olivia neutral z at spop
    o "Hehe, of course!"
    show olivia neutral z at spop
    o "You {i}always{/i} need to be ready in case any cuties walk into the store!"
    play audio "audio/sfx/shoes alt.ogg"
    show ren frown z at spop with ease:
        xalign 0.05
    r "…"
    show ren blushing z at spop
    r "I… Well, I wouldn't want to sound like a hypocrite or anything…"
    n "[ch_ren] looks at me with a shy, knowing look before he hesitantly reaches out to take the piece of paper."

    if d1_inviteren == True:
        n "What did he mean by that?"
        n "Before I even get the chance to ask, [ch_ren] {b}already{/b} answers my silent question with red cheeks and a crooked smile."
        show ren flushed z at spop
        r "I-I… Uh— This is embarrassing, but…"
        show ren blushing z at spop
        r "I {i}also{/i} had my number prepared for when we met at the library yesterday. Here."
        n "He reaches into his back pocket and pulls out a folded, pink sticky note of his own before discreetly handing it to me… alongside [ch_olivia]'s number as well."
        y "…Huh?"
        n "Why was he giving me her number as well?"
    else:
        n "A hypocrite? …Oh, right. [ch_ren] {b}did{/b} leave his number on that pink sticky note yesterday. I'd almost forgotten about that."
        n "But… Did he really have it prepared beforehand? Admittedly, the thought {b}was{/b} kind of endearing — though before I have the chance to dwell on it any further, [ch_ren] cuts me off by subtly handing me [ch_olivia]'s number."
        n "Wait, what? He didn't want to pocket her number? Glancing up at the pink-haired man, I press him for more answers."
        y "…Huh?"

    n "My confusion must've been blatantly obvious since [ch_ren] was quick to explain his intentions. With a mischievous grin, he leans closer to whisper into my ear."
    show ren smirk z at spop
    r "Maybe we could prank call her later? That'll teach her not to give her number out to strangers."
    if d1_inviteren == True:
        y "But isn't that what you {i}just{/i} did with me, [ch_ren]?"
        n "I match his teasing smile with my own as I run my thumb over the pink sticky note in my hand."
    else:
        y "But isn't that what you did with me, [ch_ren]?"
        n "I match his teasing smile with my own as I recall the sticky note [ch_ren] left on my monitor at work."
    show ren happy z at spop
    r "T-Touché. But… I've yet to receive any prank calls from you, though."
    y "Pfft— Don't jinx it."
    n "Just as [ch_ren] lets out a puff of laughter at my joke, [ch_olivia] cuts him off."
    show olivia frown z at spop
    o "Umm, hello? I'm still here."
    show ren sad z at spop
    r "O-Oh. Right. Sorry."
    show olivia smirk z at spop
    o "Anyway! Now that you've got my number and I've got your attention again, I think it's only fair I show you around the store."
    show olivia happy z at spop
    o "I don't do this for just anybody, you know?"

    n "[ch_ren] doesn't seem to answer her initial question — nor does he seem to outright respond to her — and instead casts an inquisitive glance in my direction."
    n "It was like he was asking me for {b}my{/b} opinion — and I can only assume it was because he knew about my interest in anime."
    n "It was thoughtful of him to do that, but I kind of wanted him to tell that rude worker off instead."
    n "Wait… Did I really want him to do that? What was wrong with me?"
    n "I'm sure that the cashier just took an interest in him, and there was nothing wrong with that."
    n "It's not like we were a couple anyway — but we {b}were{/b} supposed to be on a date right now, and [ch_ren] {b}did{/b} declare himself as my boyfriend earlier."
    n "But I just assumed he said that in order to get [ch_teo] off my back."
    n "Does that mean… Was he feeling the same way as me? Was jealousy on his mind when we talked with [ch_leon] and [ch_teo] earlier?"
    n "I wasn't sure how I felt about this new discovery."
    show ren smirk z at spop
    r "[ch_angel]?"
    y "…Huh?"
    show ren happy z at spop
    r "Do you want to go look at the items? We've still got a bit of time to kill."
    show olivia neutral z at spop
    o "Here, why don't I show you the most recent stock! We haven't shown this to the general public yet, but I'm sure you'll love it!"
    play audio "audio/sfx/heels.ogg"
    play audio "audio/sfx/walking.ogg"
    show ren frown z at spop, left:
        xalign 0.5
    show olivia neutral z at spop, right:
        xalign 0.8
    with easeinleft
    n "Without warning, [ch_olivia] — was that her name? — reaches out for [ch_ren]'s arm and practically drags him inside the store."
    n "He lets out a surprised sound before leaning back and trying to grab hold of my own arm as well, but I was {b}just{/b} out of his reach."
    n "There was nothing else I could do but watch as [ch_ren] helplessly gets pulled into the store."
    play audio "audio/sfx/shoes alt.ogg"
    play audio "audio/sfx/heels alt.ogg"
    show ren frown
    show olivia happy at spop, right:
        xalign 0.7
    with dissolve
    o "It's back here in the stockrooms. Usually we don't allow customers downstairs, but you're a real hottie, so I'll let you take a sneak peek."
    show ren sad at spop
    r "No, actually, I'm good—"
    show olivia smirk at spop
    o "Don't worry, we won't get caught! I'm sure your [partner] won't mind if I borrow you for a bit."
    show olivia neutral at spop
    o "I'll even throw in some of those cartoon stickers for you! Surely that'll make it worth your time?"
    n "The wink she sends him felt a little excessive, and I honestly wished [ch_ren] would turn around so I could gauge his reaction."
    n "But instead, he leans in close to her face and whispers in a hushed tone that I could barely hear from my spot outside the store."

    if unlockable == "kitsune":
        show ren angry at spop
        r "{size=-6}If [ch_angel] wasn't standing there right now, I would've dumped your body in the caves without a second thought.{/size}"
    elif are == "are":
        show ren happy at spop
        r "{size=-6}If [they] weren't sta— {i}*mumble*{/i} —right now, I would've s— {i}*mumble*{/i} —down this stair— {i}*mumble*{/i} —without a— {i}*mumble*{/i} —thought.{/size}"
    else:
        show ren happy at spop
        r "{size=-6}If [they] wasn't sta— {i}*mumble*{/i} —right now, I would've s— {i}*mumble*{/i} —down this stair— {i}*mumble*{/i} —without a— {i}*mumble*{/i} —thought.{/size}"

    show ren smirk at spop

    if persistent.streamermode == True:
        r "{size=-6}And honestly, there— {i}*mumble*{/i} —nothing more I'd rather do.{/size}"
    else:
        r "{size=-6}And honestly, it's— {i}*mumble*{/i} —{i}fucking{/i} tempting.{/size}"

    show olivia sad at spop
    o "{size=-6}…?!{/size}"
    n "From their current position, it looked as though they were having a really intimate conversation, and I felt the sudden urge to look away."
    n "Why was I getting so bothered over this? I know we aren't together, but [ch_ren] shouldn't be off flirting with other people while on a date with someone else."

    if relationship_teo == "exboyfriend":
        n "Besides, this was {b}exactly{/b} the type of thing [ch_teo] would do to me when we were \"dating\"."
        n "He'd go around shamelessly flirting with other people — sometimes while I was in the very same room."
        n "And what made it worse was that he'd simply laugh it off by saying that he was just \"messing around\" and that I \"shouldn't be getting so worked up\"."
        n "I honestly couldn't believe that [ch_ren] was doing the same thing to me right now."
    else:
        n "I would never want to be with someone who wasn't considerate of my feelings — and up until now, I honestly thought [ch_ren] would've had a chance."
        n "I guess I was wrong."

    n "But still… there was this nagging voice at the back of my head that kept telling me not to give up on him so easily."
    n "[ch_ren] was the one who confidently stood his ground when [ch_teo] got a bit suggestive, so maybe I should do the same?"
    n "Would he even mind?"
    n "Before I can stop myself, my feet start to move on autopilot as I march towards the two of them and reach for [ch_ren]'s sleeve."
    show ren neutral
    n "I give it a hesitant tug, and I swear I could almost feel the relief wash over his body because of it."
    n "[ch_ren]'s entire demeanour seems to change in that moment, and he turns to me with a relieved smile on his soft features."
    y "I don't really have any interest in this store. Can we go somewhere else?"
    show ren happy at bpop
    r "Y-Yeah! Of course!"
    play audio "audio/sfx/heels alt.ogg"
    show olivia sad at spop, right:
        xalign 0.8
    with easeinleft
    o "Wait— Hold on—"
    n "[ch_ren] carelessly shoves [ch_olivia]'s outstretched hand aside and gently places an arm over my shoulder instead."
    n "And just like that, he's already guiding me out of the store and back onto the busy street."
    n "I can hear [ch_olivia] sputter out confused sounds as she watches the two of us leave, and I suddenly felt guilty for causing a rift between them."

################################################################################
## BYEEEEE BESTIEEEEEEE
################################################################################
label day2_rainscene:
    scene beach_street_day
    play music "audio/bgm/Summer Memories.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/movement.ogg"
    show peffect
    with Fade(1.0, 1.0, 1.0)

    n "No matter how many times I try to brush it aside, I still couldn't get my mind off of what had just occurred earlier. What if… What if [ch_ren] {b}was{/b} interested in her?"
    n "Granted, he probably shouldn't have blatantly flirted with her while on a date with me, but… He wasn't exactly the most confident guy."
    n "Would he still be able to talk to her again if things didn't work out between us?"
    n "No, I shouldn't be thinking like that."
    show ren happy with dissolve
    n "Peering up to gauge his expression, I notice how he didn't really look all that upset about leaving her."
    n "If anything, he seemed rather {b}content{/b} to be walking down the street with his fingers entwined with mine once more."
    n "I can feel him give my hand a protective squeeze as he looks down at me with his soft blue eyes, and all of my worries somehow melt away."
    n "Maybe I {b}did{/b} make the right choice after all. It might've been selfish, but it was worth having [ch_ren] look at me with such a gentle expression."
    n "Eventually, the sun starts to set behind the ocean as [ch_ren] and I continue to walk along the beach walk."
    n "Most of the conversation was geared towards me and my interests again, but every time I tried to learn more about [ch_ren], he only seemed to divert the conversation back to {b}me{/b} once more."
    n "But the more I focussed on this odd behaviour, the more I began to pick up on {b}his{/b} social habits as well."
    n "I learned that [ch_ren] would subtly pick at the sleeves of his cardigan whenever he got nervous, or how he'd scratch at his jaw whenever the conversation strayed down a path he didn't feel comfortable with."
    n "His little quirks told me more about himself than the dead-end conversations that only lead back to me — and I was content with knowing more about him than I did yesterday."
    n "[ch_ren] no longer felt like a stranger I had met at a library, but rather, someone I could consider a friend."

    if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
        call DLC_day2_s3 from _call_DLC_day2_s3
    else:
        n "Except friends aren't supposed to get jealous whenever they see them flirt with someone else."

    n "Jeez, what was wrong with me? It had barely been two days, and I was already contemplating whether or not I truly saw [ch_ren] in a romantic light."
    n "Was I going too fast? All of these thoughts were starting to get a bit overwhelming, and—"
    show ren sad at spop
    r "—Angel? Hello?"
    y "Huh?"
    show ren smirk at spop
    r "You're spacing out on me again."
    n "There's that look again."
    n "He keeps peering down at me with so much adoration in his eyes, and if I didn't know any better, I would think that he was already halfway in love with me."
    n "But that was a very conceited thought and probably wasn't even true."
    y "S-Sorry! I was just… thinking about things."
    show ren happy at spop zorder 1
    r "Are you going to share those \"things\" with the rest of the class?"
    n "He sends me a playful smile and a gentle nudge into my side, and I couldn't help but laugh."
    n "When did we become so comfortable with each other? And when did he lose his stutter?"
    y "It's nothing, really. Maybe a bit embarrassing, but… Well, I was wondering…"
    y "How do you feel ab—"
    n "My sentence gets cut short when a drop of rain lands on my cheek."
    show ren sad
    n "Instinctively, I look up and find myself wondering {b}how{/b} I didn't notice those dark clouds in the sky sooner."

    play ambience "audio/ambience/rain.ogg" fadein 1 fadeout 1
    show reffect

    n "All of a sudden, more droplets fall down — until it's all but pouring rain and forcing everyone in the area to find cover."
    show ren frown z at spop with dissolve
    r "Over here!" with vpunch
    play audio "audio/sfx/running.ogg"
    play audio "audio/sfx/sprinting.ogg"
    n "[ch_ren] doesn't seem to pay much attention when he grabs me by the wrist and pulls me underneath one of the awnings of a nearby building."
    n "He shields me from the rain with his body, and I couldn't help but feel {b}tiny{/b} with the way his arms cage me in as he rests them against the wall."

    scene CG D2_RAIN
    hide screen dayscalendar
    show screen menuwu
    $ quick_menu = False
    $ meet_ren = True
    $ persistent.cg_d2_rain = True
    show reffect:
        alpha 0.2
    with Fade(1.0, 1.0, 1.0)
    
    r "…"
    y "…"
    n "We look at each other in silence for a brief moment before erupting in laughter."
    n "Perhaps it was because of the adrenaline from all the panicked running, or the fact that [ch_ren]'s hair was starting to lose its fluffiness — but I couldn't hold back from letting out a fit of giggles."
    n "This only seems to spur [ch_ren] on as well, until we're both wheezing out our lungs and gulping down air."
    y "I {i}*huff*{/i} I can't remember the last time I ran that fast!"
    r "M-Me too!"
    
    play audio "audio/sfx/thunder.ogg"
    
    n "The looming sound of thunder echoes from afar, and drowns out our laughter until we're both silent once more."
    n "Once we both calm down, [ch_ren] moves me further away from the rain before casting a glance behind him."
    
    if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
        call DLC_day2_rain from _call_DLC_day2_rain
    
    r "Wait here. I'll buy us an umbrella so we can get out of this rain."
    y "But you'll get soaked!"

    if persistent.dlc_14nightswithyou == True and dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou_type == "paid":
        r "…You'll keep me warm later, won't you?"
        n "I roll my eyes at his attempt to flirt and send him off with an amused smile."
    elif unlockable == "kitsune":
        r "Haha, it's okay, I don't really mind the water when I'm in this form!"
        n "I shoot him a confused look and usher him away with an amused chuckle."
    else:
        r "Haha, 'tis a sacrifice I'm willing to make!"
        n "I roll my eyes at his corny joke and send him off with an amused smile."

    scene beach_street_day
    $ quick_menu = True
    hide screen menuwu
    show screen dayscalendar
    play audio "audio/sfx/running.ogg"
    show peffect
    show reffect
    with Fade(1.0, 1.0, 1.0)

    n "He doesn't look back before he makes a mad dash out into the rain, and down the street towards the closest convenience store."
    n "…"
    n "Though the rain only seems to get heavier the moment he leaves, and I find myself pressing even further against the wall behind me to avoid the recoil of the rain bouncing off the pavement."
    n "There wasn't much for me to do while I waited for [ch_ren] to return — aside from watching people scramble around for shelter."
    n "And just like that, the carefree sounds of laughter echoing from down the street capture my attention as I watch [ch_leon], [ch_teo], and [ch_jae] all run to cover like their life depended on it."
    n "Well. It seems as though their beach outing got cut short as well."
    n "Glancing back once more, I barely make out the figure of [ch_leon] using his bag as a makeshift umbrella as he ducks under one of the awnings of an ice cream stand."
    n "All while [ch_teo] and [ch_jae] trail behind at a leisurely pace, kicking and splashing water at each other in the rain."
    n "I had to look away the moment [ch_teo] started to remove his shirt, and I had an inkling that it was so that he could show off."
    n "And knowing [ch_jae], he'll follow along without a care in the world — because that's what he always does when it comes to his friends."
    n "A part of me feels like calling out to the group to see if I can wait out the storm alongside them, but they all seem to be enjoying themselves and I didn't want to get in between that."
    n "Plus, I did promise [ch_ren] that I'd wait for him here."
    y "…Even if he was taking his sweet time."
    n "Was he ever going to return? There was still no sign of him {b}or{/b} his comfy-looking cardigan, and I was beginning to wonder if he really did ditch me."
    n "After all, it must have been more than fifteen minutes by now."
    n "What if he got caught up with something? Or… What if he went back to see that cashier lady again?"
    n "Her store {b}did{/b} happen to be on the same street… But after spending the afternoon with [ch_ren] and getting to know him, I concluded that he wasn't the type of person to do such a thing."

    if relationship_teo == "exboyfriend":
        n "But if he was, then that would only add insult to injury — considering how [ch_teo] had done the same to me multiple times in the past."
    else:
        n "Plus, that'd be a really low blow considering that he was the one who offered to take me out on a date today."

    n "Although, if I was being honest with myself… It {b}did{/b} seem as though they had chemistry."
    n "Especially with how she looked at him and touched his arm as though it was the most natural thing in the world."
    n "She apparently knew him as well. Or, at least, he looked recognisable enough."
    n "Why did that thought make my blood boil?"
    n "Thankfully the rain was there to cool me off… As well as soak the ends of my outfit and make everything feel damp and uncomfortable."
    n "…"
    n "Was [ch_ren] really coming back? It shouldn't take this long to buy an umbrella."

    $ choice_style = "box"
    menu:
        "[rh_o]Wait for [ch_ren][rh_c]":
            $ affection_ren += 10
            $ ren_purity += 1
            y "Maybe something {i}did{/i} come up… I'm sure he'll come back."
            n "And as if on cue, I spot a familiar patch of pink hair from within the misty rain, frantically sprinting with an umbrella in one hand and a bag under the other."
            play audio "audio/sfx/running.ogg"
            play audio ["<silence 0.8>", "audio/sfx/sprinting.ogg"]
            show ren sad at spop, center with dissolve
            r "{size=-6}Angel? [ch_angel]?{/size}"
            play audio "audio/sfx/item.ogg"
            show ren frown z at spop with dissolve
            r "Ah!" with hpunch
            n "He almost slams into me before stopping just in time, and I could tell by the way he was wheezing that he ran all the way back here without stopping."
            show ren flushed z at spop, center
            r "S-S-Sorry! I thought I almost lost you for a second! It's so hard to see in this weather…"
        "Walk home alone":
            $ affection_ren -= 10
            $ ren_decay += 1
            y "This is stupid. Forget it."
            n "It doesn't really matter what he was doing; [ch_ren] shouldn't have taken over twenty minutes to buy an umbrella."
            n "That was just ridiculous. Besides, it was getting cold and the wind was starting to pick up. If I stay out here any longer, I'll probably get swept away."
            y "[ch_violet]'s flower shop should be somewhere nearby… Maybe I could wait out the storm there?"
            n "I mean, it was only a few blocks away, and she {b}did{/b} tell me about the spare key under one of the flower pots in case of an emergency."
            n "This was kind of an emergency, right?"
            n "Just as I psyched myself up to sprint towards the next overhanging roof across the street, a cold hand wraps around my wrist and scares the absolute [shit] out of me."
            n "Yanking back, I instinctively turn around in panic before meeting [ch_ren]'s worried blue eyes."
            show ren frown z at spop, center with dissolve
            r "…A-Angel! Where are you going? You shouldn't be running anywhere in this weather."
    $ choice_style = "default"

    y "Jeez [ch_ren], what took you so long!"
    n "I almost wanted to cuss him out for taking well over twenty minutes just to buy a single umbrella, but the genuinely apologetic look on his features made me hold my tongue."
    show ren flushed z at spop, center
    r "Sorry! I, um— Do you remember your friends from earlier? I ran into them on the way there, which took forever for me to shake them off—"
    show ren sad z at spop, center
    r "And then the convenience store ended up closing early due to the sudden weather change—"
    show ren frown z at spop, center
    r "So then I had to go to that {i}awful{/i} souvenir shop with that obnoxious and clingy cashier again, and she asked me if I—"
    n "He was talking a mile a minute, and I was worried he'd end up biting his tongue."
    n "Gently, I raise a hand to signal him to calm down, and his intense monologue soon comes to a halt."
    show ren sad z at spop, center
    r "I'm really sorry about making you wait so long, buuuut—"
    show ren happy z at spop, center
    r "Tada! I {i}did{/i} manage to get an umbrella! Among other things as well, hehe."
    n "He gives it a small twirl in his hands, sending droplets of water all over the place."
    show ren neutral z at spop, center
    r "We can start heading back home now if you want. Unless you want to go somewhere specific?"

    menu:
        "\"We can go to my apartment.\"":
            $ death_flag = "olivia"
            $ affection_ren += 1
            $ ren_purity += 5
            $ affection_jae += 1
            $ affection_olivia += 1
            $ affection_teo += 1
            show ren happy z at spop, center with dissolve
            r "Your apartment? Sure! It's close by anyway. I can walk you home."
            n "The image of me taking a nice, warm bath after being out in this weather was too hard to resist, so I end up eagerly stepping under [ch_ren]'s umbrella before heading back home."
            jump day2_angelapartment
        "[rh_o]\"We can go to your apartment.\"[rh_c]":
            $ d2_visitren = True
            $ affection_ren += 1
            $ affection_elanor += 1
            $ affection_kiara += 1
            $ affection_moth += 1
            show ren blushing z at spop, center with dissolve
            r "M-My apartment? Sure… It's not that far anyway. We could wait out the storm there if you'd like."
            show ren neutral z at spop, center
            r "I even have a heater and dryer we could use."
            n "The image of me sitting in front of a warm, cosy heater was too hard to resist, so I end up eagerly stepping under [ch_ren]'s umbrella while he leads the way."
            jump day2_renapartment
        "\"Where do you want to go?\"":
            $ affection_ren += 1
            $ affection_conan += 1
            $ affection_leon += 1
            $ affection_violet += 1
            $ d2_visitren = True
            show ren happy z at spop, center with dissolve
            r "Well… My place isn't far? We could wait out the storm there if you'd like."
            show ren neutral z at spop, center
            r "I even have a heater and dryer we could use."
            n "The image of me sitting in front of a warm, cosy heater was too hard to resist, and I ended up agreeing with [ch_ren]'s suggestion."
            jump day2_renapartment
        "[de_o]\"Forget it, I'm going home alone.\"[de_c]":
            show ren sad z with dissolve
            pass

    y "[ch_ren], you took way too long. I honestly thought you left me at this point."
    show ren sad z at spop
    r "…Huh? Wh-Why would I—"
    y "Look, it doesn't matter. You've already wasted my time, and now I'm all soaked."
    y "I'm just gonna head home. Thanks for today, but after waiting for so long, I'm no longer in a good mood."
    show ren frown z at spop
    r "W-Wait!"
    n "He grabs onto my wrist again, but this time his grip was much stronger — almost as if he wanted to keep me here."
    n "Turning to face him, I barely give him more than a second to explain himself before I decide to walk off."
    show ren neutral z at spop
    r "I-I was just… I— You wanted that Haruko plushie from earlier, right? I bought it on the way back."
    show ren sad z at spop
    r "I really didn't think I'd take that long, but—"
    n "As if to prove a point, he offers me the bag from under his arm."
    n "And true to his word, there was the plushie I was eyeing earlier — all wrapped up in a plastic casing to stop it from getting wet."
    n "It almost pulled at my heartstrings — and I would've found his consideration endearing like usual — but something about seeing [ch_ren] with that cashier from earlier still rubbed me the wrong way."
    n "For all I know, he could've been chatting her up while she wrapped the toy."
    y "No, it's fine. You can keep it. I just want to go home, okay? So let go of my arm now."
    n "As if {b}finally{/b} noticing his grip on me, [ch_ren] hesitantly lets go of my arm."
    play audio "audio/sfx/item.ogg"
    n "But not before gently placing the bag into my arms for me to take and offering me a pitiful smile."
    show ren frown z at spop
    r "R-Really! I was just buying this for you! I'm really sorry it took me so long…"
    n "I merely offer him one final nod of my head before I turn on my heel. Whether or not he perceived that as me accepting his apology was up to him."
    show ren sad z at spop
    r "You're really going? W-Wait— I—!"
    n "He reaches for my sleeve this time, and I feel him give it a faint tug before he lets go, almost as if he remembered my words from earlier."
    show ren frown z at spop
    r "Please don't go. Please stay. I-I'll buy you something else!"
    show ren frown z at spop
    r "What about your favourite snack? Or— D-Do you want another [favourite_snack]? There's a convenience store nearby!"
    show ren sad z at spop
    r "O-Or… Maybe some more manga? We can go to the library instead!"
    n "Was [ch_ren] {b}seriously{/b} putting up that timid act again? After all this time? I don't even bother turning around at this point."
    show ren frown z at spop
    r "Angel, please!"
    show ren sad z at spop
    r "Please don't go! I'm sorry! Let me make it up to you!"
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/shoes alt.ogg"
    show ren frown at spop with dissolve
    r "[ch_angel]!"
    n "His voice gets drowned out by the rain as I hurriedly run back home, using his bag as a makeshift umbrella."

    ## ANGY ARC STARTS HERE

    scene angel_lounge_night
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/running.ogg"
    stop ambience fadeout 2.0
    show peffect
    with Fade(1.0, 1.0, 1.0)
    
    play audio "audio/sfx/door.ogg"
    n "Slamming the door shut, I immediately throw the bag in frustration—"
    extend " before picking it back up and ensuring that the contents inside it were still okay."
    n "After all, while this poor Haruko plushie didn't deserve such horrid treatment, [ch_ren] sure did."
    n "Placing it back on the table, I decide to change out of my wet clothes and take a quick shower."
    n "There was no use in making things {b}even worse{/b} by catching a cold."
    n "I could even check to see if [ch_moth] was online later and vent to them. Ugh, I really wanted to scream right now."

    scene black
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/Lonely Doll.ogg" fadein 1 fadeout 1

    n "Once I was finished with my shower, I noticed how the plushie was no longer on the table where I left it."
    n "Strange… Did it fall off? I shuffle around the kitchen island to investigate when the power suddenly turns off."
    y "Great. Now there's a blackout too, huh?"
    n "In a pathetic attempt to not bump into anything, I fumble around for the cupboard under the sink to try and find some spare matches and candles." 
    play audio "audio/sfx/glitch.ogg"
    stop music fadeout 1

    n "But as\ \ \ \ \ \ I do\ \ \ so, I barely make\ \ \ \ \ \ out\ \ \ \ \ \ \ \ {color=#a30b11}{size=-6}01101000{/size}{/color}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ the sound \ \ {color=#a30b11}{size=-6}01101001{/size}{/color}\ \ \ \ \ \ \ \ {color=#a30b11}{size=-6}01011110{/size}{/color} \ \ \ \ \ \ \ \ \ of my front\ \ \ \ \ \ door \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ creaking\ \ {color=#a30b11}{size=-6}01011110{/size}{/color}\ \ \ \ \ \ \ \ \ \ \ \ \ open—"

    jump day2_deadend

################################################################################
## REN'S APARTMENT BRANCH
################################################################################
label day2_renapartment:
    scene black
    stop ambience fadeout 2.0
    show peffect
    with Fade(1.0, 1.0, 1.0)

    $ persistent.d2_visitren = True
    $ persistent.fact_residence = True
    $ location_conan = "home"
    $ location_jae = "home"
    $ location_violet = "random"
    $ location_leon = "home"
    $ location_teo = "random"
    $ location_olivia = "random"
    $ location_ren = "home"

    n "Despite the heavy downpour of rain, we managed to make it to [ch_ren]'s apartment complex in one piece."
    n "I guess he {b}really{/b} wasn't lying when he said his apartment wasn't far from mine…"
    n "But judging from the pristine interior and fully-functioning elevators, his building seemed to be in {b}far better{/b} shape compared to my apartment."
    n "The elevator ride could've been a little less awkward though, if it weren't for the slow ascend and tacky music…"
    n "Or for the fact that [ch_ren] deemed it appropriate to shake his hair like a wet dog and get water droplets everywhere."

    scene sh_complex_night
    play music "audio/bgm/With You.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve
    n "Once the elevator doors slid open, I was immediately met with a grandiose corridor and large, spacious doors — and I found myself wondering how much it'd cost to live in a place like this."
    play audio "audio/sfx/shoes alt.ogg"
    show ren flushed at spop, center with dissolve
    r "Don't look too hard at how messy my place is, okay?"
    show ren blushing at spop, center
    r "I wasn't expecting to have someone over today, so I didn't bother cleaning up…"

    if d1_inviteren == True:
        y "I'm getting a weird sense of déjà vu…"
        show ren happy at spop, center
        r "Haha~ Thankfully, I don't have any white-haired neighbours who like to take their plants on walks."
        show ren neutral at spop, center
        r "Actually, now that I think about it…"
    else:
        y "Haha, I'm sure it's not as bad as my place. Or the entire apartment I live in, for that matter."
        show ren happy at spop, center
        r "O-Oh. That bad, huh? {size=-6}Maybe you could live with me instead…{/size}"
        y "Sorry, did you say something?"
        show ren flushed at spop, center
        r "Ah! N-No! I mean— Well… I was just thinking—"

    show ren sad at spop, center
    r "It's a bit strange, but no one lives on this floor aside from me. I'm not really sure why, but I'm not gonna complain."
    show ren smirk at spop, center
    r "I can make as much noise as I want, n' no one would notice."
    n "[ch_ren] shoots me a mischievous grin, and I find myself wondering what he meant by that."
    y "Like… Loud music and stuff? Movies?"
    show ren smirk at spop
    r "…Yeah, somethin' like that."
    n "He unlocks the door with some electronic card attached to his key chain, and the moment the door swings open, I let out an audible gasp."

    scene ren_lounge_day
    show peffect
    play audio "audio/sfx/door.ogg"
    with dissolve

    n "[ch_ren] doesn't seem phased in the slightest as he flicks on the lights and walks into his own home — but I could only stand at the entrance to his foyer in shock."
    n "Yes. {b}Foyer{/b}. He had a whole [damn] foyer in his apartment."
    n "Was this even an apartment? Surely a penthouse would've made more sense."
    y "Holy [shit], [ch_ren]…"
    play audio "audio/sfx/item.ogg"
    show ren sad z at spop, center with dissolve
    r "Is there something wrong? What is it?"
    show ren flushed z at spop, center
    r "I know the decor is kind of tacky, but it came with the apartment, a-and I haven't found the time to do anything about it yet…"
    y "I'm sorry, but are you the long-lost heir of a billionaire or something? This place is huge!"
    y "…And hello? Is that marble?"
    show ren blushing z at spop, center
    r "Ahaha! No, I just… I get paid a lot from my job. Enough to afford rent, at least."
    y "Y'know, I don't think I've asked you this yet, but… What exactly is your job?"
    show ren sad z at spop, center
    r "Uh—! My job is… Um! Well—"
    show ren smirk z at spop, center
    $ persistent.fact_job = True
    r "I-I guess you could say I'm a programmer? I dunno. I just take on a few jobs every so often. Nothing super fancy or anything."
    y "Nothing super fancy? [ch_ren], you have {i}marble{/i} flooring."
    n "Leaving the newly discovered programmer at the entrance, I curiously venture further into his 'apartment'."

    play audio "audio/sfx/walking.ogg"
    show ren angry at spop, center with dissolve
    if persistent.streamermode == True:
        r "{size=-6}Marble's a pain in the rear end to clean too…{/size}"
    else:
        r "{size=-6}Marble's a pain in the ass to clean too…{/size}"

    show ren neutral at spop, center
    r "Oh— Angel! D-Do you want some slippers? The floors can get cold, and your shoes are probably soaked, right?"
    n "Turning around, I notice [ch_ren] opening a small closet and pulling out a pair of dark house slippers. He looks at me with a curious expression, but makes no effort to hand them over."
    show ren happy at spop, center
    r "Only if you want them."
    y "…I'll take them — but only because they look like they're Ducci."
    n "[ch_ren] lets out a puff of laughter through his nose at my joke, but doesn't seem to deny it."
    n "Were these slippers {b}really{/b} from a luxury brand?!"
    n "As I put them on, I notice how they're an exact fit, and it makes me wonder if I just have average-sized feet — or if [ch_ren] had bought a bunch of expensive house slippers in varying sizes."
    n "But as funny as that imagery was… How {b}did{/b} he accurately guess my shoe size without seeing my feet?"
    show ren neutral at spop, center
    r "Here, why don't I show you to the bathroom? I'll find you something to wear in the meantime while your clothes are in the dryer."
    show ren blushing at spop, center
    r "Or would you prefer a towel instead? I guess that'd make more sense…"
    show ren flushed at spop, center
    r "S-Sorry, I— Um, I don't usually invite people over."
    n "Seeing his timid side resurface once more gave me the sudden urge to tease him."

    menu:
        "[rh_o]\"Just a towel?\"[rh_c]":
            $ affection_ren += 1
            $ affection_olivia += 1
            show ren blushing at center
            y "Just a towel? Nothing else?"
            show ren sad at spop, center
            r "Yeah…? T-To keep you warm instead of taking a shower? Unless you'd prefer a blanket, because I'm pretty sure I have an electric—"
            show ren blushing at bpop, center
            extend " {i}Oh.{/i}"
            n "It was as if all the gears inside his head were finally clicking together."
            show ren flushed at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
            r "N-N-No! I didn't mean— I meant a {i}towel{/i} that you can {i}wear{/i} over your clothes! Not… Not just {i}you{/i} in a towel… Unless you'd want to— But that's— Why would you—"
            show ren frown at spop, center
            r "Ugh. I'm just going to shut up now. S-Sorry."
            n "That… wasn't what I meant at all, but his reaction was priceless nonetheless."
            show ren blushing at spop, center
            r "A-Anyway!"
        "\"Is it Egyptian cotton?\"":
            $ affection_teo += 1
            $ affection_kiara += 1
            show ren neutral at spop, center
            r "'Egyptian cotton'? …What's that?"
            y "It's kind of in the name, [ch_ren]."
            show ren sad at spop, center
            r "Ah. Well, I don't think my towels come from Egypt? I mean…? That's pretty far away, and I can only imagine how expensive the shipping would be…"
            y "Pfft— You know what? Forget I asked."
            n "He actually looked like he was considering the question, and I had to roll my eyes in good humour."
            n "Especially at his comment on shipping being expensive. What were shipping costs to him if he could afford a place like this?"
            show ren flushed at spop, center
            r "So… Uh… A-Anyway!"
        "\"Don't you have any friends?\"":
            $ affection_jae += 1
            $ affection_moth += 1
            if unlockable == "starshine":
                show ren flushed at spop, center
                r "Wha—?! I-I do! He's just… He's busy with his job at the gas station, a-and…"
                r "Well, he doesn't exactly live in Corland Bay in the first place…"
                y "Uh… what?"
            elif unlockable == "kitsune":
                show ren flushed at spop, center
                r "Wha—?!S-So maybe they're not exactly human, but…"
                r "Well… You probably don't remember them either, right?"
                y "Uh… what?"
            else:
                show ren flushed at spop, center
                r "Wha—?! I-I do! …I think? Though, to be fair, I haven't invited him to my new place yet…"
                show ren sad at spop, center
                r "But he doesn't exactly live in Corland Bay in the first place…"
                y "Uh… what?"
            show ren blushing at spop, center
            r "W-What? Nothing! Never mind! A-Anyway!"
        "\"Am I your first house guest?\"":
            $ affection_leon += 1
            $ affection_violet += 1
            $ affection_conan += 1
            $ affection_elanor += 1
            if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
                call DLC_day2_s4 from _call_DLC_day2_s4
            else:
                show ren blushing at spop, center
                r "…M-Maybe."
            show ren sad at spop, center
            r "I'm… I'm actually very picky with who I invite over. And I prefer to be on my own most of the time, so… I don't usually bring people over."
            y "You never answered the question."
            n "I give him a teasing smile, and he shyly turns his head away instead."
            show ren flushed at spop, center
            r "…A-Anyway!"

    show ren happy at spop, center
    r "I'll show you to the bathroom. You can use whatever you want in there. Nothing is off-limits."
    n "First it was offering to spend the night at my place, then it was asserting himself as my boyfriend in front of my friends…"
    n "He really doesn't care about personal boundaries, huh?"
    n "I was beginning to think that [ch_ren] didn't really seem to mind when it came to me invading his personal bubble as well."
    n "Though he still seemed pretty standoff-ish around [ch_teo] and [ch_leon] — and it took him a while to warm up to [ch_elanor] back at the library."

    if d1_inviteren == True:
        n "He even seemed indifferent when he first met [ch_violet], but I figured it was only because he was shy."
    else:
        n "But it chalked it all up to him being his usual shy and eccentric self."

    n "Speaking of being shy, I still noticed how [ch_ren] didn't seem to be switching up his personality as much anymore, and I was beginning to think that he was showing me his real side."
    n "Up until now, everything felt real and genuine, and I found that we could bounce back witty retorts between each other more easily."
    n "Though every now and again he might slip up and stutter, but I just assumed it was because my teasing made him flustered."
    n "So… Maybe the timid side of him {b}was{/b} genuine after all?"
    show ren neutral at spop, center
    r "—But I'll leave some clothes for you outside, and put the plushie I bought for you in your room."
    y "Huh? Oh, uh… yeah! Thanks."
    n "Great, I was zoning out again and completely missed half of what he was saying."
    n "Something about clothes? And a plushie he bought? Was he talking about the Haruko plushie I was eyeing up earlier?"
    n "I mean, he {b}was{/b} carrying a gift bag from that souvenir shop earlier… Did he really buy me that toy?"
    n "[ch_ren], however, doesn't seem to pick up on my confusion though, and invitingly opens the bathroom door for me with a soft smile."
    n "And so, without trying to make things awkward, I quickly slip inside and lean against the door for support."
    n "Which was fortunate for me because one sweep of the bathroom had me stumbling back in surprise."

    scene ren_bathroom_day
    show peffect
    play audio "audio/sfx/movement.ogg"
    with GlitchDissolve

    y "Woah…"
    n "Even his restroom looked expensive… I was afraid of touching anything, fearing I'd accidentally break it and end up paying for it."
    $ persistent.fact_cosmetics = True
    n "Glancing around again, I notice how his countertop seems to be void of any dental care, hairbrushes, and skincare products — though a few bottles of concealer and an opened box of hair dye sit in the corner near the sink."
    n "Well, I guess that answers my burning question on whether or not he naturally had pink hair…"
    n "But now it made me wonder; if [ch_ren] {b}does{/b} dye his hair, then what was his natural hair colour?"
    n "There were still so many things I didn't know about that soft-looking guy, and I was beginning to question whether coming here was a good idea or not."
    n "With a sigh, I decide not to waste any more time thinking about irrelevant things and instead turn my attention back to the shower."
    n "Quickly stripping out of my clothes, I jump into the unnecessarily large glass booth and turn the water on."

    scene black
    play ambience "audio/ambience/shower.ogg" fadein 1 fadeout 1
    with dissolve

    n "Glancing at [ch_ren]'s shelf of (albeit limited) hair and body products, I couldn't help but notice that one brand in particular happened to be the exact same as mine."
    n "Did we use the same body wash? He didn't really smell like me, but maybe that was because I wasn't paying much attention."
    n "I mean, who randomly smells people out of the blue anyway?"
    n "Shaking my head at such a silly notion, I begin to scrub away the lingering smell of rain from my body and quickly finish washing up."

    scene ren_bathroom_day
    show peffect
    stop ambience fadeout 2.0
    with dissolve

    n "Bundled up in a warm towel, I crack open the large door and poke my head out into the hallway."
    n "True to his word, [ch_ren] left a small pile of clothing outside the bathroom — neatly stacked and propped against the side of the wall."
    n "Bringing the contents back inside, I notice that one piece of clothing in particular was a rather comfy-looking hoodie…"
    n "But the design on the front, however, was rather morbid looking and didn't really suit [ch_ren]'s vibes."
    y "…Maybe from a horror film or something? {i}Ehh.{/i}"
    n "Shrugging my shoulders, I put the hoodie on and instantly get enveloped by the sheer amount of fabric."
    n "I mean, it made sense considering [ch_ren]'s large and lanky frame, but this was just absurd."
    n "I had to stifle a laugh from the amusing sight in the fogged-up mirror, but I had to admit that the soft fabric felt nice and warm against my skin."
    n "Even the scent that came from it felt oddly comforting somehow."
    n "Turning back to the remaining clothes in the pile, I gently pick up the next item and try to put it on."
    n "The grey sweatpants didn't seem to fit the length of my legs despite the number of times I tried to tug at the fabric, but luckily [ch_ren] was thoughtful enough to give me other alternatives."
    n "The dark pair of shorts seemed like the better option, especially since it came with a drawstring {b}and{/b} deep pockets."

    scene ren_loungeroom_night
    $ ren_outfit = "lounge"
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    show peffect
    with GlitchDissolve

    n "Once I was fully dressed, I step out of the bathroom and aimlessly walk around until I hear the faint sounds of a TV playing."
    play audio "audio/sfx/walking.ogg"
    n "Feeling curious, I follow the source of the sound down the hallway."
    npc "—eaking news! A sudden storm hits the Bay, as galeforce winds and— *crrk!* —nock over street signs and even awnings—" with hpunch
    npc "*crrk!* —gists believe that this sudden change in weather will die down soon, and to stay safe indoo—"
    n "I continue to follow the noise until it suddenly cuts out and changes into a glaring monotone sound, indicating that the television must've lost all signal."
    n "And soon enough, I find myself in [ch_ren]'s spacious lounge room."
    n "Aside from the TV, the rest of the lights were off — but I could still make out most of the dark shapes within the room with ease."
    n "It was just as ostentatious as the rest of his house, though I couldn't help but feel like it lacked any form of life."
    n "It just didn't seem like someone actually lived here."
    n "The furniture was gaudy yet tasteless, there was hardly any personal decoration or colours, and there was nothing that really screamed '[ch_ren]' to me."
    n "There were no personal touches, photos, items, hobbies, {b}nothing{/b}. Just tacky furniture and the bland smell of something sterile."
    n "If I was being honest, it gave off the same vibe as a dentist's clinic or a hospital."

    if d1_inviteren == True:
        y "I mean, he {i}did{/i} mention recently moving in, right? Maybe that's why…"
    else:
        y "Maybe he recently moved in?"

    play audio "audio/sfx/shoes alt.ogg"
    show ren smirk at spop, center with dissolve
    r "—Who moved in?"
    n "Surprised by the sudden voice, I spin on my heel only to find [ch_ren] coming out from one of the hallways with a new set of comfy clothing."
    n "He seemed much more at ease like this, especially with the gentle expression on his face."
    n "I watch as he takes a respectful glance at my attire, before sheepishly averting his attention to the ends of his sleeve."
    show ren blushing at spop, center
    r "Sorry… That's the only pair of clothing I could find that might fit you. It looks really good on you, though."
    y "Oh… Thanks."
    show ren flushed at spop, center
    r "{size=-6}You can even keep 'em, if y'want—{/size}"
    play audio "audio/sfx/thunder.ogg"
    n "The sound of thunder rumbling in the distance cuts off [ch_ren]'s mumbling, and I involuntarily step closer to him."
    play audio "audio/sfx/item.ogg"
    show ren flushed z at center with dissolve
    n "Without missing a beat, he reaches out and rests a protective hand on my shoulder to steady me."
    n "[ch_ren] idly glances out of the window before turning his undivided attention back to me once more — only this time, with a determined look."
    show ren frown z at spop, center
    r "It's really pouring, huh?"
    n "I could only nod my head at his words, suddenly feeling sheepish all of a sudden."
    n "I {b}really{/b} should've checked the weather forecast before I went out today…"
    n "But to be fair, it didn't look as though it'd start spontaneously raining when I left my apartment this morning."
    n "And I guess I was enjoying my time with [ch_ren] to the point where I didn't even realise the weather was turning sour."
    show ren neutral z at spop, center
    r "—Angel?"
    y "Sorry, what did you say?"
    show ren smirk z at spop, center
    r "Ah, I just asked if you wanted to stay the night here. Y'know… Seeing how hard it's raining out there, and your clothes haven't finished drying yet."

    if d1_inviteren == True:
        show ren neutral z at spop, center
        r "It'd be no trouble. And I could return the favour, considering how you let me stay at your apartment yesterday…"
    else:
        show ren neutral z at spop, center
        r "It'd be no trouble. I really wouldn't mind at all — but only if y'wanna, of course."

    n "Staying at his place for the night? Well, this certainly isn't how I expected to end my day."
    n "But would it {b}really{/b} be that bad? It definitely beats waiting out the storm and walking home with a bunch of puddles everywhere."
    
    #hide ren with dissolve

    $ choice_style = "box"
    menu:
        #with dissolve
        "Spend the night":
            $ affection_ren += 10
            show ren neutral z at center with dissolve
            pass
        "{glitch=10.0}{b}Spend the night{/b}{/glitch}":
            $ ren_decay += 1
            $ affection_ren -= 10
            play audio "audio/sfx/glitch.ogg"
            show gwitch
            show ren neutral z at center
            with GlitchDissolve
            n "Wait, what… was that? Did I really want to stay the night at [ch_ren]'s place?"
            hide gwitch
            n "…I guess I did? I couldn't really remember otherwise."

    $ choice_style = "default"
    y "I guess I could stay… if that's really okay with you."
    show ren happy z at bpop, center
    r "Yeah! Of course! It's totally fine!"
    n "Wow, he really was an energetic, eccentric man, wasn't he?"

    scene ren_hallway_night
    show peffect
    with Fade(1.0, 1.0, 1.0)

    show ren neutral at bpop, center
    r "Lemme know if you need any more pillows or blankets."
    show ren happy at bpop, center
    r "Or if the room gets too cold. I haven't worked out how to use the fancy heater system yet, but I can definitely try."
    show ren sad at bpop, center
    r "Also— you already know where the bathroom is, but if you—"
    y "Okay! I think I got it, [ch_ren]."
    n "I shoot him a reassuring smile as I turn to face him at the door."
    n "I should've gotten used to his attentive and observant behaviour by now, but it still felt like a foreign side of him that I hadn't fully uncovered."
    n "Still, at least he wasn't stuttering as much anymore."

    show ren flushed at spop, center
    r "Ahaha… I know. Sorry."
    show ren happy at spop, center
    r "I just want you to be as comfortable as possible. So just… Treat this house like it's your own."
    y "Alright. Gotcha."
    n "He looks like he doesn't want to leave, and instead lingers in front of the door a little while longer."
    show ren sad at spop, center
    r "Are you sure there isn't anything else you'd need? Anything at all?"

    menu:
        "[rh_o]\"Can I get a goodnight kiss?\"[rh_c]":
            $ affection_ren += 1
            $ affection_teo += 1
            $ affection_olivia += 1
            $ affection_moth += 1
            show ren blushing at bpop
            r "U-Uh—!"
            n "Almost sheepishly, I dared to look up and gauge [ch_ren]'s reaction to my words."
            n "He seems to be taking it as best he can, judging from how bright red his cheeks and neck get — and the fact that he can't seem to look me in my eyes."
            y "[ch_ren]? Don't get all shy on me now—"
            n "Before I could finish my sentence, [ch_ren] was {b}already{/b} leaning down and pressing his soft lips against my own."
            n "I barely notice the way his hands gently hold my shoulder to keep me steady as his head tilts to the side."
            n "This kiss was brief and chaste, but it still made the both of us flustered."
            show ren flushed at spop, center
            r "I-Is that okay?"
            y "…Uh-huh?"
            show ren blushing at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
            r "Okay…! Good! I'm uh— I'm glad!"
            show ren flushed at bpop, center
            r "G-G-G-Goodnight!"
            play audio "audio/sfx/sprinting.ogg"
            hide ren with easeoutright
            n "Before I can even respond, he's already turning on his heels and speed walking towards his own room."
        "{image=14NWY symbol alt}  \"Can you sleep in my bed tonight?\"" if dlc_14nightswithyou_scenes == True and persistent.dlc_14nightswithyou == True and persistent.streamermode == False:
            show ren blushing at center with dissolve
            show ren blushing at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
            r "S-Sleep in your b—?!"
            show ren flushed at spop, center
            r "…"
            show ren blushing at spop, center
            r "Angel! Do you know what you're asking me— Wait, {i}are{/i} you asking me to… to—"
            show ren flushed at spop, center
            r "To…"
            n "Deciding to put him out of his misery, I answer his question by stepping closer towards his lanky frame and into his personal space."
            y "Yes, [ch_ren]. I want to spend a bit more time with you."
            y "I don't want to be lonely tonight."
            r "…Y'don't want to be lonely? I-I mean-! You're not sick of me yet?"
            n "[ch_ren]'s cheeks flush red as he awkwardly shuffles his weight from one foot to the other."
            n "I watch as he begins to pick at the ends of his sleeve — perhaps out of habit — before he notices his actions and stops."
            n "Bright blue eyes look down at me, and I could practically feel the hope radiating from his body."
            n "Deciding to take the initiative, I step {b}even closer{/b} to the pink-haired man and rest my hands against his sides."
            r "…[player_fl]-[ch_angel]?"
            jump day2_wahooscene
        "\"Can I sleep in your bed instead?\"" if dlc_14nightswithyou_scenes == False or persistent.dlc_14nightswithyou == False or persistent.streamermode == True:
            $ affection_ren += 1
            $ affection_jae += 1
            show ren blushing at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
            r "Y-You want to— In my room?!"
            n "Did I just say that?! I can't keep letting these intrusive thoughts win!"
            show ren flushed at spop, center
            r "…I don't mind, b-but what's wrong with the guest bedroom?"
            n "He peers behind my head to glance around the room behind me, before sheepishly meeting my gaze once more."
            y "Nothing's wrong! I just… I wanted to tease you a little bit, is all."
            y "Sorry. I don't really know why I said that."
            show ren happy at spop, center
            r "O-Oh! …I see. Haha~ Don't worry about it then."
            show ren flushed at spop, center
            r "{size=-6}And to be honest, I kinda enjoy it when you tease me.{/size}"
            show ren smirk at spop, center
            r "Well! If everything's okay, I guess I'll let you get some sleep then?"
            y "Y-Yeah, okay…"
            show ren neutral at spop, center
            r "Alright then…"
            n "Great, I successfully made the mood completely mortifying again."
            show ren happy at spop, center
            r "Goodnight, [ch_angel]. Sweet dreams."
            y "G-Goodnight."
            hide ren with dissolve
            n "I watch in silence as [ch_ren] turns on his heel and makes his way towards his own room down the hall."
        "\"What's behind that locked door?\"":
            $ d2_snooping = True
            $ persistent.d2_snooparound = True
            $ ren_decay += 1
            $ affection_ren -= 1
            $ affection_conan += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            show ren flushed at bpop
            r "The… The locked door? Ahaha… What door? Oh—"
            show ren blushing at spop, center
            r "Y-You mean the one at the end of the hallway?"
            n "All of a sudden, his timid persona is back again. Was he just nervous? What could he possibly be hiding in that room to make him act like this?"
            show ren frown at spop, center
            r "There's n-nothing in particular! Just… err…"
            show ren neutral at spop, center
            r "You see, I-I'm currently using it as a… s-storage room for all the furniture from my old place!"
            show ren sad at spop, center
            r "I-It's… It's really messy in there. I'd be embarrassed if you saw what's behind that door."
            y "Oh! Yeah, okay. That… actually makes a lot of sense…"
            n "Great, now I'm the person who threw accusations at someone kind enough to offer me a place to stay for the night."
            n "Still, it was nice to know that he {b}did{/b} own some kind of furniture."
            y "Sorry, I guess I was just really curious about it… Usually people don't leave the lights on behind locked doors."
            show ren flushed at spop, center
            r "Oh… Y-Yeah…"
            show ren blushing at spop, center
            r "I'd be happy to show you what's behind that door when it's not so… cluttered."
            show ren neutral at spop, center
            r "But… If that's all, then I guess I'll let you get some sleep. If you need anything, my room is just three doors down."
            y "Gotcha. G'night, [ch_ren]."
            show ren happy at spop, center
            r "Goodnight [ch_angel]. Sweet dreams."
            play audio "audio/sfx/walking.ogg"
            hide ren with dissolve
            n "I watch in silence as [ch_ren] turns on his heel and makes his way towards his own room down the hall."
        "\"No, I'm good. Thank you.\"":
            $ affection_violet += 1
            $ affection_elanor += 1
            show ren neutral at spop
            r "Alright then. If you need anything, my room is just three doors down. You don't even have to knock — just let yourself in, okay?"
            show ren happy at spop, center
            r "In fact, you can even share my bed if you—"
            y "Uh, okay… Gotcha. But I think I'll knock, just to be safe."
            show ren blushing at spop, center
            r "You {i}really{/i} don't have to. But alright."
            show ren happy at spop, center
            r "Well, if that's everything… I'll let you get some sleep now. Goodnight [ch_angel]. Sweet dreams."
            play audio "audio/sfx/walking.ogg"
            hide ren with dissolve
            n "I watch in silence as [ch_ren] turns on his heel and makes his way towards his own room down the hall."

    scene ren_spareroom_night
    show peffect
    play audio "audio/sfx/movement.ogg"
    with GlitchDissolve

    n "Shaking my head at his odd behaviour, I close the door behind me and slowly make my way towards the bed."
    n "I notice that the Haruko plushie [ch_ren] had bought earlier was sitting atop the sheets, and I gently bring it closer to my chest to give it a soft squeeze."
    n "So he really did buy this for me after all?"
    jump day2_plushieend

################################################################################
## MC APARTMENT BRANCH
################################################################################
label day2_angelapartment:
    scene oh_street_night
    play music "audio/bgm/Summer Memories.ogg" fadein 1 fadeout 1
    show ceffect
    show reffect
    with Fade(1.0, 1.0, 1.0)

    $ persistent.d2_visitangel = True
    $ location_conan = "home"
    $ location_jae = "home"
    $ location_leon = "home"
    $ location_teo = "random"
    $ location_olivia = "random"
    $ location_ren = "home"
    $ location_violet = "home"

    n "In the end, [ch_ren] ended up walking me back home."
    n "Yet despite being the one to hold the umbrella, he still got wet because he offered most of it to me."
    n "[ch_ren] {b}really was{/b} considerate, but it didn't stop me from feeling bad whenever I saw the wet patch on his shoulder."
    n "Eventually enough, my apartment entrance comes into view and I suddenly wished that time would slow down."
    n "I wasn't sure why, but I was enjoying my time with [ch_ren] — even though I still didn't know much about him."
    n "All that I {b}did{/b} know was that he was very attentive when it came to me, and that he was willing to put in the effort to get to know me better."

    if relationship_teo == "exboyfriend":
        n "Which, in hindsight, was far more effort than [ch_teo] ever put into our relationship. No matter how short-lived it was."
    else:
        n "It was honestly… very sweet seeing [ch_ren] be so considerate."
        n "He still came off a bit odd and eccentric at times, but that side of him was slowly starting to grow on me."

    n "Glancing back at the pink-haired man beside me once more, I watch as he casually twirls the umbrella in his grip and shoots me a playful smile."
    n "It seems as though he shared the same sentiment as me, judging by how his feet started slowing down the moment we ascended my apartment staircase."
    n "With a smile, I turn to face [ch_ren] — only to realise that he was already looking at me with an all-too-familiar soft grin."
    show ren sad at spop, center with dissolve
    r "So… here we are…"
    show ren blushing at spop, center
    r "Th-Thanks for going out with me today! I'm sorry it got cut short because of the weather…"
    show ren flushed at spop, center
    r "I really should've looked at the weather app before leaving, huh?"
    y "It's fine. Maybe we could try this again another time? Preferably on a day without rain."
    show ren happy at bpop, center
    r "Y-Yeah! I'd like that…"
    n "We stand around at the entrance for a while before I…"

    menu:
        "Lean in and kiss him":
            $ affection_ren += 1
            $ affection_moth += 1
            $ affection_jae += 1
            $ affection_olivia += 1
            $ first_kiss = True
            $ d2_renkiss = True
            show ren flushed at center with dissolve
            n "Before I can stop myself, I take a step closer to [ch_ren] and gently pull him closer by the front of his cardigan."
            n "He seems surprised at my actions with how wide his eyes get, but it doesn't stop me from leaning upwards and pressing a soft kiss against his lips."
            n "The taste of cherry lingers when I pull away, and I watch with slight amusement as [ch_ren]'s cheeks instantly flare a deep scarlet."
        "Lean in and kiss his cheek":
            $ affection_ren += 1
            $ d2_renkiss = True
            show ren flushed at center with dissolve
            n "Before I can stop myself, I take a step closer to [ch_ren] and gently pull him closer by the front of his cardigan."
            n "He seems surprised at my actions with how wide his eyes get, but it doesn't stop me from leaning upwards and pressing a soft kiss against his cheek."
            n "The smell of cherries and fresh linen lingers when I pull away, and I watch with slight amusement as [ch_ren]'s cheeks instantly flare a deep scarlet."
        "Thank him for walking you home":
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            show ren happy at center with dissolve
            y "Thanks for walking me home. You didn't have to, but I appreciate it."
            show ren happy at bpop, center
            r "Y-Yeah! Of course! N-No problem!"
            show ren smirk at bpop, center
            r "I had fun today. It's been a while since I've been to the beach walk, anyway."
            show ren happy at bpop, center
            r "I'm glad I got to go visit it again with you. E-Even if the weather had to come along and ruin it, ahaha."
            y "Yeah! I had fun too."
            jump day2_goinside
        "Enter your apartment without a word":
            $ affection_ren -= 1
            $ affection_violet += 1
            $ affection_teo += 1
            $ ren_decay += 1
            show ren sad at center with dissolve
            n "Almost abruptly, I turn around and start punching in the key code to enter my apartment complex."
            show ren frown at spop, center
            r "U-Um…"
            n "I can hear [ch_ren] stutter behind me, but I pay him no mind as the front door clicks open, and I rush inside."
            show ren blushing at spop, center
            r "Oh! Before you go— Th-This is for you!"
            n "Without another word, [ch_ren] shoves the bag he was holding into my arms with a forced smile."
            n "Peering inside, I notice the Haruko plushie I had been eyeing earlier."
            n "He really went out of his way to get this for me? Wow…"
            show ren flushed at spop, center
            r "W-Well then… I'll be going. G-Goodbye, Angel!"
            n "Before I could respond, [ch_ren] was {b}already{/b} turning on his heels and walking back the same way he came."
            play audio "audio/sfx/walking.ogg"
            jump day2_leaveren

    show ren blushing at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    r "…!"
    y "Thanks for walking me home."
    show ren flushed at spop, center
    r "U-Uh-huh…"
    n "I could almost see the steam rise from his head as he remains in his slouched-over position, so I awkwardly pat his chest to get him to loosen up."
    show ren blushing at bpop, center
    r "I-I mean, yeah! Of course! Don't mention it!"
    n "He almost bumps his head with the umbrella as he leans back, but remains close to my side."

    label day2_goinside:
    y "Well then…"
    n "Much like the first time I met him at the library, I awkwardly gesture to the door behind me as I try and find a way to excuse myself."
    n "Sometimes [ch_ren] {b}really{/b} made these kinds of situations difficult."
    y "I should head back inside now. And you should get out of this rain!"
    show ren sad at spop, center
    r "Oh! Y-Yeah! I probably should…"
    n "He still makes no sign of leaving, which made me wonder if he was waiting to make sure that I made it safely inside my apartment. As if to test that theory, I give him a small wave and turn on my heel."
    show ren blushing at spop, center
    r "Oh! Before you go— Th-This is for you!"
    play audio "audio/sfx/item.ogg"
    n "Without another word, [ch_ren] shoves the bag he was holding into my arms with a forced smile."
    n "Peering inside, I notice the Haruko plushie I had been eyeing earlier."
    n "He really went out of his way to get this for me? Wow…"
    show ren flushed at spop, center
    r "W-Well then… I'll be going. G-Goodbye, Angel!"
    play audio "audio/sfx/sprinting.ogg"
    hide ren with easeoutleft
    n "Before I could respond, [ch_ren] was {b}already{/b} turning on his heels and leaving back the same way he came."

    label day2_leaveren:
    scene oh_complex_night
    stop ambience fadeout 2.0
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/movement.ogg"
    show peffect
    with Fade(1.0, 1.0, 1.0)

    if d2_renkiss == True:
        n "With a warm and fuzzy feeling still inside me, I climb up the flight of stairs until I reach my floor."
        n "I highly doubt my landlord had fixed the elevator yet, if the caution tape was anything to go by."
        n "But it was difficult to focus on those things when all I could think about was [ch_ren]'s warmth lingering on my lips."
    else:
        n "Without looking back to see if [ch_ren] had left or not, I climb up the flight of stairs until I reach my floor."
        n "I highly doubt my landlord had fixed the elevator yet, if the caution tape was anything to go by."
        n "But it was difficult to focus on those things when all I could think about was the date I just went on with [ch_ren]."

    n "But a flash of white manages to pull me from my thoughts, and I notice [ch_violet] lingering near the stairwell entrance to our floor."
    play audio "audio/sfx/heels alt.ogg"
    show violet happy at spop, center with dissolve
    v "[ch_angel]! Hey! I'm guessing the weather put a fork in your plans too, huh?"
    n "She moves to unlock her door, and I notice how one of her potted plants had been moved to the busted window at the end of the hallway."
    n "I'm guessing [ch_violet] had moved it to make use of the free rain, and make it easier to water her plants without the effort."
    show violet smirk at spop, center
    v "Want to come in for a while? This weather is making me feel rather chilly…"
    show violet happy at spop, center
    v "I can brew some tea to warm us up if you'd like."
    y "Sorry, Vi. As much as I'd love to, my social battery is kinda drained by now…"
    show violet neutral at spop, center
    v "Oh, that's okay! I totally get it. You just need some time alone to unwind, right?"
    show violet happy at spop, center
    v "In that case, Carla over here is good company. She won't talk, but she'll listen to your problems without a complaint."
    play audio "audio/sfx/heels.ogg"
    show violet happy at left with easeinright
    n "She hands me a small bouquet made from an assortment of coloured tulips before waving me off and stepping into her apartment."
    n "The smell of lavender wafts out as she pokes her head out of the door, and the scent immediately calms my senses."
    show violet smirk at spop, left
    v "My offer still stands if you ever change your mind, though! Just knock, and I'll get the kettle running."
    show violet happy at spop, left
    v "Enjoy the rest of your evening, [ch_angel]. Toodles!"
    play audio "audio/sfx/heels alt.ogg"
    hide violet with moveoutleft
    n "Man, [ch_violet] really was something, huh?"

    scene angel_lounge_night
    show peffect
    play audio "audio/sfx/walking.ogg"
    play audio "audio/sfx/door.ogg"
    with GlitchDissolve

    $ status_olivia = False
    $ persistent.d2_killolivia = True

    n "Stepping into the comfort of my apartment, I discard my keys into the bowl and take off my shoes."
    n "Ignoring the awful squelching sound it makes, I try my best not to leave a puddle of water in my wake as I make my way into the lounge room."
    n "I pull out the Haruko plushie from the bag and set it on the couch, before I turn the television on and prepare myself for a much-needed shower."
    play music "audio/bgm/Lonely Doll.ogg" fadein 1 fadeout 1
    npc "—eaking news! The body of a young woman has been pulled from a dumpster on Cornel— *crrk!* —street, no more than five feet from the place she worked at—"
    npc "*crrk!* —ramedics say she suffered multiple blunt forces to her vital organs, as well as showing signs of stress and struggle."
    npc "Viewer— *crrk!* —creetion is advised, as these images contain scenes that may be trigg—"
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    n "All of a sudden, the TV turns into static, and I can only assume that it was caused by the storm."
    n "I didn't need to look outside the window to know that it had only gotten worse, and I wonder if [ch_ren] was going to be alright on the walk back to his apartment."
    n "Also… Who was the person on the TV?"
    n "The reporter seemed to be standing outside of a hardware store, which wasn't far from the pier [ch_ren] and I went to today."
    y "[damn!c], I really wanted to know more…"
    n "Despite that, I don't feel like taking any chances with this freak storm, so I quickly race to the bathroom before the power turns off next."

################################################################################
## ENGING SCENE (Angel's apartment)
################################################################################
label day2_angelending:
    scene angel_bedroom_night
    show peffect
    with GlitchDissolve

    n "With my body {b}finally{/b} free from the smell of rain, I let out a satisfied sigh as I slip into the comfort of my bed."
    n "I didn't even notice that I had brought my new plushie into my bedroom, but I bring it closer to my side and bury my face in all of its fluffiness."

    label day2_plushieend:
    n "The faintest hint of cherry and mint emits from the toy, and makes my mind drift to thoughts of that strange, pink-haired man once more."
    n "He was still as odd as usual, but some parts of him were starting to feel rather endearing."
    n "I noticed how he was no longer stuttering as much or acting as shy, and it made me wonder if we were getting closer."
    n "Now that I {b}really{/b} thought about it, how did I feel about [ch_ren]?"

    label day2_wahooend:
    menu:
        "[rh_o]I'm crushing on him[rh_c]":
            $ relationship_ren = "crush"
            $ ren_purity -= 1
            $ affection_ren += 10
            $ affection_moth += 1
            $ affection_olivia += 1
            n "Okay, so maybe I {b}did{/b} find him rather endearing and attractive."
            n "[ch_ren] was very considerate and attentive towards me during our date, and I could see myself wanting to go on another date in the near future."
            if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
                call DLC_day2_s5 from _call_DLC_day2_s5
            else:
                n "He certainly had boyfriend potential, but I still needed to work up the nerve to make it lead towards that direction."
                n "He seemed far too hesitant to do it himself, but it would've been nice to see him put more effort into it as well."
                n "Ah well, just knowing [ch_ren] wanted to spend the entire day with me is enough."
                n "Rolling onto my side, I hug the plushie closer so I can be surrounded by his comforting scent and slowly drift off to sleep."
        "I think I like him":
            $ relationship_ren = "like"
            $ affection_ren += 5
            $ affection_elanor += 1
            $ affection_conan += 1
            $ affection_jae += 1
            n "Okay, so I guess he {b}was{/b} kind of cute and endearing in his own way."
            n "[ch_ren] was very considerate and attentive towards me today, which I really liked, {b}and{/b} he even bought me a plushie without being asked."
            n "That instantly raises him from a four out of ten to a solid seven out of ten."
            n "[ch_ren] certainly had boyfriend potential, but things were still too awkward between us for it to lead in that direction."
            if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
                call DLC_day2_s6 from _call_DLC_day2_s6
            else:
                n "But still… It was nice to think about. {b}He{/b} was certainly nice to think about."
                n "Rolling onto my side, I hug the plushie closer so I can be surrounded by his comforting scent and slowly drift off to sleep."
        "I think he's alright":
            $ relationship_ren = "neutral"
            $ affection_ren += 1
            $ affection_leon += 1
            $ affection_kiara += 1
            n "What was there to say? We still didn't know each other that well, but he seemed very kind and considerate towards me."
            n "I feel like I just needed to get to know [ch_ren] better before I could decide on a strong opinion of him."
            if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
                call DLC_day2_s7 from _call_DLC_day2_s7
            else:
                n "Maybe we could get closer in the future? He'd have to actually {b}try{/b} and put the effort in though — because right now, it felt like I was doing all the work."
                n "Ah well, there was no point in me stressing over something trivial."
                n "Rolling onto my side, I hug the plushie closer and slowly drift off to sleep."
        "He's kind of creepy":
            $ relationship_ren = "dislike"
            $ affection_ren -= 10
            $ affection_violet += 1
            $ affection_teo += 1
            $ ren_decay += 1
            n "What was there to say? He still had that flippant personality of his going on, and he somehow knew all of my favourite things without asking me."
            n "That sounded like a grade-A creep to me, but I didn't have any solid proof to back up my theory."
            if persistent.dlc_14nightswithyou == True and rem_wahoo == True:
                call DLC_day2_s8 from _call_DLC_day2_s8
            elif d2_visitren == True:
                n "But I guess I shouldn't be calling him a creep when {b}I{/b} was the one who willingly agreed to go to his apartment — despite only knowing him for two whole days."
            else:
                pass
            n "There was also that break-in that [ch_violet] mentioned yesterday, but [ch_ren] didn't fit their description at all."
            n "Ah well. I shouldn't be concerning myself over this. I still had that new lock installed, so I doubt they'd want to come back."
            n "Rolling onto my side, I push those thoughts aside as I hug the plushie closer and slowly drift off to sleep."

    if unlockable == "meowdacted":
        $ ren_outfit = "meow"
        jump day2_ending_good
    else:
        $ ren_outfit = "normal"
        jump day2_ending_good

################################################################################
## EEUUUGHGHGUEGHEUSGH
################################################################################
label day2_ending_good:
    $ ending_good = "obtained"
    $ persistent.d2_ending_gooding = True
    jump pathpoint

label day2_deadend:
    $ persistent.deadendings += 1
    $ persistent.deadend2 = True
    $ persistent.d2_badending = True
    jump pathpoint