def read_whole_file(filename):
    try:
        # Mở file ở chế độ đọc
        with open(filename, 'r') as file:
            # Đọc toàn bộ nội dung của file
            content = file.read()
        
        # In ra toàn bộ nội dung
        print(content)
    
    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
filename = 'c1.py'  # Thay 'example.txt' bằng tên file của bạn
read_whole_file(filename)
