def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1)>len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if nucleotide == char :
            count += 1

    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 
    'A', 'T', 'C'and 'G'). A string is not a valid DNA sequence if it contains lowercase letters.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGCB')
    False
    >>> is_valid_sequence('atcgg')
    False

    """
    isValid = True

    for char in dna:
        if char not in ('ATCG'):
            isValid = False
            break

    return isValid

def insert_sequence(dna1, dna2, num):
    """  (str, str, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG', 'AT',2)
    'CCATGG'
    >>> insert_sequence('TCCAGG', 'GT',4)
    'TCCAGTGG'

    """
    new_dna = dna1[:num] + dna2 + dna1[int(num):]
    
    return  new_dna


def get_complement(nucleotide):
    """(str) -> str
​
    Return the nucleotide's complement

    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('A')
    'T'

    """
    
    if nucleotide =='A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    else:
        return 'C'
    

def get_complementary_sequence(dna):
    """ (str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence. 
    
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('GC')
    'CG'
    >>> get_complementary_sequence('GT')
    'CA'

    """
    comp_dna = ''

    for char in dna:
        if char =='A':
            comp_dna = comp_dna + 'T'
        elif char == 'T':
            comp_dna = comp_dna + 'A'
        elif char == 'C':
            comp_dna = comp_dna + 'G'
        else:
            comp_dna = comp_dna + 'C'

    return comp_dna

