Mốt của mẫu số liệu ghép nhóm, kí hiệu $M_o$, được tính theo công thức sau:

$$ M_o = u + \left( \frac{n_i - n_{i-1}}{2n_i - n_{i-1} - n_{i+1}} \right) \cdot g. $$

Chú ý: • Khi $i = 0$ thì $n_0 = 0$; • Khi $i = m$ thì $n_{m+1} = 0$.

Ví dụ 7 Kết quả kiểm tra môn Toán của lớp 11D như sau:

5 6 7 5 6 9 10 8 5 5 4 5 4 5 7 4 5 8 9 10
5 3 5 6 5 7 5 8 4 9 5 6 5 6 8 8 7 9 7 9

a) Lập bảng tần số ghép nhóm của mẫu số liệu trên có bốn nhóm ứng với bốn nửa khoảng: [3 ; 5), [5 ; 7), [7 ; 9), [9 ; 11).

b) Mốt của mẫu số liệu ghép nhóm trên là bao nhiêu (làm tròn kết quả đến hàng phần mười)?

Tìm mốt của mẫu số liệu trong Ví dụ 6 (làm tròn các kết quả đến hàng phần mười).

Giải

a) Bảng 14 là bảng tần số ghép nhóm cho kết quả kiểm tra môn Toán của lớp 11D.

b) Ta thấy: Nhóm 2 ứng với nửa khoảng [5 ; 7) là nhóm có tần số lớn nhất với $u = 5$; $g = 2$; $n_2 = 18$. Nhóm 1 có tần số $n_1 = 5$, nhóm 3 có tần số $n_3 = 10$.

Áp dụng công thức, ta có mốt của mẫu số liệu là:

$$ M_o = 5 + \left( \frac{18 - 5}{2 \cdot 18 - 5 - 10} \right) \cdot 2 \approx 6,2. $$

[Bảng 14 được hiển thị với các cột Nhóm và Tần số]

Nhóm | Tần số
[3 ; 5) | 5
[5 ; 7) | 18
[7 ; 9) | 10
[9 ; 11) | 7
n = 40

2. Ý nghĩa

Như ta đã biết, mốt của một mẫu số liệu không ghép nhóm đặc trưng cho số lần lặp đi lặp lại nhiều nhất tại một giá trị của mẫu số liệu đó. Vì thế, có thể dùng mốt để đo xu thế trung tâm của mẫu số liệu khi mẫu số liệu có nhiều giá trị trùng nhau.

Bằng cách ghép nhóm mẫu số liệu và tính toán mốt của mẫu số liệu ghép nhóm, ta nhận được giá trị mới cũng có thể dùng để đo xu thế trung tâm của mẫu số liệu đã cho.

Mốt của mẫu số liệu sau khi ghép nhóm xấp xỉ với mốt của mẫu số liệu không ghép nhóm ban đầu. Một mẫu số liệu ghép nhóm có thể có nhiều mốt.