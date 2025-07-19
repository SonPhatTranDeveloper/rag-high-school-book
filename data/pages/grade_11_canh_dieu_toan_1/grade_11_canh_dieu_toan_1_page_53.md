Cho cấp số cộng (un) có số hạng đầu u1 và công sai d. Đặt $S_n = u_1 + u_2 + u_3 + ... + u_n$.
Khi đó:
$S_n = \frac{(u_1 + u_n)n}{2}$.

Nhận xét: Do $u_n = u_1 + (n - 1)d$ nên $u_1 + u_n = 2u_1 + (n - 1)d$. Suy ra $S_n = \frac{[2u_1 + (n - 1)d]n}{2}$.

Ví dụ 4 Tính tổng: $S = 1 + 5 + 9 + 13 + ... + 97$.

Giải
Ta thấy dãy số 1, 5, 9, ..., 97 là cấp số cộng có số hạng đầu $u_1 = 1$, số hạng cuối $u_n = 97$, công sai $d = 4$. Vì thế, số các số hạng của cấp số cộng trên là:

$n = \frac{u_n - u_1}{d} + 1 = \frac{97 - 1}{4} + 1 = 25$.

Vậy $S = \frac{(1 + 97) \cdot 25}{2} = 1225$.

Ví dụ 5 Một nhà thi đấu có 20 hàng ghế dành cho khán giả. Hàng thứ nhất có 20 ghế, hàng thứ hai có 21 ghế, hàng thứ ba có 22 ghế, ... Cứ như thế, số ghế ở hàng sau nhiều hơn số ghế ở hàng trước là 1 ghế. Trong một giải thi đấu, ban tổ chức đã bán được hết số vé phát ra và số tiền thu được từ bán vé là 70 800 000 đồng. Tính giá tiền của mỗi vé (đơn vị: đồng), biết số vé bán ra bằng số ghế dành cho khán giả của nhà thi đấu và các vé là đồng giá.

Giải
Số ghế ở mỗi hàng lập thành một cấp số cộng có số hạng đầu $u_1 = 20$, công sai $d = 1$.
Cấp số cộng này có 20 số hạng.

Do đó, tổng số ghế trong nhà thi đấu là: $S_{20} = \frac{[2 \cdot 20 + (20 - 1) \cdot 1] \cdot 20}{2} = 590$.

Vì số vé bán ra bằng số ghế dành cho khán giả của nhà thi đấu nên số vé bán ra là 590.

Vậy giá tiền của một vé là: 70 800 000 : 590 = 120 000 (đồng).

BÀI TẬP

1. Trong các dãy số sau, dãy số nào là cấp số cộng? Vì sao?
   a) 10, - 2, - 14, - 26, - 38;
   b) $\frac{1}{2}, \frac{5}{4}, 2, \frac{11}{4}, \frac{7}{2}$;
   c) $\sqrt{1}, \sqrt{2}, \sqrt{3}, \sqrt{4}, \sqrt{5}$;
   d) 1, 4, 7, 10, 13.

4 Tính tổng n số hạng đầu của mỗi cấp số cộng sau:
a) 3, 1, - 1, ... với n = 10;
b) 1,2; 1,7; 2,2; ...
với n = 15.