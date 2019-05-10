"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".

"""


# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    dict = {'C': 'G', 'A': 'T', 'G': 'C', 'T': 'A'}
    complementtemp = ""

    for i in range(0, len(dna)):
        complementtemp += dict.get(dna[i])
    return complementtemp

# print("Question1 ---------- ")
# print(fast_complement("CTAG"))

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    newString = ""
    newString += s[0:start]
    newString += s[stop+1:len(s)]

    return newString

# print("Question2 ---------- ")
# print(remove_interval('ABCDEFGHI', 2, 5))

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    kmer = []
    for i in range(0,len(s)):
        string = s[i:i+k]
        if len(string) == k:
            kmer.append(string)
    return kmer

    
# print("Question3 ---------- ")
# print(kmer_list('CATCAT',3))

def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer = set()
    for i in range(0,len(s)):
        string = s[i:i+k]
        if len(string) == k:
            kmer.add(string)
    return kmer

# print("Question4 ---------- ")
# print(kmer_set('CATCAT',3))

def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmer = {}
    for i in range(0,len(s)):
        string = s[i:i+k]
        if len(string) == k:
            if string in kmer:
                kmer[string] += 1
            else:
                kmer[string] = 1
    return kmer


# print("Question5 ---------- ")
# print(kmer_dict('CATCAT',3))

# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name,'r') as p:
        x = p.readlines()[0:10]
        for i in x:
            print i,
    return

# print("Question6 ---------- ")
# head('homework_1.py')

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name, 'r') as p:
        line = p.readlines()
        newline = "".join(line[-10:])
        print(newline)
    return

# print("Question7 ---------- ")
# tail('homework_1.py')


def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    line_no = 1
    with open(file_name, 'r') as p:
        for line in p.readlines():
            if line_no % 2 == 0:
                print(line),
            line_no += 1
    return

# print("Question8 ---------- ")
# print_even('homework_1.py')


def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    
    with open(file_name, 'r') as f:
        results = []
        for line in f.readlines():
            line = line.replace("\r\n","") 
            words = line.split(',')
            results.append((words[0:]))

    return results

# print("Question9 ---------- ")
# print(csv_list('mycsvfile.csv'))


def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    list = []

    with open(file_name, 'r') as f:
        results =[]
        for line in f.readlines():
            line = line.replace("\r\n","") 
            words = line.split(',')
            results.append((words[0:]))
         
        for i in results:
            list.append(i[column])                        

    return list

# print("Question10 ---------- ")
# print(get_csv_column('mycsvfile.csv', 0))


def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    list_seqs =[]
    
    with open (file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            if seq <> '':
                try:
                    x = seq.split('\n', 1)                   
                    sequence = x[1].replace('\r', '')
                    sequence = sequence.replace('\n', '')
                    list_seqs.append(sequence)
                                                
                except:
                    print('error')
          
    return list_seqs

# print("Question11 ---------- ")
# print(fasta_seqs('proper_fasta.fasta'))

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """

    list_headers = []
    
    with open (file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            if seq <> '':
                try:
                    x = seq.split('\n', 1)
                    header = x[0].replace('\r','')                       
                    list_headers.append(header)                          
                                
                except:
                    print('error')

    return list_headers


# print("Question12 ---------- ")
# print(fasta_headers('proper_fasta.fasta'))

def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """

    
    my_dictionary ={}
    my_list=['A','C','G','T']
    output_seq = ""
    
    with open (file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
                if seq <> '':              
                    x = seq.split('\n', 1)
                    header = x[0].replace('\r','')                       
                    sequence = x[1].replace('\r', '')
                    sequence = sequence.replace('\n', '')
                    my_dictionary[header] = sequence
                            
    return my_dictionary
    
# print("Question13 ---------- ")
# print(fasta_dict("proper_fasta.fasta"))

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """

    with open (file_name, 'r') as infile:
        text = infile.read()
        file_name = file_name.split('.')
        seqs = text.split('@')
        for seq in seqs:
            if seq <> '':
                    try:
                        x = seq.split('\n', 1)                       
                        header = x[0].replace('\r','')                       
                        sequence = x[1]
                        newseq = sequence.split('+')[0]
                 
                                     
                        with open(file_name[0] +'.fasta','a') as outfile:
                            outfile.write('>')
                            outfile.write(header)
                            outfile.write("\n")
                            outfile.write(newseq)
                    except:
                        print('error')        

    return None

# print("Question14 ---------- ")
# print (fastq_to_fasta('proper_fastq.fastq'))

# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """

    dict = {'C': 'G', 'A': 'T', 'G': 'C', 'T': 'A'}
    complement = ""

    for i in range(0, len(dna)):
        complement += dict.get(dna[i])
    complement =complement[::-1]    
    return complement


# print("Question15 ---------- ")
# print (reverse_complement('CTAG'))

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """

    result = ""
    for i in dna:
        i = i.replace('T','U')
        result += i
    
    return result

# print("Question16 ---------- ")
# print(transcribe('CGAT'))

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
 
    i = 0
    protein = ""
    rnalength = len(rna)
    while (rnalength != 0):
        x = rna[i:i+3]
        if x is None:
            x=  ''
        else:
            x = str(x)
        m = RNA_CODON_TABLE.get(x)
        if m <> '*':
            protein += m
        i+=3
        rnalength -= 3
        
    return protein



# print("Question17 ---------- ")
# print(translate('UUUGGUGGUUAA'))


def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    
    dict = {'C': 'G', 'A': 'T', 'G': 'C', 'T': 'A'}
    complementdna = ""
    i = 0 
    count = 0
    str1 =""
    str2 =""
    str3=""
    str4 =""
    str5=""
    str6=""
    list =[]

    length = len(dna)
    nof1 = len(dna)/3

    for m in range(0, len(dna)):
        complementdna += dict.get(dna[m])
    
    complementdna = complementdna[::-1]

    while (count != nof1):
        str1 += dna[i:i+3]
        str2 += dna[i+1:i+4]
        str3 += dna[i+2:i+5]
        str4 += complementdna[i:i+3]
        str5 += complementdna[i+1:i+4]
        str6 += complementdna[i+2:i+5]
             
        i+=3
        count += 1
     
    list.append(str1)
    list.append(str2)
    list.append(str3)
    list.append(str4)
    list.append(str5)
    list.append(str6)

    return list

# print("Question18 ---------- ")
# print(reading_frames('CTAGAT'))
