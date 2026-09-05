################################################################################
# CG ART BABEYYYYYYYY
################################################################################
# Day 1 CG
image CG D1_LIBRARY = Composite(
    (1920, 1080),
    (0, 0), Transform("ren cg/d1 library/background.webp", zoom=1.3, crop=(200, 30, 1920, 1080)),
    (0, 0), Transform("ren cg/d1 library/ren hair [ren_hair].webp", zoom=1.3, crop=(200, 30, 1920, 1080)),
    (0, 0), Transform("d1 library blink", zoom=1.3, crop=(200, 30, 1920, 1080)),
    (0, 0), "peffect",
    (0, 0), "ren cg/d1 library/sparkle.webp",
    )

image d1 library blink:
    "ren cg/d1 library/eyes 1.webp"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren cg/d1 library/eyes 0.webp"
    .05
    repeat

## Day 2 CG
image CG D2_RAIN = Composite(
    (1920, 1080),
    (0, 0), "ren cg/d2 rain/ren hair [ren_hair].webp",
    (0, 0), "d2 rain blink",
    )

image d2 rain blink:
    "ren cg/d2 rain/eyes 1.webp"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren cg/d2 rain/eyes 0.webp"
    .05
    repeat

# Day 3 CG
image CG D3_MANGA = Composite(
    (1920, 1080),
    (0, 0), "ren cg/d3 manga/background.webp",
    (0, 0), "ren cg/d3 manga/ren hair [ren_hair].webp",
    (0, 0), "d3 manga blink",
    (0,0), "ren cg/d3 manga/shelf.webp",
    )

image d3 manga blink:
    "ren cg/d3 manga/eyes 1.webp"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren cg/d3 manga/eyes 0.webp"
    .05
    repeat

# Day 4 CG
image CG D4_AQUARIUM = Composite(
    (1920, 1080),
    (0, 0), "ren cg/d4 aquarium/ren hair [ren_hair].webp",
    (0, 0), "d4 aquarium blink",
    (0, 0), "peffectp",
    (0, 0), "ren cg/d4 aquarium/sparkle.webp",
    )

image d4 aquarium blink:
    "ren cg/d4 aquarium/eyes 1.webp"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren cg/d4 aquarium/eyes 0.webp"
    .05
    repeat

# Day 5 CG
image CG D5_BEACH = Composite(
    (1920, 1080),
    (0, 0), "ren cg/d5 beach/ren hair [ren_hair].webp",
    (0, 0), "peffect",
    (0, 0), "d5 beach blink",
    )

image d5 beach blink:
    "ren cg/d5 beach/eyes 1.webp"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren cg/d5 beach/eyes 0.webp"
    .05
    repeat

# Day 5 CG ALT
image CG D5_ALLEYWAY1 = Composite(
    (1920, 1080),
    (0, 0), "ren cg/d5 alleyway/ren hair [ren_hair].webp",
    (0, 0), "ren cg/d5 alleyway/brows 0.webp",
    (0, 0), "ren cg/d5 alleyway/mouth 0.webp",
    (0, 0), "peffectp",
    (0, 0), "d5 alleyway blink1",
    )

image CG D5_ALLEYWAY2 = Composite(
    (1920, 1080),
    (0, 0), "ren cg/d5 alleyway/ren hair [ren_hair].webp",
    (0, 0), "ren cg/d5 alleyway/brows 1.webp",
    (0, 0), "ren cg/d5 alleyway/mouth 1.webp",
    (0, 0), "peffectp",
    (0, 0), "d5 alleyway blink2",
    )

image d5 alleyway blink1:
    "ren cg/d5 alleyway/eyes 1.webp"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren cg/d5 alleyway/eyes 0.webp"
    .05
    repeat

image d5 alleyway blink2:
    "ren cg/d5 alleyway/eyes 2.webp"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren cg/d5 alleyway/eyes 0.webp"
    .05
    repeat

################################################################################
# ren
################################################################################
## ren neutral
image ren neutral = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 1.png",
    (0, 0), "ren sprites/ren mouth 1.png",
    (0, 0), "ren eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes neutral:
    "ren sprites/ren eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren neutral z:
    "ren neutral"
    zoom 1.3
    yoffset 300

## ren happy
image ren happy = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 1.png",
    (0, 0), "ren sprites/ren mouth 2.png",
    (0, 0), "ren eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes happy:
    "ren sprites/ren eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren happy z:
    "ren happy"
    zoom 1.3
    yoffset 300

## ren angry
image ren angry = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 3.png",
    (0, 0), "ren sprites/ren mouth 4.png",
    (0, 0), "ren eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes angry:
    "ren sprites/ren eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren angry z:
    "ren angry"
    zoom 1.3
    yoffset 300

## ren frown
image ren frown = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 3.png",
    (0, 0), "ren sprites/ren mouth 5.png",
    (0, 0), "ren eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes frown:
    "ren sprites/ren eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren frown z:
    "ren frown"
    zoom 1.3
    yoffset 300

## ren sad
image ren sad = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 2.png",
    (0, 0), "ren sprites/ren mouth 3.png",
    (0, 0), "ren eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes sad:
    "ren sprites/ren eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren sad z:
    "ren sad"
    zoom 1.3
    yoffset 300

## ren flushed
image ren flushed = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 2.png",
    (0, 0), "ren sprites/ren mouth 1.png",
    (0, 0), "ren sprites/ren blush.png",
    (0, 0), "ren eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes flushed:
    "ren sprites/ren eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren flushed z:
    "ren flushed"
    zoom 1.3
    yoffset 300

## ren blushing
image ren blushing = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 3.png",
    (0, 0), "ren sprites/ren mouth 5.png",
    (0, 0), "ren sprites/ren blush 1.png",
    (0, 0), "ren eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes blushing:
    "ren sprites/ren eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren blushing z:
    "ren blushing"
    zoom 1.3
    yoffset 300

## ren smirk
image ren smirk = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 1.png",
    (0, 0), "ren sprites/ren mouth 1.png",
    (0, 0), "ren eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes smirk:
    "ren sprites/ren eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren smirk z:
    "ren smirk"
    zoom 1.3
    yoffset 300

## ren lovesick
image ren lovesick = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 2.png",
    (0, 0), "ren sprites/ren mouth 2.png",
    (0, 0), "ren sprites/ren blush.png",
    (0, 0), "ren eyes lovesick",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes lovesick:
    "ren sprites/ren eyes 4.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren lovesick z:
    "ren lovesick"
    zoom 1.3
    yoffset 300

## ren lovesmirk
image ren lovesmirk = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 2.png",
    (0, 0), "ren sprites/ren mouth 5.png",
    (0, 0), "ren sprites/ren blush.png",
    (0, 0), "ren eyes lovesmile",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes lovesmirk:
    "ren sprites/ren eyes 4.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren lovesmirk z:
    "ren lovesmirk"
    zoom 1.3
    yoffset 300

