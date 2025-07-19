Chú ý. Ta biết rằng nếu đường thẳng $y = ax + b$ ($a \neq 0$) là tiệm cận xiên của đồ thị hàm số $y = f(x)$ thì $\lim_{x \to +\infty} [f(x) - (ax + b)] = 0$ hoặc $\lim_{x \to -\infty} [f(x) - (ax + b)] = 0$.

Do đó $\lim_{x \to +\infty} [f(x) - (ax + b)] \cdot \frac{1}{x} = 0$ hoặc $\lim_{x \to -\infty} [f(x) - (ax + b)] \cdot \frac{1}{x} = 0$.

Từ đây suy ra $a = \lim_{x \to \infty} \frac{f(x)}{x}$ hoặc $a = \lim_{x \to -\infty} \frac{f(x)}{x}$.

Khi đó, ta có $b = \lim_{x \to +\infty} [f(x) - ax]$ hoặc $b = \lim_{x \to -\infty} [f(x) - ax]$.

Ngược lại, với a và b xác định như trên, đường thẳng $y = ax + b$ ($a \neq 0$) là một tiệm cận xiên của đồ thị hàm số $y = f(x)$. Đặc biệt, nếu $a = 0$ thì đồ thị hàm số có tiệm cận ngang.

Ví dụ 6. Tìm tiệm cận xiên của đồ thị hàm số $y = f(x) = \frac{x^2 - x + 2}{x + 1}$.

Giải
Ta có:

$a = \lim_{x \to \infty} \frac{f(x)}{x} = \lim_{x \to \infty} \frac{x^2 - x + 2}{x^2 + x} = 1$

$b = \lim_{x \to \infty} [f(x) - x] = \lim_{x \to \infty} \frac{-2x + 2}{x + 1} = -2$.

(Tương tự, $\lim_{x \to -\infty} \frac{f(x)}{x} = 1$, $\lim_{x \to -\infty} [f(x) - x] = -2$.)

Vậy đồ thị hàm số $f(x)$ có tiệm cận xiên là đường thẳng $y = x - 2$.

Nhận xét. Trong thực hành, để tìm tiệm cận xiên của hàm phân thức trong Ví dụ 6, ta viết:

$y = f(x) = \frac{x^2 - x + 2}{x + 1} = x - 2 + \frac{4}{x + 1}$.

Ta có: $\lim_{x \to \infty} [f(x) - (x - 2)] = \lim_{x \to \infty} \frac{4}{x + 1} = 0$;

$\lim_{x \to -\infty} [f(x) - (x - 2)] = \lim_{x \to -\infty} \frac{4}{x + 1} = 0$.

Do đó, đồ thị hàm số $f(x)$ có tiệm cận xiên là đường thẳng $y = x - 2$.

Luyện tập 3. Tìm các tiệm cận đứng và tiệm cận xiên của đồ thị hàm số $y = f(x) = \frac{x^2 - 4x + 2}{1 - x}$