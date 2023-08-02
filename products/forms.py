from django import forms


class ClothesCreate(forms.Form):
    name = forms.CharField(max_length=255)
    type = forms.ChoiceField(choices=[('TShirt', 'TShirt'), ('Sweatshirt', 'Sweatshirt'), ('Hoody', 'Hoody')])
    size = forms.ChoiceField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')])
    color = forms.CharField(max_length=20)
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    material = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
