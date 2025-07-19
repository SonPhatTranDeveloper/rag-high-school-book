Chú ý
• Ta quy ước rằng khi nói giá trị lớn nhất và giá trị nhỏ nhất của hàm số f(x) (mà không nói "trên tập D") thì ta hiểu đó là giá trị lớn nhất hay giá trị nhỏ nhất của f(x) trên tập xác định của hàm số.

• Để tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên tập D, ta thường lập bảng biến thiên của hàm số trên tập D để kết luận.

Ví dụ 1. Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = f(x) = \sqrt{1-x^2}$.

Giải

Tập xác định của hàm số là [-1; 1].

Cách 1. Sử dụng định nghĩa.

Ta có:

• $f(x) = \sqrt{1-x^2} \geq 0$; dấu bằng xảy ra khi $1-x^2 = 0$, tức là khi $x = -1$ hoặc $x = 1$.
  Do đó $\min_{[-1;1]} f(x) = f(-1) = f(1) = 0$.

• $f(x) = \sqrt{1-x^2} \leq 1$; dấu bằng xảy ra khi $1-x^2 = 1$, tức là khi $x = 0$. Do đó $\max_{[-1;1]} f(x) = f(0) = 1$.

Cách 2. Sử dụng bảng biến thiên.

Với $x \in (-1; 1)$, ta có: $y' = \frac{(1-x^2)'}{2\sqrt{1-x^2}} = -\frac{x}{\sqrt{1-x^2}}$; $y' = 0 \Leftrightarrow x = 0$.

Lập bảng biến thiên của hàm số trên đoạn [-1; 1]:

[Bảng biến thiên được vẽ với 3 cột x, y', y. Giá trị x từ -1 đến 0 đến 1. y' dương từ -1 đến 0, bằng 0 tại 0, âm từ 0 đến 1. y tăng từ 0 tại -1 lên 1 tại 0, rồi giảm xuống 0 tại 1.]

Từ bảng biến thiên, ta được: $\min_{[-1;1]} f(x) = f(-1) = f(1) = 0$; $\max_{[-1;1]} f(x) = f(0) = 1$.

Chú ý. Trong thực hành, ta cũng dùng các kí hiệu $\min_D y$, $\max_D y$ để chỉ giá trị nhỏ nhất, giá trị lớn nhất (nếu có) của hàm số $y = f(x)$ trên tập D. Do đó, trong Ví dụ 1 ta có thể viết:

$\min_{[-1;1]} y = y(-1) = y(1) = 0$; $\max_{[-1;1]} y = y(0) = 1$.

Ví dụ 2. Tìm giá trị lớn nhất và giá trị nhỏ nhất (nếu có) của hàm số $y = x - 2 + \frac{1}{x}$ trên khoảng $(0; +\infty)$.

Giải

Ta có: $y' = 1 - \frac{1}{x^2}$; $y' = 0 \Leftrightarrow x = 1$ (vì $x > 0$).

Tính các giới hạn:

$\lim_{x \to 0^+} y = \lim_{x \to 0^+} (x - 2 + \frac{1}{x}) = +\infty$;    $\lim_{x \to +\infty} y = \lim_{x \to +\infty} (x - 2 + \frac{1}{x}) = +\infty$.