from django import forms

class new_User(forms.Form):
    user_id=forms.IntegerField()
    user_fname=forms.CharField()
    user_lname=forms.CharField()
    user_email=forms.EmailField()
    user_contact=forms.IntegerField()
    user_address=forms.CharField(widget=forms.Textarea)
