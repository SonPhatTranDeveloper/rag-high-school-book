Một dãy số có thể cho bằng:
• Liệt kê các số hạng (chỉ dùng cho các dãy hữu hạn và có ít số hạng);
• Công thức của số hạng tổng quát;
• Phương pháp mô tả;
• Phương pháp truy hồi.

Ví dụ 3. Tìm năm số hạng đầu và số hạng thứ 100 của dãy số cho bởi công thức sau:

a) $u_n = 2n$;                b) $u_n = \frac{(-1)^n}{n}$.

Giải
a) Năm số hạng đầu của dãy số là: 2, 4, 6, 8, 10.
   Số hạng thứ 100 của dãy số là $u_{100} = 2 \cdot 100 = 200$.

b) Năm số hạng đầu của dãy số là: $-1, \frac{1}{2}, -\frac{1}{3}, \frac{1}{4}, -\frac{1}{5}$.

   Số hạng thứ 100 của dãy số là $u_{100} = \frac{(-1)^{100}}{100} = -\frac{1}{100}$.

Ví dụ 4. Xét dãy số gồm tất cả các số nguyên tố theo thứ tự tăng dần. Viết năm số hạng đầu của dãy số đó.

Giải. Năm số hạng đầu của dãy số là: 2, 3, 5, 7, 11.

Chú ý. Dãy số gồm tất cả các số nguyên tố ở Ví dụ 4 được cho bởi phương pháp mô tả (số hạng thứ n là số nguyên tố thứ n). Cho đến nay người ta vẫn chưa biết có hay không một công thức tính số nguyên tố thứ n theo n (với n bất kì), hoặc là một hệ thức tính số nguyên tố thứ n theo một vài số nguyên tố đứng trước nó.

Ví dụ 5. Cho dãy số xác định bằng hệ thức truy hồi:
$u_1 = 1, u_n = 3u_{n-1} + 2$ với $n \geq 2$.
Viết ba số hạng đầu của dãy số này.

Giải
Ta có: $u_1 = 1, u_2 = 3u_1 + 2 = 3 \cdot 1 + 2 = 5, u_3 = 3u_2 + 2 = 3 \cdot 5 + 2 = 17$.

Ví dụ 6. Giải bài toán ở tình huống mở đầu.

Giải
Ở đây ta có $n = 2030 - 2020 = 10$. Vậy số dân của thành phố đó vào năm 2030 sẽ là
$P_{10} = 500 \cdot (1,02)^{10} \approx 609$ (nghìn người).

Luyện tập 2.
a) Viết năm số hạng đầu của dãy số $(u_n)$ với số hạng tổng quát $u_n = n!$.

b) Viết năm số hạng đầu của dãy số Fibonacci $(F_n)$ cho bởi hệ thức truy hồi
$\begin{cases}
F_1 = 1, F_2 = 1 \\
F_n = F_{n-1} + F_{n-2} \quad (n \geq 3).
\end{cases}$

[Hình minh họa: Một robot đang giơ tay chào và một nhân vật hoạt hình đang giơ ngón tay cái lên]

[Ghi chú bên lề: 
- "Số nguyên tố là số tự nhiên lớn hơn 1 mà chỉ có hai ước số là 1 và chính nó."
- "Hệ thức truy hồi là hệ thức biểu thị số hạng thứ n của dãy số qua số hạng (hay vài số hạng) đứng trước nó."]