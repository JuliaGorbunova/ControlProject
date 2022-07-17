def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

def generate_string(n):
    return n*'x'

correct_email="markovna.zin@yandex.ru"
correct_pass="Qwerty1234567"
incorrect_email={'':'empty string',
                 ' ':'whitespace',
                 'murkovna.zin@yandex.ru':'uncorrect email',
                 generate_string(255):'255 symbols',
                 russian_chars():'russian',
                 chinese_chars():'chinese',
                 special_chars():'specials',
                 '123':'digit'}
incorrect_pass={'':'empty string',
                 ' ':'whitespace',
                 'Qwerty':'uncorrect pass',
                 generate_string(255):'255 symbols',
                 russian_chars():'russian',
                 chinese_chars():'chinese',
                 special_chars():'specials',
                 '123':'digit'}
