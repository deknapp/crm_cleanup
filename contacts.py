import os

def contact_dict(): 
  record_name = '~/Desktop/akpirg/akpirg_contacts_901.txt'
  record_handle = open(record_name, 'r')
  lines = record_handle.readlines()
  header = lines[0].split('|') 
  contact_dict = {}
  for line in lines[1:]:
    split_line = line.split('|')
    for i in range(len(header)):
      contact_dict[header[i]] = split_line[i]
  print(contact_dict)      
