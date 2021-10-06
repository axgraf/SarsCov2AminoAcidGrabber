
class Codon:

    def __init__(self):
        self.codonMap = dict()
        self._initialize()

    def getAminoAcid(self, triplet):
        if triplet in self.codonMap:
            return self.codonMap[triplet]

    def _initialize(self):
        self.codonMap["TTT"] = "F"
        self.codonMap["TTC"] = "F"

        self.codonMap["TTA"] = "L"
        self.codonMap["TTG"] = "L"

        self.codonMap["TCT"] = "S"
        self.codonMap["TCC"] = "S"
        self.codonMap["TCA"] = "S"
        self.codonMap["TCG"] = "S"

        self.codonMap["TAT"] = "Y"
        self.codonMap["TAC"] = "Y"

        self.codonMap["TAA"] = "*"
        self.codonMap["TAG"] = "*"
        self.codonMap["TGA"] = "*"

        self.codonMap["TGT"] = "C"
        self.codonMap["TGC"] = "C"

        self.codonMap["TGG"] = "W"

        self.codonMap["CTT"] = "L"
        self.codonMap["CTC"] = "L"
        self.codonMap["CTA"] = "L"
        self.codonMap["CTG"] = "L"

        self.codonMap["CCT"] = "P"
        self.codonMap["CCC"] = "P"
        self.codonMap["CCA"] = "P"
        self.codonMap["CCG"] = "P"

        self.codonMap["CAT"] = "H"
        self.codonMap["CAC"] = "H"

        self.codonMap["CAA"] = "Q"
        self.codonMap["CAG"] = "Q"

        self.codonMap["CGT"] = "R"
        self.codonMap["CGC"] = "R"
        self.codonMap["CGA"] = "R"
        self.codonMap["CGG"] = "R"

        self.codonMap["ATT"] = "I"
        self.codonMap["ATC"] = "I"
        self.codonMap["ATA"] = "I"

        self.codonMap["ATG"] = "M"

        self.codonMap["ACT"] = "T"
        self.codonMap["ACC"] = "T"
        self.codonMap["ACA"] = "T"
        self.codonMap["ACG"] = "T"

        self.codonMap["AAT"] = "N"
        self.codonMap["AAC"] = "N"

        self.codonMap["AAA"] = "K"
        self.codonMap["AAG"] = "K"

        self.codonMap["AGT"] = "S"
        self.codonMap["AGC"] = "S"

        self.codonMap["AGA"] = "R"
        self.codonMap["AGG"] = "R"

        self.codonMap["GTT"] = "V"
        self.codonMap["GTC"] = "V"
        self.codonMap["GTA"] = "V"
        self.codonMap["GTG"] = "V"

        self.codonMap["GCT"] = "A"
        self.codonMap["GCC"] = "A"
        self.codonMap["GCA"] = "A"
        self.codonMap["GCG"] = "A"

        self.codonMap["GAT"] = "D"
        self.codonMap["GAC"] = "D"

        self.codonMap["GAA"] = "E"
        self.codonMap["GAG"] = "E"

        self.codonMap["GGT"] = "G"
        self.codonMap["GGC"] = "G"
        self.codonMap["GGA"] = "G"
        self.codonMap["GGG"] = "G"
