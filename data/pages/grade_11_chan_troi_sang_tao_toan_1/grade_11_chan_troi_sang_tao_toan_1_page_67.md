Ta thừa nhận một số giới hạn cơ bản dưới đây. Chúng thường được sử dụng để tìm giới hạn của nhiều dãy số khác.

• $\lim_{n \to \infty} \frac{1}{n^k} = 0$, với $k$ nguyên dương bất kì.
• $\lim_{n \to \infty} q^n = 0$, với $q$ là số thực thoả mãn $|q| < 1$.

Ví dụ 2. Áp dụng giới hạn cơ bản, tìm $\lim_{n \to \infty} \frac{1}{(\sqrt{3})^n}$.

Giải

Ta có $\frac{1}{(\sqrt{3})^n} = (\frac{1}{\sqrt{3}})^n$.

Do $|\frac{1}{\sqrt{3}}| = \frac{1}{\sqrt{3}} < 1$ nên $\lim_{n \to \infty} \frac{1}{(\sqrt{3})^n} = \lim_{n \to \infty} (\frac{1}{\sqrt{3}})^n = 0$.

Tìm các giới hạn sau:

a) $\lim_{n \to \infty} \frac{1}{n^2}$;

b) $\lim_{n \to \infty} (-\frac{3}{4})^n$.

Giới hạn hữu hạn của dãy số

Cho dãy số $(u_n)$ với $u_n = \frac{2n+1}{n}$

a) Cho dãy số $(v_n)$ với $v_n = u_n - 2$. Tìm giới hạn $\lim_{n \to \infty} v_n$.

b) Biểu diễn các điểm $u_1, u_2, u_3, u_4$ trên trục số. Có nhận xét gì về vị trí của các điểm $u_n$ khi $n$ trở nên rất lớn?

Ta nói dãy số $(u_n)$ có giới hạn hữu hạn là số $a$ (hay $u_n$ dần tới $a$) khi $n$ dần tới dương vô cực, nếu $\lim_{n \to \infty} (u_n - a) = 0$. Khi đó, ta viết $\lim_{n \to \infty} u_n = a$ hay $\lim u_n = a$ hay $u_n \to a$ khi $n \to \infty$.

Chú ý: Nếu $u_n = c$ ($c$ là hằng số) thì $\lim_{n \to \infty} u_n = \lim c = c$.

Ví dụ 3. Dùng định nghĩa, tìm giới hạn $\lim_{n \to \infty} \frac{3n^2 + 1}{n^2}$.

Giải

Đặt $u_n = \frac{3n^2 + 1}{n^2}$. Ta có $u_n = 3 + \frac{1}{n^2}$ hay $u_n - 3 = \frac{1}{n^2}$.

Suy ra $\lim_{n \to \infty} (u_n - 3) = \lim_{n \to \infty} \frac{1}{n^2} = 0$.

Theo định nghĩa, ta có $\lim_{n \to \infty} u_n = 3$. Vậy $\lim_{n \to \infty} \frac{3n^2 + 1}{n^2} = 3$.

Tìm các giới hạn sau:

a) $\lim_{n \to \infty} (2 + (\frac{2}{3})^n)$;

b) $\lim_{n \to \infty} (\frac{1-4n}{n})$.