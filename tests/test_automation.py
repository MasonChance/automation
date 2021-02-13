from automation import __version__


import pytest
from automation.automation import phone_re, email_re, phone_form, check_dupe



def test_version():
    assert __version__ == '0.1.0'

# @pytest.mark.skip('pending code')
def test_phone_regex(strings_with_phone_number):
    match = phone_re(strings_with_phone_number)
    actual = match
    expected = ['861-5898', '178-383-0937x54779', '048-736-2919']
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_email_regex(strings_with_email):
    match = email_re(strings_with_email)
    actual = match
    expected = ['danielletaylor@hotmail.com', 'hsoto@sharp-king.org']
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_phone_formatter_with_ext(strings_with_phone_number):
    w_ext = phone_re(strings_with_phone_number)
    actual = phone_form(w_ext[1])
    expected = '178-383-0937'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_phone_formatter_with_missing_area(strings_with_phone_number):
    w_missing = phone_re(strings_with_phone_number)
    actual = phone_form(w_missing[0])
    expected = '206-861-5898'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_phone_formatter_with_13_digits(strings_with_phone_number):
    w_13 = phone_re(strings_with_phone_number)
    actual = phone_form(w_13[2])
    expected = '048-736-2919'
    assert actual == expected

def test_check_dupe_with_phone_no_dupe(strings_with_phone_number):
    dupe = phone_re(strings_with_phone_number)
    actual = check_dupe('206-412-6226', dupe)
    expected = False
    assert actual == expected


def test_check_dupe_with_phone_yes_dupe(strings_with_phone_number):
    dupe = phone_re(strings_with_phone_number)
    actual = check_dupe(dupe[0], dupe)
    expected = True
    assert actual == expected


def test_check_dupe_with_email_no_dupe(strings_with_email):
    dupe = email_re(strings_with_email)
    actual = check_dupe('frogger@gmail.com', dupe)
    expected = False
    assert actual == expected

def test_check_dupe_with_email_yes_dupe(strings_with_email):
    dupe = email_re(strings_with_email)
    actual = check_dupe(dupe[0], dupe)
    expected = True
    assert actual == expected
    

# @pytest.mark.skip('pending code')
def test_phone_writer():
    line = ''
    with open('assets/phone_numbers.txt', 'r') as f:
        line += f.readline()
    
    actual = line
    expected = '008-445-7591 \n'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_email_writer():
    line = ''
    with open('assets/emails.txt', 'r') as f:
        line += f.readline()
    
    actual = line
    expected = 'aaron84@gmail.com \n'
    assert actual == expected


# ========== Fixtures ============

@pytest.fixture
def strings_with_phone_number():
  return 'find.861-5898Especially com +1-178-383-0937x54779Th 001-048-736-2919Much'

@pytest.fixture  
def strings_with_email():
    return ' eye. danielletaylor@hotmail.com Less  character. hsoto@sharp-king.org See'


