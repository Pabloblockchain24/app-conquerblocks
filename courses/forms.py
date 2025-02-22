from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'content', 'call_link', 'created_at', 'contenido', 'course_image']  
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("El nombre debe tener al menos 10 caracteres")
        return title