Ví dụ 5. Tính:

a) $\int_1^4 (x^3 + 3\sqrt{x}) dx$;

b) $\int_0^{\frac{\pi}{2}} (e^x - 2\cos x) dx$;

c) $\int_1^4 \left(2^x - \frac{3}{x^2}\right) dx$.

Giải

a) $\int_1^4 (x^3 + 3\sqrt{x}) dx = \int_1^4 x^3 dx + 3 \int_1^4 \sqrt{x} dx = \left.\frac{x^4}{4}\right|_1^4 + 3 \cdot \left.\frac{x^{\frac{3}{2}}}{\frac{3}{2}}\right|_1^4$

   $= \frac{1}{4}(4^4 - 1) + 2\left(4^{\frac{3}{2}} - 1\right) = \frac{255}{4} + 14 = \frac{311}{4}$.

b) $\int_0^{\frac{\pi}{2}} (e^x - 2\cos x) dx = \int_0^{\frac{\pi}{2}} e^x dx - 2 \int_0^{\frac{\pi}{2}} \cos x dx$

   $= \left.e^x\right|_0^{\frac{\pi}{2}} - 2\sin x\left|_0^{\frac{\pi}{2}} = \left(e^{\frac{\pi}{2}} - 1\right) - 2(1 - 0) = e^{\frac{\pi}{2}} - 3\right.$.

c) $\int_1^4 \left(2^x - \frac{3}{x^2}\right) dx = \int_1^4 2^x dx - 3 \int_1^4 x^{-2} dx = \left.\frac{2^x}{\ln 2}\right|_1^4 + 3 \cdot \left.\frac{1}{x}\right|_1^4$

   $= \frac{1}{\ln 2}(2^4 - 2^1) + 3\left(\frac{1}{4} - 1\right) = \frac{15}{\ln 2} - \frac{9}{4}$.

Luyện tập 3. Tính các tích phân sau:

a) $\int_0^{2\pi} (2x + \cos x) dx$;

b) $\int_1^2 \left(3^x - \frac{3}{x}\right) dx$;

c) $\int_0^{\frac{\pi}{3}} \left(\frac{1}{\cos^2 x} - \frac{1}{\sin^2 x}\right) dx$.

Ví dụ 6. Tính $\int_0^3 |x - 2| dx$.

Giải

Ta có:

$\int_0^3 |x - 2| dx = \int_0^2 |x - 2| dx + \int_2^3 |x - 2| dx = \int_0^2 (2 - x) dx + \int_2^3 (x - 2) dx$

$= \left(2x - \frac{x^2}{2}\right)\Big|_0^2 + \left(\frac{x^2}{2} - 2x\right)\Big|_2^3 = [(4 - 2) - 0] + \left[\left(\frac{9}{2} - 6\right) - (2 - 4)\right] = \frac{5}{2}$.

Luyện tập 4. Tính $\int_0^3 |2x - 3| dx$.

Vận dụng 2. Giá trị trung bình của hàm số liên tục f(x) trên đoạn [a; b] được định nghĩa là

$\frac{1}{b - a} \int_a^b f(x) dx$.

Giả sử nhiệt độ (tính bằng °C) tại thời điểm t giờ trong khoảng thời gian từ 6 giờ sáng đến 12 giờ trưa ở một địa phương vào một ngày nào đó được mô hình hóa bởi hàm số

$T(t) = 20 + 1,5(t - 6), 6 \leq t \leq 12$.

Tìm nhiệt độ trung bình vào ngày đó trong khoảng thời gian từ 6 giờ sáng đến 12 giờ trưa.