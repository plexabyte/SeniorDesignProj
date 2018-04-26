from django import forms
from .models import Layout

# from .models import post

class UploadLayoutForm(forms.Form):
    # layout_title = forms.CharField(max_length=50)
    # layout_owner = forms.CharField(max_length=50)
    # layout_image = forms.ImageField(label='Select an image', help_text='max. 1000x1000px')
    class Meta:
        model = Layout
        fields = ('layout_title', 'layout_owner', 'layout_image')
