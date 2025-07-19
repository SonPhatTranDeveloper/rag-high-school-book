2. Tìm hiểu một số hàm tính số liệu thống kê trong bảng tính Excel

Tên số đo đặc trưng | Nhập hàm trong Excel | Kết quả
--- | --- | ---
Số trung bình | =AVERAGE(C4:C28) | 6,66
Trung vị | =MEDIAN(C4:C28) | 6,5
Tứ phân vị thứ nhất (Q₁) | =QUARTILE.EXC(C4:C28,1) | 5
Tứ phân vị thứ hai (Q₂) | =QUARTILE.EXC(C4:C28,2) | 6,5
Tứ phân vị thứ ba (Q₃) | =QUARTILE.EXC(C4:C28,3) | 8
Mốt | =MODE(C4:C28) | 6,5
Phương sai | =VAR.P(C4:C28) | 2,8144
Độ lệch chuẩn | =STDEV.P(C4:C28) | 1,677617358
Khoảng tứ phân vị (IQR) | =I7-I5 | 3

Trong đó, C4:C28 là địa chỉ cột C từ hàng 4 đến hàng 28 của bảng tính, nơi ghi số liệu điểm kiểm tra môn Toán của lớp.

[Hình ảnh minh họa bảng tính Excel với tiêu đề "BẢNG THỐNG KÊ ĐIỂM KIỂM TRA MÔN TOÁN LỚP 10A". Bảng này bao gồm các cột: STT, Họ và Tên, Điểm KT môn Toán, Điểm, Tần số. Bên cạnh bảng chính là một bảng nhỏ hiển thị các số liệu thống kê như Số trung bình, Trung vị, Tứ phân vị, Mốt, Phương sai, Độ lệch chuẩn và Khoảng tứ phân vị.]