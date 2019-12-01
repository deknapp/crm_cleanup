# load voter file
import contacts
import csv
import codecs

def read_voter_file(voter_file_name):
  fle = open(voter_file_name, 'r')
  return csv.DictReader(fle, quotechar='|')

def name_contact_dict(contact_dict):
  name_dict = dict()
  for key, val in contact_dict:
    k = val['First'] + val['Last']
    name_dict[k] = val
  return name_dict

def state_voices_line(voter, contact):
  # TODO: figure out best way to format this from EveryAction site
  return line 

def correct_contact_list(voter_dict, contact_dict, contact_correction_file):
  corrected_contacts = open(contact_correction_file, 'r')
  for voter in voter_dict:
    first = voter['first_name']
    last = voter['last_name']  
    key = first + last
    if key in contact_dict.keys():
      contact = contact_dict[key]
      correct_contacts.write(state_voices_line(voter, contact)) 

voter_name = '/Users/nknapp/Desktop/akpirg/voter_file.csv'
contact_name = '/Users/nknapp/Desktop/akpirg/state_voices.txt'
 
voter_dict = read_voter_file(voter_name)
contact_dict = contacts.contact_dict(contact_name)
name_contact_dict = name_contact_dict(contact_dict)

voter_list = list(voter_dict)

for voter in voter_list:
  print(voter)
  break

print(contact_dict[list(contact_dict.keys())[0]]) 
