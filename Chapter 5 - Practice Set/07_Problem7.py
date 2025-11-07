# --------------------------------------------
# Problem 7: Same Names Issue
# --------------------------------------------

# If two friends have the same name, the later value will overwrite the earlier one.

fav_lang = {}
fav_lang['Ali'] = 'Python'
fav_lang['Ali'] = 'JavaScript'

print(fav_lang)  # Output: {'Ali': 'JavaScript'}
# Explanation: Duplicate keys are not allowed. The last value is kept.
