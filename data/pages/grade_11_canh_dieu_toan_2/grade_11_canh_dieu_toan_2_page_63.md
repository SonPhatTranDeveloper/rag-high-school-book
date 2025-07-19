Nhận xét: Trong định nghĩa trên, ta đặt:
$\Delta x = x - x_0$ và gọi $\Delta x$ là số gia của biến số tại điểm $x_0$;
$\Delta y = f(x_0 + \Delta x) - f(x_0)$ và gọi $\Delta y$ là số gia của hàm số ứng với số gia $\Delta x$ tại điểm $x_0$.

Khi đó, ta có: $f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$.

3. Cách tính đạo hàm bằng định nghĩa

Cho hàm số $y = f(x)$ xác định trên khoảng $(a ; b)$ và điểm $x_0$ thuộc khoảng đó.
Để tính đạo hàm $f'(x_0)$ của hàm số $y = f(x)$ tại $x_0$, ta lần lượt thực hiện ba bước sau:

Bước 1. Xét $\Delta x$ là số gia của biến số tại điểm $x_0$. Tính $\Delta y = f(x_0 + \Delta x) - f(x_0)$.

Bước 2. Rút gọn tỉ số $\frac{\Delta y}{\Delta x}$

Bước 3. Tính $\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$.

Kết luận: Nếu $\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = a$ thì $f'(x_0) = a$.

Ví dụ 1: Tính đạo hàm của hàm số $f(x) = \frac{1}{x}$ tại $x_0 = 2$ bằng định nghĩa.

Giải
• Xét $\Delta x$ là số gia của biến số tại điểm $x_0 = 2$.
  Ta có: $\Delta y = f(2 + \Delta x) - f(2) = \frac{1}{2 + \Delta x} - \frac{1}{2} = \frac{2-(2 + \Delta x)}{2(2 + \Delta x)} = \frac{-\Delta x}{2(2 + \Delta x)}$.

  Suy ra: $\frac{\Delta y}{\Delta x} = \frac{-1}{2(2 + \Delta x)}$.

• Ta thấy: $\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{-1}{2(\Delta x + 2)} = -\frac{1}{4}$.

  Vậy $f'(2) = -\frac{1}{4}$.

Tính đạo hàm của hàm số $f(x) = 2x$ tại $x_0 = 3$ bằng định nghĩa.

Ví dụ 2: Tính đạo hàm của hàm số $f(x) = x^2$ tại điểm $x$ bất kì bằng định nghĩa.

Giải
• Xét $\Delta x$ là số gia của biến số tại điểm $x$.
  Ta có: $\Delta y = f(x + \Delta x) - f(x) = (x + \Delta x)^2 - x^2 = \Delta x(2x + \Delta x)$.