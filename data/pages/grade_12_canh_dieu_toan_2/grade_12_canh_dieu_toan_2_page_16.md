a) Viết công thức xác định hàm số h(t).

b) Mực nước trong hồ chứa cao nhất và thấp nhất bằng bao nhiêu (làm tròn kết quả đến hàng phần mười của mét)?

c) Mực nước trong hồ chứa thay đổi nhanh nhất khi nào? Tốc độ thay đổi của mực nước trong hồ chứa khi đó là bao nhiêu?

Giải

a) Ta có: $\int h'(t)dt = \int \frac{1}{216}(5t^2 - 120t + 480)dt = \frac{1}{216}\int(5t^2 - 120t + 480)dt$

$= \frac{5}{216}\int t^2dt - \frac{120}{216}\int tdt + \frac{480}{216}\int dt = \frac{5}{648}t^3 - \frac{5}{18}t^2 + \frac{20}{9}t + C.$

Suy ra $h(t) = \frac{5}{648}t^3 - \frac{5}{18}t^2 + \frac{20}{9}t + C.$

Tại thời điểm $t = 0$, mực nước trong hồ chứa là 6 m nên $h(0) = 6$, suy ra $C = 6$.

Vậy mực nước trong hồ chứa được cho bởi hàm số:

$h(t) = \frac{5}{648}t^3 - \frac{5}{18}t^2 + \frac{20}{9}t + 6 (0 \leq t \leq 24).$

b) Ta tìm $\min_{[0;24]} h(t)$ và $\max_{[0;24]} h(t)$.

• $h'(t) = 0 \Leftrightarrow 5t^2 - 120t + 480 = 0$

$\Leftrightarrow t^2 - 24t + 96 = 0 \Leftrightarrow t = 12 - 4\sqrt{3}$ hoặc $t = 12 + 4\sqrt{3}$.

• Bảng biến thiên:

[Bảng biến thiên được mô tả như sau:
- Cột 1 (t): 0, $12 - 4\sqrt{3}$, $12 + 4\sqrt{3}$, 24
- Cột 2 (h'(t)): +, 0, -, 0, +
- Cột 3 (h(t)): Bắt đầu từ 6, tăng lên $h(12 - 4\sqrt{3}) \approx 11,1$, giảm xuống $h(12 + 4\sqrt{3}) \approx 0,9$, rồi tăng lên 6]

Do đó, ta có: $\min_{[0;24]} h(t) = \min\{h(0); h(12 + 4\sqrt{3})\} = h(12 + 4\sqrt{3}) \approx 0,9$;

$\max_{[0;24]} h(t) = \max\{h(24); h(12 - 4\sqrt{3})\} = h(12 - 4\sqrt{3}) \approx 11,1$

Vậy mực nước trong hồ chứa cao nhất khoảng 11,1 m và thấp nhất khoảng 0,9 m.

14

Đọc bản mới nhất trên hoc10.vn