2.7. Chị Hương vay trả góp một khoản tiền 100 triệu đồng và đồng ý trả dần 2 triệu đồng mỗi tháng với lãi suất 0,8% số tiền còn lại của mỗi tháng.

Gọi $A_n (n \in \mathbb{N})$ là số tiền còn nợ (triệu đồng) của chị Hương sau n tháng.

a) Tìm lần lượt $A_0, A_1, A_2, A_3, A_4, A_5, A_6$ để tính số tiền còn nợ của chị Hương sau 6 tháng.

b) Dự đoán hệ thức truy hồi đối với dãy số $(A_n)$.

Em có biết?

Dãy số Fibonacci

Fibonacci là nhà toán học nổi tiếng người Italia. Trong cuốn sách Liber Abaci (Sách tính) của ông, được viết năm 1202, có bài toán sau:

"Một đôi thỏ (gồm một thỏ đực và một thỏ cái) cứ mỗi tháng đẻ được một đôi thỏ con (cũng gồm một thỏ đực và thỏ cái); mỗi đôi thỏ con, khi tròn 2 tháng tuổi, sau mỗi tháng đẻ ra một đôi thỏ con, và quá trình sinh nở cứ thế tiếp diễn. Hỏi sau n tháng có bao nhiêu đôi thỏ, nếu đầu năm (tháng Giêng) có một đôi thỏ sơ sinh?".

Việc giải quyết bài toán nói trên dẫn đến việc nghiên cứu dãy số $(F_n)$ cho bởi hệ thức truy hồi

$$\begin{cases}
F_1 = 1, F_2 = 1 \\
F_n = F_{n-1} + F_{n-2} (n \geq 3).
\end{cases}$$

Dãy số này được gọi là dãy số Fibonacci và các số hạng của nó được gọi là các số Fibonacci.

Người ta chứng minh được rằng số hạng tổng quát của dãy Fibonacci cho bởi

$$F_n = \frac{1}{\sqrt{5}} \left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right].$$

Dãy số Fibonacci có rất nhiều tính chất đẹp, chẳng hạn:

1) $F_n^2 = F_{n-1}F_{n+1} + (-1)^{n-1}$ với mọi $n \geq 2$;

2) $F_1 + F_3 + F_5 + ... + F_{2n-1} = F_{2n}$ với mọi $n \geq 1$;

3) $F_n^2 + F_{n+1}^2 = F_{2n+1}$ với mọi $n \geq 1$.

Dãy số Fibonacci liên quan mật thiết với nhiều vấn đề của Toán học, Vật lí, Hội họa, Âm nhạc.

Các số Fibonacci xuất hiện ở khắp nơi trong thiên nhiên.

Hầu hết các bông hoa có số cánh hoa là một trong các số: $F_4, F_5, F_8, F_7, F_8, F_9, F_{10}, F_{11}$. Chẳng hạn, hoa loa kèn có 3 cánh, hoa mao lương vàng có 5 cánh, hoa cải ô rô thường có 8 cánh, hoa cúc vạn thọ có 13 cánh, hoa cúc tây có 21 cánh, hoa cúc thường có 34, hoặc 55 hoặc 89 cánh.

[Hình ảnh chân dung của một người đàn ông đội mũ trùm đầu, có vẻ là Fibonacci]

Fibonacci (1170 - 1250)