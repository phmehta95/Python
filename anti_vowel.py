def anti_vowel(t):
    new_t = ""
    for i in t:
        if i not in "aeiouAEIOU":
            new_t += i
    return new_t

print (anti_vowel("Hello"))
