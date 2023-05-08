from django import forms
from .models import Payment


class CreatePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'ong']
        widgets = {
            'payday': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.1", "min": 0, "placeholder": "Escriba una cantidad"}),
            'concept': forms.TextInput(attrs={"placeholder": "Introduzca un concepto"}),

        }

    def __init__(self, ong, *args, **kwargs):
        super(CreatePaymentForm, self).__init__(*args, **kwargs)
        if ong.name == "ASEM":
            self.fields.pop('godfather')
            self.fields.pop('project')
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control'})


class FilterPaymentForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False, label="Búsqueda")
    min_payday_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Día de cobro después del")
    max_payday_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Día de cobro antes del")
    concept = forms.CharField(max_length=100, required=False, label="Concepto")
    ong = forms.CharField(max_length=100, required=False, label="Ong")
    paid = forms.ChoiceField(choices=[(
        '', '--Seleccione--'), (True, 'Pagado'), (False, 'No pagado')], required=False, label="Pago")
    godfather = forms.CharField(required=False, label="Padrino")
    project = forms.CharField(required=False, label="Proyecto")
    amount_min = forms.IntegerField(
        required=False, label="Importe mínimo de cantidad")
    amount_max = forms.IntegerField(
        required=False, label="Importe máximo de cantidad")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = "get"
