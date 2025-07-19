Kết hợp công thức trên với công thức xác suất toàn phần, ta có:

Giả sử A và B là hai biến cố ngẫu nhiên thỏa mãn P(A) > 0 và 0 < P(B) < 1. Khi đó,

$P(B|A) = \frac{P(B)P(A|B)}{P(B)P(A|B) + P(\overline{B})P(A|\overline{B})}$

gọi là công thức Bayes.

Chú ý: Với P(A) > 0, công thức $P(B|A) = \frac{P(B)P(A|B)}{P(A)}$ cũng được gọi là công thức Bayes.

Ví dụ 2. Một nhà máy có hai phân xưởng I và II. Phân xưởng I sản xuất 40% số sản phẩm và phân xưởng II sản xuất 60% số sản phẩm. Tỉ lệ sản phẩm bị lỗi của phân xưởng I là 2% và của phân xưởng II là 1%.

a) Kiểm tra ngẫu nhiên 1 sản phẩm của nhà máy và tính xác suất để sản phẩm đó bị lỗi.

b) Biết rằng sản phẩm được chọn bị lỗi. Hỏi xác suất sản phẩm đó do phân xưởng nào sản xuất cao hơn?

Giải

a) Gọi A là biến cố "Sản phẩm bị lỗi" và B là biến cố "Sản phẩm lấy ra do phân xưởng I sản xuất".

Do phân xưởng I sản xuất 40% số sản phẩm và phân xưởng II sản xuất 60% số sản phẩm nên

$P(B) = 0,4$ và $P(\overline{B}) = 1 - 0,4 = 0,6$.

Do tỉ lệ sản phẩm bị lỗi của phân xưởng I là 2% và của phân xưởng II là 1% nên

$P(A|B) = 0,02$ và $P(A|\overline{B}) = 0,01$.

Xác suất để sản phẩm lấy ra bị lỗi là

$P(A) = P(B)P(A|B) + P(\overline{B})P(A|\overline{B}) = 0,4 \cdot 0,02 + 0,6 \cdot 0,01 = 0,014$.

b) Nếu sản phẩm lấy ra bị lỗi thì xác suất sản phẩm đó do phân xưởng I sản xuất là

$P(B|A) = \frac{P(B)P(A|B)}{P(A)} = \frac{0,4 \cdot 0,02}{0,014} = \frac{4}{7}$.

Nếu sản phẩm lấy ra bị lỗi thì xác suất sản phẩm đó do phân xưởng II sản xuất là

$P(\overline{B}|A) = 1 - P(B|A) = \frac{3}{7}$.

Vậy nếu sản phẩm lấy ra bị lỗi thì xác suất sản phẩm đó do phân xưởng I sản xuất cao hơn xác suất sản phẩm đó do phân xưởng II sản xuất.

Ví dụ 3. Trong [biểu tượng video], một người làm xét nghiệm và nhận được kết quả dương tính. Tính xác suất người đó thực sự nhiễm virus (kết quả làm tròn đến hàng phần nghìn).