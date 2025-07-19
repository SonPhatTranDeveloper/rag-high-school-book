Ví dụ 4 Dãy số được nêu trong phần mở đầu được gọi là dãy số Fibonacci.

Dãy số Fibonacci là dãy số $(u_n)$ được xác định bởi:
$u_1 = 1, u_2 = 1$ và $u_n = u_{n-1} + u_{n-2}$ với mọi $n \geq 3$ (9)

Viết mười số hạng đầu của dãy số $(u_n)$.

Giải
Ta có: $u_1 = u_2 = 1$.
Để tìm $u_3$, thay $n = 3$ vào công thức (9), ta được: $u_3 = u_2 + u_1 = 1 + 1 = 2$.
Để tìm $u_4$, thay $n = 4$ vào công thức (9), ta được: $u_4 = u_3 + u_2 = 2 + 1 = 3$.
Cứ như thế, ta tìm được mười số hạng đầu của dãy số $(u_n)$ là: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.

III. DÃY SỐ TĂNG, DÃY SỐ GIẢM

4 Cho dãy số $(u_n)$ với $u_n = n^2$. Tính $u_{n+1}$. Từ đó, hãy so sánh $u_{n+1}$ và $u_n$ với mọi $n \in \mathbb{N}^*$.

• Dãy số $(u_n)$ được gọi là dãy số tăng nếu $u_{n+1} > u_n$ với mọi $n \in \mathbb{N}^*$.
• Dãy số $(u_n)$ được gọi là dãy số giảm nếu $u_{n+1} < u_n$ với mọi $n \in \mathbb{N}^*$.

Ví dụ 5 Chứng minh rằng dãy số $(u_n)$ với $u_n = 3n - 2$ là một dãy số tăng.

Giải
Với mọi $n \in \mathbb{N}^*$, ta có: $u_{n+1} = 3(n+1) - 2 = 3n + 1$.
Xét hiệu: $u_{n+1} - u_n = (3n + 1) - (3n - 2) = 3 > 0$
hay $u_{n+1} > u_n$ với mọi $n \in \mathbb{N}^*$.
Vậy dãy số $(u_n)$ là một dãy số tăng.

Chú ý
Không phải mọi dãy số đều là dãy số tăng hay dãy số giảm. Chẳng hạn, dãy số $(u_n)$ với $u_n = (-1)^n$ có dạng khai triển: -1, 1, -1, 1, -1, ... không là dãy số tăng, cũng không là dãy số giảm.

3 Cho dãy số $(u_n)$ với $u_n = \frac{n-3}{3n+1}$. Tìm $u_{33}, u_{333}$ và viết dãy số dưới dạng khai triển.

4 Chứng minh rằng dãy số $(v_n)$ với $v_n = \frac{1}{3^n}$ là một dãy số giảm.