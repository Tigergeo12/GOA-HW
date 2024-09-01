def is_anagram(test, original):
    test1 = sorted(list(test.lower()))
    original1 = sorted(list(original.lower()))
    if test1 == original1:
        return True
    else:
        return False
    