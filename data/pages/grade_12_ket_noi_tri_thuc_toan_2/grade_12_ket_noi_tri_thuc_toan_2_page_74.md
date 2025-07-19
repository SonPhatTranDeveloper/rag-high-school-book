Bài 19: CÔNG THỨC XÁC SUẤT TOÀN PHẦN VÀ CÔNG THỨC BAYES

THUẬT NGỮ:
• Công thức xác suất toàn phần
• Sơ đồ hình cây
• Công thức Bayes

KIẾN THỨC, KĨ NĂNG:
• Mô tả và biết vận dụng công thức xác suất toàn phần vào các tình huống có nội dung thực tiễn.
• Nắm được và biết vận dụng công thức Bayes vào các tình huống có nội dung thực tiễn.

1. CÔNG THỨC XÁC SUẤT TOÀN PHẦN

Số khán giả đến xem buổi biểu diễn ca nhạc ngoài trời phụ thuộc vào thời tiết. Giả sử, nếu trời không mưa thì xác suất để bán hết vé là 0,9; còn nếu trời mưa thì xác suất để bán hết vé chỉ là 0,4. Dự báo thời tiết cho thấy xác suất để trời mưa vào buổi biểu diễn là 0,75. Nhà tổ chức sự kiện quan tâm đến xác suất để bán được hết vé là bao nhiêu.

Công thức xác suất trong Mục 1 sẽ trả lời cho ta câu hỏi đó.

[Hình ảnh minh họa về dự báo thời tiết từ website thời tiết]

Hình 6.1. Minh họa về dự báo thời tiết
(Ảnh: https://thoitiet.edu.vn/)

HD1. Hình thành công thức xác suất toàn phần

Gọi A là biến cố "Trời mưa" và B là biến cố "Bán hết vé" trong tình huống mở đầu.

a) Tính $P(A)$, $P(\overline{A})$, $P(B|A)$, $P(B|\overline{A})$.

b) Trong hai xác suất P(A) và P(B), nhà tổ chức sự kiện quan tâm đến xác suất nào nhất?

Dựa trên các dữ kiện đã biết, có thể tính được P(B) hay không? Công thức sau đây giúp ta trả lời cho câu hỏi này.

Cho hai biến cố A và B. Khi đó, ta có công thức sau:

$P(B) = P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A})$.

Công thức trên được gọi là công thức xác suất toàn phần.