Luyện tập 5. Trở lại tình huống mở đầu Mục 2. Thống kê cho thấy tỉ lệ dân số mắc bệnh hiếm nghèo X là 0,2%.

a) Trước khi tiến hành xét nghiệm, xác suất mắc bệnh hiếm nghèo X của ông M là bao nhiêu?

b) Sau khi xét nghiệm cho kết quả dương tính, xác suất mắc bệnh hiếm nghèo X của ông M là bao nhiêu?

Ví dụ 4. Một thống kê cho thấy tỉ lệ dân số mắc bệnh hiếm nghèo Y là 0,5%. Bà N đi xét nghiệm bệnh hiếm nghèo Y và nhận được kết quả là âm tính. Biết rằng, nếu mắc bệnh hiếm nghèo Y thì với xác suất 0,94 xét nghiệm là dương tính; nếu không bị bệnh hiếm nghèo Y thì với xác suất 0,97 xét nghiệm là âm tính.

a) Trước khi tiến hành xét nghiệm xác suất không mắc bệnh hiếm nghèo Y của bà N là bao nhiêu?

b) Sau khi xét nghiệm cho kết quả âm tính, xác suất không mắc bệnh hiếm nghèo Y của bà N là bao nhiêu?

Giải
Gọi A là biến cố: "Bà N bị bệnh hiếm nghèo Y"; B là biến cố: "Xét nghiệm cho kết quả dương tính".

a) Trước khi tiến hành xét nghiệm, xác suất không mắc bệnh hiếm nghèo Y của bà N là

$P(\overline{A}) = 1 - P(A) = 1 - 0,005 = 0,995.$

b) Ta cần tính $P(\overline{A}|\overline{B})$.

Theo công thức Bayes ta có

$P(\overline{A}|\overline{B}) = \frac{P(\overline{A}) \cdot P(\overline{B}|\overline{A})}{P(\overline{A}) \cdot P(\overline{B}|\overline{A}) + P(A) \cdot P(\overline{B}|A)}.$

$P(\overline{B}|\overline{A})$ là xác suất để bà N có xét nghiệm là âm tính nếu bà N không bị bệnh Y.

Theo bài ra ta có:

$P(\overline{B}|\overline{A}) = 0,97;$

$P(\overline{B}|A)$ là xác suất để bà N có xét nghiệm là âm tính nếu bà N bị bệnh Y;

$P(\overline{B}|A) = 1 - 0,94 = 0,06.$

Thay vào công thức Bayes ta có

$P(\overline{A}|\overline{B}) = \frac{0,995 \cdot 0,97}{0,995 \cdot 0,97 + 0,005 \cdot 0,06} \approx 0,9997.$

Như vậy, với xét nghiệm cho kết quả âm tính, xác suất không mắc bệnh Y của bà N tăng lên thành 99,97% (trước xét nghiệm là 99,5%).

BÀI TẬP

6.7. Trong quân sự, một máy bay chiến đấu của đối phương có thể xuất hiện ở vị trí X với xác suất 0,55. Nếu máy bay đó không xuất hiện ở vị trí X thì nó xuất hiện ở vị trí Y. Để phòng thủ, các bệ phóng tên lửa được bố trí tại các vị trí X và Y. Khi máy bay đối phương xuất hiện ở vị trí X hoặc Y thì tên lửa sẽ được phóng để hạ máy bay đó. Xét phương án tác chiến sau: Nếu máy bay xuất hiện tại X thì bắn 2 quả tên lửa và nếu máy bay xuất hiện tại Y thì bắn 1 quả tên lửa.