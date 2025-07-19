Toán học cho phép thiết lập công thức xác định vị trí của thiết bị theo vị trí của các vệ tinh và khoảng cách tương ứng, nhờ đó có thể lập trình tính toán xác định vị trí của thiết bị. Ta hãy xét một trường hợp cụ thể sau đây:

Trong không gian Oxyz, giả sử tại một thời điểm, một thiết bị GPS xác định được khoảng cách từ nó tới ba vệ tinh A, B, C tương ứng là $\sqrt{5}, \sqrt{2}, 2$. Tại thời điểm đó, các vệ tinh trên ở vị trí có tọa độ là $A(2;0;0), B(0;2;0), C\left(0;\frac{11}{4};\frac{\sqrt{7}}{4}\right)$. Từ thông tin trên, ta hoàn toàn có thể xác định tọa độ cũng như vĩ độ và kinh độ của vị trí thiết bị GPS.

• Giả sử tại thời điểm đã cho, thiết bị GPS ở vị trí $P(x;y;z)$.

Do thiết bị thuộc mặt đất và $PA = \sqrt{5}$ nên

$x^2 + y^2 + z^2 = 1$ (1) và $(x - 2)^2 + y^2 + z^2 = 5$ (2).

Trừ vế theo vế của (1) và (2), ta được $4x - 4 = -4$. Vậy $x = 0$.

Do $PB = \sqrt{2}$ nên $x^2 + (y - 2)^2 + z^2 = 2$ (3).

Trừ vế theo vế của (1) và (3), ta được ta được $4y - 4 = -1$. Vậy $y = \frac{3}{4}$.

Thay $x = 0, y = \frac{3}{4}$ vào phương trình (1), ta được $0^2 + \frac{9}{16} + z^2 = 1$.

Suy ra $z = \frac{\sqrt{7}}{4}$ hoặc $z = -\frac{\sqrt{7}}{4}$. Kiểm tra điều kiện $PC = 2$, ta thấy chỉ có điểm $P\left(0;\frac{3}{4};\frac{\sqrt{7}}{4}\right)$ thỏa mãn.

• Vị trí P của GPS có tung độ dương nên thuộc bán cầu Đông và có cao độ dương nên thuộc bán cầu Bắc. Gọi vĩ độ, kinh độ của P tương ứng là $\alpha°N, \beta°E (0 < \alpha < 90, 0 < \beta < 180)$. Khi đó $P(\cos\alpha°\cos\beta°; \cos\alpha°\sin\beta°; \sin\alpha°)$.

Mặt khác, ta có $P\left(0;\frac{3}{4};\frac{\sqrt{7}}{4}\right)$ nên $\sin\alpha° = \frac{\sqrt{7}}{4}$. Do đó $\alpha ≈ 41,4096$.

Ta có $\cos\alpha° ≠ 0$ và $\cos\alpha°\cos\beta° = 0$ nên $\cos\beta° = 0$.

Vậy $\beta = 90$ và do đó vị trí của GPS (xấp xỉ) là 41,4096°N, 90°E.