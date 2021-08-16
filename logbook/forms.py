from logbook.models import Workweek
from .models import Workweek
from django.forms import ModelForm, Textarea

class WeekUpdateForm(ModelForm):
    class Meta:
        model = Workweek
        fields = ["d" + str(i) for i in range(1, 6)]
        widgets = {"d" + str(i): Textarea(attrs={'cols': 50, 'rows': 6}) for i in range(1, 6)}

        