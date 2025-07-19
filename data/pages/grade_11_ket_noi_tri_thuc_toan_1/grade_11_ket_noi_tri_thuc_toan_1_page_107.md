Ví dụ 2. Xét dãy số $(u_n)$ với $u_n = \frac{2n + 1}{n}$. Chứng minh rằng $\lim_{n \to +\infty} u_n = 2$.

Giải
Ta có $u_n - 2 = \frac{2n + 1}{n} - 2 = \frac{(2n + 1) - 2n}{n} = \frac{1}{n} \to 0$ khi $n \to +\infty$.
Do vậy $\lim_{n \to +\infty} u_n = 2$.

Chú ý. Nếu $u_n = c$ (c là hằng số) thì $\lim_{n \to +\infty} u_n = c$.

Luyện tập 2. Cho dãy số $(u_n)$ với $u_n = \frac{3 \cdot 2^n - 1}{2^n}$. Chứng minh rằng $\lim_{n \to +\infty} u_n = 3$.

Vận dụng 1. Một quả bóng cao su được thả từ độ cao 5 m xuống một mặt sàn. Sau mỗi lần chạm sàn, quả bóng nảy lên độ cao bằng $\frac{2}{3}$ độ cao trước đó. Giả sử rằng quả bóng luôn chuyển động vuông góc với mặt sàn và quá trình này tiếp diễn vô hạn lần. Giả sử $u_n$ là độ cao (tính bằng mét) của quả bóng sau lần nảy lên thứ n. Chứng minh rằng dãy số $(u_n)$ có giới hạn là 0.

2. ĐỊNH LÍ VỀ GIỚI HẠN HỮU HẠN CỦA DÃY SỐ

HD3. Hình thành quy tắc tính giới hạn

Cho hai dãy số $(u_n)$ và $(v_n)$ với $u_n = 2 + \frac{1}{n}, v_n = 3 - \frac{2}{n}$.

Tính và so sánh: $\lim_{n \to +\infty} (u_n + v_n)$ và $\lim_{n \to +\infty} u_n + \lim_{n \to +\infty} v_n$.

Tổng quát, ta có các quy tắc tính giới hạn sau đây:

a) Nếu $\lim_{n \to +\infty} u_n = a$ và $\lim_{n \to +\infty} v_n = b$ thì
   $\lim_{n \to +\infty} (u_n + v_n) = a + b$;
   $\lim_{n \to +\infty} (u_n \cdot v_n) = a \cdot b$;
   $\lim_{n \to +\infty} (u_n - v_n) = a - b$;
   $\lim_{n \to +\infty} \frac{u_n}{v_n} = \frac{a}{b}$ (nếu $b \neq 0$).
b) Nếu $u_n \geq 0$ với mọi n và $\lim_{n \to +\infty} u_n = a$ thì
   $a \geq 0$ và $\lim_{n \to +\infty} \sqrt{u_n} = \sqrt{a}$.

Ví dụ 3. Tìm $\lim_{n \to +\infty} \frac{n^2 + n + 1}{2n^2 - 1}$.

Giải
Áp dụng các quy tắc tính giới hạn, ta được

$\lim_{n \to +\infty} \frac{n^2 + n + 1}{2n^2 - 1} = \lim_{n \to +\infty} \frac{1 + \frac{1}{n} + \frac{1}{n^2}}{2 - \frac{1}{n^2}} = \frac{\lim_{n \to +\infty} (1 + \frac{1}{n} + \frac{1}{n^2})}{\lim_{n \to +\infty} (2 - \frac{1}{n^2})} = \frac{1}{2}$.

[Hình minh họa: Một nhân vật hoạt hình nữ đang giải thích với nét mặt vui vẻ và tay giơ lên minh họa]

[Hình minh họa: Một nhân vật hoạt hình nam đang chỉ tay lên trên với nét mặt vui vẻ]

[Ghi chú ở góc phải trên: $\lim_{n \to +\infty} u_n = a$ khi và chỉ khi $\lim_{n \to +\infty} (u_n - a) = 0$.]

[Ghi chú ở góc phải dưới: Để tính giới hạn của dãy số dạng phân thức, ta chia cả tử thức và mẫu thức cho lũy thừa cao nhất của n, rồi áp dụng các quy tắc tính giới hạn.]