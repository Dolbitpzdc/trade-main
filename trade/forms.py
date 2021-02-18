from django import forms

USER_TYPES = (
    ('natural', 'Физ. лицо'),
    ('entity', 'Юр. лицо')
)

class UserRegistration(forms.Form):
    type = forms.ChoiceField(choices=USER_TYPES)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    password_1 = forms.CharField(widget=forms.PasswordInput())
    password_2 = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'placeholder': 'Моска, бла бла бла'})
        
    )
