# sample functions

# symbol watchlist
def get_symbols():
    watchlist = set()
    while True:
        symbol = input("Enter symbol or enter to quit: ").strip().upper()
        if not symbol:
            break
        watchlist.add(symbol)
    return list(sorted(watchlist))   

# watchlist = get_symbols()
# print(watchlist)


# clean a string
dirty_string ="""They're selling postcards of the hanging, they're painting the passports brown
The beauty parlor is filled with sailors, the circus is in town
Here comes the blind commissioner, they've got him in a trance
One hand is tied to the tight-rope walker, the other is in his pants"""

def clean_string(string):
    for letter in string:
        if letter in '.,?!;:"':
            string= string.replace(letter, '')
    return string    

# print(clean_string(dirty_string))   

# replace vowels
def replace_vowels(sentence):
    vowels = {'a': '4', 'e': '3', 'i' : '1', 'o': '0', 'u' : '8'}
    replaced =''
    for char in sentence:
        if char.lower() in vowels:
            replaced += vowels[char.lower()]
        else:
            replaced += char.lower()
    return replaced        

# print(replace_vowels(dirty_string))                

# sort of works
def is_anagram(text1, text2):
    val1 = 0
    val2 = 0
    for letter in text1.lower():
        val1 += ord(letter)
    for letter in text2.lower():
        val2 += ord(letter)    
    if val1 == val2:
        return True
    else:
        return False
    
print(is_anagram("Dormitory", "Dirty Room"))        

# anagram tester or use strings, sets, etc
def is_anagram(text1, text2):
    text1 = sorted([letter for letter in text1 if letter != " "])
    text2 = sorted([letter for letter in text2 if letter != " "])
    if text1 == text2:
        return True
    else:
        return False














