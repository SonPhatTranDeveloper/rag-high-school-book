Bạn có biết?

# DÃY SỐ FIBONACCI

Fibonacci (Phi-bô-na-xi) (còn có tên là Leonardo Fibonacci) là một nhà toán học nổi tiếng người Ý. Trong cuốn sách Liber Abaci, năm 1202, ông có viết bài toán sau:

"Một đôi thỏ (gồm một thỏ đực và một thỏ cái) cứ mỗi tháng đẻ được một đôi thỏ con (cũng gồm một thỏ đực và một thỏ cái); mỗi đôi thỏ con, khi tròn hai tháng tuổi, lại mỗi tháng đẻ ra một đôi thỏ con, và quá trình sinh nở cứ thế tiếp diễn. Hỏi sau một năm sẽ có tất cả bao nhiêu đôi thỏ, nếu đầu năm (tháng 1) có một đôi thỏ sơ sinh?"

(Nguồn: https://www.britannica.com/science/Fibonacci-number)

[Hình 4. Leonardo Fibonacci: Hình vẽ phác họa chân dung một người đàn ông với trang phục cổ điển, bên cạnh là một biểu đồ hình xoắn ốc]

Rõ ràng ở tháng 1, cũng như ở tháng 2, chỉ có một đôi thỏ. Sang tháng 3, đôi thỏ này sẽ đẻ ra một đôi thỏ con, vì thế ở tháng 3 sẽ có 1 + 1 = 2 đôi thỏ. Sang tháng 4, vì chỉ có đôi thỏ ban đầu sinh con nên ở tháng này có 1 + 2 = 3 đôi thỏ. Sang tháng 5, hai đôi thỏ gồm đôi thỏ ban đầu và đôi thỏ được sinh ra ở tháng 3 cũng sinh con nên tháng này có 3 + 2 = 5 đôi thỏ; ...

[Hình 5: Biểu đồ minh họa sự sinh sản của thỏ qua các tháng, với số lượng thỏ tăng dần từ 1 đến 5 đôi]

Khái quát, nếu kí hiệu $F_n$ là số đôi thỏ có ở tháng thứ $n$, thì với $n \geq 3$, ta có:

$F_n = F_{n-1}$ + số đôi thỏ được sinh ra ở tháng thứ $n$.

Do các đôi thỏ được sinh ra ở tháng thứ $(n - 1)$ chưa thể sinh con ở tháng thứ $n$ và mỗi đôi thỏ có ở tháng thứ $(n - 2)$ sẽ sinh ra một đôi thỏ con, nên số đôi thỏ con được sinh ra ở tháng thứ $n$ chính bằng $F_{n-2}$ (số đôi thỏ có ở tháng thứ $(n - 2)$).

Như vậy: $F_n = F_{n-1} + F_{n-2}$.

Việc giải quyết bài toán trên của Fibonacci dẫn đến việc khảo sát dãy số:

$\begin{cases}
F_1 = 1 \\
F_2 = 1 \\
F_n = F_{n-1} + F_{n-2} \quad (n \geq 3).
\end{cases}$

Dãy số trên sau này được nhà toán học Pháp Edouard Lucas gọi là dãy số Fibonacci.

Áp dụng quy luật dãy số trên, ta tính được số đôi thỏ sau một năm là $F_{12} = 144$.