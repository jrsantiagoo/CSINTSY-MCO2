
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

#vowel to consonant ratio, the lesser the value, the more likely it is consonant, bigger value (approaching one)
#is more likely a vowel
def vowelConsonantRatio(w: str)-> float:
    word = str(w)
    length = len(word)
    vowelCount = 0
    consCount = 0
    i = 0
    while i < length:
        if (word[i] == 'A' or word[i] == 'a' or word[i] == 'E' or word[i] == 'e' 
            or word[i] == 'i' or word[i] == 'I' or word[i] == 'o' or word[i] == 'O'
            or word[i] == 'u' or word[i] == 'U'):
            vowelCount += 1
        else:
            consCount += 1

        i += 1
        
    if (consCount == 0):
        return 1e9
        
    return vowelCount / consCount

#2 letter prefix feature, if first 2 letters contain ma, pa, na, ka, if it contains, return 1, else return 0
def twoLetterPrefix(w: str):
    word = str(w)
    if (len(word) < 2):
        return 0
    stringCheck = word[0] + word[1]
    stringCheck = stringCheck.lower()
    prefixes = ['na', 'ma', 'pa', 'ka']
    if stringCheck in prefixes:
        return 1
    
    else:
        return 0



#3 letter prefix feature, if first 3 letters contain "nag", "mag", "pag", "ika", if it contains, return 1, else return 0
def threeLetterPrefix(w: str):
    word = str(w)
    if (len(word) < 3):
        return 0
    stringCheck = word[0] + word[1] + word[2]
    stringCheck = stringCheck.lower()
    prefixes = ['nag', 'mag', 'pag', 'ika']
    if stringCheck in prefixes:
        return 1
    else:
        return 0

#4 letter prefix feature, if first 4 letters contain "maka", "naka", "pang", "mala", "ipag", "pina", if it contains, return 1, else return 0
def fourLetterPrefix(w: str):
    word = str(w)
    if (len(word) < 4):
        return 0
    stringCheck = word[0] + word[1] + word[2] + word[3]
    stringCheck = stringCheck.lower()
    prefixes = ['maka', 'naka', 'pang', 'mala', 'ipag', 'pina']
    if stringCheck in prefixes:
        return 1
    
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


#Creates an array of numerics, each corresponding to given feature
def create_features(word):

    # Number of features
    num_of_features = 10

    word_features = [0] * num_of_features
    word_features[0] = containsFVZC(word)
    word_features[1] = vowelConsonantRatio(word)
    word_features[2] = twoLetterPrefix(word)
    word_features[3] = threeLetterPrefix(word)
    word_features[4] = fourLetterPrefix(word)
    word_features[5] = containsNG(word)
    word_features[6] = endingLetter(word)
    word_features[7] = has_adjacent_vowels(word)
    word_features[8] = containsK(word)
    word_features[9] = containsEnglishConsonants(word)


    return word_features


if __name__ == "__main__":
    print(containsEnglishConsonants("Ipagkalat"))
    print(containsEnglishConsonants("Hello"))
    print(containsEnglishConsonants("Training"))
    print(containsEnglishConsonants("fuck"))
    print(containsEnglishConsonants("ano bayan bro baket ganyan"))
    print(containsEnglishConsonants("OO"))
    print(containsEnglishConsonants("Naglaro"))
    print(containsEnglishConsonants("kakain"))
    print(containsEnglishConsonants("kakalaro"))
    print(containsEnglishConsonants("masaya"))
    print(containsEnglishConsonants("maglaro"))



    
