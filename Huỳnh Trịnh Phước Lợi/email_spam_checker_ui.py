import tkinter as tk
from tkinter import messagebox
from pybloom_live import BloomFilter
import hashlib

# ================================
# 1. Khởi tạo Bloom Filter
# ================================
spam_filter = BloomFilter(capacity=100000, error_rate=0.01)

# ================================
# 2. Hàm xử lý email và trích xuất đặc trưng
# ================================
def extract_features(email_text):
    features = []
    for word in email_text.split():
        features.append(word.lower())
    features.append(hashlib.sha256(email_text.encode()).hexdigest())
    return features

# ================================
# 3. Huấn luyện từ email spam mẫu
# ================================
spam_dataset = [
    "Congratulations, you've won a free iPhone! Click here to claim.",
    "You have been selected for a cash prize. Click the link now!",
    "Free money waiting for you. Limited time offer."
]

for spam_email in spam_dataset:
    features = extract_features(spam_email)
    for feature in features:
        spam_filter.add(feature)

# ================================
# 4. Hàm kiểm tra email có phải spam không
# ================================
def is_spam(email_text, threshold=0.6):
    features = extract_features(email_text)
    if not features:
        return False
    matches = sum(1 for f in features if f in spam_filter)
    return matches / len(features) >= threshold

# ================================
# 5. Giao diện người dùng bằng Tkinter
# ================================
class SpamCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Spam Checker (Bloom Filter)")

        self.label = tk.Label(root, text="Nhập nội dung email:")
        self.label.pack(pady=5)

        self.text_entry = tk.Text(root, height=10, width=60)
        self.text_entry.pack(pady=5)

        self.check_button = tk.Button(root, text="Kiểm tra Spam", command=self.check_spam)
        self.check_button.pack(pady=10)

    def check_spam(self):
        email_content = self.text_entry.get("1.0", tk.END).strip()
        if not email_content:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập nội dung email.")
            return
        result = is_spam(email_content)
        if result:
            messagebox.showinfo("Kết quả", "⚠️ Email này có thể là SPAM!")
        else:
            messagebox.showinfo("Kết quả", "✅ Email này có vẻ an toàn.")

# ================================
# 6. Chạy ứng dụng
# ================================
if __name__ == '__main__':
    root = tk.Tk()
    app = SpamCheckerApp(root)
    root.mainloop()