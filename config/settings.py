from pathlib import Path

# إعداد المسار الأساسي للمشروع | تنظیم مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات سريعة لتطوير المشروع (غير مناسبة للإنتاج) | تنظیمات سریع برای توسعه (برای تولید مناسب نیست)
SECRET_KEY = 'django-insecure-i*z#zxw#id!j)=w%zk%b%d-u9x+cq(kqz5^70ib)_u&*#p3#7%'
DEBUG = True
ALLOWED_HOSTS = []

# تعريف التطبيقات المثبتة | تعریف اپلیکیشن‌های نصب‌شده
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'matab_app',  # ← تطبيقك الخاص | اپلیکیشن شما
]

# إعدادات الوسيط (Middleware) | تنظیمات میان‌افزارها
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# المسار الرئيسي للروابط | مسیر اصلی فایل urls
ROOT_URLCONF = 'config.urls'

# إعدادات القوالب | تنظیمات قالب‌ها
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # لو أردت مستقبلاً مسار إضافي للقوالب، ضعه هنا | اگر می‌خواهید مسیر اضافی برای قالب‌ها اضافه کنید، اینجا قرار دهید
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# إعداد تطبيق WSGI | تنظیم اپلیکیشن WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# إعداد قاعدة البيانات | تنظیم پایگاه داده
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تحقق من كلمات المرور | بررسی اعتبار رمزهای عبور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# إعدادات اللغة والمنطقة الزمنية | تنظیمات زبان و منطقه زمانی
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# إعدادات الملفات الثابتة (CSS/JS...) | تنظیم فایل‌های استاتیک (مثل CSS و JS)
STATIC_URL = 'static/'

# نوع المفتاح الأساسي الافتراضي للنماذج | نوع کلید اصلی پیش‌فرض برای مدل‌ها
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔧 حل مشكلة الروابط اللي تنتهي بشرطة مائلة | حل مشکل لینک‌هایی که با / تمام می‌شوند
APPEND_SLASH = True

# لعرض الصور التي يتم رفعها من لوحة الإدارة | برای نمایش تصاویر بارگذاری‌شده از طریق پنل مدیریت
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
