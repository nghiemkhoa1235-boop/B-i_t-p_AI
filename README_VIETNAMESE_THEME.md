# 🍜 GIAO DIỆN AI THEME MÓN ĂN VIỆT NAM 🇻🇳

## 📖 Giới thiệu

Đây là giao diện AI với **chủ đề ẩm thực Việt Nam** được thiết kế đẹp mắt và hiện đại, sử dụng:
- 🎨 Màu sắc đặc trưng: Đỏ (ớt), Vàng (nghệ), Xanh lá (rau thơm)
- 🍜 Icon và biểu tượng món ăn Việt: Phở, bánh mì, cơm, nước mắm, v.v.
- ✨ Hiệu ứng animation mượt mà
- 📱 Responsive design - tương thích mọi thiết bị

---

## 🚀 Cài đặt

### 1. Cài đặt thư viện cần thiết

```bash
pip install gradio tensorflow opencv-python pillow numpy
```

### 2. Chuẩn bị model

Đảm bảo bạn đã có model được train sẵn tại:
```
/content/hand_gesture_model.h5
```

Hoặc thay đổi đường dẫn trong file `vietnamese_food_theme_interface.py`:
```python
MODEL_PATH = 'đường_dẫn_tới_model_của_bạn.h5'
```

---

## 💻 Cách chạy

### Chạy trong Google Colab

```python
# Upload file vietnamese_food_theme_interface.py lên Colab
# Sau đó chạy:
!python vietnamese_food_theme_interface.py
```

### Chạy trên máy local

```bash
python vietnamese_food_theme_interface.py
```

Giao diện sẽ tự động mở tại: `http://localhost:7860`

---

## 🎨 Tính năng giao diện

