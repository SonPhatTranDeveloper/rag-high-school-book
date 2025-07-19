Cho mẫu số liệu ghép nhóm như trong Bảng 3.2.

Để tính trung vị của mẫu số liệu ghép nhóm, ta làm như sau:
Bước 1. Xác định nhóm chứa trung vị. Giả sử đó là nhóm thứ p: [a_p; a_p+1).

Bước 2. Trung vị là $M_e = a_p + \frac{\frac{n}{2} - (m_1 + ... + m_{p-1})}{m_p} \cdot (a_{p+1} - a_p)$,

trong đó n là cỡ mẫu, m_p là tần số nhóm p. Với p = 1, ta quy ước m_1 + ... + m_p-1 = 0.

Ví dụ 2. Thời gian (phút) truy cập Internet mỗi buổi tối của một số học sinh được cho trong bảng sau:

Thời gian (phút) | [9,5;12,5) | [12,5; 15,5) | [15,5; 18,5) | [18,5; 21,5) | [21,5; 24,5)
Số học sinh      |     3      |     12      |     15      |     24      |     2

Tính trung vị của mẫu số liệu ghép nhóm này.

Giải
Cỡ mẫu là n = 3 + 12 + 15 + 24 + 2 = 56.
Gọi x_1, ..., x_56 là thời gian vào Internet của 56 học sinh và giả sử dãy này đã được sắp xếp

theo thứ tự tăng dần. Khi đó, trung vị là $\frac{x_{28} + x_{29}}{2}$. Do 2 giá trị x_28, x_29 thuộc nhóm [15,5; 18,5)

nên nhóm này chứa trung vị. Do đó, p = 3; a_3 = 15,5; m_3 = 15; m_1 + m_2 = 3 + 12 = 15; a_4 - a_3 = 3
và ta có

$M_e = 15,5 + \frac{\frac{56}{2} - 15}{15} \cdot 3 = 18,1$.

Luyện tập 2. Ghi lại tốc độ bóng trong 200 lần giao bóng của một vận động viên môn quần vợt cho kết quả như bảng bên.
Tính trung vị của mẫu số liệu ghép nhóm này.

Tốc độ v (km/h) | Số lần
150 ≤ v < 155   |   18
155 ≤ v < 160   |   28
160 ≤ v < 165   |   35
165 ≤ v < 170   |   43
170 ≤ v < 175   |   41
175 ≤ v < 180   |   35

Ý nghĩa. Trung vị của mẫu số liệu ghép nhóm xấp xỉ cho trung vị của mẫu số liệu gốc, nó chia mẫu số liệu thành hai phần, mỗi phần chứa 50% giá trị.

3. TỬ PHÂN VỊ CỦA MẪU SỐ LIỆU GHÉP NHÓM

HĐ3. Với mẫu số liệu ghép nhóm cho trong HĐ2, hãy cho biết tứ phân vị thứ nhất Q_1 và tứ phân vị thứ ba Q_3 thuộc nhóm nào.

Cho mẫu số liệu ghép nhóm như Bảng 3.2.

Với tứ phân vị Q_1, Q_2, Q_3 lần lượt có 25%, 50%, 75% số giá trị nhỏ hơn Q_1, Q_2, Q_3.

[Hình minh họa: Robot đang giải thích]