## ren lovesmile
image ren lovesmile = Composite(
    (551, 1080),
    (0, 0), "ren sprites/ren back [ren_length].png",
    (0, 0), "ren sprites/ren base [ren_outfit].png",
    (0, 0), "ren sprites/ren hair [ren_hair].png",
    (0, 0), "ren sprites/ren brows 2.png",
    (0, 0), "ren sprites/ren mouth 6.png",
    (0, 0), "ren sprites/ren blush 1.png",
    (0, 0), "ren eyes lovesmile",
    (0,0), ConditionSwitch ("froggy_switch == True", "ren sprites/ren froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    (0,0), ConditionSwitch ("ren_blood == True", "ren sprites/ren blood.png", "ren_blood == False", "images/misc/blank.png",),
    )

image ren eyes lovesmile:
    "ren sprites/ren eyes 4.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "ren sprites/ren eyes 1.png"
    .05
    repeat

image ren lovesmile z:
    "ren lovesmile"
    zoom 1.3
    yoffset 300

################################################################################
# violet
################################################################################
## violet neutral
image violet neutral = Composite(
    (551, 1080),
    (0, 0), "violet sprites/violet base.png",
    (0, 0), "violet sprites/violet mouth 1.png",
    (0, 0), "violet sprites/violet brows 1.png",
    (0, 0), "violet eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "violet sprites/violet froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image violet eyes neutral:
    "violet sprites/violet eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "violet sprites/violet eyes 1.png"
    .05
    repeat

image violet neutral z:
    "violet neutral"
    zoom 1.3
    yoffset 230

## violet happy
image violet happy = Composite(
    (551, 1080),
    (0, 0), "violet sprites/violet base.png",
    (0, 0), "violet sprites/violet brows 1.png",
    (0, 0), "violet sprites/violet mouth 2.png",
    (0, 0), "violet eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "violet sprites/violet froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image violet eyes happy:
    "violet sprites/violet eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "violet sprites/violet eyes 1.png"
    .05
    repeat

image violet happy z:
    "violet happy"
    zoom 1.3
    yoffset 230

## violet angry
image violet angry = Composite(
    (551, 1080),
    (0, 0), "violet sprites/violet base.png",
    (0, 0), "violet sprites/violet brows 3.png",
    (0, 0), "violet sprites/violet mouth 3.png",
    (0, 0), "violet eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "violet sprites/violet froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image violet eyes angry:
    "violet sprites/violet eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "violet sprites/violet eyes 1.png"
    .05
    repeat

image violet angry z:
    "violet angry"
    zoom 1.3
    yoffset 230

## violet frown
image violet frown = Composite(
    (551, 1080),
    (0, 0), "violet sprites/violet base.png",
    (0, 0), "violet sprites/violet brows 3.png",
    (0, 0), "violet sprites/violet mouth 4.png",
    (0, 0), "violet eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "violet sprites/violet froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image violet eyes frown:
    "violet sprites/violet eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "violet sprites/violet eyes 1.png"
    .05
    repeat

image violet frown z:
    "violet frown"
    zoom 1.3
    yoffset 230

## violet sad
image violet sad = Composite(
    (551, 1080),
    (0, 0), "violet sprites/violet base.png",
    (0, 0), "violet sprites/violet brows 2.png",
    (0, 0), "violet sprites/violet mouth 3.png",
    (0, 0), "violet eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "violet sprites/violet froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image violet eyes sad:
    "violet sprites/violet eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "violet sprites/violet eyes 1.png"
    .05
    repeat

image violet sad z:
    "violet sad"
    zoom 1.3
    yoffset 230

## violet flushed
image violet flushed = Composite(
    (551, 1080),
    (0, 0), "violet sprites/violet base.png",
    (0, 0), "violet sprites/violet brows 2.png",
    (0, 0), "violet sprites/violet mouth 3.png",
    (0, 0), "violet sprites/violet blush.png",
    (0, 0), "violet eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "violet sprites/violet froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image violet eyes flushed:
    "violet sprites/violet eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "violet sprites/violet eyes 1.png"
    .05
    repeat

image violet flushed z:
    "violet flushed"
    zoom 1.3
    yoffset 230

## violet blushing
image violet blushing = Composite(
    (551, 1080),
    (0, 0), "violet sprites/violet base.png",
    (0, 0), "violet sprites/violet brows 1.png",
    (0, 0), "violet sprites/violet mouth 2.png",
    (0, 0), "violet sprites/violet blush.png",
    (0, 0), "violet eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "violet sprites/violet froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image violet eyes blushing:
    "violet sprites/violet eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "violet sprites/violet eyes 1.png"
    .05
    repeat

image violet blushing z:
    "violet blushing"
    zoom 1.3
    yoffset 230

## violet smirk
image violet smirk = Composite(
    (551, 1080),
    (0, 0), "violet sprites/violet base.png",
    (0, 0), "violet sprites/violet brows 1.png",
    (0, 0), "violet sprites/violet mouth 2.png",
    (0, 0), "violet eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "violet sprites/violet froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image violet eyes smirk:
    "violet sprites/violet eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "violet sprites/violet eyes 1.png"
    .05
    repeat

image violet smirk z:
    "violet smirk"
    zoom 1.3
    yoffset 230

################################################################################
# elanor
################################################################################
## elanor neutral
image elanor neutral = Composite(
    (551, 1080),
    (0, 0), "elanor sprites/elanor base.png",
    (0, 0), "elanor sprites/elanor brows 1.png",
    (0, 0), "elanor sprites/elanor mouth 3.png",
    (0, 0), "elanor eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "elanor sprites/elanor froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image elanor eyes neutral:
    "elanor sprites/elanor eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "elanor sprites/elanor eyes 1.png"
    .05
    repeat

image elanor neutral z:
    "elanor neutral"
    zoom 1.3
    yoffset 230

## elanor happy
image elanor happy = Composite(
    (551, 1080),
    (0, 0), "elanor sprites/elanor base.png",
    (0, 0), "elanor sprites/elanor brows 1.png",
    (0, 0), "elanor sprites/elanor mouth 2.png",
    (0, 0), "elanor eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "elanor sprites/elanor froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image elanor eyes happy:
    "elanor sprites/elanor eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "elanor sprites/elanor eyes 1.png"
    .05
    repeat

image elanor happy z:
    "elanor happy"
    zoom 1.3
    yoffset 230

## elanor angry
image elanor angry = Composite(
    (551, 1080),
    (0, 0), "elanor sprites/elanor base.png",
    (0, 0), "elanor sprites/elanor brows 3.png",
    (0, 0), "elanor sprites/elanor mouth 3.png",
    (0, 0), "elanor eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "elanor sprites/elanor froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image elanor eyes angry:
    "elanor sprites/elanor eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "elanor sprites/elanor eyes 1.png"
    .05
    repeat

image elanor angry z:
    "elanor angry"
    zoom 1.3
    yoffset 230

## elanor frown
image elanor frown = Composite(
    (551, 1080),
    (0, 0), "elanor sprites/elanor base.png",
    (0, 0), "elanor sprites/elanor brows 3.png",
    (0, 0), "elanor sprites/elanor mouth 3.png",
    (0, 0), "elanor eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "elanor sprites/elanor froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image elanor eyes frown:
    "elanor sprites/elanor eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "elanor sprites/elanor eyes 1.png"
    .05
    repeat

image elanor frown z:
    "elanor frown"
    zoom 1.3
    yoffset 230

## elanor sad
image elanor sad = Composite(
    (551, 1080),
    (0, 0), "elanor sprites/elanor base.png",
    (0, 0), "elanor sprites/elanor brows 2.png",
    (0, 0), "elanor sprites/elanor mouth 3.png",
    (0, 0), "elanor eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "elanor sprites/elanor froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image elanor eyes sad:
    "elanor sprites/elanor eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "elanor sprites/elanor eyes 1.png"
    .05
    repeat

image elanor sad z:
    "elanor sad"
    zoom 1.3
    yoffset 230

## elanor flushed
image elanor flushed = Composite(
    (551, 1080),
    (0, 0), "elanor sprites/elanor base.png",
    (0, 0), "elanor sprites/elanor brows 3.png",
    (0, 0), "elanor sprites/elanor mouth 3.png",
    (0, 0), "elanor sprites/elanor blush.png",
    (0, 0), "elanor eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "elanor sprites/elanor froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image elanor eyes flushed:
    "elanor sprites/elanor eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "elanor sprites/elanor eyes 1.png"
    .05
    repeat

image elanor flushed z:
    "elanor flushed"
    zoom 1.3
    yoffset 230

## elanor blushing
image elanor blushing = Composite(
    (551, 1080),
    (0, 0), "elanor sprites/elanor base.png",
    (0, 0), "elanor sprites/elanor brows 2.png",
    (0, 0), "elanor sprites/elanor mouth 1.png",
    (0, 0), "elanor sprites/elanor blush.png",
    (0, 0), "elanor eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "elanor sprites/elanor froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image elanor eyes blushing:
    "elanor sprites/elanor eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "elanor sprites/elanor eyes 1.png"
    .05
    repeat

image elanor blushing z:
    "elanor blushing"
    zoom 1.3
    yoffset 230

## elanor smirk
image elanor smirk = Composite(
    (551, 1080),
    (0, 0), "elanor sprites/elanor base.png",
    (0, 0), "elanor sprites/elanor brows 1.png",
    (0, 0), "elanor sprites/elanor mouth 1.png",
    (0, 0), "elanor eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "elanor sprites/elanor froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image elanor eyes smirk:
    "elanor sprites/elanor eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "elanor sprites/elanor eyes 1.png"
    .05
    repeat

image elanor smirk z:
    "elanor smirk"
    zoom 1.3
    yoffset 230

################################################################################
# leon
################################################################################
## leon neutral
image leon neutral = Composite(
    (551, 1080),
    (0, 0), "leon sprites/leon base.png",
    (0, 0), "leon sprites/leon brows 1.png",
    (0, 0), "leon sprites/leon mouth 1.png",
    (0, 0), "leon eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "leon sprites/leon froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image leon eyes neutral:
    "leon sprites/leon eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "leon sprites/leon eyes 1.png"
    .05
    repeat

image leon neutral z:
    "leon neutral"
    zoom 1.3
    yoffset 290

## leon happy
image leon happy = Composite(
    (551, 1080),
    (0, 0), "leon sprites/leon base.png",
    (0, 0), "leon sprites/leon brows 1.png",
    (0, 0), "leon sprites/leon mouth 2.png",
    (0, 0), "leon eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "leon sprites/leon froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image leon eyes happy:
    "leon sprites/leon eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "leon sprites/leon eyes 1.png"
    .05
    repeat

image leon happy z:
    "leon happy"
    zoom 1.3
    yoffset 290

## leon angry
image leon angry = Composite(
    (551, 1080),
    (0, 0), "leon sprites/leon base.png",
    (0, 0), "leon sprites/leon brows 3.png",
    (0, 0), "leon sprites/leon mouth 3.png",
    (0, 0), "leon eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "leon sprites/leon froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image leon eyes angry:
    "leon sprites/leon eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "leon sprites/leon eyes 1.png"
    .05
    repeat

image leon angry z:
    "leon angry"
    zoom 1.3
    yoffset 290

## leon frown
image leon frown = Composite(
    (551, 1080),
    (0, 0), "leon sprites/leon base.png",
    (0, 0), "leon sprites/leon brows 3.png",
    (0, 0), "leon sprites/leon mouth 4.png",
    (0, 0), "leon eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "leon sprites/leon froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image leon eyes frown:
    "leon sprites/leon eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "leon sprites/leon eyes 1.png"
    .05
    repeat

image leon frown z:
    "leon frown"
    zoom 1.3
    yoffset 290

## leon sad
image leon sad = Composite(
    (551, 1080),
    (0, 0), "leon sprites/leon base.png",
    (0, 0), "leon sprites/leon brows 2.png",
    (0, 0), "leon sprites/leon mouth 3.png",
    (0, 0), "leon eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "leon sprites/leon froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image leon eyes sad:
    "leon sprites/leon eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "leon sprites/leon eyes 1.png"
    .05
    repeat

image leon sad z:
    "leon sad"
    zoom 1.3
    yoffset 290

## leon flushed
image leon flushed = Composite(
    (551, 1080),
    (0, 0), "leon sprites/leon base.png",
    (0, 0), "leon sprites/leon brows 2.png",
    (0, 0), "leon sprites/leon mouth 3.png",
    (0, 0), "leon sprites/leon blush.png",
    (0, 0), "leon eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "leon sprites/leon froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image leon eyes flushed:
    "leon sprites/leon eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "leon sprites/leon eyes 1.png"
    .05
    repeat

image leon flushed z:
    "leon flushed"
    zoom 1.3
    yoffset 290

## leon blushing
image leon blushing = Composite(
    (551, 1080),
    (0, 0), "leon sprites/leon base.png",
    (0, 0), "leon sprites/leon brows 2.png",
    (0, 0), "leon sprites/leon mouth 2.png",
    (0, 0), "leon sprites/leon blush.png",
    (0, 0), "leon eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "leon sprites/leon froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image leon eyes blushing:
    "leon sprites/leon eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "leon sprites/leon eyes 1.png"
    .05
    repeat

image leon blushing z:
    "leon blushing"
    zoom 1.3
    yoffset 290

## leon smirk
image leon smirk = Composite(
    (551, 1080),
    (0, 0), "leon sprites/leon base.png",
    (0, 0), "leon sprites/leon brows 1.png",
    (0, 0), "leon sprites/leon mouth 2.png",
    (0, 0), "leon eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "leon sprites/leon froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image leon eyes smirk:
    "leon sprites/leon eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "leon sprites/leon eyes 1.png"
    .05
    repeat

image leon smirk z:
    "leon smirk"
    zoom 1.3
    yoffset 290

################################################################################
# teo
################################################################################
## teo neutral
image teo neutral = Composite(
    (551, 1080),
    (0, 0), "teo sprites/teo base.png",
    (0, 0), "teo sprites/teo brows 1.png",
    (0, 0), "teo sprites/teo mouth 1.png",
    (0, 0), "teo eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "teo sprites/teo froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image teo eyes neutral:
    "teo sprites/teo eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "teo sprites/teo eyes 1.png"
    .05
    repeat

image teo neutral z:
    "teo neutral"
    zoom 1.3
    yoffset 300

## teo happy
image teo happy = Composite(
    (551, 1080),
    (0, 0), "teo sprites/teo base.png",
    (0, 0), "teo sprites/teo brows 1.png",
    (0, 0), "teo sprites/teo mouth 2.png",
    (0, 0), "teo eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "teo sprites/teo froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image teo eyes happy:
    "teo sprites/teo eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "teo sprites/teo eyes 1.png"
    .05
    repeat

image teo happy z:
    "teo happy"
    zoom 1.3
    yoffset 300

## teo angry
image teo angry = Composite(
    (551, 1080),
    (0, 0), "teo sprites/teo base.png",
    (0, 0), "teo sprites/teo brows 3.png",
    (0, 0), "teo sprites/teo mouth 3.png",
    (0, 0), "teo eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "teo sprites/teo froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image teo eyes angry:
    "teo sprites/teo eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "teo sprites/teo eyes 1.png"
    .05
    repeat

image teo angry z:
    "teo angry"
    zoom 1.3
    yoffset 300

## teo frown
image teo frown = Composite(
    (551, 1080),
    (0, 0), "teo sprites/teo base.png",
    (0, 0), "teo sprites/teo brows 3.png",
    (0, 0), "teo sprites/teo mouth 4.png",
    (0, 0), "teo eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "teo sprites/teo froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image teo eyes frown:
    "teo sprites/teo eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "teo sprites/teo eyes 1.png"
    .05
    repeat

image teo frown z:
    "teo frown"
    zoom 1.3
    yoffset 300

## teo sad
image teo sad = Composite(
    (551, 1080),
    (0, 0), "teo sprites/teo base.png",
    (0, 0), "teo sprites/teo brows 2.png",
    (0, 0), "teo sprites/teo mouth 3.png",
    (0, 0), "teo eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "teo sprites/teo froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image teo eyes sad:
    "teo sprites/teo eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "teo sprites/teo eyes 1.png"
    .05
    repeat

image teo sad z:
    "teo sad"
    zoom 1.3
    yoffset 300

## teo flushed
image teo flushed = Composite(
    (551, 1080),
    (0, 0), "teo sprites/teo base.png",
    (0, 0), "teo sprites/teo brows 2.png",
    (0, 0), "teo sprites/teo mouth 3.png",
    (0, 0), "teo sprites/teo blush.png",
    (0, 0), "teo eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "teo sprites/teo froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image teo eyes flushed:
    "teo sprites/teo eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "teo sprites/teo eyes 1.png"
    .05
    repeat

image teo flushed z:
    "teo flushed"
    zoom 1.3
    yoffset 300

## teo blushing
image teo blushing = Composite(
    (551, 1080),
    (0, 0), "teo sprites/teo base.png",
    (0, 0), "teo sprites/teo brows 2.png",
    (0, 0), "teo sprites/teo mouth 2.png",
    (0, 0), "teo sprites/teo blush.png",
    (0, 0), "teo eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "teo sprites/teo froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image teo eyes blushing:
    "teo sprites/teo eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "teo sprites/teo eyes 1.png"
    .05
    repeat

image teo blushing z:
    "teo blushing"
    zoom 1.3
    yoffset 300

## teo smirk
image teo smirk = Composite(
    (551, 1080),
    (0, 0), "teo sprites/teo base.png",
    (0, 0), "teo sprites/teo brows 1.png",
    (0, 0), "teo sprites/teo mouth 2.png",
    (0, 0), "teo eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "teo sprites/teo froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image teo eyes smirk:
    "teo sprites/teo eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "teo sprites/teo eyes 1.png"
    .05
    repeat

image teo smirk z:
    "teo smirk"
    zoom 1.3
    yoffset 300

################################################################################
# conan
################################################################################
## conan neutral
image conan neutral = Composite(
    (551, 1080),
    (0, 0), "conan sprites/conan base.png",
    (0, 0), "conan sprites/conan brows 1.png",
    (0, 0), "conan sprites/conan mouth 1.png",
    (0, 0), "conan eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "conan sprites/conan froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image conan eyes neutral:
    "conan sprites/conan eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "conan sprites/conan eyes 1.png"
    .05
    repeat

image conan neutral z:
    "conan neutral"
    zoom 1.3
    yoffset 300

## conan happy
image conan happy = Composite(
    (551, 1080),
    (0, 0), "conan sprites/conan base.png",
    (0, 0), "conan sprites/conan brows 1.png",
    (0, 0), "conan sprites/conan mouth 2.png",
    (0, 0), "conan eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "conan sprites/conan froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image conan eyes happy:
    "conan sprites/conan eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "conan sprites/conan eyes 1.png"
    .05
    repeat

image conan happy z:
    "conan happy"
    zoom 1.3
    yoffset 300

## conan angry
image conan angry = Composite(
    (551, 1080),
    (0, 0), "conan sprites/conan base.png",
    (0, 0), "conan sprites/conan brows 3.png",
    (0, 0), "conan sprites/conan mouth 3.png",
    (0, 0), "conan eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "conan sprites/conan froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image conan eyes angry:
    "conan sprites/conan eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "conan sprites/conan eyes 1.png"
    .05
    repeat

image conan angry z:
    "conan angry"
    zoom 1.3
    yoffset 300

## conan frown
image conan frown = Composite(
    (551, 1080),
    (0, 0), "conan sprites/conan base.png",
    (0, 0), "conan sprites/conan brows 3.png",
    (0, 0), "conan sprites/conan mouth 4.png",
    (0, 0), "conan eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "conan sprites/conan froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image conan eyes frown:
    "conan sprites/conan eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "conan sprites/conan eyes 1.png"
    .05
    repeat

image conan frown z:
    "conan frown"
    zoom 1.3
    yoffset 300

## conan sad
image conan sad = Composite(
    (551, 1080),
    (0, 0), "conan sprites/conan base.png",
    (0, 0), "conan sprites/conan brows 2.png",
    (0, 0), "conan sprites/conan mouth 3.png",
    (0, 0), "conan eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "conan sprites/conan froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image conan eyes sad:
    "conan sprites/conan eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "conan sprites/conan eyes 1.png"
    .05
    repeat

image conan sad z:
    "conan sad"
    zoom 1.3
    yoffset 300

## conan flushed
image conan flushed = Composite(
    (551, 1080),
    (0, 0), "conan sprites/conan base.png",
    (0, 0), "conan sprites/conan brows 2.png",
    (0, 0), "conan sprites/conan mouth 3.png",
    (0, 0), "conan sprites/conan blush.png",
    (0, 0), "conan eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "conan sprites/conan froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image conan eyes flushed:
    "conan sprites/conan eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "conan sprites/conan eyes 1.png"
    .05
    repeat

image conan flushed z:
    "conan flushed"
    zoom 1.3
    yoffset 300

## conan blushing
image conan blushing = Composite(
    (551, 1080),
    (0, 0), "conan sprites/conan base.png",
    (0, 0), "conan sprites/conan brows 2.png",
    (0, 0), "conan sprites/conan mouth 2.png",
    (0, 0), "conan sprites/conan blush.png",
    (0, 0), "conan eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "conan sprites/conan froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image conan eyes blushing:
    "conan sprites/conan eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "conan sprites/conan eyes 1.png"
    .05
    repeat

image conan blushing z:
    "conan blushing"
    zoom 1.3
    yoffset 300

## conan smirk
image conan smirk = Composite(
    (551, 1080),
    (0, 0), "conan sprites/conan base.png",
    (0, 0), "conan sprites/conan brows 1.png",
    (0, 0), "conan sprites/conan mouth 3.png",
    (0, 0), "conan eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "conan sprites/conan froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image conan eyes smirk:
    "conan sprites/conan eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "conan sprites/conan eyes 1.png"
    .05
    repeat

image conan smirk z:
    "conan smirk"
    zoom 1.3
    yoffset 300

################################################################################
# jae
################################################################################
## jae neutral
image jae neutral = Composite(
    (551, 1080),
    (0, 0), "jae sprites/jae base.png",
    (0, 0), "jae sprites/jae brows 1.png",
    (0, 0), "jae sprites/jae mouth 1.png",
    (0, 0), "jae eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "jae sprites/jae froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image jae eyes neutral:
    "jae sprites/jae eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "jae sprites/jae eyes 1.png"
    .05
    repeat

image jae neutral z:
    "jae neutral"
    zoom 1.3
    yoffset 290

## jae happy
image jae happy = Composite(
    (551, 1080),
    (0, 0), "jae sprites/jae base.png",
    (0, 0), "jae sprites/jae brows 1.png",
    (0, 0), "jae sprites/jae mouth 2.png",
    (0, 0), "jae eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "jae sprites/jae froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image jae eyes happy:
    "jae sprites/jae eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "jae sprites/jae eyes 1.png"
    .05
    repeat

image jae happy z:
    "jae happy"
    zoom 1.3
    yoffset 290

## jae angry
image jae angry = Composite(
    (551, 1080),
    (0, 0), "jae sprites/jae base.png",
    (0, 0), "jae sprites/jae brows 3.png",
    (0, 0), "jae sprites/jae mouth 3.png",
    (0, 0), "jae eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "jae sprites/jae froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image jae eyes angry:
    "jae sprites/jae eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "jae sprites/jae eyes 1.png"
    .05
    repeat

image jae angry z:
    "jae angry"
    zoom 1.3
    yoffset 290

## jae frown
image jae frown = Composite(
    (551, 1080),
    (0, 0), "jae sprites/jae base.png",
    (0, 0), "jae sprites/jae brows 3.png",
    (0, 0), "jae sprites/jae mouth 4.png",
    (0, 0), "jae eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "jae sprites/jae froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image jae eyes frown:
    "jae sprites/jae eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "jae sprites/jae eyes 1.png"
    .05
    repeat

image jae frown z:
    "jae frown"
    zoom 1.3
    yoffset 290

## jae sad
image jae sad = Composite(
    (551, 1080),
    (0, 0), "jae sprites/jae base.png",
    (0, 0), "jae sprites/jae brows 2.png",
    (0, 0), "jae sprites/jae mouth 3.png",
    (0, 0), "jae eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "jae sprites/jae froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image jae eyes sad:
    "jae sprites/jae eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "jae sprites/jae eyes 1.png"
    .05
    repeat

image jae sad z:
    "jae sad"
    zoom 1.3
    yoffset 290

## jae flushed
image jae flushed = Composite(
    (551, 1080),
    (0, 0), "jae sprites/jae base.png",
    (0, 0), "jae sprites/jae brows 2.png",
    (0, 0), "jae sprites/jae mouth 3.png",
    (0, 0), "jae sprites/jae blush.png",
    (0, 0), "jae eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "jae sprites/jae froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image jae eyes flushed:
    "jae sprites/jae eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "jae sprites/jae eyes 1.png"
    .05
    repeat

image jae flushed z:
    "jae flushed"
    zoom 1.3
    yoffset 290

## jae blushing
image jae blushing = Composite(
    (551, 1080),
    (0, 0), "jae sprites/jae base.png",
    (0, 0), "jae sprites/jae brows 2.png",
    (0, 0), "jae sprites/jae mouth 2.png",
    (0, 0), "jae sprites/jae blush.png",
    (0, 0), "jae eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "jae sprites/jae froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image jae eyes blushing:
    "jae sprites/jae eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "jae sprites/jae eyes 1.png"
    .05
    repeat

image jae blushing z:
    "jae blushing"
    zoom 1.3
    yoffset 290

## jae smirk
image jae smirk = Composite(
    (551, 1080),
    (0, 0), "jae sprites/jae base.png",
    (0, 0), "jae sprites/jae brows 3.png",
    (0, 0), "jae sprites/jae mouth 1.png",
    (0, 0), "jae eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "jae sprites/jae froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image jae eyes smirk:
    "jae sprites/jae eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "jae sprites/jae eyes 1.png"
    .05
    repeat

image jae smirk z:
    "jae smirk"
    zoom 1.3
    yoffset 300

################################################################################
# olivia
################################################################################
## olivia neutral
image olivia neutral = Composite(
    (551, 1080),
    (0, 0), "olivia sprites/olivia base.png",
    (0, 0), "olivia sprites/olivia brows 1.png",
    (0, 0), "olivia sprites/olivia mouth 1.png",
    (0, 0), "olivia eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "olivia sprites/olivia froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image olivia eyes neutral:
    "olivia sprites/olivia eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "olivia sprites/olivia eyes 1.png"
    .05
    repeat

image olivia neutral z:
    "olivia neutral"
    zoom 1.3
    yoffset 290

## olivia happy
image olivia happy = Composite(
    (551, 1080),
    (0, 0), "olivia sprites/olivia base.png",
    (0, 0), "olivia sprites/olivia brows 1.png",
    (0, 0), "olivia sprites/olivia mouth 2.png",
    (0, 0), "olivia eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "olivia sprites/olivia froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image olivia eyes happy:
    "olivia sprites/olivia eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "olivia sprites/olivia eyes 1.png"
    .05
    repeat

image olivia happy z:
    "olivia happy"
    zoom 1.3
    yoffset 290

## olivia angry
image olivia angry = Composite(
    (551, 1080),
    (0, 0), "olivia sprites/olivia base.png",
    (0, 0), "olivia sprites/olivia brows 2.png",
    (0, 0), "olivia sprites/olivia mouth 3.png",
    (0, 0), "olivia eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "olivia sprites/olivia froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image olivia eyes angry:
    "olivia sprites/olivia eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "olivia sprites/olivia eyes 1.png"
    .05
    repeat

image olivia angry z:
    "olivia angry"
    zoom 1.3
    yoffset 290

## olivia frown
image olivia frown = Composite(
    (551, 1080),
    (0, 0), "olivia sprites/olivia base.png",
    (0, 0), "olivia sprites/olivia brows 3.png",
    (0, 0), "olivia sprites/olivia mouth 3.png",
    (0, 0), "olivia eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "olivia sprites/olivia froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image olivia eyes frown:
    "olivia sprites/olivia eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "olivia sprites/olivia eyes 1.png"
    .05
    repeat

image olivia frown z:
    "olivia frown"
    zoom 1.3
    yoffset 290

## olivia sad
image olivia sad = Composite(
    (551, 1080),
    (0, 0), "olivia sprites/olivia base.png",
    (0, 0), "olivia sprites/olivia brows 2.png",
    (0, 0), "olivia sprites/olivia mouth 3.png",
    (0, 0), "olivia eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "olivia sprites/olivia froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image olivia eyes sad:
    "olivia sprites/olivia eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "olivia sprites/olivia eyes 1.png"
    .05
    repeat

image olivia sad z:
    "olivia sad"
    zoom 1.3
    yoffset 290

## olivia flushed
image olivia flushed = Composite(
    (551, 1080),
    (0, 0), "olivia sprites/olivia base.png",
    (0, 0), "olivia sprites/olivia brows 2.png",
    (0, 0), "olivia sprites/olivia mouth 3.png",
    (0, 0), "olivia sprites/olivia blush.png",
    (0, 0), "olivia eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "olivia sprites/olivia froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image olivia eyes flushed:
    "olivia sprites/olivia eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "olivia sprites/olivia eyes 1.png"
    .05
    repeat

image olivia flushed z:
    "olivia flushed"
    zoom 1.3
    yoffset 290

## olivia blushing
image olivia blushing = Composite(
    (551, 1080),
    (0, 0), "olivia sprites/olivia base.png",
    (0, 0), "olivia sprites/olivia brows 2.png",
    (0, 0), "olivia sprites/olivia mouth 2.png",
    (0, 0), "olivia sprites/olivia blush.png",
    (0, 0), "olivia eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "olivia sprites/olivia froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image olivia eyes blushing:
    "olivia sprites/olivia eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "olivia sprites/olivia eyes 1.png"
    .05
    repeat

image olivia blushing z:
    "olivia blushing"
    zoom 1.3
    yoffset 290

## olivia smirk
image olivia smirk = Composite(
    (551, 1080),
    (0, 0), "olivia sprites/olivia base.png",
    (0, 0), "olivia sprites/olivia brows 1.png",
    (0, 0), "olivia sprites/olivia mouth 2.png",
    (0, 0), "olivia eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "olivia sprites/olivia froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image olivia eyes smirk:
    "olivia sprites/olivia eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "olivia sprites/olivia eyes 1.png"
    .05
    repeat

image olivia smirk z:
    "olivia smirk"
    zoom 1.3
    yoffset 300

################################################################################
# fox
################################################################################
## fox neutral
image fox neutral = Composite(
    (551, 1080),
    (0, 0), "fox sprites/fox base [ren_outfit].png",
    (0, 0), "fox sprites/fox brows 1.png",
    (0, 0), "fox sprites/fox mouth 1.png",
    (0, 0), "fox eyes neutral",
    )

image fox eyes neutral:
    "fox sprites/fox eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "fox sprites/fox eyes 1.png"
    .05
    repeat

image fox neutral z:
    "fox neutral"
    zoom 1.3
    yoffset 300

## fox happy
image fox happy = Composite(
    (551, 1080),
    (0, 0), "fox sprites/fox base [ren_outfit].png",
    (0, 0), "fox sprites/fox brows 1.png",
    (0, 0), "fox sprites/fox mouth 2.png",
    (0, 0), "fox eyes happy",
    )

image fox eyes happy:
    "fox sprites/fox eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "fox sprites/fox eyes 1.png"
    .05
    repeat

image fox happy z:
    "fox happy"
    zoom 1.3
    yoffset 300

## fox angry
image fox angry = Composite(
    (551, 1080),
    (0, 0), "fox sprites/fox base [ren_outfit].png",
    (0, 0), "fox sprites/fox brows 3.png",
    (0, 0), "fox sprites/fox mouth 4.png",
    (0, 0), "fox eyes angry",
    )

image fox eyes angry:
    "fox sprites/fox eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "fox sprites/fox eyes 1.png"
    .05
    repeat

image fox angry z:
    "fox angry"
    zoom 1.3
    yoffset 300

## fox frown
image fox frown = Composite(
    (551, 1080),
    (0, 0), "fox sprites/fox base [ren_outfit].png",
    (0, 0), "fox sprites/fox brows 3.png",
    (0, 0), "fox sprites/fox mouth 5.png",
    (0, 0), "fox eyes frown",
    )

image fox eyes frown:
    "fox sprites/fox eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "fox sprites/fox eyes 1.png"
    .05
    repeat

image fox frown z:
    "fox frown"
    zoom 1.3
    yoffset 300

## fox sad
image fox sad = Composite(
    (551, 1080),
    (0, 0), "fox sprites/fox base [ren_outfit].png",
    (0, 0), "fox sprites/fox brows 2.png",
    (0, 0), "fox sprites/fox mouth 3.png",
    (0, 0), "fox eyes sad",
    )

image fox eyes sad:
    "fox sprites/fox eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "fox sprites/fox eyes 1.png"
    .05
    repeat

image fox sad z:
    "fox sad"
    zoom 1.3
    yoffset 300

## fox flushed
image fox flushed = Composite(
    (551, 1080),
    (0, 0), "fox sprites/fox base [ren_outfit].png",
    (0, 0), "fox sprites/fox brows 2.png",
    (0, 0), "fox sprites/fox mouth 1.png",
    (0, 0), "fox sprites/fox blush.png",
    (0, 0), "fox eyes flushed",
    )

image fox eyes flushed:
    "fox sprites/fox eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "fox sprites/fox eyes 1.png"
    .05
    repeat

image fox flushed z:
    "fox flushed"
    zoom 1.3
    yoffset 300

## fox blushing
image fox blushing = Composite(
    (551, 1080),
    (0, 0), "fox sprites/fox base [ren_outfit].png",
    (0, 0), "fox sprites/fox brows 3.png",
    (0, 0), "fox sprites/fox mouth 5.png",
    (0, 0), "fox sprites/fox blush.png",
    (0, 0), "fox eyes blushing",
    )

image fox eyes blushing:
    "fox sprites/fox eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "fox sprites/fox eyes 1.png"
    .05
    repeat

image fox blushing z:
    "fox blushing"
    zoom 1.3
    yoffset 300

## fox smirk
image fox smirk = Composite(
    (551, 1080),
    (0, 0), "fox sprites/fox base [ren_outfit].png",
    (0, 0), "fox sprites/fox brows 1.png",
    (0, 0), "fox sprites/fox mouth 1.png",
    (0, 0), "fox eyes smirk",
    )

image fox eyes smirk:
    "fox sprites/fox eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "fox sprites/fox eyes 1.png"
    .05
    repeat

image fox smirk z:
    "fox smirk"
    zoom 1.3
    yoffset 300

################################################################################
# kiara
################################################################################
## kiara neutral
image kiara neutral = Composite(
    (551, 1080),
    (0, 0), "kiara sprites/kiara base.png",
    (0, 0), "kiara sprites/kiara brows 1.png",
    (0, 0), "kiara sprites/kiara mouth 1.png",
    (0, 0), "kiara eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "kiara sprites/kiara froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image kiara eyes neutral:
    "kiara sprites/kiara eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "kiara sprites/kiara eyes 1.png"
    .05
    repeat

image kiara neutral z:
    "kiara neutral"
    zoom 1.3
    yoffset 230

## kiara happy
image kiara happy = Composite(
    (551, 1080),
    (0, 0), "kiara sprites/kiara base.png",
    (0, 0), "kiara sprites/kiara brows 1.png",
    (0, 0), "kiara sprites/kiara mouth 2.png",
    (0, 0), "kiara eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "kiara sprites/kiara froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image kiara eyes happy:
    "kiara sprites/kiara eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "kiara sprites/kiara eyes 1.png"
    .05
    repeat

image kiara happy z:
    "kiara happy"
    zoom 1.3
    yoffset 230

## kiara angry
image kiara angry = Composite(
    (551, 1080),
    (0, 0), "kiara sprites/kiara base.png",
    (0, 0), "kiara sprites/kiara brows 3.png",
    (0, 0), "kiara sprites/kiara mouth 3.png",
    (0, 0), "kiara eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "kiara sprites/kiara froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image kiara eyes angry:
    "kiara sprites/kiara eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "kiara sprites/kiara eyes 1.png"
    .05
    repeat

image kiara angry z:
    "kiara angry"
    zoom 1.3
    yoffset 230

## kiara frown
image kiara frown = Composite(
    (551, 1080),
    (0, 0), "kiara sprites/kiara base.png",
    (0, 0), "kiara sprites/kiara brows 3.png",
    (0, 0), "kiara sprites/kiara mouth 4.png",
    (0, 0), "kiara eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "kiara sprites/kiara froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image kiara eyes frown:
    "kiara sprites/kiara eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "kiara sprites/kiara eyes 1.png"
    .05
    repeat

image kiara frown z:
    "kiara frown"
    zoom 1.3
    yoffset 230

## kiara sad
image kiara sad = Composite(
    (551, 1080),
    (0, 0), "kiara sprites/kiara base.png",
    (0, 0), "kiara sprites/kiara brows 2.png",
    (0, 0), "kiara sprites/kiara mouth 3.png",
    (0, 0), "kiara eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "kiara sprites/kiara froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image kiara eyes sad:
    "kiara sprites/kiara eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "kiara sprites/kiara eyes 1.png"
    .05
    repeat

image kiara sad z:
    "kiara sad"
    zoom 1.3
    yoffset 230

## kiara flushed
image kiara flushed = Composite(
    (551, 1080),
    (0, 0), "kiara sprites/kiara base.png",
    (0, 0), "kiara sprites/kiara brows 2.png",
    (0, 0), "kiara sprites/kiara mouth 3.png",
    (0, 0), "kiara sprites/kiara blush.png",
    (0, 0), "kiara eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "kiara sprites/kiara froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image kiara eyes flushed:
    "kiara sprites/kiara eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "kiara sprites/kiara eyes 1.png"
    .05
    repeat

image kiara flushed z:
    "kiara flushed"
    zoom 1.3
    yoffset 230

## kiara blushing
image kiara blushing = Composite(
    (551, 1080),
    (0, 0), "kiara sprites/kiara base.png",
    (0, 0), "kiara sprites/kiara brows 1.png",
    (0, 0), "kiara sprites/kiara mouth 2.png",
    (0, 0), "kiara sprites/kiara blush.png",
    (0, 0), "kiara eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "kiara sprites/kiara froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image kiara eyes blushing:
    "kiara sprites/kiara eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "kiara sprites/kiara eyes 1.png"
    .05
    repeat

image kiara blushing z:
    "kiara blushing"
    zoom 1.3
    yoffset 230

## kiara smirk
image kiara smirk = Composite(
    (551, 1080),
    (0, 0), "kiara sprites/kiara base.png",
    (0, 0), "kiara sprites/kiara brows 1.png",
    (0, 0), "kiara sprites/kiara mouth 2.png",
    (0, 0), "kiara eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "kiara sprites/kiara froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image kiara eyes smirk:
    "kiara sprites/kiara eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "kiara sprites/kiara eyes 1.png"
    .05
    repeat

image kiara smirk z:
    "kiara smirk"
    zoom 1.3
    yoffset 230

################################################################################
# moth
################################################################################
## moth neutral
image moth neutral = Composite(
    (551, 1080),
    (0, 0), "moth sprites/moth base [moth_outfit].png",
    (0, 0), "moth sprites/moth brows 1.png",
    (0, 0), "moth sprites/moth mouth 1.png",
    (0, 0), "moth eyes neutral",
    (0,0), ConditionSwitch ("froggy_switch == True", "moth sprites/moth froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image moth eyes neutral:
    "moth sprites/moth eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "moth sprites/moth eyes 1.png"
    .05
    repeat

image moth neutral z:
    "moth neutral"
    zoom 1.3
    yoffset 230

## moth happy
image moth happy = Composite(
    (551, 1080),
    (0, 0), "moth sprites/moth base [moth_outfit].png",
    (0, 0), "moth sprites/moth brows 1.png",
    (0, 0), "moth sprites/moth mouth 2.png",
    (0, 0), "moth eyes happy",
    (0,0), ConditionSwitch ("froggy_switch == True", "moth sprites/moth froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image moth eyes happy:
    "moth sprites/moth eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "moth sprites/moth eyes 1.png"
    .05
    repeat

image moth happy z:
    "moth happy"
    zoom 1.3
    yoffset 230

## moth angry
image moth angry = Composite(
    (551, 1080),
    (0, 0), "moth sprites/moth base [moth_outfit].png",
    (0, 0), "moth sprites/moth brows 3.png",
    (0, 0), "moth sprites/moth mouth 3.png",
    (0, 0), "moth eyes angry",
    (0,0), ConditionSwitch ("froggy_switch == True", "moth sprites/moth froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image moth eyes angry:
    "moth sprites/moth eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "moth sprites/moth eyes 1.png"
    .05
    repeat

image moth angry z:
    "moth angry"
    zoom 1.3
    yoffset 230

## moth frown
image moth frown = Composite(
    (551, 1080),
    (0, 0), "moth sprites/moth base [moth_outfit].png",
    (0, 0), "moth sprites/moth brows 3.png",
    (0, 0), "moth sprites/moth mouth 4.png",
    (0, 0), "moth eyes frown",
    (0,0), ConditionSwitch ("froggy_switch == True", "moth sprites/moth froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image moth eyes frown:
    "moth sprites/moth eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "moth sprites/moth eyes 1.png"
    .05
    repeat

image moth frown z:
    "moth frown"
    zoom 1.3
    yoffset 230

## moth sad
image moth sad = Composite(
    (551, 1080),
    (0, 0), "moth sprites/moth base [moth_outfit].png",
    (0, 0), "moth sprites/moth brows 2.png",
    (0, 0), "moth sprites/moth mouth 3.png",
    (0, 0), "moth eyes sad",
    (0,0), ConditionSwitch ("froggy_switch == True", "moth sprites/moth froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image moth eyes sad:
    "moth sprites/moth eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "moth sprites/moth eyes 1.png"
    .05
    repeat

image moth sad z:
    "moth sad"
    zoom 1.3
    yoffset 230

## moth flushed
image moth flushed = Composite(
    (551, 1080),
    (0, 0), "moth sprites/moth base [moth_outfit].png",
    (0, 0), "moth sprites/moth brows 2.png",
    (0, 0), "moth sprites/moth mouth 3.png",
    (0, 0), "moth sprites/moth blush.png",
    (0, 0), "moth eyes flushed",
    (0,0), ConditionSwitch ("froggy_switch == True", "moth sprites/moth froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image moth eyes flushed:
    "moth sprites/moth eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "moth sprites/moth eyes 1.png"
    .05
    repeat

image moth flushed z:
    "moth flushed"
    zoom 1.3
    yoffset 230

## moth blushing
image moth blushing = Composite(
    (551, 1080),
    (0, 0), "moth sprites/moth base [moth_outfit].png",
    (0, 0), "moth sprites/moth brows 1.png",
    (0, 0), "moth sprites/moth mouth 2.png",
    (0, 0), "moth sprites/moth blush.png",
    (0, 0), "moth eyes blushing",
    (0,0), ConditionSwitch ("froggy_switch == True", "moth sprites/moth froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image moth eyes blushing:
    "moth sprites/moth eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "moth sprites/moth eyes 1.png"
    .05
    repeat

image moth blushing z:
    "moth blushing"
    zoom 1.3
    yoffset 230

## moth smirk
image moth smirk = Composite(
    (551, 1080),
    (0, 0), "moth sprites/moth base [moth_outfit].png",
    (0, 0), "moth sprites/moth brows 1.png",
    (0, 0), "moth sprites/moth mouth 1.png",
    (0, 0), "moth eyes smirk",
    (0,0), ConditionSwitch ("froggy_switch == True", "moth sprites/moth froggy.png", "froggy_switch == False", "images/misc/blank.png",),
    )

image moth eyes smirk:
    "moth sprites/moth eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "moth sprites/moth eyes 1.png"
    .05
    repeat

image moth smirk z:
    "moth smirk"
    zoom 1.3
    yoffset 230

################################################################################
# saint
################################################################################
## saint neutral
image saint neutral = Composite(
    (551, 1080),
    (0, 0), "saint sprites/saint base.png",
    (0, 0), "saint sprites/saint brows 1.png",
    (0, 0), "saint sprites/saint mouth 1.png",
    (0, 0), "saint eyes neutral",
    )

image saint eyes neutral:
    "saint sprites/saint eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "saint sprites/saint eyes 1.png"
    .05
    repeat

image saint neutral z:
    "saint neutral"
    zoom 1.3
    yoffset 300

## saint happy
image saint happy = Composite(
    (551, 1080),
    (0, 0), "saint sprites/saint base.png",
    (0, 0), "saint sprites/saint brows 1.png",
    (0, 0), "saint sprites/saint mouth 2.png",
    (0, 0), "saint eyes happy",
    )

image saint eyes happy:
    "saint sprites/saint eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "saint sprites/saint eyes 1.png"
    .05
    repeat

image saint happy z:
    "saint happy"
    zoom 1.3
    yoffset 300

## saint angry
image saint angry = Composite(
    (551, 1080),
    (0, 0), "saint sprites/saint base.png",
    (0, 0), "saint sprites/saint brows 3.png",
    (0, 0), "saint sprites/saint mouth 3.png",
    (0, 0), "saint eyes angry",
    )

image saint eyes angry:
    "saint sprites/saint eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "saint sprites/saint eyes 1.png"
    .05
    repeat

image saint angry z:
    "saint angry"
    zoom 1.3
    yoffset 300

## saint frown
image saint frown = Composite(
    (551, 1080),
    (0, 0), "saint sprites/saint base.png",
    (0, 0), "saint sprites/saint brows 3.png",
    (0, 0), "saint sprites/saint mouth 4.png",
    (0, 0), "saint eyes frown",
    )

image saint eyes frown:
    "saint sprites/saint eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "saint sprites/saint eyes 1.png"
    .05
    repeat

image saint frown z:
    "saint frown"
    zoom 1.3
    yoffset 300

## saint sad
image saint sad = Composite(
    (551, 1080),
    (0, 0), "saint sprites/saint base.png",
    (0, 0), "saint sprites/saint brows 2.png",
    (0, 0), "saint sprites/saint mouth 3.png",
    (0, 0), "saint eyes sad",
    )

image saint eyes sad:
    "saint sprites/saint eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "saint sprites/saint eyes 1.png"
    .05
    repeat

image saint sad z:
    "saint sad"
    zoom 1.3
    yoffset 300

## saint flushed
image saint flushed = Composite(
    (551, 1080),
    (0, 0), "saint sprites/saint base.png",
    (0, 0), "saint sprites/saint brows 2.png",
    (0, 0), "saint sprites/saint mouth 3.png",
    (0, 0), "saint sprites/saint blush.png",
    (0, 0), "saint eyes flushed",
    )

image saint eyes flushed:
    "saint sprites/saint eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "saint sprites/saint eyes 1.png"
    .05
    repeat

image saint flushed z:
    "saint flushed"
    zoom 1.3
    yoffset 300

## saint blushing
image saint blushing = Composite(
    (551, 1080),
    (0, 0), "saint sprites/saint base.png",
    (0, 0), "saint sprites/saint brows 2.png",
    (0, 0), "saint sprites/saint mouth 2.png",
    (0, 0), "saint sprites/saint blush.png",
    (0, 0), "saint eyes blushing",
    )

image saint eyes blushing:
    "saint sprites/saint eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "saint sprites/saint eyes 1.png"
    .05
    repeat

image saint blushing z:
    "saint blushing"
    zoom 1.3
    yoffset 300

## saint smirk
image saint smirk = Composite(
    (551, 1080),
    (0, 0), "saint sprites/saint base.png",
    (0, 0), "saint sprites/saint brows 3.png",
    (0, 0), "saint sprites/saint mouth 1.png",
    (0, 0), "saint eyes smirk",
    )

image saint eyes smirk:
    "saint sprites/saint eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "saint sprites/saint eyes 1.png"
    .05
    repeat

image saint smirk z:
    "saint smirk"
    zoom 1.3
    yoffset 300

################################################################################
# rosie
################################################################################
## rosie neutral
image rosie neutral = Composite(
    (551, 1080),
    (0, 0), "rosie sprites/rosie base.png",
    (0, 0), "rosie sprites/rosie brows 1.png",
    (0, 0), "rosie sprites/rosie mouth 1.png",
    (0, 0), "rosie eyes neutral",
    )

image rosie eyes neutral:
    "rosie sprites/rosie eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "rosie sprites/rosie eyes 1.png"
    .05
    repeat

image rosie neutral z:
    "rosie neutral"
    zoom 1.3
    yoffset 300

## rosie happy
image rosie happy = Composite(
    (551, 1080),
    (0, 0), "rosie sprites/rosie base.png",
    (0, 0), "rosie sprites/rosie brows 1.png",
    (0, 0), "rosie sprites/rosie mouth 2.png",
    (0, 0), "rosie eyes happy",
    )

image rosie eyes happy:
    "rosie sprites/rosie eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "rosie sprites/rosie eyes 1.png"
    .05
    repeat

image rosie happy z:
    "rosie happy"
    zoom 1.3
    yoffset 300

## rosie angry
image rosie angry = Composite(
    (551, 1080),
    (0, 0), "rosie sprites/rosie base.png",
    (0, 0), "rosie sprites/rosie brows 3.png",
    (0, 0), "rosie sprites/rosie mouth 3.png",
    (0, 0), "rosie eyes angry",
    )

image rosie eyes angry:
    "rosie sprites/rosie eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "rosie sprites/rosie eyes 1.png"
    .05
    repeat

image rosie angry z:
    "rosie angry"
    zoom 1.3
    yoffset 300

## rosie frown
image rosie frown = Composite(
    (551, 1080),
    (0, 0), "rosie sprites/rosie base.png",
    (0, 0), "rosie sprites/rosie brows 3.png",
    (0, 0), "rosie sprites/rosie mouth 4.png",
    (0, 0), "rosie eyes frown",
    )

image rosie eyes frown:
    "rosie sprites/rosie eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "rosie sprites/rosie eyes 1.png"
    .05
    repeat

image rosie frown z:
    "rosie frown"
    zoom 1.3
    yoffset 300

## rosie sad
image rosie sad = Composite(
    (551, 1080),
    (0, 0), "rosie sprites/rosie base.png",
    (0, 0), "rosie sprites/rosie brows 2.png",
    (0, 0), "rosie sprites/rosie mouth 3.png",
    (0, 0), "rosie eyes sad",
    )

image rosie eyes sad:
    "rosie sprites/rosie eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "rosie sprites/rosie eyes 1.png"
    .05
    repeat

image rosie sad z:
    "rosie sad"
    zoom 1.3
    yoffset 300

## rosie flushed
image rosie flushed = Composite(
    (551, 1080),
    (0, 0), "rosie sprites/rosie base.png",
    (0, 0), "rosie sprites/rosie brows 2.png",
    (0, 0), "rosie sprites/rosie mouth 3.png",
    (0, 0), "rosie sprites/rosie blush.png",
    (0, 0), "rosie eyes flushed",
    )

image rosie eyes flushed:
    "rosie sprites/rosie eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "rosie sprites/rosie eyes 1.png"
    .05
    repeat

image rosie flushed z:
    "rosie flushed"
    zoom 1.3
    yoffset 300

## rosie blushing
image rosie blushing = Composite(
    (551, 1080),
    (0, 0), "rosie sprites/rosie base.png",
    (0, 0), "rosie sprites/rosie brows 2.png",
    (0, 0), "rosie sprites/rosie mouth 2.png",
    (0, 0), "rosie sprites/rosie blush.png",
    (0, 0), "rosie eyes blushing",
    )

image rosie eyes blushing:
    "rosie sprites/rosie eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "rosie sprites/rosie eyes 1.png"
    .05
    repeat

image rosie blushing z:
    "rosie blushing"
    zoom 1.3
    yoffset 300

## rosie smirk
image rosie smirk = Composite(
    (551, 1080),
    (0, 0), "rosie sprites/rosie base.png",
    (0, 0), "rosie sprites/rosie brows 3.png",
    (0, 0), "rosie sprites/rosie mouth 2.png",
    (0, 0), "rosie eyes smirk",
    )

image rosie eyes smirk:
    "rosie sprites/rosie eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "rosie sprites/rosie eyes 1.png"
    .05
    repeat

image rosie smirk z:
    "rosie smirk"
    zoom 1.3
    yoffset 300

################################################################################
# nate
################################################################################
## nate neutral
image nate neutral = Composite(
    (551, 1080),
    (0, 0), "nate sprites/nate base.png",
    (0, 0), "nate sprites/nate brows 1.png",
    (0, 0), "nate sprites/nate mouth 1.png",
    (0, 0), "nate eyes neutral",
    )

image nate eyes neutral:
    "nate sprites/nate eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "nate sprites/nate eyes 1.png"
    .05
    repeat

image nate neutral z:
    "nate neutral"
    zoom 1.3
    yoffset 300

## nate happy
image nate happy = Composite(
    (551, 1080),
    (0, 0), "nate sprites/nate base.png",
    (0, 0), "nate sprites/nate brows 1.png",
    (0, 0), "nate sprites/nate mouth 2.png",
    (0, 0), "nate eyes happy",
    )

image nate eyes happy:
    "nate sprites/nate eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "nate sprites/nate eyes 1.png"
    .05
    repeat

image nate happy z:
    "nate happy"
    zoom 1.3
    yoffset 300

## nate angry
image nate angry = Composite(
    (551, 1080),
    (0, 0), "nate sprites/nate base.png",
    (0, 0), "nate sprites/nate brows 3.png",
    (0, 0), "nate sprites/nate mouth 3.png",
    (0, 0), "nate eyes angry",
    )

image nate eyes angry:
    "nate sprites/nate eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "nate sprites/nate eyes 1.png"
    .05
    repeat

image nate angry z:
    "nate angry"
    zoom 1.3
    yoffset 300

## nate frown
image nate frown = Composite(
    (551, 1080),
    (0, 0), "nate sprites/nate base.png",
    (0, 0), "nate sprites/nate brows 3.png",
    (0, 0), "nate sprites/nate mouth 4.png",
    (0, 0), "nate eyes frown",
    )

image nate eyes frown:
    "nate sprites/nate eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "nate sprites/nate eyes 1.png"
    .05
    repeat

image nate frown z:
    "nate frown"
    zoom 1.3
    yoffset 300

## nate sad
image nate sad = Composite(
    (551, 1080),
    (0, 0), "nate sprites/nate base.png",
    (0, 0), "nate sprites/nate brows 2.png",
    (0, 0), "nate sprites/nate mouth 3.png",
    (0, 0), "nate eyes sad",
    )

image nate eyes sad:
    "nate sprites/nate eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "nate sprites/nate eyes 1.png"
    .05
    repeat

image nate sad z:
    "nate sad"
    zoom 1.3
    yoffset 300

## nate flushed
image nate flushed = Composite(
    (551, 1080),
    (0, 0), "nate sprites/nate base.png",
    (0, 0), "nate sprites/nate brows 2.png",
    (0, 0), "nate sprites/nate mouth 4.png",
    (0, 0), "nate sprites/nate blush.png",
    (0, 0), "nate eyes flushed",
    )

image nate eyes flushed:
    "nate sprites/nate eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "nate sprites/nate eyes 1.png"
    .05
    repeat

image nate flushed z:
    "nate flushed"
    zoom 1.3
    yoffset 300

## nate blushing
image nate blushing = Composite(
    (551, 1080),
    (0, 0), "nate sprites/nate base.png",
    (0, 0), "nate sprites/nate brows 2.png",
    (0, 0), "nate sprites/nate mouth 2.png",
    (0, 0), "nate sprites/nate blush.png",
    (0, 0), "nate eyes blushing",
    )

image nate eyes blushing:
    "nate sprites/nate eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "nate sprites/nate eyes 1.png"
    .05
    repeat

image nate blushing z:
    "nate blushing"
    zoom 1.3
    yoffset 300

## nate smirk
image nate smirk = Composite(
    (551, 1080),
    (0, 0), "nate sprites/nate base.png",
    (0, 0), "nate sprites/nate brows 3.png",
    (0, 0), "nate sprites/nate mouth 1.png",
    (0, 0), "nate eyes smirk",
    )

image nate eyes smirk:
    "nate sprites/nate eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "nate sprites/nate eyes 1.png"
    .05
    repeat

image nate smirk z:
    "nate smirk"
    zoom 1.3
    yoffset 300

### this is so scuffed lmao
image side side_ren:
    "icon_ren"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_moth:
    "icon_moth"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_violet:
    "icon_violet"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_elanor:
    "icon_elanor"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_conan:
    "icon_conan"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_jae:
    "icon_jae"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_leon:
    "icon_leon"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_teo:
    "icon_teo"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_olivia:
    "icon_olivia"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_kiara:
    "icon_kiara"
    align (0.12,0.82)
    anchor (0.5,0.5)

image side side_default:
    "icon_default"
    align (0.12,0.82)
    anchor (0.5,0.5)

################################################################################
# beau
################################################################################
## beau neutral
image beau neutral = Composite(
    (551, 1080),
    (0, 0), "beau sprites/beau base.png",
    (0, 0), "beau sprites/beau brows 1.png",
    (0, 0), "beau sprites/beau mouth 1.png",
    (0, 0), "beau eyes neutral",
    )

image beau eyes neutral:
    "beau sprites/beau eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "beau sprites/beau eyes 1.png"
    .05
    repeat

image beau neutral z:
    "beau neutral"
    zoom 1.3
    yoffset 300

## beau happy
image beau happy = Composite(
    (551, 1080),
    (0, 0), "beau sprites/beau base.png",
    (0, 0), "beau sprites/beau brows 1.png",
    (0, 0), "beau sprites/beau mouth 2.png",
    (0, 0), "beau eyes happy",
    )

image beau eyes happy:
    "beau sprites/beau eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "beau sprites/beau eyes 1.png"
    .05
    repeat

image beau happy z:
    "beau happy"
    zoom 1.3
    yoffset 300

## beau angry
image beau angry = Composite(
    (551, 1080),
    (0, 0), "beau sprites/beau base.png",
    (0, 0), "beau sprites/beau brows 3.png",
    (0, 0), "beau sprites/beau mouth 3.png",
    (0, 0), "beau eyes angry",
    )

image beau eyes angry:
    "beau sprites/beau eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "beau sprites/beau eyes 1.png"
    .05
    repeat

image beau angry z:
    "beau angry"
    zoom 1.3
    yoffset 300

## beau frown
image beau frown = Composite(
    (551, 1080),
    (0, 0), "beau sprites/beau base.png",
    (0, 0), "beau sprites/beau brows 3.png",
    (0, 0), "beau sprites/beau mouth 4.png",
    (0, 0), "beau eyes frown",
    )

image beau eyes frown:
    "beau sprites/beau eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "beau sprites/beau eyes 1.png"
    .05
    repeat

image beau frown z:
    "beau frown"
    zoom 1.3
    yoffset 300

## beau sad
image beau sad = Composite(
    (551, 1080),
    (0, 0), "beau sprites/beau base.png",
    (0, 0), "beau sprites/beau brows 2.png",
    (0, 0), "beau sprites/beau mouth 3.png",
    (0, 0), "beau eyes sad",
    )

image beau eyes sad:
    "beau sprites/beau eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "beau sprites/beau eyes 1.png"
    .05
    repeat

image beau sad z:
    "beau sad"
    zoom 1.3
    yoffset 300

## beau flushed
image beau flushed = Composite(
    (551, 1080),
    (0, 0), "beau sprites/beau base.png",
    (0, 0), "beau sprites/beau brows 2.png",
    (0, 0), "beau sprites/beau mouth 2.png",
    (0, 0), "beau sprites/beau blush.png",
    (0, 0), "beau eyes flushed",
    )

image beau eyes flushed:
    "beau sprites/beau eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "beau sprites/beau eyes 1.png"
    .05
    repeat

image beau flushed z:
    "beau flushed"
    zoom 1.3
    yoffset 300

## beau blushing
image beau blushing = Composite(
    (551, 1080),
    (0, 0), "beau sprites/beau base.png",
    (0, 0), "beau sprites/beau brows 2.png",
    (0, 0), "beau sprites/beau mouth 2.png",
    (0, 0), "beau sprites/beau blush.png",
    (0, 0), "beau eyes blushing",
    )

image beau eyes blushing:
    "beau sprites/beau eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "beau sprites/beau eyes 1.png"
    .05
    repeat

image beau blushing z:
    "beau blushing"
    zoom 1.3
    yoffset 300

## beau smirk
image beau smirk = Composite(
    (551, 1080),
    (0, 0), "beau sprites/beau base.png",
    (0, 0), "beau sprites/beau brows 3.png",
    (0, 0), "beau sprites/beau mouth 1.png",
    (0, 0), "beau eyes smirk",
    )

image beau eyes smirk:
    "beau sprites/beau eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "beau sprites/beau eyes 1.png"
    .05
    repeat

image beau smirk z:
    "beau smirk"
    zoom 1.3
    yoffset 300

################################################################################
# haruka
################################################################################
## haruka neutral
image haruka neutral = Composite(
    (551, 1080),
    (0, 0), "haruka sprites/haruka base.png",
    (0, 0), "haruka sprites/haruka brows 1.png",
    (0, 0), "haruka sprites/haruka mouth 1.png",
    (0, 0), "haruka eyes neutral",
    )

image haruka eyes neutral:
    "haruka sprites/haruka eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "haruka sprites/haruka eyes 1.png"
    .05
    repeat

image haruka neutral z:
    "haruka neutral"
    zoom 1.3
    yoffset 300

## haruka happy
image haruka happy = Composite(
    (551, 1080),
    (0, 0), "haruka sprites/haruka base.png",
    (0, 0), "haruka sprites/haruka brows 1.png",
    (0, 0), "haruka sprites/haruka mouth 2.png",
    (0, 0), "haruka eyes happy",
    )

image haruka eyes happy:
    "haruka sprites/haruka eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "haruka sprites/haruka eyes 1.png"
    .05
    repeat

image haruka happy z:
    "haruka happy"
    zoom 1.3
    yoffset 300

## haruka angry
image haruka angry = Composite(
    (551, 1080),
    (0, 0), "haruka sprites/haruka base.png",
    (0, 0), "haruka sprites/haruka brows 3.png",
    (0, 0), "haruka sprites/haruka mouth 3.png",
    (0, 0), "haruka eyes angry",
    )

image haruka eyes angry:
    "haruka sprites/haruka eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "haruka sprites/haruka eyes 1.png"
    .05
    repeat

image haruka angry z:
    "haruka angry"
    zoom 1.3
    yoffset 300

## haruka frown
image haruka frown = Composite(
    (551, 1080),
    (0, 0), "haruka sprites/haruka base.png",
    (0, 0), "haruka sprites/haruka brows 3.png",
    (0, 0), "haruka sprites/haruka mouth 3.png",
    (0, 0), "haruka eyes frown",
    )

image haruka eyes frown:
    "haruka sprites/haruka eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "haruka sprites/haruka eyes 1.png"
    .05
    repeat

image haruka frown z:
    "haruka frown"
    zoom 1.3
    yoffset 300

## haruka sad
image haruka sad = Composite(
    (551, 1080),
    (0, 0), "haruka sprites/haruka base.png",
    (0, 0), "haruka sprites/haruka brows 2.png",
    (0, 0), "haruka sprites/haruka mouth 3.png",
    (0, 0), "haruka eyes sad",
    )

image haruka eyes sad:
    "haruka sprites/haruka eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "haruka sprites/haruka eyes 1.png"
    .05
    repeat

image haruka sad z:
    "haruka sad"
    zoom 1.3
    yoffset 300

## haruka flushed
image haruka flushed = Composite(
    (551, 1080),
    (0, 0), "haruka sprites/haruka base.png",
    (0, 0), "haruka sprites/haruka brows 2.png",
    (0, 0), "haruka sprites/haruka mouth 2.png",
    (0, 0), "haruka sprites/haruka blush.png",
    (0, 0), "haruka eyes flushed",
    )

image haruka eyes flushed:
    "haruka sprites/haruka eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "haruka sprites/haruka eyes 1.png"
    .05
    repeat

image haruka flushed z:
    "haruka flushed"
    zoom 1.3
    yoffset 300

## haruka blushing
image haruka blushing = Composite(
    (551, 1080),
    (0, 0), "haruka sprites/haruka base.png",
    (0, 0), "haruka sprites/haruka brows 2.png",
    (0, 0), "haruka sprites/haruka mouth 2.png",
    (0, 0), "haruka sprites/haruka blush.png",
    (0, 0), "haruka eyes blushing",
    )

image haruka eyes blushing:
    "haruka sprites/haruka eyes 3.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "haruka sprites/haruka eyes 1.png"
    .05
    repeat

image haruka blushing z:
    "haruka blushing"
    zoom 1.3
    yoffset 300

## haruka smirk
image haruka smirk = Composite(
    (551, 1080),
    (0, 0), "haruka sprites/haruka base.png",
    (0, 0), "haruka sprites/haruka brows 3.png",
    (0, 0), "haruka sprites/haruka mouth 1.png",
    (0, 0), "haruka eyes smirk",
    )

image haruka eyes smirk:
    "haruka sprites/haruka eyes 2.png"
    choice:
        1.5
    choice:
        4.5
    choice:
        2.5
    "haruka sprites/haruka eyes 1.png"
    .05
    repeat

image haruka smirk z:
    "haruka smirk"
    zoom 1.3
    yoffset 300

################################################################################
# MOTH PHONE SPRITE
################################################################################
image mothphone neutral = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth neutral z", crop=(85, 100, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone happy = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth happy z", crop=(85, 100, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone angry = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth angry z", crop=(85, 100, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone frown = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth frown z", crop=(85, 100, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone sad = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth sad z", crop=(85, 100, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone flushed = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth flushed z", crop=(85, 100, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone blushing = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth blushing z", crop=(85, 100, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone smirk = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth smirk z", crop=(85, 100, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone error = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask("images/bg/other_dark.webp","phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

image mothphone bg = Composite(
    (551, 1080),
    (0, 0), "phone/phone shadow.png",
    (0, 0), "phone/phone back.png",
    (0, 0), AlphaMask(Transform("moth smirk z", zoom=2.5, crop=(180, 30, 551, 1200)), 
    mask="phone/phone back.png"),
    (0, 0), "phone/phone front.png",
    )

################################################################################
# MISC STUFF YAHOO
################################################################################
image glitch_1 = "images/effects/glitch.png"
image glitch_2 = "images/effects/glitch 2.webp"
image true_red = "#850106"
image ghost_olivia = "misc/hehe/ghostolivia.png"
image ghost_teo = "misc/hehe/ghostteo.png"

################################################################################
# PROFILE STUFF
################################################################################
image angel_icon2 = ConditionSwitch(
    "angel_icon == 'sprite'", "picon_angelsprite",
    "angel_icon == 'def'", "gui/socials/icons/custom/icon_angel.png",
    "angel_icon == 'alt'", "gui/socials/icons/custom/icon_angelalt.png",
    "angel_icon == 'haruko'", "gui/socials/icons/custom/icon_haruko.png",
    "angel_icon == 'mon'", "gui/socials/icons/custom/icon_mod_mon.png",
    "angel_icon == 'ten'", "gui/socials/icons/custom/icon_mod_ten.png",
    "angel_icon == 'puppy'", "gui/socials/icons/custom/icon_mod_puppy.png",
    "angel_icon == 'rosie'", "gui/socials/icons/custom/icon_mod_rosie.png",
    "angel_icon == 'chii'", "gui/socials/icons/custom/icon_mod_chii.png",
    "angel_icon == 'shalls'", "gui/socials/icons/custom/icon_mod_shalls.png",
    "angel_icon == 'eve'", "gui/socials/icons/custom/icon_mod_eve.png",
    "angel_icon == 'cutiesai'", "gui/socials/icons/custom/icon_cutiesai.png",
    "angel_icon == 'teo'", "gui/socials/icons/custom/icon_honkers_teo.png",
    "angel_icon == 'ren'", "gui/socials/icons/custom/icon_honkers_ren.png",
    "angel_icon == 'redacted'", "gui/socials/icons/custom/icon_redacted.png",
    "angel_icon == 'ayaya'", "gui/socials/icons/custom/icon_renayaya.png",
)

image icon_profile = Composite(
    (98,98),
    (0,0), AlphaMask(Transform("angel_icon2"),
    mask="gui/socials/icons/icon_base.png"),
)

image icon_sprite = Composite(
    (98,98),
    (0,0), AlphaMask(Transform("socials_neutral", zoom=7.0, crop=(20, 0, 150, 150)), mask="gui/socials/icons/icon_base.png"),
    (0,0), AlphaMask(Transform("player_sprite", zoom=1.4, crop=(-3, 0, 150, 150)), mask="gui/socials/icons/icon_base.png"),
)

image icon_angel = Composite(
    (98,98),
    (0,0), AlphaMask(Transform("angel_icon2"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_angel"
)

image icon_ren = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_ren.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_ren",
)

image icon_moth = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/custom/icon_haruko.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_moth",
)

image icon_violet = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_violet.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_violet",
)

image icon_elanor = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_elanor.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_elanor",
)

image icon_conan = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_conan.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_conan",
)

image icon_jae = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_jae.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_jae",
)

image icon_leon = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_leon.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_leon",
)

image icon_teo = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_teo.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_teo",
)

image icon_olivia = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_olivia.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_olivia",
)

image icon_kiara = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_kiara.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_kiara",
)

image icon_default = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_default.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_default",
)

image icon_redacted = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_redacted.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_redacted",
)

image icon_river = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/cast/icon_river.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_river",
)
################################################################################
# MAIN MENU STUFF
################################################################################
image menu_ren = Composite(
    (1100,660),
    (0,0), AlphaMask(Transform("ren cg/mm/mainmenu_cg.png", zoom = 0.61),
    mask="gui/boxes/frames/menu_background.png"),
    (0,0), "gui/boxes/frames/menu_frame.png"
)

################################################################################
# DLC IMAGES
################################################################################
image 14NWY symbol:
    "gui/ui/dlc icon.png"

image 14NWY symbol alt:
    "gui/ui/dlc icon alt.png"

################################################################################
# SOCIALS SCREEN STUFF
################################################################################
## heart colours
image heart_love:
    "gui/base/heart_tint.png"
    matrixcolor TintMatrix("#F57BAA")

image heart_like:
    "gui/base/heart_tint.png"
    matrixcolor TintMatrix("#87DA6E")

image heart_neutral:
    "gui/base/heart_tint.png"
    matrixcolor TintMatrix("#7BAAF5")

image heart_dislike:
    "gui/base/heart_tint.png"
    matrixcolor TintMatrix("#E85858")

image heart_empty:
    "gui/base/heart_tint.png"
    matrixcolor TintMatrix("#A6A6A6")

image heart_terminated:
    "gui/base/heart_tint.png"
    matrixcolor TintMatrix("#141414")

## username colours
image socials_angel:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#9d64fd")

image socials_ren:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#ff66cb")

image socials_moth:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#5269b9")

image socials_violet:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#c6b3f8")

image socials_elanor:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#d8c365")

image socials_conan:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#98d2ff")

image socials_jae:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#faa97e")

image socials_leon:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#ee6c6d")

image socials_teo:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#93b482")

image socials_olivia:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#a8a7a7")

image socials_kiara:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#b18f84")

image socials_neutral:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#d4d4d4")

image socials_offblack:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#282828")

image socials_black:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#141414")

image socials_redacted:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#141414")

image socials_river:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#80322F")

## icon border colours
image border_angel:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#9d64fd")

image border_ren:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#ff66cb")

image border_moth:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#5269b9")

image border_violet:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#c6b3f8")

image border_elanor:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#d8c365")

image border_conan:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#98d2ff")

image border_jae:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#faa97e")

image border_leon:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#ee6c6d")

image border_teo:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#93b482")

image border_olivia:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#a8a7a7")

image border_kiara:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#b18f84")

image border_default:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#141414")

image border_redacted:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#141414")

image border_river:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#80322F")

################################################################################
# PROFILE ICONS BECAUSE I AM NAWT MAKING 3291 .PNG VARIATIONS
################################################################################
## Angel
image picon_angel:
    "gui/socials/icons/custom/icon_angel.png"

image picon_angel_hover:
    "gui/socials/icons/custom/icon_angel.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_angel_selected:
    "gui/socials/icons/custom/icon_angel.png"
    matrixcolor SaturationMatrix (0.2)

## Angel alt
image picon_angelalt:
    "gui/socials/icons/custom/icon_angelalt.png"
    
image picon_angelalt_hover:
    "gui/socials/icons/custom/icon_angelalt.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_angelalt_selected:
    "gui/socials/icons/custom/icon_angelalt.png"
    matrixcolor SaturationMatrix (0.2)

## Angel sprite
image picon_angelsprite = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("socials_neutral", zoom=7.0, crop=(20, 0, 150, 150)), mask="gui/socials/icons/custom/icon_angel.png"),
    (0,0), AlphaMask(Transform("player_sprite", zoom=1.4, crop=(-4, 0, 150, 150)), mask="gui/socials/icons/custom/icon_angel.png"),
)

image picon_angelsprite_hover:
    "picon_angelsprite"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_angelsprite_selected:
    "picon_angelsprite"
    matrixcolor SaturationMatrix (0.2)

## Teo honkers
image picon_teohonkers:
    "gui/socials/icons/custom/icon_honkers_teo.png"
    
image picon_teohonkers_hover:
    "gui/socials/icons/custom/icon_honkers_teo.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_teohonkers_selected:
    "gui/socials/icons/custom/icon_honkers_teo.png"
    matrixcolor SaturationMatrix (0.2)

## Ren honkers
image picon_renhonkers:
    "gui/socials/icons/custom/icon_honkers_ren.png"
    
image picon_renhonkers_hover:
    "gui/socials/icons/custom/icon_honkers_ren.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_renhonkers_selected:
    "gui/socials/icons/custom/icon_honkers_ren.png"
    matrixcolor SaturationMatrix (0.2)

## Ren ayaya
image picon_renayaya:
    "gui/socials/icons/custom/icon_renayaya.png"
    
image picon_renayaya_hover:
    "gui/socials/icons/custom/icon_renayaya.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_renayaya_selected:
    "gui/socials/icons/custom/icon_renayaya.png"
    matrixcolor SaturationMatrix (0.2)

## Redacted
image picon_redacted:
    "gui/socials/icons/custom/icon_redacted.png"
    
image picon_redacted_hover:
    "gui/socials/icons/custom/icon_redacted.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_redacted_selected:
    "gui/socials/icons/custom/icon_redacted.png"
    matrixcolor SaturationMatrix (0.2)

## cutiesai
image picon_cutiesai:
    "gui/socials/icons/custom/icon_cutiesai.png"
    
image picon_cutiesai_hover:
    "gui/socials/icons/custom/icon_cutiesai.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_cutiesai_selected:
    "gui/socials/icons/custom/icon_cutiesai.png"
    matrixcolor SaturationMatrix (0.2)

## Mon
image picon_mon:
    "gui/socials/icons/custom/icon_mod_mon.png"
    
image picon_mon_hover:
    "gui/socials/icons/custom/icon_mod_mon.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_mon_selected:
    "gui/socials/icons/custom/icon_mod_mon.png"
    matrixcolor SaturationMatrix (0.2)

## Ten
image picon_ten:
    "gui/socials/icons/custom/icon_mod_ten.png"
    
image picon_ten_hover:
    "gui/socials/icons/custom/icon_mod_ten.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_ten_selected:
    "gui/socials/icons/custom/icon_mod_ten.png"
    matrixcolor SaturationMatrix (0.2)

## Puppy
image picon_puppy:
    "gui/socials/icons/custom/icon_mod_puppy.png"
    
image picon_puppy_hover:
    "gui/socials/icons/custom/icon_mod_puppy.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_puppy_selected:
    "gui/socials/icons/custom/icon_mod_puppy.png"
    matrixcolor SaturationMatrix (0.2)

## Chii
image picon_chii:
    "gui/socials/icons/custom/icon_mod_chii.png"
    
image picon_chii_hover:
    "gui/socials/icons/custom/icon_mod_chii.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_chii_selected:
    "gui/socials/icons/custom/icon_mod_chii.png"
    matrixcolor SaturationMatrix (0.2)

## Eve
image picon_eve:
    "gui/socials/icons/custom/icon_mod_eve.png"
    
image picon_eve_hover:
    "gui/socials/icons/custom/icon_mod_eve.png"
    matrixcolor BrightnessMatrix (0.2)
    matrixcolor TintMatrix("#9d64fd")

image picon_eve_selected:
    "gui/socials/icons/custom/icon_mod_eve.png"
    matrixcolor SaturationMatrix (0.2)

################################################################################
# MISC
################################################################################
image bubble_bottomright:
    "gui/boxes/bubble_black.png"
    yzoom -1.0

image bubble_topright:
    "gui/boxes/bubble_black.png"

image icon_cutiesai = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/custom/icon_cutiesai.png"),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_cutiesai",
)

image border_cutiesai:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#eaadd2")

image socials_cutiesai:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#eaadd2")

image icon_10chimes = Composite(
    (150,150),
    (0,0), AlphaMask(Transform("gui/socials/icons/custom/icon_mod_ten.png", zoom=1.3, crop=(25, 10, 150, 150)),
    mask="gui/socials/icons/icon_base.png"),
    (0,0), "border_10chimes",
)
image border_10chimes:
    "gui/base/border_tint.png"
    matrixcolor TintMatrix("#70a47f")

image socials_10chimes:
    "gui/base/socials_tint.png"
    matrixcolor TintMatrix("#70a47f")

image demo_cutiesai_idle:
    "icon_cutiesai"
    zoom 0.6

image demo_cutiesai_hover:
    "icon_cutiesai"
    matrixcolor TintMatrix("#ffcdeb")
    zoom 0.6

## misc colours
image status_box:
    "gui/base/status_tint.png"
    matrixcolor TintMatrix("#EEEEEE")


################################################################################
## lil pixel sprites that i spent 5 minutes on lmao
################################################################################
image sprite_ren:
    "gui/socials/sprites/ren.png"
image sprite_moth:
    "gui/socials/sprites/moth.png"
image sprite_violet:
    "gui/socials/sprites/violet.png"
image sprite_elanor:
    "gui/socials/sprites/elanor.png"
image sprite_conan:
    "gui/socials/sprites/conan.png"
image sprite_jae:
    "gui/socials/sprites/jae.png"
image sprite_leon:
    "gui/socials/sprites/leon.png"
image sprite_teo:
    "gui/socials/sprites/teo.png"
image sprite_olivia:
    "gui/socials/sprites/olivia.png"
image sprite_kiara:
    "gui/socials/sprites/kiara.png"

## idle and hover stuff (test)
image sprite_ren_idle:
    "gui/socials/sprites/ren.png"
image sprite_moth_idle:
    "gui/socials/sprites/moth.png"
image sprite_violet_idle:
    "gui/socials/sprites/violet.png"
image sprite_elanor_idle:
    "gui/socials/sprites/elanor.png"
image sprite_conan_idle:
    "gui/socials/sprites/conan.png"
image sprite_jae_idle:
    "gui/socials/sprites/jae.png"
image sprite_leon_idle:
    "gui/socials/sprites/leon.png"
image sprite_teo_idle:
    "gui/socials/sprites/teo.png"
image sprite_olivia_idle:
    "gui/socials/sprites/olivia.png"
image sprite_kiara_idle:
    "gui/socials/sprites/kiara.png"

image sprite_ren_hover:
    "gui/socials/sprites/ren.png"
image sprite_moth_hover:
    "gui/socials/sprites/moth.png"
image sprite_violet_hover:
    "gui/socials/sprites/violet.png"
image sprite_elanor_hover:
    "gui/socials/sprites/elanor.png"
image sprite_conan_hover:
    "gui/socials/sprites/conan.png"
image sprite_jae_hover:
    "gui/socials/sprites/jae.png"
image sprite_leon_hover:
    "gui/socials/sprites/leon.png"
image sprite_teo_hover:
    "gui/socials/sprites/teo.png"
image sprite_olivia_hover:
    "gui/socials/sprites/olivia.png"
image sprite_kiara_hover:
    "gui/socials/sprites/kiara.png"

################################################################################
## character customisation icons/buttons
################################################################################
image customisation_eyes_1_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/eyes 1.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_eyes_2_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/eyes 2.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_face_1_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/face/face 1.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_face_2_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/face/face 2.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_hair_1_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 1.png", crop=(5, 15, 70, 70), zoom=2.0),
)

image customisation_hair_2_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 2.png", crop=(15, 10, 70, 70), zoom=2.0),
)

image customisation_hair_3_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 3.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_4_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 4.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_5_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 5.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_hair_6_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 6.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_hair_7_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 7.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_8_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.35,0.47), Text("NO HAIR", color="#000000", size=20, font="Assistant-Regular.ttf"),
)

image customisation_body_1_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/clothes/body 1.png", crop=(15, 90, 70, 70), zoom=2.0),
)

image customisation_body_2_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/clothes/body 2.png", crop=(15, 90, 70, 70), zoom=2.0),
)

image customisation_lashes_1_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.3,0.47), Text("NO LASHES", color="#000000", size=20, font="Assistant-Regular.ttf"),
)

image customisation_lashes_2_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/lashes 1.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_lashes_3_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#8f8f8f")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/lashes 2.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_eyes_1_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/eyes 1.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_eyes_2_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/eyes 2.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_face_1_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/face/face 1.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_face_2_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/face/face 2.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_hair_1_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 1.png", crop=(5, 15, 70, 70), zoom=2.0),
)

image customisation_hair_2_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 2.png", crop=(15, 10, 70, 70), zoom=2.0),
)

image customisation_hair_3_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 3.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_4_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 4.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_5_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 5.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_hair_6_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 6.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_hair_7_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 7.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_8_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.35,0.47), Text("NO HAIR", color="#000000", size=20, font="Assistant-Regular.ttf"),
)

image customisation_body_1_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/clothes/body 1.png", crop=(15, 90, 70, 70), zoom=2.0),
)

image customisation_body_2_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/clothes/body 2.png", crop=(15, 90, 70, 70), zoom=2.0),
)

image customisation_lashes_1_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.3,0.47), Text("NO LASHES", color="#000000", size=20, font="Assistant-Regular.ttf"),
)

image customisation_lashes_2_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/lashes 1.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_lashes_3_hover = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#f8f8f8")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/lashes 2.png", crop=(15, 20, 70, 70), zoom=2.0),
)

## bruh
image customisation_eyes_1_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/eyes 1.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_eyes_2_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/eyes 2.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_face_1_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/face/face 1.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_face_2_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/face/face 2.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_hair_1_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 1.png", crop=(5, 15, 70, 70), zoom=2.0),
)

image customisation_hair_2_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 2.png", crop=(15, 10, 70, 70), zoom=2.0),
)

image customisation_hair_3_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 3.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_4_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 4.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_5_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 5.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_hair_6_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 6.png", crop=(15, 20, 70, 70), zoom=2.0),
)

image customisation_hair_7_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/hair/hair 7.png", crop=(15, 35, 70, 70), zoom=2.0),
)

image customisation_hair_8_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.35,0.47), Text("NO HAIR", color="#000000", size=20, font="Assistant-Regular.ttf"),
)

image customisation_body_1_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/clothes/body 1.png", crop=(15, 90, 70, 70), zoom=2.0),
)

image customisation_body_2_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/clothes/body 2.png", crop=(15, 90, 70, 70), zoom=2.0),
)

image customisation_lashes_1_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.3,0.47), Text("NO LASHES", color="#000000", size=20, font="Assistant-Regular.ttf"),
)

image customisation_lashes_2_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/lashes 1.png", crop=(15, 25, 70, 70), zoom=2.0),
)

image customisation_lashes_3_selected_idle = Composite(
    (250,250),
    (0,0), Transform("gui/base/swatch_tint.png", matrixcolor=TintMatrix("#9d64fd")),
    (0.21,0.24), Transform("gui/socials/sprites/angel/eyes/lashes 2.png", crop=(15, 20, 70, 70), zoom=2.0),
)

################################################################################
## skintone palette
################################################################################
image skintone_1_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_1}")

image skintone_1_hover = Composite(
    (90,90),
    (0,0), "skintone_1_idle",
    (25,30), "palette_heart_hover",
)

image skintone_1_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_1_idle",
    (25,30), "palette_heart_selected",
)

image skintone_1_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_1_idle",
    (25,30), "palette_heart_hover",
)

image skintone_2_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_2}")

image skintone_2_hover = Composite(
    (90,90),
    (0,0), "skintone_2_idle",
    (25,30), "palette_heart_hover",
)

image skintone_2_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_2_idle",
    (25,30), "palette_heart_selected",
)

image skintone_2_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_2_idle",
    (25,30), "palette_heart_hover",
)

image skintone_3_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_3}")

image skintone_3_hover = Composite(
    (90,90),
    (0,0), "skintone_3_idle",
    (25,30), "palette_heart_hover",
)

image skintone_3_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_3_idle",
    (25,30), "palette_heart_selected",
)

image skintone_3_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_3_idle",
    (25,30), "palette_heart_hover",
)

image skintone_4_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_4}")

image skintone_4_hover = Composite(
    (90,90),
    (0,0), "skintone_4_idle",
    (25,30), "palette_heart_hover",
)

image skintone_4_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_4_idle",
    (25,30), "palette_heart_selected",
)

image skintone_4_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_4_idle",
    (25,30), "palette_heart_hover",
)

image skintone_5_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_5}")

image skintone_5_hover = Composite(
    (90,90),
    (0,0), "skintone_5_idle",
    (25,30), "palette_heart_hover",
)

image skintone_5_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_5_idle",
    (25,30), "palette_heart_selected",
)

image skintone_5_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_5_idle",
    (25,30), "palette_heart_hover",
)

image skintone_6_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_6}")

image skintone_6_hover = Composite(
    (90,90),
    (0,0), "skintone_6_idle",
    (25,30), "palette_heart_hover",
)

image skintone_6_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_6_idle",
    (25,30), "palette_heart_selected",
)

image skintone_6_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_6_idle",
    (25,30), "palette_heart_hover",
)

image skintone_7_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_7}")

image skintone_7_hover = Composite(
    (90,90),
    (0,0), "skintone_7_idle",
    (25,30), "palette_heart_hover",
)

image skintone_7_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_7_idle",
    (25,30), "palette_heart_selected",
)

image skintone_7_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_7_idle",
    (25,30), "palette_heart_hover",
)

image skintone_8_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_8}")

image skintone_8_hover = Composite(
    (90,90),
    (0,0), "skintone_8_idle",
    (25,30), "palette_heart_hover",
)

image skintone_8_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_8_idle",
    (25,30), "palette_heart_selected",
)

image skintone_8_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_8_idle",
    (25,30), "palette_heart_hover",
)

image skintone_9_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_9}")

image skintone_9_hover = Composite(
    (90,90),
    (0,0), "skintone_9_idle",
    (25,30), "palette_heart_hover",
)

image skintone_9_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_9_idle",
    (25,30), "palette_heart_selected",
)

image skintone_9_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_9_idle",
    (25,30), "palette_heart_hover",
)

image skintone_10_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{sc_10}")

image skintone_10_hover = Composite(
    (90,90),
    (0,0), "skintone_10_idle",
    (25,30), "palette_heart_hover",
)

image skintone_10_selected_idle = Composite(
    (90,90),
    (0,0), "skintone_10_idle",
    (25,30), "palette_heart_selected",
)

image skintone_10_selected_hover = Composite(
    (90,90),
    (0,0), "skintone_10_idle",
    (25,30), "palette_heart_hover",
)

################################################################################
## regular colour palettes
################################################################################
image palette_1_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_1}")

image palette_1_hover = Composite(
    (90,90),
    (0,0), "palette_1_idle",
    (25,30), "palette_heart_hover",
)

image palette_1_selected_idle = Composite(
    (90,90),
    (0,0), "palette_1_idle",
    (25,30), "palette_heart_selected",
)

image palette_1_selected_hover = Composite(
    (90,90),
    (0,0), "palette_1_idle",
    (25,30), "palette_heart_hover",
)

image palette_2_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_2}")

image palette_2_hover = Composite(
    (90,90),
    (0,0), "palette_2_idle",
    (25,30), "palette_heart_hover",
)

image palette_2_selected_idle = Composite(
    (90,90),
    (0,0), "palette_2_idle",
    (25,30), "palette_heart_selected",
)

image palette_2_selected_hover = Composite(
    (90,90),
    (0,0), "palette_2_idle",
    (25,30), "palette_heart_hover",
)

image palette_3_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_3}")

image palette_3_hover = Composite(
    (90,90),
    (0,0), "palette_3_idle",
    (25,30), "palette_heart_hover",
)

image palette_3_selected_idle = Composite(
    (90,90),
    (0,0), "palette_3_idle",
    (25,30), "palette_heart_selected",
)

image palette_3_selected_hover = Composite(
    (90,90),
    (0,0), "palette_3_idle",
    (25,30), "palette_heart_hover",
)

image palette_4_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_4}")

image palette_4_hover = Composite(
    (90,90),
    (0,0), "palette_4_idle",
    (25,30), "palette_heart_hover",
)

image palette_4_selected_idle = Composite(
    (90,90),
    (0,0), "palette_4_idle",
    (25,30), "palette_heart_selected",
)

image palette_4_selected_hover = Composite(
    (90,90),
    (0,0), "palette_4_idle",
    (25,30), "palette_heart_hover",
)
image palette_5_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_5}")

image palette_5_hover = Composite(
    (90,90),
    (0,0), "palette_5_idle",
    (25,30), "palette_heart_hover",
)

image palette_5_selected_idle = Composite(
    (90,90),
    (0,0), "palette_5_idle",
    (25,30), "palette_heart_selected",
)

image palette_5_selected_hover = Composite(
    (90,90),
    (0,0), "palette_5_idle",
    (25,30), "palette_heart_hover",
)
image palette_6_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_6}")

image palette_6_hover = Composite(
    (90,90),
    (0,0), "palette_6_idle",
    (25,30), "palette_heart_hover",
)

image palette_6_selected_idle = Composite(
    (90,90),
    (0,0), "palette_6_idle",
    (25,30), "palette_heart_selected",
)

image palette_6_selected_hover = Composite(
    (90,90),
    (0,0), "palette_6_idle",
    (25,30), "palette_heart_hover",
)

image palette_7_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_7}")

image palette_7_hover = Composite(
    (90,90),
    (0,0), "palette_7_idle",
    (25,30), "palette_heart_hover",
)

image palette_7_selected_idle = Composite(
    (90,90),
    (0,0), "palette_7_idle",
    (25,30), "palette_heart_selected",
)

image palette_7_selected_hover = Composite(
    (90,90),
    (0,0), "palette_7_idle",
    (25,30), "palette_heart_hover",
)

image palette_8_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_8}")

image palette_8_hover = Composite(
    (90,90),
    (0,0), "palette_8_idle",
    (25,30), "palette_heart_hover",
)

image palette_8_selected_idle = Composite(
    (90,90),
    (0,0), "palette_8_idle",
    (25,30), "palette_heart_selected",
)

image palette_8_selected_hover = Composite(
    (90,90),
    (0,0), "palette_8_idle",
    (25,30), "palette_heart_hover",
)

image palette_9_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_9}")

image palette_9_hover = Composite(
    (90,90),
    (0,0), "palette_9_idle",
    (25,30), "palette_heart_hover",
)

image palette_9_selected_idle = Composite(
    (90,90),
    (0,0), "palette_9_idle",
    (25,30), "palette_heart_selected",
)

image palette_9_selected_hover = Composite(
    (90,90),
    (0,0), "palette_9_idle",
    (25,30), "palette_heart_hover",
)

image palette_10_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_10}")

image palette_10_hover = Composite(
    (90,90),
    (0,0), "palette_10_idle",
    (25,30), "palette_heart_hover",
)

image palette_10_selected_idle = Composite(
    (90,90),
    (0,0), "palette_10_idle",
    (25,30), "palette_heart_selected",
)

image palette_10_selected_hover = Composite(
    (90,90),
    (0,0), "palette_10_idle",
    (25,30), "palette_heart_hover",
)

image palette_11_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_11}")

image palette_11_hover = Composite(
    (90,90),
    (0,0), "palette_11_idle",
    (25,30), "palette_heart_hover",
)

image palette_11_selected_idle = Composite(
    (90,90),
    (0,0), "palette_11_idle",
    (25,30), "palette_heart_selected",
)

image palette_11_selected_hover = Composite(
    (90,90),
    (0,0), "palette_11_idle",
    (25,30), "palette_heart_hover",
)

image palette_12_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_12}")

image palette_12_hover = Composite(
    (90,90),
    (0,0), "palette_12_idle",
    (25,30), "palette_heart_hover",
)

image palette_12_selected_idle = Composite(
    (90,90),
    (0,0), "palette_12_idle",
    (25,30), "palette_heart_selected",
)

image palette_12_selected_hover = Composite(
    (90,90),
    (0,0), "palette_12_idle",
    (25,30), "palette_heart_hover",
)
image palette_13_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_13}")

image palette_13_hover = Composite(
    (90,90),
    (0,0), "palette_13_idle",
    (25,30), "palette_heart_hover",
)

image palette_13_selected_idle = Composite(
    (90,90),
    (0,0), "palette_13_idle",
    (25,30), "palette_heart_selected",
)

image palette_13_selected_hover = Composite(
    (90,90),
    (0,0), "palette_13_idle",
    (25,30), "palette_heart_hover",
)
image palette_14_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_14}")

image palette_14_hover = Composite(
    (90,90),
    (0,0), "palette_14_idle",
    (25,30), "palette_heart_hover",
)

image palette_14_selected_idle = Composite(
    (90,90),
    (0,0), "palette_14_idle",
    (25,30), "palette_heart_selected",
)

image palette_14_selected_hover = Composite(
    (90,90),
    (0,0), "palette_14_idle",
    (25,30), "palette_heart_hover",
)

image palette_15_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_15}")

