from django.forms import DateTimeInput

class XDsoftDateTimePickerInput(DateTimeInput):
    template_name = '/widgets/my_dtp.html' #date time picker widget template