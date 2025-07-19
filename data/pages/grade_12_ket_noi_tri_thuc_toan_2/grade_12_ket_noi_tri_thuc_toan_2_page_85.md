Phương pháp đơn giản nhất là phương pháp hình thang, có nội dung như sau:

Giả sử f(x) là hàm số liên tục trên đoạn [a; b]. Khi đó:

$\int_a^b f(x)dx \approx \frac{b-a}{2n}[f(x_0) + 2f(x_1) + 2f(x_2) + ... + 2f(x_{n-1}) + f(x_n)]$,

ở đó đoạn [a; b] được chia thành n đoạn con $[x_0; x_1], [x_1; x_2], ..., [x_{n-1}; x_n]$, mỗi đoạn có độ dài là $\Delta x = \frac{b-a}{n}$.

Khi f(x) là hàm liên tục và không âm trên đoạn [a; b], ta có:

Ý nghĩa hình học: Diện tích của hình phẳng giới hạn bởi đồ thị y = f(x), trục hoành và hai đường thẳng x = a, x = b xấp xỉ với tổng diện tích của các hình thang con $A_1, A_2, ..., A_n$ (H.T3).

[Hình minh họa T3 mô tả ý nghĩa hình học của phương pháp hình thang, với trục tọa độ Oxy, đường cong f(x) và các hình thang con được tạo ra]

Đánh giá sai số: Người ta chứng minh được rằng nếu $f''(x)$ liên tục trên đoạn [a; b] thì sai số |E| của phương pháp hình thang được đánh giá như sau:

$|E| \leq \frac{(b-a)^3 M}{12n^2}$, trong đó $M = \max_{x \in [a,b]}|f''(x)|$.

Thuật toán: Để tính xấp xỉ $\int_a^b f(x)dx$ với độ chính xác không vượt quá số ε cho trước, ta thực hiện lần lượt các bước sau:

Bước 1. Tính $f''(x)$ và tìm $M = \max_{x \in [a,b]}|f''(x)|$
(hoặc đánh giá $\max_{x \in [a,b]}|f''(x)| \leq M$, nếu việc tìm chính xác là khó).

Bước 2. Với sai số ε cho trước, tìm số tự nhiên n (nhỏ nhất) sao cho
$|E| \leq \frac{(b-a)^3 M}{12n^2} < \varepsilon$.

Bước 3. Chia đoạn [a; b] thành n đoạn con có độ dài bằng nhau và áp dụng công thức hình thang.

Ví dụ. Tính gần đúng $\int_0^1 e^{-x^2}dx$ với độ chính xác nhỏ hơn 0,01.

Giải

a) Ta có: $f(x) = e^{-x^2}; f'(x) = -2xe^{-x^2}$;

$f''(x) = 4x^2e^{-x^2} - 2e^{-x^2}; f'''(x) = 4x(3-2x^2)e^{-x^2}; f^{(4)}(x) = 0 \Leftrightarrow x = 0$ hoặc $x = \pm\sqrt{\frac{3}{2}}$.

Ta có: $f''(0) = -2; f''(\pm\sqrt{\frac{3}{2}}) = \frac{4}{e\sqrt{e}}; f''(1) = \frac{2}{e}$.

Do đó $M = \max_{x \in [0,1]}|f''(x)| = |f''(0)| = 2$.