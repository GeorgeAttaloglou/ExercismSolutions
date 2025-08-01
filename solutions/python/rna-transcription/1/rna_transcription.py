def to_rna(dna_strand):

    return dna_strand.translate(str.maketrans("ACGT","UGCA"))

"""
    translations = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
        rna = ''
        for letter in sequence:
            rna += translations[letter]
        return rna
"""
