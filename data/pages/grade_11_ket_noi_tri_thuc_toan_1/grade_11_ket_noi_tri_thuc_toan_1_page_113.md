Giải

Lấy dãy số $(x_n)$ bất kì sao cho $x_n \neq 1$ và $x_n \to 1$. Ta có $f(x_n) = \frac{x_n - 1}{x_n^2 - 1} = \frac{1}{x_n + 1}$.

Do đó $\lim_{n \to \infty} f(x_n) = \lim_{n \to \infty} \frac{1}{x_n + 1} = \frac{1}{2}$. Vậy $\lim_{x \to 1} f(x) = \frac{1}{2}$.

Tương tự đối với dãy số, ta có các quy tắc tính giới hạn của hàm số tại một điểm như sau:

a) Nếu $\lim_{x \to x_0} f(x) = L$ và $\lim_{x \to x_0} g(x) = M$ thì
   $\lim_{x \to x_0} [f(x) + g(x)] = L + M$;
   $\lim_{x \to x_0} [f(x) - g(x)] = L - M$;
   $\lim_{x \to x_0} [f(x) \cdot g(x)] = L \cdot M$;
   $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \frac{L}{M}$, nếu $M \neq 0$.

b) Nếu $f(x) \geq 0$ với mọi $x \in (a; b) \setminus \{x_0\}$ và $\lim_{x \to x_0} f(x) = L$
   thì $L \geq 0$ và $\lim_{x \to x_0} \sqrt{f(x)} = \sqrt{L}$.

[Hình ảnh một robot hoạt hình màu xám và vàng đang vẫy tay chào]

• $\lim_{x \to x_0} c = c$ với c là hằng số.
• $\lim_{x \to x_0} x^n = x_0^n$ với $n \in \mathbb{N}$.

Ví dụ 2. Cho $f(x) = x - 1$ và $g(x) = x^3$. Tính các giới hạn sau:

a) $\lim_{x \to 1} [3f(x) - g(x)]$;

b) $\lim_{x \to 1} \frac{[f(x)]^2}{g(x)}$

Giải

Ta có $\lim_{x \to 1} f(x) = \lim_{x \to 1} (x - 1) = \lim_{x \to 1} x - \lim_{x \to 1} 1 = 1 - 1 = 0$. Mặt khác, ta thấy $\lim_{x \to 1} g(x) = \lim_{x \to 1} x^3 = 1$.

a) Ta có
   $\lim_{x \to 1} [3f(x) - g(x)] = \lim_{x \to 1} [3f(x)] - \lim_{x \to 1} g(x) = \lim_{x \to 1} 3 \cdot \lim_{x \to 1} f(x) - \lim_{x \to 1} g(x) = 3 \cdot 0 - 1 = -1$.

b) Ta có
   $\lim_{x \to 1} \frac{[f(x)]^2}{g(x)} = \frac{\lim_{x \to 1} [f(x)]^2}{\lim_{x \to 1} g(x)} = \frac{\lim_{x \to 1} f(x) \cdot \lim_{x \to 1} f(x)}{\lim_{x \to 1} g(x)} = \frac{0}{1} = 0$.

Ví dụ 3. Tính $\lim_{x \to 0} \frac{\sqrt{x + 9} - 3}{x}$

Giải

Do mẫu thức có giới hạn là 0 khi $x \to 0$ nên ta không thể áp dụng ngay quy tắc tính giới hạn của thương hai hàm số.

Chú ý rằng $\frac{\sqrt{x + 9} - 3}{x} = \frac{(\sqrt{x + 9})^2 - 3^2}{x(\sqrt{x + 9} + 3)} = \frac{x}{x(\sqrt{x + 9} + 3)} = \frac{1}{\sqrt{x + 9} + 3}$.