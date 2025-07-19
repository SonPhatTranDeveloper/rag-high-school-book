Tổng quát, ta có:

Cho $F(x)$ là một nguyên hàm của hàm số $f(x)$ trên $K$. Khi đó:
• Với mỗi hằng số $C$, hàm số $F(x) + C$ là một nguyên hàm của $f(x)$ trên $K$;
• Nếu $G(x)$ là một nguyên hàm của hàm số $f(x)$ trên $K$ thì tồn tại hằng số $C$ sao cho $G(x) = F(x) + C$ với mọi $x$ thuộc $K$.

Như vậy, mọi nguyên hàm của hàm số $f(x)$ trên $K$ đều có dạng $F(x) + C$, với $C$ là một hằng số. Ta gọi $F(x) + C, C \in \mathbb{R}$ là họ tất cả các nguyên hàm của $f(x)$ trên $K$, kí hiệu $\int f(x)dx$ và viết

$\int f(x)dx = F(x) + C$.

Chú ý: Biểu thức $f(x)dx$ gọi là vi phân của nguyên hàm $F(x)$ của $f(x)$, kí hiệu là $dF(x)$.
Vậy $dF(x) = F'(x)dx = f(x)dx$.

Ví dụ 2. Tìm:

a) $\int x^2dx$ trên $\mathbb{R}$;

b) $\int \frac{1}{\sin^2 x}dx$ trên $(0; \pi)$.

Giải

a) Vì $(\frac{x^3}{3})' = x^2$, với mọi $x$ thuộc $\mathbb{R}$ nên $F(x) = \frac{x^3}{3}$ là một nguyên hàm của $x^2$ trên $\mathbb{R}$.

Vậy $\int x^2dx = \frac{x^3}{3} + C$ trên $\mathbb{R}$.

b) Vì $(-\cot x)' = \frac{1}{\sin^2 x}$ với mọi $x$ thuộc $(0; \pi)$ nên $F(x) = -\cot x$ là một nguyên hàm của $\frac{1}{\sin^2 x}$ trên $(0; \pi)$. Vậy $\int \frac{1}{\sin^2 x}dx = -\cot x + C$ trên $(0; \pi)$.

Chú ý:
a) Mọi hàm số $f(x)$ liên tục trên $K$ đều có nguyên hàm trên $K$.
Bài toán tìm nguyên hàm của một hàm số mà không chỉ rõ khoảng $K$ thì được hiểu là tìm nguyên hàm trên từng khoảng xác định của hàm số đó.

b) Từ định nghĩa nguyên hàm, ta có $\int f'(x)dx = f(x) + C$.

Chứng minh rằng $F(x) = e^{2x+1}$ là một nguyên hàm của hàm số $f(x) = 2e^{2x+1}$ trên $\mathbb{R}$.