from django.contrib.auth.models import User
from newnotes.models import Comment
from django.forms import ModelForm, TextInput, PasswordInput, CharField, ValidationError, EmailInput

class UserRegistrationForm(ModelForm):
    password = CharField(widget=PasswordInput(attrs={
            'placeholder':'Пароль...',
            'minlength':'6',
            'maxlength':'16',
            'required':'',
        }))
    password2 = CharField(widget=PasswordInput(attrs={
            'placeholder':'Повторите пароль...',
            'minlength':'6',
            'maxlength':'16',
            'required':'',
        }))

    class Meta:
        model = User
        fields = ('username', 'email')

        widgets = {
            'username':TextInput(attrs={
                'placeholder':'Имя пользователя...',
                'maxlength':'150',
                'required':'',
                }),
            'email':EmailInput(attrs={
                'placeholder':'Почта...',
                'required':'',
                }),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_email(self):
    	data = self.cleaned_data['email']
    	if User.objects.filter(email=data).exists():
        	raise ValidationError("Аккаунт с таким email уже существует!")
    	return data

    def save(self, commit = True):
        user = super(UserRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user
