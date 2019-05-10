"""
Exam 1

Complete each of the definitions below. If you are stuck on a problem, move on and come back to it later.
If you have any questions about what a definition should do, please ask.

Here are some rules to follow:
    1) When you submit this completed exam, running it should not print anything. Please remove or comment
        all print statements.
    2) Remove or comment all ASSERT statements. If you leave a ASSERT statement uncommented and it fails,
        I am unable to import your code and grade it, which is bad for your grade.
    3) Your submission should NOT write any files, if it does, I will make exam 2 harder.
    3) Double check that each definition has a return value. Your exams will be graded using the return values.
    4) No Cheating. If you are caught cheating, you fail the course immediately. Instead, just fail the exam
        without cheating, there are more opportunities to improve your grade later.
    5) The 'assert' test cases are not the grader. These statements are to provide examples of how to test your code;
        they will not include every possible test case and passing all assert statements is not an "A".

"""


# 0) Name and RedID -----------------------------------------------------
def name_id():
    """
    This def is how I will identify who this exam belongs to. If you would like me to double check this question, please ask
    :return: a list of [redID, first_name, last_name]
    """
    return ['819800560', 'Lakshmiprabha', 'Sudersanan']

#assert name_id() == ['819800560', 'Lakshmiprabha', 'Sudersanan'], "Please return your own name and redID, or you wont recieve a grade"



# 1) Reverse compliment -------------------------------------------------
def reverse_compliment(dna):
    """
    Given a string of DNA, return its reverse compliment
    :param dna: a string of only the characters "A", "C", "T", and "G"
    :return: a string of only the characters "A", "C", "T", and "G"
    """
    new_string = ''
    comp = {'A':'T','T':'A','C':'G','G':'C'}
    for i in dna:
        new_string = new_string + comp[i] 
    return new_string[::-1]

#print(reverse_compliment("AAACCCTGTG"))
#assert reverse_compliment("AAACCCTGTG") == "CACAGGGTTT", "Try question 1 again."



# 2) K-mer list ------------------------------------------------------
# Remember k-mers?  at k=3  "AACCGT" -> ['AAC', 'ACC', 'CCG', 'CGT']
def kmer_to_list(dna, k):
    """
    Given a string of DNA, return a list of all k-mers of length k
    :param dna: a string of only the characters "A", "C", "T", and "G"
    :param k: an integer > 0
    :return: a list of DNA strings that are all length k
    """
    kmer_list = []
    for idx,letter in enumerate(dna):
        if idx + k >len(dna):
            break
        kmer_list.append(dna[idx:idx+k])

    return kmer_list
# print( kmer_to_list("AACCGT", 3))
# assert kmer_to_list("AACCGT", 3) == ['AAC', 'ACC', 'CCG', 'CGT'], "Try question 2 again"



# 3) K-mer counts -----------------------------------------------------
def kmer_counts(kmer_list):
    """
    Given a list of k-mers (similar to the output from #2), use a dictionary to count how many times each k-mer occurred;
    the key should be the k-mer (string) and the value should be the number of times it appears in the list (integer)
    :param kmer_list: a list of DNA strings
    :return: a dictionary of the form {k-mer: count, ..} where k-mer is a DNA string, and count is an integer
    """
    dict ={}
    for kmer in kmer_list:
       if kmer in dict:
           count = dict[kmer]
           dict[kmer] = count+1
       else:
           dict[kmer] = 1
    return dict
# print(kmer_counts(['AAA', 'AAA', 'AAA', 'AAC', 'ACC', 'CCC', 'CCC']))
#assert kmer_counts(['AAA', 'AAA', 'AAA', 'AAC', 'ACC', 'CCC', 'CCC']) == {'AAA': 3, 'AAC': 1, 'ACC': 1, 'CCC': 2}, "Try question 3 again"



# 4) Dictionary iterating ----------------------------------------------
def most_abundant(my_dict):
    """
    Given a dictionary where keys are strings, and values are integers, return the key with the highest value.
    If there are multiple keys with the largest value, you may return any one.
    :param my_dict: a dictionary of the form {string: int, ...}
    :return: a string
    """
    count = 0
    sequence_key = ''
    for key in my_dict.keys():
        if my_dict[key] > count:
            count = my_dict[key]
            sequence_key = key

    return sequence_key

# print(most_abundant({'AAA': 3, 'AAC': 1, 'ACC': 1, 'CCC': 2}))
# assert most_abundant({'AAA': 3, 'AAC': 1, 'ACC': 1, 'CCC': 2}) == "AAA", "Try question 4 again"



