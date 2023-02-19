n = "mageshABC1234"
# def key_func(char: str) -> int:
#     if not char.isdigit():
#         return char
#     if char.islower():
#         return ord(char)-ord('a')
#     if char.isupper():
#         return ord(char)-ord('A') + 26
#     if int(char) % 2 != 0:
#         return int(char)//2 + 52
#     return int(char)//2 + 57

# print(''.join(sorted(n, key=key_func)))

# def missingCharacters(s):
#     # Write your code here
#     MAX_CHAR =26
#     present = [False for i in range(MAX_CHAR)]
#     digits_missing = [i for i in range(0,10)]
#     print("digits missing - ", digits_missing)
#     # Traverse string and mark characters
#     # present in string.
#     for i in range(len(s)):
#         # print(s[i])
#         if (s[i] >= 'a' and s[i] <= 'z'):
#             present[ord(s[i]) - ord('a')] = True
#         if ((s[i]).isdigit()):
#             if int(s[i]) in digits_missing:
#               digits_missing.remove(int(s[i]))
 
#     # Store missing characters in alphabetic
#     # order.
#     res = ""
#     digits_m = "".join(map(str, digits_missing))
#     for i in range(MAX_CHAR):
#         if (present[i] == False):
#             res += chr(i + ord('a'))
             
#     return str(digits_m)+res
    
# print(missingCharacters("167"))

def transformSentence(sentence):
    # Write your code here
    new_sentence = []
    first = 0
    # j=0
    for i in range(0, len(sentence)):
        if first == 0 or sentence[i] == " ":
            new_sentence.append(sentence[i])
            if first != 0:
              first = 0
            else:
              first = 1
        elif ord(sentence[i].lower()) > ord(sentence[i-1].lower()):
            new_sentence.append(sentence[i].upper())
            j=0
        elif ord(sentence[i].lower()) < ord(sentence[i-1].lower()):
            new_sentence.append(sentence[i].lower())
            j=0
        elif ord(sentence[i].lower()) == ord(sentence[i-1].lower()):
            new_sentence.append(sentence[i])
            j=0
    return "".join(new_sentence)

print(transformSentence("ab cB GG"))
#aB cb GG
# lower - 97
# Upp - 65
# odd - 48 - 57
# Eve