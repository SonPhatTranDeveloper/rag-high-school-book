Hãy tìm các giá trị thích hợp thay vào ? ở sơ đồ hình cây sau:

[Hình vẽ mô tả sơ đồ hình cây với các nhánh "Thứ Bảy" và "Chủ nhật", có các xác suất và dấu hỏi cần điền]

Ở 3, gọi A là biến cố "Ngày thứ Bảy trời nắng" và B là biến cố "Ngày Chủ nhật trời mưa".

Ta có $P(A) = 0,7; P(B|A) = 0,2; P(B|\overline{A}) = 0,3$.

Do đó $P(\overline{A}) = 1 - P(A) = 0,3; P(\overline{B}|A) = 1 - P(B|A) = 0,8; P(\overline{B}|\overline{A}) = 1 - P(B|\overline{A}) = 0,7$.

Áp dụng công thức nhân xác suất, ta có xác suất trời nắng vào thứ Bảy và trời mưa vào Chủ nhật là

$P(AB) = P(A)P(B|A) = 0,7 \cdot 0,2 = 0,14$.

Tương tự, ta có

$P(A\overline{B}) = P(A)P(\overline{B}|A) = 0,7 \cdot 0,8 = 0,56$;

$P(\overline{A}B) = P(\overline{A})P(B|\overline{A}) = 0,3 \cdot 0,3 = 0,09$;

$P(\overline{A}\overline{B}) = P(\overline{A})P(\overline{B}|\overline{A}) = 0,3 \cdot 0,7 = 0,21$.

Ta có thể biểu diễn các kết quả trên theo sơ đồ hình cây như sau:

[Hình vẽ mô tả sơ đồ hình cây hoàn chỉnh với các xác suất và kết quả]

Nhận xét: Trên sơ đồ hình cây:
- Xác suất của các nhánh trong sơ đồ hình cây từ đỉnh thứ hai là xác suất có điều kiện.
- Xác suất xảy ra của mỗi kết quả bằng tích các xác suất trên các nhánh của cây đi đến kết quả đó.

Ví dụ 5. Ở một sân bay, người ta sử dụng một loại máy soi tự động phát hiện hàng cấm trong hành lí kí gửi. Máy phát chuông cảnh báo với 95% các kiện hành lí có chứa hàng cấm và 2% các kiện hành lí không chứa hàng cấm. Tỉ lệ các kiện hành lí có chứa hàng cấm là 1%.