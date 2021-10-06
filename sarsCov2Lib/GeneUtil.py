import pkgutil
import re
from sarsCov2Lib.Codon import Codon
from sarsCov2Lib.RangeDict import RangeDict

class GFFEntry:

    def __init__(self, chromosome, startPos, endPos, geneName, geneFastaSequence):
        self.chromosome = chromosome
        self.startPos = startPos
        self.endPos = endPos
        self.geneName = geneName
        self.geneFastaSequence = geneFastaSequence
        self.aminoAcidTripletDict = RangeDict()
        self.__enrichAminoAcids()

    def __enrichAminoAcids(self):
        codon = Codon()
        triplets = [(i, self.geneFastaSequence[i:i+3]) for i in range(0, len(self.geneFastaSequence), 3)]
        for idx, triplet in triplets:
            aminoAcidRange = (self.startPos + idx, self.startPos + 2 + idx)
            aminoAcid = codon.getAminoAcid(triplet)
            self.aminoAcidTripletDict[aminoAcidRange] = aminoAcid

    def getAminoAcidPosition(self, position):
        if position in self.aminoAcidTripletDict:
            test = self.aminoAcidTripletDict[position]
            return self.aminoAcidTripletDict[position]

 #   def getAminoAcidRange(self, position):
 #       if position in self.aminoAcidTripletDict:
 #           test = self.aminoAcidTripletDict.transform_key(position)
 #           return self.aminoAcidTripletDict.transform_key(position)


class GeneUtil:

    def __init__(self):
        self.gffMap = dict()
        self.fastaSequence = ""
        self.genomeLength = None
        self.gffFile = "reference/NC_045512.2.gff3"
        self.fastaReference = "reference/NC_045512.2.fasta"
        self._readFastaReference()
        self._readGFF()


    def _readFastaReference(self):
        self.fastaSequence = ""
        fasta_reader = pkgutil.get_data(__name__, self.fastaReference)
#        with open(fasta, 'r') as fasta_reader:
        fasta = fasta_reader.decode('utf-8')
        for line in fasta.splitlines():
            if not line.startswith(">"):
                line = line.rstrip()
                self.fastaSequence += line
        self.genomeLength = len(self.fastaSequence)


    def getFastaSequenceRange(self, startPos, endPos):
        return self.fastaSequence[startPos - 1 :endPos]

    def getFastaSequence(self, position):
        return self.fastaSequence[position-1]


    def getGffEntryByPosition(self, position):
        for geneName, gffEntryList in self.gffMap.items():
            for gffEntry in gffEntryList:
                if gffEntry.startPos <= position <= gffEntry.endPos:
                    return gffEntry
        return None

    def _readGFF(self):
        p = re.compile("gene=(\w*);")
        gffFile = pkgutil.get_data(__name__, self.gffFile)
        gff = gffFile.decode('utf-8')
        #with open(self.gffFile, 'r') as gff_reader:
        for line in gff.splitlines():
            line = line.rstrip()
            if not line.startswith("#") and line != "":
                tabs = line.split("\t")
                chromosome = tabs[0]
                annotationType = tabs[2]
                startPos = int(tabs[3])
                stopPos = int(tabs[4])
                if annotationType == "CDS":
                    result = p.search(tabs[8])
                    if result:
                        fastaSeq = self.getFastaSequenceRange(startPos, stopPos)
                        geneName = result.group(1)
                        gffEntry = GFFEntry(chromosome, startPos, stopPos, geneName, fastaSeq)
                        if geneName in self.gffMap:
                            self.gffMap[geneName].append(gffEntry)
                        else:
                            self.gffMap[geneName] = [gffEntry]

