from django import forms

class EmailInput(forms.widgets.Input):
   input_type = 'email'

   def render(self, name, value, attrs=None):
       if attrs is None:
           attrs = {}
       attrs.update(dict(autocorrect='off',
                         autocapitalize='off',
                         spellcheck='false'))
       return super(EmailInput, self).render(name, value, attrs=attrs)

class ContactForm(forms.Form):
    Email  = forms.EmailField(widget=EmailInput())
    Nombre = forms.CharField(widget=forms.TextInput())
    Titulo = forms.CharField(widget=forms.TextInput())
    Texto  = forms.CharField(widget=forms.Textarea())
    