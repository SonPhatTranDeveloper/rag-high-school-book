HOẠT ĐỘNG THỰC HÀNH TRẢI NGHIỆM

TÍNH NGUYÊN HÀM VÀ TÍCH PHÂN VỚI PHẦN MỀM GEOGEBRA. TÍNH GẦN ĐÚNG TÍCH PHÂN BẰNG PHƯƠNG PHÁP HÌNH THANG

MỤC TIÊU
Thực hành tính nguyên hàm và tính gần đúng tích phân với phần mềm GeoGebra. Tính gần đúng tích phân bằng phương pháp hình thang trong trường hợp hàm dưới dấu tích phân cho dạng bảng (tại một số mốc) hoặc cho bởi một đồ thị (mà ta không biết phương trình của nó) hoặc không có nguyên hàm dưới dạng hàm sơ cấp.

1. TÍNH NGUYÊN HÀM VÀ TÍCH PHÂN VỚI PHẦN MỀM GEOGEBRA

Khởi động phần mềm GeoGebra [Hình biểu tượng GeoGebra], chọn Complex Adaptive System (CAS) để thực hiện tính toán nguyên hàm và tích phân.

a) Tính nguyên hàm của hàm số
Để tính nguyên hàm của hàm số, ta dùng lệnh IntegralSymbolic (<hàm số>), kết quả sẽ được hiển thị ngay bên dưới.

[Hình T1 - Bảng kết quả tính nguyên hàm]

1. IntegralSymbolic(sin(2 x))
   $\rightarrow -\frac{1}{2} \cos(2 x) + c_1$

2. IntegralSymbolic($\frac{x + \sqrt{x}}{\sqrt{x}}$)
   $\rightarrow \frac{3}{5} \sqrt{x^2} x + \frac{6}{7} \sqrt[4]{x} + c_2$

3. IntegralSymbolic($x(1 + x^2)^{\frac{1}{3}}$)
   $\rightarrow \frac{1}{5} \sqrt{x^2 + 1} (x^2 + 1)^2 + c_2$

4. IntegralSymbolic(x sin(2x + 1))
   $\rightarrow \frac{1}{4} \sin(2 x + 1) - \frac{1}{2} x \cos(2 x + 1) + c_2$

Hình T1