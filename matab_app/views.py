from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Clinic, Laboratory, Imaging

# ✅ الصفحة الرئيسية | صفحه اصلی
def home(request):
    return render(request, 'matab_app/project_main_page_code.html')

# ✅ تسجيل الدخول | ورود کاربر
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # ← استخراج الإيميل | دریافت ایمیل
        password = request.POST.get('password')  # ← استخراج كلمة المرور | دریافت رمز عبور
        user = authenticate(request, username=email, password=password)  # ← التحقق من صحة البيانات | احراز هویت کاربر
        if user:
            login(request, user)  # ← تسجيل الدخول | ورود به سیستم
            messages.success(request, 'ورود با موفقیت انجام شد.')  # ← رسالة نجاح | پیام موفقیت
            return redirect('home')
        else:
            messages.error(request, 'ایمیل یا رمز عبور نادرست است.')  # ← رسالة خطأ | پیام خطا
    return render(request, 'matab_app/sign_in_page_code.html')

# ✅ إنشاء حساب جديد | ایجاد حساب کاربری جدید
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, 'رمز عبور و تکرار آن یکسان نیستند.')  # ← كلمة السر غير متطابقة | رمزها مطابقت ندارند
        elif User.objects.filter(username=email).exists():
            messages.error(request, 'این ایمیل قبلاً ثبت شده است.')  # ← الإيميل مستخدم مسبقًا | ایمیل قبلاً استفاده شده است
        else:
            User.objects.create_user(username=email, email=email, password=password)  # ← إنشاء المستخدم | ایجاد کاربر
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد!')  # ← رسالة نجاح | پیام موفقیت
            return redirect('login')
    return render(request, 'matab_app/sign_up_page_code.html')

# ✅ تسجيل الخروج | خروج از حساب کاربری
def logout_view(request):
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید.')  # ← رسالة تأكيد الخروج | پیام خروج موفقیت‌آمیز
    return redirect('login')

# ✅ عرض العيادات من قاعدة البيانات | نمایش کلینیک‌ها از پایگاه داده
def clinic_view(request):
    clinics = Clinic.objects.all()
    return render(request, 'matab_app/clinic.html', {'clinics': clinics})

# ✅ عرض قائمة الأطباء | نمایش لیست پزشکان
def doctor_lists_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'matab_app/doctor_lists_code.html', {'doctors': doctors})

# ✅ عرض مراكز الأشعة من قاعدة البيانات | نمایش مراکز تصویربرداری
def imaging_view(request):
    imagings = Imaging.objects.all()
    return render(request, 'matab_app/imaging.html', {'imagings': imagings})

# ✅ عرض المختبرات من قاعدة البيانات | نمایش آزمایشگاه‌ها
def laboratory_view(request):
    laboratories = Laboratory.objects.all()
    return render(request, 'matab_app/laboratory.html', {'laboratories': laboratories})

# ✅ صفحة التفاصيل (غير مفعّلة حالياً) | صفحه جزئیات (فعلاً غیرفعال است)
def details_view(request):
    return render(request, 'matab_app/details.html')

# ✅ عرض صفحة الذكاء الاصطناعي وتشغيل النموذج | نمایش صفحه هوش مصنوعی و اجرای مدل
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from django.conf import settings

# تحميل النموذج المدرب من الملف | بارگذاری مدل آموزش‌دیده از فایل
model = load_model(os.path.join(settings.BASE_DIR, 'matab_app/skin_ai/skin_disease_model.h5'))

# التصنيفات التي تم تدريب النموذج عليها | برچسب‌هایی که مدل روی آن آموزش دیده
labels = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
label_encoder = LabelEncoder()
label_encoder.fit(labels)

# شرح نتائج التشخيص بالفارسية | توضیح نتایج پیش‌بینی به زبان فارسی
diagnosis_info = {
    'nv': 'خال عادی پوستی و بدون خطر',
    'mel': 'ملانوما، سرطان خطرناک پوست، نیاز به بررسی فوری پزشکی دارد.',
    'bkl': 'زائده‌های خوش‌خیم مانند کراتوز سبورئیک، معمولا بی‌ضرر.',
    'bcc': 'سرطان سلول‌های پایه‌ای، معمولاً به‌آرامی رشد می‌کند و قابل درمان است.',
    'akiec': 'کراتوز آکتینیک، اگر درمان نشود ممکن است سرطانی شود.',
    'vasc': 'ضایعات عروقی مانند رگ‌ها یا لکه‌های خونی.',
    'df': 'فیبروم پوستی، غیرسرطانی و بی‌خطر.'
}

# ✅ الدالة المسؤولة عن رفع الصورة وتشخيصها باستخدام النموذج | تابعی برای بارگذاری تصویر و تشخیص آن با استفاده از مدل
def skin_diagnosis_view(request):
    prediction = None
    confidence = None

    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        image = Image.open(image_file).resize((64, 64)).convert("RGB")  # ← تحويل إلى RGB | تبدیل به RGB
        img_array = img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)

        result = model.predict(img_array)
        predicted_index = np.argmax(result)
        predicted_label = label_encoder.inverse_transform([predicted_index])[0]
        prediction = diagnosis_info.get(predicted_label, 'تشخیص نامشخص')  # ← إذا لم توجد النتيجة | اگر نتیجه یافت نشد
        confidence = round(np.max(result) * 100, 2)

    return render(request, 'matab_app/skin_diagnosis.html', {
        'prediction': prediction,
        'confidence': confidence
    })

# ✅ الصفحة الرئيسية بعد ربط التخصصات والمدن من قاعدة البيانات | صفحه اصلی با اتصال تخصص‌ها و شهرها از پایگاه داده
from .models import Specialty, City

def home(request):
    specialties = Specialty.objects.all()
    cities = City.objects.all()
    return render(request, 'matab_app/project_main_page_code.html', {
        'specialties': specialties,
        'cities': cities
    })
