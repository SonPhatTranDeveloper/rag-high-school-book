a) Với bất kì $x_0 \neq 0$, ta có:

$$f'(x_0) = \lim_{x \to x_0} \frac{\frac{1}{x} - \frac{1}{x_0}}{x - x_0} = \lim_{x \to x_0} \frac{x_0 - x}{xx_0(x - x_0)} = \lim_{x \to x_0} \frac{-1}{xx_0} = -\frac{1}{x_0^2}.$$

Vậy $f'(x) = \left(\frac{1}{x}\right)' = -\frac{1}{x^2}$ trên các khoảng $(-\infty; 0)$ và $(0; +\infty)$.

1. Tính đạo hàm của hàm số $f(x) = x^3$.

Chú ý: Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$, có đạo hàm tại $x_0 \in (a; b)$.

a) Đại lượng $\Delta x = x - x_0$ gọi là số gia của biến tại $x_0$. Đại lượng $\Delta y = f(x) - f(x_0)$ gọi là số gia tương ứng của hàm số. Khi đó, $x = x_0 + \Delta x$ và

$$f'(x_0) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}.$$

b) Tỉ số $\frac{\Delta y}{\Delta x}$ biểu thị tốc độ thay đổi trung bình của đại lượng $y$ theo đại lượng $x$ trong khoảng từ $x_0$ đến $x_0 + \Delta x$; còn $f'(x_0)$ biểu thị tốc độ thay đổi (tức thời) của đại lượng $y$ theo đại lượng $x$ tại điểm $x_0$.

Ý nghĩa vật lí của đạo hàm
• Nếu hàm số $s = f(t)$ biểu thị quãng đường di chuyển của vật theo thời gian $t$ thì $f'(t_0)$ biểu thị tốc độ tức thời của chuyển động tại thời điểm $t_0$.
• Nếu hàm số $T = f(t)$ biểu thị nhiệt độ $T$ theo thời gian $t$ thì $f'(t_0)$ biểu thị tốc độ thay đổi nhiệt độ theo thời gian tại thời điểm $t_0$.

Với tình huống trong 1, hãy tính vận tốc tức thời của chuyển động lúc $t = 2$.

2. Ý nghĩa hình học của đạo hàm

2. Cho hàm số $y = f(x) = \frac{1}{2}x^2$ có đồ thị $(C)$ và điểm $M\left(1; \frac{1}{2}\right)$ thuộc $(C)$.
a) Vẽ $(C)$ và tính $f'(1)$.
b) Vẽ đường thẳng $d$ đi qua điểm $M$ và có hệ số góc bằng $f'(1)$. Nêu nhận xét về vị trí tương đối giữa $d$ và $(C)$.

Trong mặt phẳng tọa độ $Oxy$, cho đồ thị $(C)$ của hàm số $y = f(x)$ và điểm $M_0(x_0; f(x_0))$ thuộc $(C)$. Xét $M(x; f(x))$ là một điểm di chuyển trên $(C)$. Đường thẳng $M_0M$ là một cát tuyến của $(C)$. Hệ số góc của cát tuyến $M_0M$ được tính bởi công thức $k_{M_0M} = \tan \beta = \frac{f(x) - f(x_0)}{x - x_0}$. Khi cho $x$ dần tới $x_0$ thì $M$ di chuyển trên $(C)$ tới $M_0$. Giả sử cát tuyến $M_0M$ có vị trí giới hạn là $M_0T$ thì $M_0T$ được gọi là tiếp tuyến của $(C)$ tại $M_0$ và $M_0$ được gọi là tiếp điểm.

Ta có hệ số góc của tiếp tuyến $M_0T$ là $k_{M_0T} = \tan \alpha = \lim_{x \to x_0} \tan \beta = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = f'(x_0)$.

[Hình 3: Đồ thị minh họa cho ý nghĩa hình học của đạo hàm, bao gồm đường cong $(C)$, điểm $M_0$, tiếp tuyến $M_0T$, và các góc $\alpha$ và $\beta$.]