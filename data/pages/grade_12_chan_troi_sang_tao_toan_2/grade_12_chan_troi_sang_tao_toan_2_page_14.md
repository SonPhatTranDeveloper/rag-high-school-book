2. Khái niệm tích phân

Cho hàm số $f(x) = 2x - 1$. Lấy hai nguyên hàm tùy ý $F(x)$ và $G(x)$ của $f(x)$, rồi tính $F(3) - F(0)$ và $G(3) - G(0)$. Nhận xét về kết quả nhận được.

Cho $f(x)$ là hàm số liên tục trên đoạn $[a; b]$. Giả sử $F(x)$ và $G(x)$ là hai nguyên hàm của $f(x)$ trên đoạn $[a; b]$. Khi đó, $G(x) = F(x) + C$ với hằng số $C$ nào đó. Do đó,

$G(b) - G(a) = F(b) + C - [(F(a) + C)] = F(b) - F(a)$.

Như vậy, hiệu số $F(b) - F(a)$ không phụ thuộc vào việc chọn nguyên hàm $F(x)$ của $f(x)$.

Cho hàm số $f(x)$ liên tục trên đoạn $[a; b]$. Nếu $F(x)$ là một nguyên hàm của $f(x)$ trên đoạn $[a; b]$ thì hiệu số $F(b) - F(a)$ gọi là tích phân từ $a$ đến $b$ của hàm số $f(x)$, kí hiệu $\int_a^b f(x)dx$.

Hiệu số $F(b) - F(a)$ còn được kí hiệu là $F(x)|_a^b$.

Vậy $\int_a^b f(x)dx = F(x)|_a^b = F(b) - F(a)$.

Ta gọi $\int$ là dấu tích phân, $a$ và $b$ là cận tích phân, $a$ là cận dưới, $b$ là cận trên, $f(x)dx$ là biểu thức dưới dấu tích phân và $f(x)$ là hàm số dưới dấu tích phân.

Chú ý:
a) Trong trường hợp $a = b$ hoặc $a > b$, ta quy ước

$\int_a^a f(x)dx = 0$ và $\int_a^b f(x)dx = -\int_b^a f(x)dx$.

b) Người ta chứng minh được rằng, tích phân chỉ phụ thuộc vào hàm số $f$ và các cận $a, b$ mà không phụ thuộc vào biến số $x$ hay $t$, nghĩa là $\int_a^b f(x)dx = \int_a^b f(t)dt$.

c) Ý nghĩa hình học của tích phân

Nếu hàm số $y = f(x)$ liên tục và không âm trên đoạn $[a; b]$ thì $\int_a^b f(x)dx$ là diện tích $S$ của hình thang cong giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành và hai đường thẳng $x = a, x = b$.

Vậy

$S = \int_a^b f(x)dx$.

[Hình 5: Biểu diễn đồ thị hàm số $y = f(x)$ trên đoạn $[a; b]$ và diện tích $S$ dưới đường cong.]