import os

def to_utf8(filename, newFilename, encoding_to='UTF-8'):
  with open(filename, 'r') as fr:
    with open(newFilename, 'w', encoding=encoding_to) as fw:
      for line in fr:
        fw.write(line[:-1]+'\r\n')

def contact_dict(record_name): 
 
  new_record_name = record_name + 'utf8' 
  to_utf8(record_name, new_record_name)
  record_handle = open(new_record_name, 'r')
  lines = record_handle.readlines()
  header = lines[0].split(' ') 
  contact_dict = {}
  for line in lines[1:]:
    split_line = line.split('|')
    contact_dict[split_line[0]] = {}
    for i in range(1, len(header)-1):
      contact_dict[split_line[0]][header[i]] = split_line[i]
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
     
       
