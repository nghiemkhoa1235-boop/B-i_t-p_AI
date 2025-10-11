"""
🍜 GIAO DIỆN CHỦ ĐỀ MÓN ĂN VIỆT NAM 🇻🇳
Ứng dụng AI nhận diện với theme ẩm thực Việt Nam
"""

import gradio as gr
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

# ============== CẤU HÌNH ==============
MODEL_PATH = '/content/hand_gesture_model.h5'  # Đường dẫn model của bạn

# Các class của model (thay đổi theo model thực tế)
CLASS_NAMES = ['Sinh_menh', 'Tinh_duyen', 'Tri_Tue']

# Mapping với icon món ăn Việt Nam (chỉ để trang trí theme)
FOOD_ICONS = {
    'Sinh_menh': '🍜',  # Phở
    'Tinh_duyen': '🥖',  # Bánh mì
    'Tri_Tue': '🍚'      # Cơm
}

# ============== LOAD MODEL ==============
try:
    model = load_model(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"⚠️ Warning: Could not load model - {e}")
    model = None

# ============== HÀM XỬ LÝ ==============
def preprocess_image(image):
    """Tiền xử lý ảnh"""
    if image is None:
        return None
    
    if isinstance(image, Image.Image):
        image = np.array(image)
    
    if len(image.shape) == 3:
        gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray_img = image
    
    resized_img = cv2.resize(gray_img, (100, 100))
    normalized_img = resized_img / 255.0
    img_array = normalized_img.reshape(1, 100, 100)
    
    return img_array, resized_img

def predict_image(image):
    """Hàm dự đoán chính"""
    if image is None:
        return None, "⚠️ Vui lòng tải lên ảnh", "", "🍜 Hãy chọn một ảnh để bắt đầu phân tích!"
    
    if model is None:
        return None, "❌ Model chưa được load", "0%", "Vui lòng kiểm tra đường dẫn model!"
    
    try:
        processed_img, resized_img = preprocess_image(image)
        
        if processed_img is None:
            return None, "Lỗi xử lý", "0%", "Không thể xử lý ảnh này!"
        
        predictions = model.predict(processed_img, verbose=0)
        class_idx = np.argmax(predictions[0])
        confidence = predictions[0][class_idx] * 100
        
        predicted_class = CLASS_NAMES[class_idx]
        food_icon = FOOD_ICONS.get(predicted_class, '🍲')
        
        result_text = f"{food_icon} {predicted_class}"
        confidence_text = f"{confidence:.1f}%"
        
        description = f"""
### {food_icon} Kết quả: **{predicted_class}**

📊 **Độ tin cậy:** {confidence:.2f}%

🎯 **Chi tiết phân tích:**
- Lớp dự đoán: {predicted_class}
- Chỉ số tin cậy: {confidence:.2f}%
- Trạng thái: {"✅ Rất tốt" if confidence > 80 else "⚠️ Khá tốt" if confidence > 60 else "❓ Cần xem xét"}

---
🍜 *Phân tích bằng AI với chủ đề ẩm thực Việt Nam*
        """
        
        processed_display = Image.fromarray((resized_img * 255).astype(np.uint8))
        
        return processed_display, result_text, confidence_text, description
        
    except Exception as e:
        return None, "Lỗi", "0%", f"❌ Có lỗi xảy ra: {str(e)}"

def reset_interface():
    """Reset giao diện"""
    return None, None, "", "", "🍜 **Chào mừng đến với ứng dụng AI theme ẩm thực Việt Nam!**\n\n✨ Tải lên một ảnh để bắt đầu."

