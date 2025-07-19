b) Cường độ tức thời

HD2. Điện lượng Q truyền trong dây dẫn là một hàm số của thời gian t, có dạng Q = Q(t).
a) Tính cường độ trung bình của dòng điện trong khoảng thời gian từ $t_0$ đến t.
b) Giới hạn $\lim_{t \to t_0} \frac{Q(t) - Q(t_0)}{t - t_0}$ cho ta biết điều gì?

Nhận xét. Nhiều bài toán trong Vật lí, Hoá học, Sinh học,... đưa đến việc tìm giới hạn dạng

$\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$,

ở đó y = f(x) là một hàm số đã cho.

Giới hạn trên dẫn đến một khái niệm quan trọng trong Toán học, đó là khái niệm đạo hàm.

2. ĐẠO HÀM CỦA HÀM SỐ TẠI MỘT ĐIỂM

Cho hàm số y = f(x) xác định trên khoảng (a; b) và điểm $x_0 \in (a; b)$.
Nếu tồn tại giới hạn hữu hạn

$\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$

thì giới hạn đó được gọi là đạo hàm của hàm số y = f(x) tại điểm $x_0$, kí hiệu bởi $f'(x_0)$ (hoặc $y'(x_0)$), tức là

$f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$.

Chú ý. Để tính đạo hàm của hàm số y = f(x) tại điểm $x_0 \in (a; b)$, ta thực hiện theo các bước sau:

1. Tính f(x) - f($x_0$).

2. Lập và rút gọn tỉ số $\frac{f(x) - f(x_0)}{x - x_0}$ với $x \in (a; b)$, $x \neq x_0$.

3. Tìm giới hạn $\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$.

Ví dụ 1. Tính đạo hàm của hàm số y = f(x) = $x^2 + 2x$ tại điểm $x_0 = 1$.

Giải
Ta có: f(x) - f(1) = $x^2 + 2x - 3 = x^2 - 1 + 2x - 2 = (x - 1)(x + 3)$.

Với $x \neq 1$, $\frac{f(x) - f(1)}{x - 1} = \frac{(x - 1)(x + 3)}{x - 1} = x + 3$.

Tính giới hạn: $\lim_{x \to 1} \frac{f(x) - f(1)}{x - 1} = \lim_{x \to 1} (x + 3) = 4$.

Vậy f'(1) = 4.