from django.contrib import admin
from .models import Doctor, Clinic, Laboratory, Imaging, Specialty, City  # ← استيراد جميع النماذج | وارد کردن همه مدل‌ها

# تسجيل النماذج في لوحة التحكم | ثبت مدل‌ها در پنل مدیریت
admin.site.register(Doctor)        # ← تسجيل نموذج الطبيب | ثبت مدل پزشک
admin.site.register(Clinic)        # ← تسجيل نموذج العيادة | ثبت مدل کلینیک
admin.site.register(Imaging)       # ← تسجيل نموذج مراكز الأشعة | ثبت مدل تصویربرداری
admin.site.register(Laboratory)    # ← تسجيل نموذج المختبر الجديد | ثبت مدل آزمایشگاه
admin.site.register(Specialty)     # ← تسجيل نموذج التخصص | ثبت مدل تخصص
admin.site.register(City)          # ← تسجيل نموذج المدينة | ثبت مدل شهر
from .models import AppointmentSlot

admin.site.register(AppointmentSlot)  # ← تسجيل المواعيد في لوحة التحكم
