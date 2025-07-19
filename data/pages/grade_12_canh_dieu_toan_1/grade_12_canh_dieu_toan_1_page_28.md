Ví dụ 5 Tìm tiệm cận xiên của đồ thị hàm số $y = f(x) = \frac{x^2 + 3x}{x - 2}$.

Giải

Ta có: $a = \lim_{x \to +\infty} \frac{f(x)}{x} = \lim_{x \to +\infty} \frac{x^2 + 3x}{x(x - 2)} = 1$

và $b = \lim_{x \to +\infty} [f(x) - x] = \lim_{x \to +\infty} \frac{5x}{x - 2} = 5$.

Vậy đường thẳng $y = x + 5$ là tiệm cận xiên của đồ thị hàm số đã cho (khi $x \to +\infty$).

Tương tự, do $\lim_{x \to -\infty} \frac{f(x)}{x} = 1$ và $\lim_{x \to -\infty} [f(x) - x] = 5$ nên đường thẳng $y = x + 5$ cũng là tiệm cận xiên của đồ thị hàm số đã cho (khi $x \to -\infty$).

[Hình ảnh hiển thị một ô màu xanh lá cây với nội dung:]
4. Tìm tiệm cận xiên của đồ thị hàm số
$y = f(x) = \frac{x^2 - 3x + 2}{x + 3}$

Ví dụ 6 Một bể chứa 5 000 lít nước tinh khiết. Người ta bơm vào bể đó nước muối có nồng độ 30 gam muối cho mỗi lít nước với tốc độ 25 lít/phút.

a) Chứng tỏ nồng độ muối trong bể sau t phút (tính bằng tỉ số của khối lượng muối trong bể và thể tích nước trong bể, đơn vị: gam/lít) là $f(t) = \frac{30t}{200 + t}$.

b) Xem $y = f(t)$ là một hàm số xác định trên nửa khoảng $[0; +\infty)$, hãy tìm tiệm cận ngang của đồ thị hàm số đó.

c) Nêu nhận xét về nồng độ muối trong bể sau thời gian t ngày càng lớn.

Giải

a) Sau t phút, ta có: khối lượng muối trong bể là $25 \cdot 30 \cdot t = 750t$ (gam); thể tích của lượng nước trong bể là $5000 + 25t$ (lít). Vậy nồng độ muối sau t phút là

$f(t) = \frac{750t}{5000 + 25t} = \frac{30t}{200 + t}$ (gam/lít).

b) Ta có:

$\lim_{t \to +\infty} f(t) = \lim_{t \to +\infty} \frac{30t}{200 + t}$

$= \lim_{t \to +\infty} \left(30 - \frac{6000}{200 + t}\right) = 30$.

Vậy đường thẳng $y = 30$ là tiệm cận ngang của đồ thị hàm số $f(t)$ (Hình 17).

c) Ta có đồ thị hàm số $y = f(t)$ nhận đường thẳng $y = 30$ làm tiệm cận ngang, tức là khi t càng lớn thì nồng độ muối trong bể sẽ tiến gần đến mức 30 (gam/lít). Lúc đó, nồng độ muối trong bể sẽ gần như bằng nồng độ muối trong nước muối được bơm vào bể.

[Hình 17: Đồ thị biểu diễn hàm số $y = f(t)$ với tiệm cận ngang $y = 30$]