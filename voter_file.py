# load voter file
import contacts
import csv
import codecs

def read_voter_file(voter_file_name):
  fle = open(voter_file_name, 'r')
  return csv.DictReader(fle, quotechar='|')

voter_name = '/Users/nknapp/Desktop/akpirg/voter_file.csv'
contact_name = '/Users/nknapp/Desktop/akpirg/state_voices.txt'
 
voter_dict = read_voter_file(voter_name)
contact_dict = contacts.contact_dict(contact_name)

voter_list = list(voter_dict)

print(voter_list[1:3])
print(contact_dict)
 
