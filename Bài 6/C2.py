class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        """
        Khởi tạo đối tượng Hinhchunhat với chiều dài và chiều rộng
        :param chieu_dai: Chiều dài của hình chữ nhật
        :param chieu_rong: Chiều rộng của hình chữ nhật
        """
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_dien_tich(self):
        """
        Tính diện tích của hình chữ nhật
        :return: Diện tích (chiều dài * chiều rộng)
        """
        return self.chieu_dai * self.chieu_rong
    
# Hàm main để kiểm tra
def main():
    # Nhập chiều dài và chiều rộng từ người dùng
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    
    # Tạo đối tượng Hinhchunhat
    hinhchunhat = Hinhchunhat(chieu_dai, chieu_rong)
    
    # Tính diện tích và in kết quả
    dien_tich = hinhchunhat.tinh_dien_tich()
    print(f"Diện tích hình chữ nhật là: {dien_tich}")

if __name__ == "__main__":
    main()
