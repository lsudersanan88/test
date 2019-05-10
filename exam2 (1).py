"""
Exam 2

Please put your name and RED ID in the definition below
"""

def name_id():
    """
    Please return your REDID followed by your first and last name as separate elements in a list.
    :return: a list of [redID, first_name, last_name]
    """
    return ['820992504', 'Mohan', 'Thazhathethil']

"""
Section 1: list, dictionary, and set comprehensions

Complete each definition below, using one line of code.
Your solution should be on the same line as the return statement.
Solving the problem on multiple lines will result in a 70% penalty for the problem.


"""

def ceiling(my_list, max_value):
    """
    Return a list, where every element in my_list that is greater than the max_value, is reduced to max_value.
    EX: ceiling([1, 10, 100, 200, 300], 150) -> [1, 10, 100, 150, 150]
    """
    return [max_value if number > max_value else number for number in my_list]


def squish(my_list, min_value, max_value):
    """
    Return a list, where every element in my_list that is less than min_value is raised to min_value, AND
     every element that is greater than max_value is reduced to max_value.
    EX: squish([1, 10, 100, 200, 300], 15, 150) -> [15, 15, 100, 150, 150]
    """
    return [ (min_value if number < min_value else (max_value if number > max_value else number) )for number in my_list]

def n_by_m_zeros(m, n):
    """
    Return a list of length m, where each element in m, is a list of 0's length n.
    EX: n_by_m_zeros(4, 2) -> [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    return [[0 for _ in range(0,n)]for _ in range (0,m)]

def dict_low_pass(my_dict):
    """
    Return a dictionary of only the key/value pairs from my_dict whose value is GREATER THAN 10.
    EX: dict_low_pass({'a': 1, 'b': 10, 'c': 11}) -> {'c': 11}
    """
    return {key: my_dict[key] for key in my_dict if my_dict[key] > 10}

def shared_element_count(list_a, list_b):
    """
    Return an int representing the number of elements that are in both list_a and list_b
    EX: shared_element_count([1, 3, 5], [1, 2, 3]) -> 2
    """
    return len(list(set(list_a).intersection(set(list_b))))

def len_2_number_strings():
    """
    Return a list of strings (all length 2) representing all numbers '00' to '99'
    EX: len_2_number_strings() -> ['00', '01', '02', ... '98', '99']
    """
    return [ '0' + str(number) if number <10 else str(number) for number in range(0, 100)]

def index_dict(my_list):
    """
    Return a dictionary where each key is an element in my_list and each value is the index of that element. There
     are no repeated elements in my_list.
    EX: index_dict(['name', 'id', 'age']) -> {'name': 0, 'id': 1, 'age': 2}
    """
    return {val: my_list.index(val) for val in my_list}


def absolute_average(my_list):
    """
    Return the average of the absolute values of all integers in my_list.
    EX: absolute_average([10, -10, 12, 12]) -> 11
    """
    return int(sum(abs(num) for num in my_list) / len(my_list))


def specific_rows(filename, my_string):
    """
    Return a list of lines from filename that start with my_string
    EX: specific_rows('example.fastQ', '@') -> ['@srr_3403639', '@srr3403565', ...]
    """
    return [line.replace('\n', '') for line in open(filename) if line.startswith(my_string)]


from math import log10

def log10_row(my_list):
    """
    Return a list of the log10 of every value in my_list or '-' if the log cannot be taken.
    EX: log10([0, 1, 10 100]) -> ['-', 0.0, 1.0, 2.0]
    """
    return ['-' if number <= 0 else log10(number) for number in my_list]

def log10_csv(list_of_lists):
    """
    Given a list containing lists, convert every value contained within to its log10 transformation or '-' if
     it is not possible. DO THIS WITHOUT CALLING THE log10_row() DEFINITION.
    EX: log10_csv([[0, 1, 10 100], [0, 1, 10 100]]) -> [['-', 0.0, 1.0, 2.0], ['-', 0.0, 1.0, 2.0]]
    """
    return [[('-' if number <= 0 else log10(number) ) for number in lists] for lists in list_of_lists ]

"""
Section 2: classes and style

