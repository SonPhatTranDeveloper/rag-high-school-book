b) Số e và lôgarit tự nhiên

Bài toán lãi kép liên tục và số e

Ta đã biết: Nếu đem gửi ngân hàng một số vốn ban đầu là P theo thể thức lãi kép với lãi suất hàng năm không đổi là r và chia mỗi năm thành m kì tính lãi thì sau t năm (tức là sau tm kì) số tiền thu được (cả vốn lẫn lãi) là

$A_m = P\left(1 + \frac{r}{m}\right)^m$

Nếu kì tính lãi được chia càng ngày càng nhỏ, tức là tính lãi hàng ngày, hàng giờ, hàng phút, hàng giây,... thì dẫn đến việc tính giới hạn của dãy số $A_m$ khi $m \to +\infty$. Ta có:

$A_m = P\left(1 + \frac{r}{m}\right)^m = P\left[\left(1 + \frac{1}{\frac{m}{r}}\right)^{\frac{m}{r}}\right]^r$

Để tính giới hạn $\lim_{m \to +\infty} A_m$, ta cần xét giới hạn $\lim_{m \to +\infty} \left(1 + \frac{1}{m}\right)^m$.

Một cách tổng quát, ta xét giới hạn $\lim_{x \to +\infty} \left(1 + \frac{1}{x}\right)^x$.

Người ta chứng minh được giới hạn trên tồn tại, nó là một số vô tỉ có giá trị bằng 2,718281828... và kí hiệu là e. Vậy

$e = \lim_{x \to +\infty} \left(1 + \frac{1}{x}\right)^x \approx 2,7183$

Từ các kết quả trên suy ra $\lim_{m \to +\infty} A_m = Pe^r$.

Thể thức tính lãi khi $m \to +\infty$ theo cách trên gọi là thể thức lãi kép liên tục.

Như vậy, với số vốn ban đầu là P, theo thể thức lãi kép liên tục, lãi suất hàng năm không đổi là r thì sau t năm, số tiền thu được cả vốn lẫn lãi sẽ là

$A = Pe^{rt}$

Công thức trên gọi là công thức lãi kép liên tục.

Lôgarit tự nhiên

Ta có định nghĩa sau:

Lôgarit cơ số e của một số dương M gọi là lôgarit tự nhiên của M, kí hiệu là ln M (đọc là lôgarit Nêpe của M).

Ví dụ 6. Biết thời gian cần thiết (tính theo năm) để tăng gấp đôi số tiền đầu tư theo thể thức lãi kép liên tục với lãi suất không đổi r mỗi năm được cho bởi công thức sau:

$t = \frac{\ln2}{r}$

Tính thời gian cần thiết để tăng gấp đôi một khoản đầu tư khi lãi suất là 6% mỗi năm (làm tròn kết quả đến chữ số thập phân thứ nhất).