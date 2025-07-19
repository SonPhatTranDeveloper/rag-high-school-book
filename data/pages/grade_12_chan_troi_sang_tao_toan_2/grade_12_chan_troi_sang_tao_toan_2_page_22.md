Ví dụ 1. Tính diện tích hình phẳng giới hạn bởi đồ thị của hàm số $y = x^2 - 4x + 3$, trục hoành và hai đường thẳng $x = 0$, $x = 3$.

Giải

Diện tích cần tìm là $S = \int_0^3 |x^2 - 4x + 3| dx$.

Ta có: $x^2 - 4x + 3 = 0 \Rightarrow x = 1$ hoặc $x = 3$.

Với $x \in [0; 1]$ thì $f(x) \geq 0$. Với $x \in [1; 3]$ thì $f(x) \leq 0$.

Vậy $S = \int_0^3 |x^2 - 4x + 3| dx$

$= \int_0^1 (x^2 - 4x + 3) dx + \int_1^3 (-(x^2 - 4x + 3)) dx$

$= \left[\frac{x^3}{3} - 2x^2 + 3x\right]_0^1 - \left[\frac{x^3}{3} - 2x^2 + 3x\right]_1^3 = \frac{8}{3}$.

[Hình 2: Đồ thị hàm số $y = x^2 - 4x + 3$ với trục hoành và các đường thẳng $x = 0$, $x = 3$. Diện tích cần tính được tô màu.]

Chú ý: Giả sử hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$.

Nếu $f(x)$ không đổi dấu trên đoạn $[a; b]$ thì

$\int_a^b |f(x)| dx = |\int_a^b f(x)dx|$.

Nếu phương trình $f(x) = 0$ không có nghiệm trên khoảng $(a; b)$ thì công thức trên vẫn đúng.

Ví dụ 2. Tính diện tích hình phẳng giới hạn bởi đồ thị của hàm số $y = \sin x$, trục hoành và hai đường thẳng $x = 0$, $x = 3\pi$.

Giải

Diện tích cần tìm là $S = \int_0^{3\pi} |\sin x| dx$.

Trên khoảng $(0; 3\pi)$, phương trình $\sin x = 0$ chỉ có hai nghiệm là $x = \pi$ và $x = 2\pi$.

[Hình 3: Đồ thị hàm số $y = \sin x$ trên khoảng $[0; 3\pi]$.]

Vậy $S = \int_0^{3\pi} |\sin x| dx = \int_0^\pi \sin x dx + \int_\pi^{2\pi} |\sin x| dx + \int_{2\pi}^{3\pi} \sin x dx$

$= |\int_0^\pi \sin x dx| + |\int_\pi^{2\pi} \sin x dx| + |\int_{2\pi}^{3\pi} \sin x dx| = |(-\cos x)|_0^\pi + |(-\cos x)|_\pi^{2\pi} + |(-\cos x)|_{2\pi}^{3\pi}$

$= |2| + |-2| + |2| = 6$.

1. Tính diện tích hình phẳng giới hạn bởi đồ thị của hàm số $y = 2x - x^2$, trục hoành và hai đường thẳng $x = 0$, $x = 3$.

2. Tính diện tích hình phẳng giới hạn bởi đồ thị của hàm số $y = \cos x - 2$, trục hoành và hai đường thẳng $x = 0$, $x = \pi$.