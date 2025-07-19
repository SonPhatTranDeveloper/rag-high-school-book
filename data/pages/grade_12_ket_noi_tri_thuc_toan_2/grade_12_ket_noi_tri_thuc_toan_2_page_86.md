b) Ta cần tìm n sao cho

$\frac{(1-0)^3 \cdot 2}{12n^2} < 0,01 \Leftrightarrow \frac{1}{6n^2} < 0,01 \Leftrightarrow n > 4.$

Do đó, ta chọn n = 5.

c) Chia đoạn [0; 1] thành 5 đoạn có độ dài bằng nhau là [0; 0,2], [0,2; 0,4], [0,4; 0,6], [0,6; 0,8], [0,8; 1].

Áp dụng công thức hình thang, ta có:

$\int_0^1 e^{-x^2} dx \approx \frac{1-0}{10} \left[ \frac{1}{e^0} + \frac{2}{e^{0,04}} + \frac{2}{e^{0,16}} + \frac{2}{e^{0,36}} + \frac{2}{e^{0,64}} + \frac{1}{e} \right] \approx 0,744.$

Thực hành 2. Sử dụng phương pháp hình thang, tính gần đúng $\int_1^2 \frac{e^x}{x} dx$ với độ chính xác 0,01.

Vận dụng. Một thân cây dài 4,8 m được cắt thành các khúc gỗ dài 60 cm. Người ta đo đường kính của mỗi mặt cắt ngang và diện tích S của nó được ghi lại trong bảng dưới đây, ở đây x (cm) là khoảng cách tính từ đỉnh thân cây đến vết cắt.

| x (cm) | 0 | 60 | 120 | 180 | 240 | 300 | 360 | 420 | 480 |
|--------|---|----|----|----|----|----|----|----|----|
| S (cm²) | 240 | 248 | 256 | 260 | 264 | 272 | 298 | 316 | 320 |

Tìm thể tích gần đúng của thân cây này.

Hướng dẫn.

Thể tích cần tính là $V = \int_0^{480} S(x)dx$, trong đó S(x) là diện tích mặt cắt ngang tại vị trí cách đỉnh thân cây một khoảng x (cm). Sử dụng phương pháp hình thang để tính gần đúng tích phân này.