2. CÔNG THỨC BAYES

Trong Y học, để chẩn đoán bệnh X nào đó, người ta thường dùng một xét nghiệm. Xét nghiệm dương tính, tức là xét nghiệm đó kết luận một người mắc bệnh X. Xét nghiệm âm tính, tức là xét nghiệm đó kết luận một người không mắc bệnh X. Vì không có một xét nghiệm nào tuyệt đối đúng nên trên thực tế có thể xảy ra hai sai lầm sau:
- Xét nghiệm dương tính nhưng thực tế người xét nghiệm không mắc bệnh. Ta gọi đây là dương tính giả.
- Xét nghiệm âm tính nhưng thực tế người xét nghiệm lại mắc bệnh. Ta gọi đây là âm tính giả.

[Hình ảnh minh họa một bác sĩ đang khám bệnh cho bệnh nhân]

Ông M đi xét nghiệm bệnh hiếm nghèo X. Biết rằng, nếu một người mắc bệnh X thì với xác suất 0,95 xét nghiệm cho dương tính; nếu một người không bị bệnh X thì với xác suất 0,01 xét nghiệm cho dương tính.

Xét nghiệm của ông M cho kết quả dương tính. Ông M hoảng hốt khi nghĩ rằng mình có xác suất 0,95 mắc bệnh hiếm nghèo X. Mục 2 giúp chúng ta hiểu đúng xác suất đó.

HD2. Phân biệt P(A | B) và P(B | A)

Trong tình huống mở đầu Mục 2, gọi A là biến cố "Ông M mắc bệnh hiếm nghèo X", B là biến cố: "Xét nghiệm cho kết quả dương tính".

a) Nếu các nội dung còn thiếu tương ứng với "(?) để hoàn thành các câu sau đây:
• P(A | B) là xác suất để (?) với điều kiện (?);
• P(B | A) là xác suất để (?) với điều kiện (?).

b) 0,95 là P(A | B) hay P(B | A)? Có phải ông M có xác suất 0,95 mắc bệnh hiếm nghèo X không?

Công thức sau đây cho ta tính P(A | B) khi biết P(B | A) và P(A):

Cho A và B là hai biến cố, với P(B) > 0.
Khi đó, ta có công thức sau:

$P(A|B) = \frac{P(A) \cdot P(B|A)}{P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A})}$

Công thức trên có tên là công thức Bayes.

Chú ý: Theo công thức xác suất toàn phần, ta có:

$P(B) = P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A})$

Do đó, công thức Bayes còn có thể viết dưới dạng:

$P(A|B) = \frac{P(A) \cdot P(B|A)}{P(B)}$

Ý nghĩa của công thức Bayes: Một nhà nghiên cứu quan tâm đến xác suất xảy ra của biến cố A. Theo tính toán ban đầu A có xác suất là P(A) = p. Sau đó, nhà nghiên cứu có được thông tin rằng: "Biến cố B đã xảy ra". Với thông tin mới này, nhà nghiên cứu sẽ cập nhật lại hiểu biết của mình về khả năng xảy ra biến cố A, bằng cách tính P(A | B), xác suất của A khi biết B đã xảy ra. Công thức Bayes cho ta tính P(A | B).

[Hình ảnh chân dung Thomas Bayes (1701 - 1761) với chú thích: Công thức Bayes đóng vai trò quan trọng trong Lí thuyết Xác suất.]