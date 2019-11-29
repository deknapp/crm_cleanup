# load voter file
import contacts
import csv

voter_file_name = '/Users/nknapp/Desktop/akpirg/voter_file.csv'

def read_voter_file(voter_file_name):
  fle = open(voter_file_name, 'r')
  contact_reader = csv.reader(fle, quotechar='|')
  for row in list(contact_reader)[:10]:
    print(row)

read_voter_file(voter_file_name)

  
