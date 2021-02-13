# Automation: cherry pick phone numbers and emails out of txt file

project developed to familiarize myself with automation and Regex with the `re` package. 

## Feature tasks
*copied from canvas assignment for lab:19-automation. codefellows python 401.*

- Given a document potential-contacts, find and collect all email addresses and phone numbers.
- Phone numbers may be in various formats:
    (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
    phone numbers with missing area code should presume 206
    phone numbers should be stored in xxx-yyy-zzzz format.
- Once emails and phone numbers are found they should be stored in two separate documents.
- The information should be sorted in ascending order.
- Duplicate entries are not allowed.

### Dependencies

`re`
`pytest`

### Citations
Regex pattern for Phone numbers taken from:
[]

### Pull request log 
pull requests are labeled by feature task branches.

- [set-up](https://github.com/MasonChance/automation/pull/1)
- [test-set-up](https://github.com/MasonChance/automation/pull/2)
- [phone-email-regex](https://github.com/MasonChance/automation/pull/3)