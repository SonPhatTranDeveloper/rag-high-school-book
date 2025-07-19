Nhận xét: Cho hai biến cố A, B với P(A) > 0, 0 < P(B) < 1. Do
P(A) = P(B) . P(A|B) + P(B̄) . P(A|B̄)
nên công thức Bayes còn có dạng: P(B|A) = $\frac{P(B) . P(A|B)}{P(B) . P(A|B) + P(B̄) . P(A|B̄)}$.

Ví dụ 4 Cho hai biến cố A, B sao cho P(A) = 0,6;
P(B) = 0,4; P(A|B) = 0,3. Tính P(B|A).
Giải
Áp dụng công thức Bayes, ta có:
P(B|A) = $\frac{P(B) . P(A|B)}{P(A)}$ = $\frac{0,4 . 0,3}{0,6}$ = 0,2.

Ví dụ 5 Giả sử có một loại bệnh mà tỉ lệ người mắc bệnh là 0,1%. Giả sử có một loại xét nghiệm, mà ai mắc bệnh khi xét nghiệm cũng có phản ứng dương tính, nhưng tỉ lệ phản ứng dương tính giả là 5% (tức là trong số những người không bị bệnh có 5% số người xét nghiệm lại có phản ứng dương tính).
a) Vẽ sơ đồ hình cây biểu thị tình huống trên.
b) Khi một người xét nghiệm có phản ứng dương tính thì khả năng mắc bệnh của người đó là bao nhiêu phần trăm (làm tròn kết quả đến hàng phần trăm)?

Giải
a) Xét hai biến cố: K: "Người được chọn ra không mắc bệnh";
               D: "Người được chọn ra có phản ứng dương tính".
Do tỉ lệ người mắc bệnh là 0,1% = 0,001 nên P(K) = 1 - 0,001 = 0,999.
Trong số những người không mắc bệnh có 5% số người có phản ứng dương tính nên P(D|K) = 5% = 0,05. Vì ai mắc bệnh khi xét nghiệm cũng có phản ứng dương tính nên P(D|K̄) = 1.
Sơ đồ hình cây ở Hình 3 biểu thị tình huống đã cho.

[Hình 3: Sơ đồ hình cây biểu thị tình huống với các nhánh và xác suất tương ứng]

3 Cho hai biến cố A, B sao cho P(A) = 0,4 P(B) = 0,8; P(B|A) = 0,3. Tính P(A|B).

4 Được biết có 5% đàn ông bị mù màu, và 0,25% phụ nữ bị mù màu (Nguồn: F. M. Dekking et al., A modern introduction to probability and statistics - Understanding why and how, Springer, 2005). Giả sử số đàn ông bằng số phụ nữ. Chọn một người bị mù màu một cách ngẫu nhiên. Hỏi xác suất để người đó là đàn ông là bao nhiêu?

101
Bản mẫu góp ý