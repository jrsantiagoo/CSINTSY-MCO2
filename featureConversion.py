
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

#Creates an array of numerics, each corresponding to given feature
def create_features(word):

    # Number of features
    num_of_features = 5

    word_features = [0] * num_of_features
    word_features[0] = containsFVZC(word)
    word_features[1] = vowelConsonantRatio(word)
    word_features[2] = twoLetterPrefix(word)
    word_features[3] = threeLetterPrefix(word)
    word_features[4] = fourLetterPrefix(word)

    return word_features


if __name__ == "__main__":
    print(fourLetterPrefix("Ipagkalat"))
    print(fourLetterPrefix("Hello"))
    print(fourLetterPrefix("Training"))
    print(containsFVZC("fuck"))
    print(fourLetterPrefix("ano bayan bro baket ganyan"))
    print(fourLetterPrefix("OO"))
    print(fourLetterPrefix("Naglaro"))
    print(fourLetterPrefix("kakain"))
    print(fourLetterPrefix("kakalaro"))
    print(fourLetterPrefix("masaya"))
    print(fourLetterPrefix("maglaro"))



    
