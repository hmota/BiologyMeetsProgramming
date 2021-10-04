import sys                              # needed to read the genome

# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable

    k = len(Pattern)
    n = len(Genome)
    for i in range(n - k + 1):
        Match = Genome[i:i + k]
        if Match == Pattern:
            positions.append(i)

    return positions


input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]

print(PatternMatching("CTTGATCAT", v_cholerae))

# print(PatternMatching("ACAC", "TTTTACACTTTTTTGTGTAAAAA"))
# print(PatternMatching("AAA", "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT"))
# print(PatternMatching("TTT", "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"))
# print(PatternMatching("ATA", "ATATATA"))
