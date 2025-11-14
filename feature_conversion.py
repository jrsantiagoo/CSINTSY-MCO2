import re

#number of vowels and consonants
def vowel_consonant_count(w: str):
    word = str(w)
    vowels = "AEIOUaeiou"
    vowel_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1

    return vowel_count, len(word) - vowel_count

#vowel to consonant ratio
def vowel_consonant_ratio(v, c):
    if c == 0:
        return 1e9

    return v / c

#if ends with vowel
def ends_with_vowel(w: str):
    word = str(w)
    vowels = "AEIOUaeiou"

    if word[-1] in vowels:
        return 1
    return 0

#check if word has vowels next to each other
def has_adjacent_vowels(w: str):
    word = str(w)
    length = len(word)
    vowels = "aeiouAEIOU"
    for i in range(length - 1):
        if word[i] in vowels and word[i+1] in vowels:
            return 1
    return 0

#check if word has same vowels next to each other
def has_same_adjacent_vowels(w: str):
    word = str(w)
    length = len(word)
    vowels = "aaeeiioouuAAEEIIOOUU"
    for i in range(length - 1):
        if word[i] in vowels and word[i+1] in vowels:
            return 1
    return 0

#if word contains F, V, Z, C, X, or Q it returns 1, else returns 0
def containsFVZCXQ(w: str): 
    word = str(w)
    letters = 'FVZCXQfvzcxq'
    for letter in letters:
        if letter in word.upper():
            return 1
        
    return 0

#if word has the usual Filipino prefixes such as na, ma, mag
def has_fil_prefix(w: str):
    word = str(w)
    word = word.lower()
    prefixes = ['na', 'ma', 'pa', 'ka',
                'nag', 'mag', 'pag', 'ika',
                'maka', 'naka', 'pang', 'mala', 
                'ipag', 'pina', 'napag', 'kapag',
                'mapag']
    found = ""
    
    for p in prefixes:
        if word.startswith(p):
            found = p
    
    if len(found) > 1:
        return len(found)
    else:
        return 0

#if word has common consonant clusters
def has_eng_consonant_cluster(w: str):
    word = str(w)
    word = word.lower()
    clusters = ['bl', 'br', 'cl', 'ct', 'cr',
                'fl', 'fr', 'gl', 'gr', 'nt',
                'pl', 'pr', 'sk', 'sn', 'sp',
                'st', 'str', 'spr', 'thr', 'tr', 
                'th', 'ch', 'sh', 'ph', 'wh']
    
    count = 0

    for c in clusters:
        if c in word:
            count += 1
    
    return count

#percentage of capital letters
def caps_percentage(w: str):
    word = str(w)
    capital_count = 0

    for letter in word:
        if letter.isupper():
            capital_count += 1
    
    return capital_count / len(word)

#reduplication (repeat of words/syllables)
def is_reduplicated(w: str):
    word = str(w)
    return int(bool(re.search(r"(\b\w+\b)-\1", word)) or
               bool(re.search(r"(.{2,})\1", word)))

#count of each word's syllables
def syllable_count(w: str):
    word = str(w)
    pattern = r"[bcdfghjklmnpqrstvwxyz]*[aeiou]+"
    return len(re.findall(pattern, word))

#consonant repeats
def repeat_consonants(w: str):

    word = str(w).lower()

    vowels = "aeiou"

    for i in range(1, len(word)):
        if(word[i] == word[i - 1] and word[i] not in vowels):
            return 1
    return 0

#count of each word's syllables
def is_alpha(w: str):
    word = str(w)
    return word.isalpha()

#english prefixes
def prefixENG(w: str):
    pre = ['ante', 'anti', 'auto', 'circu', 'co', 'com', 'con', 'contra', 
           'contro', 'de', 'dis', 'extra', 'pre', 'pro', 're', 'sub', 'sym', 
           'syn', 'tele', 'trans', 'tri', 'un', 'uni', 'up']
    for p in pre:
        if w.lower().startswith(p):
            return 1
    return 0

#english suffixes
def suffixENG(w: str):
    suf = ['acy', 'al', 'ance', 'ence', 'dom', 'er', 'or', 
           'ism', 'ist', 'ity', 'ty', 'ment', 'ness', 'ship', 
           'sion', 'tion', 'ate', 'en', 'ify', 'fy', 'ize', 'ise', 
           'able', 'ible', 'al', 'ful', 'ic', 'ical', 'ious', 'ous', 
           'ish', 'ive', 'less', 'y', '\'s', 'ck']

    for s in suf:
        if w.lower().endswith(s):
            return 1
    return 0

# common filipino words
def dic_FIL(w: str):
    fil = {"ang","ng","mga","sa","ay","siya","ito","kami"}

    for wo in fil:
        if wo == w:
            return 1
    
    return 0

# common eng words
def dic_ENG(w: str):
    eng = {"the","of","to","and","is","are","it", "how"}

    for wo in eng:
        if wo == w:
            return 1
    
    return 0

# ASCII value of last letter 
def ascii_final_letter(w: str):
    return ord(w[-1].lower())

# ASCII value of first letter
def ascii_first_letter(w: str):
    return ord(w[0].lower())

#Creates an array of numerics, each corresponding to given feature
def create_features(word):
    word = str(word) 

    word_features = []
    vowels, consonants = vowel_consonant_count(word)
    word_features.append(len(word))
    word_features.append(vowel_consonant_ratio(vowels, consonants))
    word_features.append(ends_with_vowel(word))
    word_features.append(has_same_adjacent_vowels(word))
    word_features.append(has_adjacent_vowels(word))

    word_features.append(containsFVZCXQ(word))
    word_features.append(has_fil_prefix(word))
    word_features.append(has_eng_consonant_cluster(word))
    word_features.append(caps_percentage(word))
    word_features.append(is_reduplicated(word))

    word_features.append(syllable_count(word))
    word_features.append(repeat_consonants(word))
    word_features.append(is_alpha(word))
    word_features.append(prefixENG(word))
    word_features.append(suffixENG(word))

    word_features.append(dic_ENG(word))
    word_features.append(dic_FIL(word))
    word_features.append(ascii_final_letter(word))
    word_features.append(ascii_first_letter(word))

    return word_features