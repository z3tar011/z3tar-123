from django.db import models  # ← لاستعمال نماذج Django

# -------------------------------
# 🩺 نموذج الطبيب (Doctor)
# -------------------------------
class Doctor(models.Model):
    name = models.CharField(max_length=100)  # اسم الطبيب
    specialty = models.CharField(max_length=100)  # التخصص
    email = models.EmailField()  # البريد الإلكتروني
    phone = models.CharField(max_length=20, blank=True)  # رقم الهاتف (اختياري)
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)  # صورة الطبيب (اختياري)

    def __str__(self):
        return self.name  # عند الطباعة يظهر اسم الطبيب بدلًا من الكائن نفسه


# -------------------------------
# 🏥 نموذج العيادة (Clinic)
# -------------------------------
class Clinic(models.Model):
    name = models.CharField(max_length=100)  # اسم العيادة
    bio = models.TextField(blank=True)  # وصف مختصر عن العيادة
    address = models.TextField()  # العنوان الكامل
    image = models.ImageField(upload_to='clinic_images/', blank=True, null=True)  # صورة العيادة (اختياري)

    def __str__(self):
        return self.name  # عند الطباعة يظهر اسم العيادة


# -------------------------------
# 🧪 نموذج المختبر (Laboratory)
# -------------------------------
class Laboratory(models.Model):
    name = models.CharField(max_length=100)  # اسم المختبر
    bio = models.TextField(blank=True)  # وصف مختصر
    address = models.TextField()  # العنوان الكامل
    image = models.ImageField(upload_to='laboratory_images/', blank=True, null=True)  # صورة المختبر (اختياري)

    def __str__(self):
        return self.name  # عرض الاسم في لوحة التحكم


# -------------------------------
# 🖼️ نموذج مركز الأشعة (Imaging)
# -------------------------------
class Imaging(models.Model):
    name = models.CharField(max_length=100)  # اسم مركز الأشعة
    bio = models.TextField(blank=True)  # وصف مختصر
    address = models.TextField()  # العنوان
    image = models.ImageField(upload_to='imaging_images/', blank=True, null=True)  # صورة المركز (اختياري)

    def __str__(self):
        return self.name  # عرض اسم المركز في لوحة التحكم

from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='specialties/')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
