# functions are 2 types
# 1. Standalone functions
# 2. Method of a class
# 3. Operations (Magic methods)
from itertools import count
from string import whitespace

ph_no = '91-7993709-109'
latest_ph_no = ph_no.replace('-', '')
print(latest_ph_no)




# Transformations



price = "$29,000.00"
rec_price = price.replace("$", '').replace(',', '').replace('.00','')
print(rec_price)


# challange

# covert this messy number into a clean number
n = "+44 (176) 123-4567"
clean_messy_n = n.replace("+",'').replace(' ', '').replace('(','').replace(')','').replace("-", "")
print(clean_messy_n)




# join strings
first_name = "harish"
last_name = "chowdary"
full_name = first_name + " " + last_name
print(full_name)



first_name = "harish"
last_name = "chowdary"
full_name = first_name + "-" + last_name
print(full_name)


first_name = "harish"
last_name = "chowdary"
full_name = first_name + last_name
print(full_name)



# joiin strings
folder = "C:/users/harish/learning/python/"
file = "data.txt"

full_path = folder + file
print(full_path)

# example-2
folder = "C:/users/harish/learning/java/"
file = "src/main/java/data.txt"
full_path = folder + file
print(full_path)



# f-string 
name,age = 'sam', 27
print(f'My name is {name} and my age is {age}')

# example-2
name = 'harish'
loc = 'India'
print(f'Hello i am {name} from {loc}')



# split

str_1 = 'hari-21-bglr'
U_str = str_1.split('-')
print(U_str)

stamp = '2026-02-27 14:29'
print(stamp.split(' '))


stamp = "2026-02-27"
sep_stamp = stamp.split('-')
print(sep_stamp)

csv_file = '1234,hari,USA,1998-01-21,M'
print(csv_file.split(','))



# indexing

welcome = 'Hello'
print(welcome[4]==welcome[-1])


date = '1998-15-06'

# extract year -
print("year",date[:4])
print('year:',date[-10:-6])

print("date:",date[5:7])
print('date:',date[-5:-3])

print('month',date[8:])
print('month:',date[-2:])



# cleaning vales in list
# --Remove spaces
# whitespace cleaning

text = 'data Engineering'
nr_spaces= len(text)-len(text.strip())
is_my_code_clean = len(text) == len(text.strip())
print('nr_spaces:',nr_spaces)
print('is_my_code_clean:',is_my_code_clean)


# challenge

d = "968-Maria, ( D@t@ Engineer );; 27y  "
print(d)
print(d.replace('-', '').replace(',', '').replace('(', '').replace(')', '').replace('@', 'a').replace(' ', '').replace(';', ''))