# 5) String formatting ------------------------------------------------
def string_corrector(my_str, my_char):
    """
    Given a string, enforce the following conditions, and apply the fix if necessary:
        1. If the string ends in a new line character ('\n') remove it
        2. If there are any tab characters ('\t') in the string, replace them with commas (',')
        3. If the character at index 7 is not my_char, change it to my_char
        * tab and newline characters are only length 1, despite appearing as 2 characters
            (for example: 'abc\n' is length 4, because \n counts as 1 character)
    :param my_str: a string of length > 10
    :param my_char: a string of length 1
    :return: a string
    """
    my_str = my_str.replace('\n','').replace('\t',',')
    if not my_str[7] == my_char:
        my_list = list(my_str)
        my_list[7] = my_char
    return ''.join(my_list)

# print(string_corrector("012345678\t9\t10\n", "X"))

#assert string_corrector("012345678\t9\t10\n", "X") == '0123456X8,9,10', "Try question 5 again"



# 6) FASTA check -------------------------------------------------------
def duplicate_headers(fasta_file):
    """
    Given a fasta file, check to see if there are any duplicate headers, return True if there are, False otherwise
    :param fasta_file: a text file in the FASTA file
    :return: boolean, True or False
    """
    all_headers = []
    with open(fasta_file) as input_file:
        for line in input_file:
            line = line.strip()
            if line.startswith('>'):
                all_headers.append(line.replace('\n', '').replace('>',''))
        if len(all_headers) > len(set(all_headers)):
            return True
        else:
            return False

# print(duplicate_headers('fasta_example.fasta'))

# assert duplicate_headers('fasta_example.fasta') == False, "Try problem 6 again"
# Uncomment the following line to generate the test file: "fasta_example.fasta"
# with open('fasta_example.fasta', 'w') as outfile: [outfile.write(line) for line in ['>human\n', 'AAACCCGGGTTT\n', '>corn\n', 'GGGTTTAAACC\n', 'CCCGGGTTTAA\n', '>cat\n', 'CATCAT\n', '>cat\n', 'CATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT\n']]



# 7) CSV Reading --------------------------------------------------------
def csv_to_dictionary(csv_file, column1, column2):
    """
    Given a CSV file and two column numbers, return a dictionary where each line in the CSV file becomes one entry and
     the key is the item in column1 and the value is in column2.
    You should also ignore the header line, and not input that line into your dictionary
    :param csv_file: string, name of the CSV file
    :param column1: int, index of the first column, these will become keys
    :param column2: int, index of the second column, these will become values
    :return: a dictionary
    """
    dictionary = {}
    with open(csv_file) as input_file:
        for idx, line in enumerate(input_file):
            if idx == 0:
                continue
            line = line.strip()
            value = line.split(',')
            dictionary[value[column1]] = value[column2]
    return dictionary

# print(csv_to_dictionary('csv_example.csv', 0, 3))
# assert csv_to_dictionary('csv_example.csv', 0, 3) == {'banana': '2', 'apple': '5', 'grapes': '2', 'lemon': '4', 'orange': '3', 'watermelon': '5', 'tomato': '1'}
# Uncomment the following line to generate the test file: "fasta_example.fasta"
# with open('csv_example.csv', 'w') as outfile: [outfile.write(line) for line in ['fruit,flavor,convenience,durability\n', 'banana,5,5,2\n', 'apple,3,4,5\n', 'grapes,4,4,2\n', 'lemon,1,3,4\n', 'orange,3,3,3\n', 'watermelon,4,1,5\n', 'tomato,2,2,1']]



# 8) Transcription ------------------------------------------------------
def transcription(dna):
    """
    Transcribe the DNA string given into RNA and return the resulting string
        DNA 5'-ACGACCGTTCCA-3'
        RNA 3'-UGCUGGCAAGGU-5'
        (always write nucleotides from 5' to 3')
        RNA 5'-UGGAACGGUCGU-3'
    :param dna: string
    :return: string
    """
    compliment = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
    transcribed_dna = ""
    for i in dna:
        transcribed_dna = transcribed_dna + compliment[i];
    return transcribed_dna[::-1]

# print(transcription('ACGACCGTTCCA'))
#assert transcription('ACGACCGTTCCA') == "UGGAACGGUCGU", 'Try question 8 agian'



# 9) Translation --------------------------------------------------------
RNA_TO_AA = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
    "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def translate(rna):
    string = ''
    for i in range(0,len(rna),3):
        codon = rna[i:i+3]
        string = string + RNA_TO_AA [codon] 

    """
    Given a string of RNA, convert it entirely to its Amino Acid sequence
    :param rna: a string
    :return: a string
    """
    return string

# print(translate('UGGAACGGUCGU'))
# assert translate('UGGAACGGUCGU') == 'WNGR', "Try question 9 again"
