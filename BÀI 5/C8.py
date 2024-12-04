# main.py

from sequential_search import Sequential_Search

def main():
    # Nhập số lượng phần tử trong danh sách
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập các phần tử của danh sách
    dlist = []
    for i in range(n):
        element = input(f"Nhập phần tử thứ {i + 1}: ")
        dlist.append(element)
    
    # Nhập phần tử cần tìm
    item = input("Nhập phần tử cần tìm: ")
    
    # Sử dụng hàm tìm kiếm tuyến tính
    result = Sequential_Search(dlist, item)
    
    if result != -1:
        print(f"Phần tử '{item}' được tìm thấy ở vị trí {result}.")
    else:
        print(f"Phần tử '{item}' không có trong danh sách.")

if __name__ == "__main__":
    main()

