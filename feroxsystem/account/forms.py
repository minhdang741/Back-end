from django import forms

# Create login form
class LoginForm(forms.Form):
    email = forms.CharField(label='EMAIL', max_length=32)
    password = forms.CharField(label='PASSWORD', widget=forms.PasswordInput())

# Create sign up forms
class SignUpForm1(forms.Form):
    emailsignup = forms.EmailField(label='EMAIL')
    passwordsignup = forms.CharField(label='PASSWORD', widget=forms.PasswordInput(), min_length=8, help_text="Password has at least 8 characters      ")
    name = forms.CharField(label='NAME', max_length=20)
    cmnd = forms.CharField(label='CMND', max_length=12)
    referralcode = forms.CharField(label='REFERRAL CODE', max_length=12)
    birthday = forms.DateField(label='BIRTHDAY', widget=forms.DateInput(attrs={'require': 'true'}, format='%d/%m/%Y'))
    phone = forms.CharField(label='PHONE', max_length=11)
    address = forms.CharField(label='ADDRESS')
class SignUpForm2(forms.Form):
    cmndimg1 = forms.ImageField(label='CMNDIMG1', widget=forms.ClearableFileInput(attrs={'require': 'true'}))
    cmndimg2 = forms.ImageField(label='CMNDIMG2', widget=forms.ClearableFileInput(attrs={'require': 'true'}))


"""
class SignUpForm(forms.Form):
    emailsignup = forms.EmailField(label='EMAIL')
    passwordsignup = forms.CharField(label='PASSWORD', widget=forms.PasswordInput())
    name = forms.CharField(label='NAME', max_length=20)
    birthday = forms.DateField(label='BIRTHDAY', widget=forms.DateInput(attrs={'require': 'true'}, format='%d/%m/%Y'))
    referralcode = forms.CharField(label='REFERRAL CODE', max_length=12)
    cmnd = forms.CharField(label='CMND', max_length=12)
    phone = forms.CharField(label='PHONE', max_length=11)
    address = forms.CharField(label='ADDRESS')
    cmndimg1 = forms.ImageField(label='CMNDIMG1', widget=forms.ClearableFileInput(attrs={'require': 'true'}))
    cmndimg2 = forms.ImageField(label='CMNDIMG2', widget=forms.ClearableFileInput(attrs={'require': 'true'}))
"""
