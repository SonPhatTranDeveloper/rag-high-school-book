b) Một số quy tắc tính giới hạn vô cực

Chú ý các quy tắc tính giới hạn hữu hạn không còn đúng cho giới hạn vô cực.

Ta có một số quy tắc tính giới hạn của tích và thương hai hàm số khi một trong hai hàm số đó có giới hạn vô cực.

• Quy tắc tìm giới hạn của tích $f(x)g(x)$.

Giả sử $\lim_{x \to x_0} f(x) = L \neq 0$ và $\lim_{x \to x_0} g(x) = +\infty$ (hoặc $-\infty$). Khi đó $\lim_{x \to x_0} f(x)g(x)$ được tính theo quy tắc cho trong bảng sau:

$\begin{array}{|c|c|c|}
\hline
\lim_{x \to x_0} f(x) & \lim_{x \to x_0} g(x) & \lim_{x \to x_0} f(x)g(x) \\
\hline
L > 0 & +\infty & +\infty \\
& -\infty & -\infty \\
\hline
L < 0 & +\infty & -\infty \\
& -\infty & +\infty \\
\hline
\end{array}$

• Quy tắc tìm giới hạn của thương $\frac{f(x)}{g(x)}$:

$\begin{array}{|c|c|c|c|}
\hline
\lim_{x \to x_0} f(x) & \lim_{x \to x_0} g(x) & \text{Dấu của } g(x) & \lim_{x \to x_0} \frac{f(x)}{g(x)} \\
\hline
L & +\infty & \text{Tùy ý} & 0 \\
\hline
L > 0 & 0 & + & +\infty \\
& & - & -\infty \\
\hline
L < 0 & 0 & + & -\infty \\
& & - & +\infty \\
\hline
\end{array}$

Các quy tắc trên vẫn đúng cho các trường hợp $x \to x_0^+$, $x \to x_0^-$.

Ví dụ 9. Tính $\lim_{x \to 0} \frac{x+1}{x^2}$.

Giải

Ta sử dụng quy tắc tìm giới hạn của thương. Rõ ràng, giới hạn của tử số $\lim_{x \to 0} (x+1) = 1$.

Ngoài ra, mẫu số nhận giá trị dương với mọi $x \neq 0$ và $\lim_{x \to 0} x^2 = 0$. Do vậy $\lim_{x \to 0} \frac{x+1}{x^2} = +\infty$.

Ví dụ 10. Tính $\lim_{x \to 1^-} \frac{1}{x(1-x)}$ và $\lim_{x \to 1^+} \frac{1}{x(1-x)}$.

Giải

Viết $\frac{1}{x(1-x)} = \frac{1}{x} \cdot \frac{1}{1-x}$, ta có $\lim_{x \to 1^-} \frac{1}{x} = 1 > 0$. Hơn nữa $\lim_{x \to 1^-} \frac{1}{1-x} = -\infty$ do $1-x > 0$ khi $x > 1$.

Áp dụng quy tắc tìm giới hạn của tích, ta được $\lim_{x \to 1^-} \frac{1}{x(1-x)} = -\infty$.

Lí luận tương tự, ta có $\lim_{x \to 1^+} \frac{1}{x(1-x)} = +\infty$.