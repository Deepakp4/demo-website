from django import forms

class user(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    contact=forms.IntegerField()
    password=forms.CharField()
    
    
 
        
    