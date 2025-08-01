VOWELS = list("aeiou")
VOWELS_Y = list("aeiouy")
SPECIALS = ["xr", "yt"]

def translate(text: str) -> str:
    piggyfied = []

    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            piggyfied.append(word + "ay")
            continue

        for position in range(1,len(word)):
            if word[position] in VOWELS_Y:
                position += 1 if word[position] == "u" and word[position-1] == "q" else 0
                piggyfied.append(word[position:] + word[:position] + "ay")
                break
    
    return " ".join(piggyfied)