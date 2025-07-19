Em có biết?

Dãy số Fibonacci và tỉ lệ vàng

Ta đã biết dãy Fibonacci cho bởi hệ thức truy hồi:

$u_1 = u_2 = 1, u_n = u_{n-1} + u_{n-2}$

với $n > 2$.

Chia hai vế cho $u_{n-1}$ và đặt $v_n = \frac{u_n}{u_{n-1}}$, ta có công thức

$v_n = 1 + \frac{1}{v_{n-1}}$.

Dãy $(v_n)$ có giới hạn là một số dương $r$ thỏa mãn phương trình $r = 1 + \frac{1}{r}$, hay tương đương $r^2 - r - 1 = 0$. Giải phương trình này ta được $r = \frac{1+\sqrt{5}}{2}$.

Đây chính là tỉ lệ vàng (golden ratio) được sử dụng trong kiến trúc, hội họa, tôn giáo, ...
Dãy Fibonacci và tỉ lệ vàng cũng xuất hiện nhiều trong thế giới tự nhiên.

[Hình ảnh minh họa dãy Fibonacci bằng các hình vuông xếp chồng lên nhau, với các số 1, 1, 2, 3, 5, 8 được ghi trong các hình vuông tương ứng.]

Dãy số logistic

Trong sinh thái học, người ta sử dụng dãy $(p_n)$ cho bởi công thức truy hồi $p_{n+1} = kp_n(1-p_n)$ để mô phỏng hệ sinh thái của một loài (động vật hoặc thực vật), trong đó $p_n$ là tỉ lệ giữa số lượng cá thể theo thời gian và sức chứa của môi trường, $k$ là hệ số phụ thuộc đặc điểm của loài và điều kiện môi trường. Dãy số này được gọi là dãy logistic, do nhà sinh học Robert May đưa ra năm 1976. Tùy thuộc hệ số $k$ và giá trị ban đầu $p_0$, ta có thể dự đoán sự thay đổi của hệ trong tương lai. Đặc biệt, trong trường hợp dãy $(p_n)$ có giới hạn là một số dương, ta nói hệ sinh thái của loài là ổn định.

(Theo Stewart, Calculus, Nhà xuất bản Cengage Learning)