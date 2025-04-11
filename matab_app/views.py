from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Doctor, Clinic, Laboratory, Imaging, Specialty, City, AppointmentSlot, PatientProfile
from .forms import PatientProfileForm
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from sklearn.preprocessing import LabelEncoder

# ✅ الصفحة الرئيسية | صفحه اصلی
def home(request):
    specialties = Specialty.objects.all()
    cities = City.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'matab_app/project_main_page_code.html', {
        'specialties': specialties,
        'cities': cities,
        'doctors': doctors
    })

# ✅ تسجيل الدخول | ورود کاربر
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'ورود با موفقیت انجام شد.')
            return redirect('home')
        else:
            messages.error(request, 'ایمیل یا رمز عبور نادرست است.')
    return render(request, 'matab_app/sign_in_page_code.html')

# ✅ إنشاء حساب جديد | ایجاد حساب کاربری جدید
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, 'رمز عبور و تکرار آن یکسان نیستند.')
        elif User.objects.filter(username=email).exists():
            messages.error(request, 'این ایمیل قبلاً ثبت شده است.')
        else:
            User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد!')
            return redirect('login')
    return render(request, 'matab_app/sign_up_page_code.html')

# ✅ تسجيل الخروج | خروج از حساب کاربری
def logout_view(request):
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید.')
    return redirect('login')

# ✅ عرض العيادات | نمایش کلینیک‌ها
def clinic_view(request):
    clinics = Clinic.objects.all()
    return render(request, 'matab_app/clinic.html', {'clinics': clinics})

# ✅ عرض قائمة الأطباء | نمایش لیست پزشکان
def doctor_lists_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'matab_app/doctor_lists_code.html', {'doctors': doctors})

# ✅ عرض مراكز الأشعة | نمایش مراکز تصویربرداری
def imaging_view(request):
    imagings = Imaging.objects.all()
    return render(request, 'matab_app/imaging.html', {'imagings': imagings})

# ✅ عرض المختبرات | نمایش آزمایشگاه‌ها
def laboratory_view(request):
    laboratories = Laboratory.objects.all()
    return render(request, 'matab_app/laboratory.html', {'laboratories': laboratories})

# ✅ عرض تفاصيل طبيب معين | صفحه جزئیات یک پزشک
def doctor_detail_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    appointments = AppointmentSlot.objects.filter(doctor=doctor, is_booked=False).order_by('day', 'start_time')
    return render(request, 'matab_app/details.html', {
        'doctor': doctor,
        'appointments': appointments
    })

# ✅ حجز موعد | رزرو نوبت
@login_required
def book_appointment_view(request):
    if request.method == 'POST':
        slot_id = request.POST.get('slot_id')
        slot = get_object_or_404(AppointmentSlot, id=slot_id)
        already_booked = AppointmentSlot.objects.filter(user=request.user, is_booked=True).exists()
        if already_booked:
            messages.error(request, "شما قبلاً یک نوبت رزرو کرده‌اید.")
        elif slot.is_booked:
            messages.error(request, "این زمان قبلاً رزرو شده است.")
        else:
            slot.is_booked = True
            slot.user = request.user
            slot.save()
            messages.success(request, "رزرو با موفقیت انجام شد.")
        return redirect('doctor_detail', doctor_id=slot.doctor.id)
    return redirect('home')

# ✅ تحميل نموذج الذكاء الاصطناعي | بارگذاری مدل هوش مصنوعی
model = load_model(os.path.join(settings.BASE_DIR, 'matab_app/skin_ai/skin_disease_model.h5'))

labels = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
label_encoder = LabelEncoder()
label_encoder.fit(labels)

diagnosis_info = {
    'nv': 'خال عادی پوستی و بدون خطر',
    'mel': 'ملانوما، سرطان خطرناک پوست، نیاز به بررسی فوری پزشکی دارد.',
    'bkl': 'زائده‌های خوش‌خیم مانند کراتوز سبورئیک، معمولا بی‌ضرر.',
    'bcc': 'سرطان سلول‌های پایه‌ای، معمولاً به‌آرامی رشد می‌کند و قابل درمان است.',
    'akiec': 'کراتوز آکتینیک، اگر درمان نشود ممکن است سرطانی شود.',
    'vasc': 'ضایعات عروقی مانند رگ‌ها یا لکه‌های خونی.',
    'df': 'فیبروم پوستی، غیرسرطانی و بی‌خطر.'
}

# ✅ تشخيص الأمراض الجلدية | تشخیص بیماری‌های پوستی
def skin_diagnosis_view(request):
    prediction = None
    confidence = None
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        image = Image.open(image_file).resize((64, 64)).convert("RGB")
        img_array = img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)
        result = model.predict(img_array)
        predicted_index = np.argmax(result)
        predicted_label = label_encoder.inverse_transform([predicted_index])[0]
        prediction = diagnosis_info.get(predicted_label, 'تشخیص نامشخص')
        confidence = round(np.max(result) * 100, 2)
    return render(request, 'matab_app/skin_diagnosis.html', {
        'prediction': prediction,
        'confidence': confidence
    })

# ✅ صفحة البروفايل للمريض | صفحه پروفایل کاربر
@login_required
def profile_view(request):
    profile, created = PatientProfile.objects.get_or_create(user=request.user)
    appointments = AppointmentSlot.objects.filter(user=request.user, is_booked=True)

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل با موفقیت به‌روزرسانی شد.')
            return redirect('profile')
    else:
        form = PatientProfileForm(instance=profile)

    return render(request, 'matab_app/profile.html', {
        'form': form,
        'appointments': appointments
    })
