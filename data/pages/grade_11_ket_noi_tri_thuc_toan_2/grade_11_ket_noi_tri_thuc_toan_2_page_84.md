Trong thực hành, ta thường trình bày ngắn gọn như sau:

$f'(1) = \lim_{x \to 1} \frac{f(x) - f(1)}{x-1} = \lim_{x \to 1} \frac{(x^2 + 2x) - 3}{x-1}$

$= \lim_{x \to 1} \frac{(x-1)(x+3)}{x-1} = \lim_{x \to 1} (x+3) = 4.$

Chú ý: Đặt $h = x - x_0$, khi đó đạo hàm của hàm số đã cho tại điểm $x_0 = 1$ có thể tính như sau:

$f'(1) = \lim_{h \to 0} \frac{f(1+h) - f(1)}{h} = \lim_{h \to 0} \frac{[(1+h)^2 + 2(1+h)] - (1^2 + 2)}{h}$

$= \lim_{h \to 0} \frac{(h^2 + 4h + 3) - 3}{h} = \lim_{h \to 0} (h + 4) = 4.$

[Hình ảnh minh họa một robot đang chỉ vào công thức: $f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$]

Luyện tập 1. Tính đạo hàm của hàm số $y = -x^2 + 2x + 1$ tại điểm $x_0 = -1$.

3. ĐẠO HÀM CỦA HÀM SỐ TRÊN MỘT KHOẢNG

HĐ3. Tính đạo hàm $f'(x_0)$ tại điểm $x_0$ bất kì trong các trường hợp sau:

a) $f(x) = c$ (c là hằng số);
b) $f(x) = x$.

Hàm số $y = f(x)$ được gọi là có đạo hàm trên khoảng $(a; b)$ nếu nó có đạo hàm $f'(x)$ tại mọi điểm $x$ thuộc khoảng đó, kí hiệu là $y' = f'(x)$.

Ví dụ 2. Tìm đạo hàm của hàm số $y = cx^2$, với c là hằng số.

[Hình ảnh minh họa công thức: $(c)' = 0; (x)' = 1; (cx^2)' = 2cx.$]

Giải
Với $x_0$ bất kì, ta có:

$f'(x_0) = \lim_{x \to x_0} \frac{cx^2 - cx_0^2}{x - x_0} = \lim_{x \to x_0} \frac{c(x - x_0)(x + x_0)}{x - x_0}$

$= \lim_{x \to x_0} c(x + x_0) = c(x_0 + x_0) = 2cx_0.$

Vậy hàm số $y = cx^2$ (với c là hằng số) có đạo hàm là hàm số $y' = 2cx$.

[Hình ảnh minh họa một nhân vật đang giơ ngón tay cái lên]

Chú ý: Nếu phương trình chuyển động của vật là $s = f(t)$ thì $v(t) = f'(t)$ là vận tốc tức thời của vật tại thời điểm t.