image palette_15_hover = Composite(
    (90,90),
    (0,0), "palette_15_idle",
    (25,30), "palette_heart_hover",
)

image palette_15_selected_idle = Composite(
    (90,90),
    (0,0), "palette_15_idle",
    (25,30), "palette_heart_selected",
)

image palette_15_selected_hover = Composite(
    (90,90),
    (0,0), "palette_15_idle",
    (25,30), "palette_heart_hover",
)

image palette_16_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix(f"{colour_16}")

image palette_16_hover = Composite(
    (90,90),
    (0,0), "palette_16_idle",
    (25,30), "palette_heart_hover",
)

image palette_16_selected_idle = Composite(
    (90,90),
    (0,0), "palette_16_idle",
    (25,30), "palette_heart_selected",
)

image palette_16_selected_hover = Composite(
    (90,90),
    (0,0), "palette_16_idle",
    (25,30), "palette_heart_hover",
)

################################################################################
## character customisation
################################################################################
image player_sprite = Composite(
    (100,160),
    (0, 0), "gui/socials/sprites/angel/clothes/[customise_body].png",
    (0, 0), "[customise_face]_[customise_skintone]",
    (0,0), ConditionSwitch("customise_hair == 'hair_8'", "images/misc/blank.png", "customise_hair != 'hair_8'", "[customise_hair]_[customise_strandcolour]"),
    (0, 0), "gui/socials/sprites/angel/eyes/[customise_eyes].png",
    (0, 0), "gui/socials/sprites/angel/eyes/[customise_lashes].png",
    (0, 0), "[customise_iris]_[customise_iriscolour]",
)

