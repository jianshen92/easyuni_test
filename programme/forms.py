from django.forms import ModelForm
from programme.models import ProgramCategory, Program, Training, TrainingDate

class ProgramCategoryForm(ModelForm):
    class Meta:
        model = ProgramCategory
        fields = '__all__'

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = '__all__'

class TrainingDateForm(ModelForm):
    class Meta:
        model = TrainingDate
        fields = '__all__'