Luyện tập 3. Tìm $\lim_{n \to \infty} \frac{\sqrt{2n^2 + 1}}{n + 1}$.

3. TỔNG CỦA CẤP SỐ NHÂN LUI VÔ HẠN

H94. Làm quen với việc tính tổng vô hạn

Cho hình vuông cạnh 1 (đơn vị đo dài). Chia hình vuông đó thành bốn hình vuông nhỏ bằng nhau, sau đó tô màu hình vuông nhỏ góc dưới bên trái (H.5.2). Lặp lại các thao tác này với hình vuông nhỏ góc trên bên phải. Giả sử quá trình trên tiếp diễn vô hạn lần. Gọi $u_1, u_2,..., u_n,...$ lần lượt là độ dài cạnh của các hình vuông được tô màu.

a) Tính tổng $S_n = u_1 + u_2 + ... + u_n$.

b) Tìm $S = \lim_{n \to \infty} S_n$.

[Hình 5.2: Hình minh họa quá trình chia và tô màu hình vuông]

Cấp số nhân vô hạn $(u_n)$ có công bội $q$ với $|q| < 1$ được gọi là cấp số nhân lui vô hạn.

Cho cấp số nhân lui vô hạn $(u_n)$ với công bội $q$. Khi đó

$S_n = u_1 + u_2 + ... + u_n = \frac{u_1(1-q^n)}{1-q}$.

Vì $|q| < 1$ nên $q^n \to 0$ khi $n \to \infty$. Do đó, ta có

$\lim_{n \to \infty} S_n = \lim_{n \to \infty} \left[\frac{u_1}{1-q} - \left(\frac{u_1}{1-q}\right)q^n\right] = \frac{u_1}{1-q}$.

Giới hạn này được gọi là tổng của cấp số nhân lui vô hạn $(u_n)$, và kí hiệu là

$S = u_1 + u_2 + ... + u_n + ...$

Như vậy

$S = \frac{u_1}{1-q} \quad (|q| < 1)$.

Ví dụ 4. Tính tổng $S = 1 - \frac{1}{2} + \frac{1}{4} - \frac{1}{8} + ... + \left(-\frac{1}{2}\right)^{n-1} + ...$

Giải

Đây là tổng của cấp số nhân lui vô hạn với $u_1 = 1$ và $q = -\frac{1}{2}$.
Do đó

$S = \frac{u_1}{1-q} = \frac{1}{1-\left(-\frac{1}{2}\right)} = \frac{2}{3}$.