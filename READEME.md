🚀

یک پروژه‌ی نمونه برای پیاده‌سازی سیستم احراز هویت (Authentication & Authorization) با استفاده از FastAPI و PostgreSQL. این پروژه قابلیت‌هایی مثل ثبت‌نام، ورود، JWT (Access/Refresh Tokens) و Protected Routes را پوشش می‌دهد و می‌تواند به‌عنوان پایه‌ای برای توسعه‌ی اپلیکیشن‌های واقعی استفاده شود.

✨ امکانات

📝 ثبت‌نام کاربر جدید (Signup) | 🔐 ورود کاربر (Login) | 🔑 تولید Access Token کوتاه‌مدت برای درخواست‌های سریع | ♻️ تولید Refresh Token بلندمدت برای مدیریت نشست (Session) | 🔒 مسیرهای محافظت‌شده (Protected Routes) | 🗄 اتصال به دیتابیس PostgreSQL (یا SQLite برای تست سریع)

🛠 تکنولوژی‌های استفاده‌شده

⚡ FastAPI — فریم‌ورک سریع و مدرن برای ساخت API | 🗄 PostgreSQL — دیتابیس قدرتمند رابطه‌ای | 🧩 SQLAlchemy — ORM برای مدیریت دیتابیس | 🐳 Docker & Docker Compose — اجرای پروژه در محیط ایزوله | 🔑 JWT (python-jose) — مدیریت توکن‌ها | 🔒 Passlib — هش کردن و امنیت رمز عبور

📂 ساختار پروژه

fastapi-auth-app/
│── app/
│ ├── main.py # فایل اصلی اجرای FastAPI
│ ├── models.py # تعریف مدل‌های دیتابیس (SQLAlchemy)
│ ├── schemas.py # تعریف مدل‌های Pydantic برای Request/Response
│ ├── crud.py # عملیات پایگاه‌داده (Create, Read, Update, Delete)
│ ├── auth.py # مدیریت JWT و امنیت
│── requirements.txt # لیست وابستگی‌های پروژه
│── docker-compose.yml # تنظیمات Docker Compose
│── Dockerfile # تنظیمات ایمیج FastAPI
│── README.md # مستندات پروژه

🚀 اجرای پروژه با Docker

برای اجرای سریع پروژه با Docker کافی است دستور زیر را اجرا کنید:
docker compose up --build
پس از اجرا، سرویس روی آدرس http://localhost:8010