# 14 Days With You — Thai Localization Mod

![Hero Banner](hero-banner.png)

ม็อดแปลภาษาไทยสำหรับเกม **14 Days With You** 5.5 (Ren'Py 8.5.2)

Thai localization mod for the visual novel *14 Days With You* 5.5.

## วิธีติดตั้ง (Installation)

1. ดาวน์โหลด `thai_mod.zip` จาก [Releases](../../releases)
2. แตกไฟล์ zip จะได้โฟลเดอร์ `game/tl/thai/`
3. คัดลอกโฟลเดอร์ `tl` ทั้งโฟลเดอร์ไปยังโฟลเดอร์ `game\` ของเกม

   ```
   14DaysWithYou-5.5-pc\game\tl\thai\
   ```

4. เปิดเกม — ภาษาไทยจะเปิดใช้งานอัตโนมัติ
5. กดปุ่ม **EN / ไทย** ที่มุมซ้ายบนเพื่อสลับภาษา

## วิธีถอน (Uninstall)

- ลบโฟลเดอร์ `tl\thai\` ออกจากโฟลเดอร์ `game\`

## ข้อกำหนด (Requirements)

- เกม 14 Days With You 5.5 (เวอร์ชันเดียวกันเท่านั้น)
- Windows / Linux / Mac

## โครงสร้างไฟล์ (File Structure)

```
14DaysWithYou-5.5-pc\
└── game\
    ├── script.rpa              # ไฟล์เดิมของเกม (ห้ามลบ)
    └── tl\
        └── thai\               # ม็อดแปลไทย
            ├── common.rpy
            ├── replace_font.rpy
            ├── replace_screens.rpy
            ├── *.ttf            # ฟอนต์ไทย
            └── scripts\         # ไฟล์แปลบทพูด + UI
```

## เครดิต (Credits)

- แปลและปรับแต่ง: [runarissu](https://github.com/runarissu)
- เกมต้นฉบับ: [14 Days With You](https://14dayswithyou.tumblr.com) by cutiesai
- ฟอนต์: Noto Sans Thai, PlainPixel (OFL/Apache)
