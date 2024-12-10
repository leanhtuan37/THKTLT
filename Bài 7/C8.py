# Danh sách cần ghi vào tệp
data = ["Dòng 1: Hello, world!\n", "Dòng 2: Python là tuyệt vời!\n", "Dòng 3: Chúc bạn học tốt!\n"]

# Mở tệp văn bản để ghi ('w'), nếu tệp không tồn tại, Python sẽ tạo mới tệp
with open('output.txt', 'w', encoding='utf-8') as file:
    # Ghi từng dòng trong danh sách vào tệp
    file.writelines(data)

print("Nội dung đã được ghi vào tệp 'output.txt'")
