2. Các phép toán về giới hạn hữu hạn của dãy số

Ở trên ta đã biết $\lim\left(3+\frac{1}{n^2}\right)=\lim\frac{3n^2+1}{n^2}=1$.

a) Tìm các giới hạn $\lim 3$ và $\lim\frac{1}{n^2}$.

b) Từ đó, nếu nhận xét về $\lim\left(3+\frac{1}{n^2}\right)$ và $\lim 3 + \lim\frac{1}{n^2}$.

Để tìm giới hạn hữu hạn của dãy số, người ta thường vẫn dùng các phép toán về giới hạn hữu hạn của dãy số.

Cho $\lim u_n = a$, $\lim v_n = b$ và $c$ là hằng số. Khi đó:
• $\lim(u_n + v_n) = a + b$                • $\lim(u_n - v_n) = a - b$
• $\lim(c . u_n) = c . a$                  • $\lim(u_n . v_n) = a . b$
• $\lim\frac{u_n}{v_n} = \frac{a}{b}$ $(b \neq 0)$    • Nếu $u_n \geq 0, \forall n \in \mathbb{N}^*$ thì $a \geq 0$ và $\lim\sqrt{u_n} = \sqrt{a}$

Ví dụ 4. Tìm các giới hạn sau:

a) $\lim\frac{3n+2}{2n-1}$;                b) $\lim\frac{\sqrt{9n^2+1}}{n}$.

Giải

a) Ta có $\frac{3n+2}{2n-1} = \frac{3+\frac{2}{n}}{2-\frac{1}{n}}$ (chia cả tử và mẫu cho $n$).

Từ đó $\lim\frac{3n+2}{2n-1} = \lim\frac{3+\frac{2}{n}}{2-\frac{1}{n}} = \frac{\lim\left(3+\frac{2}{n}\right)}{\lim\left(2-\frac{1}{n}\right)} = \frac{\lim 3 + 2\lim\frac{1}{n}}{\lim 2 - \lim\frac{1}{n}} = \frac{3+2.0}{2-0} = \frac{3}{2}$.

b) Ta có $\frac{\sqrt{9n^2+1}}{n} = \sqrt{\frac{9n^2+1}{n^2}} = \sqrt{9+\frac{1}{n^2}}$.

Từ đó $\lim\frac{\sqrt{9n^2+1}}{n} = \lim\sqrt{9+\frac{1}{n^2}} = \sqrt{\lim\left(9+\frac{1}{n^2}\right)} = \sqrt{\lim 9 + \lim\frac{1}{n^2}} = \sqrt{9+0} = 3$.

Tìm các giới hạn sau:

a) $\lim\frac{2n^2+3n}{n^2+1}$;            b) $\lim\frac{\sqrt{4n^2+3}}{n}$.