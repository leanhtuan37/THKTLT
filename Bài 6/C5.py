class ReverseWords:
    def __init__(self, sentence):
        """
        Khởi tạo đối tượng với chuỗi cần xử lý
        :param sentence: Chuỗi cần đảo ngược từ
        """
        self.sentence = sentence

    def reverse_words(self):
        """
        Đảo ngược từng từ trong chuỗi mà không thay đổi thứ tự các từ
        :return: Chuỗi sau khi đảo ngược từng từ
        """
        # Tách chuỗi thành danh sách các từ
        words = self.sentence.split()
        
        # Đảo ngược từng từ trong danh sách
        reversed_words = [word[::-1] for word in words]
        
        # Kết hợp lại thành chuỗi và trả về kết quả
        return ' '.join(reversed_words)

# Hàm main để kiểm tra
def main():
    sentence = input("Nhập chuỗi cần đảo ngược từng từ: ")
    reverser = ReverseWords(sentence)
    result = reverser.reverse_words()
    print(f"Chuỗi sau khi đảo ngược từng từ: {result}")

if __name__ == "__main__":
    main()
