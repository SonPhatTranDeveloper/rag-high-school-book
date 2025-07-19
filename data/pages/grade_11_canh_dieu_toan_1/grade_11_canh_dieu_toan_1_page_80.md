a) Chứng tỏ hàm số h(t) liên tục trên tập xác định.

b) Dựa vào đồ thị hãy xác định $\lim_{t \to 2} (-2t^2 + 8t)$.

[Hình 16: Đồ thị biểu diễn hàm số h(t) với trục hoành là t(s) và trục tung là h(m). Đồ thị là một đường cong parabol đi qua gốc tọa độ, đạt đỉnh tại điểm (2, 8) và cắt trục hoành tại một điểm khác ngoài gốc tọa độ.]

TÌM HIỂU THÊM

# 1. Giới hạn của hàm số

Ở bài học trước, ta đã định nghĩa khái niệm $\lim_{x \to x_0} f(x) = L$ trong trường hợp hàm số f(x) xác định trên khoảng K hoặc trên $K \setminus \{x_0\}$, ở đó khoảng K chứa điểm $x_0$ và khoảng K có một trong những dạng sau: (a ; b), (- ∞ ; b), (a ; + ∞), (- ∞ ; + ∞).

Tuy nhiên, các hàm số thường gặp có thể có miền xác định ở dạng phức tạp hơn, chẳng hạn miền xác định có thể có dạng [0 ; 3) và $x_0 = 1 \in [0; 3)$. Vì thế, ta cần mở rộng khái niệm trên cho những hàm số có miền xác định ở dạng phức tạp hơn.

Cụ thể, ta có thể làm như sau:

Cho hàm số f(x) xác định trên tập hợp $K \subset \mathbb{R}$ và cho $x_0 \in \mathbb{R}$. Giả sử có số thực a > 0 sao cho $(x_0 - a; x_0 + a) \subset K$ hoặc $(x_0 - a; x_0 + a) \setminus \{x_0\} \subset K$.

Ta nói hàm số f(x) có giới hạn là số L khi x dần tới $x_0$ nếu với dãy số $(x_n)$ bất kì, $x_n \in (x_0 - a; x_0 + a) \setminus \{x_0\}$ và $x_n \to x_0$, ta có $f(x_n) \to L$.

# 2. Ứng dụng tính liên tục của hàm số vào xét sự tồn tại nghiệm của phương trình

Cho hàm số y = f(x) liên tục trên đoạn [a ; b] sao cho f(a) < 0, f(b) > 0. Khi đó, đồ thị hàm số y = f(x) trên đoạn [a ; b] là một đường cong liên nét đi từ điểm M(a ; f(a)) nằm dưới trục hoành đến điểm N(b; f(b)) nằm phía trên trục hoành (Hình 17). Vì thế, trong khoảng (a ; b) đồ thị đó sẽ cắt trục hoành, tức là tồn tại ít nhất một điểm c ∈ (a ; b) sao cho f(c) = 0. Nói cách khác, phương trình f(x) = 0 có ít nhất một nghiệm nằm trong khoảng (a ; b).

Trong trường hợp tổng quát, ta có định lí sau:

Nếu hàm số y = f(x) liên tục trên đoạn [a ; b] và f(a) . f(b) < 0,

thì tồn tại ít nhất một điểm c ∈ (a ; b) sao cho f(c) = 0.

[Hình 17: Đồ thị minh họa cho định lí trên, với trục hoành là x, trục tung là y. Đường cong f(x) đi từ điểm M(a; f(a)) dưới trục hoành, cắt trục hoành tại một điểm giữa a và b, rồi đi lên điểm N(b; f(b)) trên trục hoành.]

Ví dụ: Chứng minh rằng phương trình $x^3 + x - 4 = 0$ có ít nhất một nghiệm.

Giải

Xét hàm số $f(x) = x^3 + x - 4$. Ta có: f(0) = - 4; f(2) = 6. Suy ra f(0).f(2) < 0. Do f(x) liên tục trên [0 ; 2] nên phương trình f(x) = 0 có ít nhất một nghiệm thuộc khoảng (0 ; 2).