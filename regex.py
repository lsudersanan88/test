
test_protein = """MHMWSFMMRFRKGGKPYHTVADARGPYDNGHLHKTYYLKNLMYYTVGMWVKEQLCCRHEP
RSFLLAFIWSWCLAGVYRLTHRGSGPEMNRVVMFQYQDECSYLLQVTDVAYCNEQAWYAR
FWSCIASSFEMSSHELHTQHYYTLTGSVDWNMYVQNGVWAHGIACSMTDNQDGSCRQPIM
DTDYVDTHDHEKRYRQRGLCSTPCNDQFPGYEFPTVHGTMAWISGEMMCASGYKPYNFKH
GEFSPKSIWEWQLFACCCCGKTEWSNVMIFMVVEIEIFASKSNEENWSGMNIIEDDDPQH
HFKNIYRKYLDFQFYLIYGGYRMGFLHHRDSMINALVCKTGRWQQMHSFLKCDRRCKYLI
NIYADGKWYDNWSKVEDKVLDRGIRFLQSWNATEMVNSSMYRKPFYQSQYAPRFCWETFC
QHEIYFHQEYASNCKARCGSYQSSAQSATLAIKYSELYQGFWGTSEWGHHQLFIHRWGVQ
IYQVKLHDSIMRPWIDWSRKCKWLLHRLHCDIELVPIHWEHKPQRVSFYYFKAMTDVLRE
ICWSAQYHVVIQKFAFITMAWICTFYVHMYPSLDRHGSVTGIAWKLSGQWTGQEAYSKLN
TEKETITEHNCPRVANIIVDCLEHEQVEMRMKRCHTWMVEVMKYPEQKFLWQCEHFRALY
GLVGHNCPIKAWVRWIPHMEQKVCSACCCCGKSMLKNPMSRDSVCRREMEYDMAISRMPY
GDCHAVGKWLPYFLNRYTPWWVWIWMAPFQGNRFFYHYKKDWRHCGNYLGGLCVLMTFWH
HPIYVPCPKTKADFKQACCYCGKTRQACTDENMDTQRQKFQALHQARICQPYTVRNMSIQ
CGKNPIKANHNNNVRRPTMHICNLPAMTRRFVYTPFMKLKQSLGHDKWHIPEIQPYMDFT
YHSVWIHQPHMNSCAACTGTVALALALALHYYTHPIQGEYIIYTSCDARYKSQKQEDIYQLPPIIIW
ITSTCLEFSSKFKAQMMGTTWEIAGMNFCKVIETSCRQKIZZZZZZZZZZZZZZZCHHCPPPCYYY
LPPIIIW""".replace('\n', '')


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
    pattern = r'C[HP]{2}C[HP]{2,4}C'
    return re.findall(pattern, my_string)
# print(protein_motif1(test_protein))

def protein_motif2(my_string):
    """
    Return a list of all matches in my_string to the protein motif:
        a single L
        followed by 2 to 7 of any P, K, W or G
        followed by either 3 L or 3 I
        followed by a W
    """
    pattern = r'L[PKWG]{2,7}(LLL|III)W'
    return [x.group(0) for x in re.finditer(pattern, my_string)]
    #return re.findall(pattern, my_string)
print(protein_motif2(test_protein))

def protein_motif3(my_string):
    """
    Return all non-overlapping matches to the motif:
        A single L, followed by a single R, repeated 2 to 1000 times
    every match should extend up to 1000 repeats, preferring the longest match possible
     EX: LRLRLRLRLRLRLRLRxxxxxLR  --should match--> 'LRLRLRLRLRLRLRLR' and 'LR'
    """
    # r'(LR){2,1000}'
    pattern = r'(LR){2,1000}'
    return [x.group() for x in re.finditer(pattern, my_string)]
# print(protein_motif3(test_protein))


def motif_starts(my_string):
    """
    Return a list of ints, representing the start positions of every match to the motif:
        a single L
        followed by 2 P
        followed by a single C
        followed by 8 to 10 of any I, V, L
     EX: LPPCVVVVVVVVXXXXLPPCVVVVVVVV --> [0, 16]
    """
    pattern = r'LPPC[IVL]{8,10}'
    matches = re.finditer(pattern, my_string)
    return [x.start() for x in matches]


def motif_lengths(my_string):
    """
    Return a list of ints, representing the length of every match to the motif:
         2 to 3 C
         followed by a single A
         followed by 2 to 3 T
     EX: CCATTXXCCCATTTXXCCCATT --> [5, 7, 6]
    """
    pattern = r'C{2,3}AT{2,3}'
    matches = re.findall(pattern, my_string)
    return [len(x) for x in matches]

test = "WWWWABCDEWWWWABCDEWQWQWQ"

def variable_region(my_string):
    """
    Return a list of strings representing ONLY the variable region (not the whole match) for the motif:
        4 W
        followed by an unknown number of letters  (This is the variable region that should be returned)
        followed by 4 to 7 of any W or Q
    This definition should prefer the shortest possible matches, and ignore overlapping matches
     EX:  WWWWABCDEWWWWABCDEWQWQWQ  --should match only-->  WWWWABCDEWWWW  --and return-->  ABCDE
    """
    pattern = r'WWWW(.*?)[WQ]{4,7}'
    return re.findall(pattern, my_string)


print(variable_region(test))