# ============== CSS THEME MÓN ĂN VIỆT NAM ==============
vietnamese_food_css = """
/* Import Google Fonts - Font Việt Nam đẹp */
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;600;700;900&family=Quicksand:wght@300;500;700&display=swap');

/* === BACKGROUND THEME MÓN ĂN VIỆT NAM === */
.gradio-container {
    background: linear-gradient(135deg, 
        #FF6B6B 0%,      /* Đỏ - màu của ớt, cà chua */
        #FFD93D 25%,     /* Vàng - màu của nghệ, trứng */
        #6BCB77 50%,     /* Xanh lá - màu của rau thơm */
        #4D96FF 75%,     /* Xanh dương - màu của biển */
        #FF6B6B 100%     /* Đỏ - lặp lại */
    ) !important;
    background-size: 400% 400% !important;
    animation: vietnameseFoodGradient 20s ease infinite !important;
    min-height: 100vh !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
}

@keyframes vietnameseFoodGradient {
    0% { background-position: 0% 50%; }
    25% { background-position: 50% 100%; }
    50% { background-position: 100% 50%; }
    75% { background-position: 50% 0%; }
    100% { background-position: 0% 50%; }
}

/* === HEADER STYLE === */
h1 {
    font-family: 'Be Vietnam Pro', sans-serif !important;
    font-weight: 900 !important;
    font-size: 3.5rem !important;
    background: linear-gradient(45deg, 
        #FF6B6B,  /* Đỏ */
        #FFD93D,  /* Vàng */
        #6BCB77,  /* Xanh lá */
        #FF9A3D   /* Cam */
    ) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    text-align: center !important;
    margin: 2rem 0 !important;
    text-shadow: 0 5px 15px rgba(255, 107, 107, 0.3) !important;
    animation: titleBounce 2s ease-in-out infinite alternate !important;
    filter: drop-shadow(0 0 20px rgba(255, 215, 61, 0.5));
}

@keyframes titleBounce {
    0% { transform: translateY(0px); }
    100% { transform: translateY(-10px); }
}

/* === DECORATIVE PATTERNS === */
.gradio-container::before {
    content: '🍜 🥖 🍚 🥢 🌶️ 🥗 🍲 🥟 🦐 🐟';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    padding: 1rem;
    font-size: 2rem;
    text-align: center;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-bottom: 2px solid rgba(255, 255, 255, 0.3);
    z-index: 1000;
    animation: foodIconsFloat 3s ease-in-out infinite;
}

@keyframes foodIconsFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-5px); }
}

/* === CARD & PANEL STYLING === */
.gr-panel, .gr-box, .gr-form {
    background: rgba(255, 255, 255, 0.95) !important;
    backdrop-filter: blur(20px) !important;
    border: 3px solid rgba(255, 107, 107, 0.3) !important;
    border-radius: 25px !important;
    box-shadow: 
        0 10px 40px rgba(0, 0, 0, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.6),
        0 0 0 1px rgba(255, 215, 61, 0.1) !important;
    padding: 2rem !important;
    margin: 1.5rem !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* Decorative corner */
.gr-panel::after, .gr-box::after {
    content: '🌾';
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 2rem;
    opacity: 0.3;
    animation: rotate 5s linear infinite;
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.gr-panel:hover, .gr-box:hover {
    transform: translateY(-5px) !important;
    border-color: rgba(255, 215, 61, 0.6) !important;
    box-shadow: 
        0 15px 50px rgba(255, 107, 107, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.8) !important;
}

/* === BUTTON STYLING - VIETNAMESE FOOD THEME === */
.gr-button {
    background: linear-gradient(135deg, 
        #FF6B6B 0%, 
        #FFD93D 50%, 
        #FF6B6B 100%
    ) !important;
    background-size: 200% 200% !important;
    border: none !important;
    border-radius: 50px !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 1.2rem !important;
    padding: 18px 40px !important;
    box-shadow: 
        0 10px 30px rgba(255, 107, 107, 0.4),
        inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    position: relative !important;
    overflow: hidden !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

.gr-button::before {
    content: '🍜';
    position: absolute !important;
    left: 15px !important;
    font-size: 1.5rem !important;
    animation: buttonIconBounce 1s ease-in-out infinite !important;
}

@keyframes buttonIconBounce {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2); }
}

.gr-button::after {
    content: '' !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    width: 0 !important;
    height: 0 !important;
    border-radius: 50% !important;
    background: rgba(255, 255, 255, 0.5) !important;
    transform: translate(-50%, -50%) !important;
    transition: width 0.6s, height 0.6s !important;
}

.gr-button:hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 
        0 15px 40px rgba(255, 107, 107, 0.6),
        inset 0 1px 0 rgba(255, 255, 255, 0.5) !important;
    background-position: 100% 50% !important;
}

.gr-button:hover::after {
    width: 300px !important;
    height: 300px !important;
}

.gr-button:active {
    transform: translateY(-1px) scale(1.02) !important;
}

/* === PRIMARY BUTTON === */
.gr-button-primary {
    background: linear-gradient(135deg, 
        #FF6B6B 0%, 
        #FF9A3D 50%, 
        #FFD93D 100%
    ) !important;
    background-size: 200% 200% !important;
    animation: primaryButtonGradient 3s ease infinite !important;
}

@keyframes primaryButtonGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* === SECONDARY BUTTON === */
.gr-button-secondary {
    background: linear-gradient(135deg, 
        #6BCB77 0%, 
        #4D96FF 50%, 
        #6BCB77 100%
    ) !important;
    background-size: 200% 200% !important;
}

.gr-button-secondary::before {
    content: '🔄';
}

/* === IMAGE UPLOAD AREA === */
.gr-image {
    border: 4px dashed rgba(255, 107, 107, 0.6) !important;
    border-radius: 25px !important;
    background: linear-gradient(135deg, 
        rgba(255, 215, 61, 0.1) 0%, 
        rgba(107, 203, 119, 0.1) 100%
    ) !important;
    transition: all 0.3s ease !important;
    position: relative !important;
    min-height: 300px !important;
}

.gr-image::before {
    content: '📸 Tải lên ảnh của bạn';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 1.2rem;
    color: rgba(255, 107, 107, 0.6);
    font-weight: 600;
    pointer-events: none;
    font-family: 'Be Vietnam Pro', sans-serif;
}

.gr-image:hover {
    border-color: #FFD93D !important;
    background: linear-gradient(135deg, 
        rgba(255, 215, 61, 0.2) 0%, 
        rgba(107, 203, 119, 0.2) 100%
    ) !important;
    transform: scale(1.02) !important;
    box-shadow: 0 10px 30px rgba(255, 107, 107, 0.3) !important;
}

/* === TEXTBOX STYLING === */
.gr-textbox, .gr-text-input input {
    background: linear-gradient(135deg, 
        rgba(255, 255, 255, 0.95) 0%, 
        rgba(255, 215, 61, 0.05) 100%
    ) !important;
    border: 2px solid rgba(255, 107, 107, 0.3) !important;
    border-radius: 15px !important;
    color: #333 !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    padding: 1rem 1.5rem !important;
    transition: all 0.3s ease !important;
}

.gr-textbox:focus, .gr-text-input input:focus {
    border-color: #FFD93D !important;
    box-shadow: 0 0 20px rgba(255, 215, 61, 0.4) !important;
    transform: scale(1.02) !important;
    background: white !important;
}

/* === LABEL STYLING === */
label {
    color: #333 !important;
    font-weight: 700 !important;
    font-size: 1.2rem !important;
    text-shadow: 0 2px 4px rgba(255, 215, 61, 0.2) !important;
    margin-bottom: 0.8rem !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
    display: flex !important;
    align-items: center !important;
}

label::before {
    content: '🌶️';
    margin-right: 8px;
    font-size: 1.3rem;
    animation: labelIconSpin 3s linear infinite;
}

@keyframes labelIconSpin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* === MARKDOWN CONTENT === */
.gr-markdown {
    background: linear-gradient(135deg, 
        rgba(255, 255, 255, 0.95) 0%, 
        rgba(255, 215, 61, 0.1) 100%
    ) !important;
    border-radius: 20px !important;
    padding: 2rem !important;
    color: #333 !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
    line-height: 1.8 !important;
    border: 2px solid rgba(255, 107, 107, 0.2) !important;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1) !important;
}

.gr-markdown h1, .gr-markdown h2, .gr-markdown h3 {
    color: #FF6B6B !important;
    margin: 1.5rem 0 1rem 0 !important;
    font-weight: 700 !important;
}

.gr-markdown h1::before {
    content: '🍜 ';
}

.gr-markdown h2::before {
    content: '🥢 ';
}

.gr-markdown h3::before {
    content: '🌶️ ';
}

.gr-markdown strong {
    color: #FF9A3D !important;
    font-weight: 700 !important;
}

.gr-markdown code {
    background: rgba(255, 215, 61, 0.2) !important;
    padding: 2px 8px !important;
    border-radius: 5px !important;
    color: #FF6B6B !important;
    font-weight: 600 !important;
}

/* === ROW & COLUMN === */
.gr-row {
    gap: 2rem !important;
}

.gr-column {
    padding: 1rem !important;
}

/* === FOOTER === */
.gr-footer {
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
    border-top: 2px solid rgba(255, 107, 107, 0.3) !important;
    padding: 2rem !important;
    margin-top: 3rem !important;
    border-radius: 20px 20px 0 0 !important;
}

/* === LOADING ANIMATION === */
.gr-loading {
    border: 4px solid rgba(255, 215, 61, 0.3) !important;
    border-top: 4px solid #FF6B6B !important;
    animation: vietnameseSpinner 1s linear infinite !important;
}

@keyframes vietnameseSpinner {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* === SCROLLBAR === */
::-webkit-scrollbar {
    width: 14px;
}

::-webkit-scrollbar-track {
    background: linear-gradient(135deg, 
        rgba(255, 255, 255, 0.1) 0%, 
        rgba(255, 215, 61, 0.1) 100%
    );
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, 
        #FF6B6B 0%, 
        #FFD93D 50%, 
        #FF6B6B 100%
    );
    border-radius: 10px;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, 
        #FFD93D 0%, 
        #FF6B6B 50%, 
        #FFD93D 100%
    );
}

/* === RESPONSIVE DESIGN === */
@media (max-width: 768px) {
    h1 {
        font-size: 2.5rem !important;
    }
    
    .gr-button {
        padding: 14px 30px !important;
        font-size: 1rem !important;
    }
    
    .gr-panel, .gr-box {
        padding: 1.5rem !important;
        margin: 1rem !important;
    }
    
    .gradio-container::before {
        font-size: 1.5rem;
        padding: 0.8rem;
    }
}

@media (max-width: 480px) {
    h1 {
        font-size: 2rem !important;
    }
    
    .gr-button {
        padding: 12px 25px !important;
        font-size: 0.9rem !important;
    }
    
    .gradio-container::before {
        font-size: 1.2rem;
        padding: 0.5rem;
    }
}

/* === FADE IN ANIMATION === */
.gr-panel, .gr-box, .gr-button, .gr-image {
    animation: fadeInUp 0.8s ease-out !important;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* === VIETNAMESE PATTERN DECORATION === */
.gr-panel::before {
    content: '';
    position: absolute;
    top: -5px;
    left: -5px;
    right: -5px;
    bottom: -5px;
    background: linear-gradient(45deg,
        transparent 30%,
        rgba(255, 215, 61, 0.1) 30%,
        rgba(255, 215, 61, 0.1) 70%,
        transparent 70%
    );
    background-size: 20px 20px;
    z-index: -1;
    border-radius: 25px;
    opacity: 0.3;
}
"""

