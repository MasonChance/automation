from automation import __version__


import pytest
from automation.automation import phone_re, email_re, phone_form, write_phone, write_email, check_dupe



def test_version():
    assert __version__ == '0.1.0'

# @pytest.mark.skip('pending code')
def test_phone_regex(strings_with_phone_number):
    phone = ''
    match = phone_re(strings_with_phone_number)
    actual = phone
    expected = '.861-5898 lif 1-178-383-0937Mat bog001-048-736-2919'
    assert actual == expected

@pytest.mark.skip('pending code')
def test_email_regex(strings_with_email):
    email = []
    for line in strings_with_email:
        match = email_re(line)
        email.append(match)
    
    actual = email
    expected = ['danielletaylor@hotmail.com', 'hsoto@sharp-king.org']
    assert actual == expected


@pytest.mark.skip('pending code')
def test_phone_formatter_with_ext(strings_with_phone_number):
    w_ext = strings_with_phone_number[1]
    actual = phone_form(w_ext)
    expected = '1-178-383-0937'
    assert actual == expected


@pytest.mark.skip('pending code')
def test_phone_formatter_with_missing_area(strings_with_phone_number):
    w_missing = strings_with_phone_number[0]
    actual = phone_form(w_missing)
    expected = '206-861-5898'
    assert actual == expected


@pytest.mark.skip('pending code')
def test_phone_formatter_with_13_digits(strings_with_phone_number):
    w_13 = strings_with_phone_number[2]
    actual = phone_form(w_13)
    expected = '048-736-2919'
    assert actual == expected


@pytest.mark.skip('pending code')
def test_phone_writer():
    line = ''
    with open('assets/phone_numbers.txt', 'r') as f:
        line += f.readline(1)
    
    actual = line
    expected = '861-26-5898'
    assert actual == expected

@pytest.mark.skip('pending code')
def test_email_writer():
    line = ''
    with open('assets/emails.txt', 'r') as f:
        line += f.readline(1)
    
    actual = line
    expected = 'danielletaylor@hotmail.com'
    assert actual == expected


# ========== Fixtures ============

@pytest.fixture
def strings_with_phone_number():
  return ['find.861-5898Especially com +1-178-383-0937x54779Th 001-048-736-2919Much']

@pytest.fixture  
def strings_with_email():
    return [' eye. danielletaylor@hotmail.com Less  character. hsoto@sharp-king.org See']


