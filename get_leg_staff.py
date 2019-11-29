import os
import sys

def get_email(first, last):
  return first + '.' + last + '@akleg.gov'

def leg_to_key(leg):
  return leg[0] + ',' + leg[1]

def cleanup(line):
  first_chunk = ''
  middle_chunk = ''
  if 'Sen.' in line:
    first_chunk = line.split('Sen.')[0].replace('.', ',')
    middle_chunk = 'Sen.' + line.split('Sen.')[1].split('gov')[0] + 'gov'
  elif 'Rep.' in line:
    first_chunk = line.split('Rep.')[0].replace('.', ',')
    middle_chunk = 'Rep.' + line.split('Rep.')[1].split('gov')[0] + 'gov'
  else:
    return ''
  last_chunk = line.split('gov')[-1].replace('.', ',')
  return first_chunk + middle_chunk + last_chunk

def dots_to_comma(line):
  cleaned_line = []
  for chunk in line.split('.'):
    if chunk != '':
      cleaned_line.append(chunk) 
  joined_line = '.'.join(cleaned_line) 
  return cleanup(joined_line)

def print_rep_file(leg_list):
  handle = open('/Users/nknapp/Desktop/akpirg/reps_contact.txt', 'w')
  handle.write('First,Last,Email,Phone\n')
  for leg in leg_list:
    if 'Rep.' in leg[2]:
      handle.write(','.join(leg) + '\n')

def print_sen_file(leg_list):
  handle = open('/Users/nknapp/Desktop/akpirg/sens_contact.txt', 'w')
  handle.write('First,Last,Email,Phone\n')
  for leg in leg_list:
    if 'Sen.' in leg[2]:
      handle.write(','.join(leg) + '\n')

def print_staff_file(staff_dict):
  handle = open('/Users/nknapp/Desktop/akpirg/staff_contact.txt', 'w')
  handle.write('First,Last,Email,Phone,Legislator Type,Legislator\n')
  for legislator in staff_dict:
    for staff in staff_dict[legislator]:
      line_info = []
      line_info.append(staff[0])
      line_info.append(staff[1])
      line_info.append(get_email(staff[0], staff[1]))
      line_info.append(staff[2])
      line_info.append(staff[3])
      line_info.append(legislator)
      handle.write(','.join(line_info) + '\n')

bad_file = '/Users/nknapp/Desktop/akpirg/leg_staff.txt'
handle = open(bad_file, 'r')
lines = handle.readlines()
leg_list = []
staff_dict = {}

for line in lines:
  if 'akleg' in line:
    dot_split_line = line.split('.')
    leg_name = dot_split_line[0].lower()
    leg_last_name = leg_name.split(' ')[0][:-1].title()
    leg_first_name = leg_name.split(' ')[1].title()
    full_staff_list = line[:-1].split('Staff:')[-1].split(',')
    leg_key = leg_first_name + ' ' + leg_last_name
    staff_dict[leg_key] = []
    cleaned_line = dots_to_comma(line)
    comma_split_line = cleaned_line.split(',')
    email = comma_split_line[2].strip()
    phone = comma_split_line[3].strip()  
    leg_type = ''
    if 'Sen.' in line:
      leg_type = 'Senator'
    else:
      leg_type = 'Representative' 
    for staff in full_staff_list:
      first = staff.split(' ')[1] 
      last = staff.split(' ')[2] 
      staff_dict[leg_key].append([first, last, '907-' + phone, leg_type])
    leg_list.append([leg_first_name, leg_last_name, email, '907-' + phone])

print_rep_file(leg_list)
print_sen_file(leg_list)
#print_staff_file(staff_dict)    
