class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman
        # Từ điển chứa các giá trị của ký tự La Mã
        self.roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

    def convert(self):
        """
        Chuyển đổi số La Mã thành số nguyên.
        :return: Số nguyên tương ứng với số La Mã
        """
        total = 0
        length = len(self.roman)

        # Duyệt qua từng ký tự trong chuỗi La Mã
        for i in range(length):
            current_value = self.roman_values[self.roman[i]]

            # Kiểm tra nếu ký tự tiếp theo có giá trị lớn hơn thì trừ đi
            if i + 1 < length and current_value < self.roman_values[self.roman[i + 1]]:
                total -= current_value
            else:
                total += current_value

        return total

# Hàm main để kiểm tra
def main():
    roman = input("Nhập số La Mã: ").upper()
    roman_converter = RomanToInteger(roman)
    result = roman_converter.convert()
    print(f"Số nguyên tương ứng là: {result}")

if __name__ == "__main__":
    main()
