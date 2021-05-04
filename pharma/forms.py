from django import forms
from .models import Payment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Submit('submit', 'Proceed', css_class='button white btn-block btn-primary')
        )
