# ObesityRisk_UI

Đây là một ứng dụng giao diện người dùng (UI) cho dự án Obesity Risk, được xây dựng bằng Django.

## Mục đích
Ứng dụng này cung cấp giao diện người dùng để dự đoán nguy cơ béo phì dựa trên các đặc điểm như thói quen ăn uống, hoạt động thể chất, và các yếu tố cá nhân khác.

## Yêu cầu hệ thống
- Python 3.8 hoặc cao hơn
- Django 4.x
- Các thư viện Python khác được liệt kê trong `requirements.txt`

## Cài đặt
1. **Cloning repository:**
```bash
    git clone https://github.com/ddkhoa2605/ObesityRisk_UI.git
    cd ObesityRisk_UI
```

2. **Tạo và kích hoạt môi trường ảo (khuyến khích):**
```bash
    python -m venv env
    source env/bin/activate      # Trên Linux/MacOS
    .\env\Scripts\activate      # Trên Windows
```

3. **Cài đặt các thư viện cần thiết:**
```bash
    pip install -r requirements.txt
```

4. **Chạy các lệnh migrate để tạo cơ sở dữ liệu:**
```bash
    python manage.py makemigrations
    python manage.py migrate
```

## Chạy ứng dụng
```bash
    python manage.py runserver
```
Sau khi chạy lệnh trên, truy cập vào trình duyệt tại địa chỉ: `http://127.0.0.1:8000/`

## Cấu trúc thư mục chính
```
ObesityRisk_UI/
│
├── manage.py
├── obesity_app/                # Ứng dụng chính của Django
├── static/                     # Các file CSS, JavaScript và hình ảnh
├── templates/                  # Các file HTML
├── requirements.txt            # Các thư viện cần cài đặt
├── db.sqlite3                  # Cơ sở dữ liệu SQLite (tạo sau khi migrate)
```

## Ghi chú
- Hãy đảm bảo rằng bạn đã kích hoạt môi trường ảo trước khi cài đặt các thư viện.
- Nếu có lỗi khi chạy lệnh `migrate`, hãy kiểm tra file `settings.py` trong ứng dụng Django.

## Đóng góp
Mọi đóng góp đều được hoan nghênh. Hãy tạo một nhánh (`git checkout -b feature/YourFeature`), commit các thay đổi (`git commit -m 'Thêm tính năng mới'`), push nhánh của bạn (`git push origin feature/YourFeature`) và tạo một Pull Request.

