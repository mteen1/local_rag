
## Local RAG Agent with Llama 3.2 and Qdrant


**Llama 3.2 + Qdrant + Ollama + Phi package**

 for my *Bachelor's final project*


## ایجنت RAG لوکال با Llama 3.2 و Qdrant

این پروژه یک ایجنت هوش مصنوعی برای جستجوی دانش پزشکی از طریق فایل‌های PDF است. عامل از مدل Llama 3.2 برای پردازش زبان طبیعی و Qdrant برای مدیریت دیتابیس وکتور استفاده می‌کند.

## ویژگی‌ها
- استفاده از مدل قدرتمند Llama 3.2
- مدیریت داده‌های برداری با Qdrant
- بارگذاری دانش از فایل‌های PDF

## نحوه اجرا

1. **پیش‌نیازها**: 
   - Python 3.8+ 
   - نصب کتابخانه‌ها:
     ```bash
     pip install -r requirements.txt
     ```

2. **راه‌اندازی Qdrant**:
   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

3. **اجرای برنامه**:
   فایل `main.py` را اجرا کنید:
   ```bash
   python main.py
   ```

4. رابط کاربری در مرورگر در دسترس خواهد بود.

## منابع
- [مستندات Qdrant](https://qdrant.tech/documentation/)
- [مدل Llama](https://www.ollama.ai/)
- فایل PDF پزشکی: [لینک دانلود](https://s1cc232ef9981fc8b.jimcontent.com/download/version/1666002108/module/8094728862/name/2022%2C%20CURRENT%20Medical%20Diagnosis%20and%20Treatment-%20Original.pdf)
