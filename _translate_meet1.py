import re, sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days\day 1 - meet 1.rpy"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Translation map: English dialog -> Thai translation
# Only translate lines that start with "    " (indented) and contain a character prefix + "text"
# Pattern: "    PREFIX \"English text\""
# Keep comment lines (starting with "    #") unchanged

translations = {
    # meetviolet section
    'n "With a grumble, I tug at the fabric of my coat before slamming the door shut with a little bit {b}too much{/b} force than necessary."':
    'n "พร้อมเสียงบ่นพึมพำ ฉันดึงผ้าเสื้อโค้ทของตัวเองก่อนจะปิดประตูดังปังด้วยแรงที่{b}มากไปหน่อย{/b}"',

    'n "Even trying to insert my key came with a bit of a struggle, and I had to fight the urge to yell in frustration as I attempted to lock my door."':
    'n "แค่จะสอดกุญแจเข้าก็ยากลำบากแล้ว ฉันต้องอดกลั้นไม่ตะโกนออกไปด้วยความหงุดหงิดขณะพยายามล็อกประตู"',

    'y "Seriously… When will that lazy {i}bum{/i} of a landlord do something about this?"':
    'y "พูดจริงๆ… เจ้าของที่{i}ขี้เกียจ{/i}คนนี้จะทำอะไรสักทีมั้ย?"',

    'y "I swear I\'ve complained about this at least {i}four{/i} times this month…"':
    'y "ฉันสาบานว่าเดือนนี้ฉันร้องเรียนเรื่องนี้มาแล้วอย่างน้อย{i}สี่{/i}ครั้งแล้ว…"',

    'v "Oh! Hey there [ch_angel]! Looking good!"':
    'v "โอ้! สวัสดีค่ะ [ch_angel]! ดูดีนะวันนี้!"',

    'n "My neighbour — [ch_violet] — practically beams at me while she fishes through her pockets for her own apartment key."':
    'n "เพื่อนบ้านของฉัน — [ch_violet] — ยิ้มร่าไปหมดทั้งตัวขณะควานหากุญแจอพาร์ตเมนต์ในกระเป๋า"',

    'n "Resting on her hip was {i}yet another{/i} potted plant, and I found myself wondering where she was going to put it this time."':
    'n "ตรงสะโพกของเธอมีต้นไม้กระถาง{i}อีกต้น{/i}วางอยู่ ฉันเลยนึกสงสัยว่าครั้งนี้เธอจะเอาไปวางที่ไหนอีก"',

    'n "I was almost {b}entirely{/b} convinced that her whole apartment had been turned into a greenhouse at this point, considering how her balcony was practically filled to the brim with different kinds of plants, greenery, and other various kinds of flora."':
    'n "ฉัน{b}แทบจะมั่นใจ{/b}แล้วว่าอพาร์ตเมนต์ของเธอคงกลายเป็นเรือนกระจกไปแล้ว เพราะระเบียงของเธอแน่นไปด้วยต้นไม้นานาพันธุ์จนล้น"',

    'n "But I wasn\'t about to complain or anything. The fragrance that wafted in with the wind always smelled floral and earthy, and it did well to mask the smell of smoke and burnt food whenever I tried to cook."':
    'n "แต่ฉันก็ไม่ได้จะว่าอะไร กลิ่นหอมที่ลอยตามลมเข้ามามักหอมอ่อนๆ ของดอกไม้และดิน แถมยังช่วยกลบกลิ่นควันและของไหม้ตอนฉันทำกับข้าวได้ดีเลย"',

    'v "Hey, your outfit is just my style! You look so cute!"':
    'v "เฮ้ ชุดของคุณเป็นสไตล์ที่ฉันชอบเลยนะ! น่ารักมาก!"',

    'v "Hey, isn\'t your top from that high-end brand? I didn\'t know we had similar taste in fashion!"':
    'v "เฮ้ เสื้อตัวนี้จากแบรนด์ดังใช่มั้ย? ฉันไม่รู้นะว่าเรามีรสนิยมแฟชั่นคล้ายกัน!"',

    'v "Love the shoes, by the way! The colour reeeeally compliments your aura this morning."':
    'v "รองเท้าก็ชอบนะ! สีมันเข้ากับออร่าของคุณช่างเป็นตอนเช้าวันนี้จริงๆ"',

    'v "You\'ll have to let me peek inside your closet some day. I\'ve been looking for some new inspiration lately."':
    'v "สักวันต้องให้ฉันแวะดูตู้เสื้อผ้าในตู้ของคุณบ้างนะ ช่วงนี้ฉันกำลังหาไอเดียใหม่ๆ อยู่"',

    'v "Especially with winter right around the corner… Ahh, I\'m getting excited just thinking about it! Oh—"':
    'v "ยิ่งฤดูหนาวกำลังจะมาถึงแล้วด้วย… อาาา คิดแล้วมันตื่นเต้นเลย! โอะ—"',

    'extend " But back to you!"':
    'extend " ว่าแต่กลับมาที่คุณนะ!"',

    'n "Her voice pulls me away from my thoughts, and I notice how the growing smile on her face doesn\'t seem to falter."':
    'n "เสียงของเธอดึงฉันกลับจากภวังค์ แล้วฉันก็สังเกตเห็นรอยยิ้มที่ขยายใหญ่ขึ้นบนใบหน้าเธอไม่ได้เลือนหายไปเลย"',

    'n "Wow, [ch_violet] sure was extra chirpy this morning… I wonder if she\'d let me borrow some of that energy?"':
    'n "ว้าว [ch_violet] สดใสเป็นพิเศษจริงๆ ตอนเช้านี้… สงสัยเธอจะยืมพลังงานให้ฉันบ้างมั้ย?"',

    'n "In response, I shoot my neighbour a grin of my own, and it was apparently enough to brighten her mood {b}even more{/b} than it was already."':
    'n "ฉันยิ้มกว้างตอบเพื่อนบ้านบ้าง แล้วมันก็ดูเหมือนจะทำให้อารมณ์ของเธอ{b}ดีขึ้นไปอีก{/b}"',

    'v "Oh, this? It {i}maaaaaay or may not{/i} be another plant I impulsively bought from work… Heehee, isn\'t she beautiful?"':
    'v "โอ้ ต้นนี้นะ? {i}อาจจะ{/i}เป็นต้นไม้ที่ฉันซื้อมาอย่างหุนหันจากที่ทำงานอีกต้น… ฮีฮี น่ารักใช่มั้ย?"',

    'n "She briefly pulls away from her lock to gently pet the succulent plant. The look on her face is soft now, and I couldn\'t help but stare."':
    'n "เธอหันจากกุญแจมาลูบต้นไม้สดในมือเบาๆ สีหน้าของเธอดูนุ่มนวล ฉันเลยจ้องมองไม่วางตา"',

    'v "Hmm? {i}Oh!{/i} Yeah, this is Charlie! I\'m thinking of putting her next to Whitney."':
    'v "หรือ? {i}โอ้!{/i} อ๋อ นี่ Charlie ค่ะ! ฉันกำลังคิดจะวางเธอข้าง Whitney"',

    'n "Great, she names her plants."':
    'n "ดีมาก เธอตั้งชื่อต้นไม้เลย"',

    'v "Yeah, it\'s nice to see you too! I\'d usually still be at the flower shop at this time, so it\'s nice to finally be able to catch up with you like this — {i}especially{/i} when our schedules align!"':
    'v "ใช่ ฉันก็ดีใจที่ได้เจอคุณเหมือนกัน! ปกติฉันคงยังอยู่ที่ร้านดอกไม้ตอนนี้ ก็เลยดีใจที่ได้คุยกับคุณแบบนี้สักที — {i}ยิ่ง{/i}ตอนที่ตารางเราตรงกันด้วย!"',

    'v "Speaking of! You should stop by my place the next time you\'re free. I\'d love to introduce you to this little guy\'s family."':
    'v "พูดถึงเรื่องนี้! คราวหน้าว่างแวะมาที่บ้านฉันบ้างนะ ฉันอยากพาคุณไปรู้จักครอบครัวของตัวน้อยนี่จัง"',

    'v "That\'s okay, don\'t let me stop you!"':
    'v "ไม่เป็นไรค่ะ ไปเลยไปเลย ฉันไม่ขวางหรอก!"',

    'n "She gives me a soft smile and waves her free hand before focusing her attention back on her door. That is, until she suddenly jolts as if she just remembered something and swivels on her heels to look at me once more."':
    'n "เธอยิ้มนุ่มๆ ให้ฉันแล้วโบกมือข้างที่ว่างก่อนจะหันไปสนใจประตูของเธอต่อ จนกระทั่งเธอสะดุ้งขึ้นมาราวกับนึกอะไรได้ แล้วหันส้นเท้ากลับมามองฉันอีกครั้ง"',

    'v "Oh, I almost forgot! I\'ve been meaning to ask you this, but… When were you going to tell me that you were seeing someone?"':
    'v "โอ้ ฉันลืมไปแล้ว! ฉันอยากจะถามคุณมานานแล้วว่า… คุณจะบอกฉันสักทีไหมว่าคุณกำลังคบใครอยู่?"',

    'y "{i}…Huh?{/i}"':
    'y "{i}…อะไรนะ?{/i}"',

    'n "A knowing look pulls at her features as [ch_violet] continues to fiddle with the lock on her door."':
    'n "สีหน้ารู้ทันปรากฏขึ้นบนใบหน้าเธอขณะที่[ch_violet]ยังคงแก้กุญแจประตูต่อไป"',

    'y "What are you talking about?"':
    'y "คุณพูดเรื่องอะไรอยู่อ่ะ?"',

    'v "{i}C\'mooon!{/i} Don\'t act like you {i}didn\'t{/i} just have a guy over last night. I saw him leaving when I took Cathy out for a walk."':
    'v "{i}โอ้ย!{/i} อย่าทำเป็นว่าคุณ{i}ไม่ได้{/i}มีผู้ชายมาค้างคืนเมื่อคืนนะ ฉันเห็นเขาออกไปตอนที่ฉันพา Cathy ออกไปเดินเล่น"',

    'n "I\'d be more worried about my neighbour taking her plants — {b}named{/b} plants — out on a walk at night, but the thought of someone leaving my apartment seemed to set off {b}way more{/b} alarm bells."':
    'n "ฉันน่าจะเป็นห่วงเพื่อนบ้านที่พาต้นไม้ — ต้นไม้ที่{b}มีชื่อ{/b} — ออกไปเดินกลางคืนมากกว่า แต่ความคิดที่ว่ามีคนออกจากอพาร์ตเมนต์ของฉันกลับ{b}กระตุ้นสัญญาณเตือน{/b}มากกว่า"',

    'n "I give [ch_violet] a concerned look, and she picks up on it almost immediately."':
    'n "ฉันมอง[ch_violet]ด้วยสีหน้ากังวล เธอก็รับรู้ได้ทันทีเลย"',

    'v "…You don\'t remember? Don\'t tell me you were drunk or something!"':
    'v "…คุณไม่จำเหรอ? อย่าบอกนะว่าคุณเมาหรืออะไรงั้น!"',

    'n "With a huff, she gives up on trying to unlock her door (it seemed as though we both shared the same problem with our apartment locks) and places her potted plant on the ground before slowly making her way towards me."':
    'n "พร้อมเสียงงึมงำ เธอยอมแพ้การแก้กุญแจประตู (ดูเหมือนเราจะมีปัญหาเรื่องล็อกอพาร์ตเมนต์เหมือนกัน) แล้ววางต้นไม้กระถางลงบนพื้นก่อนจะเดินตรงมาหาฉันช้าๆ"',

    'v "Tall guy?"':
    'v "ผู้ชายตัวสูง?"',

    'extend " Wearing a dark slasher hoodie? "':
    'extend " ใส่ฮู้ดี้สีเข้ม? "',

    'extend "Really into alternative fashion with the crazy amount of belts and loops wrapped around his leg?"':
    'extend "แต่งตัวแฟชั่นเทิร์นๆ มีสายเข็มขัดกับหูหิ้วพันรอบขาเยอะมาก?"',

    'extend "Probably into either alt fashion {i}or{/i} bondage with the crazy amount of belts and loops wrapped around his leg?"':
    'extend "น่าจะเป็นแฟชั่นเทิร์น{i}หรือ{/i}บอนเดจ กับสายเข็มขัดกับหูหิ้วพันรอบขาเยอะมากนั่นแหละ?"',

    'v "Ring any bells?"':
    'v "นึกอะไรออกมั้ย?"',

    'y "Err… no? Last night I was just catching up on some tv shows and talking with my friend."':
    'y "เอ่อ… ไม่อ่ะ? เมื่อคืนฉันแค่ดูทีวีที่ค้างไว้แล้วคุยกับเพื่อนเฉยๆ"',

    'y "No one came here, even if they did, I would\'ve heard them. My place isn\'t really that big anyway."':
    'y "ไม่มีใครมาที่นี่หรอก ถ้ามาจริงฉันก็คงได้ยิน บ้านฉันก็ไม่ได้ใหญ่อะไรขนาดนั้น"',

    'v "Really? But I was so sure it was your door…"':
    'v "จริงเหรอ? แต่ฉันแน่ใจนะว่าเป็นประตูของคุณ…"',

    'n "A hand rests on her cheek in a thinking manner before she pouts up at me, seemingly giving in… for now."':
    'n "เธอวางมือบนแก้มทำท่าครุ่นคิดก่อนจะมองฉันด้วยสีหนงงอลง เหมือนจะยอมแพ้… ชั่วคราว"',

    'v "Well… alright then. Maybe it was somebody else\'s apartment? I mean, it\'s always so dark in these hallways at night. Honestly… What is our landlord doing?"':
    'v "อ้าว… งั้นก็แล้วแต่ คงเป็นอพาร์ตเมนต์ของคนอื่นมั้ง? ตอนกลางคืนทางเดินมันก็มืดอยู่แล้ว พูดจริงๆ… เจ้าของที่เราทำอะไรอยู่อ่ะ?"',

    'v "Would you mind if I check in with security downstairs later? It\'d give me some peace of mind."':
    'v "คุณว่าไหมถ้าฉันไปถามรปภ. ข้างล่างทีหลัง? จะได้สบายใจหน่อย"',

    'y "Yeah, that\'s fine."':
    'y "อ่อ ไม่เป็นไร"',

    'v "Alright then. Thank you, [ch_angel]."':
    'v "งั้นก็ตกลง ขอบคุณนะคะ [ch_angel]"',

    'v "{i}Welp!{/i} I got some plants to water and some MMOs to raid in, so…"':
    'v "{i}โอเค!{/i} ฉันมีต้นไม้ต้องรดน้ำและมีดันเจี้ยน MMO ต้องบุก งั้น…"',

    'n "[ch_violet] lets out one last huff before she picks up her plant (what did she name this one again?) and goes back to unlocking her door."':
    'n "[ch_violet] งึมงำออกมาอีกครั้งก่อนจะหยิบต้นไม้ขึ้นมา (ต้นนี้เธอตั้งชื่อว่าอะไรนะ?) แล้วกลับไปแก้กุญแจต่อ"',

    'v "Good talk, I guess! Even if it {i}was{/i} kinda awkward, hee hee."':
    'v "คุยกันสนุกดีนะ! แม้มัน{i}จะ{/i}อึดอัดไปหน่อย ฮีฮี"',

    'y "Uh, yeah… Sure. See ya later, Vi."':
    'y "เอ่อ อ๋อ… ครับ แล้วเจอกันใหม่นะ Vi"',

    'n "Slipping past my neighbour and into the cramped hallway, I quickly make for the stairs — when will they fix that broken elevator? — and break into a slight jog."':
    'n "ลัดผ่านเพื่อนบ้านเข้าไปในทางเดินแคบๆ ฉันรีบเดินไปหาบันได — จะซ่อมลิฟต์พังซักทีมั้ย? — แล้วออกวิ่งเบาๆ"',

    'n "Thankfully the weather was rather cool today, and the shoes I chose weren\'t going to leave me with blisters by the time I reached the library."':
    'n "โชคดีที่อากาศวันนี้เย็นสบาย และรองเท้าที่ฉันเลือกก็คงไม่ทำให้เท้าเป็นแผลพุพองตอนถึงห้องสมุด"',

    # meetelanor section
    'n "The smell of old paper, coffee, and soft incense floods my senses as I step through the library\'s glass doors."':
    'n "กลิ่นของกระดาษเก่า กาแฟ และกลิ่นหอมเบาๆ โชยเข้าจมูกฉันทันทีที่ก้าวผ่านประตูกระจกของห้องสมุด"',

    'n "The melodic chimes alert the woman at the reception desk of my arrival, and I watch as she tucks a strand of stray blonde hair behind her ear as she turns around to greet me."':
    'n "เสียงกริ่งเพราะๆ แจ้งเตือนผู้หญิงที่เคาน์เตอร์รับแขกว่าฉันมาถึง ฉันเห็นเธอเกล้าผมบลอนด์ที่หลุดมาเสียบไว้หลังหูก่อนจะหันมาทักทาย"',

    'y "Good morning, [ch_elanor]."':
    'y "สวัสดีตอนเช้าครับ [ch_elanor]"',

    'e "Oh!"':
    'e "โอ้!"',

    'n "She looks surprised for some reason before her expression morphs into a soft smile, and she beckons me closer with a nod of her head."':
    'n "เธอดูประหลาดใจสักพักก่อนสีหน้าจะเปลี่ยนเป็นรอยยิ้มนุ่มๆ แล้วพยักหน้าเรียกฉันเข้าไปใกล้"',

    'n "[ch_elanor] is one of my co-workers here at Corland Bay Library, and one of the {b}very few{/b} people here who actually gets the work done."':
    'n "[ch_elanor] เป็นหนึ่งในเพื่อนร่วมงานของฉันที่ห้องสมุด Corland Bay และเป็นหนึ่งใน{b}ไม่กี่คน{/b}ที่ทำงานจริงจัง"',

    'n "And although she\'s notorious for being rather scatterbrained, she more than makes up for it with her caring and doting attitude towards everyone."':
    'n "ถึงเธอจะมีชื่อเสียงเรื่องขี้ลืม แต่เธอชดเชยด้วยนิสัยที่ใส่ใจและเอาใจใส่ทุกคนได้มากกว่าพอ"',

    'n "But her nurturing personality can get rather… overbearing at times, and I often find myself having to step away to get some breathing room."':
    'n "แต่บุคลิกที่เอาใจใส่ของเธอบางครั้งก็… มากไปหน่อย ฉันมักต้องแยกตัวไปหายใจบ้าง"',

    'n "Nevertheless, she\'s charming to work with, and I appreciate her always looking out for me. After all, who knows what my sleeping schedule would\'ve looked like without her help."':
    'n "ยังไงซะ เธอก็น่ารักที่ได้ทำงานด้วย และฉันก็ขอบคุณที่เธอคอยดูแลฉัน ใครจะรู้ล่ะว่าตารางการนอนของฉันจะเป็นยังไงถ้าไม่มีเธอช่วย"',

    'e "[ch_angel]! Just on time. I printed out your— Wait… {i}where did I—?{/i}"':
    'e "[ch_angel]! มาถูกเวลาเลย ฉันพิมพ์เอกสารของคุณ— เดี๋ยว… {i}ฉันเอาไปไว้ไหนนะ?{/i}"',

    'n "Her expression turns into a slight panic as she spins on her heels, and I silently watch with amusement as she shuffles through the various books and stacks of papers lining her desk."':
    'n "สีหน้าเธอเปลี่ยนเป็นอาการตื่นเล็กน้อยขณะหันส้นเท้ากลับ ฉันเงียบๆ มองด้วยความขบขันขณะเธอควานหาไปตามหนังสือและกองกระดาษบนโต๊ะ"',

    'e "Where did I leave it?"':
    'e "ฉันเอาไว้ไหนนะ?"',

    'e "Ah! Here it is!"':
    'e "อ๋อ! อยู่นี่เอง!"',
}

# Apply translations
applied = 0
skipped = 0
new_lines = []
for line in lines:
    stripped = line.rstrip("\n")
    # Try to match dialog lines (indented, with character prefix)
    # Pattern: "    PREFIX "text""
    m = re.match(r'^    (\w+) "(.*)"$', stripped)
    if m:
        prefix = m.group(1)
        text = m.group(2)
        full_key = f'{prefix} "{text}"'
        if full_key in translations:
            new_line = f'    {translations[full_key]}"\n'
            # Need to reconstruct properly
            thai_text = translations[full_key]
            # thai_text already has prefix + " text"
            new_line = f'    {thai_text}\n'
            new_lines.append(new_line)
            applied += 1
            continue
    new_lines.append(line)
    skipped += 1

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Applied: {applied}")
print(f"Skipped: {skipped}")
