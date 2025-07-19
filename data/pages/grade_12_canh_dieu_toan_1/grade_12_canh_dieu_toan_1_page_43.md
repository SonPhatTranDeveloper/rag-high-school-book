Ta có hệ phương trình sau:

$\begin{cases}
100 000 000a + 100c = 1,5 \\
3 000 000a + c = -0,01,
\end{cases}$

suy ra

$\begin{cases}
a = -\frac{1}{80 000 000} \\
c = \frac{11}{400}.
\end{cases}$

Vậy hàm số bậc ba cần tìm là

$f(x) = -\frac{1}{80 000 000}x^3 + \frac{1}{40 000}x^2 + \frac{11}{400}x + 50$.

7. Trong Ví dụ 9, góc độc của con đường trên đoạn [-1 000 ; 1 000] lớn nhất tại điểm nào?

Ví dụ 10 (Bài toán thiết kế mô hình đánh giá kĩ năng) Một trung tâm dạy nghề cần thiết kế mô hình đánh giá kĩ năng của một học viên theo học nghề đánh máy. Người ta có thể làm như sau:

• Để xây dựng mô hình toán học cho bài toán trên, ta sử dụng thống kê. Bằng cách khảo sát tốc độ đánh máy trung bình S (tính bằng từ trên phút) của học viên đó sau t tuần học (5 ≤ t ≤ 30), ta thu thập các số liệu thống kê được cho trong Bảng 1 (Nguồn: R. Larson and B. Edwards, Calculus 10e, Cengage 2014).

[Bảng 1 được hiển thị với các cột t và S, trong đó t có giá trị từ 5 đến 30 và S có giá trị tương ứng từ 38 đến 94]

• Ta cần chọn hàm số y = f(t) để biểu diễn các số liệu ở Bảng 1, tức là đồ thị của hàm số đó trên khoảng (0 ; + ∞) "gần" với các điểm A(5 ; 38), B(10 ; 56), C(15 ; 79), D(20 ; 90), E(25 ; 93), G(30 ; 94). Ngoài ra, do tốc độ đánh máy trung bình của học viên tăng theo thời gian t và chỉ đến một giới hạn M nào đó cho dù thời gian t có kéo dài đến vô cùng nên hàm số y = f(t) phải thỏa mãn thêm hai điều kiện: Hàm số đó đồng biến trên khoảng (0 ; + ∞) và $\lim_{t \to +\infty} f(t) = M \in \mathbb{R}, M > 94$.

Vì các hàm đa thức (với bậc lớn hơn hoặc bằng 1) không thỏa mãn hai điều kiện đó nên ta chọn một hàm phân thức hữu tỉ để biểu diễn các số liệu ở Bảng 1. Ta có thể chọn hàm số có dạng $f(t) = \frac{at + b}{ct + d}$ (ac ≠ 0) cho mục đích đó. Dựa vào Bảng 1, ta chọn hàm số

$f(t) = \frac{110t - 280}{t + 2}$ (t > 0).

a) Dựa theo mô hình đó, dự đoán tốc độ đánh máy trung bình của học viên đó sau 40 tuần (làm tròn kết quả đến hàng đơn vị của từ/phút).

b) Xem y = f(t) là một hàm số xác định trên khoảng (0 ; + ∞), hãy tìm tiệm cận ngang của đồ thị hàm số đó.

c) Nêu nhận xét về tốc độ đánh máy trung bình của học viên đó sau thời gian t ngày càng lớn.