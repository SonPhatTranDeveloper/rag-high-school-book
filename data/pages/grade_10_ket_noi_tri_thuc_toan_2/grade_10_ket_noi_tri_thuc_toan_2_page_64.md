H94. Để lắp ghế vào một phòng chiếu phim, các ghế được gắn nhãn bằng một chữ cái in hoa (trong bảng 26 chữ cái tiếng Anh từ A đến Z) đứng trước và một số nguyên từ 1 đến 20, chẳng hạn X15, Z2, ...
Hỏi có thể gắn nhãn tối đa được cho bao nhiêu ghế?

[Hình ảnh minh họa với hai ô trống: "Chữ cái" và "Số", được ghi chú là "Số ghế"]

Ta nhận thấy muốn làm một việc có hai công đoạn lần lượt thì trước hết ta xét xem công đoạn một có bao nhiêu cách, sau đó với mỗi cách của công đoạn một, ta tính xem công đoạn hai có bao nhiêu cách. Khi đó số cách thực hiện công việc tính theo quy tắc sau:

Quy tắc nhân
Giả sử một công việc nào đó phải hoàn thành qua hai công đoạn liên tiếp nhau:
- Công đoạn một có $m_1$ cách thực hiện,
- Với mỗi cách thực hiện công đoạn một, có $m_2$ cách thực hiện công đoạn hai.
Khi đó số cách thực hiện công việc là: $m_1 \cdot m_2$ cách.

Chú ý
Quy tắc nhân áp dụng để tính số cách thực hiện một công việc có nhiều công đoạn, các công đoạn nối tiếp nhau và những công đoạn này độc lập với nhau.

Ví dụ 3. Một người muốn mua vé tàu ngồi đi từ Hà Nội vào Vinh. Có ba chuyến tàu là SE5, SE7 và SE35. Trên mỗi tàu có 2 loại vé ngồi khác nhau: ngồi cứng hoặc ngồi mềm. Hỏi có bao nhiêu loại vé ngồi khác nhau để người đó lựa chọn?

Giải
Để mua được vé tàu, người đó phải thực hiện hai công đoạn:

Chọn chuyến tàu → Chọn loại vé

Có 3 cách chọn chuyến tàu, với mỗi chuyến tàu có 2 cách chọn loại vé ngồi. Áp dụng quy tắc nhân, ta có số cách chọn loại vé là: 3 · 2 = 6 (cách).

[Hình ảnh minh họa quy trình chọn vé tàu với các bước: Chọn chuyến tàu (SE5, SE35, SE7) → Chọn loại vé (Cứng, Mềm) → Hoàn thành]

Chú ý: Ta cũng có thể dùng quy tắc cộng. Người mua vé có thể lựa chọn một trong ba trường hợp: SE5, SE7 hoặc SE35.
Nếu lựa chọn SE5, có hai loại vé: loại vé SE5 ngồi cứng và SE5 ngồi mềm. Tương tự cho trường hợp SE7 và trường hợp SE35.
Mỗi trường hợp có hai loại vé. Tổng cộng có:
2 + 2 + 2 = 6 (cách chọn loại vé).

[Hình ảnh minh họa sơ đồ chọn tàu và loại vé:
SE5 → ngồi cứng / ngồi mềm
SE7 → ngồi cứng / ngồi mềm
SE35 → ngồi cứng / ngồi mềm]