Chú ý: Đối với số liệu rời rạc, người ta thường cho các nhóm dưới dạng $k_1 - k_2$, trong đó $k_1, k_2 \in \mathbb{N}$. Nhóm $k_1 - k_2$ được hiểu là nhóm gồm các giá trị $k_1, k_1 + 1, ..., k_2$. Khi đó, ta cần hiệu chỉnh mẫu dữ liệu ghép nhóm để đưa về dạng Bảng 3.2 trước khi thực hiện tính toán các số đặc trưng bằng cách hiệu chỉnh nhóm $k_1 - k_2$ với $k_1, k_2 \in \mathbb{N}$ thành nhóm $[k_1 - 0,5; k_2 + 0,5)$. Chẳng hạn, với dữ liệu ghép nhóm điểm thi môn Toán trong Bảng 3.3 sau khi hiệu chỉnh ta được Bảng 3.4.

Bảng 3.3
Điểm thi | 1-4 | 5-7 | 8-10
Số học sinh | 5 | 20 | 10

Bảng 3.4
Điểm thi | [0,5; 4,5) | [4,5; 7,5) | [7,5; 10]
Số học sinh | 5 | 20 | 10

Ví dụ 1. Tìm cân nặng trung bình của học sinh lớp 11D cho trong Bảng 3.5.

Bảng 3.5. Cân nặng của học sinh lớp 11D
Cân nặng | [40,5; 45,5) | [45,5; 50,5) | [50,5; 55,5) | [55,5; 60,5) | [60,5; 65,5) | [65,5; 70,5)
Số học sinh | 10 | 7 | 16 | 4 | 2 | 3

Giải

Trong mỗi khoảng cân nặng, giá trị đại diện là trung bình cộng của giá trị hai đầu mút nên ta có bảng sau:

Cân nặng (kg) | 43 | 48 | 53 | 58 | 63 | 68
Số học sinh | 10 | 7 | 16 | 4 | 2 | 3

Tổng số học sinh là $n = 42$. Cân nặng trung bình của học sinh lớp 11D là

$\bar{x} = \frac{10 \cdot 43 + 7 \cdot 48 + 16 \cdot 53 + 4 \cdot 58 + 2 \cdot 63 + 3 \cdot 68}{42} \approx 51,81(\text{kg})$.

Luyện tập 1. Tìm hiểu thời gian xem ti vi trong tuần trước (đơn vị: giờ) của một số học sinh thu được kết quả sau:

Thời gian (giờ) | [0; 5) | [5;10) | [10;15) | [15; 20) | [20; 25)
Số học sinh | 8 | 16 | 4 | 2 | 2

Tính thời gian xem ti vi trung bình trong tuần trước của các bạn học sinh này.

Ý nghĩa. Số trung bình của mẫu số liệu ghép nhóm xấp xỉ cho số trung bình của mẫu số liệu gốc, nó cho biết vị trí trung tâm của mẫu số liệu và có thể dùng để đại diện cho mẫu số liệu.

2. TRUNG VỊ CỦA MẪU SỐ LIỆU GHÉP NHÓM

HD2. Cho mẫu số liệu ghép nhóm về chiều cao của 21 cây na giống.

Chiều cao (cm) | [0; 5) | [5;10) | [10;15) | [15; 20)
Số cây | 3 | 8 | 7 | 3

Gọi $x_1, x_2, ..., x_{21}$ là chiều cao của các cây giống, đã được sắp xếp theo thứ tự tăng dần. Khi đó, $x_1, ..., x_3$ thuộc [0; 5), $x_4, ..., x_{11}$ thuộc [5; 10), ... Hỏi trung vị thuộc nhóm nào?

63