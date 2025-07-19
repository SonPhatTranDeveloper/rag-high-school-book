b) Tính đạo hàm $f'(x)$ và tìm các điểm $x \in (-1; 2)$ mà $f'(x) = 0$.

c) Tính giá trị của hàm số tại hai đầu mút của đoạn [-1; 2] và tại các điểm x đã tìm ở câu b. So sánh số nhỏ nhất trong các giá trị này với $\min_{[-1;2]} f(x)$, số lớn nhất trong các giá trị này với $\max_{[-1;2]} f(x)$.

Giả sử $y = f(x)$ là hàm số liên tục trên [a; b] và có đạo hàm trên (a; b), có thể trừ ra tại một số hữu hạn điểm mà tại đó hàm số không có đạo hàm. Giả sử chỉ có hữu hạn điểm trong đoạn [a; b] mà đạo hàm $f'(x)$ bằng 0.

Các bước tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số f(x) trên đoạn [a; b]:
1. Tìm các điểm $x_1, x_2,..., x_n \in (a; b)$, tại đó $f'(x)$ bằng 0 hoặc không tồn tại.
2. Tính $f(x_1), f(x_2),..., f(x_n), f(a)$ và $f(b)$.
3. Tìm số lớn nhất M và số nhỏ nhất m trong các số trên. Ta có:
   $M = \max_{[a;b]} f(x); m = \min_{[a;b]} f(x)$.

Ví dụ 4. Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = x^4 - 4x^2 + 3$ trên đoạn [0; 4].

Giải

Ta có: $y' = 4x^3 - 8x = 4x(x^2 - 2)$; $y' = 0 \Leftrightarrow x = 0$ hoặc $x = \sqrt{2}$ (vì $x \in [0; 4]$);

$y(0) = 3; y(4) = 195; y(\sqrt{2}) = -1$.

Do đó: $\max_{[0;4]} y = y(4) = 195$; $\min_{[0;4]} y = y(\sqrt{2}) = -1$.

Ví dụ 5. Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = \sin x + \cos x$ trên đoạn $[0; 2\pi]$.

Giải

Ta có: $y' = \cos x - \sin x; y' = 0 \Leftrightarrow \cos x = \sin x \Leftrightarrow x = \frac{\pi}{4}$ hoặc $x = \frac{5\pi}{4}$ (vì $x \in [0; 2\pi]$);

$y(0) = 1; y(2\pi) = 1; y(\frac{\pi}{4}) = \sqrt{2}; y(\frac{5\pi}{4}) = -\sqrt{2}$.

Do đó: $\max_{[0;2\pi]} y = y(\frac{\pi}{4}) = \sqrt{2}$; $\min_{[0;2\pi]} y = y(\frac{5\pi}{4}) = -\sqrt{2}$.

Luyện tập 2. Tìm giá trị lớn nhất và giá trị nhỏ nhất của các hàm số sau:

a) $y = 2x^3 - 3x^2 + 5x + 2$ trên đoạn [0; 2];     b) $y = (x + 1)e^{-x}$ trên đoạn [-1; 1].

Vận dụng. Giả sử sự lây lan của một loại virus ở một địa phương có thể được mô hình hóa bằng hàm số $N(t) = -t^3 + 12t^2, 0 \leq t \leq 12$, trong đó N là số người bị nhiễm bệnh (tính bằng trăm người) và t là thời gian (tuần).

a) Hãy ước tính số người tối đa bị nhiễm bệnh ở địa phương đó.

b) Đạo hàm $N'(t)$ biểu thị tốc độ lây lan của virus (còn gọi là tốc độ truyền bệnh). Hỏi virus sẽ lây lan nhanh nhất khi nào?