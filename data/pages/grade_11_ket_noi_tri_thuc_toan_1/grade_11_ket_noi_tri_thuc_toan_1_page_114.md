Do đó $\lim_{x \to 0} \frac{\sqrt{x + 9} - 3}{x} = \lim_{x \to 0} \frac{1}{\sqrt{x + 9} + 3} = \lim_{x \to 0} \left[ \frac{1}{\sqrt{x + 9} + 3} \right] = \frac{1}{6}$.

Luyện tập 1. Tính $\lim_{x \to 1} \frac{x - 1}{\sqrt{x} - 1}$

HB1. Nhận biết khái niệm giới hạn một bên

Cho hàm số $f(x) = \frac{|x - 1|}{x - 1}$.

a) Cho $x_n = \frac{n}{n+1}$ và $x'_n = \frac{n+1}{n}$. Tính $y_n = f(x_n)$ và $y'_n = f(x'_n)$.

b) Tìm giới hạn của các dãy số $(y_n)$ và $(y'_n)$.

c) Cho các dãy số $(x_n)$ và $(x'_n)$ bất kì sao cho $x_n < 1 < x'_n$ và $x_n \to 1, x'_n \to 1$, tính $\lim_{n \to +\infty} f(x_n)$ và $\lim_{n \to +\infty} f(x'_n)$.

- Cho hàm số $y = f(x)$ xác định trên khoảng $(x_0; b)$. Ta nói số $L$ là giới hạn bên phải của $f(x)$ khi $x \to x_0$ nếu với dãy số $(x_n)$ bất kì thỏa mãn $x_0 < x_n < b$ và $x_n \to x_0$, ta có $f(x_n) \to L$, kí hiệu $\lim_{x \to x_0^+} f(x) = L$.

- Cho hàm số $y = f(x)$ xác định trên khoảng $(a; x_0)$. Ta nói số $L$ là giới hạn bên trái của $f(x)$ khi $x \to x_0$ nếu với dãy số $(x_n)$ bất kì thỏa mãn $a < x_n < x_0$ và $x_n \to x_0$, ta có $f(x_n) \to L$, kí hiệu $\lim_{x \to x_0^-} f(x) = L$.

Ví dụ 4. Cho hàm số $f(x) = \begin{cases} x^2 & \text{nếu } 0 < x < 1 \\ x + 1 & \text{nếu } 1 \leq x < 2. \end{cases}$

Tính $\lim_{x \to 1^-} f(x)$ và $\lim_{x \to 1^+} f(x)$.

Giải

Với dãy số $(x_n)$ bất kì sao cho $0 < x_n < 1$ và $x_n \to 1$, ta có $f(x_n) = x_n^2$.

Do đó $\lim_{x \to 1^-} f(x) = \lim_{n \to +\infty} f(x_n) = 1$.

Tương tự, với dãy số $(x_n)$ bất kì mà $1 < x_n < 2, x_n \to 1$,

ta có $f(x_n) = x_n + 1$, cho nên $\lim_{x \to 1^+} f(x) = \lim_{n \to +\infty} f(x_n) = 2$.

$\lim_{x \to x_0} f(x) = L$ khi và chỉ khi $\lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = L$.

Luyện tập 2. Cho hàm số $f(x) = \begin{cases} -x & \text{nếu } x < 0 \\ \sqrt{x} & \text{nếu } x \geq 0. \end{cases}$

Tính $\lim_{x \to 0^+} f(x), \lim_{x \to 0^-} f(x)$ và $\lim_{x \to 0} f(x)$.

[Hình minh họa: Một hình vẽ nhỏ của một nhân vật nữ đang giải thích với nụ cười thân thiện]