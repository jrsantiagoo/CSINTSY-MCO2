#number of vowels and consonants
def vowelAndConsCount(w: str):
    word = str(w)
    vowels = "AEIOUaeiou"
    vowel_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1

    return vowel_count, len(word) - vowel_count

#vowel to consonant ratio, the lesser the value, the more likely it is consonant, bigger value (approaching one)
#is more likely a vowel
def vowelConsonantRatio(v, c):
    if (c == 0):
        return 1e9
        
    return v / c 

#if ends with vowel
def endsWithVowel(w: str):
    word = str(w)
    vowels = "AEIOUaeiou"

    if word[-1] in vowels:
        return 1
    return 0
'''
def vowelConsonantStructure(w: str):
    word = str(word)
    vowels = "AEIOUaeiou"
    structure = ""

    for letter in word:
        if letter in vowels:
            structure = structure + 'v'
        else:
            structure = structure + 'c'

    return structure
'''

#check if word has vowels next to each other
def has_adjacent_vowels(w: str):
    word = str(w)
    length = len(word)
    vowels = "aeiouAEIOU"
    for i in range(length - 1):
        if word[i] in vowels and word[i+1] in vowels:
            return 1
    return 0

#if word contains F, V, Z or C, it returns 1, else returns 0
def containsFVZC(w: str): 
    word = str(w)
    length = len(word)
    i = 0
    while i < length:
        if (word[i] == 'F' or word[i] == 'V' or word[i] == 'Z' or word[i] == 'C' 
            or word[i] == 'f' or word[i] == 'v' or word[i] == 'z' or word[i] == 'c'):
            return 1
        i += 1
        
    return 0

#if word contains t, n, r, s, l, v, z, x, q, it returns 1, else returns 0
def containsEnglishConsonants(w: str): 
    word = str(w).lower()
    length = len(word)
    consonants = "tnrslvzxq"
    for i in range(length - 1):
        if word[i] in consonants:
            return 1
    return 0

#if word has the usual Filipino prefixes such as na, ma, mag
def hasFilPrefix(w: str):
    word = str(w)
    word = word.lower()
    prefixes = ['na', 'ma', 'pa', 'ka',
                'nag', 'mag', 'pag', 'ika',
                'maka', 'naka', 'pang', 'mala', 'ipag', 'pina']
    
    for p in prefixes:
        if word.startswith(p):
            return len(p) / len(word)
    
    else:
        return 0
    
# word has ng
def containsNG(w: str): 
    word = str(w).lower()  
    return 1 if "ng" in word else 0
    

# words ending with vowel or consonant
def endingLetter(w: str): 
    word = str(w)
    length = len(word)
    if (word[length - 1] == 'A' or word[length - 1] == 'a' or word[length - 1] == 'E' or word[length - 1] == 'e' 
        or word[length - 1] == 'i' or word[length - 1] == 'I' or word[length - 1] == 'o' or word[length - 1] == 'O'
        or word[length - 1] == 'u' or word[length - 1] == 'U'):
        return 1
    
    return 0

# same vowels together
def has_adjacent_vowels(w: str):
    word = str(w)
    length = len(word)
    vowels = "aeiouAEIOU"
    for i in range(length - 1):
        if word[i] in vowels and word[i+1] in vowels:
            return 1
    return 0


# if letter has k, fil  
def containsK(w: str): 
    word = str(w)
    length = len(word)
    i = 0
    while i < length:
        if (word[i] == 'K' or word[i] == 'k'):
            return 1
        i += 1
        
    return 0

# repeat root word (will add maybe)

    return 0

#if word has common consonant clusters
def hasEngConsonantCluster(w: str):
    word = str(w)
    word = word.lower()
    clusters = ['bl', 'br', 'cl', 'ct', 'cr',
                'fl', 'fr', 'gl', 'gr', 'nt',
                'pl', 'pr', 'sk', 'sn', 'sp',
                'st', 'str', 'spr', 'thr', 'tr', 
                'th', 'ch']
    
    count = 0

    for c in clusters:
        if c in word:
            count += 1
    
    return count



#Creates an array of numerics, each corresponding to given feature
def create_features(word):
    word = str(word) 

    word_features = []
    vowels, consonants = vowelAndConsCount(word)
    word_features.append(vowels)
    word_features.append(consonants)
    word_features.append(vowelConsonantRatio(vowels, consonants))
    word_features.append(endsWithVowel(word))
    word_features.append(has_adjacent_vowels(word))

    word_features.append(len(word))
    word_features.append(containsFVZC(word))
    word_features.append(hasFilPrefix(word))
    word_features.append(hasEngConsonantCluster(word))

    return word_features


if __name__ == "__main__":
    while True:
        word: str = input()
        print(hasEngConsonantCluster(word))
