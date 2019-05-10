
#Exercise01

def hello():
    print("Hello World")
    return

def percent_decimal(i):
    if (i<=100 and i>=1):
        answer = round(i / 100, 6)
    else :
        answer = round(i * 100, 6)
    return answer

def exponent(integer, power):
    expo = 1
    while (power != 0) :
        expo = expo * integer
        power = power - 1
    return expo

def complement(dna):
    dict = {'C': 'G', 'A': 'T', 'G': 'C','T':'A'}
    dnasize = len(dna)
    complementtemp = ""
    for i in range(0,dnasize):
        complementtemp = complementtemp + dict.get(dna[i])
    return complementtemp
