################################################################################
## Thai Pronoun Override — 14 Days With You
##
## Thai has no gendered pronouns. This file wraps the game's refresh_pronouns()
## function so that when Thai language is active, all pronoun variables are
## replaced with gender-neutral Thai equivalents.
##
## This handles the 48 dynamic pronoun insertion points in the game scripts
## without needing to manually edit each one.
################################################################################

init 1 python:
    # Helper: apply Thai pronoun overrides (called after any English refresh)
    def _apply_thai_pronouns():
        if _preferences.language == "thai":
            global they, them, their, theirs, themself
            global person, baby, partner, spouse, are, gorgeous

            # Thai has no gendered pronouns — "เขา" covers all cases
            they      = "เขา"
            them      = "เขา"
            their     = "ของเขา"
            theirs    = "ของเขา"
            themself  = "ตัวเอง"

            # Gender-neutral nouns
            person    = "คน"
            baby      = "ตัวเล็ก"
            partner   = "คู่รัก"
            spouse    = "คู่สมรส"
            gorgeous  = "ดีตา"

            # Thai has no subject-verb agreement — empty string
            are       = ""

    # Wrap refresh_pronouns() — called when player changes pronoun setting
    if 'refresh_pronouns' in globals():
        _original_refresh_pronouns = refresh_pronouns

        def refresh_pronouns():
            _original_refresh_pronouns()
            _apply_thai_pronouns()

    # Wrap refresh_custom_angel() — called when player toggles default/custom angel
    # This function ALSO resets pronouns to English, so we must override after it
    if 'refresh_custom_angel' in globals():
        _original_refresh_custom_angel = refresh_custom_angel

        def refresh_custom_angel():
            _original_refresh_custom_angel()
            _apply_thai_pronouns()

## --- Force refresh_pronouns() on game start so Thai overrides apply ---
## Without this, the default pronoun values (English) stay until the player
## manually clicks a pronoun button, causing mixed Thai/English text.
init 2 python:
    def _thai_refresh_pronouns_on_start():
        try:
            _apply_thai_pronouns()
        except Exception:
            pass

    if _thai_refresh_pronouns_on_start not in config.start_callbacks:
        config.start_callbacks.append(_thai_refresh_pronouns_on_start)
