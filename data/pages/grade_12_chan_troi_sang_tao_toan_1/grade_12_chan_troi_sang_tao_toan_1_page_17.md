Một cách tổng quát, cho hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$ và có đạo hàm trên $(a; b)$ (có thể trừ một số hữu hạn các điểm) và $f'(x) = 0$ chỉ tại một số hữu hạn các điểm trong $(a; b)$, ta có thể tìm giá trị lớn nhất và giá trị nhỏ nhất của $f(x)$ trên đoạn $[a; b]$ theo các bước như sau:

Bước 1. Tìm các điểm $x_1; x_2; ...; x_n$ thuộc khoảng $(a; b)$ mà tại đó $f'(x)$ bằng 0 hoặc không tồn tại.

Bước 2. Tính $f(a); f(x_1); f(x_2); ...; f(x_n); f(b)$.

Bước 3. Gọi $M$ là số lớn nhất và $m$ là số nhỏ nhất trong các giá trị tìm được ở Bước 2.

Khi đó:

$M = \max_{[a;b]} f(x), m = \min_{[a;b]} f(x)$.

Ví dụ 3. Tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số $f(x) = x^4 - 8x^2 + 9$ trên đoạn $[-1; 3]$.

Giải

Ta có: $f'(x) = 4x^3 - 16x$;

$f'(x) = 0 \Rightarrow x = 0$ hoặc $x = 2$ hoặc $x = -2$ (loại vì không thuộc $[-1; 3]$);

$f(-1) = 2; f(0) = 9; f(2) = -7; f(3) = 18$.

Vậy $\max_{[-1,3]} f(x) = f(3) = 18$ và $\min_{[-1,3]} f(x) = f(2) = -7$.

Ví dụ 4. Từ một tấm bìa hình chữ nhật có chiều rộng 30 cm và chiều dài 80 cm (Hình 4a), người ta cắt ở bốn góc bốn hình vuông có cạnh $x$ (cm) với $5 \leq x \leq 10$ và gấp lại để tạo thành chiếc hộp có dạng hình hộp chữ nhật không nắp như Hình 4b. Tìm $x$ để thể tích chiếc hộp là lớn nhất (kết quả làm tròn đến hàng phần trăm).

[Hình minh họa cho bài toán, gồm hai phần a) và b) mô tả tấm bìa ban đầu và hình dạng hộp sau khi gấp]

Giải

Thể tích chiếc hộp là: $V(x) = x(30 - 2x)(80 - 2x) = 2 400x - 220x^2 + 4x^3$ với $5 \leq x \leq 10$.

Ta có: $V'(x) = 12x^2 - 440x + 2 400$;

$V'(x) = 0 \Rightarrow x = \frac{20}{3}$ hoặc $x = 30$ (loại vì không thuộc $[5; 10]$);

$V(5) = 7 000; V\left(\frac{20}{3}\right) = \frac{200 000}{27}; V(10) = 6 000$.