## BASIC PLAYER STUFF
default player = "Angel"
default surname = "Mentior"
default player_fl = "A" ## options: POV you are the entire aplhabet
default surname_fl = "M" ## options: POV you are still the entire aplhabet
default pronoun = "neutral" #options: female, male, neutral, custom
default they = "they" ## options: she, he, they
default them = "them" ## options: her, him, them
default their = "their" ## options: her, his, their
default theirs = "theirs" ## options: hers, his, theirs
default themself = "themself" ## options: herself, himself, themself
default baby = "baby" ## options: boy, girl, baby
default person = "person" ## options: man, woman, person
default are = "are" ## options: is, are
default partner = "partner" ## options: girlfriend, boyfriend, partner
default spouse = "spouse" ## options: wife, husband, spouse
default gorgeous = "gorgeous" ## options: pretty, gorgeous, handsome
default body = "ambiguous" ## options: feminine, masculine, ambiguous

## CUSTOM PLAYER STUFF
default custom_angel = False
default customise_category = "face"
default customise_body = "body 1" ## options: body 1, body 2
default customise_face = "face_1" ## options: face 1, face 2
default customise_hair = "hair_1" ## options: hair 1, hair 2, hair 3, hair 4, hair 5, hair 6
default customise_eyes = "eyes 1" ## options: eyes 1, eyes 2
default customise_lashes = "lashes 0" ## options: lashes 0, lashes 1, lashes 2
default customise_iris = "iris_1" ## options: iris 1, iris 2, iris 3, iris 4
default customise_strandcolour = "cc_14"
default customise_iriscolour = "cc_10"
default customise_skintone = "cc_19"

## CUSTOM COLOURS
## so I don't lose my mind manually updating these one by one in CSP
default colour_1 = "#94C1EB"
default colour_2 = "#626C7C"
default colour_3 = "#A9CB7B"
default colour_4 = "#64693E"
default colour_5 = "#86663F"
default colour_6 = "#BD8628"
default colour_7 = "#473125"
default colour_8 = "#2C2C2C"
default colour_9 = "#8B3F3F"
default colour_10 = "#E4564E"
default colour_11 = "#FFDB64"
default colour_12 = "#FAE4A7"
default colour_13 = "#F68EB0"
default colour_14 = "#5e207d"
default colour_15 = "#395FB2"
default colour_16 = "#e1e1e1"

default sc_1 = "#f4e5df"
default sc_2 = "#ecd6ca"
default sc_3 = "#e1bfa8"
default sc_4 = "#cea99d"
default sc_5 = "#b98979"
default sc_6 = "#9e6e58"
default sc_7 = "#825140"
default sc_8 = "#6b432d"
default sc_9 = "#492f28"
default sc_10 = "#382b26"

default ec_1 = "blue"
default ec_2 = "grey"
default ec_3 = "green"
default ec_4 = "hazel"
default ec_5 = "hazel"
default ec_6 = "brown"
default ec_7 = "brown"
default ec_8 = "black"
default ec_9 = "red"
default ec_10 = "red"
default ec_11 = "yellow"
default ec_12 = "yellow"
default ec_13 = "pink"
default ec_14 = "purple"
default ec_15 = "blue"
default ec_16 = "white"

default hc_1 = "blue"
default hc_2 = "grey"
default hc_3 = "green"
default hc_4 = "green"
default hc_5 = "brunette"
default hc_6 = "brunette"
default hc_7 = "brunette"
default hc_8 = "black"
default hc_9 = "red"
default hc_10 = "red"
default hc_11 = "blonde"
default hc_12 = "blonde"
default hc_13 = "pink"
default hc_14 = "purple"
default hc_15 = "blue"
default hc_16 = "white"

default colour_ren = "#ff66cb"
default colour_fade = "#ff66cb"

## GAME STUFF
default calendar_day = "00"
default skipday = "Return"
default choice_style = "default"
default death_flag = "hehe"
default version_number = "5.5.2"
default mainmenutext = random.choice(mainmenulist)
default android_toggle = False ## This is genuinely so annoying lmao
default under18 = False ## Boy oh boy this sure better stay false >:((((( /gen
default playtest = False

## SPRITES BABYYYY
default ren_blood = False
default ren_hair = "normal" ## options: short, medium, long
default ren_length = "normal" ## options: normal, blue
default ren_outfit = "normal" ## options: normal, nakey, lounge, swimwear
default moth_outfit = "normal" ## options: normal, swimwear

## INPUT STUFF PART 2 ELECTRIC BOOGALOO
default input_prompt = "question"
default input_answer = "answer" ## this is so poorly done jdgjsgk
default input_actual = VariableInputValue("input_answer", default=False)

## CUSTOMISE ANGEL OR WHATEVAAA
default favourite_outfit = "casual" ## options: cute, comfy, edgy, professional, trendy, casual
default favourite_snack = "scone" ##options: scone, croissant, cake, cookie
default favourite_drink = "coffee" ## options: coffee, latte, soda, smoothie
default favourite_icecream = "vanilla" ## has custom input
default player_hair = "hidden"
default hair_length = "short" ## options: short, mid-length, long, bald
default hair_texture = "straight" ## options: straight, wavy, curly, coily, braided, locs
default hair_colour = "purple"
default eye_colour = "red"
default first_kiss = False ## to make sure Angel doesn't say unecessary lines in Day 1

