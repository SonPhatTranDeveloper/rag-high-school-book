Bài 1. Giới hạn của dãy số

Từ khóa: Giới hạn hữu hạn của dãy số; Tổng của cấp số nhân lùi vô hạn.

[Hình minh họa: Ba học sinh đang thảo luận về một vấn đề toán học. Một học sinh nói: "Số thập phân vô hạn tuần hoàn 0,666... và số $\frac{2}{3}$ là hai số bằng nhau." Học sinh khác đáp: "Không thể như vậy được, vì $0,6 < \frac{2}{3}; 0,66 < \frac{2}{3}; 0,666 < \frac{2}{3};...$" Học sinh thứ ba thắc mắc: "???"]

1. Giới hạn hữu hạn của dãy số

Giới hạn 0 của dãy số

Cho dãy số $(u_n)$ với $u_n = \frac{(-1)^n}{n}$.

a) Tìm các giá trị còn thiếu trong bảng sau:

| n | 10 | 20 | 50 | 100 | 1000 | | |
|---|----|----|----|----|------|---|---|
|$|u_n|$| 0,1 | 0,05 | 0,02 | ? | ? |

b) Với n như thế nào thì $|u_n|$ bé hơn 0,01; 0,001?

c) Một số số hạng của dãy số được biểu diễn trên trục số như Hình 1.

[Hình 1: Trục số từ -1 đến 1 với các điểm $u_1$, $u_3$, $u_5$, $u_{100}$, $u_{50}$, $u_4$, $u_2$ được đánh dấu]

Từ các kết quả trên, có nhận xét gì về khoảng cách từ điểm $u_n$ đến điểm 0 khi n trở nên rất lớn?

Ta nói dãy số $(u_n)$ có giới hạn 0 khi n dần tới dương vô cực, nếu $|u_n|$ nhỏ hơn một số dương bất kì cho trước, kể từ một số hạng nào đó trở đi, kí hiệu $\lim_{n \to +\infty} u_n = 0$ hay $u_n \to 0$ khi $n \to +\infty$. Ta còn viết là $\lim u_n = 0$.

Ví dụ 1. Với dãy số $u_n = \frac{(-1)^n}{n}$, sử dụng định nghĩa, chứng tỏ rằng $\lim u_n = 0$.

Giải

Với số thực dương d bé tùy ý cho trước, lấy số tự nhiên N sao cho $N > \frac{1}{d}$. Khi đó, với mọi số tự nhiên n sao cho $n \geq N$, ta có $|u_n| = \left|\frac{(-1)^n}{n}\right| = \frac{1}{n} \leq \frac{1}{N} < d$.

Theo định nghĩa, $\lim u_n = 0$.