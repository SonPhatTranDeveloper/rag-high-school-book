Chú ý:
Khi hàm số $y = f(x)$ không liên tục tại điểm $x_0$ thì ta nói $f(x)$ gián đoạn tại điểm $x_0$ và $x_0$ được gọi là điểm gián đoạn của hàm số $f(x)$.

Ví dụ 1. Xét tính liên tục của hàm số:

a) $f(x) = x^2 - 2x + 3$ tại điểm $x_0 = 2$;

b) $f(x) = \begin{cases}
x^2 + 2 & \text{khi } x > 0 \\
2x & \text{khi } x \leq 0
\end{cases}$ tại điểm $x_0 = 0$.

Giải

a) Ta có $f(2) = 3$ và $\lim_{x \to 2} f(x) = \lim_{x \to 2} (x^2 - 2x + 3) = 2^2 - 2 \cdot 2 + 3 = 3$, suy ra $\lim_{x \to 2} f(x) = f(2)$.

Vậy hàm số $y = f(x)$ liên tục tại điểm $x_0 = 2$.

b) Ta có: $f(0) = 2 \cdot 0 = 0$;

$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (2x) = 2 \lim_{x \to 0^-} x = 2 \cdot 0 = 0$;

$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (x^2 + 2) = 0 + 2 = 2$.

Suy ra không tồn tại $\lim_{x \to 0} f(x)$.

Vậy hàm số $y = f(x)$ không liên tục tại điểm $x_0 = 0$.

[Hình 2: Đồ thị minh họa hàm số trong ví dụ b, với trục tọa độ Oxy. Đồ thị gồm hai nhánh: một nhánh parabol phía trên trục x khi x > 0, và một đường thẳng đi qua gốc tọa độ khi x ≤ 0.]

1 Xét tính liên tục của hàm số:

a) $f(x) = 1 - x^2$ tại điểm $x_0 = 3$;

b) $f(x) = \begin{cases}
x^2 + 1 & \text{khi } x > 1 \\
-x & \text{khi } x \leq 1
\end{cases}$ tại điểm $x_0 = 1$.

2. Hàm số liên tục trên một khoảng, trên một đoạn

2 Cho hàm số $y = f(x) = \begin{cases}
x + 1 & \text{khi } 1 < x \leq 2 \\
k & \text{khi } x = 1.
\end{cases}$

a) Xét tính liên tục của hàm số tại mọi điểm $x_0 \in (1; 2)$.
b) Tìm $\lim_{x \to 2} f(x)$ và so sánh giá trị này với $f(2)$.
c) Với giá trị nào của $k$ thì $\lim_{x \to 1^+} f(x) = k$?

• Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$.
Hàm số $y = f(x)$ được gọi là liên tục trên khoảng $(a; b)$ nếu $f(x)$ liên tục tại mọi điểm trong khoảng ấy.

• Cho hàm số $y = f(x)$ xác định trên đoạn $[a; b]$.
Hàm số $f(x)$ được gọi là liên tục trên đoạn $[a; b]$ nếu $f(x)$ liên tục trên khoảng $(a; b)$ và $\lim_{x \to a^+} f(x) = f(a)$, $\lim_{x \to b^-} f(x) = f(b)$.