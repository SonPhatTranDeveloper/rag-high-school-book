b) Cho hàm số $y = f(x)$ xác định trên khoảng $(-\infty; a)$.
Ta nói hàm số $y = f(x)$ có giới hạn là số $L$ khi $x \to -\infty$ nếu với dãy số $(x_n)$ bất kì, $x_n < a$ và $x_n \to -\infty$, ta có $f(x_n) \to L$.
Kí hiệu $\lim_{x \to -\infty} f(x) = L$ hay $f(x) \to L$ khi $x \to -\infty$.

Chú ý

• Với $c, k$ là các hằng số và $k$ nguyên dương, ta luôn có:
$\lim_{x \to +\infty} c = c$; $\lim_{x \to -\infty} c = c$; $\lim_{x \to +\infty} \frac{c}{x^k} = 0$; $\lim_{x \to -\infty} \frac{c}{x^k} = 0$.

• Các phép toán trên giới hạn hữu hạn của hàm số khi $x \to x_0$ vẫn còn đúng khi $x \to +\infty$ hoặc $x \to -\infty$.

Ví dụ 5 Tính $\lim_{x \to +\infty} \frac{2x+1}{x-1}$.

Giải

Ta có: $\lim_{x \to +\infty} \frac{2x+1}{x-1} = \lim_{x \to +\infty} \frac{x(2+\frac{1}{x})}{x(1-\frac{1}{x})} = \lim_{x \to +\infty} \frac{2+\frac{1}{x}}{1-\frac{1}{x}} = \frac{\lim_{x \to +\infty} 2+ \lim_{x \to +\infty} \frac{1}{x}}{\lim_{x \to +\infty} 1- \lim_{x \to +\infty} \frac{1}{x}} = \frac{2+0}{1-0} = 2$.

4 Tính $\lim_{x \to -\infty} \frac{3x+2}{4x-5}$.

III. GIỚI HẠN VÔ CỰC (MỘT PHÍA) CỦA HÀM SỐ TẠI MỘT ĐIỂM

5 Cho hàm số $f(x) = \frac{1}{x-1}$ $(x \neq 1)$ có đồ thị như Hình 8. Quan sát đồ thị đó và cho biết:

a) Khi biến $x$ dần tới 1 về bên phải thì $f(x)$ dần tới đâu.

b) Khi biến $x$ dần tới 1 về bên trái thì $f(x)$ dần tới đâu.

Trong trường hợp tổng quát, ta có định nghĩa sau:

• Cho hàm số $y = f(x)$ xác định trên khoảng $(a; +\infty)$.
Ta nói hàm số $y = f(x)$ có giới hạn là $+\infty$ khi $x \to a^+$ nếu với dãy số $(x_n)$ bất kì, $x_n > a$ và $x_n \to a$, ta có $f(x_n) \to +\infty$.
Kí hiệu $\lim_{x \to a^+} f(x) = +\infty$ hay $f(x) \to +\infty$ khi $x \to a^+$.

• Các trường hợp $\lim_{x \to a^+} f(x) = -\infty$; $\lim_{x \to a^-} f(x) = +\infty$; $\lim_{x \to a^-} f(x) = -\infty$ được định nghĩa tương tự.

[Hình 8: Đồ thị hàm số $f(x) = \frac{1}{x-1}$ với trục tọa độ Oxy. Đồ thị là một đường cong tiệm cận với trục y tại $x=1$, và tiệm cận với trục x khi $x$ tiến đến vô cực.]