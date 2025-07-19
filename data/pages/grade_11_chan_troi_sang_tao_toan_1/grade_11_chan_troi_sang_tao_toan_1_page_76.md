Nếu chỉ xét trên khoảng từ 0 đến 5 (tính theo 100 gam) thì hàm số giá cước (tính theo nghìn đồng) xác định như sau:

$f(x) = \begin{cases}
6 & \text{khi } x \in (0; 1] \\
7 & \text{khi } x \in (1; 2,5] \\
10 & \text{khi } x \in (2,5; 5].
\end{cases}$

Đồ thị của hàm số như Hình 2.

[Hình 2: Đồ thị hàm số f(x) được vẽ trên hệ trục tọa độ Oxy. Đồ thị gồm 3 đoạn thẳng nằm ngang ở các độ cao y = 6, y = 7 và y = 10 tương ứng với các khoảng x đã cho trong định nghĩa hàm.]

a) Giả sử $(x_n)$ là dãy số bất kì sao cho $x_n \in (1; 2,5)$ và $\lim x_n = 1$. Tìm $\lim f(x_n)$.

b) Giả sử $(x_n')$ là dãy số bất kì sao cho $(x_n') \in (0; 1)$ và $\lim x_n' = 1$. Tìm $\lim f(x_n')$.

c) Nhận xét về kết quả ở a) và b).

• Cho hàm số $y = f(x)$ xác định trên khoảng $(x_0; b)$.

Ta nói hàm số $y = f(x)$ có giới hạn bên phải là số L khi x dần tới $x_0$ nếu với dãy số $(x_n)$ bất kì, $x_0 < x_n < b$ và $x_n \to x_0$ thì $f(x_n) \to L$, kí hiệu $\lim_{x \to x_0^+} f(x) = L$.

• Cho hàm số $y = f(x)$ xác định trên khoảng $(a; x_0)$.

Ta nói hàm số $y = f(x)$ có giới hạn bên trái là số L khi x dần tới $x_0$ nếu với dãy số $(x_n)$ bất kì, $a < x_n < x_0$ và $x_n \to x_0$ thì $f(x_n) \to L$, kí hiệu $\lim_{x \to x_0^-} f(x) = L$.

Chú ý:

a) Ta thừa nhận các kết quả sau:

• $\lim_{x \to x_0^-} f(x) = L$ và $\lim_{x \to x_0^+} f(x) = L$ khi và chỉ khi $\lim_{x \to x_0} f(x) = L$;

• Nếu $\lim_{x \to x_0^-} f(x) \neq \lim_{x \to x_0^+} f(x)$ thì không tồn tại $\lim_{x \to x_0} f(x)$.

b) Các phép toán về giới hạn hữu hạn của hàm số ở Mục 2 vẫn đúng khi ta thay $x \to x_0$ bằng $x \to x_0^+$ hoặc $x \to x_0^-$.

Ví dụ 4. Cho hàm số $f(x) = \begin{cases}
0 & \text{khi } x < 0 \\
1 & \text{khi } x > 0.
\end{cases}$

a) Tìm các giới hạn $\lim_{x \to 0^-} f(x)$ và $\lim_{x \to 0^+} f(x)$.

b) Có tồn tại giới hạn $\lim_{x \to 0} f(x)$?