"""
exercise_02
"""


def first_elements(my_list, n):
    new_list = my_list[:n]
    return new_list

def last_elements(my_list, n):
    new_list = my_list[-n:]
    return new_list

def n_elements(my_list, start, n):
    end = n + start
    new_list = my_list[start:end]
    return new_list

def count_letters(s):
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict

def protein_weight(protein):
    AMINO_ACID_WEIGHTS = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
                          'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
                          'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
                          'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06}
    mass = 0 
    for i in protein:
        mass =  mass + AMINO_ACID_WEIGHTS[i]
    return mass

