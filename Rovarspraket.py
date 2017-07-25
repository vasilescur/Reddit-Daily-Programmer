# Obfuscates text by replacing consonants with consonant + 'o' + consonant groups (Ex. "Hello" --> "Hohelollolo")
# Source: https://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_rövarspråket/

for c in input():
    if c.lower() in "aeiouåäö" or not c.isalpha():
        print(c, end = "")
    else:
        print(c + "o" + c.lower(), end = "")
