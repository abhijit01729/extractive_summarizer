import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

import nltk
nltk.download('punkt')

class TextSummarizer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Extractive Text Summarizer')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.label = QLabel('Enter text to summarize:')
        self.layout.addWidget(self.label)

        self.input_text = QTextEdit(self)
        self.layout.addWidget(self.input_text)

        self.summarize_button = QPushButton('Summarize', self)
        self.summarize_button.clicked.connect(self.summarize_text)
        self.layout.addWidget(self.summarize_button)

        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        self.layout.addWidget(self.output_text)

        self.setLayout(self.layout)

    def summarize_text(self):
        input_text = self.input_text.toPlainText()
        if input_text.strip():
            summary = self.extractive_summary(input_text)
            self.output_text.setPlainText(summary)
        else:
            self.output_text.setPlainText('Please enter some text to summarize.')

    def extractive_summary(self, text):
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 5)  # Summarize to 5 sentences

        summary_text = "\n".join([str(sentence) for sentence in summary])
        return summary_text

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextSummarizer()
    ex.show()
    sys.exit(app.exec_())