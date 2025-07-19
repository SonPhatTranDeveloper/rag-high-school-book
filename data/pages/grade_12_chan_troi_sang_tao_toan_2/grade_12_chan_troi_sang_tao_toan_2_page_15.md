Ví dụ 2. Tính các tích phân sau:

a) $\int_1^2 x^2dx$;

b) $\int_1^e \frac{1}{t}dt$;

c) $\int_{\frac{\pi}{2}}^{\pi} \cos x dx$.

Giải

a) $\int_1^2 x^2dx = \frac{x^3}{3}\bigg|_1^2 = \frac{1}{3}(2^3 - 1^3) = \frac{7}{3}$;

b) $\int_1^e \frac{1}{t}dt = \ln |t|\bigg|_1^e = \ln e - \ln 1 = 1$;

c) $\int_{\frac{\pi}{2}}^{\pi} \cos x dx = -\int_{\frac{\pi}{2}}^{\pi} \cos x dx = -(\sin x)\bigg|_{\frac{\pi}{2}}^{\pi} = -\left[\sin \pi - \sin \frac{\pi}{2}\right] = -2$.

Chú ý:

a) Nếu hàm số $f(x)$ có đạo hàm $f'(x)$ và $f'(x)$ liên tục trên đoạn $[a; b]$ thì

$f(b) - f(a) = \int_a^b f'(x)dx$.

b) Ta đã biết rằng, đạo hàm của quãng đường di chuyển theo thời gian bằng tốc độ của chuyển động tại mỗi thời điểm $(v(t) = s'(t))$. Do đó, nếu biết tốc độ $v(t)$ tại mọi thời điểm $t \in [a; b]$ thì tính được quãng đường di chuyển trong khoảng thời gian từ $a$ đến $b$ theo công thức

$s = s(b) - s(a) = \int_a^b v(t)dt$.

Lưu ý: Tốc độ chuyển động $v(t)$ luôn nhận giá trị không âm.

Ví dụ 3.

a) Tính quãng đường xe di chuyển từ khi hãm phanh đến khi dừng trong tình huống ở (trang 12).

b) Tính tốc độ trung bình của xe trong khoảng thời gian đó.

Giải

a) Xe dừng khi $v(t) = 20 - 5t = 0$ hay $t = 4$ $(v(t) = 20 - 5t \geq 0$ với mọi $t \in [0; 4])$.

Từ đó, quãng đường xe di chuyển từ khi bắt đầu hãm phanh đến khi dừng là

$s = \int_0^4 v(t)dt = \int_0^4 (20 - 5t)dt = \left[20t - \frac{5t^2}{2}\right]_0^4 = 40$ (m).

b) Tốc độ trung bình của xe trong khoảng thời gian đó là:

$v_{tb} = \frac{s}{4} = \frac{40}{4} = 10$ (m/s).

Nhận xét: Cho hàm số $f(x)$ liên tục trên đoạn $[a; b]$. Khi đó $\frac{1}{b-a}\int_a^b f(x)dx$ được gọi là giá trị trung bình của hàm số $f(x)$ trên đoạn $[a; b]$.