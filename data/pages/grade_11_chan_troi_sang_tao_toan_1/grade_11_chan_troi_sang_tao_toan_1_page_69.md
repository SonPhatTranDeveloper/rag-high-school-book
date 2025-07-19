3. Tổng của cấp số nhân lùi vô hạn

Từ một hình vuông có cạnh bằng 1, tô màu một nửa hình vuông, rồi tô màu một nửa hình còn lại, và cứ tiếp tục như vậy (xem Hình 2).

a) Xác định diện tích $u_k$ của phần hình được tô màu lần thứ $k$ ($k = 1, 2, 3, ...$).

b) Tính tổng diện tích $S_n$ của phần hình được tô màu sau lần tô thứ $n$ ($n = 1, 2, 3, ...$).

c) Tìm giới hạn $\lim S_n$ và so sánh giới hạn này với diện tích hình vuông ban đầu.

[Hình 2: Một hình vuông được chia thành các phần nhỏ với các diện tích được đánh dấu $u_1$, $u_2$, $u_3$, $u_4$, $u_5$, và $u_6$.]

Xét cấp số nhân vô hạn $(u_n)$ có công bội $q$ thỏa mãn $|q| < 1$.

Tổng $S_n$ của $n$ số hạng đầu của cấp số nhân này là:

$S_n = u_1 + u_2 + ... + u_n = u_1 \frac{1-q^n}{1-q} = \frac{u_1}{1-q} - \frac{u_1}{1-q}q^n$

Vì $|q| < 1$ nên $\lim q^n = 0$ và do đó

$\lim S_n = \frac{u_1}{1-q} - \frac{u_1}{1-q} \lim q^n = \frac{u_1}{1-q} - \frac{u_1}{1-q} \cdot 0 = \frac{u_1}{1-q}$

Giới hạn này được gọi là tổng của cấp số nhân $(u_n)$, kí hiệu là

$S = u_1 + u_2 + u_3 + ... + u_n + ...$

Cấp số nhân vô hạn $(u_n)$ có công bội $q$ thỏa mãn $|q| < 1$ được gọi là cấp số nhân lùi vô hạn.

Cấp số nhân lùi vô hạn này có tổng là

$S = u_1 + u_2 + ... + u_n + ... = \frac{u_1}{1-q}$

Ví dụ 5. Tính tổng của cấp số nhân lùi vô hạn: $1 - \frac{1}{4} + \frac{1}{16} - \frac{1}{64} + ... + \left(-\frac{1}{4}\right)^n + ...$

Giải

Tổng trên là tổng của cấp số nhân lùi vô hạn có số hạng đầu $u_1 = 1$ và công bội $q = -\frac{1}{4}$ nên

$1 - \frac{1}{4} + \frac{1}{16} - \frac{1}{64} + ... + \left(-\frac{1}{4}\right)^n + ... = \frac{1}{1-\left(-\frac{1}{4}\right)} = \frac{4}{5}$