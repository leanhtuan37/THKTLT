def reverse_file_content(filename):
    try:
        # Mở file ở chế độ đọc
        with open(filename, 'r') as file:
            # Đọc tất cả các dòng của file
            lines = file.readlines()

        # Đảo ngược thứ tự của các dòng
        reversed_lines = lines[::-1]
        
        # Đảo ngược nội dung trong mỗi dòng và in ra
        for line in reversed_lines:
            print(line.strip()[::-1])
    
    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
filename = 'C1.py'  # Thay 'example.txt' bằng tên file của bạn
reverse_file_content(filename)
