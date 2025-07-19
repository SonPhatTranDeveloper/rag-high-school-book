c) Các phép toán trên giới hạn hàm số của Mục 2 chỉ áp dụng được khi tất cả các hàm số được xét có giới hạn hữu hạn. Với giới hạn vô cực, ta có một số quy tắc sau đây.

Nếu $\lim_{x \to x_0} f(x) = L \neq 0$ và $\lim_{x \to x_0} g(x) = +\infty$ (hoặc $\lim_{x \to x_0} g(x) = -\infty$) thì $\lim_{x \to x_0} [f(x) \cdot g(x)]$ được tính theo quy tắc cho bởi bảng sau:

$\begin{array}{|c|c|c|}
\hline
\lim_{x \to x_0} f(x) & \lim_{x \to x_0} g(x) & \lim_{x \to x_0} [f(x) \cdot g(x)] \\
\hline
\multirow{2}{*}{L > 0} & +\infty & +\infty \\
\cline{2-3}
 & -\infty & -\infty \\
\hline
\multirow{2}{*}{L < 0} & +\infty & -\infty \\
\cline{2-3}
 & -\infty & +\infty \\
\hline
\end{array}$

Các quy tắc trên vẫn đúng khi thay $x_0^+$ thành $x_0^-$ (hoặc $+\infty, -\infty$).

Ví dụ 7. Tìm các giới hạn sau:

a) $\lim_{x \to 2^+} \frac{1-2x}{x-2}$; b) $\lim_{x \to \infty} (x^2 + 1)$.

Giải

a) Ta có $\lim_{x \to 2^+} (1-2x) = 1-2 \lim_{x \to 2^+} x = 1-2 \cdot 2 = -3$; $\lim_{x \to 2^+} \frac{1}{x-2} = +\infty$.

Do đó $\lim_{x \to 2^+} \frac{1-2x}{x-2} = \lim_{x \to 2^+} [(1-2x) \cdot \frac{1}{x-2}] = -\infty$.

b) Viết $x^2 + 1 = x^2 (1 + \frac{1}{x^2})$. Ta có $\lim_{x \to \infty} x^2 = +\infty$; $\lim_{x \to \infty} (1 + \frac{1}{x^2}) = 1 + \lim_{x \to \infty} \frac{1}{x^2} = 1 + 0 = 1$.

Do đó $\lim_{x \to \infty} (x^2 + 1) = \lim_{x \to \infty} [x^2 (1 + \frac{1}{x^2})] = +\infty$.

5. Tìm các giới hạn sau:

a) $\lim_{x \to 3} \frac{2x}{x-3}$; b) $\lim_{x \to +\infty} (3x-1)$.

2. Xét tình huống ở đầu bài học. Gọi x là hoành độ điểm H. Tính diện tích S(x) của hình chữ nhật OHMK theo x. Diện tích này thay đổi như thế nào khi $x \to 0^+$ và khi $x \to +\infty$.