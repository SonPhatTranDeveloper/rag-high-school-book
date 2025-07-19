Giả sử nhóm k là nhóm đầu tiên có tần số tích lũy lớn hơn hoặc bằng $\frac{n}{2}$, tức là $cf_{k-1} < \frac{n}{2}$ nhưng $cf_k \geq \frac{n}{2}$. Ta gọi r, d, n_k lần lượt là đầu mút trái, độ dài, tần số của nhóm k; $cf_{k-1}$ là tần số tích lũy của nhóm k - 1.

Trung vị của mẫu số liệu ghép nhóm, kí hiệu M_e, được tính theo công thức sau:

$$M_e = r + \left(\frac{\frac{n}{2} - cf_{k-1}}{n_k}\right) \cdot d.$$

Ví dụ 5 Sau khi điều tra về số học sinh trong 100 lớp học, người ta chia mẫu số liệu đó thành năm nhóm căn cứ vào số lượng học sinh của mỗi lớp (đơn vị: học sinh) và lập bảng tần số ghép nhóm bao gồm cả tần số tích lũy như Bảng 11. Tìm trung vị của mẫu số liệu đó (làm tròn kết quả đến hàng đơn vị).

Giải

Số phần tử của mẫu là n = 100. Ta có:

$\frac{n}{2} = \frac{100}{2} = 50$

mà cf_3 = 49 < 50 ≤ cf_4 = 79. Suy ra nhóm 4 là nhóm đầu tiên có tần số tích lũy lớn hơn hoặc bằng 50.

Xét nhóm 4 là nhóm [42 ; 44) có r = 42; d = 2; n_4 = 30 và nhóm 3 là nhóm [40 ; 42) có cf_3 = 49.

Áp dụng công thức, ta có trung vị của mẫu số liệu là:

$M_e = 42 + \left(\frac{50-49}{30}\right) \cdot 2 \approx 42$ (học sinh).

2. Ý nghĩa

Trung vị của mẫu số liệu sau khi ghép nhóm xấp xỉ với trung vị của mẫu số liệu không ghép nhóm ban đầu và có thể dùng để đại diện cho mẫu số liệu đã cho.

[Bảng 11 được hiển thị với các cột: Nhóm, Tần số, Tần số tích lũy. Các dòng dữ liệu như sau:
[36 ; 38) | 9 | 9
[38 ; 40) | 15 | 24
[40 ; 42) | 25 | 49
[42 ; 44) | 30 | 79
[44 ; 46) | 21 | 100
n = 100]

[Một ghi chú nhỏ ở góc phải dưới: 5 Xác định trung vị của mẫu số liệu ghép nhóm ở Bảng 1.]