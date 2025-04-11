from django import forms
from .models import PatientProfile, MedicalFile

# ✅ نموذج تعديل معلومات المريض | فرم اطلاعات بیمار
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['full_name', 'phone', 'address', 'notes']

# ✅ نموذج رفع ملفات طبية | فرم بارگذاری فایل پزشکی
class MedicalFileForm(forms.ModelForm):
    class Meta:
        model = MedicalFile
        fields = ['file']
