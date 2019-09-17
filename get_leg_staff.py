import os
import sys

def get_email(first, last):
  return first + '.' + last + 'akleg.gov'

def leg_to_key(leg):
  return leg[1] + leg[0]

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
    leg_list.append([leg_first_name, leg_last_name])
    full_staff_list = line[:-1].split('Staff:')[-1].split(',')
    leg_key = leg_last_name + leg_first_name
    staff_dict[leg_key] = []
    for staff in full_staff_list:
      first = staff.split(' ')[1] 
      last = staff.split(' ')[2] 
      staff_dict[leg_key].append([first, last])

for line in lines:
  print(dots_to_comma(line))
