• Tính số trung bình, trung vị, mốt (H.T.5).

[Hình ảnh mô tả một bảng tính Excel với các công thức tính trung bình, trung vị và mốt]

= AVERAGE(A2:A46)
= MEDIAN(A2:A46)
= MODE(A2:A46)

Hình T.5

Chú ý: Hàm MODE sẽ trả về giá trị #N/A nếu mẫu số liệu không có giá trị lặp lại. Trong trường hợp mẫu số liệu có nhiều mốt thì phần mềm bảng tính hiện thị giá trị mốt nhỏ nhất.

• Tính tứ phân vị (H.T.6).

[Hình ảnh mô tả một bảng tính Excel với các công thức tính tứ phân vị]

= QUARTILE(A2:A46,1)
= QUARTILE(A2:A46,2)
= QUARTILE(A2:A46,3)

Hình T.6

Chú ý: Kết quả tính tứ phân vị bằng phần mềm bảng tính có sự sai khác nhỏ so với cách tính được giới thiệu ở Bài 13 (do dùng công thức khác nhau).