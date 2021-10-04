def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern


def Reverse(Pattern):
    rev = ''.join(reversed(Pattern))
    return rev


def Complement(Pattern):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reverseComplement = ""
    for char in Pattern:
        reverseComplement = reverseComplement + complement.get(char)
    return reverseComplement


print(ReverseComplement("GATTACA"))
