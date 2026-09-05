################################################################################
## Thai Font Replacement — 14 Days With You
## Replaces all English-only fonts with Thai-capable fonts when Thai language
## is active. Uses config.font_replacement_map via language callbacks so it
## catches every font reference, including hardcoded ones in screens.rpy.
##
## Font strategy: Noto Sans Thai (https://fonts.google.com/noto/specimen/Noto+Sans+Thai)
##   Noto Sans Thai is Thai-only (no Latin glyphs), so each replacement is a
##   *composite* TTF built by merging Noto Sans Thai with the original English
##   font. Thai glyphs come from Noto Sans Thai; Latin/numbers/punctuation come
##   from the original English font. This lets Ren'Py render mixed Thai+English
##   text with a single font file (config.font_replacement_map only accepts
##   filename strings, not FontGroup objects).
##
## Composite fonts (built by _tmp_merge_fonts.py):
##   NotoSansThai-Body.ttf     = NotoSansThai-Regular  + VarelaRound-Regular
##   NotoSansThai-Names.ttf    = NotoSansThai-SemiBold + Orbitron-Black
##   NotoSansThai-UI.ttf       = NotoSansThai-Regular  + Assistant-Regular
##   NotoSansThai-UIAlt.ttf    = NotoSansThai-Regular  + Orbitron-Regular
##   NotoSansThai-Underdog.ttf = NotoSansThai-SemiBold + Underdog-Regular
##   NotoSansThai-Flow.ttf     = NotoSansThai-Regular  + FlowBlock-Regular
##   NotoSansThai-Reenie.ttf   = NotoSansThai-Regular  + ReenieBeanie-Regular
##   PlainPixel-Regular.ttf    = Plain Pixel (CC-BY 4.0, Douglas Vautour) — Thai+Latin pixel font
################################################################################

init python:
    def _thai_setup_fonts():
        # Map (original_font, bold, italic) -> Thai-capable replacement.
        # We pass through bold/italic flags so Ren'Py applies synthetic
        # bold/italic transformation on the replacement font.
        # The tuple value is (replacement_font, bold, italic) per Ren'Py API.
        _F = "tl/thai/"
        config.font_replacement_map = {
            # Body text — VarelaRound -> NotoSansThai-Body
            ("fonts/VarelaRound-Regular.ttf", False, False): (_F + "NotoSansThai-Body.ttf", False, False),
            ("fonts/VarelaRound-Regular.ttf", True,  False): (_F + "NotoSansThai-Body.ttf", True,  False),
            ("fonts/VarelaRound-Regular.ttf", False, True):  (_F + "NotoSansThai-Body.ttf", False, True),
            ("fonts/VarelaRound-Regular.ttf", True,  True):  (_F + "NotoSansThai-Body.ttf", True,  True),

            # Character names / display headers — Orbitron-Black -> NotoSansThai-Names
            ("fonts/Orbitron-Black.ttf", False, False): (_F + "NotoSansThai-Names.ttf", False, False),
            ("fonts/Orbitron-Black.ttf", True,  False): (_F + "NotoSansThai-Names.ttf", True,  False),
            ("fonts/Orbitron-Black.ttf", False, True):  (_F + "NotoSansThai-Names.ttf", False, True),
            ("fonts/Orbitron-Black.ttf", True,  True):  (_F + "NotoSansThai-Names.ttf", True,  True),

            # Interface text — Assistant -> NotoSansThai-UI
            ("fonts/Assistant-Regular.ttf", False, False): (_F + "NotoSansThai-UI.ttf", False, False),
            ("fonts/Assistant-Regular.ttf", True,  False): (_F + "NotoSansThai-UI.ttf", True,  False),
            ("fonts/Assistant-Regular.ttf", False, True):  (_F + "NotoSansThai-UI.ttf", False, True),
            ("fonts/Assistant-Regular.ttf", True,  True):  (_F + "NotoSansThai-UI.ttf", True,  True),

            # Orbitron-Regular (used in some UI labels) -> NotoSansThai-UIAlt
            ("fonts/Orbitron-Regular.ttf", False, False): (_F + "NotoSansThai-UIAlt.ttf", False, False),
            ("fonts/Orbitron-Regular.ttf", True,  False): (_F + "NotoSansThai-UIAlt.ttf", True,  False),
            ("fonts/Orbitron-Regular.ttf", False, True):  (_F + "NotoSansThai-UIAlt.ttf", False, True),
            ("fonts/Orbitron-Regular.ttf", True,  True):  (_F + "NotoSansThai-UIAlt.ttf", True,  True),

            # Underdog (used by the "it" centered entity) -> NotoSansThai-Underdog
            ("fonts/Underdog-Regular.ttf", False, False): (_F + "NotoSansThai-Underdog.ttf", False, False),
            ("fonts/Underdog-Regular.ttf", True,  False): (_F + "NotoSansThai-Underdog.ttf", True,  False),
            ("fonts/Underdog-Regular.ttf", False, True):  (_F + "NotoSansThai-Underdog.ttf", False, True),
            ("fonts/Underdog-Regular.ttf", True,  True):  (_F + "NotoSansThai-Underdog.ttf", True,  True),

            # Decorative fonts -> Noto Sans Thai composite (Thai readable, Latin keeps style)
            ("fonts/FlowBlock-Regular.ttf", False, False): (_F + "NotoSansThai-Flow.ttf", False, False),
            ("fonts/FlowBlock-Regular.ttf", True,  False): (_F + "NotoSansThai-Flow.ttf", True,  False),
            ("fonts/FlowBlock-Regular.ttf", False, True):  (_F + "NotoSansThai-Flow.ttf", False, True),
            ("fonts/FlowBlock-Regular.ttf", True,  True):  (_F + "NotoSansThai-Flow.ttf", True,  True),

            ("fonts/ReenieBeanie-Regular.ttf", False, False): (_F + "NotoSansThai-Reenie.ttf", False, False),
            ("fonts/ReenieBeanie-Regular.ttf", True,  False): (_F + "NotoSansThai-Reenie.ttf", True,  False),
            ("fonts/ReenieBeanie-Regular.ttf", False, True):  (_F + "NotoSansThai-Reenie.ttf", False, True),
            ("fonts/ReenieBeanie-Regular.ttf", True,  True):  (_F + "NotoSansThai-Reenie.ttf", True,  True),

            ("fonts/VT323-Regular.ttf", False, False): (_F + "PlainPixel-Regular.ttf", False, False),
            ("fonts/VT323-Regular.ttf", True,  False): (_F + "PlainPixel-Regular.ttf", True,  False),
            ("fonts/VT323-Regular.ttf", False, True):  (_F + "PlainPixel-Regular.ttf", False, True),
            ("fonts/VT323-Regular.ttf", True,  True):  (_F + "PlainPixel-Regular.ttf", True,  True),
        }

    def _thai_reset_fonts():
        config.font_replacement_map = { }

    # Register callbacks so fonts swap when language changes
    if not hasattr(config, 'language_callbacks'):
        config.language_callbacks = { }

    if "thai" not in config.language_callbacks:
        config.language_callbacks["thai"] = [ ]
    config.language_callbacks["thai"].append(_thai_setup_fonts)

    if None not in config.language_callbacks:
        config.language_callbacks[None] = [ ]
    config.language_callbacks[None].append(_thai_reset_fonts)

    # Always apply font replacement at init — composite fonts have both
    # Thai and Latin glyphs, so English text still renders correctly.
    # This ensures fonts are ready before any screen (including confirm)
    # is displayed, even before language callbacks fire.
    _thai_setup_fonts()
