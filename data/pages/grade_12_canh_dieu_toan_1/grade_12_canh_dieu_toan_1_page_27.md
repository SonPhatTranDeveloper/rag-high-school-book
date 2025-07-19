Trong trường hợp tổng quát, ta có định nghĩa sau:

Đường thẳng $y = ax + b (a \neq 0)$ được gọi là đường tiệm cận xiên (hay tiệm cận xiên) của đồ thị hàm số $y = f(x)$ nếu:

$$\lim_{x \to +\infty} [f(x) - (ax + b)] = 0 \text{ hoặc } \lim_{x \to -\infty} [f(x) - (ax + b)] = 0.$$

Nhận xét: Giả sử đường thẳng $y = ax + b (a \neq 0)$ là tiệm cận xiên của đồ thị hàm số $y = f(x)$. Lấy điểm $M$ thuộc đồ thị hàm số $y = f(x)$ và điểm $N$ thuộc đường thẳng $y = ax + b$ có cùng hoành độ $x$. Khi đó, độ dài $MN$ tiến tới 0 khi $x \to +\infty$ (Hình 16a) hay $x \to -\infty$ (Hình 16b).

[Hình 16: Hai đồ thị minh họa cho tiệm cận xiên. Hình a) cho trường hợp $x \to +\infty$ và hình b) cho trường hợp $x \to -\infty$. Mỗi hình có hai đường: một đường cong biểu diễn hàm số $y = f(x)$ và một đường thẳng biểu diễn tiệm cận xiên $y = ax + b$.]

Ví dụ 4: Chứng minh rằng đường thẳng $y = 2x - 1$ là tiệm cận xiên của đồ thị hàm số $y = f(x) = 2x - 1 - \frac{1}{x^2 + 1}$.

Giải

Do $\lim_{x \to +\infty} [f(x) - (2x - 1)] = \lim_{x \to +\infty} \frac{-1}{x^2 + 1} = 0$

nên đường thẳng $y = 2x - 1$ là tiệm cận xiên của đồ thị hàm số đã cho.

Chú ý: Để xác định hệ số $a, b$ của đường tiệm cận xiên $y = ax + b$ của đồ thị hàm số $y = f(x)$, ta có thể áp dụng công thức sau:

$$a = \lim_{x \to \infty} \frac{f(x)}{x} \text{ và } b = \lim_{x \to \infty} [f(x) - ax] \text{ hoặc } a = \lim_{x \to -\infty} \frac{f(x)}{x} \text{ và } b = \lim_{x \to -\infty} [f(x) - ax].$$

(Khi $a = 0$ thì ta có tiệm cận ngang $y = b$).

[Ở góc phải dưới của trang có một hộp màu xanh lá cây với nội dung:]
3. Chứng minh rằng đường thẳng $y = -x$ là tiệm cận xiên của đồ thị hàm số $y = f(x) = \frac{-x^2 - 2x + 3}{x + 2}$.