from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name', widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Name',
            }
        )
    )
    email = forms.EmailField(
        label='E-Mail', widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your E-Mail',
            }
        )
    )
    mobile = forms.IntegerField(
        label='Mobile Number', widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Mobile No.',
            }
        )
    )
    message = forms.CharField(
        label='Message', widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Message',
            }
        )
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        )
    )
    password = forms.IntegerField(
        label='Password', widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )