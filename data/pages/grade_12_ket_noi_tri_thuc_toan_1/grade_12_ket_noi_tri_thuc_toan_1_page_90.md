c) Tính đạo hàm cấp cao của hàm số

Để tính đạo hàm cấp n của hàm số trên một khoảng xác định, ta dùng lệnh Derivative (<hàm số>, <số cấp>), kết quả sẽ được hiển thị ngay bên dưới.

Derivative($x^5 - 4x^3 + 2x - 3,3$)
→ $60x^2 - 24$

Cho hàm số $y = f(x)$ có đạo hàm cấp $n - 1$, kí hiệu là $f^{(n-1)}(x) (n \in \mathbb{N}, n > 1)$. Nếu $f^{(n-1)}(x)$ có đạo hàm thì đạo hàm của nó được gọi là đạo hàm cấp n của $f(x)$, kí hiệu là $f^{(n)}(x)$.

$f^{(n)}(x) = (f^{(n-1)}(x))'$

2. TÌM CỰC TRỊ, GIÁ TRỊ LỚN NHẤT, GIÁ TRỊ NHỎ NHẤT (NẾU CÓ) CỦA HÀM SỐ

a) Tìm cực trị của hàm số

Để tìm cực trị của hàm số, ta dùng lệnh Extremum (<hàm số>), kết quả sẽ được hiển thị ngay bên dưới, dưới dạng tọa độ các điểm cực trị của đồ thị hàm số.

Extremum($2x^3 + 3x^2 - 36x - 10$)
→ {(-3, 71), (2, -54)}

Ngoài ra ta có thể dùng lệnh Extremum (<hàm số>, <giá trị của a>, <giá trị của b>) để tìm cực trị của hàm số đã cho trên đoạn [a; b].

Extremum($x^4 + 2x^2 - 3, -5, 7$)
→ (0, -3)

Extremum($x^4 + 2x^2 - 3, -5, 0$)
→ (?, ?)

Kết quả bên có nghĩa: hàm số đã cho không có cực trị nào trên khoảng (-5; 0).

Chú ý: Ta có thể quan sát kênh hình để có hình ảnh trực quan bằng cách chọn View → Graphics 2.

Để xác định cực trị là cực đại hay cực tiểu, ta có thể dùng đồ thị hàm số để kết luận điểm cực trị là điểm cực đại hay điểm cực tiểu.

b) Tìm giá trị lớn nhất, giá trị nhỏ nhất (nếu có) của hàm số (trên khoảng, đoạn, tập xác định)

Để tìm giá trị lớn nhất của hàm số trên một đoạn [a;b] cho trước, ta dùng lệnh Max (<hàm số>, <a>, <b>); kết quả trả về sẽ là tọa độ của một điểm, tung độ của điểm đó chính là giá trị lớn nhất cần tìm.

Max($x^4 - 3x^2 + 2, 0, 3$)
→ (3, 56)

Kết quả bên có nghĩa: Hàm số đã cho có giá trị lớn nhất trên đoạn [0; 3] là 56, đạt tại x = 3.