image angel_sprite_idle = Composite(
    (20,32),
    (0, 0), Transform("gui/socials/sprites/angel/clothes/[customise_body].png", zoom=0.2),
    (0, 0), Transform("[customise_face]_[customise_skintone]", zoom=0.2),
    (0,0), Transform(ConditionSwitch("customise_hair == 'hair_8'", "images/misc/blank.png", "customise_hair != 'hair_8'", "[customise_hair]_[customise_strandcolour]"), zoom=0.2),
    (0, 0), Transform("gui/socials/sprites/angel/eyes/[customise_eyes].png", zoom=0.2),
    (0, 0), Transform("gui/socials/sprites/angel/eyes/[customise_lashes].png", zoom=0.2),
    (0, 0), Transform("[customise_iris]_[customise_iriscolour]", zoom=0.2),
)

image angel_sprite_hover = Composite(
    (20,32),
    (0, 0), Transform("gui/socials/sprites/angel/clothes/[customise_body].png", zoom=0.2),
    (0, 0), Transform("[customise_face]_[customise_skintone]", zoom=0.2),
    (0,0), Transform(ConditionSwitch("customise_hair == 'hair_8'", "images/misc/blank.png", "customise_hair != 'hair_8'", "[customise_hair]_[customise_strandcolour]"), zoom=0.2),
    (0, 0), Transform("gui/socials/sprites/angel/eyes/[customise_eyes].png", zoom=0.2),
    (0, 0), Transform("gui/socials/sprites/angel/eyes/[customise_lashes].png", zoom=0.2),
    (0, 0), Transform("[customise_iris]_[customise_iriscolour]", zoom=0.2),
)

