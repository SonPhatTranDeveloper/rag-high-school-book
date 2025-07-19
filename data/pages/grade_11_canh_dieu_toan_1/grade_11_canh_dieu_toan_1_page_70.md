Ví dụ 2 Tính:

a) $\lim_{x \to 2} (x^2 + x - 6)$;    b) $\lim_{x \to 1} \frac{x^2 + 2x + 3}{2x - 1}$

Giải

a) $\lim_{x \to 2} (x^2 + x - 6) = \lim_{x \to 2} x^2 + \lim_{x \to 2} x - \lim_{x \to 2} 6$
   $= 4 + 2 - 6 = 0$.

b) $\lim_{x \to 1} \frac{x^2 + 2x + 3}{2x - 1} = \frac{\lim_{x \to 1} (x^2 + 2x + 3)}{\lim_{x \to 1} (2x - 1)} = \frac{\lim_{x \to 1} x^2 + \lim_{x \to 1} (2x) + \lim_{x \to 1} 3}{\lim_{x \to 1} (2x) - \lim_{x \to 1} 1} = \frac{1 + 2 + 3}{2 - 1} = 6$.

2 Tính:

a) $\lim_{x \to 2} [(x + 1)(x^2 + 2x)]$;

b) $\lim_{x \to 2} \sqrt{x^2 + x + 3}$.

3. Giới hạn một phía

Cho hàm số $f(x) = \begin{cases} -1 \text{ nếu } x < 0 \\ 0 \text{ nếu } x = 0 \\ 1 \text{ nếu } x > 0. \end{cases}$

Hàm số $f(x)$ có đồ thị ở Hình 6.

[Hình 6: Đồ thị hàm số f(x) với trục tọa độ Oxy. Đồ thị gồm 3 phần: đường thẳng nằm ngang ở y = -1 khi x < 0, điểm (0,0), và đường thẳng nằm ngang ở y = 1 khi x > 0.]

a) Xét dãy số $(u_n)$ sao cho $u_n < 0$ và $\lim u_n = 0$.
   Xác định $f(u_n)$ và tìm $\lim f(u_n)$.
b) Xét dãy số $(v_n)$ sao cho $v_n > 0$ và $\lim v_n = 0$.
   Xác định $f(v_n)$ và tìm $\lim f(v_n)$.

Nhận xét
• Ở câu a, ta xét giới hạn của hàm $f(x)$ khi $x$ tiến tới 0 về bên trái. Giới hạn đó là giới hạn bên trái của hàm số $y = f(x)$ khi $x \to 0$.
• Ở câu b, ta xét giới hạn của hàm $f(x)$ khi $x$ tiến tới 0 về bên phải. Giới hạn đó là giới hạn bên phải của hàm số $y = f(x)$ khi $x \to 0$.

Trong trường hợp tổng quát, ta có các định nghĩa sau:

• Cho hàm số $y = f(x)$ xác định trên khoảng $(a ; x_0)$.
  Số $L$ được gọi là giới hạn bên trái của hàm số $y = f(x)$ khi $x \to x_0$ nếu với dãy số $(x_n)$ bất kì, $a < x_n < x_0$ và $x_n \to x_0$, ta có $f(x_n) \to L$.
  Kí hiệu $\lim_{x \to x_0^-} f(x) = L$.

• Cho hàm số $y = f(x)$ xác định trên khoảng $(x_0 ; b)$.
  Số $L$ được gọi là giới hạn bên phải của hàm số $y = f(x)$ khi $x \to x_0$ nếu với dãy số $(x_n)$ bất kì, $x_0 < x_n < b$ và $x_n \to x_0$, ta có $f(x_n) \to L$.
  Kí hiệu $\lim_{x \to x_0^+} f(x) = L$.