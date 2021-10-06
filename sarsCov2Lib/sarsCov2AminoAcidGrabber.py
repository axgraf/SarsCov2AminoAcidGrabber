#!/usr/bin/env python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from sarsCov2Lib.GeneUtil import GeneUtil
from sarsCov2Lib.HtmlUtil import GeneHtmlConverter

__version__ = '0.1'
__author__ = 'Alexander Graf'
__email__ = 'graf@genzentrum.lmu.de'


# Create a subclass of QMainWindow to setup the calculator's GUI
class AminoAcidGrabber(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sars-CoV-2 Amino Acid Grabber')
        # self.setFixedSize(1200, 450)
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.setMaximumHeight(450)
        self.generalLayout = QGridLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._initialize()
        self._createApp()

    def _initialize(self):
        self.geneUtil = GeneUtil()

    def _createApp(self):
        self.header = QLabel()
        self.header.setText("Sars-CoV-2 amino acid grabber")
        font = self.font()
        font.setPointSize(20)
        self.header.setFont(font)
        self.generalLayout.addWidget(self.header, 0, 1, Qt.AlignCenter)

        self.position_label = QLabel()
        self.position_label.setText("Nucleotide Position:")
        self.generalLayout.addWidget(self.position_label, 1, 0)

        self.positionInput = QSpinBox()
        self.positionInput.setRange(0, self.geneUtil.genomeLength)
        self.positionInput.setValue(21559)
        self.positionInput.setFixedWidth(100)
        self.generalLayout.addWidget(self.positionInput, 1, 1)

        self.offset_label = QLabel()
        self.offset_label.setText("Offset (left & right):")
        self.generalLayout.addWidget(self.offset_label, 2, 0)

        self.offsetInput = QSpinBox()
        self.offsetInput.setFixedWidth(100)
        self.offsetInput.setRange(0, 5000)
        self.offsetInput.setValue(10)
        self.generalLayout.addWidget(self.offsetInput, 2, 1)

        self.button = QPushButton("Grab amino acid")
        self.button.setFixedWidth(200)
        self.generalLayout.addWidget(self.button, 3, 1, Qt.AlignCenter)
        self.button.clicked.connect(self.grabAminoAcid)

        self.textArea = QTextBrowser()
        self.textArea.setFixedHeight(130)
        self.generalLayout.addWidget(self.textArea, 4, 1)

        self.copyAminoAcidButton = QPushButton("Copy amino acid sequence")
        self.copyAminoAcidButton.setFixedWidth(250)

        self.copyAminoAcidButton.setDisabled(True)
        self.copyAminoAcidButton.clicked.connect(self.copyAminoAcidSequence)
        self.generalLayout.addWidget(self.copyAminoAcidButton, 5, 1, Qt.AlignLeft)

        self.copyNucleotideButton = QPushButton("Copy nucleotide sequence")
        self.copyNucleotideButton.setFixedWidth(250)
        self.copyNucleotideButton.setDisabled(True)
        self.copyNucleotideButton.clicked.connect(self.copyNucleotideSequence)
        self.generalLayout.addWidget(self.copyNucleotideButton, 5, 1, Qt.AlignRight)

        self.footer = QLabel()
        self.footer.setText(
            "© Dr. Alexander Graf - Laboratory for functional genome Analysis - Gene Center - LMU Munich")
        font = self.font()
        font.setPointSize(7)
        self.footer.setFont(font)
        self.footer.setFixedHeight(30)
        self.footer.setContentsMargins(0, 15, 0, 0)
        self.generalLayout.addWidget(self.footer, 6, 1, Qt.AlignCenter)

    def enableCopyButtons(self):
        if self.html_converter:
            if len(self.html_converter.getAminoAcidHtml()) > 0:
                self.copyAminoAcidButton.setDisabled(False)
            if len(self.html_converter.getNucleotideList()) > 0:
                self.copyNucleotideButton.setDisabled(False)

    def limitPositions(self, startPos, endPos):
        if startPos < 0:
            startPos = 1
        if endPos > self.geneUtil.genomeLength:
            endPos = self.geneUtil.genomeLength
        return startPos, endPos

    def grabAminoAcid(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.html_converter = GeneHtmlConverter()
        position = self.positionInput.value()
        offset = self.offsetInput.value()
        startPos, endPos = self.limitPositions(position - offset, position + offset)

        for i in range(startPos, endPos + 1, 1):
            nucleotide = self.geneUtil.getFastaSequence(i);
            gffEntry = self.geneUtil.getGffEntryByPosition(i)
            if gffEntry:
                pos_range, aminoAcid = gffEntry.getAminoAcidPosition(i)
#                pos_range = aminoAcidEntry.getAminoAcidRange(i)
                pos_rangelist = [str(i) for i in list(pos_range)]
                self.html_converter.addEntry(gffEntry.geneName, aminoAcid, nucleotide, "-".join(pos_rangelist), i)
            else:
                self.html_converter.addEntry("", "", nucleotide, i, i)
        self.textArea.setHtml(self.html_converter.convert2Html())
        self.enableCopyButtons()
        QApplication.restoreOverrideCursor()

    def copyAminoAcidSequence(self):
        QApplication.clipboard().clear()
        QApplication.clipboard().setText("".join(self.html_converter.getAminoAcidGroupedList()))

    def copyNucleotideSequence(self):
        QApplication.clipboard().clear()
        QApplication.clipboard().setText("".join(self.html_converter.getNucleotideList()))


def main():
    aminoAcidGrabber = QApplication(sys.argv)
    view = AminoAcidGrabber()
    view.show()
    sys.exit(aminoAcidGrabber.exec_())


if __name__ == '__main__':
    main()
