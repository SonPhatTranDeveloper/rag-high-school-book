a) Hãy liệt kê tất cả các cách Lan có thể chọn 3 cuốn sách từ 4 cuốn sách. Có tất cả bao nhiêu cách?

b) Lan dự định đọc lần lượt từng cuốn. Lan có bao nhiêu cách xếp thứ tự 3 cuốn đã chọn?

c) Lan có bao nhiêu cách chọn 3 cuốn sách từ 4 cuốn sách và xếp theo thứ tự để đọc lần lượt từng cuốn một?

Mỗi cách chọn 3 cuốn sách từ 4 cuốn sách A, B, C, D được gọi là một tổ hợp chập 3 của 4 phần tử A, B, C, D.

Ta biết rằng, với mỗi cách chọn 3 cuốn sách (chẳng hạn A, B, C) thì có $P_3 = 3!$ cách xếp chúng theo thứ tự. Mỗi thứ tự này chính là một chỉnh hợp chập 3 của 4 phần tử A, B, C, D. Do đó, nếu kí hiệu $C_4^3$ là số tổ hợp chập 3 của 4 phần tử thì ta có hệ thức $C_4^3 \cdot 3! = A_4^3$ hay $C_4^3 = \frac{A_4^3}{3!}$.

Tổng quát, ta có định nghĩa sau đây:

Cho tập hợp A có n phần tử (n ≥ 1).
Mỗi tập con gồm k phần tử (1 ≤ k ≤ n) của A được gọi là một tổ hợp chập k của n phần tử.

Kí hiệu $C_n^k$ là số tổ hợp chập k của n phần tử (1 ≤ k ≤ n).

Người ta chứng minh được rằng:

Số các tổ hợp chập k của n phần tử (1 ≤ k ≤ n) bằng

$C_n^k = \frac{n!}{k!(n-k)!}$

Chú ý: Người ta quy ước $C_n^0 = 1$.

Ví dụ 5

Tổ Một có 9 thành viên. Tuần tới là phiên trực nhật của tổ, nên cần phân công 4 bạn đi bê ghế của lớp cho buổi chào cờ.

a) Tổ có bao nhiêu cách phân công 4 bạn đi bê ghế?

b) Tổ có bao nhiêu cách chọn 5 bạn không phải đi bê ghế?

[Hình 6: Minh họa một nhóm gồm 5 người đang đứng cùng nhau, trong đó có 4 người mặc áo đỏ và 1 người mặc áo xanh.]