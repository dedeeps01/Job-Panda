# the goal of this is to extract text from a PDF uploaded by the user and to tokenize the text 
import nltk
from nltk import sent_tokenize, word_tokenize
from pdfminer.high_level import extract_text 
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import levelsfyiDA
import random

textSents = []
sentDict = {}
salary = 0
AvgRoleSal = 0
def main():
    rawText = extractTextPDF()
    tokenText = tokenizeText(rawText)
    salaryExists = findSal(tokenText)
    if salaryExists:
        actualSalary = calcSal()
    else:
        print('''Can't continue, no salary data found''')
    jobPosition = findRole(tokenText)
    generateEmail = roleComparison(jobPosition, actualSalary)
    if generateEmail:
        generateNegotiation()
        
# from pdfminer documentation, extracting text into a str var
def extractTextPDF():
    jobOffOutput = StringIO()
    with open('samples/sampleOfferLetter.pdf', 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, jobOffOutput, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    raw = jobOffOutput.getvalue()
    return raw
    
def tokenizeText(text):
    global textSents
    global sentDict
    textSents = sent_tokenize(text)
    count = 1
    for i in textSents:
        sentDict[count] = word_tokenize(i) 
        count += 1
    return sentDict
   
def findSal(text):
    salaryKeywords = ['salary', 'rate','pay', 'compensation','wage']
    dictValues = [value for value in text.values()]
    isSalary = False
    for lst in dictValues:
        for j in lst:
            if j in salaryKeywords:
                isSalary = True
    return isSalary       
  
def calcSal():
    global sentDict
    global textSents
    global salary
    dictValues = [value for value in sentDict.values()]
    count = 0
    for lst in dictValues:
        count += 1
        count2 = 0
        for j in lst:
            count2 += 1 
            if j == '$':
                '''print(count)   
                print(count2)
                print(lst)'''
                salary = lst[lst.index('$')+1]  
                #print(salary)      
    return salary  

def findRole(text):
    global textSents
    global sentDict
    global role
    role = 'Not Found'
    jobKeywords = ['analyst', 'developer','scientist', 'engineer','designer']
    dictValues = [value for value in text.values()]
    for lst in dictValues:
        for j in lst:
            if j in jobKeywords:
                role = j
    # print(role)
    return role       

def roleComparison(role, sal):
    global avgRoleSal
    noCommaSal = sal.replace(",","")
    salary = float(noCommaSal)
    if (role == 'analyst') or (role == 'scientist'):
        avgDSSal = levelsfyiDA.meanBaseSalaryDS
        if salary <= avgDSSal: 
            lowerSal = True
        else:
            lowerSal = False
    elif (role == 'developer') or (role == 'engineer'):
        avgSESal = levelsfyiDA.meanBaseSalarySE
        avgRoleSal = avgSESal 

        if salary <= avgSESal:
            lowerSal = True
        else:
            lowerSal = False
    elif (role == 'designer'):
        avgPDSal = levelsfyiDA.meanBaseSalaryPD
        avgRoleSal = avgPDSal 
        if salary <= avgPDSal:
            lowerSal = True
        else: 
            lowerSal = False
    elif role == 'analyst':
        avgBASal = levelsfyiDA.meanBaseSalaryBA
        avgRoleSal = avgBASal        
        if salary <= avgBASal:
            lowerSal = True
        else:
            lowerSal = False
    else:
        print('Position not in database')
    return lowerSal

def generateNegotiation():
    emailOpt1= '''Thank you so much for offering me the position as''' '''[Company Name]. 
    I truly believe I will be a strong asset to your team, and my 10 years of experience in this industry has equipped me with the 
    skills and knowledge needed to help your company advance to the next level in [industry name].
    Before I can accept this offer, I wanted to discuss the proposed salary listed in the job offer details 
    you sent over this [time of day received]. As we had discussed during the interview, I have 
    [insert the number of years of relevant work or project experience] and also hold a [highest education degree/diploma]. 
    In my previous role, I [discuss accomplishments in relevant experiences, high impact results, any 
    accolades]. I believe I have proven my capabilities and produced noteworthy results.
    With my expertise and proven skill set, I feel that a salary around '''
    '''is appropriate, which is slightly more than the'''
    ''' you offered. Which is in line with industry standards 
    for similar roles. I am confident that my work ethic and expertise will contribute to the increased success of your organization, 
    and I am excited about the possibility of being part of [Company]. Please let me know when we can further 
    discuss the salary for this position.
    Thank you for your time, and I look forward to hearing from you soon.
    
    Sincerely,
    
    [Your Name]'''
    emailOpt2 = ''' Thank you for offering me the opportunity to work as''' 
    emailOpt3 = '''. I am really excited 
    and cannot wait to resume my responsibilities at [Company Name].
    Before I accept the offer, however, I would like to state that I was expecting something 
    between [insert a range]. The reason being [insert a valid reason such as industry standards]. I hope you will consider this request with an open mind.
    As we had discussed during the interview, I have [insert the number of years of relevant work experience] and also hold a [highest education degree/diploma]. Over the years, I have demonstrated my capabilities by producing notable results. [Talk briefly about some of the accomplishments and unique skills that you possess] Lastly, what I am asking for is in line with the industry standards.
    I can guarantee that I will be adding a lot of value to the company and am thrilled at the prospects of joining soon. Hope we can come to a mutual agreement on an acceptable salary.
        
    Thank you for your valuable time.
        
    Regards,
        
        [Your Name]'''
    # emailOpt3 = ''
    # possibleEmails = [emailOpt1, emailOpt] 
    print('''Dear Ms./Dr./Mr. [First name] [Last name], \n ''')
    print('''
    Thank you so much for offering me the position as''',role, '''[Company Name]. I truly believe I will be a strong asset to your team, and my 10 years of experience in this industry has equipped me with the skills and knowledge needed to help your company advance to the next level in [industry name]. \n
    Before I can accept this offer, I wanted to discuss the proposed salary listed in the job offer details 
    you sent over this [time of day received]. As we had discussed during the interview, I have [insert the number of years of relevant work or project experience] and also hold a [highest education degree/diploma]. In my previous role, I [discuss accomplishments in relevant experiences, high impact results, any accolades]. I believe I have proven my capabilities and produced noteworthy results. \n
    With my expertise and proven skill set, I feel that a salary around $''', avgRoleSal, '''is appropriate, which is slightly more than the''', salary, ''' you offered. Which is in line with industry standards for similar roles. I am confident that my work ethic and expertise will contribute to the increased success of your organization, and I am excited about the possibility of being part of [Company]. Please let me know when we can further discuss the salary for this position. \n
    Thank you for your time, and I look forward to hearing from you soon.
    
    Sincerely,
    
    [Your Name]''')
    
    
main()