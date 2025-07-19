Ví dụ 4. Ở lúa, hạt gạo đục là tính trạng trội hoàn toàn so với hạt gạo trong. Cho cây lúa có hạt gạo đục thuần chủng thụ phấn với cây lúa có hạt gạo trong được F1 toàn hạt gạo đục. Tiếp tục cho các cây lúa F1 thụ phấn với nhau và thu được các hạt gạo mới. Lần lượt chọn ra ngẫu nhiên 2 hạt gạo mới, tính xác suất của biến cố "Có đúng 1 hạt gạo đục trong 2 hạt gạo được lấy ra".

Giải

Quy ước gene A: hạt gạo đục và gene a: hạt gạo trong. Ở thế hệ F2, ba kiểu gene AA, Aa, aa xuất hiện với tỉ lệ 1: 2: 1 nên tỉ lệ hạt gạo đục so với hạt gạo trong là 3: 1.

Gọi $A_1$, $A_2$ lần lượt là biến cố "Hạt gạo lấy ra lần thứ nhất là hạt gạo đục" và biến cố "Hạt gạo lấy ra lần thứ hai là hạt gạo đục".

Ta có $A_1$, $A_2$ là hai biến cố độc lập và $P(A_1) = P(A_2) = \frac{3}{4}$. Xác suất của biến cố "Có đúng 1 hạt gạo đục trong 2 hạt gạo được lấy ra" là

$P(A_1\overline{A_2} \cup \overline{A_1}A_2) = P(A_1\overline{A_2}) + P(\overline{A_1}A_2) = P(A_1)P(\overline{A_2}) + P(\overline{A_1})P(A_2) = 2 \cdot \frac{3}{4} \cdot \frac{1}{4} = \frac{3}{8}$.

Hãy trả lời câu hỏi ở [biểu tượng phát video].

Quy tắc cộng cho hai biến cố bất kì

Rút ngẫu nhiên 1 lá bài từ bộ bài tây 52 lá. Tính xác suất của biến cố "Lá bài được chọn có màu đỏ hoặc là lá có số chia hết cho 5".

Với hai biến cố A, B bất kì, ta có công thức cộng tổng quát như sau:

Cho hai biến cố A và B. Khi đó

$P(A \cup B) = P(A) + P(B) - P(AB)$.

Ví dụ 5. Một hộp chứa 100 tấm thẻ cùng loại được đánh số lần lượt từ 1 đến 100. Chọn ngẫu nhiên 1 thẻ từ hộp. Tính xác suất của biến cố "Số ghi trên thẻ được chọn chia hết cho 3 hoặc 5".

Giải

Gọi A là biến cố "Số ghi trên thẻ được chọn chia hết cho 3" và B là biến cố "Số ghi trên thẻ được chọn chia hết cho 5".

$A \cup B$ là biến cố "Số ghi trên thẻ được chọn chia hết cho 3 hoặc 5".

Từ 1 đến 100 có 33 số chia hết cho 3 nên $P(A) = \frac{33}{100} = 0,33$.

Từ 1 đến 100 có 20 số chia hết cho 5 nên $P(B) = \frac{20}{100} = 0,2$.