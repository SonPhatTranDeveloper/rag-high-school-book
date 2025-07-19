Ví dụ 6. Tại một nhà máy, gọi C(x) là tổng chi phí (tính theo triệu đồng) để sản xuất x tấn sản phẩm A trong một tháng. Khi đó, đạo hàm C'(x), gọi là chi phí cận biên, cho biết tốc độ gia tăng tổng chi phí theo lượng gia tăng sản phẩm được sản xuất. Giả sử chi phí cận biên (tính theo triệu đồng trên tấn) của nhà máy được ước lượng bởi công thức

$C'(x) = 5 - 0,06x + 0,00072x^2$ với $0 \leq x \leq 150$.

Biết rằng C(0) = 30 triệu đồng, gọi là chi phí cố định. Tính tổng chi phí khi nhà máy sản xuất 100 tấn sản phẩm A trong tháng.

Giải
Ta có:

$$C(100) - C(0) = \int_0^{100} C'(x)dx = \int_0^{100} (5-0,06x+0,00072x^2)dx$$

$$= 5\int_0^{100} dx - 0,06\int_0^{100} xdx + 0,00072\int_0^{100} x^2dx$$

$$= 5x|_0^{100} - 0,03x^2|_0^{100} + 0,00024x^3|_0^{100} = 440.$$

Suy ra C(100) = C(0) + 440 = 30 + 440 = 470 (triệu đồng).

Vậy khi nhà máy sản xuất 100 tấn sản phẩm A trong tháng thì tổng chi phí là 470 triệu đồng.

Tính các tích phân sau:

a) $\int_1^2 \frac{x-1}{x^2}dx;$

b) $\int_0^{\frac{\pi}{2}} (1+2\sin^2 \frac{x}{2})dx;$

c) $\int_{-2}^1 (x-2)^2dx + \int_{-2}^1 (4x-x^2)dx.$

Tại một nhà máy sản xuất một loại phân bón, gọi P(x) là lợi nhuận (tính theo triệu đồng) thu được từ việc bán x tấn sản phẩm trong một tuần. Khi đó, đạo hàm P'(x), gọi là lợi nhuận cận biên, cho biết tốc độ tăng lợi nhuận theo lượng sản phẩm bán được. Giả sử lợi nhuận cận biên (tính theo triệu đồng trên tấn) của nhà máy được ước lượng bởi công thức

$P'(x) = 16 - 0,02x$ với $0 \leq x \leq 100$.

Tính lợi nhuận nhà máy thu được khi bán 90 tấn sản phẩm trong tuần. Biết rằng nhà máy lỗ 25 triệu đồng nếu không bán được lượng sản phẩm nào trong tuần.

Tính chất 3

Cho hàm số f(x) = 2x. Tính và so sánh kết quả:

$$\int_0^2 f(x)dx \text{ và } \int_0^1 f(x)dx + \int_1^2 f(x)dx.$$

Trong trường hợp tổng quát, ta có:

Cho hàm số y = f(x) liên tục trên đoạn [a; b], c ∈ (a; b). Khi đó,

$$\int_a^b f(x)dx = \int_a^c f(x)dx + \int_c^b f(x)dx.$$