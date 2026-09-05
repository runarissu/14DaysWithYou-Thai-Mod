import re, sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days\day 1 - meet 1.rpy"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

translations = {
    # meetelanor continued
    'n "Spinning around once more, [ch_elanor] comes back and hands me a sheet of paper with the word \\"SCHEDULE\\" printed in big, bold letters. I take it from her grasp and give the sheet a once-over."':
    'n "หันกลับมาอีกครั้ง [ch_elanor] เดินกลับมายื่นกระดาษให้ฉัน มีคำว่า \\"SCHEDULE\\" พิมพ์ด้วยตัวอักษรตัวใหญ่ๆ ฉันรับมามาดูสักครู่"',

    'n "Well, it looks like I\'m going to be busy for the next few weeks… But I guess [ch_elanor] doesn\'t seem to share the same disdain as me, judging from the playful look plastered on her face."':
    'n "อืม ดูเหมือนฉันจะยุ่งอยู่สักสองสามสัปดาห์… แต่ที่ทำงานดูเหมือนจะไม่ได้รู้สึกแบบเดียวกับฉันเลย จากสีหน้าเจ้าเล่ห์ของเธอ"',

    'e "{i}Sooooo?{/i} How does it feel to no longer be the one in charge of stacking books all day long?"':
    'e "{i}แล้วไง?{/i} รู้สึกยังไงบ้างที่ไม่ต้องเป็นคนจัดหนังสือตลอดทั้งวันแล้ว?"',

    'e "Although… You\'ll still have to work the front desk from time to time though. {i}Unfortunately{/i}."':
    'e "แม้ว่า… คุณก็ยังต้องมานั่งเคาน์เตอร์บ้างเป็นบางครั้งนะ {i}น่าเสียดายจริงๆ{/i}"',

    'n "I offer a weak smile at her words before rounding the corner and placing my bag under the desk. And as I begin to pull out some of my belongings, the front door chimes again, letting everyone know that another patron has come in."':
    'n "ฉันยิ้มแหยๆ ให้เธอก่อนจะเดินไปวางกระเป๋าใต้โต๊ะ แล้วพอฉันเริ่มหยิบของออกมา เสียงกริ่งประตูก็ดังขึ้นอีก แจ้งให้ทราบว่ามีลูกค้าเข้ามาใหม่"',

    'n "Figuring [ch_elanor] has it all covered, I leave the customer to her as I go back to preparing everything for the day."':
    'n "คิดว่า[ch_elanor]คงจัดการได้แล้ว ฉันเลยปล่อยให้เธอดูแขกเอง ส่วนฉันก็กลับไปเตรียมงานประจำวันต่อ"',

    'n "But as I turn around to check on her, I notice that she had {b}already{/b} finished greeting the customer and was on her way back to her own desk across from mine."':
    'n "แต่พอฉันหันไปดู ก็พบว่าเธอ{b}จบ{/b}การทักทายลูกค้าแล้ว และกำลังเดินกลับไปโต๊ะตัวเองที่อยู่ตรงข้ามฉัน"',

    'n "As if sensing my gaze, she spins around in her office chair and flashes me a teasing grin."':
    'n "ราวกับรู้สึกถึงสายตาของฉัน เธอหมุนเก้าอี้กลับมาแล้วยิ้มแซวให้ฉัน"',

    'e "Looks like {i}he\'s{/i} back again."':
    'e "ดูเหมือน{i}เขา{/i}จะมาอีกแล้ว"',

    'n "[ch_elanor] gives a soft chuckle as she inclines her head in the direction of the person she was talking about."':
    'n "[ch_elanor] หัวเราะเบาๆ แล้วเอียงหัวไปทางคนที่เธอพูดถึง"',

    'e "You know, that new guy. I don\'t know when he started showing up here in the Bay, but he always comes in and rents out the books you recommend on the display window."':
    'e "คุณก็รู้นะ ผู้ชายคนใหม่นั่น ฉันไม่รู้ว่าเขาเริ่มมาตอนไหน แต่เขามาทุกทีแล้วก็ยืมหนังสือที่คุณแนะนำในตู้จัดแสดง"',

    'e "And if I didn\'t know any better, I\'d say he has a little crush on you."':
    'e "และถ้าฉันไม่รู้เรื่องเลย ฉันคงว่าเขาแอบชอบคุณอยู่"',

    'e "Especially with that outfit! I don\'t know about him, but I think that blazer looks great on you!"':
    'e "ยิ่งกับชุดนั้นด้วย! ฉันไม่รู้เรื่องเขาหรอก แต่ฉันว่าเบลเซอร์ตัวนั้นเหมาะกับคุณมาก!"',

    'e "Especially with that outfit! Honestly, the laid-back look makes {i}me{/i} jealous. Maybe I shouldn\'t have worn heels today…"':
    'e "ยิ่งกับชุดนั้นด้วย! พูดตรงๆ ลุคสบายๆ แบบนั้นทำให้{i}ฉัน{/i}อิจฉาเลย ฉันไม่น่าใส่ส้นสูงมาวันนี้…"',

    'e "Especially with that outfit you\'ve got on! It makes you look rather [gorgeous], so I can\'t really fault him for staring."':
    'e "ยิ่งกับชุดที่คุณใส่ด้วย! มันทำให้คุณดู[gorgeous]เลย ฉันเลยไม่ค่อยว่าเขาที่จ้องมองได้"',

    'e "Because he {i}was{/i} staring."':
    'e "เพราะเขา{i}กำลัง{/i}จ้องมองอยู่"',

    'extend " {i}A lot{/i}."':
    'extend " {i}เยอะมาก{/i}"',

    'n "Snorting, I push [ch_elanor]\'s office chair so that she\'s facing the other way and focus my attention {i}back{/i} to the papers in front of me."':
    'n "ฉันเสียงจาม ผลักเก้าอี้ของ[ch_elanor]ให้หันไปทางอื่น แล้วโฟกัส{i}กลับ{/i}ไปที่เอกสารตรงหน้า"',

    'n "What was with everyone today? Always smiling, gossiping about other people, and meddling in business that wasn\'t their own."':
    'n "วันนี้คนทั้งนั้นเลย ยิ้มกันไม่หยุด นินทาคนอื่น แล้วก็ยุ่งกับเรื่องที่ไม่เกี่ยวกับตัวเอง"',

    'n "It was bad enough that I had to deal with a potential intruder — but I doubt my deadbeat landlord was going to do anything about it."':
    'n "ฉันมีเรื่องคนแปลกหน้าที่อาจจะบุกขึ้นมาพอแล้ว — แต่เจ้าของที่ขี้เกียจของฉันคงไม่ทำอะไรหรอก"',

    'n "I might need to buy a stronger lock on my way home from work… Maybe even some kind of alarm system. But would the stores still be open by then?"':
    'n "ฉันอาจต้องซื้อกุญแจที่แน่นกว่านี้ระหว่างทางกลับ… หรือไม่ก็ระบบเตือนภัยอะไรสักอย่าง แต่ร้านคงยังเปิดอยู่มั้ย?"',

    'n "All of a sudden, I get pulled backwards as [ch_elanor] playfully wheels my chair around and leans over my shoulder to softly speak into my ear."':
    'n "ทันใดนั้นฉันถูกดึงไปข้างหลัง [ch_elanor] หมุนเก้าอี้ฉันเล่นๆ แล้วเอียงตัวมากระซิบข้างหูฉันเบาๆ"',

    'e "Would you look at that… {i}Loverboy{/i} in aisle eight needs some help, it seems."':
    'e "ดูสิ… {i}หนุ่มจี้{/i}ที่แถวแปดดูเหมือนจะต้องการความช่วยเหลือ"',

    'n "She nods in the direction of the red light flashing above the bookshelves, signalling to the staff that someone in that row needed assistance."':
    'n "เธอพยักหน้าไปทางไฟแดงที่กระพริบเหนือชั้นหนังสือ ซึ่งเป็นสัญญาณบอกพนักงานว่ามีคนต้องการความช่วยเหลือในแถวนั้น"',

    'n "With a sigh, I reluctantly stand up and make my way over. I already knew for a fact that [ch_elanor] wasn\'t going to go help them herself, so I begrudgingly begin to make my way towards aisle eight alone."':
    'n "พร้อมเสียงถอนหายใจ ฉันลุกขึ้นอย่างไม่เต็มใจแล้วเดินไป ฉันรู้อยู่แล้วว่า[ch_elanor]คงไม่ไปช่วยเอง ฉันเลยเดินไปแถวแปดอย่างจำใจ"',

    'n "I knew better than to glance back at her, though, knowing fully well that my teasing co-worker would be sporting the {b}biggest{/b} grin on her face at my misfortune."':
    'n "ฉันรู้ดีว่าไม่ควรหันไปมองเธอ เพราะรู้ว่าเพื่อนร่วมงานตัวแสบคนนี้คงกำลังยิ้ม{b}กว้างสุด{/b}กับเคราะห์ร้ายของฉัน"',

    # meetren section
    'n "Ducking around the corner and into the aisle, I was immediately met with a broad backside that was covered by what had to be the {b}comfiest{/b} looking cardigan I\'d ever seen."':
    'n "ลัดเลาะมุมเข้าไปในแถว สิ่งแรกที่ฉันเห็นคือหลังกว้างที่ห่ออยู่ในเสื้อการ์ดิแกนที่ดู{b}นุ่มสบาย{/b}ที่สุดเท่าที่ฉันเคยเห็น"',

    'n "The person whom it belonged to, however, hadn\'t seemed to notice me yet, so I awkwardly clear my throat and absent-mindedly shift my weight from one foot to the other."':
    'n "แต่เจ้าของเสื้อดูเหมือนยังไม่สังเกตเห็นฉัน ฉันเลยไอแก้เขินแล้วยืนเปลี่ยนเท้าถ่ายน้ำหนักไปมาอย่างไม่เป็นธรรมชาติ"',

    'y "{i}Ahem—!{/i}"':
    'y "{i}อืม—!{/i}"',

    'rpc "{size=+10}{i}…Ah—!{/i}{/size}" with vpunch':
    'rpc "{size=+10}{i}…อะ—!{/i}{/size}" with vpunch',

    'n "He seems to jump at the sudden noise before sheepishly turning around to face me. Immediately, I was taken aback by his soft demeanour, doe-like eyes, and imposing height."':
    'n "เขาดูเหมือนจะสะดุ้งกับเสียงก่อนจะหันมาหาฉันอย่างเขินอาย ทันใดนั้นฉันก็ตกตะลึงกับท่าทางอ่อนโยน ดวงตาคล้ายกวาง และส่วนสูงที่สูงร่มของเขา"',

    'n "So {i}this{/i} was the guy who always rented out my recommended books on the display window, huh? He definitely fit the aesthetic of a cosy literature-lover needing a good book."':
    'n "งั้น{i}นี่{/i}คือคนที่ยืมหนังสือแนะนำจากตู้จัดแสดงตลอดเหรอ? เขาดูเหมาะกับลุคคนรักวรรณกรรมที่อบอุ่นและกำลังหาหนังสือดีสักเล่มจริงๆ"',

    'n "His pink hair also reminded me of Haruko, an anime character I had recently been obsessing over with [ch_moth] during our late-night video calls. In fact, even the overall cut and style appeared vaguely similar to his…"':
    'n "ผมสีชมพูของเขาทำให้ฉันนึกถึง Haruko ตัวละครอนิเมะที่ฉันกับ[ch_moth]กำลังเมาอยู่ช่วงนี้ ตอนคุยกันทางวิดีโอคอลดึกๆ จริงๆ ทรงผมก็ดูคล้ายกัน…"',

    'n "But then again, this hairstyle could\'ve been trending right now or something, and I just so happened to be the last to know about it."':
    'n "แต่อีกอย่าง ทรงผมแบบนี้อาจจะกำลังเป็นเทรนด์ก็ได้ แล้วฉันก็เพิ่งรู้เป็นคนสุดท้าย"',

    'n "But… Now that I {b}really{/b} had a good look at him — which proved difficult considering his towering height — this stranger also seemed to bear a near {b}picture-perfect{/b} resemblance to the male lead from this webcomic I was reading."':
    'n "แต่… ตอนที่ฉันมองเขา{b}จริงๆ{/b} — ซึ่งยากเพราะเขาสูงมาก — คนแปลกหน้าคนนี้ก็ดูเหมือนพระเอกในเว็บตูนที่ฉันกำลังอ่านอยู่{b}เป๊ะ{/b}"',

    'n "It was called \\"Always with you\\", and it involved the main character meeting the love of [their] life at a—"':
    'n "ชื่อเรื่อง \\"Always with you\\" เนื้อเรื่องเกี่ยวกับพระเอกที่ได้พบกับรักแท้ของ[their]ที่—"',

    'n "As if noticing my spaced-out look, the stranger absent-mindedly scratches at his jaw while he waits for me to snap out of my thoughts. In fact, I had been so distracted that I didn\'t even realise that he had been muttering quietly to himself."':
    'n "เหมือนสังเกตเห็นสีหน้าเหม่อลอยของฉัน คนแปลกหน้าเกาคางไปมาอย่างเผลอขณะรอให้ฉันฟื้นจากภวังค์ จริงๆ ฉันเหม่อมากจนไม่รู้เลยว่าเขากำลังพึมพำอะไรกับตัวเอง"',

    'rpc "{size=-6}Okay, fox-feet… Make sure your ears aren\'t showing…{/size}"':
    'rpc "{size=-6}โอเค หูจิ้งจอก… ระวังอย่าให้หูโผล่นะ…{/size}"',

    'rpc "{size=-6}Woah… You look…{/size}"':
    'rpc "{size=-6}ว้าว… คุณดู…{/size}"',

    'rpc "{size=-6}But I thought you preferred softer clothing…? That\'s why I…{/size}"':
    'rpc "{size=-6}แต่ฉันคิดว่าคุณชอบเสื้อผมนุ่มๆ ไม่ใช่เหรอ…? ก็เลย…{/size}"',

    'rpc "{size=-6}Heh, I knew you preferred softer-looking clothing. I made the right choice with this outfit.{/size}"':
    'rpc "{size=-6}เฮ้ ฉันรู้ว่าคุณชอบเสื้อผ้านุ่มๆ ฉันเลือกชุดนี้ถูกแล้วล่ะ{/size}"',

    'rpc "{size=-6}I-I wasn\'t expecting you to show up so soon…!{/size}"':
    'rpc "{size=-6}ฉ-ฉันไม่คิดว่าคุณจะมาเร็วขนาดนี้…!{/size}"',

    'rpc "{i}Ahem!{/i} Um… S-Sorry, I hope I\'m not bothering you."':
    'rpc "{i}อืม!{/i} เอ่อ… ข-ขอโทษครับ หวังว่าจะไม่รบกวนนะ"',
}

applied = 0
new_lines = []
for line in lines:
    stripped = line.rstrip("\n")
    m = re.match(r'^    (\w+) "(.*)"$', stripped)
    if m:
        prefix = m.group(1)
        text = m.group(2)
        full_key = f'{prefix} "{text}"'
        # Also try with escaped quotes
        if full_key in translations:
            new_lines.append(f'    {translations[full_key]}\n')
            applied += 1
            continue
        # Try with escaped quotes in the key
        escaped_key = full_key.replace('"', '\\"')
        if escaped_key in translations:
            new_lines.append(f'    {translations[escaped_key]}\n')
            applied += 1
            continue
    new_lines.append(line)

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Applied: {applied}")
