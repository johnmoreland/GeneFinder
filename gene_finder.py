# -*- coding: utf-8 -*-
"""
YOUR HEADER COMMENT HERE

@author: john moreland

"""

import random
from amino_acids import aa, codons, aa_table   # you may find these useful
from load import load_seq


def shuffle_string(s):
    """Shuffles the characters in the input string
        NOTE: this is a helper function, you do not
        have to modify this in any way """
    return ''.join(random.sample(s, len(s)))

# YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """
    if nucleotide == "A" or nucleotide == "C" or nucleotide == "T" or nucleotide == "G":
    	if nucleotide == "A":
    		return "T" 
    	elif nucleotide == "C": 
    		return "G"
    	elif nucleotide == "T":
    		return "A"
    	elif nucleotide == "G":
    		return "C"
        else:
            return ""

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence

        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """

    reversed_string = dna[::-1] #reverses input DNA string because of backwards step
    complementedstring = ""
    for c in reversed_string:
        complementedstring = complementedstring + get_complement(c)
    return complementedstring


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start
        codon and returns the sequence up to but not including the
        first in frame stop codon.  If there is no in frame stop codon,
        returns the whole string.

        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATGAAGATAGG") #stop codon present, but not in this frame
    'ATGAAGATAGG'
    """
    
    stop_codons = ['TAA', 'TAG', 'TGA']
    stop_codon_indices = []
    #search for stop codon indices
    i = 0
    while i < len(dna):
        if (dna[i:i+3] in stop_codons) and (i % 3 == 0): #store index if dna matches stop codon and is in frame
            stop_codon_indices.append(i)
        else:
            stop_codon_indices.append(len(dna)) #if no stop codons found, set end index to be full length of DNA
        i += 3
    end = min(stop_codon_indices)
    # print (dna[:end])
    return dna[:end]


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA
        sequence and returns them as a list.  This function should
        only find ORFs that are in the default frame of the sequence
        (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """

    start_codon = 'ATG'
    i = 0
    orf_list = []
    while i < len(dna):
        if (dna[i:i+3]) == start_codon and (i % 3 == 0):
            print i
            store = rest_of_ORF(dna[i:])
            print store
            orf_list = orf_list + [store] #find rest of ORF
            i = i + len(store)     #change start index to end of current ORF
        else:
            i = i + 3
    print orf_list
    return orf_list


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in
        all 3 possible frames and returns them as a list.  By non-nested we
        mean that if an ORF occurs entirely within another ORF and they are
        both in the same frame, it should not be included in the returned list
        of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    return find_all_ORFs_oneframe(dna) + find_all_ORFs_oneframe(dna[1:]) +find_all_ORFs_oneframe(dna[2:])



def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    return find_all_ORFs(get_reverse_complement(dna)) + find_all_ORFs(dna)


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).

        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass


def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna

        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    # TODO: implement this
    pass





# get_reverse_complement("ATGCGAATGTAGCATCAAA")
# find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
# get_reverse_complement("CCGCGTTCA")
find_all_ORFs_oneframe("ATGCATGAATGTTAGATGTGCCC")
    # 'ATGAGA'
if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    # doctest.run_docstring_examples(rest_of_ORF, globals())


