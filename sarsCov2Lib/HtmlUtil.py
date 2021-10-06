import collections


class GeneHtmlConverter:

    def __init__(self):
        self.geneMap = collections.OrderedDict()
        self.genesList = []
        self.aminoAcidList = []
        self.rangeList = []
        self.nucleotideList = []
        self.positionList = []

        self.aminoAcidListGrouped = []

    def addEntry(self, geneName, aminoAcid, nucleotide, range, position):
        self.genesList.append(geneName)
        self.aminoAcidList.append(aminoAcid)
        self.nucleotideList.append(nucleotide)
        self.rangeList.append(range)
        self.positionList.append(position)

    def __getBackgroundColor(self, entity):
        backgroundColor = "#ebebeb"
        if entity == "":
            backgroundColor = "white"
        return backgroundColor

    def getGenesHtml(self):
        genesHtml = "<tr><td style='white-space: nowrap;'>Gene:</td>"
        counter = 0
        for gene, nextGene in zip(self.genesList, self.genesList[1:]):
            counter += 1
            if gene != nextGene:
                genesHtml += "<td style='border:1px solid white; " \
                             "background-color:" + self.__getBackgroundColor(gene) + "; text-align:center;'" \
                                                                                     " colspan='" + str(
                    counter) + "'>" + gene + "</td> "
                counter = 0
        genesHtml += "<td style='border:1px solid white; " \
                     "background-color:" + self.__getBackgroundColor(nextGene) + "; text-align:center;'" \
                                                                                 " colspan='" + str(
            counter + 1) + "'>" + nextGene + "</td> "
        return genesHtml

    def getAminoAcidHtml(self):
        self.aminoAcidListGrouped = []
        aminoAcidHtml = "<tr><td style='white-space: nowrap;'>Amino acid:</td>"
        counter = 0
        for idx, (aminoAcid, nextAminoAcid) in enumerate(zip(self.rangeList, self.rangeList[1:])):
            counter += 1
            if aminoAcid != nextAminoAcid:
                self.aminoAcidListGrouped.append(self.aminoAcidList[idx])
                aminoAcidHtml += "<td style='border:1px solid white; " \
                                 "background-color:" + self.__getBackgroundColor(
                    self.aminoAcidList[idx]) + "; text-align:center;'" \
                                               " colspan='" + str(counter) + "'>" + self.aminoAcidList[idx] + "</td> "
                counter = 0
        self.aminoAcidListGrouped.append(self.aminoAcidList[idx + 1])
        aminoAcidHtml += "<td style='border:1px solid white; " \
                         "background-color:" + self.__getBackgroundColor(
            self.aminoAcidList[idx + 1]) + "; text-align:center;'" \
                                           " colspan='" + str(counter + 1) + "'>" + self.aminoAcidList[
                             idx + 1] + "</td> "
        return aminoAcidHtml

    def getMargin(self, position):
        pos = str(position)
        posMap = {
            1: "12",
            2: "10",
            3: "7",
            4: "4",
            5: "2",
        }
        return posMap[len(pos)]

    def getPositionHtml(self):
        positionHtml = "<tr><td>&nbsp;</td>"
        for position in self.positionList:
            if position % 5 == 0:
                positionHtml += "<td style='font-size:10px; text-align:center;' ><div> &#x7c;</div>" \
                                "<div style='white-space: nowrap; margin-left:" + self.getMargin(
                    position) + "; margin-right:" + self.getMargin(position) + ";'> " \
                                                                               "" + str(position) + "</div></td>"
            else:
                positionHtml += "<td style='font-size:10px;'> <div style='margin-left:15px; margin-right:15px;'>&nbsp;</div></td>"
        return positionHtml

    def getNucleotideHtml(self):
        nucleotideHtml = "<tr><td>Nucleotide:</td>"
        for nucleotide in self.nucleotideList:
            nucleotideHtml += "<td style='border:1px solid white; background-color:#ebebeb; text-align:center;'>" \
                              + self.__colorNucleotides(nucleotide) \
                              + "</td>"
        return nucleotideHtml

    def convert2Html(self):
        htmlResult = "<table >" + self.getGenesHtml() + "</tr>" + self.getAminoAcidHtml() + "</tr>" + \
                     self.getNucleotideHtml() + "</tr>" + self.getPositionHtml() + "</tr></table>"
        return htmlResult

    def getAminoAcidGroupedList(self):
        return [aminoAcid if aminoAcid != "" else " " for aminoAcid in self.aminoAcidListGrouped]

    def getNucleotideList(self):
        return self.nucleotideList

    def __colorNucleotides(self, nucleotide):
        colors = {
            'G': "<span style='color:orange'>G</span>",
            'A': "<span style='color:green'>A</span>",
            'T': "<span style='color:red'>T</span>",
            'C': "<span style='color:blue'>C</span>"
        }
        return colors[nucleotide]
