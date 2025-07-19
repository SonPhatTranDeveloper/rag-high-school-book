Nhận xét: $\lim_{x \to x_0} x = x_0$; $\lim_{x \to x_0} c = c$, với c là hằng số.

Ví dụ 1 Xét hàm số $f(x) = \frac{x^2 - 9}{x - 3}$ $(x \neq 3)$. Chứng minh rằng $\lim_{x \to 3} f(x) = 6$.

Giải

Giả sử $(x_n)$ là dãy số bất kì, thỏa mãn $x_n \neq 3$ và $\lim x_n = 3$.

Ta có $\lim f(x_n) = \lim \frac{x_n^2 - 9}{x_n - 3} = \lim \frac{(x_n - 3)(x_n + 3)}{x_n - 3}$

$= \lim(x_n + 3) = \lim x_n + \lim 3 = 3 + 3 = 6$.

Vậy $\lim_{x \to 3} f(x) = 6$.

Chú ý: Hàm số $f(x)$ có thể không xác định tại $x = x_0$ nhưng vẫn tồn tại giới hạn của hàm số đó khi x dần tới $x_0$.

2. Phép toán trên giới hạn hữu hạn của hàm số

Cho hai hàm số $f(x) = x^2 - 1$, $g(x) = x + 1$.

a) Tính $\lim_{x \to 1} f(x)$ và $\lim_{x \to 1} g(x)$.

b) Tính $\lim_{x \to 1} [f(x) + g(x)]$ và so sánh với $\lim_{x \to 1} f(x) + \lim_{x \to 1} g(x)$.

c) Tính $\lim_{x \to 1} [f(x) - g(x)]$ và so sánh với $\lim_{x \to 1} f(x) - \lim_{x \to 1} g(x)$.

d) Tính $\lim_{x \to 1} [f(x).g(x)]$ và so sánh với $\lim_{x \to 1} f(x). \lim_{x \to 1} g(x)$.

e) Tính $\lim_{x \to 1} \frac{f(x)}{g(x)}$ và so sánh với $\frac{\lim_{x \to 1} f(x)}{\lim_{x \to 1} g(x)}$.

Ta thừa nhận định lí sau:

a) Nếu $\lim_{x \to x_0} f(x) = L$ và $\lim_{x \to x_0} g(x) = M$ $(L, M \in \mathbb{R})$ thì

• $\lim_{x \to x_0} [f(x) + g(x)] = L + M$;    • $\lim_{x \to x_0} [f(x) - g(x)] = L - M$;

• $\lim_{x \to x_0} [f(x) . g(x)] = L . M$;    • $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \frac{L}{M}$ (nếu $M \neq 0$).

b) Nếu $f(x) \geq 0$ và $\lim_{x \to x_0} f(x) = L$ thì $L \geq 0$ và $\lim_{x \to x_0} \sqrt{f(x)} = \sqrt{L}$.

[Hình ảnh phụ: Một ghi chú trong khung màu xanh lá cây nói "Sử dụng định nghĩa, chứng minh rằng $\lim_{x \to 2} x^2 = 4$."]