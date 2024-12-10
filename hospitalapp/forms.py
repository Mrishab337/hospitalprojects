from django import forms
from .models import  Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields= ['p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date']

        widgets = {
            'booking_date': DateInput(),
        }