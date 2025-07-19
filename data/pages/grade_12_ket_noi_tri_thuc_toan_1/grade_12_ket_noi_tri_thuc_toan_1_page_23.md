Ví dụ 1. Tìm tiệm cận ngang của đồ thị hàm số $y = f(x) = \frac{3x - 2}{x + 1}$.

Giải

Ta có: $\lim_{x \to \infty} f(x) = \lim_{x \to \infty} \frac{3x - 2}{x + 1} = \lim_{x \to \infty} \frac{3 - \frac{2}{x}}{1 + \frac{1}{x}} = 3$. Tương tự, $\lim_{x \to -\infty} f(x) = 3$.

Vậy đồ thị hàm số $f(x)$ có tiệm cận ngang là đường thẳng $y = 3$.

Ví dụ 2. Tìm các tiệm cận ngang của đồ thị hàm số $y = f(x) = \frac{\sqrt{x^2 + 1}}{x}$.

Giải

Ta có:

$\lim_{x \to +\infty} f(x) = \lim_{x \to +\infty} \frac{\sqrt{x^2 + 1}}{x} = \lim_{x \to +\infty} \sqrt{\frac{x^2 + 1}{x^2}} = \lim_{x \to +\infty} \sqrt{1 + \frac{1}{x^2}} = 1$

$\lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} \frac{\sqrt{x^2 + 1}}{x} = \lim_{x \to -\infty} \left(-\sqrt{\frac{x^2 + 1}{x^2}}\right) = \lim_{x \to -\infty} \left(-\sqrt{1 + \frac{1}{x^2}}\right) = -1$

Vậy đồ thị hàm số $f(x)$ có hai tiệm cận ngang là $y = 1$ và $y = -1$.

Nhận xét: Đồ thị hàm số $f(x)$ như Hình 1.21.

[Hình 1.21: Đồ thị hàm số với hai tiệm cận ngang y = 1 và y = -1]

Luyện tập 1. Tìm tiệm cận ngang của đồ thị hàm số $y = f(x) = \frac{2x - 1}{x - 1}$

Vận dụng 1. Giải bài toán trong tình huống mở đầu.

2. ĐƯỜNG TIỆM CẬN ĐỨNG

HD2. Nhận biết đường tiệm cận đứng

Cho hàm số $y = f(x) = \frac{x}{x - 1}$ có đồ thị $(C)$. Với $x > 1$, xét điểm $M(x; f(x))$ thuộc $(C)$. Gọi $H$ là hình chiếu vuông góc của $M$ trên đường thẳng $x = 1$ (H.1.22).

a) Tính khoảng cách $MH$.

b) Khi $M$ thay đổi trên $(C)$ sao cho khoảng cách $MH$ dần dần 0, có nhận xét gì về tung độ của điểm $M$?

[Hình 1.22: Đồ thị hàm số và đường tiệm cận đứng]

Đường thẳng $x = x_0$ gọi là đường tiệm cận đứng (gọi tắt là tiệm cận đứng) của đồ thị hàm số $y = f(x)$ nếu ít nhất một trong các điều kiện sau được thoả mãn:

$\lim_{x \to x_0^+} f(x) = +\infty$;     $\lim_{x \to x_0^+} f(x) = -\infty$;     $\lim_{x \to x_0^-} f(x) = -\infty$;     $\lim_{x \to x_0^-} f(x) = +\infty$.