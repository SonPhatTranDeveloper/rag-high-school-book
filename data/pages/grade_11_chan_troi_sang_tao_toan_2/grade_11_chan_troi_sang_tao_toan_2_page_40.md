Khi đó, giới hạn

$\lim_{t \to t_0} \frac{s(t) - s(t_0)}{t - t_0}$

được gọi là vận tốc tức thời của chuyển động tại thời điểm $t_0$, kí hiệu $v(t_0)$. Giới hạn này cũng được gọi là đạo hàm của hàm số $s(t)$ theo thời gian $t$ tại thời điểm $t_0$, kí hiệu $s'(t_0)$.

Vậy

$v(t_0) = s'(t_0) = \lim_{t \to t_0} \frac{s(t) - s(t_0)}{t - t_0}$.

Tổng quát, ta có định nghĩa đạo hàm của hàm số bất kì như sau:

Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ và $x_0 \in (a; b)$.
Nếu tồn tại giới hạn hữu hạn

$\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$

thì giới hạn này được gọi là đạo hàm của hàm số $f(x)$ tại $x_0$, kí hiệu là $f'(x_0)$ hoặc $y'(x_0)$.
Vậy:

$f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$.

Ví dụ 1. Cho hàm số $f(x) = x^2$. Tính $f'(x_0)$ với $x_0 \in \mathbb{R}$.

Giải

Ta có $f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = \lim_{x \to x_0} \frac{x^2 - x_0^2}{x - x_0} = \lim_{x \to x_0} (x + x_0) = 2x_0$.

Chú ý:
Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$. Nếu hàm số này có đạo hàm tại mọi điểm $x \in (a; b)$ thì ta nói nó có đạo hàm trên khoảng $(a; b)$, kí hiệu $y'$ hoặc $f'(x)$.

Ví dụ 2. Tính đạo hàm của các hàm số sau:

a) $f(x) = C$ ($C$ là hằng số);

b) $f(x) = \frac{1}{x}$ với $x \neq 0$.

Giải

a) Với bất kì $x_0$, ta có:

$f'(x) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = \lim_{x \to x_0} \frac{C - C}{x - x_0} = \lim_{x \to x_0} 0 = 0$.

Vậy $f'(x) = (C)' = 0$ trên $\mathbb{R}$.