# ============== TẠO GIAO DIỆN ==============
def create_vietnamese_interface():
    with gr.Blocks(
        css=vietnamese_food_css,
        title="🍜 AI Theme Món Ăn Việt Nam",
        theme=gr.themes.Soft(
            primary_hue="red",
            secondary_hue="orange",
            neutral_hue="slate",
            font=("Be Vietnam Pro", "sans-serif")
        )
    ) as interface:
        
        # HEADER
        gr.HTML("""
        <div style="text-align: center; padding: 4rem 2rem 2rem 2rem;">
            <h1>🍜 GIAO DIỆN AI THEME MÓN ĂN VIỆT NAM 🇻🇳</h1>
            <p style="font-size: 1.5rem; color: #333; font-weight: 500; margin: 1rem 0; font-family: 'Be Vietnam Pro', sans-serif;">
                ✨ Phân tích hình ảnh với giao diện đậm chất ẩm thực Việt ✨
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; font-size: 2.5rem; margin: 1rem 0;">
                🍜 🥖 🍚 🥢 🌶️ 🥗 🍲
            </div>
            <div style="width: 150px; height: 5px; background: linear-gradient(90deg, #FF6B6B, #FFD93D, #6BCB77); margin: 1rem auto; border-radius: 3px;"></div>
        </div>
        """)
        
        # MAIN CONTENT
        with gr.Row():
            # CỘT TRÁI - INPUT
            with gr.Column(scale=1):
                gr.Markdown("### 📸 **Tải lên hình ảnh**")
                
                input_image = gr.Image(
                    type="pil",
                    label="🖼️ Chọn ảnh của bạn",
                    height=350
                )
                
                gr.Markdown("""
                💡 **Hướng dẫn:**
                - Chọn ảnh rõ ràng, đủ sáng
                - Định dạng: JPG, PNG
                - Kích thước tối đa: 10MB
                """)
                
                with gr.Row():
                    predict_btn = gr.Button(
                        "🔍 Phân tích ngay",
                        variant="primary",
                        scale=2
                    )
                    
                    reset_btn = gr.Button(
                        "🔄 Làm mới",
                        variant="secondary",
                        scale=1
                    )
            
            # CỘT PHẢI - OUTPUT
            with gr.Column(scale=1):
                gr.Markdown("### 🎯 **Kết quả phân tích**")
                
                processed_image = gr.Image(
                    label="📊 Ảnh đã xử lý",
                    height=200
                )
                
                with gr.Row():
                    prediction_output = gr.Textbox(
                        label="🏆 Kết quả dự đoán",
                        placeholder="Chưa có kết quả",
                        interactive=False,
                        scale=2
                    )
                    
                    confidence_output = gr.Textbox(
                        label="📈 Độ tin cậy",
                        placeholder="0%",
                        interactive=False,
                        scale=1
                    )
        
        # DESCRIPTION AREA
        gr.Markdown("### 📋 **Chi tiết phân tích**")
        description_output = gr.Markdown(
            value="🍜 **Chào mừng đến với ứng dụng AI theme ẩm thực Việt Nam!**\n\n✨ Tải lên một ảnh để bắt đầu phân tích."
        )
        
        # FOOTER
        gr.HTML("""
        <div style="text-align: center; margin-top: 4rem; padding: 3rem 2rem; border-top: 3px solid rgba(255, 107, 107, 0.3); background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 215, 61, 0.1) 100%); border-radius: 25px;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">
                🍜 🥖 🍚 🥢 🌶️
            </div>
            <h3 style="color: #FF6B6B; margin-bottom: 1rem; font-family: 'Be Vietnam Pro', sans-serif;">
                Giao Diện Ẩm Thực Việt Nam
            </h3>
            <p style="color: #666; font-style: italic; margin-bottom: 1rem; font-family: 'Be Vietnam Pro', sans-serif;">
                ⚠️ <strong>Lưu ý:</strong> Đây là ứng dụng AI với theme trang trí món ăn Việt Nam
            </p>
            <p style="color: #999; font-size: 0.95rem; font-family: 'Be Vietnam Pro', sans-serif;">
                Phát triển với ❤️ • TensorFlow + Gradio • 2025
            </p>
            <div style="margin-top: 1.5rem; font-size: 2rem;">
                🇻🇳 ✨ 🎉 💫 ⭐
            </div>
        </div>
        """)
        
        # EVENT HANDLERS
        predict_btn.click(
            fn=predict_image,
            inputs=[input_image],
            outputs=[processed_image, prediction_output, confidence_output, description_output]
        )
        
        reset_btn.click(
            fn=reset_interface,
            inputs=None,
            outputs=[input_image, processed_image, prediction_output, confidence_output, description_output]
        )
        
        # Auto-predict khi upload
        input_image.change(
            fn=predict_image,
            inputs=[input_image],
            outputs=[processed_image, prediction_output, confidence_output, description_output]
        )
    
    return interface

# ============== MAIN ==============
if __name__ == "__main__":
    print("="*60)
    print("🍜 KHỞI ĐỘNG GIAO DIỆN THEME MÓN ĂN VIỆT NAM 🇻🇳")
    print("="*60)
    print(f"📁 Model path: {MODEL_PATH}")
    print(f"🏷️ Classes: {CLASS_NAMES}")
    print(f"🎨 Theme: Vietnamese Food")
    print("="*60)
    
    app = create_vietnamese_interface()
    
    app.launch(
        share=True,
        debug=True,
        show_error=True,
        server_name="0.0.0.0",
        server_port=7860,
        inbrowser=True
    )
