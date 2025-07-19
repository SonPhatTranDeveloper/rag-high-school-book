Tổng quát ta có

Một hoán vị của một tập hợp có n phần tử là một cách sắp xếp có thứ tự n phần tử đó (với n là một số tự nhiên, n ≥ 1).

Số các hoán vị của tập hợp có n phần tử, kí hiệu là $P_n$, được tính bằng công thức

$P_n = n \cdot (n - 1) \cdot (n - 2) \cdots 2 \cdot 1.$

Chú ý: Kí hiệu $n \cdot (n - 1) \cdot (n - 2) \cdots 2 \cdot 1$ là n! (đọc là n giai thừa), ta có: $P_n = n!$. Chẳng hạn $P_3 = 3! = 3 \cdot 2 \cdot 1 = 6$.
Quy ước 0! = 1.

Ví dụ 1. Từ các chữ số 6, 7, 8 và 9 có thể lập được bao nhiêu số có bốn chữ số khác nhau?

Giải
Mỗi cách sắp xếp bốn chữ số đã cho để lập thành một số có bốn chữ số khác nhau là một hoán vị của bốn chữ số đó.
Vậy số các số có bốn chữ số khác nhau có thể lập được là $P_4 = 4! = 24$.

Luyện tập 1. Trong một cuộc thi điền kinh gồm 6 vận động viên chạy trên 6 đường chạy. Hỏi có bao nhiêu cách xếp các vận động viên vào các đường chạy đó?

2. CHỈNH HỢP

HD2. Trong lớp 10T có bốn bạn Tuấn, Hương, Việt, Dung đủ tiêu chuẩn tham gia cuộc thi hùng biện của trường.

a) Giáo viên cần chọn ra hai bạn phụ trách nhóm trên. Hỏi có bao nhiêu cách chọn hai bạn từ bốn bạn nêu trên?

b) Có bao nhiêu cách chọn hai bạn, trong đó một bạn làm nhóm trưởng, một bạn làm nhóm phó?

Nhận xét: Trong HD2b, mỗi cách sắp xếp hai bạn từ bốn bạn làm nhóm trưởng, nhóm phó được gọi là một chỉnh hợp chập 2 của 4. Để tính số các chỉnh hợp ta dùng quy tắc nhân. Tổng quát ta có:

Một chỉnh hợp chập k của n là một cách sắp xếp có thứ tự k phần tử từ một tập hợp n phần tử (với k, n là các số tự nhiên, 1 ≤ k ≤ n).

Số các chỉnh hợp chập k của n, kí hiệu là $A_n^k$, được tính bằng công thức

$A_n^k = n \cdot (n - 1) \cdots (n - k + 1)$ hay $A_n^k = \frac{n!}{(n - k)!}$ (1 ≤ k ≤ n).

Ví dụ 2. Một lớp có 30 học sinh, giáo viên cần chọn lần lượt 4 học sinh trồng bốn cây khác nhau để tham gia lễ phát động Tết trồng cây của trường. Hỏi giáo viên có bao nhiêu cách chọn?