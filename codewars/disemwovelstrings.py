def disemvowel(string_):
    vowels = "aeiou"
    result = ""
    for char in string_:
        if char.lower() not in vowels:
            result = result + char
    return result