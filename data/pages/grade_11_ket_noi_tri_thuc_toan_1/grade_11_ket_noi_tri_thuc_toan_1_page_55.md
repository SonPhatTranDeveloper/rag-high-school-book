Do đó $u_1 = 3$ và $q = 2$.

Vậy số hạng thứ 20 của cấp số nhân đã cho là $u_{20} = u_1 \cdot q^{19} = 3 \cdot 2^{19} = 1572864$.

Luyện tập 2. Trong một lọ nuôi cấy vi khuẩn, ban đầu có 5 000 con vi khuẩn và số lượng vi khuẩn tăng lên thêm 8% mỗi giờ. Hỏi sau 5 giờ thì số lượng vi khuẩn là bao nhiêu?

# 3. TỔNG CỦA n SỐ HẠNG ĐẦU CỦA MỘT CẤP SỐ NHÂN

HD3. Xây dựng công thức tính tổng n số hạng đầu của cấp số nhân

Cho cấp số nhân $(u_n)$ với số hạng đầu $u_1 = a$ và công bội $q = 1$.

Để tính tổng của n số hạng đầu

$S_n = u_1 + u_2 + ... + u_{n-1} + u_n$,

thực hiện lần lượt các yêu cầu sau:

a) Biểu diễn mỗi số hạng trong tổng trên theo $u_1$ và $q$ để được biểu thức tính tổng $S_n$ chỉ chứa $u_1$ và $q$.

b) Từ kết quả phần a, nhân cả hai vế với $q$ để được biểu thức tính tích $q \cdot S_n$ chỉ chứa $u_1$ và $q$.

c) Trừ từng vế hai đẳng thức nhận được ở a và b và giản ước các số hạng đồng dạng để tính $(1-q)S_n$ theo $u_1$ và $q$. Từ đó suy ra công thức tính $S_n$.

Cho cấp số nhân $(u_n)$ với công bội $q \neq 1$. Đặt $S_n = u_1 + u_2 + ... + u_n$. Khi đó

$S_n = \frac{u_1(1-q^n)}{1-q}$

Nếu cấp số nhân có công bội $q = 1$ thì tổng n số hạng đầu $S_n$ của nó bằng bao nhiêu?

Ví dụ 5. Giải bài toán ở tình huống mở đầu.

Giải

Lương hàng năm (triệu đồng) của chuyên gia lập thành một cấp số nhân, với số hạng đầu $u_1 = 240$ và công bội $q = 1,05$. Tổng số lương của chuyên gia đó sau 10 năm chính là tổng của 10 số hạng đầu của cấp số nhân này và bằng

$S_{10} = \frac{u_1(1-q^{10})}{1-q} = \frac{240[1-(1,05)^{10}]}{1-1,05} \approx 3019$.

Vậy tổng số lương (làm tròn đến triệu đồng) của chuyên gia đó sau 10 năm là 3 019 triệu đồng hay 3,019 tỉ đồng.

Ví dụ 6. Cần lấy tổng của bao nhiêu số hạng đầu của cấp số nhân 2, 6, 18, ... để được kết quả bằng 728?