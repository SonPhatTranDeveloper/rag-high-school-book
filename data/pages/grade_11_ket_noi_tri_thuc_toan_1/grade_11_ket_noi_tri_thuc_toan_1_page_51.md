3. TỔNG n SỐ HẠNG ĐẦU CỦA MỘT CẤP SỐ CỘNG

H63. Xây dựng công thức tính tổng n số hạng đầu của cấp số cộng

Cho cấp số cộng $(u_n)$ với số hạng đầu $u_1$ và công sai d.
Để tính tổng của n số hạng đầu

$S_n = u_1 + u_2 + ... + u_{n-1} + u_n$,

hãy lần lượt thực hiện các yêu cầu sau:

a) Biểu diễn mỗi số hạng trong tổng $S_n$ theo số hạng đầu $u_1$ và công sai d.

b) Viết $S_n$ theo thứ tự ngược lại: $S_n = u_n + u_{n-1} + ... + u_2 + u_1$ và sử dụng kết quả ở phần a) để biểu diễn mỗi số hạng trong tổng này theo $u_1$ và d.

c) Cộng từng vế hai đẳng thức nhận được ở a), b), để tính $S_n$ theo $u_1$ và d.

Cho cấp số cộng $(u_n)$ với công sai d. Đặt $S_n = u_1 + u_2 + ... + u_n$. Khi đó

$S_n = \frac{n}{2}[2u_1 + (n-1)d]$.

Chú ý. Sử dụng công thức $u_n = u_1 + (n-1)d$, ta có thể viết tổng $S_n$ dưới dạng

$S_n = \frac{n(u_1 + u_n)}{2}$

Ví dụ 5. Giải bài toán ở tình huống mở đầu.

Giải. Số ghế ở mỗi hàng của nhà hát lập thành một cấp số cộng, gồm 25 số hạng, với số hạng đầu $u_1 = 16$ và công sai $d = 2$. Tổng các số hạng này là

$S_{25} = u_1 + u_2 + ... + u_{25} = \frac{25}{2}[2u_1 + (25-1)d] = \frac{25}{2}[2 \cdot 16 + 24 \cdot 2] = 1000$.

Vậy nhà hát đó có tổng cộng 1 000 ghế.

Ví dụ 6. Cần lấy tổng của bao nhiêu số hạng đầu của cấp số cộng 2, 5, 8, ... để được kết quả bằng 345?

Giải

Cấp số cộng này có số hạng đầu $u_1 = 2$ và công sai $d = 3$. Gọi n là số các số hạng đầu của cấp số cộng cần lấy tổng, ta có

$345 = S_n = \frac{n}{2}[2u_1 + (n-1)d] = \frac{n}{2}[2 \cdot 2 + (n-1) \cdot 3] = \frac{n}{2}(3n + 1)$.

Do đó $3n^2 + n - 690 = 0$. Giải phương trình bậc hai này ta được $n = \frac{230}{15}$ (loại) và $n = 15$.

Vậy phải lấy tổng của 15 số hạng đầu của cấp số cộng đã cho để được tổng bằng 345.

Vận dụng. Anh Nam được nhận vào làm việc ở một công ty về công nghệ với mức lương khởi điểm là 100 triệu đồng một năm. Công ty sẽ tăng thêm lương cho anh Nam mỗi năm là 20 triệu đồng. Tính tổng số tiền lương mà anh Nam nhận được sau 10 năm làm việc cho công ty đó.