import os

SUSTAINER_FILE = '/Users/nknapp/Desktop/akpirg/Sustainers_List.csv'
OUTPUT_FILE = '/Users/nknapp/Desktop/akpirg/Sustainers_List_With_Action_Codes.csv'
os.system('rm ' + OUTPUT_FILE)
read_handle = open(SUSTAINER_FILE, 'r')
write_handle = open(OUTPUT_FILE, 'w')
lines = read_handle.readlines()
sustaining_header_string = ',activist code'
sustaining_donor_string = ',sustaining donor'
write_handle.write(lines[0][:-1] + sustaining_header_string + '\n') 
for line in lines[1:]:
  if len(line) < 2:
    continue
  write_handle.write(line[:-1])
  write_handle.write(',sustaining donor')
  write_handle.write("\n")
write_handle.close()

