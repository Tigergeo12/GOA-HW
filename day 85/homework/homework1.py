ch = input("Please enter a letter : ")
if ch.islower() == "a" or "i" or "e" or "u" or "o":
    print("The letter is a vowel")
else:
    print("The letter is a consonant")

ch1 = ch.lower()
if ch1 in "aeiou":
    print("The letter is a vowel")
else:
    print("the letter is a consonant")