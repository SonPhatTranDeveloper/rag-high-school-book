Luyện tập 3. Cho hàm số $f(x) = x^n (n \in \mathbb{N}^*)$.

a) Chứng minh rằng hàm số $F(x) = \frac{x^{n+1}}{n+1}$ là một nguyên hàm của hàm số $f(x)$. Từ đó tìm $\int x^n dx$.

b) Từ kết quả câu a, tìm $\int kx^n dx$ (k là hằng số thực khác 0).

HD4. Khám phá nguyên hàm của một tổng

Cho f(x) và g(x) là hai hàm số liên tục trên K. Giả sử F(x) là một nguyên hàm của f(x), G(x) là một nguyên hàm của g(x) trên K.

a) Chứng minh F(x) + G(x) là một nguyên hàm của hàm số f(x) + g(x) trên K.

b) Nêu nhận xét về $\int [f(x) + g(x)] dx$ và $\int f(x) dx + \int g(x) dx$.

$\int [f(x) + g(x)] dx = \int f(x) dx + \int g(x) dx.$

$\int [f(x) - g(x)] dx = \int f(x) dx - \int g(x) dx.$

Ví dụ 4. Sử dụng kết quả của Luyện tập 3 và tính chất cơ bản của nguyên hàm, hãy tìm:

a) $\int (x^2 + x) dx$;     b) $\int (4x^3 - 3x^2) dx$.

Giải

Ta có:

a) $\int (x^2 + x) dx = \int x^2 dx + \int x dx = \frac{x^3}{3} + \frac{x^2}{2} + C$.

b) $\int (4x^3 - 3x^2) dx = 4 \int x^3 dx - 3 \int x^2 dx = x^4 - x^3 + C$.

Luyện tập 4. Tìm:

a) $\int (3x^2 + 1) dx$;     b) $\int (2x - 1)^2 dx$.

Ví dụ 5. Giải bài toán trong tình huống mở đầu.

Giải

Gọi S(t) (0 ≤ t ≤ 30) là quãng đường máy bay di chuyển được sau t giây kể từ lúc bắt đầu chạy đà.

Ta có v(t) = S'(t). Do đó, S(t) là một nguyên hàm của hàm số vận tốc v(t). Sử dụng tính chất của nguyên hàm ta được

$S(t) = \int v(t) dt = \int (5 + 3t) dt = 5 \int dt + 3 \int t dt = 5t + \frac{3}{2}t^2 + C$.

Theo giả thiết, S(0) = 0 nên C = 0 và ta được $S(t) = \frac{3}{2}t^2 + 5t$ (m).

Máy bay rời đường băng khi t = 30 (giây) nên $S = S(30) = \frac{3}{2} \cdot 30^2 + 5 \cdot 30 = 1500$ (m).

Vậy quãng đường máy bay đã di chuyển từ khi bắt đầu chạy đà đến khi nó rời đường băng là S = 1500 m.