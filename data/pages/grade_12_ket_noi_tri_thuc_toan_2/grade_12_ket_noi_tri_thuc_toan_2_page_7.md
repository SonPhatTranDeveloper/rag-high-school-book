Cho hàm số $f(x)$ xác định trên một khoảng $K$ (hoặc một đoạn, hoặc một nửa khoảng). Hàm số $F(x)$ được gọi là một nguyên hàm của hàm số $f(x)$ trên $K$ nếu $F'(x) = f(x)$ với mọi $x$ thuộc $K$.

Chú ý: Trường hợp $K = [a;b]$ thì các đẳng thức $F'(a) = f(a)$ và $F'(b) = f(b)$ được hiểu là đạo hàm bên phải tại điểm $x = a$ và đạo hàm bên trái tại điểm $x = b$ của hàm số $F(x)$, tức là

$$\lim_{x \to a^+} \frac{F(x) - F(a)}{x-a} = f(a) \text{ và } \lim_{x \to b^-} \frac{F(x) - F(b)}{x-b} = f(b).$$

Ví dụ 1. Cho hàm số $f(x) = x^2 - 2x$. Trong các hàm số cho dưới đây, hàm số nào là một nguyên hàm của hàm số $f(x)$ trên $\mathbb{R}$?

a) $F(x) = \frac{x^3}{3} - x^2$;    b) $G(x) = \frac{x^3}{3} + x^2$.

Giải

Ta có: $F'(x) = x^2 - 2x$, $G'(x) = x^2 + 2x$.

Vì $F'(x) = f(x)$ với mọi $x \in \mathbb{R}$ nên hàm số $F(x)$ là một nguyên hàm của $f(x)$ trên $\mathbb{R}$.

Hàm số $G(x)$ không là nguyên hàm của $f(x)$ trên $\mathbb{R}$ vì với $x = 1$, ta có

$$G'(1) = 3 \neq -1 = f(1).$$

Luyện tập 1. Hàm số nào dưới đây là một nguyên hàm của hàm số $f(x) = x + \frac{1}{x}$ trên khoảng $(0; +\infty)$?

a) $F(x) = \frac{1}{2}x^2 + \ln x$;    b) $G(x) = \frac{x^2}{2} - \ln x$.

HD2. Nhận biết họ nguyên hàm của một hàm số

a) Chứng minh rằng hàm số $F(x) = \frac{x^4}{4}$ là một nguyên hàm của hàm số $f(x) = x^3$ trên $\mathbb{R}$.

b) Hàm số $G(x) = \frac{x^4}{4} + C$ (với $C$ là hằng số) có là một nguyên hàm của hàm số $f(x)$ trên $\mathbb{R}$ không? Vì sao?

Giả sử hàm số $F(x)$ là một nguyên hàm của $f(x)$ trên $K$. Khi đó:

a) Với mọi hằng số $C$, hàm số $F(x) + C$ cũng là một nguyên hàm của $f(x)$ trên $K$;

b) Nếu hàm số $G(x)$ là một nguyên hàm của $f(x)$ trên $K$ thì tồn tại một hằng số $C$ sao cho $G(x) = F(x) + C$ với mọi $x \in K$.

Như vậy, nếu $F(x)$ là một nguyên hàm của $f(x)$ trên $K$ thì mọi nguyên hàm của $f(x)$ trên $K$ đều có dạng $F(x) + C$ ($C$ là hằng số). Ta gọi $F(x) + C (C \in \mathbb{R})$ là họ các nguyên hàm của $f(x)$ trên $K$, kí hiệu bởi $\int f(x)dx$.