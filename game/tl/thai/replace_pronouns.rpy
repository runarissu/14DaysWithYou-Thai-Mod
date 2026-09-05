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
    # Save the original function defined in scripts/misc/other.rpy
    if 'refresh_pronouns' in globals():
        _original_refresh_pronouns = refresh_pronouns

        def refresh_pronouns():
            # Call the original to set base English values
            _original_refresh_pronouns()

            # Override with Thai gender-neutral values when Thai is active
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
                # Translated strings should NOT use [are]; restructure instead
                are       = ""

        # Do NOT call refresh_pronouns() here — the 'pronoun' default variable
        # is not yet initialized at init time. The wrapped function will be
        # called automatically when the game starts or when the player changes
        # their pronoun setting.
