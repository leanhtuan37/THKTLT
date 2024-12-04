import numpy as np

def main():
    # Tạo dữ liệu mẫu: ID sinh viên và chiều cao
    student_ids = np.array([101, 102, 103, 104, 105, 106])
    heights = np.array([1.70, 1.85, 1.60, 1.75, 1.80, 1.65])
    
    # Sử dụng lexsort để sắp xếp theo nhiều cột
    # Chú ý: lexsort yêu cầu các cột phải được truyền vào theo thứ tự ngược lại
    # Cột 1: chiều cao (tăng dần), cột 0: id sinh viên (tăng dần nếu chiều cao giống nhau)
    sorted_indices = np.lexsort((student_ids, heights))
    
    # Sắp xếp dữ liệu theo chỉ số đã tìm được
    sorted_student_ids = student_ids[sorted_indices]
    sorted_heights = heights[sorted_indices]
    
    # In chỉ số sắp xếp và dữ liệu đã sắp xếp
    print("Chỉ số sắp xếp theo chiều cao và ID sinh viên:")
    print(sorted_indices)
    
    print("\nDữ liệu đã sắp xếp:")
    for i in range(len(sorted_indices)):
        print(f"ID: {sorted_student_ids[i]}, Chiều cao: {sorted_heights[i]}")

if __name__ == "__main__":
    main()
