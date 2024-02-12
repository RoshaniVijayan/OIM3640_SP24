# how to make pig latin

text = """Darkness at the break of noon
          Shadows even the silver spoon
          The handmade blade, the child's balloon 
          Eclipses both the sun and moon"""
VOWELS = 'aeiou'

latin_translation = ''

for word in text.split():
    if word[0] not in VOWELS and word[1] in VOWELS:
        latin_translation = f"{word[1:]} {word[0]}ay"
        text = text.replace(word, latin_translation)
    elif word[0] not in VOWELS and word[1] not in VOWELS:
        latin_translation = f"{word[2:]} {word[:2]}ay"
        text = text.replace(word, latin_translation)
    elif word[0] in VOWELS:
        latin_translation = f"{word} way"
        text = text.replace(word, latin_translation)
print(text)

