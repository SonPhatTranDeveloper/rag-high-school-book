Thông thường một dãy số có thể được cho bằng các cách sau:
Cách 1: Liệt kê các số hạng (với các dãy số hữu hạn).
Cách 2: Cho công thức của số hạng tổng quát $u_n$.
Cách 3: Cho hệ thức truy hồi, nghĩa là
• Cho số hạng thứ nhất $u_1$ (hoặc một vài số hạng đầu tiên);
• Cho một công thức tính $u_n$ theo $u_{n-1}$ (hoặc theo vài số hạng đứng ngay trước nó).
Cách 4: Cho bằng cách mô tả.

Trong 🔍, $(a_n)$ là dãy số chỉ có 5 số hạng được cho bằng cách liệt kê, $(b_n)$ được cho bởi công thức của số hạng tổng quát, $(c_n)$ được cho bởi hệ thức truy hồi và $(d_n)$ được cho bằng cách mô tả.

Ví dụ 3. Cho dãy số $(u_n)$ với $u_n = \frac{n-1}{3n+1}$.

a) Tìm ba số hạng đầu tiên.
b) Tính $u_{50}$ và $u_{99}$.

Giải

a) Ba số hạng đầu tiên là: $u_1 = 0; u_2 = \frac{1}{7}; u_3 = \frac{2}{10} = \frac{1}{5}$.

b) Ta có: $u_{50} = \frac{50-1}{3 \cdot 50+1} = \frac{49}{151}; u_{99} = \frac{99-1}{3 \cdot 99+1} = \frac{98}{298} = \frac{49}{149}$.

Ví dụ 4. Cho dãy số $(u_n)$ xác định bởi: $\begin{cases} u_1 = 1, u_2 = 1 \\ u_n = u_{n-1} + u_{n-2} (n \geq 3). \end{cases}$

Tính $u_5$.

Giải

Ta có: $u_3 = u_2 + u_1 = 1 + 1 = 2; u_4 = u_3 + u_2 = 2 + 1 = 3; u_5 = u_4 + u_3 = 3 + 2 = 5$.
Vậy $u_5 = 5$.

Cho dãy số $(u_n)$ xác định bởi: $\begin{cases} u_1 = 3 \\ u_{n+1} = 2u_n (n \geq 1). \end{cases}$

a) Chứng minh $u_2 = 2 \cdot 3; u_3 = 2^2 \cdot 3; u_4 = 2^3 \cdot 3$.
b) Dự đoán công thức số hạng tổng quát của dãy số $(u_n)$.

Một chồng cột gỗ được xếp thành các lớp, hai lớp liền tiếp hơn kém nhau 1 cột gỗ (Hình 1). Gọi $u_n$ là số cột gỗ nằm ở lớp thứ $n$ tính từ trên xuống và cho biết lớp trên cùng có 14 cột gỗ. Hãy xác định dãy số $(u_n)$ bằng hai cách:

a) Viết công thức số hạng tổng quát $u_n$.
b) Viết hệ thức truy hồi.

[Hình 1: Một hình ảnh minh họa chồng cột gỗ được xếp thành các lớp, với lớp trên cùng có nhiều cột gỗ nhất và các lớp dưới giảm dần số lượng cột gỗ, tạo thành hình dạng tam giác.]