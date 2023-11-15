from django import forms


class CalcForm(forms.Form):
    equation = forms.CharField()
    class Meta:
        fields = ["equation"]
