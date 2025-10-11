#!/bin/bash
# 🍜 Script chạy nhanh ứng dụng Vietnamese Food Theme

echo "🍜 =========================================="
echo "   KHỞI ĐỘNG GIAO DIỆN MÓN ĂN VIỆT NAM 🇻🇳"
echo "=========================================="
echo ""

# Kiểm tra Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 chưa được cài đặt!"
    echo "Vui lòng cài đặt Python 3.8 trở lên"
    exit 1
fi

echo "✅ Python đã được cài đặt"
echo ""

# Kiểm tra và cài đặt dependencies
echo "📦 Kiểm tra dependencies..."
if [ -f "requirements.txt" ]; then
    echo "📥 Đang cài đặt packages từ requirements.txt..."
    pip install -r requirements.txt
    echo ""
else
    echo "⚠️ File requirements.txt không tìm thấy"
    echo "📥 Cài đặt packages cần thiết..."
    pip install gradio tensorflow opencv-python pillow numpy
    echo ""
fi

# Kiểm tra file chính
if [ ! -f "vietnamese_food_theme_interface.py" ]; then
    echo "❌ Không tìm thấy file vietnamese_food_theme_interface.py"
    exit 1
fi

echo "✅ Tất cả đã sẵn sàng!"
echo ""
echo "🚀 Đang khởi động ứng dụng..."
echo "🌐 Giao diện sẽ mở tại: http://localhost:7860"
echo ""
echo "⏹️  Nhấn Ctrl+C để dừng"
echo ""
echo "=========================================="
echo ""

# Chạy ứng dụng
python3 vietnamese_food_theme_interface.py

echo ""
echo "👋 Cảm ơn bạn đã sử dụng! Hẹn gặp lại!"
