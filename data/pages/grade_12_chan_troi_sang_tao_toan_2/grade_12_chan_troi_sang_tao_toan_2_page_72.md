Ở 2, ta nhận thấy $\frac{P(A \cap B)}{P(B)} = P(A|B)$ và $\frac{P(C \cap A)}{P(A)} = P(C|A)$.

Một cách tổng quát, ta có công thức tính xác suất có điều kiện như sau:

Cho A và B là hai biến cố, trong đó P(B) > 0. Khi đó

$P(A|B) = \frac{P(A \cap B)}{P(B)}$

Chú ý:

a) Ta cũng kí hiệu biến cố giao của hai biến cố A và B là AB.

b) Trong thực tế, người ta thường dùng tỉ lệ phần trăm để mô tả xác suất. Chẳng hạn, phát biểu "Khả năng xảy ra một sự kiện là 20%" cũng có nghĩa là "Xác suất xảy ra sự kiện đó là 0,2", phát biểu "Tỉ lệ phế phẩm của một lô hàng là 5%" cũng có nghĩa là "Nếu chọn ra ngẫu nhiên 1 sản phẩm từ lô hàng, xác suất sản phẩm đó là phế phẩm là 0,05".

Ví dụ 3. Một công ty bảo hiểm nhận thấy có 48% số người mua bảo hiểm ô tô là phụ nữ và có 36% số người mua bảo hiểm ô tô là phụ nữ trên 45 tuổi. Biết một người mua bảo hiểm ô tô là phụ nữ, tính xác suất người đó trên 45 tuổi.

Giải

Gọi A là biến cố "Người mua bảo hiểm ô tô là phụ nữ", B là biến cố "Người mua bảo hiểm ô tô trên 45 tuổi". Ta cần tính P(B|A).

Do có 48% người mua bảo hiểm ô tô là phụ nữ nên P(A) = 0,48.

Do có 36% số người mua bảo hiểm ô tô là phụ nữ trên 45 tuổi nên P(AB) = 0,36.

Vậy $P(B|A) = \frac{P(AB)}{P(A)} = \frac{0,36}{0,48} = 0,75$.

Chú ý:
- Từ công thức xác suất có điều kiện, với P(B) > 0, ta có P(AB) = P(B)P(A|B).
- Trong trường hợp tổng quát, người ta chứng minh được rằng
P(AB) = P(B)P(A|B).
Công thức trên được gọi là công thức nhân xác suất cho hai biến cố bất kì.

Ví dụ 4. Cho hai biến cố A và B có P(A) = 0,3; P(B) = 0,5 và P(A|B) = 0,4. Tính $P(\overline{AB})$ và $P(\overline{A}|B)$.

Giải

Theo công thức nhân xác suất, ta có P(AB) = P(B)P(A|B) = 0,2.

Vì $\overline{AB}$ và AB là hai biến cố xung khắc và $\overline{AB} \cup AB = B$ nên theo tính chất của xác suất, ta có $P(\overline{AB}) = P(B) - P(AB) = 0,3$.