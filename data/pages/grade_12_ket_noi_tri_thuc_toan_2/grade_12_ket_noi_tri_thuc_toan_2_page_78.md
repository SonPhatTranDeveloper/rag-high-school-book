Ví dụ 2. Trong một kì thi tốt nghiệp trung học phổ thông, một tỉnh X có 80% học sinh lựa chọn tổ hợp A00 (gồm các môn Toán, Vật lí, Hoá học). Biết rằng, nếu một học sinh chọn tổ hợp A00 thì xác suất để học sinh đó đỗ đại học là 0,6; còn nếu một học sinh không chọn tổ hợp A00 thì xác suất để học sinh đó đỗ đại học là 0,7. Chọn ngẫu nhiên một học sinh của tỉnh X đã tốt nghiệp trung học phổ thông trong kì thi trên. Biết rằng học sinh này đã đỗ đại học. Tính xác suất để học sinh đó chọn tổ hợp A00.

Giải

Gọi A là biến cố: "Học sinh đó chọn tổ hợp A00"; B là biến cố: "Học sinh đó đỗ đại học".
Ta cần tính $P(A | B)$. Theo công thức Bayes, ta cần biết: $P(A)$, $P(\overline{A})$, $P(B | A)$ và $P(B | \overline{A})$.
Ta có: $P(A) = 0,8$; $P(\overline{A}) = 1 - P(A) = 1 - 0,8 = 0,2$.
$P(B | A)$ là xác suất để một học sinh đỗ đại học với điều kiện học sinh đó chọn tổ hợp A00
$\Rightarrow P(B | A) = 0,6$.
$P(B | \overline{A})$ là xác suất để một học sinh đỗ đại học với điều kiện học sinh đó không chọn tổ hợp A00 $\Rightarrow P(B | \overline{A}) = 0,7$.
Thay vào công thức Bayes ta được:

$$P(A|B) = \frac{P(A) \cdot P(B|A)}{P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A})} = \frac{0,8 \cdot 0,6}{0,8 \cdot 0,6 + 0,2 \cdot 0,7} \approx 0,7742.$$

Luyện tập 4. Trong một kho rượu có 30% là rượu loại I. Chọn ngẫu nhiên một chai rượu đưa cho ông Tùng, một người sành rượu, để nếm thử. Biết rằng, một chai rượu loại I có xác suất 0,9 để ông Tùng xác nhận là loại I; một chai rượu không phải loại I có xác suất 0,95 để ông Tùng xác nhận đây không phải là loại I. Sau khi nếm, ông Tùng xác nhận đây là rượu loại I. Tính xác suất để chai rượu đúng là rượu loại I.

Ví dụ 3. Trở lại tình huống mở đầu Mục 2. Tính xác suất để ông M mắc bệnh hiếm nghèo X nếu kết quả xét nghiệm cho kết quả dương tính.

Giải

Gọi A là biến cố: "Ông M mắc bệnh hiếm nghèo X"; B là biến cố: "Xét nghiệm cho kết quả dương tính".
Ta cần tính $P(A | B)$.
Theo công thức Bayes để tính $P(A | B)$, ta cần biết: $P(A)$, $P(\overline{A})$, $P(B | A)$ và $P(B | \overline{A})$.
Gọi p là tỉ lệ dân số mắc bệnh hiếm nghèo X.
Khi đó $P(A) = p$. Suy ra $P(\overline{A}) = 1 - p$.
$P(B | A)$ là xác suất để ông M có xét nghiệm là dương tính nếu ông M mắc bệnh hiếm nghèo X
$\Rightarrow P(B | A) = 0,95$.
$P(B | \overline{A})$ là xác suất để ông M có xét nghiệm là dương tính nếu ông M không mắc bệnh hiếm nghèo X $\Rightarrow P(B | \overline{A}) = 0,01$.
Thay vào công thức Bayes ta có:

$$P(A|B) = \frac{P(A) \cdot P(B|A)}{P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A})} = \frac{p \cdot 0,95}{p \cdot 0,95 + (1-p) \cdot 0,01}.$$