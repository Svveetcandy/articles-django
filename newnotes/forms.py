from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, CharField, ValidationError, EmailInput


class UserRegistrationForm(ModelForm):
    password_repeat = CharField(widget=PasswordInput(attrs={
        'placeholder': 'Повторите пароль...',
        'minlength': '6',
        'maxlength': '16',
        'required': '',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_repeat')

        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Имя пользователя...',
                'maxlength': '150',
                'required': '',
            }),
            'email': EmailInput(attrs={
                'placeholder': 'Почта...',
                'required': '',
            }),
            'password': PasswordInput(attrs={
                'placeholder': 'Пароль...',
                'minlength': '6',
                'maxlength': '16',
                'required': '',
            }),
            'password_repeat': PasswordInput(attrs={
                'placeholder': 'Повторите пароль...',
                'minlength': '6',
                'maxlength': '16',
                'required': '',
            }),
        }

    def clean_password(self):
        cd = self.cleaned_data
        password_repeat = self.data['password_repeat']
        if cd['password'] != password_repeat:
            raise ValidationError('Пароли не совпадают.')
        return password_repeat

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError("Аккаунт с таким email уже существует!")
        return data

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
