def duplicate_count(text):
    duplicates = 0
    for i in text:
         if text.count(i) > 1:
            text.replace(i," ")
            duplicates += 1
    print(text)
    return duplicates
            