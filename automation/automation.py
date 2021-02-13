import re
import shutil

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
    return
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

# read input file, call the write fn for email and phone. 

# define main 
if __name__ == "__main__":
  all_phone = []
  all_email = []
  with open('assets/potential-contacts.txt', 'r') as f:
    extract_phone = phone_re(f.read())
    
    for num in extract_phone:
      check = check_dupe(num, all_phone)
      if check == False:
        num = phone_form(num)
        if num:
          all_phone.append(num if len(num) >= 12 else phone_form(num))
        else:
          continue
      else:
        continue
  
  with open('assets/potential-contacts.txt', 'r') as f:
    extract_email = email_re(f.read())
    for mail in extract_email:
      check = check_dupe(mail, all_email)
      if check == False:
        all_email.append(mail)
      else:
        continue
  
  with open('phone_numbers.txt','w+') as f:
    all_phone.sort()
    for num in all_phone:
      f.write(f'{num} \n')
  
  with open('emails.txt', 'w+') as f:
    all_email.sort()
    for mail in all_email:
      f.write(f'{mail} \n')

  shutil.copy('emails.txt', 'assets')
  shutil.copy('phone_numbers.txt', 'assets')



  