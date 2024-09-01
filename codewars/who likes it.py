def likes(names):
    if not names:
        return "no one likes this"
    if len(names) == 1:
        return "".join(names) + " likes this"
    elif len(names) == 2:
        return "".join(names[0]) + " and " + "".join(names[1]) + " like this"
    elif len(names) == 3:
        return "".join(names[0]) + ", " + "".join(names[1]) + " and " + "".join(names[2]) + " like this"
    elif len(names) == 4:
        return "".join(names[0]) + ", " + "".join(names[1]) + " and 2 others like this"
    elif len(names) > 4:
         return "".join(names[0]) + ", " + "".join(names[1]) + " and " + str(len(names)-2) + " others like this"
