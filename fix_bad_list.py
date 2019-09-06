import os

SUSTAINER_FILE = '/Users/nknapp/Desktop/akpirg/active_fpi.csv'
OUTPUT_FILE = '/Users/nknapp/Desktop/akpirg/big_active_fpi_list.csv'
os.system('rm ' + OUTPUT_FILE)
read_handle = open(SUSTAINER_FILE, 'r')
write_handle = open(OUTPUT_FILE, 'w')
lines = read_handle.readlines()
for line in lines[1:]:  
  if len(line.split(',')) < 10:
    continue
  line = line.split(' ')[0] + ',' + line.split('"')[1] 
  print(line)
  write_handle.write(line)
   
    
