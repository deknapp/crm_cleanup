import os
import sys

def get_email(first, last):
  return first + '.' + last + 'akleg.gov'

def leg_to_key(leg):
  return leg[1] + leg[0]

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


 
for key in staff_dict:
  print(key, staff_dict[key]) 

