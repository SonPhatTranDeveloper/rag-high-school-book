Hình phẳng giới hạn bởi đồ thị của hai hàm số và hai đường thẳng x = a, x = b

2 Cho hai hàm số $y = 4x - x^2$ và $y = x$ lần lượt có đồ thị (P) và d như Hình 4.

a) Tính diện tích $S_1$ của hình phẳng giới hạn bởi (P), trục hoành và hai đường thẳng x = 0, x = 2.

b) Tính diện tích S của hình phẳng giới hạn bởi (P), d và hai đường thẳng x = 0, x = 2.

[Hình 4: Đồ thị minh họa cho bài toán, bao gồm đường cong (P), đường thẳng d, và vùng diện tích S được tô màu vàng.]

Cho hai hàm số $y = f_1(x)$ và $y = f_2(x)$ liên tục trên đoạn [a; b]. Gọi S là diện tích hình phẳng giới hạn bởi đồ thị của hai hàm số trên và hai đường thẳng x = a, x = b.

Xét trường hợp $f_1(x) \geq f_2(x)$ với mọi x ∈ [a; b]. Kí hiệu $S_1$, $S_2$ là diện tích hình phẳng giới hạn bởi trục hoành, hai đường thẳng x = a, x = b và đồ thị của hàm số $y = f_1(x)$, $y = f_2(x)$ tương ứng. Khi đó,

$S = S_1 - S_2 = \int_a^b f_1(x)dx - \int_a^b f_2(x)dx = \int_a^b [f_1(x) - f_2(x)]dx.$

[Hình 5: Đồ thị minh họa cho công thức tính diện tích S.]

Trong trường hợp tổng quát, ta có kết quả sau:

Cho hai hàm số $y = f_1(x)$, $y = f_2(x)$ liên tục trên đoạn [a; b]. Khi đó, diện tích hình phẳng giới hạn bởi đồ thị của hai hàm số $y = f_1(x)$, $y = f_2(x)$ và hai đường thẳng x = a, x = b được tính bởi công thức:

$S = \int_a^b |f_1(x) - f_2(x)|dx.$

Ví dụ 3. Tính diện tích hình phẳng giới hạn bởi đồ thị của hai hàm số $y = x^2$, $y = 2 - x$ và hai đường thẳng x = 0, x = 2.

Giải

Diện tích cần tìm là

$S = \int_0^2 |x^2 - (2-x)| dx = \int_0^2 |x^2 + x - 2| dx.$

Ta có $x^2 + x - 2 = 0 \Leftrightarrow x = 1$ hoặc $x = -2$.

Vậy $S = \int_0^1 |x^2 + x - 2| dx + \int_1^2 |x^2 + x - 2| dx$

$= |\int_0^1 (x^2 + x - 2) dx| + |\int_1^2 (x^2 + x - 2) dx|$

$= |[\frac{x^3}{3} + \frac{x^2}{2} - 2x]_0^1| + |[\frac{x^3}{3} + \frac{x^2}{2} - 2x]_1^2| = |\frac{7}{6}| + |\frac{11}{6}| = 3.$

[Hình 6: Đồ thị minh họa cho ví dụ 3, với vùng diện tích cần tính được tô màu vàng.]