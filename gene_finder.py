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
    # TODO: implement this
    pass

    if nucleotide == "A" or nucleotide == "C" or nucleotide == "T" or nucleotide == "G":
    	if nucleotide == "A":
    		return "T" 
    	elif nucleotide == "C": 
    		return "G"
    	elif nucleotide == "T":
    		return "A"
    	elif nucleotide == "G":
    		return "C"

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
    # TODO: implement this
    pass

    stringlength = len(dna)
    # print stringlength
    t = 0
    u = 1
    complementedstring = ''
    finalstring = ''
    #get complements of each nucleotide in the string
    while t < stringlength:
    	complementedstring = complementedstring + get_complement(dna[t])
    	t = t+1
    #reverse the string
    while u < stringlength+1:
    	finalstring = finalstring + (complementedstring[stringlength-u])
    	u = u+1
    # print finalstring
    return finalstring



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
    # TODO: implement this
    pass

    i=0
    
    # print dna

    TAA = 1							#initialize variables
    storeTAA = 0
    while 1 == 1:					#start a loop
    	TAA = dna.find('TAA', TAA+1)	#search for "TAA" in dna string, starting at TAA value
    	if TAA == storeTAA:			#if loop gets the same value after two run throughs, it is an invalid value, so -1
    		TAA = -1
    	storeTAA = TAA 				#store the TAA value so it can be referenced again
        if TAA < 0: 				#if value is invalid (-1), just break
            break
        elif (TAA % 3) == 0: 		#if the value is valid (divisible by 3) keep it and break
            break
    # print('TAA', TAA)

    TAG = 1
    storeTAG = 0
    while 1 == 1:
    	TAG = dna.find('TAG', TAG+1)
    	# print(TAG)
    	if TAG == storeTAG:
    		TAG = -1
    	storeTAG = TAG
        if TAG < 0:
            break
        elif (TAG % 3) == 0:
            break
    # print('TAG', TAG)

    TGA = 0
    storeTGA = 0
    while 1 == 1:
    	TGA = dna.find('TGA', TGA+1)
    	# print(TGA)
    	if TGA == storeTGA:
    		TGA = -1
    	storeTGA = TGA
        if TGA < 0:
            break
        elif (TGA % 3) == 0:
            break
    # print('TGA', TGA)

    readingframe = ""
    if TAA > 0 or TAG > 0 or TGA > 0: #if a stop codon is present
    	#return values up to stop codon
    	while i < len(dna):
    		readingframe = readingframe + dna[i]
    		if i>0 and (i == TAA-1 or i == TAG-1 or i == TGA-1):
    			# print readingframe
    			return readingframe
    		else:
    			i = i + 1
     #else return whole string
    else:
    	return dna


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
    # TODO: implement this
    pass
    i = 0
    output=[]
    start_index = 0

    #search for an ATG  
    while 1==1:
	    start_index = dna.find('ATG', start_index)
	    # print start_index

	    if start_index % 3 == 0: #if start index starts on an actual codon
	    	#run rest_of_ORF to get the whole frame
	    	store = rest_of_ORF(dna[start_index:])
	    	#save that ORF
	    	output.append(store)
	    	#new start index = index of current ORF + lenth of ORF + 3 (stop codon)
	    	start_index = start_index + len(store) + 3
	    	i=i+1
	    elif start_index == -1:
	    	# print output
	    	return output
	    else:
	    	start_index = start_index+1


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
    # TODO: implement this
    pass

    return find_all_ORFs_oneframe(dna) + find_all_ORFs_oneframe(dna[1:]) +find_all_ORFs_oneframe(dna[2:])



def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    pass

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
get_reverse_complement("CCGCGTTCA")
if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    # doctest.run_docstring_examples(rest_of_ORF, globals())


