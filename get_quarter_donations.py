import csv

def date_is_after(after_date, date):
  after_list = after_date.split('-')
  date_list = date.split('-')
  for i in range(0, 3):
    if after_list[i] > date_list[i]:
      return False  
  return True 

# adds up donations from last quarter for contacts
test_file = '/Users/nknapp/Desktop/akpirg/contributions_test.csv'
quarter_date = '2019-09-01'

handle = open(test_file, 'r')
donation_list  = list(csv.DictReader(handle))

dct = {}

for donation in donation_list:
  date = donation['Date Received'] 
  if not date_is_after(quarter_date, date):
    continue
  name = donation['Contact Name']
  if name in dct.keys():
    dct[name] += int(donation['Amount'])
  else:
    dct[name] = int(donation['Amount'])

print(dct)
  

