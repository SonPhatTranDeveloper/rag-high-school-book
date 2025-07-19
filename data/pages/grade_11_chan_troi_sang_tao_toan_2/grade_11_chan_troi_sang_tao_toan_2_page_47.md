5. Đạo hàm của tổng, hiệu, tích, thương của hai hàm số

Cho $f(x)$ và $g(x)$ là hai hàm số có đạo hàm tại $x_0$. Xét hàm số $h(x) = f(x) + g(x)$.

Ta có $\frac{h(x) - h(x_0)}{x - x_0} = \frac{f(x) - f(x_0)}{x - x_0} + \frac{g(x) - g(x_0)}{x - x_0}$

nên $h'(x_0) = \lim_{x \to x_0} \frac{h(x) - h(x_0)}{x - x_0} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} + \lim_{x \to x_0} \frac{g(x) - g(x_0)}{x - x_0} = ... + ...$

Chọn biểu thức thích hợp thay cho chỗ chấm để tìm $h'(x_0)$.

Cho hai hàm số $u(x)$, $v(x)$ có đạo hàm tại điểm $x$ thuộc tập xác định. Ta có:

• $(u + v)' = u' + v'$
• $(u - v)' = u' - v'$
• $(u \cdot v)' = uv' + u'v$ (1)
• $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ (với $v = v(x) \neq 0$) (2)

Chú ý: • Với $u = C$ ($C$ là hằng số), công thức (1) trở thành $(C \cdot v)' = C \cdot v'$.
       • Với $u = 1$, công thức (2) trở thành $\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$ (với $v = v(x) \neq 0$).

Ví dụ 6. Tính đạo hàm của các hàm số sau:

a) $y = 3x^2 - 4x + 2$;        b) $y = x \sin x$;        c) $y = \frac{3x + 2}{2x - 1}$

Giải

a) $(3x^2 - 4x + 2)' = (3x^2)' - (4x)' + (2)' = 3(x^2)' - 4(x)' + 0 = 3 \cdot 2x - 4 \cdot 1 = 6x - 4$.

b) $(x \sin x)' = (x)' \sin x + x(\sin x)' = 1 \cdot \sin x + x \cdot \cos x = \sin x + x \cos x$.

c) $\left(\frac{3x + 2}{2x - 1}\right)' = \frac{(3x + 2)' \cdot (2x - 1) - (3x + 2) \cdot (2x - 1)'}{(2x - 1)^2} = \frac{3 \cdot (2x - 1) - (3x + 2) \cdot 2}{(2x - 1)^2}$

   $= \frac{6x - 3 - 6x - 4}{(2x - 1)^2} = -\frac{7}{(2x - 1)^2}$.

Ví dụ 7. Tính đạo hàm của các hàm số sau:

a) $y = x^2 3^x$;        b) $y = \frac{\sqrt{x}}{\cos x}$

Giải

a) $(x^2 3^x)' = (x^2)' \cdot 3^x + x^2 \cdot (3^x)' = 2x \cdot 3^x + x^2 \cdot 3^x \cdot \ln 3 = x 3^x(2 + x \ln 3)$.

b) $\left(\frac{\sqrt{x}}{\cos x}\right)' = \frac{(\sqrt{x})' \cdot \cos x - \sqrt{x} \cdot (\cos x)'}{cos^2 x} = \frac{\frac{1}{2\sqrt{x}} \cos x - \sqrt{x}(-\sin x)}{\cos^2 x} = \frac{\cos x + 2x \sin x}{2\sqrt{x} \cos^2 x}$.