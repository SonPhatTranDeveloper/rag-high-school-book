Nhận xét
• Từ định nghĩa của xác suất có điều kiện, ta suy ra: Nếu P(B) > 0 thì
P(A ∩ B) = P(B) . P(A | B).
• Người ta chứng minh được rằng: Nếu A, B là hai biến cố bất kì thì
P(A ∩ B) = P(A) . P(B | A) = P(B) . P(A | B).
Công thức trên được gọi là công thức nhân xác suất.

Ví dụ 1 Cho hai biến cố A, B có P(A) = 0,4; P(B) = 0,6; P(A ∩ B) = 0,2. Tính các xác suất sau: P(A | B); P(B | A).

Giải
Ta có: P(A | B) = $\frac{P(A \cap B)}{P(B)} = \frac{0,2}{0,6} = \frac{1}{3}$; P(B | A) = $\frac{P(B \cap A)}{P(A)} = \frac{0,2}{0,4} = 0,5$.

Ví dụ 2 Trong kì kiểm tra môn Toán của một trường trung học phổ thông có 200 học sinh tham gia, trong đó có 95 học sinh nam và 105 học sinh nữ. Khi công bố kết quả của kì kiểm tra đó, có 50 học sinh đạt điểm giỏi, trong đó có 24 học sinh nam và 26 học sinh nữ. Chọn ra ngẫu nhiên một học sinh trong số 200 học sinh đó. Tính xác suất để học sinh được chọn ra đạt điểm giỏi, biết rằng học sinh đó là nữ (làm tròn kết quả đến hàng phần trăm).

Giải
Xét hai biến cố sau:
A: "Học sinh được chọn ra đạt điểm giỏi";
B: "Học sinh được chọn ra là học sinh nữ".
Khi đó, xác suất để học sinh được chọn ra đạt điểm giỏi, biết rằng học sinh đó là nữ, chính là xác suất của A với điều kiện B.

Do có 26 học sinh nữ đạt điểm giỏi nên
P(A ∩ B) = $\frac{26}{200} = 0,13$.

Do có 105 học sinh nữ nên P(B) = $\frac{105}{200} = 0,525$. Vì thế, ta có:

P(A | B) = $\frac{P(A \cap B)}{P(B)} = \frac{0,13}{0,525} \approx 0,25$.

Vậy xác suất để học sinh được chọn ra đạt điểm giỏi, biết rằng học sinh đó là nữ, là 0,25.

Nhận xét: Cho hai biến cố A và B với P(B) > 0. Khi đó, ta có: P(A | B) = $\frac{n(A \cap B)}{n(B)}$ (*).

[Hình ảnh bên cạnh mô tả một bài toán về xác suất:]
1 Một hộp có 6 quả bóng màu xanh, 4 quả bóng màu đỏ; các quả bóng có kích thước và khối lượng như nhau. Lấy ngẫu nhiên lần lượt hai quả bóng trong hộp, lấy không hoàn lại. Tìm xác suất để lần thứ hai lấy được quả bóng màu đỏ, biết rằng lần thứ nhất đã lấy được quả bóng màu xanh.