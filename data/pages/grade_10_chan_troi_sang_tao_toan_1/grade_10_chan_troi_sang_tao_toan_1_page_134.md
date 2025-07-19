3. Dùng các kiến thức thống kê đã học để giải thích một số kết quả của bảng tính

Ví dụ:
• Tại sao MEDIAN(C4:C28) = QUARTILE.EXC(C4:C28,1)?
• Tại sao MODE(C4:C28) = 6,5?
• Tại sao IQR = QUARTILE.EXC(C4:C28,3) – QUARTILE.EXC(C4:C28,1)?
• Tại sao VAR.P(C4:C28) =[STDEV.P(C4:C28)]²?

4. Phân tích các số đặc trưng đã thu được trong bảng tính để nêu nhận xét của bạn về kết quả học tập môn Toán của lớp

1. Chia lớp theo tỉ lệ phần công làm thống kê như trên đối với điểm kiểm tra môn Toán của lớp và tổng hợp các kết quả trong một văn bản hoặc trang trình chiếu.

2. Làm tương tự với điểm kiểm tra các môn học khác của lớp.

Bạn có biết?

Nếu sử dụng hàm QUARTILE.EXC để tính tứ phân vị thứ nhất và thứ ba của mẫu số liệu trong ví dụ 4b (Chương VI – Bài 3. Các số đặc trưng đo xu thế trung tâm của mẫu số liệu):

2; 3; 10; 13; 5; 15; 5; 7

ta được kết quả $Q_1 = 4,5$ và $Q_3 = 10,75$. Kết quả này khác với kết quả ta đã tính ra. Điều này là do phần mềm Microsoft Excel đã sử dụng một dạng hiệu chỉnh của công thức tính tứ phân vị thứ nhất và thứ ba. Với mẫu ngẫu nhiên đã được sắp xếp $x_1 \leq x_2 \leq ... \leq x_n$, hàm QUARTILE.EXC tính tứ phân vị thứ nhất và thứ ba như sau:

[Bảng tính tứ phân vị Q1, Q2, Q3 theo các trường hợp n = 4k, n = 4k + 1, n = 4k + 2, n = 4k + 3]

Như vậy, hàm QUARTILE.EXC sẽ cho ra tứ phân vị thứ nhất và thứ ba giống như công thức ta đã học đối với mẫu có cỡ lẻ.

(Nguồn: https://en.wikipedia.org/wiki/Quartile)