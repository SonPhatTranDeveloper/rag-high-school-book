Cho điểm x0 thuộc khoảng K và hàm số y = f (x) xác định trên K hoặc K \ {x0}.
Ta nói hàm số y = f (x) có giới hạn hữu hạn là số L khi x dần tới x0 nếu với dãy số (xn)
bất kì, xn ∈ K \ {x0} và xn → x0, thì f (xn) → L, kí hiệu $\lim_{x \to x_0} f(x) = L$ hay f (x) → L
khi x → x0.

Ví dụ 1. Cho hàm số $f(x) = \frac{x^2 - 4}{x + 2}$. Tìm $\lim_{x \to -2} f(x)$.

Giải
Hàm số y = f (x) xác định trên ℝ \ {-2}.
Giả sử (xn) là dãy số bất kì, thỏa mãn xn ≠ -2 với mọi n và xn → -2 khi n → +∞. Ta có

$\lim f(x_n) = \lim \frac{x_n^2 - 4}{x_n + 2} = \lim \frac{(x_n - 2)(x_n + 2)}{x_n + 2} = \lim (x_n - 2) = \lim x_n - 2 = -2 - 2 = -4$.

Vậy $\lim_{x \to -2} f(x) = -4$.

Nhận xét: $\lim_{x \to x_0} x = x_0$; $\lim_{x \to x_0} c = c$ (c là hằng số).

1. Tìm các giới hạn sau: a) $\lim_{x \to 2} (2x^2 - x)$; b) $\lim_{x \to -1} \frac{x^2 + 2x + 1}{x + 1}$.

2. Các phép toán về giới hạn hữu hạn của hàm số

Cho hai hàm số $y = f(x) = 2x$ và $y = g(x) = \frac{x}{x+1}$.

a) Giả sử (xn) là dãy số bất kì thỏa mãn xn ≠ -1 với mọi n và xn → 1 khi n → +∞.
Tìm giới hạn lim [f (xn) + g(xn)].

b) Từ đó, tìm giới hạn $\lim_{x \to 1} [f(x) + g(x)]$, và so sánh với $\lim_{x \to 1} f(x) + \lim_{x \to 1} g(x)$.

Từ các phép toán về giới hạn hữu hạn của dãy số, ta nhận được các kết quả sau đây:

a) Cho $\lim_{x \to x_0} f(x) = L$ và $\lim_{x \to x_0} g(x) = M$. Khi đó:

• $\lim_{x \to x_0} [f(x) + g(x)] = L + M$

• $\lim_{x \to x_0} [f(x) - g(x)] = L - M$

• $\lim_{x \to x_0} [f(x) \cdot g(x)] = L \cdot M$

• $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \frac{L}{M}$ (với M ≠ 0)

b) Nếu f(x) ≥ 0 và $\lim_{x \to x_0} f(x) = L$ thì L ≥ 0 và $\lim_{x \to x_0} \sqrt{f(x)} = \sqrt{L}$.
(Dấu của f(x) được xét trên khoảng tìm giới hạn, x ≠ x0.)

72