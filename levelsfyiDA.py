import pandas
import requests

siteData = requests.get('https://www.levels.fyi/js/salaryData.json').json()
dataFr = pandas.DataFrame(siteData)

# data filtering 
# only include salary, compensation, years of experience (4<), and years at company (3<) in order to ensure the positions are 
# entry level and therefore relevant to current students and recent gradutes
# gender excluded due to lack of data 
dataFr[['yearsofexperience','basesalary','totalyearlycompensation','yearsatcompany']] = dataFr[['yearsofexperience','basesalary','totalyearlycompensation','yearsatcompany']].apply(pandas.to_numeric)
entryLevelData = dataFr.query("title in ('Software Engineer', 'Data Scientist', 'Business Analyst', 'Product Designer') and  yearsofexperience<4 and yearsatcompany<3")
excludedData = entryLevelData.loc[:, ~entryLevelData.columns.isin(['timestamp', 'company', 'level', 'tag', 'stockgrantvalue', 'bonus', 'otherdetails', 'dmaid', 'rowNumber', 'cityid', 'gender'])]
filteredELD0 = excludedData.dropna()
filteredELD1 = filteredELD0[filteredELD0.basesalary != 0]
filteredELD2 = filteredELD1[filteredELD1.basesalary > 15]
filteredELD2.loc[filteredELD2['basesalary'] < 1000, 'basesalary'] = filteredELD2.loc[filteredELD2['basesalary'] < 1000, 'basesalary'] * 1000
filteredELD = filteredELD2[filteredELD2.basesalary > 10000]
filteredELD.to_csv('data/levelsData')

# specific job positions
dataSCi = filteredELD[filteredELD['title'].str.contains('Data Scientist')]
softEng = filteredELD[filteredELD['title'].str.contains('Software Engineer')]
BusAnl = filteredELD[filteredELD['title'].str.contains('Business Analyst')]
prodDes = filteredELD[filteredELD['title'].str.contains('Product Designer')]

# calculating averages for each position 
meanBaseSalaryDS = dataSCi['basesalary'].mean()
meanBaseSalarySE = softEng['basesalary'].mean()
meanBaseSalaryBA = BusAnl['basesalary'].mean()
meanBaseSalaryPD = prodDes['basesalary'].mean()
