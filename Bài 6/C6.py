class StringManipulator:
    def __init__(self):
        """
        Khởi tạo đối tượng StringManipulator. 
        Không cần tham số cho phương thức khởi tạo.
        """
        self.input_string = ""  # Chuỗi người dùng nhập vào sẽ được lưu trữ ở đây
    
    def get_String(self):
        """
        Phương thức để nhận một chuỗi từ người dùng
        """
        self.input_string = input("Nhập một chuỗi: ")
    
    def print_String(self):
        """
        Phương thức để in chuỗi đã nhập ra bằng chữ in hoa.
        """
        print(self.input_string.upper())

# Hàm main để kiểm tra chương trình
def main():
    string_obj = StringManipulator()  # Tạo đối tượng StringManipulator
    string_obj.get_String()           # Nhận chuỗi từ người dùng
    string_obj.print_String()         # In chuỗi đã được chuyển thành chữ in hoa

if __name__ == "__main__":
    main()
