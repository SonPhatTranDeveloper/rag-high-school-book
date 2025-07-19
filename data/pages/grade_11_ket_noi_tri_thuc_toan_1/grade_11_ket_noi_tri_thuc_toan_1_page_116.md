Vị dụ 6. Tính $\lim_{x \to \infty} \frac{\sqrt{x^2+1}}{x}$.

Giải

Ta có $\lim_{x \to \infty} \frac{\sqrt{x^2+1}}{x} = \lim_{x \to \infty} \sqrt{\frac{x^2+1}{x^2}} = \lim_{x \to \infty} \sqrt{1+\frac{1}{x^2}}$

$= \sqrt{\lim_{x \to \infty} (1+\frac{1}{x^2})} = \sqrt{1+\lim_{x \to \infty} \frac{1}{x^2}} = 1$.

Luyện tập 3. Tính $\lim_{x \to \infty} \frac{\sqrt{x^2+2}}{x+1}$.

Vận dụng. Cho tam giác vuông OAB với A = (a; 0) và B = (0; 1) như Hình 5.5. Đường cao OH có độ dài là h.

a) Tính h theo a.

b) Khi điểm A dịch chuyển về O, điểm H thay đổi thế nào? Tại sao?

c) Khi A dịch chuyển ra vô cực theo chiều dương của trục Ox, điểm H thay đổi thế nào? Tại sao?

[Hình minh họa tam giác vuông OAB với các điểm O, A, B và H được đánh dấu. Trục tọa độ Ox và Oy cũng được thể hiện.]

3. GIỚI HẠN VÔ CỰC CỦA HÀM SỐ TẠI MỘT ĐIỂM

a) Giới hạn vô cực

H94. Nhận biết khái niệm giới hạn vô cực

Xét hàm số $f(x) = \frac{1}{x^2}$ có đồ thị như Hình 5.6.

Cho $x_n = \frac{1}{n}$, chứng tỏ rằng $f(x_n) \to +\infty$.

[Hình 5.6 minh họa đồ thị hàm số $y = \frac{1}{x^2}$]

Giả sử khoảng (a; b) chứa x₀ và hàm số y = f(x) xác định trên (a; b) \ {x₀}. Ta nói hàm số f(x) có giới hạn +∞ khi x → x₀ nếu với dãy số (x_n) bất kì, x_n ∈ (a; b) \ {x₀}, x_n → x₀, ta có f(x_n) → +∞, kí hiệu $\lim_{x \to x_0} f(x) = +\infty$.

Ta nói hàm số f(x) có giới hạn -∞ khi x → x₀, kí hiệu $\lim_{x \to x_0} f(x) = -\infty$, nếu $\lim_{x \to x_0} [-f(x)] = +\infty$.

Ví dụ 7. Tính $\lim_{x \to 1} \frac{1}{|x-1|}$.

Giải

Xét hàm số $f(x) = \frac{1}{|x-1|}$. Lấy dãy số (x_n) bất kì sao cho x_n ≠ 1, x_n → 1. Khi đó, |x_n - 1| → 0.

Do đó $f(x_n) = \frac{1}{|x_n-1|} \to +\infty$. Vậy $\lim_{x \to 1} \frac{1}{|x-1|} = +\infty$.

[Hình minh họa một nhân vật hoạt hình đang giơ ngón tay lên, kèm theo một công thức toán học: $a\sqrt{b} = \begin{cases} \sqrt{a^2b} & \text{nếu } a \geq 0 \\ -\sqrt{a^2b} & \text{nếu } a < 0. \end{cases}$]