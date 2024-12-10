def count_file_statistics(filename):
    try:
        # Khởi tạo các biến đếm
        num_lines = 0
        num_words = 0
        num_chars = 0

        # Mở file ở chế độ đọc
        with open(filename, 'r') as file:
            # Đọc từng dòng trong file
            for line in file:
                num_lines += 1  # Tăng số dòng lên 1 cho mỗi dòng trong file
                num_chars += len(line)  # Tính số ký tự trong dòng
                num_words += len(line.split())  # Tính số từ trong dòng

        # In ra kết quả thống kê
        print(f"Số dòng trong file: {num_lines}")
        print(f"Số từ trong file: {num_words}")
        print(f"Số ký tự trong file: {num_chars}")

    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
filename = 'exa'
