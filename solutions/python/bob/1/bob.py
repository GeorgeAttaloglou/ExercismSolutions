def response(hey_bob):
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    elif hey_bob.strip()[-1] == "?" and hey_bob.isupper() == False:
        return "Sure."
    elif hey_bob.strip()[-1] == "?" and hey_bob.isupper() == True:
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."

    
