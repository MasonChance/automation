import re


# define funciton/match variables with regex to be run on the files in question

def phone_re(line:str)->list:
  regi = re.compile(r'(\(\d{3}\)|(\d{3}[-.])?\d{3}[-.]\d{4}(x\d{1,5})?)')
  matches = re.findall(regi, line)
  match_list = []

  for num in matches:
    match_list.append(str(num[0]))

  return match_list

  
def email_re(line:str)->list:
  regi = r'(\w*@((\w*)|(\w*[-_]\w*))?[.]\w{3})'
  matches = re.findall(regi, line)
  match_list = []
  
  for mail in matches:
    match_list.append(str(mail[0]))
  
  return match_list
  
# define function to format phone numbers (add 206 area code if area code missing)
def phone_form(phone:str)->str:
  if len(phone) < 8:
    phone = '\n'
  if len(phone) == 8:
    phone = '206-'+ phone
  if '(' in phone:
    phone = phone[1:4] + '-' + phone[6:len(phone)]
  if 'x' in phone:
    phone = phone[0:phone.index('x')]

  return phone 



# define a function that checks for duplication to be called within the write methods prior the finish of the write method
def check_dupe(potential:str, saved:list)->bool:
  if potential in saved:
    return True
  return False
  


# define function to write the phone numbers and emails to their respective files.

def write_email(email):
  pass

def write_phone(phone):
  pass

# read input file, call the write fn for email and phone. 

# define main 
if __name__ == "__main__":
  phone_re('861-5898 1-178-383-0937 001-048-736-2919')
  email_re(' eye. danielletaylor@hotmail.com Less  character. hsoto@sharp-king.org See')
