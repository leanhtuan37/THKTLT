import numpy as np

def main():
    # Khai báo kiểu dữ liệu cho mảng có cấu trúc
    dtype = [('name', 'U50'), ('height', 'f4'), ('class', 'U10')]
    
    # Tạo dữ liệu mẫu cho sinh viên (tên, chiều cao, lớp)
    students = np.array([
        ('Alice', 1.65, 'A'),
        ('Bob', 1.75, 'B'),
        ('Charlie', 1.80, 'A'),
        ('David', 1.70, 'B'),
        ('Eve', 1.60, 'A'),
        ('Frank', 1.85, 'B'),
        ('Grace', 1.68, 'A')
    ], dtype=dtype)
    
    print("Danh sách sinh viên ban đầu:")
    print(students)
    
    # Sắp xếp theo lớp và chiều cao (nếu lớp giống nhau)
    sorted_students = np.sort(students, order=['class', 'height'])
    
    print("\nDanh sách sinh viên sau khi sắp xếp:")
    print(sorted_students)

if __name__ == "__main__":
    main()
