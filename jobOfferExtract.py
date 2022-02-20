# the goal of this is to extract text from a PDF uploaded by the user and to tokenize the text 

from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.probability import FreqDist
from pdfminer.converter import TextConverter
from pdfminer.pdfparser import PDFParser
from pdfminer import extract_text 

# extract text from pdf file
OfferText = extract_text('example.pdf')

# create tokenizer 

tokenizeText = RegexpTokenizer('\w+')

# tokenize 

offerTokens = tokenizeText.tokenize(OfferText)