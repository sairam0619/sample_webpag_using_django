from django import forms
from projapp.models import contactm
class contactmform(forms.ModelForm):
     class Meta:
          model=contactm
          fields='__all__'   