### ✨ Theme màu sắc
- **Đỏ (#FF6B6B)**: Màu của ớt, cà chua
- **Vàng (#FFD93D)**: Màu của nghệ, trứng
- **Xanh lá (#6BCB77)**: Màu của rau thơm, ngò gai
- **Cam (#FF9A3D)**: Màu của nước mắm, tôm

### 🍜 Icon món ăn
- 🍜 Phở
- 🥖 Bánh mì
- 🍚 Cơm
- 🥢 Đũa
- 🌶️ Ớt
- 🥗 Gỏi cuốn
- 🍲 Canh
- 🥟 Bánh bao

### 💫 Hiệu ứng đặc biệt
1. **Gradient động**: Background chuyển màu mượt mà
2. **Button animation**: Hiệu ứng sóng khi click
3. **Hover effects**: Transform khi di chuột
4. **Loading animation**: Spinner theo theme Việt Nam
5. **Icon animations**: Xoay, nhảy, float

---

## 📱 Responsive Design

Giao diện tự động điều chỉnh cho:
- 💻 Desktop (> 1024px)
- 📱 Tablet (768px - 1024px)
- 📱 Mobile (< 768px)

---

## 🎯 Cách sử dụng

1. **Tải ảnh lên**: Click vào ô "Chọn ảnh của bạn" hoặc kéo thả
2. **Phân tích**: Click button "🔍 Phân tích ngay"
3. **Xem kết quả**: 
   - Ảnh đã xử lý (grayscale 100x100)
   - Kết quả dự đoán với icon món ăn
   - Độ tin cậy (%)
   - Chi tiết phân tích
4. **Làm mới**: Click "🔄 Làm mới" để reset

---

## 🔧 Tùy chỉnh

### Thay đổi màu sắc chính

Trong file `vietnamese_food_theme_interface.py`, tìm và sửa:

```python
# Màu gradient chính
background: linear-gradient(135deg, 
    #FF6B6B 0%,      # Đỏ - Thay đổi tại đây
    #FFD93D 25%,     # Vàng
    #6BCB77 50%,     # Xanh lá
    #4D96FF 75%,     # Xanh dương
    #FF6B6B 100%
)
```

### Thay đổi icon món ăn

```python
FOOD_ICONS = {
    'Sinh_menh': '🍜',  # Thay đổi icon tại đây
    'Tinh_duyen': '🥖',
    'Tri_Tue': '🍚'
}
```

### Thay đổi font chữ

```python
@import url('https://fonts.googleapis.com/css2?family=Ten_Font_Ban_Muon');

font-family: 'Ten_Font_Ban_Muon', sans-serif !important;
```

---

## 📂 Cấu trúc file

```
/workspace/
├── vietnamese_food_theme_interface.py  # File chính
├── README_VIETNAMESE_THEME.md          # File hướng dẫn này
├── demo_theme.html                     # Demo HTML thuần
└── hand_gesture_model.h5               # Model AI (nếu có)
```

---

## 🐛 Troubleshooting

### Lỗi: Model not found
```
⚠️ Warning: Could not load model
```
**Giải pháp**: Kiểm tra đường dẫn MODEL_PATH trong file

### Lỗi: Gradio không cài đặt
```bash
pip install --upgrade gradio
```

### Lỗi: TensorFlow không tương thích
```bash
pip install tensorflow==2.15.0
```

### Giao diện không hiển thị đúng
- Xóa cache browser (Ctrl + F5)
- Thử browser khác (Chrome, Firefox)
- Kiểm tra console để xem lỗi CSS

---

## 🌟 Demo Features

### 1. Upload ảnh
- Drag & drop
- Click để chọn
- Auto-preview

### 2. Phân tích
- Tiền xử lý ảnh tự động
- Dự đoán real-time
- Hiển thị kết quả đẹp mắt

### 3. Kết quả
- Icon động theo class
- Màu sắc theo độ tin cậy
- Chi tiết đầy đủ

---

## 📊 Performance

- ⚡ **Tốc độ**: < 1s cho mỗi prediction
- 💾 **RAM**: ~500MB
- 🖥️ **GPU**: Không bắt buộc (chạy được trên CPU)
- 📶 **Network**: Không cần internet sau khi load xong

---

## 🎓 Học thêm

### Gradio
- Docs: https://gradio.app/docs
- Gallery: https://gradio.app/demos

### TensorFlow
- Guide: https://tensorflow.org/guide
- Tutorials: https://tensorflow.org/tutorials

### CSS Animation
- MDN: https://developer.mozilla.org/en-US/docs/Web/CSS/animation
- CSS Tricks: https://css-tricks.com/almanac/properties/a/animation/

---

## 🤝 Đóng góp

Nếu bạn muốn cải thiện giao diện:
1. Fork repository
2. Tạo branch mới
3. Commit changes
4. Push và tạo Pull Request

---

## 📄 License

MIT License - Free to use and modify

---

## 👨‍💻 Author

Phát triển với ❤️ và 🍜 

**Theme**: Vietnamese Food  
**Framework**: Gradio + TensorFlow  
**Year**: 2025

---

## 🆘 Support

Nếu gặp vấn đề, vui lòng:
1. Kiểm tra phần Troubleshooting
2. Xem log error
3. Google lỗi cụ thể
4. Hỏi trên StackOverflow với tag `gradio` và `tensorflow`

---

## 🎉 Cảm ơn

Cảm ơn bạn đã sử dụng giao diện này!

**Chúc bạn code vui vẻ!** 🍜🇻🇳✨

---

## 📸 Screenshots

*(Chạy ứng dụng để xem giao diện thực tế)*

### Desktop View
- Header với gradient động
- 2 cột: Input và Output
- Footer đẹp mắt

### Mobile View
- Stack layout
- Touch-friendly buttons
- Responsive images

---

## 🔮 Future Updates

- [ ] Thêm dark mode
- [ ] Thêm nhiều theme khác (Bánh mì, Phở, Cà phê...)
- [ ] Tích hợp API
- [ ] Multi-language support
- [ ] Export results
- [ ] History tracking

---

**🍜 Chúc bạn ngon miệng và code vui vẻ! 🇻🇳**
