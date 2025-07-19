2. Số hạng tổng quát của cấp số nhân

Cho cấp số nhân $(u_n)$ có công bội $q$. Tính $u_2, u_3, u_4$ và $u_{10}$ theo $u_1$ và $q$.

Định lí 1

Nếu một cấp số nhân $(u_n)$ có số hạng đầu $u_1$ và công bội $q$ thì số hạng tổng quát $u_n$ của nó được xác định bởi công thức:

$u_n = u_1 \cdot q^{n-1}, n \geq 2.$

Ví dụ 4. Cho cấp số nhân có 8 số hạng, số hạng đầu là 4 374, số hạng cuối là 2. Tìm công bội của cấp số nhân đó.

Giải

Ta có $u_1 = 4374$ và $u_8 = 2$. Gọi $q$ là công bội của cấp số nhân này, ta có:

$u_8 = u_1 \cdot q^7$, suy ra $q^7 = \frac{u_8}{u_1} = \frac{2}{4374} = \frac{1}{2187} = \left(\frac{1}{3}\right)^7$, do đó $q = \frac{1}{3}$.

Viết công thức số hạng tổng quát $u_n$ theo số hạng đầu $u_1$ và công bội $q$ của các cấp số nhân sau:

a) 5; 10; 20; 40; 80; ...

b) 1; $\frac{1}{10}$; $\frac{1}{100}$; $\frac{1}{1000}$; $\frac{1}{10000}$; ...

Chu kì bán rã của nguyên tố phóng xạ poloni 210 là 138 ngày, nghĩa là sau 138 ngày, khối lượng của nguyên tố đó chỉ còn một nửa (theo: https://vi.wikipedia.org/wiki/Poloni-210). Tính khối lượng còn lại của 20 gam poloni 210 sau:

a) 690 ngày;                b) 7314 ngày (khoảng 20 năm).

3. Tổng của n số hạng đầu tiên của cấp số nhân

Cho cấp số nhân $(u_n)$ có công bội $q$. Đặt $S_n = u_1 + u_2 + ... + u_n$.

a) So sánh $q \cdot S_n$ và $(u_2 + u_3 + ... + u_n) + q \cdot u_n$;

b) So sánh $u_1 + q \cdot S_n$ và $S_n + u_1 \cdot q^n$.

Định lí 2

Giả sử $(u_n)$ là một cấp số nhân có công bội $q \neq 1$. Đặt $S_n = u_1 + u_2 + ... + u_n$, khi đó

$S_n = \frac{u_1(1-q^n)}{1-q}$.

Chú ý: Khi $q = 1$ thì $S_n = n \cdot u_1$.