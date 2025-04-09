from django.contrib import admin
from django.urls import path
from matab_app import views  # ربط ملف views الخاص بالتطبيق | اتصال فایل views اپلیکیشن

# ✅ لإعداد عرض الصور من مجلد media أثناء التطوير | برای نمایش تصاویر از پوشه media در زمان توسعه
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔹 لوحة تحكم Django | پنل مدیریت Django
    path('admin/', admin.site.urls),

    # 🔹 صفحات تسجيل الدخول / تسجيل / خروج | صفحات ورود / ثبت‌نام / خروج
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # 🔹 صفحات المحتوى | صفحات محتوایی
    path('clinic/', views.clinic_view, name='clinic'),  # العيادات | کلینیک‌ها
    path('details/', views.details_view, name='details'),  # تفاصيل | جزئیات
    path('doctors/', views.doctor_lists_view, name='doctor_lists'),  # الأطباء | پزشکان
    path('imaging/', views.imaging_view, name='imaging'),  # مراكز الأشعة | مراکز تصویربرداری
    path('laboratory/', views.laboratory_view, name='laboratory'),  # المختبرات | آزمایشگاه‌ها

    # ✅ صفحة الذكاء الاصطناعي لتشخيص الشامات | صفحه تشخیص خال‌های پوستی با هوش مصنوعی
    path('skin-diagnosis/', views.skin_diagnosis_view, name='skin_diagnosis'),
]

# ✅ دعم عرض الصور من MEDIA_URL أثناء تطوير المشروع | پشتیبانی از نمایش تصاویر از طریق MEDIA_URL در حالت توسعه
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
