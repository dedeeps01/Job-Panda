# the goal of this is to extract text from a PDF uploaded by the user and to tokenize the text 
from nltk.tokenize import word_tokenize, RegexpTokenizer, sent_tokenize
#from nltk.probability import FreqDist
#from pdfminer.converter import TextConverter
#from pdfminer.pdfparser import PDFParser
from pdfminer.high_level import extract_text 

def main():
    offerText = extract_text('samples/sampleOfferLetter.pdf') # extract text from pdf, change it to be whatever we name the uploaded file
    offerSent = sent_tokenize(offerText)
    salary = searchSalary(offerSent)
    print(salary)
    '''if salary == 'fail':
        print('fail')
    else:
        print(salary)'''
    '''else:
        annualSal = salaryTime(salary,offerSent)
        print(annualSal)'''
            #print(location)
            #print(jobPosition)
'''
tokenizeText = RegexpTokenizer('\w+')
# tokenize 
offerWordTokens = tokenizeText.tokenize(offerText)'''

'''  location = searchLocation(offerSent)
        jobPosition = searchPosition(offerSent)
        if jobPosition == "Not found":
            print('fail')
        else:'''

def searchSalary(sentence):
    # maybe remove commas, maybe tokenize money?
    # tokenizeSal = RegexpTokenizer('\$[\d\.]')
    wordLst =[]
    salaryKeywords = ['salary', 'rate','pay', 'compensation','wage']
    for words in sentence:
        wordLst += word_tokenize(words)
        if salaryKeywords in wordLst:    # wordLst = [word_tokenize(i) for i in sentence]
            print('in wordLst')
            continue
    
    for num in wordLst:
        salary = 0
        if num.isdigit():
            salary = num
            print(salary)
        
             
    '''try:
        salary = tokenizeSal.word_tokenize(sentence)
        return salary 
    except:
        return 'Nothing' ''' 

'''def salaryTime(sal, sent):
    hourly = ['hour', 'hourly','hr']
    timeLst = []
    yearlySal = 0
    for words in sent:
        timeLst += word_tokenize(words)
        if hourly not in timeLst:    # wordLst = [word_tokenize(i) for i in sentence]
            yearlySal = sal
    else:
        yearlySal = sal * 40 * 48 # assumes work is fulltime and that there are 48 work weeks 
    return yearlySal'''
    
'''
def searchLocation(sentences):
    stateListFull = ["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    stateListAbbr = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MP", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UM", "UT", "VA", "VI", "VT", "WA", "WI", "WV", "WY"]
    wordLst = []
    matches = []
    # location = ''
    for words in sentences:
        wordLst+= word_tokenize(words)
        if stateListAbbr in words:
            continue
        elif stateListFull in words:
            continue         
    for found in wordLst:
        if stateListAbbr or stateListFull in found:
            matches.append(found)
    return matches
 # print(sentDict)
    # textWords = [word_tokenize(i) for i in textSents]
    #print(textWords)
    #for words in textWords:
        #print(words)
    
    # return textWords, textSents                 
def searchPosition(sents):
# assumes entry level 
# product designer (ui ux), software engineer, software developer, data analyst, project manager
# financial analyst 
    wordLst = []
    positionKeywords = ['role', 'position','job title','title','engineer','developer', 'analyst']
    jobPos = "position"
    for words in sents:
        wordLst += word_tokenize(words)
        if positionKeywords in wordLst:
            continue
        else:
            position = 'fail'
    for roles in wordLst:
        if (roles == "analyst") or (roles == "developer") or (roles == "engineer") or (roles == "designer"):
            jobPos = roles
        else:
            jobPos = "Not found"
    return jobPos'''
  # isSalary = False
'''for find in text:
    if find['JOB'] in salaryKeywords:
            isSalary = True
        else:
            count += 1 
    print(isSalary) '''

'''
def findSal(text, sentence):
    salaryKeywords = ['salary', 'rate','pay', 'compensation','wage']
    # tokenizeText = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    
    tokens = tokenizeText.tokenize(sentence)
    print(tokens)
    for words in sentence:
        wordLst += word_tokenize(words)
        if salaryKeywords in wordLst:    # wordLst = [word_tokenize(i) for i in sentence]
            print('in wordLst')
            continue
    
        for num in wordLst:
        salary = 0
        if num.isdigit():
            salary = num
            print(salary)'''
main()