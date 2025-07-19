Do tỉ lệ tăng dân số hàng năm là 1,14% nên ta có:
$u_n = u_{n-1} + u_{n-1} \cdot 0,0114 = u_{n-1} \cdot (1 + 0,0114)$
$= u_{n-1} \cdot 1,0114$ với $n \geq 2$.
Do đó, $(u_n)$ là cấp số nhân có số hạng đầu
$u_1 = 97,6 \cdot 1,0114$, công bội $q = 1,0114$.
Vậy dân số của Việt Nam sau $n$ năm kể từ năm 2020 là:
$u_n = 97,6 \cdot 1,0114 \cdot 1,0114^{n-1} = 97,6 \cdot 1,0114^n$ (triệu người).

III. TỔNG n SỐ HẠNG ĐẦU CỦA MỘT CẤP SỐ NHÂN

Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1$, công bội $q \neq 1$.
Đặt $S_n = u_1 + u_2 + u_3 + ... + u_n = u_1 + u_1q + u_1q^2 + ... + u_1q^{n-1}$.
a) Tính $S_n \cdot q$ và $S_n - S_n \cdot q$.
b) Từ đó, hãy tìm công thức tính $S_n$ theo $u_1$ và $q$.

Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1$ và công bội $q \neq 1$.
Đặt $S_n = u_1 + u_2 + u_3 + ... + u_n$. Khi đó:
$$S_n = \frac{u_1(1-q^n)}{1-q}.$$

Chú ý: Nếu $q = 1$ thì $S_n = nu_1$.

Ví dụ 5: Tính tổng: $S = 1 + \frac{1}{2} + \frac{1}{4} + ... + \frac{1}{2^9}$.
Giải
$S$ là tổng 10 số hạng đầu của cấp số nhân có
số hạng đầu $u_1 = 1$ và công bội $q = \frac{1}{2}$.
$$S = \frac{1 \cdot \left[1-\left(\frac{1}{2}\right)^{10}\right]}{1-\frac{1}{2}} = \frac{1023}{512}.$$

Ví dụ 6: Giả sử anh Tuấn kí hợp đồng lao động trong 10 năm với điều khoản về tiền lương như sau: Năm thứ nhất, tiền lương của anh Tuấn là 60 triệu. Kể từ năm thứ hai trở đi, mỗi năm tiền lương của anh Tuấn được tăng lên 8%. Tính tổng số tiền lương anh Tuấn lĩnh được trong 10 năm đi làm (đơn vị: triệu đồng, làm tròn đến hàng phần nghìn).
Giải
Gọi $u_n$ là số tiền lương (triệu đồng) anh Tuấn được lĩnh ở năm làm việc thứ $n$.
Ta có: $u_1 = 60$;

[Hình ảnh chứa một khung màu xanh lá cây với nội dung:]
3. Bác Linh gửi vào ngân hàng 100 triệu đồng tiền tiết kiệm với hình thức lãi kép, kì hạn 1 năm với lãi suất 6%/năm. Viết công thức tính số tiền (cả gốc và lãi) mà bác Linh có được sau n năm (giả sử lãi suất không thay đổi qua các năm).

[Hình ảnh chứa một khung màu xanh lá cây với nội dung:]
4. Tính tổng n số hạng đầu của mỗi cấp số nhân sau:
a) 3, -6, 12, -24, ... với n = 12;
b) $\frac{1}{10}, \frac{1}{100}, \frac{1}{1000}, ...$ với n = 5.