from abc import ABCMeta, abstractmethod
from django.forms import Form


class BaseField(metaclass=ABCMeta):
    def is_valid(self):
        return True

    @abstractmethod
    def __str__(self):
        pass


class Input(BaseField):
    def __init__(self):
        self.

    def __str__(self):


class TextField(BaseField):
    def __init__(self):
        self.type = 'text'

    def __str__(self):
        return self


class PasswordField(BaseField):
    def __init__(self):
        self.type = 'password'

    def is_valid(self):
        return True

    def __str__(self):
        return self


class Field(BaseField, TextField, PasswordField):

    def is_valid(self):
        return True

    def __str__(self):
        return "<input />"


a = TextField()
print(a.__dict__)


class Form(metaclass=OrderdDict):
    def __init__(self, form_data=None):
        self._form_data = form_data

        for key, value in vars(self.__class__).items():
            if not callable(value) and '__' not in key:
                setattr(self, key, value)

    def __str__(self):
        tags = ['<form>']
        tags +=[str(field) for key, field
                           in self.__class__.items()
                           if not key.startswith('_')]
        tags.append('</form>')
        return "\n".join(tags)
# class LoginForm(Form):

#     def __init__(self, action, method):
#         pass

#     name = Field()
#     password = Field()

# form = LoginForm()
# # print(isinstance(form.name, Field))
# # print(isinstance(form.password, Field))

# # form_data = {
# #   'name': 'Ivo',
# #   'password': 'azsampanda'
# # }

# f = LoginForm(action='/', method='POST')
# print(str(f))
