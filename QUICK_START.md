# 🚀 HƯỚNG DẪN NHANH - VIETNAMESE FOOD THEME

## ⚡ Chạy ngay trong 3 bước

### Bước 1: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

Hoặc cài thủ công:
```bash
pip install gradio tensorflow opencv-python pillow numpy
```

### Bước 2: Chuẩn bị model

Đảm bảo bạn có file model tại:
```
/content/hand_gesture_model.h5
```

Hoặc sửa đường dẫn trong file `vietnamese_food_theme_interface.py`:
```python
MODEL_PATH = 'đường_dẫn_model_của_bạn.h5'
```

### Bước 3: Chạy ứng dụng

**Cách 1: Script tự động (Linux/Mac)**
```bash
./run_app.sh
```

**Cách 2: Chạy trực tiếp**
```bash
python vietnamese_food_theme_interface.py
```

**Cách 3: Trong Google Colab**
```python
!python vietnamese_food_theme_interface.py
```

---

## 🌐 Truy cập giao diện

Sau khi chạy, mở trình duyệt và truy cập:
- **Local**: http://localhost:7860
- **Public link**: Sẽ hiển thị trong console (nếu share=True)

---

## 📁 Cấu trúc files

```
/workspace/
├── vietnamese_food_theme_interface.py  ⭐ FILE CHÍNH
├── requirements.txt                    📦 Dependencies
├── run_app.sh                          🚀 Script chạy nhanh
├── README_VIETNAMESE_THEME.md          📖 Hướng dẫn đầy đủ
├── QUICK_START.md                      ⚡ File này
├── demo_theme.html                     🎨 Demo HTML
└── Chỉ_tay.ipynb                      📓 Notebook gốc
```

---

## 🎨 Demo thiết kế

Muốn xem trước thiết kế mà không cần chạy Python?

**Mở file:** `demo_theme.html` trong trình duyệt

*Lưu ý: File HTML chỉ demo thiết kế, không có chức năng AI*

---

## 🔧 Troubleshooting nhanh

### Lỗi: Module not found
```bash
pip install tên_module_bị_thiếu
```

### Lỗi: Model not found
Kiểm tra đường dẫn MODEL_PATH trong file .py

### Lỗi: Port đã được sử dụng
Đổi port trong file .py:
```python
server_port=7861  # Thay 7860 bằng số khác
```

### Giao diện không đẹp
- Xóa cache browser (Ctrl + F5)
- Thử browser khác

---

## 📱 Tính năng chính

✅ Upload ảnh (drag & drop hoặc click)  
✅ Tự động phân tích khi upload  
✅ Hiển thị kết quả với icon món ăn  
✅ Độ tin cậy (%)  
✅ Chi tiết phân tích  
✅ Theme màu sắc Việt Nam  
✅ Responsive design  
✅ Animation đẹp mắt  

---

## 💡 Tips

1. **Ảnh tốt nhất**: Rõ nét, đủ sáng, không bị mờ
2. **Định dạng**: JPG, PNG
3. **Kích thước**: Tối đa 10MB
4. **Browser**: Chrome hoặc Firefox để trải nghiệm tốt nhất

---

## 📞 Cần trợ giúp?

1. Đọc `README_VIETNAMESE_THEME.md` để biết chi tiết
2. Xem phần Troubleshooting trong README
3. Kiểm tra console log để xem lỗi

---

## 🎉 Chúc bạn sử dụng vui vẻ!

**Made with ❤️ and 🍜**

🇻🇳 Theme: Vietnamese Food  
⚡ Framework: Gradio + TensorFlow  
📅 Year: 2025

---

**🍜 Ăn phở đi em!** 🇻🇳
