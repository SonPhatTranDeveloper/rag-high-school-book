Ví dụ 3. Hãy xác định các tứ phân vị của mẫu số liệu trong 🍑.

Giải

Nhắc lại: $x_1 \leq x_2 \leq ... \leq x_{39}$ là thời gian luyện tập của 39 vận động viên.
Tứ phân vị thứ hai của dãy số liệu $x_1, x_2, ..., x_{39}$ là $x_{20} \in [4; 6)$. Do đó tứ phân vị thứ hai của mẫu số liệu ghép nhóm là

$Q_2 = 4 + \frac{\frac{2 \cdot 39}{4} - (3+8)}{12} \cdot (6-4) = \frac{65}{12} \approx 5,417.$

Tứ phân vị thứ nhất của dãy số liệu $x_1, x_2, ..., x_{39}$ là $x_{10} \in [2; 4)$. Do đó tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là

$Q_1 = 2 + \frac{\frac{1 \cdot 39}{4} - 3}{8} \cdot (4-2) = \frac{59}{16} = 3,6875.$

Tứ phân vị thứ ba của dãy số liệu $x_1, x_2, ..., x_{39}$ là $x_{30} \in [6; 8)$. Do đó tứ phân vị thứ ba của mẫu số liệu ghép nhóm là

$Q_3 = 6 + \frac{\frac{3 \cdot 39}{4} - (3+8+12)}{12} \cdot (8-6) = \frac{169}{24} \approx 7,042.$

Chú ý: Nếu tứ phân vị thứ $k$ là $\frac{1}{2}(x_m + x_{m+1})$, trong đó $x_m$ và $x_{m+1}$ thuộc hai nhóm liên tiếp, ví dụ như $x_m \in [u_{j-1}; u_j)$ và $x_{m+1} \in [u_j; u_{j+1})$ thì ta lấy $Q_k = u_j$.

Ví dụ 4. Một hãng xe ô tô thống kê lại số lần gặp sự cố về động cơ của 100 chiếc xe cùng loại sau 2 năm sử dụng đầu tiên ở bảng sau:

| Số lần gặp sự cố | [1; 2] | [3; 4] | [5; 6] | [7; 8] | [9; 10] |
|-------------------|--------|--------|--------|--------|---------|
| Số xe             | 17     | 33     | 25     | 20     | 5       |

a) Hãy ước lượng các tứ phân vị của mẫu số liệu ghép nhóm trên.
b) Một người cho rằng có trên 25% xe của hãng gặp không ít hơn 4 sự cố về động cơ trong 2 năm sử dụng đầu tiên. Nhận định trên có hợp lí không?

Giải

a) Do số lần gặp sự cố là số nguyên nên ta hiệu chỉnh lại như sau:

| Số lần gặp sự cố | [0,5; 2,5) | [2,5; 4,5) | [4,5; 6,5) | [6,5; 8,5) | [8,5; 10,5) |
|-------------------|------------|------------|------------|------------|-------------|
| Số xe             | 17         | 33         | 25         | 20         | 5           |

Gọi $x_1, x_2, ..., x_{100}$ là mẫu số liệu được xếp theo thứ tự không giảm.

Ta có $x_1, ..., x_{17} \in [0,5; 2,5)$; $x_{18}, ..., x_{50} \in [2,5; 4,5)$; $x_{51}, ..., x_{75} \in [4,5; 6,5)$;
$x_{76}, ..., x_{95} \in [6,5; 8,5)$; $x_{96}, ..., x_{100} \in [8,5; 10,5)$.

Tứ phân vị thứ hai của dãy số liệu $x_1, x_2, ..., x_{100}$ là $\frac{1}{2}(x_{50} + x_{51})$. Do $x_{50} \in [2,5; 4,5)$ và $x_{51} \in [4,5; 6,5)$ nên tứ phân vị thứ hai của mẫu số liệu ghép nhóm là $Q_2 = 4,5$.