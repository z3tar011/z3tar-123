from django.db import models  # ← لاستعمال نماذج Django | برای استفاده از مدل‌های جنگو
from django.contrib.auth.models import User  # ← لاستعمال المستخدمين | برای استفاده از کاربران

# -------------------------------
# 🩺 نموذج الطبيب (Doctor) | مدل پزشک
# -------------------------------
class Doctor(models.Model):
    name = models.CharField(max_length=100)  # اسم الطبيب | نام پزشک
    specialty = models.CharField(max_length=100)  # التخصص | تخصص
    email = models.EmailField()  # البريد الإلكتروني | ایمیل
    phone = models.CharField(max_length=20, blank=True)  # رقم الهاتف (اختياري) | شماره تلفن (اختیاری)
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)  # صورة الطبيب (اختياري) | تصویر پزشک

    def __str__(self):
        return self.name  # عرض اسم الطبيب | نمایش نام پزشک


# -------------------------------
# 🏥 نموذج العيادة (Clinic) | مدل کلینیک
# -------------------------------
class Clinic(models.Model):
    name = models.CharField(max_length=100)  # اسم العيادة | نام کلینیک
    bio = models.TextField(blank=True)  # وصف مختصر | توضیح کوتاه
    address = models.TextField()  # العنوان الكامل | آدرس کامل
    image = models.ImageField(upload_to='clinic_images/', blank=True, null=True)  # صورة العيادة | تصویر کلینیک

    def __str__(self):
        return self.name


# -------------------------------
# 🧪 نموذج المختبر (Laboratory) | مدل آزمایشگاه
# -------------------------------
class Laboratory(models.Model):
    name = models.CharField(max_length=100)  # اسم المختبر | نام آزمایشگاه
    bio = models.TextField(blank=True)  # وصف مختصر | توضیح کوتاه
    address = models.TextField()  # العنوان الكامل | آدرس کامل
    image = models.ImageField(upload_to='laboratory_images/', blank=True, null=True)  # صورة المختبر | تصویر آزمایشگاه

    def __str__(self):
        return self.name


# -------------------------------
# 🖼️ نموذج مركز الأشعة (Imaging) | مدل مرکز تصویربرداری
# -------------------------------
class Imaging(models.Model):
    name = models.CharField(max_length=100)  # اسم المركز | نام مرکز تصویربرداری
    bio = models.TextField(blank=True)  # وصف مختصر | توضیح کوتاه
    address = models.TextField()  # العنوان | آدرس
    image = models.ImageField(upload_to='imaging_images/', blank=True, null=True)  # صورة المركز | تصویر مرکز

    def __str__(self):
        return self.name


# -------------------------------
# 🧩 نموذج التخصص (Specialty) | مدل تخصص
# -------------------------------
class Specialty(models.Model):
    name = models.CharField(max_length=100)  # اسم التخصص | نام تخصص
    image = models.ImageField(upload_to='specialties/')  # صورة التخصص | تصویر تخصص

    def __str__(self):
        return self.name


# -------------------------------
# 🌍 نموذج المدينة (City) | مدل شهر
# -------------------------------
class City(models.Model):
    name = models.CharField(max_length=100)  # اسم المدينة | نام شهر

    def __str__(self):
        return self.name


# -------------------------------
# 🕒 نموذج الموعد الزمني (AppointmentSlot) | مدل نوبت‌دهی
# -------------------------------
class AppointmentSlot(models.Model):
    DAYS_OF_WEEK = [
        ('sat', 'شنبه'),
        ('sun', 'یک‌شنبه'),
        ('mon', 'دو‌شنبه'),
        ('tue', 'سه‌شنبه'),
        ('wed', 'چهار‌شنبه'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment_slots')  # الطبيب | پزشک
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)  # اليوم | روز
    start_time = models.TimeField()  # وقت البداية | زمان شروع
    end_time = models.TimeField()  # وقت النهاية | زمان پایان
    is_booked = models.BooleanField(default=False)  # هل محجوز؟ | آیا رزرو شده؟
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # المستخدم الذي حجز | کاربر رزروکننده

    def __str__(self):
        return f"{self.doctor.name} | {self.get_day_display()} {self.start_time} - {self.end_time}"

from django.db import models
from django.contrib.auth.models import User

# ✅ معلومات البروفايل للمريض | اطلاعات پروفایل بیمار
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ربط مباشر بالمستخدم
    full_name = models.CharField(max_length=150, blank=True)     # الاسم الكامل
    phone = models.CharField(max_length=20, blank=True)          # رقم الهاتف
    address = models.TextField(blank=True)                       # العنوان
    notes = models.TextField(blank=True)                         # ملاحظات شخصية
    national_id_code = models.CharField(max_length=10, blank=True)   # کد ملی
    insurance_number = models.CharField(max_length=20, blank=True)   # شماره بیمه

    def __str__(self):
        return self.user.username



# ✅ الملفات الطبية المرفوعة من المريض | فایل‌های پزشکی بارگذاری‌شده
class MedicalFile(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='medical_files/')  # يقبل صور و PDF
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.file.name}"
