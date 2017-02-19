import string


class HasAtleastOneSymbolValidation:
    def __init__(self, symbols):
        self.__symbols = symbols

    def __call__(self, string):
        return any([ch in self.__symbols for ch in string])


class LengthValidation:
    def __init__(self, length):
        self.__length = length

    def __call__(self, string):
        return len(string) >= self.__length


class PasswordValidator:
    def __init__(self):
        self.__validators = []

    def is_valid(self, password):
        return all([v(password) for v in self.__validators])

    def add_validation(self, validator):
        self.__validators.append(validator)
        return self


SPECIAL_SYMBOLS = list(string.punctuation)


def get_validator(username):
    validator = PasswordValidator()
    validator\
        .add_validation(LengthValidation(8))\
        .add_validation(HasAtleastOneSymbolValidation(SPECIAL_SYMBOLS))\
        .add_validation(lambda password: password.count("&") == 2)\
        .add_validation(lambda password: any(x.isupper() for x in password))\
        .add_validation(lambda password: any(x.isdigit() for x in password))\
        .add_validation(lambda password: username.lower() not in password)


class StrongPasswordException(Exception):
    pass