################################################################################
## Skin tones
################################################################################
image face_1_cc_17:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_1}")

image face_2_cc_17:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_1}")

image face_1_cc_18:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_2}")

image face_2_cc_18:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_2}")

image face_1_cc_19:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_3}")

image face_2_cc_19:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_3}")

image face_1_cc_20:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_4}")

image face_2_cc_20:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_4}")

image face_1_cc_21:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_5}")

image face_2_cc_21:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_5}")

image face_1_cc_22:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_6}")

image face_2_cc_22:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_6}")

image face_1_cc_23:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_7}")

image face_2_cc_23:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_7}")

image face_1_cc_24:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_8}")

image face_2_cc_24:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_8}")

image face_1_cc_25:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_9}")

image face_2_cc_25:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_9}")

image face_1_cc_26:
    "gui/socials/sprites/angel/face/face 1.png"
    matrixcolor TintMatrix(f"{sc_10}")

image face_2_cc_26:
    "gui/socials/sprites/angel/face/face 2.png"
    matrixcolor TintMatrix(f"{sc_10}")

## Iris colous
image iris_1_cc_1:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_1}")

image iris_2_cc_1:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_1}")

image iris_1_cc_2:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_2}")

image iris_2_cc_2:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_2}")

image iris_1_cc_3:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_3}")

