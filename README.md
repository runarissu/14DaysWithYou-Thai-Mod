# 14 Days With You — Thai Localization Mod

ม็อดแปลภาษาไทยสำหรับเกม **14 Days With You** 5.5 (Ren'Py 8.5.2)

Thai localization mod for the visual novel *14 Days With You* 5.5.

## คุณสมบัติ (Features)

- แปลบทพูดครบ Day 0–5 และเนื้อหาเสริม
- แปล UI ทุกหน้าจอ (เมนู, preferences, save/load, credits, ฯลฯ)
- รองรับฟอนต์ไทย Noto Sans Thai, Prompt, Sarabun, PlainPixel
- ปุ่มสลับภาษา ไทย/EN ในเกม
- รักษา text tags, variables, และ syntax ของ Ren'Py ทั้งหมด
- ไม่แก้ไฟล์เดิมของเกม (overlay system)

## วิธีติดตั้ง (Installation)

1. ดาวน์โหลด `thai_mod.rpa` จาก [Releases](../../releases)
2. คัดลอกไฟล์ไปยังโฟลเดอร์ `game\` ของเกม

   ```
   14DaysWithYou-5.5-pc\game\thai_mod.rpa
   ```

3. เปิดเกมปกติ — Ren'Py โหลดม็อดอัตโนมัติ
4. กดปุ่ม **"ไทย"** ที่มุมจอเพื่อสลับภาษา

## วิธีถอน (Uninstall)

- ลบ `thai_mod.rpa` ออกจากโฟลเดอร์ `game\` — เกมกลับเป็นอังกฤษปกติ

## ข้อกำหนด (Requirements)

- เกม 14 Days With You 5.5 (เวอร์ชันเดียวกันเท่านั้น)
- Windows / Linux / Mac

## โครงสร้างไฟล์ม็อด (Mod Structure)

```
14DaysWithYou-5.5-pc\game\
├── script.rpa              # ไฟล์เดิมของเกม (ห้ามลบ)
└── thai_mod.rpa            # ม็อดแปลไทย
```

ไฟล์ใน `thai_mod.rpa`:
- `tl/thai/*.rpy` — ไฟล์แปลบทพูด + UI
- `tl/thai/*.ttf` — ฟอนต์ไทย

## ลิขสิทธิ์ (License)

- โค้ดแปล: MIT
- ฟอนต์: OFL/Apache (Noto Sans Thai, Sarabun, Prompt, PlainPixel)
- เกมต้นฉบับ: สงวนลิขสิทธิ์โดย [cutiesai](https://cutiesai.com)

## เครดิต (Credits)

- แปลและปรับแต่ง: [runarissu](https://github.com/runarissu)
- เกมต้นฉบับ: [14 Days With You](https://14dayswithyou.tumblr.com) by cutiesai
