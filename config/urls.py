# ✅ استيراد لوحة التحكم من Django | ایمپورت پنل مدیریت Django
from django.contrib import admin

# ✅ استيراد دوال العرض (views) من التطبيق الرئيسي | ایمپورت viewها از اپلیکیشن اصلی
from django.urls import path
from matab_app import views

# ✅ دعم عرض الصور والملفات من media أثناء التطوير | پشتیبانی از نمایش تصاویر در حالت توسعه
from django.conf import settings
from django.conf.urls.static import static

# ✅ تعريف روابط الموقع | تعریف مسیرهای وب‌سایت
urlpatterns = [
    # 🔹 لوحة تحكم Django | پنل مدیریت Django
    path('admin/', admin.site.urls),

    # 🔹 الصفحة الرئيسية | صفحه اصلی
    path('', views.home, name='home'),

    # 🔹 تسجيل الدخول | ورود کاربر
    path('login/', views.login_view, name='login'),

    # 🔹 إنشاء حساب جديد | ثبت‌نام کاربر جدید
    path('register/', views.register_view, name='register'),

    # 🔹 تسجيل الخروج | خروج از حساب کاربری
    path('logout/', views.logout_view, name='logout'),

    # 🔹 صفحة العيادات | صفحه کلینیک‌ها
    path('clinic/', views.clinic_view, name='clinic'),

    # 🔹 صفحة قائمة الأطباء | صفحه لیست پزشکان
    path('doctors/', views.doctor_lists_view, name='doctor_lists'),

    # 🔹 صفحة مراكز الأشعة | صفحه مراکز تصویربرداری
    path('imaging/', views.imaging_view, name='imaging'),

    # 🔹 صفحة المختبرات | صفحه آزمایشگاه‌ها
    path('laboratory/', views.laboratory_view, name='laboratory'),

    # 🔹 صفحة الذكاء الاصطناعي لتشخيص الأمراض الجلدية | صفحه هوش مصنوعی برای تشخیص بیماری‌های پوستی
    path('skin-diagnosis/', views.skin_diagnosis_view, name='skin_diagnosis'),

    # 🔹 صفحة تفاصيل الطبيب الفردي | صفحه جزئیات یک پزشک خاص
    path('doctor/<int:doctor_id>/', views.doctor_detail_view, name='doctor_detail'),

    # 🔹 مسار تنفيذ حجز الموعد | مسیر ثبت رزرو نوبت
    path('book/', views.book_appointment_view, name='book_appointment'),

    path('profile/', views.profile_view, name='profile'),


    # ❌ تم حذف هذا السطر لأنه لا يوجد دالة اسمها details_view في views.py
    # path('details/', views.details_view, name='details'),
]

# ✅ دعم الصور المرفوعة من مجلد media أثناء التطوير | پشتیبانی از فایل‌های رسانه‌ای در حالت توسعه
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
