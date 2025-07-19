1. XÁC SUẤT CÓ ĐIỀU KIỆN

Trong thực tế, ta thường cập nhật xác suất của một biến cố khi biết thêm một thông tin nào đó. Chẳng hạn:
• Tính xác suất để ngày mai mưa nếu hôm nay không mưa;
• Tính xác suất để bạn An là học sinh giỏi môn Toán nếu biết rằng An là một học sinh giỏi môn Tin;
• Tính xác suất để một người thọ 80 tuổi nếu người đó đã sống đến 60 tuổi. (Các công ty bảo hiểm rất quan tâm đến xác suất này).

HD1. Hình thành khái niệm xác suất có điều kiện

Trong một hộp kín có 7 chiếc bút bi xanh và 5 chiếc bút bi đen, các chiếc bút có cùng kích thước và khối lượng. Bạn Sơn lấy ngẫu nhiên một chiếc bút bi trong hộp, không trả lại. Sau đó Tùng lấy ngẫu nhiên một trong 11 chiếc bút còn lại. Tính xác suất để Tùng lấy được bút bi xanh nếu biết rằng Sơn đã lấy được bút bi đen.

Ta có định nghĩa sau:

Cho hai biến cố A và B. Xác suất của biến cố A, tính trong điều kiện biết rằng biến cố B đã xảy ra, được gọi là xác suất của A với điều kiện B và kí hiệu là P(A | B).

Xác suất có điều kiện có thể được tính theo công thức sau:

Cho hai biến cố A và B bất kì, với P(B) > 0. Khi đó

$P(A|B) = \frac{P(AB)}{P(B)}$

Ví dụ 1. Một hộp có 20 viên bi trắng và 10 viên bi đen, các viên bi có cùng kích thước và khối lượng. Bạn Bình lấy ngẫu nhiên một viên bi trong hộp, không trả lại. Sau đó bạn An lấy ngẫu nhiên một viên bi trong hộp đó.

Gọi A là biến cố: "An lấy được viên bi trắng"; B là biến cố: "Bình lấy được viên bi trắng".

Tính P(A | B) bằng định nghĩa và bằng công thức tính P(A | B) ở trên.

Giải

Cách 1: Bằng định nghĩa

Nếu B xảy ra tức là Bình lấy được viên bi trắng. Khi đó, trong hộp còn lại 29 viên bi với 19 viên bi trắng và 10 viên bi đen. Vậy P(A | B) = $\frac{19}{29}$.

Cách 2: Bằng công thức

Bình có 30 cách chọn, An có 29 cách chọn một viên bi trong hộp. Do đó n(Ω) = 30 · 29.

Bình có 20 cách chọn một viên bi trắng, An có 29 cách chọn từ 29 viên bi còn lại.

Do đó n(B) = 20 · 29 và P(B) = $\frac{n(B)}{n(Ω)}$.

Bình có 20 cách chọn một viên bi trắng, An có 19 cách chọn một viên bi trắng trong 19 viên bi trắng còn lại.

Do đó n(AB) = 20 · 19 và P(AB) = $\frac{n(AB)}{n(Ω)}$

Vậy P(A | B) = $\frac{P(AB)}{P(B)} = \frac{n(AB)}{n(B)} = \frac{20 \cdot 19}{20 \cdot 29} = \frac{19}{29}$.