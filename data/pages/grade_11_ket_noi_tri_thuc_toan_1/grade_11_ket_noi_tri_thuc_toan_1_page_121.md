Ví dụ 2. Xét tính liên tục của hàm dấu $s(x) = \begin{cases}
1 & \text{nếu } x > 0 \\
0 & \text{nếu } x = 0 \text{ tại điểm } x_0 = 0. \\
-1 & \text{nếu } x < 0
\end{cases}$

Giải
Ta thấy $\lim_{x \to 0^+} s(x) = 1$, $\lim_{x \to 0^-} s(x) = -1$. Do đó không tồn tại giới hạn $\lim_{x \to 0} s(x)$.
Vậy hàm số này gián đoạn tại 0.

Luyện tập 1. Xét tính liên tục của hàm số $f(x) = \begin{cases}
-x & \text{nếu } x < 0 \\
0 & \text{nếu } x = 0 \\
x^2 & \text{nếu } x > 0
\end{cases}$
tại điểm $x_0 = 0$.

[Hình minh họa: Robot đang giải thích] Hàm số $f(x)$ liên tục tại $x_0$ khi và chỉ khi $\lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = f(x_0)$.

2. HÀM SỐ LIÊN TỤC TRÊN MỘT KHOẢNG

HD2. Cho hai hàm số $f(x) = \begin{cases}
2x & \text{nếu } 0 \leq x \leq \frac{1}{2} \\
1 & \text{nếu } \frac{1}{2} < x \leq 1
\end{cases}$ và $g(x) = \begin{cases}
x & \text{nếu } 0 \leq x \leq \frac{1}{2} \\
1 & \text{nếu } \frac{1}{2} < x \leq 1
\end{cases}$

với đồ thị tương ứng như Hình 5.7

[Hình 5.7: Hai đồ thị biểu diễn hàm số y = f(x) và y = g(x)]

Xét tính liên tục của các hàm số $f(x)$ và $g(x)$ tại điểm $x = \frac{1}{2}$ và nhận xét về sự khác nhau giữa hai đồ thị.

Hàm số $y = f(x)$ được gọi là liên tục trên khoảng $(a; b)$ nếu nó liên tục tại mọi điểm thuộc khoảng này.

Hàm số $y = f(x)$ được gọi là liên tục trên đoạn $[a; b]$ nếu nó liên tục trên khoảng $(a; b)$ và $\lim_{x \to a^+} f(x) = f(a)$, $\lim_{x \to b^-} f(x) = f(b)$.

Các khái niệm hàm số liên tục trên nửa khoảng như $[a; b)$, $(a; +\infty)$,... được định nghĩa theo cách tương tự. Có thể thấy đồ thị của hàm số liên tục trên một khoảng là một đường liên trên khoảng đó.