In part 1, complete the functionality requirements for the VcfReader class - how you choose to do so is up to you.
You can find more about VCF files here: http://vcftools.sourceforge.net/VCF-poster.pdf
    1. Initialize the class with only a path to the VCF file
        EX: vr = VcfReader('example.vcf')
        
    2. The document header (lines starting with '##') should be a list of lines(strings) accessible with .file_header 
        EX: vr.file_header -> ['##fileformat=VCFv4.0', '##fileDate=20090805, ... ##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality]
        
    3. The column header (lines starting with '#') should be a list of column headers (strings), accessible with .column_header
        EX: vr.column_header -> ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'NA00001', 'NA00002', 'NA00003']
    
    4. The body of the file (lines not starting with any '#') should be accessible as a list of lists with .lines;
        each line should be split by columns into strings.
        EX: vr.lines -> [['20', '14370', 'rs6054257', 'G', 'A', '29', 'PASS', 'NS=3;DP=14;AF=0.5;DB;H2', 'GT:GQ:DP:HQ', '0|0:48:1:51,51', '1|0:48:8:51,51', '1/1:43:5:.,.'], ['21', '17330', 'rs6054258', 'T', 'A', '3', 'q10', 'NS=3;DP=11;AF=0.017', 'GT:GQ:DP:HQ', '0|0:49:3:58,50', '0|1:3:5:65,3', '0/0:41:3']]

    5. The definition .get_chrom(my_int) should accept a single int and return a list of lines whose #Chrom column 
        matches the input my_int. (keep in mind, vr.lines should be a list of strings, and this def accepts an int)
        EX: vr.get_chrom(20) -> [['20', '14370', 'rs6054257', 'G', 'A', '29', 'PASS', 'NS=3;DP=14;AF=0.5;DB;H2', 'GT:GQ:DP:HQ', '0|0:48:1:51,51', '1|0:48:8:51,51', '1/1:43:5:.,.']]

    6. The __str__ method should return the string with which the VcfReader class was initialized with
        EX: print(vr) -> 'example.vcf'
        
    7. The __len__ method should return an int representing the number of TOTAL lines in the file
        EX: len(vr) -> 20      
"""


# Uncomment the following line to generate an example VCF file named "example.vcf"
# with open('example.vcf', 'w') as outfile: outfile.write('\n'.join(['##fileformat=VCFv4.0', '##fileDate=20090805', '##source=myImputationProgramV3.1', '##reference=1000GenomesPilot-NCBI36', '##phasing=partial', '##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">', '##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">', '##INFO=<ID=AF,Number=.,Type=Float,Description="Allele Frequency">', '##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">', '##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">', '##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">', '##FILTER=<ID=q10,Description="Quality below 10">', '##FILTER=<ID=s50,Description="Less than 50% of samples have data">', '##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">', '##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">', '##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">', '##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">', '#CHROM POS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tNA00001\tNA00002\tNA00003', '20\t14370\trs6054257\tG\tA\t29\tPASS\tNS=3;DP=14;AF=0.5;DB;H2\tGT:GQ:DP:HQ\t0|0:48:1:51,51\t1|0:48:8:51,51\t1/1:43:5:.,.', '21\t17330\trs6054258\tT\tA\t3\tq10\tNS=3;DP=11;AF=0.017\tGT:GQ:DP:HQ\t0|0:49:3:58,50\t0|1:3:5:65,3\t0/0:41:3']))

class VcfReader:
    def __init__(self, vcf_file_name):
        self.name_of_file = vcf_file_name

        self.all_lines_file = [x.strip() for x in open(vcf_file_name)]

        self.column_header = [x.strip('\n').split('\t') for x in self.all_lines_file if ( not x.startswith('##') and  x.startswith('#'))]

        self.file_header = [x.strip() for x in self.all_lines_file if x.startswith('##')]

        self.lines = [x.strip('\n').split('\t') for x in self.all_lines_file if not x.startswith('#')]

    def __str__(self):
        return self.name_of_file

    def __len__(self):
        return len(self.all_lines_file)
    def get_chrom(self, number):
        return [x.strip('\n').split('\t') for x in self.all_lines_file if (not x.startswith('#') and x.startswith(str(number)))]


vr = VcfReader('example.vcf')


column_header = vr.column_header
header = vr.file_header

# print(vr.lines)


"""
Section 3 Regular expressions and webscraping

