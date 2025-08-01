def find_anagrams(word, candidates):
    acceptable_candidates = []

    for candidate in candidates:
        if word.lower() == candidate.lower():
            continue
        if sorted(candidate.lower()) == sorted(word.lower()):
            acceptable_candidates.append(candidate)

    return acceptable_candidates
