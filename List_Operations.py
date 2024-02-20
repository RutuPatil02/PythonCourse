def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        print(i)
        if s[i] == s[len(s) - 1 - i]: 
            matches = matches + 1

    return matches == (len(s) // 2)

print(mystery('civil'))