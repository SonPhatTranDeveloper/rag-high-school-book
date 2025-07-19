Ví dụ 5. Hai túi I và II chứa các tấm thẻ được đánh số. Túi I: {1; 2; 3; 4; 5}, túi II: {1; 2; 3; 4}. Rút ngẫu nhiên một tấm thẻ từ mỗi túi I và II. Tính xác suất để tổng hai số trên hai tấm thẻ lớn hơn 6.

[Hình ảnh minh họa hai túi đựng thẻ, một túi màu xanh lá cây và một túi màu cam]

Giải
Mô tả không gian mẫu Ω bằng cách lập bảng như sau.

[Bảng mô tả không gian mẫu với các cặp số từ túi I và túi II]

Mỗi ô là một kết quả có thể. Có 20 ô, vậy $n(Ω) = 20$.

Biến cố E: "Tổng hai số trên hai tấm thẻ lớn hơn 6" xảy ra khi tổng là một trong ba trường hợp:
Tổng bằng 7 gồm các kết quả: (3, 4); (4, 3); (5, 2).
Tổng bằng 8 gồm các kết quả: (4, 4); (5, 3).
Tổng bằng 9 có một kết quả: (5, 4).

Vậy biến cố E = {(3, 4); (4, 3); (5, 2); (4, 4); (5, 3); (5, 4)}. Từ đó $n(E) = 6$ và $P(E) = \frac{6}{20} = \frac{3}{10} = 0,3$.

Chú ý: Trong những phép thử đơn giản, ta đếm số phần tử của tập Ω và số phần tử của biến cố E bằng cách liệt kê ra tất cả các phần tử của hai tập hợp này.

Luyện tập 3. Gieo đồng thời hai con xúc xắc cân đối. Tính xác suất để tổng số chấm xuất hiện trên hai con xúc xắc bằng 4 hoặc bằng 6.

3. NGUYÊN LÍ XÁC SUẤT BÉ

Qua thực tế người ta thấy rằng một biến cố có xác suất rất bé thì sẽ không xảy ra khi ta thực hiện một phép thử hay một vài phép thử. Từ đó người ta đã thừa nhận nguyên lí sau đây gọi là nguyên lí xác suất bé:

Nếu một biến cố có xác suất rất bé thì trong một phép thử biến cố đó sẽ không xảy ra.

Chẳng hạn, xác suất một chiếc máy bay rơi là rất bé, khoảng 0,00000027. Mỗi hành khách khi đi máy bay đều tin rằng biến cố: "Máy bay rơi" sẽ không xảy ra trong chuyến bay của mình, do đó người ta vẫn không ngần ngại đi máy bay.

Chú ý: Trong thực tế, xác suất của một biến cố được coi là bé phụ thuộc vào từng trường hợp cụ thể. Chẳng hạn, xác suất một chiếc điện thoại bị lỗi kĩ thuật là 0,001 được coi là rất bé, nhưng nếu xác suất cháy nổ động cơ của một máy bay là 0,001 thì xác suất này không được coi là rất bé.