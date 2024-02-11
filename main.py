def pigLatin():
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                 'z']
    while True:
        imongWords = input("Enter a word here (between 3 to 10 characters): ").lower()

        if imongWords.isalpha() == False:

            print("Enter a valid word.")
        elif 3 <= len(imongWords) <= 10:
            break
        else:
            print("Enter between 3 to 10 characters.")

    imongWords = imongWords.split()
    for k in range(len(imongWords)):
        i = imongWords[k]
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            imongWords[k] = i + "ay"
        elif i[0] in consonant:
            imongWords[k] = i[1:]+i[:1]+"ay"
        else:
            break
    return " ".join(imongWords)
if __name__ == "__main__":
    x = pigLatin()
    print(x)







