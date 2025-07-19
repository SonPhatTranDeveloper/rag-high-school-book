Ví dụ 2. Cho dãy số $(u_n)$ với $u_n = 5n - 1$. Chứng minh rằng $(u_n)$ là một cấp số cộng. Tìm số hạng đầu $u_1$ và công sai d của nó.

Giải

Ta có $u_n - u_{n-1} = (5n - 1) - [5(n-1) - 1] = 5$, với mọi $n \geq 2$.

Do đó $(u_n)$ là cấp số cộng có số hạng đầu $u_1 = 5 \cdot 1 - 1 = 4$ và công sai $d = 5$.

Luyện tập 1. Cho dãy số $(u_n)$ với $u_n = -2n + 3$. Chứng minh rằng $(u_n)$ là một cấp số cộng. Xác định số hạng đầu và công sai của cấp số cộng này.

2. SỐ HẠNG TỔNG QUÁT

HD2. Công thức số hạng tổng quát của cấp số cộng

Cho cấp số cộng $(u_n)$ với số hạng đầu $u_1$ và công sai $d$.

a) Tính các số hạng $u_2, u_3, u_4, u_5$ theo $u_1$ và $d$.

b) Dự đoán công thức tính số hạng tổng quát $u_n$ theo $u_1$ và $d$.

Nếu cấp số cộng $(u_n)$ có số hạng đầu $u_1$ và công sai $d$ thì số hạng tổng quát $u_n$ của nó được xác định theo công thức

$u_n = u_1 + (n-1)d$.

Ví dụ 3. Tìm năm số hạng đầu và số hạng thứ 100 của cấp số cộng $(u_n)$: 10, 5, ...

Giải

Cấp số cộng này có số hạng đầu $u_1 = 10$ và công sai $d = -5$.
Do đó năm số hạng đầu là: 10, 5, 0, -5, -10.
Số hạng thứ 100 là $u_{100} = u_1 + (100 - 1)d = 10 + 99 \cdot (-5) = -485$.

Ví dụ 4. Số hạng thứ 10 của một cấp số cộng $(u_n)$ bằng 48 và số hạng thứ 18 bằng 88. Tìm số hạng thứ 100 của cấp số cộng đó.

Giải

Giả sử $u_1$ là số hạng đầu và $d$ là công sai của cấp số cộng đó. Ta có:
$u_{10} = u_1 + 9d = 48$
$u_{18} = u_1 + 17d = 88$.

Giải hệ này ta được $u_1 = 3$ và $d = 5$.

Vậy số hạng thứ 100 của cấp số cộng này là $u_{100} = u_1 + 99d = 3 + 99 \cdot 5 = 498$.

Luyện tập 2. Cho dãy số $(u_n)$ với $u_n = 4n - 3$. Chứng minh rằng $(u_n)$ là một cấp số cộng. Xác định số hạng đầu $u_1$ và công sai $d$ của cấp số cộng này. Từ đó viết số hạng tổng quát $u_n$ dưới dạng $u_n = u_1 + (n-1)d$.