Chú ý: Để có hình ảnh trực quan về dãy số, ta thường biểu diễn các số hạng của nó trên trục số. Chẳng hạn, xét dãy số $(u_n)$ với $u_n = \frac{(-1)^n}{2^n}$. Năm số hạng đầu của dãy số này là $u_1 = -\frac{1}{2}, u_2 = \frac{1}{4}, u_3 = -\frac{1}{8}, u_4 = \frac{1}{16}, u_5 = -\frac{1}{32}$ và được biểu diễn trên trục số như sau:

[Hình ảnh minh họa trục số với các điểm $u_1, u_2, u_3, u_4, u_5$ được đánh dấu tương ứng tại các vị trí -1/2, 1/4, -1/8, 1/16, -1/32 trên trục số từ -1 đến 1]

# 3. DÃY SỐ TĂNG, DÃY SỐ GIẢM VÀ DÃY SỐ BỊ CHẶN

## H04. Nhận biết dãy số tăng, dãy số giảm

a) Xét dãy số $(u_n)$ với $u_n = 3n - 1$. Tính $u_{n+1}$ và so sánh với $u_n$.

b) Xét dãy số $(v_n)$ với $v_n = \frac{1}{n^2}$. Tính $v_{n+1}$ và so sánh với $v_n$.

- Dãy số $(u_n)$ được gọi là dãy số tăng nếu ta có $u_{n+1} > u_n$ với mọi $n \in \mathbb{N}^*$.
- Dãy số $(u_n)$ được gọi là dãy số giảm nếu ta có $u_{n+1} < u_n$ với mọi $n \in \mathbb{N}^*$.

## Ví dụ 7. Xét tính tăng, giảm của dãy số $(u_n)$, với $u_n = -2n + 5$.

Giải

Ta có
$u_{n+1} - u_n = [-2(n + 1) + 5] - (-2n + 5) = (-2n - 3) + 2n - 5 = -2 < 0$, tức là $u_{n+1} < u_n, \forall n \in \mathbb{N}^*$.

Vậy $(u_n)$ là dãy số giảm.

## Luyện tập 3. Xét tính tăng, giảm của dãy số $(u_n)$, với $u_n = \frac{1}{n+1}$.

## H05. Nhận biết dãy số bị chặn

Cho dãy số $(u_n)$ với $u_n = \frac{n+1}{n}, \forall n \in \mathbb{N}^*$.

a) So sánh $u_n$ và 1.

b) So sánh $u_n$ và 2.

- Dãy số $(u_n)$ được gọi là bị chặn trên nếu tồn tại một số $M$ sao cho $u_n \leq M$ với mọi $n \in \mathbb{N}^*$.
- Dãy số $(u_n)$ được gọi là bị chặn dưới nếu tồn tại một số $m$ sao cho $u_n \geq m$ với mọi $n \in \mathbb{N}^*$.
- Dãy số $(u_n)$ được gọi là bị chặn nếu nó vừa bị chặn trên vừa bị chặn dưới, tức là tồn tại các số $m, M$ sao cho $m \leq u_n \leq M$ với mọi $n \in \mathbb{N}^*$.

## Ví dụ 8. Xét tính bị chặn của dãy số $(u_n)$, với $u_n = \frac{n-1}{n}$.