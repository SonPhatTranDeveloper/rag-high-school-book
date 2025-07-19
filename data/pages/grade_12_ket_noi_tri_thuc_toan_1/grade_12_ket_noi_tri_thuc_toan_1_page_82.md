Bài 10: PHƯƠNG SAI VÀ ĐỘ LỆCH CHUẨN

THUẬT NGỮ:
• Phương sai
• Độ lệch chuẩn

KIẾN THỨC, KĨ NĂNG:
• Tính phương sai, độ lệch chuẩn của mẫu số liệu ghép nhóm.
• Hiểu ý nghĩa, vai trò của phương sai, độ lệch chuẩn trong việc đo mức độ phân tán.

Để xác định độ ổn định của một máy đo độ ẩm không khí, người ta dùng máy này để đo 20 lần. Nếu độ lệch chuẩn của mẫu số liệu đo lớn hơn 0,15 thì người ta sẽ đưa máy đo đi sửa chữa. Trong một lần lấy mẫu, kĩ thuật viên có được mẫu số liệu ghép nhóm sau:

Độ ẩm (%) | [52; 52,1) | [52,1; 52,2) | [52,2; 52,3) | [52,3; 52,4) | [52,4; 52,5)
----------|------------|--------------|--------------|--------------|-------------
Tần số    |     1      |      5       |      8       |      4       |      2

Liệu có cần đưa máy đo này đi sửa chữa hay không?

1. PHƯƠNG SAI VÀ ĐỘ LỆCH CHUẨN

HD1. Trở lại bài toán trong tình huống mở đầu. Gọi $x_1,\ldots,x_{20}$ là các kết quả đo (mẫu số liệu gốc).
a) Có thể tính được chính xác phương sai và độ lệch chuẩn của mẫu số liệu gốc hay không?
b) Thảo luận và đề xuất ước lượng cho phương sai và độ lệch chuẩn của mẫu số liệu gốc.

Xét mẫu số liệu ghép nhóm cho bởi Bảng 3.1.

• Phương sai của mẫu số liệu ghép nhóm, kí hiệu là $s^2$, là một số được tính theo công thức sau:

$$s^2 = \frac{m_1(x_1 - \bar{x})^2 + \ldots + m_k(x_k - \bar{x})^2}{n};$$

trong đó, $n = m_1 + \ldots + m_k; x_i = \frac{a_i + a_{i+1}}{2}$ với $i = 1, 2,\ldots, k$ là giá trị đại diện cho nhóm $[a_i; a_{i+1})$ và $\bar{x} = \frac{m_1x_1 + \ldots + m_kx_k}{n}$ là số trung bình của mẫu số liệu ghép nhóm.

• Độ lệch chuẩn của mẫu số liệu ghép nhóm, kí hiệu là s, là căn bậc hai số học của phương sai của mẫu số liệu ghép nhóm, tức là $s = \sqrt{s^2}$.

Nhận xét. Ta có thể tính phương sai theo công thức: $s^2 = \frac{1}{n}(m_1 \cdot x_1^2 + \ldots + m_k \cdot x_k^2) - (\bar{x})^2$.

Độ lệch chuẩn có cùng đơn vị với đơn vị của mẫu số liệu.