import re


# define funciton/match variables with regex to be run on the files in question

def phone_re(line):
  regi = re.compile(r'\(\\d{3}\)[-.]\\d{3}[-.]\\d{4}(x\\d{5})?')
  matches = re.findall(regi, line)
  print(matches)
  for num in matches:
    print(f'num in list of matches: {str(num)}')

  return matches
  

def email_re(line):
  pass


# define function to format phone numbers (add 206 area code if area code missing)
def phone_form(phone):
  pass


# define a function that checks for duplication to be called within the write methods prior the finish of the write method
def check_dupe(potential):
  pass


# define function to write the phone numbers and emails to their respective files.

def write_email(email):
  pass

def write_phone(phone):
  pass

# read input file, call the write fn for email and phone. 

# define main 
if __name__ == "__main__":
  phone_re('861-5898 1-178-383-0937 001-048-736-2919')