image iris_2_cc_3:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_3}")

image iris_1_cc_4:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_4}")

image iris_2_cc_4:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_4}")

image iris_1_cc_5:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_5}")

image iris_2_cc_5:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_5}")

image iris_1_cc_6:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_6}")

image iris_2_cc_6:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_6}")

image iris_1_cc_7:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_7}")

image iris_2_cc_7:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_7}")

image iris_1_cc_8:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_8}")

image iris_2_cc_8:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_8}")

image iris_1_cc_9:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_9}")

image iris_2_cc_9:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_9}")

image iris_1_cc_10:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_10}")

image iris_2_cc_10:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_10}")

image iris_1_cc_11:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_11}")

image iris_2_cc_11:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_11}")

image iris_1_cc_12:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_12}")

image iris_2_cc_12:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_12}")

image iris_1_cc_13:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_13}")

image iris_2_cc_13:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_13}")

image iris_1_cc_14:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_14}")

image iris_2_cc_14:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_14}")

image iris_1_cc_15:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_15}")

image iris_2_cc_15:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_15}")

image iris_1_cc_16:
    "gui/socials/sprites/angel/eyes/iris 1.png"
    matrixcolor TintMatrix(f"{colour_16}")

image iris_2_cc_16:
    "gui/socials/sprites/angel/eyes/iris 2.png"
    matrixcolor TintMatrix(f"{colour_16}")

