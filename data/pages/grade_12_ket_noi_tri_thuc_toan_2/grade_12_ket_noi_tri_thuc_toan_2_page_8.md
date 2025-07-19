Chú ý

a) Để tìm họ các nguyên hàm (gọi tắt là tìm nguyên hàm) của hàm số $f(x)$ trên $K$, ta chỉ cần tìm một nguyên hàm $F(x)$ của $f(x)$ trên $K$ và khi đó

$\int f(x)dx = F(x) + C$, $C$ là hằng số.

b) Người ta chứng minh được rằng, nếu hàm số $f(x)$ liên tục trên khoảng $K$ thì $f(x)$ có nguyên hàm trên khoảng đó.

c) Biểu thức $f(x)dx$ gọi là vi phân của nguyên hàm $F(x)$, kí hiệu là $dF(x)$. Vậy $dF(x) = F'(x)dx = f(x)dx$.

d) Khi tìm nguyên hàm của một hàm số mà không chỉ rõ tập $K$, ta hiểu là tìm nguyên hàm của hàm số đó trên tập xác định của nó.

[Hình 4.2 mô tả mối quan hệ giữa đạo hàm và nguyên hàm. Hình vẽ gồm hai hình đa giác, một hình ghi "F(x)" và một hình ghi "f(x)". Mũi tên từ F(x) đến f(x) được ghi chú "Tính đạo hàm", và mũi tên từ f(x) đến F(x) được ghi chú "Tìm nguyên hàm".]

Ví dụ 2. Tìm một nguyên hàm của hàm số $f(x) = x^2$ trên $\mathbb{R}$. Từ đó hãy tìm $\int x^2dx$.

Giải

Vì $(\frac{x^3}{3})' = \frac{3x^2}{3} = x^2$ nên $F(x) = \frac{x^3}{3}$ là một nguyên hàm của hàm số $f(x)$ trên $\mathbb{R}$.

Do đó, $\int x^2dx = \frac{x^3}{3} + C$.

Luyện tập 2. Tìm $\int x^3dx$.

2. TÍNH CHẤT CƠ BẢN CỦA NGUYÊN HÀM

HD3. Khám phá nguyên hàm của tích một hàm số với một hằng số khác 0

Cho $f(x)$ là hàm số liên tục trên $K$, $k$ là một hằng số khác 0. Giả sử $F(x)$ là một nguyên hàm của $f(x)$ trên $K$.

a) Chứng minh $kF(x)$ là một nguyên hàm của hàm số $kf(x)$ trên $K$.

b) Nêu nhận xét về $\int kf(x)dx$ và $k\int f(x)dx$.

$\int kf(x)dx = k\int f(x)dx \quad (k \neq 0)$.

Ví dụ 3. Sử dụng kết quả của Ví dụ 2, hãy tìm:

a) $\int 3x^2dx$;                b) $\int -\frac{3}{2}x^2dx$.

Giải
Ta có:
a) $\int 3x^2dx = 3\int x^2dx = 3 \cdot \frac{x^3}{3} + C = x^3 + C$.

b) $\int -\frac{3}{2}x^2dx = -\frac{3}{2}\int x^2dx = -\frac{3}{2} \cdot \frac{x^3}{3} + C = -\frac{1}{2}x^3 + C$.