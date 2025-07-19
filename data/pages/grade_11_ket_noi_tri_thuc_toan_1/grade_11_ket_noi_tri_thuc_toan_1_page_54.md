Giải
Với mọi $n \geq 2$, ta có
$\frac{u_n}{u_{n-1}} = \frac{1}{3^{n-1}} \cdot \frac{3^{n-2}}{1} = \frac{1}{3}$,

tức là $u_n = \frac{1}{3} \cdot u_{n-1}$ với mọi $n \geq 2$.

Vậy $(u_n)$ là một cấp số nhân với số hạng đầu $u_1 = \frac{1}{3^0} = 1$
và công bội $q = \frac{1}{3}$.

Luyện tập 1. Cho dãy số $(u_n)$ với $u_n = 2 \cdot 5^n$. Chứng minh rằng dãy số này là một cấp số nhân. Xác định số hạng đầu và công bội của nó.

2. SỐ HẠNG TỔNG QUÁT

HD2. Công thức số hạng tổng quát của cấp số nhân

Cho cấp số nhân $(u_n)$ với số hạng đầu $u_1$ và công bội $q$.
a) Tính các số hạng $u_2, u_3, u_4, u_5$ theo $u_1$ và $q$.
b) Dự đoán công thức tính số hạng thứ $n$ theo $u_1$ và $q$.

Nếu một cấp số nhân có số hạng đầu $u_1$ và công bội $q$ thì số hạng tổng quát $u_n$ của nó được xác định bởi công thức
$u_n = u_1 \cdot q^{n-1}$ với $n \geq 2$.

Ví dụ 3. Tìm năm số hạng đầu và số hạng thứ 100 của cấp số nhân: 8, -4, ...

Giải

Cấp số nhân này có số hạng đầu $u_1 = 8$ và công bội $q = \frac{-4}{8} = -\frac{1}{2}$.

Do đó năm số hạng đầu là: $8, -4, 2, -1, \frac{1}{2}$.

Số hạng thứ 100 là: $u_{100} = u_1 \cdot q^{99} = 8 \cdot \left(-\frac{1}{2}\right)^{99} = -\frac{1}{2^{96}}$.

Ví dụ 4. Cho một cấp số nhân gồm các số hạng dương. Biết số hạng thứ 10 bằng 1 536 và số hạng thứ 12 bằng 6 144. Tìm số hạng thứ 20 của cấp số nhân đó.

Giải

Giả sử $u_1$ là số hạng đầu và $q$ là công bội của cấp số nhân đã cho. Ta có:
$\begin{cases}
u_{10} = u_1 \cdot q^9 = 1 536 \\
u_{12} = u_1 \cdot q^{11} = 6 144.
\end{cases}$

Từ đây suy ra $q^2 = 4$, tức là $q = 2$ hoặc $q = -2$.

Với $q = 2$, ta tính được $u_1 = 3$.

Với $q = -2$ ta tính được $u_1 = -3$ (trường hợp này loại vì $u_1 > 0$ theo giả thiết).