################################################################################
## Hair colours
################################################################################
## Hair 1
image hair_1_cc_1:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_1}")

image hair_1_cc_2:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_2}")

image hair_1_cc_3:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_3}")

image hair_1_cc_4:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_4}")

image hair_1_cc_5:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_5}")

image hair_1_cc_6:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_6}")

image hair_1_cc_7:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_7}")

image hair_1_cc_8:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_8}")

image hair_1_cc_9:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_9}")

image hair_1_cc_10:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_10}")

image hair_1_cc_11:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_11}")

image hair_1_cc_12:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_12}")

image hair_1_cc_13:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_13}")

image hair_1_cc_14:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_14}")

image hair_1_cc_15:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_15}")

image hair_1_cc_16:
    "gui/socials/sprites/angel/hair/hair 1.png"
    matrixcolor TintMatrix(f"{colour_16}")

## Hair 2
image hair_2_cc_1:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_1}")

image hair_2_cc_2:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_2}")

image hair_2_cc_3:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_3}")

image hair_2_cc_4:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_4}")

image hair_2_cc_5:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_5}")

image hair_2_cc_6:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_6}")

image hair_2_cc_7:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_7}")

image hair_2_cc_8:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_8}")

image hair_2_cc_9:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_9}")

image hair_2_cc_10:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_10}")

