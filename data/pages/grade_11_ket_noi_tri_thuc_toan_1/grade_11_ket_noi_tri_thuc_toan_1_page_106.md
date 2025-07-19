1. GIỚI HẠN HỮU HẠN CỦA DÃY SỐ

HD1. Nhận biết dãy số có giới hạn là 0

Cho dãy số $(u_n)$ với $u_n = \frac{(-1)^n}{n}$.

a) Biểu diễn năm số hạng đầu của dãy số này trên trục số.

b) Bắt đầu từ số hạng nào của dãy, khoảng cách từ $u_n$ đến 0 nhỏ hơn 0,01?

Ta nói dãy số $(u_n)$ có giới hạn là 0 khi $n$ dần tới dương vô cực, nếu $|u_n|$ có thể nhỏ hơn một số dương bé tùy ý, kể từ một số hạng nào đó trở đi, kí hiệu $\lim_{n \to +\infty} u_n = 0$ hay $u_n \to 0$ khi $n \to +\infty$.

Ví dụ 1. Xét dãy số $u_n = \frac{1}{n^2}$. Giải thích vì sao dãy số này có giới hạn là 0.

Giải

Dãy số này có giới hạn là 0, bởi vì $|u_n| = \frac{1}{n^2}$ có thể nhỏ hơn một số dương bé tùy ý khi $n$ đủ lớn.

Chẳng hạn, để $|u_n| < 0,0001$ tức là $\frac{1}{n^2} < 10^{-4}$, ta cần $n^2 > 10\ 000$ hay $n > 100$. Như vậy, các số hạng của dãy kể từ số hạng thứ 101 đều có giá trị tuyệt đối nhỏ hơn 0,0001.

Chú ý. Từ định nghĩa dãy số có giới hạn 0, ta có các kết quả sau:

• $\lim_{n \to +\infty} \frac{1}{n^k} = 0$ với $k$ là một số nguyên dương;

• $\lim_{n \to +\infty} q^n = 0$ nếu $|q| < 1$;

• Nếu $|u_n| \leq v_n$ với mọi $n \geq 1$ và $\lim_{n \to +\infty} v_n = 0$ thì $\lim_{n \to +\infty} u_n = 0$.

Luyện tập 1. Chứng minh rằng $\lim_{n \to +\infty} \frac{(-1)^{n-1}}{3^n} = 0$.

HD2. Nhận biết dãy số có giới hạn hữu hạn

Cho dãy số $(u_n)$ với $u_n = \frac{n + (-1)^n}{n}$. Xét dãy số $(v_n)$ xác định bởi $v_n = u_n - 1$.
Tính $\lim_{n \to +\infty} v_n$.

Ta nói dãy số $(u_n)$ có giới hạn là số thực $a$ khi $n$ dần tới dương vô cực nếu $\lim_{n \to +\infty} (u_n - a) = 0$, kí hiệu $\lim_{n \to +\infty} u_n = a$ hay $u_n \to a$ khi $n \to +\infty$.