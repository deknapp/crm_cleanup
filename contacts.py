import os

def contact_dict(): 
  record_name = '/Users/nknapp/Desktop/akpirg/akpirg_contacts_901.txt'
  record_handle = open(record_name, 'r')
  lines = record_handle.readlines()
  header = lines[0].split(' ') 
  contact_dict = {}
  print(len(header))
  for line in lines[1:]:
    split_line = line.split('|')
    print(len(split_line))
    for i in range(len(header)-1):
      print(header[i], split_line[i])
    contact_dict[split_line[0]] = {}
    for i in range(1, len(header)-1):
      contact_dict[split_line[0]][header[i]] = split_line[i]
  return contact_dict
  

       
