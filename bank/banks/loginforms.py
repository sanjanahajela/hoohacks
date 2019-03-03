from django import forms
from django.core.exceptions import ValidationError
import re
from django.utils.translation import ugettext_lazy as _
import json

class LoginForm(forms.Form):
	user_id = forms.CharField(label="User ID:", max_length=100, widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'Enter your username...'
			}
		))

	your_password = forms.CharField(label="Password:", max_length = 100, widget=forms.PasswordInput(
			attrs={
				'class':'form-control',
				'placeholder':'Enter your password...'
			}
		))

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()

		if 'user_id' not in cleaned_data:
			raise ValidationError(_('Please enter a valid name'))
		if 'your_password' not in cleaned_data:
			raise ValidationError(_('Please enter a valid password'))

		return cleaned_data