Complete each of the definitions below.
Unless otherwise stated, all definitions should ignore overlapping matches.
"""
import re


def protein_motif1(my_string):
    """
    Return a list of all matches in my_string to the protein motif:
        a single C,
        followed by 2 H or P
        followed by a single C
        followed by 2 to 4 H or P
        followed by a single C
    """
    return re.findall(r'C[H,P]{2}C[H,P]{2,4}C', my_string)


def protein_motif2(my_string):
    """
    Return a list of all matches in my_string to the protein motif:
        a single L
        followed by 2 to 7 of any P, K, W or G
        followed by either 3 L or 3 I
        followed by a W
    """
    return re.findall(r'L[P,K,W,G]{2,7}[L,I]{3}W', my_string)

def protein_motif3(my_string):
    """
    Return all non-overlapping matches to the motif:
        A single L, followed by a single R, repeated 2 to 1000 times
    every match should extend up to 1000 repeats, preferring the longest match possible
     EX: LRLRLRLRLRLRLRLRxxxxxLR  --should match--> 'LRLRLRLRLRLRLRLR' and 'LR'
    """
    return re.findall(r'[L,R]{2,1000}', my_string)


def motif_starts(my_string):
    """
    Return a list of ints, representing the start positions of every match to the motif:
        a single L
        followed by 2 P
        followed by a single C
        followed by 8 to 10 of any I, V, L
     EX: LPPCVVVVVVVVXXXXLPPCVVVVVVVV --> [0, 16]
    """
    all_matches = re.finditer(r'LPPC[I,V,L]{8,10}', my_string)
    list = []
    for x in all_matches:  # error if no matches
        list.append(x.start())
    return list


def motif_lengths(my_string):
    """
    Return a list of ints, representing the length of every match to the motif:
         2 to 3 C
         followed by a single A
         followed by 2 to 3 T
     EX: CCATTXXCCCATTTXXCCCATT --> [5, 7, 6]
    """
    all_matches = re.finditer(r'C{2,3}AT{2,3}', my_string)
    list = []
    for x in all_matches:  # error if no matches
        list.append(len(x.group()))
    return list



def variable_region(my_string):
    """
    Return a list of strings representing ONLY the variable region (not the whole match) for the motif:
        4 W
        followed by an unknown number of letters  (This is the variable region that should be returned)
        followed by 4 to 7 of any W or Q
    This definition should prefer the shortest possible matches, and ignore overlapping matches
     EX:  WWWWABCDEWWWWABCDEWQWQWQ  --should match only-->  WWWWABCDEWWWW  --and return-->  ABCDE
    """
    return  re.findall(r'WWWW(.*?)[W,Q]{4,7}', my_string)


"""
Section 4

__main__, importing, and argparse

Your code should meet all of the following conditions
    1. All code for this section should only run inside if this script is being run as __main__
    
    2. Import the FastaReader class (from fasta_reader.py), argparse, and sys
    
    3. Initialize an instance of the FastaReader class with the file provided by --input (args.input)
        * args.input must be a required parameter, if it is not provided, the script should fail immediately
        
    4. If --docs is specified (args.doc) then the program should print the docstring for the FastaReader class
        EX: "exam2.py  --input example.fasta --docs" ->  "THIS IS THE FastaReader DOCSTRING"
    
    5. If --comp is specified, it should write a new fasta file of the reverse complement of every sequence to 
        the path specified by args.comp. The FastaReader class has definition to help called rev_complement_seqs()
        EX: "exam2.py --input example.fasta --comp rev_comp_example.fasta" -> a new FASTA file named 
            "rev_comp_example.fasta" where the sequences are the the reverse complement of "example.fasta"
"""
# To write a file containing the FastaReader class, uncomment and run the next two lines
# with open('fasta_reader2.py', 'w') as outfile:
#     outfile.write('\n'.join(['import os', '', '', 'COMP_DICT = {"A": "T", "T": "A", "C": "G", "G": "C"}', '', 'class FastaReader:', '    """', '    THIS IS THE FastaReader DOCSTRING', '    """', '', '    def __init__(self, fname):', '        self.name = fname', '        if os.path.isdir(fname):', '            files = [os.path.join(fname, x) for x in os.listdir(fname)]', '        else:', '            files = [fname]', '        self.lines = []', '        for f in files:', '            self.lines += [x.strip() for x in open(f)]', '        self.lines = _clean_lines(self.lines)', "        self.headers = [x for x in self.lines if x.startswith('>')]", "        self.seqs = [x for x in self.lines if not x.startswith('>')]", '', '    def to_dict(self):', '        return {h:s for h,s in zip(self.headers, self.seqs)}', '', '    def get_headers(self, n):', '        return self.headers[:n]', '', '    def get_seqs(self, n):', '        return self.seqs[:n]', '', '    def __str__(self):', '        return self.name', '', '    def __len__(self):', '        return len(self.headers)', '', '    def rev_complement_seqs(self):', '        """', '        :return: a list of all reverse complemented sequences in the FASTA file', '        """', '        return [rev_complement(x) for x in self.seqs]', '', 'def rev_complement(seq):', '    """', '    Returns the complement of a sequence', '    """', "    return ''.join([COMP_DICT[x] for x in seq][::-1])", '', 'def _clean_lines(lines):', '    """', '    if the lines of a FASTA file do not alternate sequence and header,', '    then concatenate all sequences between each header and return a list of the new lines', '    (Remember, the "_" Underscore at the beginning of a definition means it is intended to', "      be 'private', but nothing is really 'private' in python -", '      see https://mail.python.org/pipermail/tutor/2003-October/025932.html for a laugh)', '    """', '    # this is a verbose solution with decent time', '    new_lines = []', "    seq = ''", '    header = None', '    for line in lines:', "        if line.startswith('>'):", '            if seq:', '                new_lines.append(header)', '                new_lines.append(seq)', "                seq = ''", '            header = line.rstrip()', '        else:', '            seq += line.rstrip()', '    new_lines.append(header)', '    new_lines.append(seq)', '', '    return new_lines']))
#
# # To write an example FASTA file, uncomment the next two liens
# with open('example.fasta', 'w') as outfile:
#     outfile.write('\n'.join(['>header1', 'AAACT', '>header2', 'CCCGT', '>header3', 'GGGTA', '>header4', 'TTTAG']))


from fasta_reader2 import FastaReader
import argparse
import sys
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input', action="store")
    parser.add_argument('doc', nargs='?', default=None)
    parser.add_argument('comp', nargs='?', default=None)
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        print('Exception while parsing the argument')
        sys.exit(1)
    f_reader = FastaReader(args.input)
    if args.doc != None:
        print(f_reader.__doc__)
    if args.comp != None:
        f_reader = FastaReader(args.comp)
        reverse_complement = f_reader.rev_complement_seqs()
        with open('rev_comp_example.fasta', 'w') as outfile:
            outfile.write('\n'.join(reverse_complement))

"""
EXAM END
"""




