# H01. Diện tích của hình thang

Kí hiệu $T$ là hình thang vuông giới hạn bởi đường thẳng $y = x + 1$, trục hoành và hai đường thẳng $x = 1$, $x = t$ $(1 \leq t \leq 4)$ (H.4.3).

a) Tính diện tích $S$ của $T$ khi $t = 4$.

b) Tính diện tích $S(t)$ của $T$ khi $t \in [1; 4]$.

c) Chứng minh rằng $S(t)$ là một nguyên hàm của hàm số $f(t) = t + 1$, $t \in [1; 4]$ và diện tích $S = S(4) - S(1)$.

[Hình 4.3: Đồ thị biểu diễn hình thang T với trục tọa độ Oxy. Trục y có giá trị từ -1 đến 5, trục x từ -1 đến 6. Hình thang được giới hạn bởi đường thẳng y = x + 1, trục hoành, và hai đường thẳng x = 1 và x = t. Diện tích S(t) được tô màu.]

# H02. Diện tích của hình thang cong

Xét hình thang cong giới hạn bởi đồ thị $y = x^2$, trục hoành và hai đường thẳng $x = 1$, $x = 2$.

Ta muốn tính diện tích $S$ của hình thang cong này.

a) Với mỗi $x \in [1; 2]$, gọi $S(x)$ là diện tích phần hình thang cong đã cho nằm giữa hai đường thẳng vuông góc với trục $Ox$ tại điểm có hoành độ bằng 1 và $x$ (H.4.5).

Cho $h > 0$ sao cho $x + h < 2$. So sánh hiệu $S(x + h) - S(x)$ với diện tích hai hình chữ nhật $MNPQ$ và $MNEF$ (H.4.6). Từ đó suy ra

$$0 \leq \frac{S(x+h) - S(x)}{h} - x^2 \leq 2xh + h^2.$$

b) Cho $h < 0$ sao cho $x + h > 1$. Tương tự phần a, đánh giá hiệu $S(x) - S(x + h)$ và từ đó suy ra

$$2xh + h^2 \leq \frac{S(x+h) - S(x)}{h} - x^2 \leq 0.$$

c) Từ kết quả phần a và phần b, suy ra với mọi $h \neq 0$, ta có

$$\left|\frac{S(x+h) - S(x)}{h} - x^2\right| \leq 2|x||h| + h^2.$$

Từ đó chứng minh $S'(x) = x^2$, $x \in (1; 2)$.

Người ta chứng minh được $S'(1) = 1$, $S'(2) = 4$, tức là $S(x)$ là một nguyên hàm của $x^2$ trên $[1; 2]$.

d) Từ kết quả của phần c, ta có $S(x) = \frac{x^3}{3} + C$. Sử dụng điều này với lưu ý $S(1) = 0$ và diện tích cần tính $S = S(2)$, hãy tính $S$.

Gọi $F(x)$ là một nguyên hàm tùy ý của $f(x) = x^2$ trên $[1; 2]$. Hãy so sánh $S$ và $F(2) - F(1)$.

Tổng quát, ta có: