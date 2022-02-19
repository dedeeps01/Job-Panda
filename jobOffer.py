# the goal of this is to upload a job offer letter, scan for position, location, 401k/Roth IRA, 
# and return a quickview summary. 
import nltk
import PyPDF2

# extracting text from pdf files 
JobOfferPDF = open('example.pdf', 'rb')

