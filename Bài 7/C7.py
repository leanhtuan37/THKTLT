# Đếm số dòng trong tệp văn bản

# Mở tệp văn bản với chế độ đọc ('r')
with open('ban_van.txt', 'r', encoding='utf-8') as file:
    # Đếm số dòng bằng cách sử dụng vòng lặp
    line_count = sum(1 for line in file)

# In số dòng ra màn hình
print(f"Số dòng trong tệp là: {line_count}")

