Giải

| Khoảng tuổi | [20; 30) | [30; 40) | [40; 50) | [50; 60) | [60; 70) |
|--------------|----------|----------|----------|----------|----------|
| Giá trị đại diện | 25 | 35 | 45 | 55 | 65 |
| Độ dài của nhóm | 10 | 10 | 10 | 10 | 10 |

Một số quy tắc ghép nhóm của mẫu số liệu
Mỗi mẫu số liệu có thể được ghép nhóm theo nhiều cách khác nhau nhưng thường tuân theo một số quy tắc sau:
- Sử dụng từ $k = 5$ đến $k = 20$ nhóm. Cỡ mẫu càng lớn thì cần càng nhiều nhóm số liệu. Các nhóm có cùng độ dài bằng $L$ thỏa mãn $R < k \cdot L$, trong đó $R$ là khoảng biến thiên, $k$ là số nhóm.
- Giá trị nhỏ nhất của mẫu thuộc vào nhóm $[u_1; u_2)$ và càng gần $u_1$ càng tốt. Giá trị lớn nhất của mẫu thuộc nhóm $[u_k; u_{k+1})$ và càng gần $u_{k+1}$ càng tốt.

Ví dụ 2. Cân nặng của 28 học sinh nam lớp 11 được cho như sau:
55,4 62,6 54,2 56,8 58,8 59,4 60,7 58    59,5 63,6 61,8 52,3 63,4 57,9
49,7 45,1 56,2 63,2 46,1 49,6 59,1 55,3 55,8 45,5 46,8 54    49,2 52,6
Hãy chia mẫu dữ liệu trên thành 5 nhóm, lập bảng tần số ghép nhóm và xác định giá trị đại diện cho mỗi nhóm.

Giải
Khoảng biến thiên của mẫu số liệu trên là $R = 63,6 - 45,1 = 18,5$.

Độ dài mỗi nhóm $L > \frac{R}{k} = \frac{18,5}{5} = 3,7$.

Ta chọn $L = 4$ và chia dữ liệu thành các nhóm [45; 49), [49; 53), [53; 57), [57; 61), [61; 65).

Khi đó ta có bảng tần số ghép nhóm sau:

| Cân nặng | [45; 49) | [49; 53) | [53; 57) | [57; 61) | [61; 65) |
|----------|----------|----------|----------|----------|----------|
| Giá trị đại diện | 47 | 51 | 55 | 59 | 63 |
| Số học sinh | 4 | 5 | 7 | 7 | 5 |

Chú ý:
• Các đầu mút của các nhóm có thể không là giá trị của mẫu số liệu.
• Ta hay gặp các bảng số liệu ghép nhóm là số nguyên, chẳng hạn như bảng thống kê số lỗi chính tả trong bài kiểm tra giữa học kì 1 môn Ngữ Văn của học sinh khối 11 như sau:

| Số lỗi | [1; 2] | [3; 4] | [5; 6] | [7; 8] | [9; 10] |
|--------|--------|--------|--------|--------|---------|
| Số bài | 122 | 75 | 14 | 5 | 2 |

Bảng số liệu này không có dạng như Bảng 1. Để thuận lợi cho việc tính các số đặc trưng cho bảng số liệu này, người ta hiệu chỉnh về dạng như Bảng 1 bằng cách thêm và bớt 0,5 đơn vị vào đầu mút bên phải và bên trái của mỗi nhóm số liệu như sau:

| Số lỗi | [0,5; 2,5) | [2,5; 4,5) | [4,5; 6,5) | [6,5; 8,5) | [8,5; 10,5) |
|--------|------------|------------|------------|------------|-------------|
| Số bài | 122 | 75 | 14 | 5 | 2 |