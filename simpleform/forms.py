from django import forms


# the declaration of our simple form
class SimpleForm(forms.Form):

    # define the input field
    kilometers = forms.FloatField(label='Kilometers', help_text="Enter number of kilometers to convert.")
