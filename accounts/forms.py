from django.forms import Form, TextInput, PasswordInput, CharField, EmailInput


class LoginForm(Form):
    username = CharField(label='username', widget=TextInput(attrs={
        'id': 'username'
    }))
    password = CharField(label='password', widget=PasswordInput(attrs={
        'id': 'password'
    }))


class RegisterForm(Form):
    first_name = CharField(label='first_name', widget=TextInput(attrs={
        'id': 'first_name'
    }))
    last_name = CharField(label='last_name', widget=TextInput(attrs={
        'id': 'last_name'
    }))
    email = CharField(label='email', widget=EmailInput(attrs={
        'id': 'email'
    }))
    username = CharField(label='username', widget=TextInput(attrs={
        'id': 'username'
    }))
    password1 = CharField(label='password', widget=PasswordInput(attrs={
        'id': 'password'
    }))
    password2 = CharField(label='password2', widget=PasswordInput(attrs={
        'id': 'password2'
    }))
