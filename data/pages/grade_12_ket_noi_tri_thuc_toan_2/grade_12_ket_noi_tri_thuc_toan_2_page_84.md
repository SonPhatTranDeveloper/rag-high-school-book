b) Tính tích phân

Để tính gần đúng tích phân, ta dùng lệnh NIntegral (<hàm số, giá trị đầu, giá trị cuối>), kết quả sẽ được hiển thị ngay bên dưới.

[Hình 72 - Bốn ví dụ về tính tích phân bằng lệnh NIntegral trong GeoGebra, kèm kết quả]

Chú ý: Nếu muốn sử dụng giao diện tiếng Việt, sau khi khởi động GeoGebra, chọn Options → Language → Vietnamese/Tiếng Việt. Khi đó, thay vì cú pháp lệnh tiếng Anh như trình bày ở trên, ta dùng cú pháp lệnh tiếng Việt tương ứng như trong bảng sau:

Lệnh | Cú pháp lệnh tiếng Anh | Cú pháp lệnh tiếng Việt
--- | --- | ---
Tính nguyên hàm | IntegralSymbolic (<hàm số>) | TíchPhân (<hàm số>)
Tính tích phân | NIntegral (<hàm số, giá trị đầu, giá trị cuối>) | TíchPhânXácĐịnh (<hàm số, giá trị đầu, giá trị cuối>)

Thực hành 1. Sử dụng phần mềm GeoGebra, tính:

a) $\int \frac{x^2 - 2x + 2}{x + 1} dx$

b) $\int_0^{\frac{\pi}{2}} e^x \cos 2x dx$

2. TÍNH GẦN ĐÚNG TÍCH PHÂN BẰNG PHƯƠNG PHÁP HÌNH THANG

Để tính tích phân $\int_a^b f(x)dx$ bằng định nghĩa, ta cần biết một nguyên hàm F(x) của f(x) trên đoạn [a; b]. Khi đó:

$\int_a^b f(x)dx = F(b) - F(a)$.

Tuy nhiên, nếu hàm số $f(x)$ không có nguyên hàm dưới dạng hàm sơ cấp, chẳng hạn, người ta biết rằng

$\int e^{x^2} dx; \int e^{-x^2} dx; \int \frac{\sin x}{x} dx; \int \frac{\cos x}{x} dx; \int \frac{e^x}{x} dx; \int \frac{1}{\sqrt{1-x^2}} dx; ...$

không phải là những hàm số sơ cấp, thì không thể dùng định nghĩa trên được. Tình huống tương tự xuất hiện khi f(x) cho bởi một đồ thị mà ta không biết phương trình của nó. Khi đó, ta cần tính xấp xỉ $\int_a^b f(x)dx$ bằng các phương pháp số.