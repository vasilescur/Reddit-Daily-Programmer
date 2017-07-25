for c in input():
    if c.lower() in "aeiouåäö" or not c.isalpha():
        print(c, end = "")
    else:
        print(c+"o"+c.lower(), end = "")
