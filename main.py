# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]
# Hàm chuẩn hóa tên bệnh và thêm vào hồ sơ
def add_diagnosis(raw_diagnosis :str, current_list: list) -> list:
    # Cố gắng chuẩn hóa tên bệnh
    format_diagnoses = raw_diagnosis.strip().title()
    # Thêm chẩn đoán vào danh sách bệnh án
    current_list.push(format_diagnoses)
    return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Gọi hàm để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)


# phân tích lỗi
# 1 string có tính bất biến, việc sử dụng các method của string chỉ tạo ra giá trị mới chứ k làm thay đổi giá trị gốc nên cần 1 biến để hứng giá trị
# 2 sửa ở trên r ạ
# 3 khi đưa 1 chuỗi vào extend thêm vào cuối list, extend sẽ coi chuỗi đó là 1 list các kí tự riêng lẽ và push từng kí tự riêng lẽ đó vào trong list
# thay thế bằng append, hoặc nếu vẫn muốn sử dụng append thì phải bọc chuỗi vào list r mới thêm vào dc