image hair_2_cc_11:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_11}")

image hair_2_cc_12:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_12}")

image hair_2_cc_13:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_13}")

image hair_2_cc_14:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_14}")

image hair_2_cc_15:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_15}")

image hair_2_cc_16:
    "gui/socials/sprites/angel/hair/hair 2.png"
    matrixcolor TintMatrix(f"{colour_16}")

## Hair 3
image hair_3_cc_1:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_1}")

image hair_3_cc_2:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_2}")

image hair_3_cc_3:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_3}")

image hair_3_cc_4:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_4}")

image hair_3_cc_5:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_5}")

image hair_3_cc_6:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_6}")

image hair_3_cc_7:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_7}")

image hair_3_cc_8:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_8}")

image hair_3_cc_9:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_9}")

image hair_3_cc_10:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_10}")

image hair_3_cc_11:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_11}")

image hair_3_cc_12:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_12}")

image hair_3_cc_13:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_13}")

image hair_3_cc_14:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_14}")

image hair_3_cc_15:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_15}")

image hair_3_cc_16:
    "gui/socials/sprites/angel/hair/hair 3.png"
    matrixcolor TintMatrix(f"{colour_16}")

## Hair 4
image hair_4_cc_1:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_1}")

image hair_4_cc_2:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_2}")

image hair_4_cc_3:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_3}")

image hair_4_cc_4:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_4}")

image hair_4_cc_5:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_5}")

image hair_4_cc_6:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_6}")

image hair_4_cc_7:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_7}")

image hair_4_cc_8:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_8}")

image hair_4_cc_9:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_9}")

image hair_4_cc_10:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_10}")

image hair_4_cc_11:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_11}")

image hair_4_cc_12:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_12}")

image hair_4_cc_13:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_13}")

image hair_4_cc_14:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_14}")

image hair_4_cc_15:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_15}")

image hair_4_cc_16:
    "gui/socials/sprites/angel/hair/hair 4.png"
    matrixcolor TintMatrix(f"{colour_16}")

## Hair 5
image hair_5_cc_1:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_1}")

image hair_5_cc_2:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_2}")

image hair_5_cc_3:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_3}")

image hair_5_cc_4:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_4}")

image hair_5_cc_5:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_5}")

image hair_5_cc_6:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_6}")

image hair_5_cc_7:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_7}")

image hair_5_cc_8:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_8}")

image hair_5_cc_9:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_9}")

image hair_5_cc_10:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_10}")

image hair_5_cc_11:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_11}")

image hair_5_cc_12:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_12}")

image hair_5_cc_13:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_13}")

image hair_5_cc_14:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_14}")

image hair_5_cc_15:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_15}")

image hair_5_cc_16:
    "gui/socials/sprites/angel/hair/hair 5.png"
    matrixcolor TintMatrix(f"{colour_16}")

## Hair 6
image hair_6_cc_1:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_1}")

image hair_6_cc_2:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_2}")

image hair_6_cc_3:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_3}")

image hair_6_cc_4:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_4}")

image hair_6_cc_5:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_5}")

image hair_6_cc_6:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_6}")

image hair_6_cc_7:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_7}")

image hair_6_cc_8:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_8}")

image hair_6_cc_9:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_9}")

image hair_6_cc_10:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_10}")

image hair_6_cc_11:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_11}")

image hair_6_cc_12:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_12}")

image hair_6_cc_13:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_13}")

image hair_6_cc_14:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_14}")

image hair_6_cc_15:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_15}")

image hair_6_cc_16:
    "gui/socials/sprites/angel/hair/hair 6.png"
    matrixcolor TintMatrix(f"{colour_16}")

## Hair 7
image hair_7_cc_1:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_1}")

image hair_7_cc_2:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_2}")

image hair_7_cc_3:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_3}")

image hair_7_cc_4:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_4}")

image hair_7_cc_5:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_5}")

image hair_7_cc_6:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_6}")

image hair_7_cc_7:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_7}")

image hair_7_cc_8:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_8}")

image hair_7_cc_9:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_9}")

image hair_7_cc_10:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_10}")

image hair_7_cc_11:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_11}")

image hair_7_cc_12:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_12}")

image hair_7_cc_13:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_13}")

image hair_7_cc_14:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_14}")

image hair_7_cc_15:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_15}")

image hair_7_cc_16:
    "gui/socials/sprites/angel/hair/hair 7.png"
    matrixcolor TintMatrix(f"{colour_16}")

################################################################################
## glitch thang
################################################################################
image gwitch:
    "misc/glitch/glitch0.png"
    choice:
        0.3
    choice:
        1.0
    choice:
        0.7
    "misc/glitch/glitch2.png"
    choice:
        0.3
    choice:
        0.2
    choice:
        0.3
    "misc/glitch/glitch3.png"
    choice:
        0.3
    choice:
        0.2
    choice:
        0.3
    "misc/glitch/glitch0.png"
    choice:
        0.5
    choice:
        1.0
    choice:
        0.8
    "misc/glitch/glitch1.png"
    choice:
        0.3
    choice:
        0.1
    choice:
        0.2
    "misc/glitch/glitch2.png"
    choice:
        0.3
    choice:
        0.2
    choice:
        0.3
    "misc/glitch/glitch0.png"
    choice:
        0.3
    choice:
        1.0
    choice:
        0.7
    "misc/glitch/glitch3.png"
    choice:
        0.3
    choice:
        0.2
    choice:
        0.3
    "misc/glitch/glitch1.png"
    choice:
        0.3
    choice:
        0.1
    choice:
        0.2
    "misc/glitch/glitch0.png"
    choice:
        0.3
    choice:
        1.0
    choice:
        0.7
    repeat

################################################################################
## customisation misc stuff
################################################################################
image palette_heart_selected:
    "gui/base/heart_tint.png"
    zoom 0.9
    matrixcolor TintMatrix("#9d64fd")

image palette_heart_hover:
    "gui/base/heart_tint.png"
    zoom 0.9
    matrixcolor TintMatrix("#f8f8f8")

image character_null_idle:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix("#414141")

image character_null_hover:
    "gui/base/status_tint.png"
    zoom 0.9
    matrixcolor TintMatrix("#414141")


## Fade stuff
image fade_folder_idle:
    "gui/ui/folder_purple_idle.png"
    matrixcolor TintMatrix("#850106")

image fade_folder_hover:
    "gui/ui/folder_pink_idle.png"
    matrixcolor TintMatrix("#850106")

image fade_folder_alt_idle:
    "gui/ui/folder_purple_hover.png"
    matrixcolor TintMatrix("#850106")

image fade_folder_alt_hover:
    "gui/ui/folder_pink_idle.png"
    matrixcolor TintMatrix("#850106")

image fade_quickbar:
    "gui/ui/textbox_b.png"
    matrixcolor TintMatrix("#850106")

image ctc_carat:
    Text("➤", color="#9d64fd", xpos=0.25, ypos=-0.25, font="DejaVuSans.ttf", size=35, outlines=[ (absolute(3), "#362A46", absolute(0), absolute(0)) ])