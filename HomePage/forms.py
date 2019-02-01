from django import forms;
from .models import Contact_information_Submitted,Comment_Table;

class ContactSubmission(forms.ModelForm):
    contact_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),required=True,max_length=100);
    phone_number=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Phone'}),required=True,max_length=50);
    email = forms.EmailField(widget=forms.EmailField(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
                                   required=True, max_length=200);
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
                                   required=True, max_length=4000);
    class Meta:
        model=Contact_information_Submitted;
        fields=['contact_name','phone_no','email','message'];
"""
class ReplySubmission(forms.ModelForm):
    comment_by=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),required=True,max_length=100);
    email = forms.EmailField(widget=forms.EmailField(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                                   required=True, max_length=200);
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
                                   required=True, max_length=4000);
    class Meta:
        model=Comment_Table;
        fields=['comment_by','email','message'];

        """