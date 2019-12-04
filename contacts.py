import os

def contact_dict(record_name): 
  record_handle = open(record_name, 'r')
  lines = record_handle.readlines()
  header = lines[0].split(' ') 
  contact_dict = {}
  for line in lines[1:]:
    split_line = line.split('|')
    contact_dict[split_line[0]] = {}
    for i in range(1, len(header)-1):
      contact_dict[split_line[0]][header[i]] = split_line[i]
  if not contact_dict:
    print("empty contact dict")
    exit()
  return contact_dict
  
def write_contact_dict(dct, out_file, header):
  handle = open(out_file, 'w')
  handle.write(header)
  for key in dct:
    handle.write(key)
    for subkey in dct[key]:
      handle.write('|')
      handle.write(subkey)
    handle.write('\n')
     
       
