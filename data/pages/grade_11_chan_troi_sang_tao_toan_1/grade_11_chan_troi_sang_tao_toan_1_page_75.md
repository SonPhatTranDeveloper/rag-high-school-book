Nhận xét:
a) $\lim_{x \to x_0} x^k = x_0^k$, k là số nguyên dương;

b) $\lim_{x \to x_0} [cf(x)] = c \lim_{x \to x_0} f(x) (c \in \mathbb{R}, \text{nếu tồn tại} \lim_{x \to x_0} f(x) \in \mathbb{R})$.

Ví dụ 2. Tìm các giới hạn sau: a) $\lim_{x \to 1} (x^2 - 4x + 2)$; b) $\lim_{x \to 2} \frac{3x-2}{2x+1}$.

Giải

a) $\lim_{x \to 1} (x^2 - 4x + 2) = \lim_{x \to 1} x^2 - \lim_{x \to 1} (4x) + \lim_{x \to 1} 2 = 1^2 - 4 \lim_{x \to 1} x + 2 = 1 - 4 \cdot 1 + 2 = -1$.

b) $\lim_{x \to 2} \frac{3x-2}{2x+1} = \frac{\lim_{x \to 2}(3x-2)}{\lim_{x \to 2}(2x+1)} = \frac{3 \lim_{x \to 2} x - 2}{2 \lim_{x \to 2} x + 1} = \frac{3 \cdot 2 - 2}{2 \cdot 2 + 1} = \frac{4}{5}$.

Ví dụ 3: Tìm các giới hạn sau: a) $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$; b) $\lim_{x \to 3} \frac{\sqrt{x+1}-2}{x-3}$.

Giải

a) $\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2} (x+2) = \lim_{x \to 2} x + \lim_{x \to 2} 2 = 2 + 2 = 4$.

b) $\lim_{x \to 3} \frac{\sqrt{x+1}-2}{x-3} = \lim_{x \to 3} \frac{(\sqrt{x+1}-2)(\sqrt{x+1}+2)}{(x-3)(\sqrt{x+1}+2)}$ (nhân cả tử và mẫu với $\sqrt{x+1}+2$)

$= \lim_{x \to 3} \frac{(x+1)-4}{(x-3)(\sqrt{x+1}+2)} = \lim_{x \to 3} \frac{1}{(\sqrt{x+1}+2)}$

$= \frac{1}{\lim_{x \to 3} (\sqrt{x+1}+2)} = \lim_{x \to 3} \frac{1}{\sqrt{x+1}+2}$

$= \frac{1}{\sqrt{\lim_{x \to 3} (x+1)}+2} = \frac{1}{\sqrt{\lim_{x \to 3} x+1+2}} = \frac{1}{\sqrt{3+1+2}} = \frac{1}{4}$

Tìm các giới hạn sau: a) $\lim_{x \to 2} (x^2 + 5x - 2)$; b) $\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$.

3. Giới hạn một phía

Giá cước vận chuyển bưu kiện giữa hai thành phố do một đơn vị cung cấp được cho bởi bảng sau:

| Khối lượng bưu kiện (100 gam) | Giá cước căn vứng (nghìn đồng) |
|-------------------------------|--------------------------------|
| đến 1                         | 6                              |
| trên 1 đến 2,5                | 7                              |
| từ 2,5 đến 5                  | 10                             |
| ...                           | ...                            |