## CUSTOMISE THE "LOVE INTEREST"
default highest_affinity = "Ren"
default li_name = "Ren"
default li_they = "he"
default li_them = "him"
default li_hair = "pink"
default li_are = "is"

## WE'RE PLAYIN CUPID
default greenyellow = False
default purplebrown = False

## CAST FLAGS
default meet_ren = False
default meet_moth = False
default meet_violet = False
default meet_elanor = False
default meet_conan = False
default meet_jae = False
default meet_leon = False
default meet_teo = False
default meet_olivia = False
default meet_kiara = False

## CAST STATUSES
default status_ren = True
default status_moth = True
default status_violet = True
default status_elanor = True
default status_conan = True
default status_jae = True
default status_leon = True
default status_teo = True
default status_olivia = True
default status_kiara = True

## AFFECTION METER
default affection_ren = 0
default affection_moth = 0
default affection_violet = 0
default affection_elanor = 0
default affection_conan = 0
default affection_jae = 0
default affection_leon = 0
default affection_teo = 0
default affection_olivia = 0
default affection_kiara = 0
default affection_total = 30

## OTHER METERS
default meter_gore = 0
default moth_confidence = 0
default angel_sanity = 0
default ren_switch = 0
default ren_purity = 0 ## Purity Run :3
default ren_decay = 0 ## Decay Run :3

## RELATIONSHIP STUFF
default relationship_ren = "neutral" ## options: dislike, neutral, like, crush
default relationship_teo = "friend" ## options: friend, exboyfriend

## PERSISTENT STUFF
default persistent.corupdate_user = ""
default persistent.streamermode = False
default persistent.warningscreen = False
default persistent.fdwyupdate = True
default persistent.menumissing = False
default persistent.imgdistortion = False
default persistent.dayend = False
default persistent.deadend1 = False
default persistent.deadend2 = False
default persistent.deadend3 = False
default persistent.deadend4 = False
default persistent.deadend5 = False
default persistent.deadendings = 0

## STREAMER MODE
default fuck = "fuck"
default fucked = "fucked"
default damn = "damn"
default dammit = "dammit"
default shit = "shit"
default pissing = "pissing"
default asshole = "asshole"

## DLCs
default persistent.dlc_14dwy_ver = "D55426"
default persistent.dlc_14nwy_ver = "000000"
default persistent.dlc_14nwy_comp = False
default dlc_14nightswithyou_scenes = False
default persistent.dlc_14nightswithyou = False
default persistent.dlc_14nightswithyou_type = "none"

## INPUT STUFF
default player_input = VariableInputValue("player", default=False)
default surname_input = VariableInputValue("surname", default=False)
default username_angel_input = VariableInputValue("username_angel", default=False)
default update_angel_input = VariableInputValue("update_angel", default=False)
default they_input = VariableInputValue("they", default=False)
default them_input = VariableInputValue("them", default=False)
default their_input = VariableInputValue("their", default=False)
default theirs_input = VariableInputValue("theirs", default=False)
default themself_input = VariableInputValue("themself", default=False)
default partner_input = VariableInputValue("partner", default=False)
default spouse_input = VariableInputValue("spouse", default=False)
default person_input = VariableInputValue("person", default=False)
default unlockable_input = VariableInputValue("unlockable", default=False)
default gallery_username_input = VariableInputValue("gallery_username", default=False)
default gallery_password_input = VariableInputValue("gallery_password", default=False)

## APP STUFF
default unlock_profile = True
default unlock_help = False
default unlock_contacts = False
default unlock_security = False

## CAM STUFF
default cam_feed = False
default cam_display = None
default cam_chance = 1
default cam_list = ["gui/socials/camera/sl_topleft.webp", "gui/socials/camera/sl_bottomleft.webp", "gui/socials/camera/sl_topright.webp", "gui/socials/camera/cam_topleft1.webp", "gui/socials/camera/cam_topright1.webp", "gui/socials/camera/cam_bottomleft1.webp"]

## GALLERY STUFF
default persistent.cg_d1_library = False
default persistent.cg_d2_rain = False
default persistent.cg_d3_manga = False
default persistent.cg_d4_aquarium = False
default persistent.cg_d5_beach = False
default persistent.cg_d5_alleyway1 = False
default persistent.cg_d5_alleyway2 = False
default persistent.cg_de1 = False
default persistent.cg_de2 = False
default persistent.cg_de3 = False
default gallery_day = "01"
default gallery_username = "*******"
default gallery_password = "*******"
default persistent.terminal_unlocked = False
default persistent.fact_name = False
default persistent.fact_dob = False
default persistent.fact_job = False
default persistent.fact_tempermentshy = False
default persistent.fact_mannerism1 = False ## Jaw
default persistent.fact_mannerism2 = False ## Sleeves
default persistent.fact_food = False
default persistent.fact_drink = False
default persistent.fact_cosmetics = False
default persistent.fact_residence = False
default persistent.fact_awy = False

