
#if word contains F, V, Z or C, it returns 1, else returns 0
def containsFVZC(word: str): 
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
def vowelConsonantRatio(word: str)-> float:
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
        return 9999999
        
    return vowelCount / consCount

#2 letter prefix feature, if first 2 letters contain ma, pa, na, ka, if it contains, return 1, else return 0
def twoLetterPrefix(word: str):
    if (len(word) < 2):
        return 0
    stringCheck = word[0] + word[1]
    stringCheck = stringCheck.lower()
    if (stringCheck == 'ma' or stringCheck == 'pa' or stringCheck == 'na' or stringCheck == 'ka'):
        return 1
    
    else:
        return 0



#3 letter prefix feature, if first 3 letters contain "nag", "mag", "pag", "ika", if it contains, return 1, else return 0
def threeLetterPrefix(word: str):
    if (len(word) < 3):
        return 0
    stringCheck = word[0] + word[1] + word[2]
    stringCheck = stringCheck.lower()
    if (stringCheck == 'nag' or stringCheck == 'mag' or stringCheck == 'pag' or stringCheck == 'ika'):
        return 1
    
    else:
        return 0

#4 letter prefix feature, if first 4 letters contain "maka", "naka", "pang", "mala", "ipag", "pina", if it contains, return 1, else return 0
def fourLetterPrefix(word: str):
    if (len(word) < 4):
        return 0
    stringCheck = word[0] + word[1] + word[2] + word[3]
    stringCheck = stringCheck.lower()
    if (stringCheck == 'maka' or stringCheck == 'naka' or stringCheck == 'pang' or stringCheck == 'mala' 
        or stringCheck == 'ipag' or stringCheck == 'pina'):
        return 1
    
    else:
        return 0

if __name__ == "__main__":
    print(fourLetterPrefix("Ipagkalat"))
    print(fourLetterPrefix("Hello"))
    print(fourLetterPrefix("Training"))
    print(fourLetterPrefix("fuck"))
    print(fourLetterPrefix("ano bayan bro baket ganyan"))
    print(fourLetterPrefix("OO"))
    print(fourLetterPrefix("Naglaro"))
    print(fourLetterPrefix("kakain"))
    print(fourLetterPrefix("kakalaro"))
    print(fourLetterPrefix("masaya"))
    print(fourLetterPrefix("maglaro"))



    
