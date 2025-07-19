Ví dụ 5. Cho hàm số $f(x) = \frac{2x-1}{x+2}$. Tìm $\lim_{x \to +\infty} f(x)$.

Giải
Hàm số xác định trên $(-\infty; -2)$ và $(-2; +\infty)$.
Giả sử $(x_n)$ là dãy số sao cho $x_n > -2$ và $x_n \to +\infty$. Ta có

$\lim f(x_n) = \lim \frac{2x_n-1}{x_n+2} = \lim \frac{2-\frac{1}{x_n}}{1+\frac{2}{x_n}} = \frac{2-\lim \frac{1}{x_n}}{1+\lim \frac{2}{x_n}} = \frac{2-0}{1+0} = 2$.

Vậy $\lim_{x \to +\infty} \frac{2x-1}{x+2} = 2$.

Chú ý:
a) Với $c$ là hằng số và $k$ là số nguyên dương, ta luôn có:
   $\lim_{x \to +\infty} c = c$ và $\lim_{x \to +\infty} \frac{c}{x^k} = 0$.

b) Các phép toán trên giới hạn hàm số ở Mục 2 vẫn đúng khi thay $x \to x_0$ bằng $x \to +\infty$ hoặc $x \to -\infty$.

Ví dụ 6. Tìm $\lim_{x \to \infty} \frac{x^2-3x}{2x^2+1}$

Giải

$\lim_{x \to \infty} \frac{x^2-3x}{2x^2+1} = \lim_{x \to \infty} \frac{1-\frac{3}{x}}{2+\frac{1}{x^2}} = \frac{\lim_{x \to \infty} (1-\frac{3}{x})}{\lim_{x \to \infty} (2+\frac{1}{x^2})} = \frac{1-\lim_{x \to \infty} \frac{3}{x}}{2+\lim_{x \to \infty} \frac{1}{x^2}} = \frac{1-0}{2+0} = \frac{1}{2}$

Tìm các giới hạn sau: a) $\lim_{x \to \infty} \frac{1-3x^2}{x^2+2x}$; b) $\lim_{x \to \infty} \frac{2}{x+1}$.

Một cái hồ đang chứa 200 m³ nước mặn với nồng độ muối 10 kg/m³. Người ta ngọt hoá nước trong hồ bằng cách bơm nước ngọt vào hồ với tốc độ 2 m³/phút.

a) Viết biểu thức $C(t)$ biểu thị nồng độ muối trong hồ sau $t$ phút kể từ khi bắt đầu bơm.

b) Tìm giới hạn $\lim_{t \to \infty} C(t)$ và giải thích ý nghĩa.