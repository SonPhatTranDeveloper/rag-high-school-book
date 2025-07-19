# 1. Công thức xác suất toàn phần

Chị An trả lời hai câu hỏi. Xác suất trả lời đúng câu hỏi thứ nhất là 0,7. Xác suất trả lời đúng câu hỏi thứ hai là 0,9 nếu chị An trả lời đúng câu hỏi thứ nhất và là 0,5 nếu chị An không trả lời đúng câu hỏi thứ nhất.

Gọi A là biến cố "Chị An trả lời đúng câu hỏi thứ nhất" và B là biến cố "Chị An trả lời đúng câu hỏi thứ hai".

[Hình minh họa: Một học sinh nữ đang ngồi tại bàn làm bài tập]

Hãy tìm các giá trị thích hợp điền vào các ô ? ở sơ đồ hình cây sau:

[Sơ đồ hình cây biểu diễn xác suất các trường hợp trả lời câu hỏi]

Ta thấy biến cố B là hợp của hai biến cố xung khắc AB và $\overline{A}B$. Do đó

$P(B) = P(AB) + P(\overline{A}B) = 0,63 + 0,15 = 0,78.$

Một cách tổng quát, ta có

Cho hai biến cố A và B với $0 < P(B) < 1$. Khi đó

$P(A) = P(B)P(A|B) + P(\overline{B})P(A|\overline{B})$

gọi là công thức xác suất toàn phần.

Chú ý: Công thức xác suất toàn phần cũng đúng với biến cố B bất kì.

Ví dụ 1. Trong ▶, hãy tính xác suất người làm xét nghiệm có kết quả dương tính.

Giải

Gọi A là biến cố "Người làm xét nghiệm có kết quả dương tính" và B là biến cố "Người làm xét nghiệm thực sự nhiễm virus".

Do xét nghiệm cho kết quả dương tính với 76,2% các ca thực sự nhiễm virus nên $P(A|B) = 0,762$.

Do xét nghiệm cho kết quả âm tính với 99,1% các ca thực sự không nhiễm virus nên $P(\overline{A}|\overline{B}) = 0,991$. Suy ra

$P(A|\overline{B}) = 1 - 0,991 = 0,009$.

Do tỉ lệ người nhiễm virus trong cộng đồng là 1% nên $P(B) = 0,01$ và $P(\overline{B}) = 0,99$.

Áp dụng công thức xác suất toàn phần, ta có xác suất người làm xét nghiệm có kết quả dương tính là

$P(A) = P(B)P(A|B) + P(\overline{B})P(A|\overline{B}) = 0,01 \cdot 0,762 + 0,99 \cdot 0,009 = 0,01653$.