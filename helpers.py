import random

class GenenateData:
    def __init__(self):
        self.digit = '1234567890'
        self.lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.punctuation = '#$%&*+-=?@^_'
        self.name = ['roman', 'anton', 'ivan', 'sergey', 'maxim', 'egor', 'evgeny', 'lubov', 'anna', 'kristy', 'lena',
                'irina', 'alsu', 'olesya', 'zhenya', 'misha', 'vlad']
        self.punctuation_email = '-._'
        self.chars_password = self.digit + self.lowercase_letters + self.uppercase_letters + self.punctuation
        self.chars_email = self.digit + self.lowercase_letters + self.uppercase_letters
        self.domen = '@ya.ru'
        self.rand = random.randint(6, 12)
        self.rand_error = random.randint(3, 5)

    def generate_email(self):
        email = ''
        for j in range(self.rand):
            email += random.choice(self.chars_email)
        return random.choice(self.name) + random.choice(self.punctuation_email) + email + self.domen

    def generate_right_password(self):
        password = ''
        for j in range(self.rand):
            password += random.choice(self.chars_password)
        return password

    def generate_error_password(self):
        password = ''
        for j in range(self.rand_error):
            password += random.choice(self.chars_password)
        return password