import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from sklearn.preprocessing import LabelEncoder

# إعدادات حجم الصورة | تنظیمات اندازه تصویر
IMAGE_SIZE = 64

# تحميل نموذج الذكاء الاصطناعي | بارگذاری مدل یادگیری عمیق
model = load_model("skin_disease_model.h5")

# تجهيز تسميات الأمراض | آماده‌سازی برچسب‌های بیماری‌ها
labels = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
label_encoder = LabelEncoder()
label_encoder.fit(labels)

# قاموس التشخيص باللغة العربية والفارسية | دیکشنری اطلاعات تشخیص به عربی و فارسی
diagnosis_info = {
    'nv': 'شامة جلدية حميدة وغير خطيرة. | خال پوستی خوش‌خیم و بی‌خطر.',
    'mel': 'سرطان الجلد الخبيث. يتطلب متابعة طبية عاجلة. | ملانوم؛ یک سرطان پوستی بدخیم که نیاز به پیگیری فوری دارد.',
    'bkl': 'نمو جلدي حميد مثل التقرن الدهني. غالبًا غير ضار. | رشد خوش‌خیم پوستی مانند کراتوز سبورئیک؛ معمولاً بی‌خطر است.',
    'bcc': 'سرطان الخلايا القاعدية. أبطأ في النمو ويُعالج غالبًا بسهولة. | سرطان سلول پایه‌ای؛ رشد آهسته دارد و معمولاً قابل درمان است.',
    'akiec': 'تقرن أكتيني. قد يتحول إلى سرطان جلدي إن لم يُعالج. | کراتوز اکتینیک؛ در صورت عدم درمان ممکن است سرطانی شود.',
    'vasc': 'آفات وعائية مثل الأوردة أو الأوعية الدموية. | ضایعات عروقی مانند رگ‌ها یا عروق خونی.',
    'df': 'ورم ليفي جلدي. آمن وغير سرطاني. | فیبروم پوستی؛ بی‌خطر و غیر سرطانی است.'
}

# إعداد واجهة التطبيق | تنظیم رابط کاربری برنامه
st.title("Skin Disease Classification")
st.write("Upload a skin lesion image and the model will predict the type of disease.")

# تحميل صورة من المستخدم | بارگذاری تصویر توسط کاربر
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # عرض الصورة على الواجهة | نمایش تصویر در رابط کاربری
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # تجهيز الصورة قبل التنبؤ | آماده‌سازی تصویر قبل از پیش‌بینی
    img = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    img = img.convert("RGB")
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # تنفيذ التنبؤ باستخدام النموذج | انجام پیش‌بینی با استفاده از مدل
    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    predicted_label = label_encoder.inverse_transform([predicted_index])[0]
    confidence = np.max(prediction)

    # عرض النتائج على الشاشة | نمایش نتایج پیش‌بینی در صفحه
    st.markdown(f"### ✅ Prediction: `{predicted_label}`")
    st.markdown(f"**🔍 Diagnosis Info (Arabic & Persian):** {diagnosis_info[predicted_label]}")
    st.markdown(f"**📊 Confidence:** `{round(confidence * 100, 2)}%`")
