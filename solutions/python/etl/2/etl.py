def transform(legacy_data: dict) -> dict:
    """
    for each key in legacy data, take the values and put them into another dict
    as keys, assigning the values of said keys with the keys from the original dict
    """
    data = {}

    for key in legacy_data.keys():
        for value in legacy_data[key]:
            data.update({value.lower() : key})
            
    return data

"""
    	for score, letters in old_data.items():
		    for letter in letters:
			    data[letter.lower()] = score
	return data
"""