• Giả sử nhóm p là nhóm đầu tiên có tần số tích lũy lớn hơn hoặc bằng $\frac{n}{4}$, tức là $cf_{p-1} < \frac{n}{4}$ nhưng $cf_p \geq \frac{n}{4}$. Ta gọi s, h, n_p lần lượt là đầu mút trái, độ dài, tần số của nhóm p; $cf_{p-1}$ là tần số tích lũy của nhóm p - 1.

Tứ phân vị thứ nhất Q_1 được tính theo công thức sau:

$Q_1 = s + \left(\frac{\frac{n}{4} - cf_{p-1}}{n_p}\right) \cdot h.$

• Giả sử nhóm q là nhóm đầu tiên có tần số tích lũy lớn hơn hoặc bằng $\frac{3n}{4}$, tức là $cf_{q-1} < \frac{3n}{4}$ nhưng $cf_q \geq \frac{3n}{4}$. Ta gọi t, l, n_q lần lượt là đầu mút trái, độ dài, tần số của nhóm q; $cf_{q-1}$ là tần số tích lũy của nhóm q - 1.

Tứ phân vị thứ ba Q_3 được tính theo công thức sau:

$Q_3 = t + \left(\frac{\frac{3n}{4} - cf_{q-1}}{n_q}\right) \cdot l.$

Ví dụ 6 Bảng 13 cho ta bảng tần số ghép nhóm số liệu thống kê cân nặng của 40 học sinh lớp 11A trong một trường trung học phổ thông (đơn vị: kilôgam). Xác định tứ phân vị của mẫu số liệu ghép nhóm đó.

Giải
Số phần tử của mẫu là n = 40.
• Ta có: $\frac{n}{4} = \frac{40}{4} = 10$ mà 2 < 10 < 12. Suy ra nhóm 2 là nhóm đầu tiên có tần số tích lũy lớn hơn hoặc bằng 10. Xét nhóm 2 là nhóm [40 ; 50) có s = 40; h = 10; n_2 = 10 và nhóm 1 là nhóm [30 ; 40) có cf_1 = 2.

Áp dụng công thức, ta có tứ phân vị thứ nhất là:

$Q_1 = 40 + \left(\frac{10-2}{10}\right) \cdot 10 = 48$ (kg).

[Bảng 13 được hiển thị với các cột: Nhóm, Tần số, Tần số tích lũy]
[Các hàng trong bảng:
[30 ; 40), 2, 2
[40 ; 50), 10, 12
[50 ; 60), 16, 28
[60 ; 70), 8, 36
[70 ; 80), 2, 38
[80 ; 90), 2, 40
n = 40]