## GAME REMEMBERING STUFF
default rem_boyfriend = False
default rem_touch = False
default rem_wahoo = False
default rem_yippee = False
default persistent.game_open = 0
default welcome_chatter = False

## DIALOGUE STUFF
default ch_angel = "Angel"
default ch_ren = "Ren"
default ch_moth = "Moth"
default ch_violet = "Violet"
default ch_elanor = "Elanor"
default ch_conan = "Conan"
default ch_jae = "Jae"
default ch_leon = "Leon"
default ch_teo = "Teo"
default ch_olivia = "Olivia"
default ch_kiara = "Kiara"

## SOCIALS STUFF
default socials_tab = "main"
default username_angel = ""
default username_ren = "REN.EXE"
default username_moth = "HARUKOLOGIST"
default username_violet = "VIOLETSEASON"
default username_elanor = "COFFEE.AND.CRYSTALS"
default username_conan = "CONAN_OROURKE1"
default username_jae = "JAELIKETHELETTER"
default username_leon = "20DAVIS20"
default username_teo = "TEODORE"
default username_olivia = "I_AM_DAWHAN"
default username_kiara = "DEARKIARA"
default update_angel = "status"
default update_ren = ""
default update_moth = ""
default update_violet = ""
default update_elanor = ""
default update_conan = ""
default update_jae = ""
default update_leon = ""
default update_teo = ""
default update_olivia = ""
default update_kiara = ""

## OTHER STUFF IDK
default unlockable = "what else?"
default angel_icon = "def"
default froggy_switch = False
default demo_bubble = False

## POSITIONS
default cpos = tright
default epos = tright
default jpos = tleft
default kpos = tleft
default lpos = cright
default mpos = cright
default opos = tleft
default rpos = tleft
default tpos = cright
default vpos = cright
default spos = tleft
default npos = tleft
default ropos = tleft
default vcpos = vcright

## LOCATIONS
default location_ren = "library" ## pier, library, bluemoss, home, oh, random, aquarium
default location_moth = "home" ## pier, library, bluemoss, home, oh, random
default location_violet = "home" ## pier, library, bluemoss, home, random, work
default location_elanor = "library" ## pier, library, bluemoss, home, apartment, random, aquarium
default location_conan = "library" ## pier, library, bluemoss, home, random, work
default location_jae = "street" ## pier, library, bluemoss, home, random, street, city
default location_leon = "street" ## pier, library, bluemoss, home, random, street, aquarium
default location_teo = "pier" ## pier, library, bluemoss, home, random, aquarium, graveyard
default location_olivia = "work" ## pier, library, bluemoss, home, work, random, graveyard
default location_kiara = "library" ## pier, library, bluemoss, home, oh, random

## REN HELP STUFF
default rh_o = ""
default rh_c = ""
default de_o = ""
default de_c = ""

## Day 0
default ending_demo = "unobtained"
default ending_good = "unobtained"

## DAY 1
default d1_makesnack = False
default d1_inviteren = False
default d1_sharebed = False
default d1_wahooren = False

## DAY 2
default d2_visitren = False
default d2_renkiss = False
default d2_snooping = False
default d2_wahooren = False

## DAY 3
default d3_datestatus = True
default d3_inviteren = False
default d3_invitestatus = False
default d3_inviteover = False
default d3_wahooren = False

## DAY 4
default d4_altroute = False
default d4_gloomy = False
default d4_snooping = False
default d4_visitren = False
default d4_inviteren = False
default d4_wahooren = False

## DAY 5
default d5_invitebed = False
default d5_inviteren = False
default d5_witnesskill = False
default d5_cuddleren = False
default d5_sharebed = False
default d5_wahooren = False

## ACHIEVEMENTS
default persistent.d1_ending_gooding = False
default persistent.d1_badending = False
default persistent.d1_inviteren = False
default persistent.d1_dontinviteren = False
default persistent.d1_sleepoutside = False
default persistent.d1_blocknumber = False

default persistent.d2_ending_gooding = False
default persistent.d2_badending = False
default persistent.d2_visitren = False
default persistent.d2_visitangel = False
default persistent.d2_snooparound = False
default persistent.d2_killolivia = False

default persistent.d3_ending_gooding = False
default persistent.d3_badending = False
default persistent.d3_scareren = False
default persistent.d3_declinedate = False
default persistent.d3_meetmoth = False
default persistent.d3_inviteover = False

default persistent.d4_ending_gooding = False
default persistent.d4_badending = False
default persistent.d4_icecream = False
default persistent.d4_visitangel = False
default persistent.d4_snooparound = False
default persistent.d4_killteo = False

default persistent.d5_ending_gooding = False
default persistent.d5_badending = False
default persistent.d5_visitviolet = False
default persistent.d5_dismissren = False
default persistent.d5_kickfigure = False
default persistent.d5_visitren = False