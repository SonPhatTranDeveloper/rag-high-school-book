HD4. Tương tự như HD3, sau khi khai triển $(a + b)^5$, ta thu được một tổng gồm $2^5$ đơn thức có dạng $x \cdot y \cdot z \cdot t \cdot u$, trong đó mỗi kí hiệu $x, y, z, t, u$ là $a$ hoặc $b$. Chẳng hạn, nếu $x, z$ là $a$, còn $y, t, u$ là $b$ thì ta có đơn thức $a \cdot b \cdot a \cdot b \cdot b$, thu gọn là $a^2b^3$. Để có đơn thức này, thì trong 5 nhân tử $x, y, z, t, u$ có 3 nhân tử là $b$, 2 nhân tử còn lại là $a$. Khi đó số đơn thức đồng dạng với $a^2b^3$ trong tổng là $C_5^3$.

Lập luận tương tự như trên, dùng kiến thức về tổ hợp, hãy cho biết, trong tổng nhận được nêu trên có bao nhiêu đơn thức đồng dạng với mỗi đơn thức thu gọn sau:

• $a^5$; • $a^4b$; • $a^3b^2$; • $a^2b^3$; • $ab^4$; • $b^5$ ?

Từ HD4, sau khi rút gọn các đơn thức đồng dạng ta thu được:

$(a + b)^5 = C_5^0a^5 + C_5^1a^4b + C_5^2a^3b^2 + C_5^3a^2b^3 + C_5^4ab^4 + C_5^5b^5$
$= a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$.

[Hình minh họa: Một hộp thoại chứa nội dung "Trong khai triển nhị thức Newton $(a + b)^5$, các đơn thức có bậc là 5." và một hình ảnh robot đang giơ tay]

Ví dụ 2. Khai triển $(x + 3)^5$.

Giải

Thay $a = x$ và $b = 3$ trong công thức khai triển của $(a + b)^5$, ta được:

$(x + 3)^5 = x^5 + 5 \cdot x^4 \cdot 3 + 10 \cdot x^3 \cdot 3^2 + 10 \cdot x^2 \cdot 3^3 + 5 \cdot x \cdot 3^4 + 3^5$
$= x^5 + 15x^4 + 90x^3 + 270x^2 + 405x + 243$.

Luyện tập 2. Khai triển $(3x - 2)^5$.

Nhận xét. Các công thức khai triển $(a + b)^n$ với $n \in \{4; 5\}$, là một công cụ hiệu quả để tính chính xác hoặc xấp xỉ một số đại lượng mà không cần dùng máy tính.

Vận dụng

a) Dùng hai số hạng đầu tiên trong khai triển của $(1 + 0,05)^4$ để tính giá trị gần đúng của $1,05^4$.

b) Dùng máy tính cầm tay tính giá trị của $1,05^4$ và tính sai số tuyệt đối của giá trị gần đúng nhận được ở câu a.

BÀI TẬP

8.12. Khai triển các đa thức:
a) $(x - 3)^4$;                b) $(3x - 2y)^4$;
c) $(x + 5)^4 + (x - 5)^4$;    d) $(x - 2y)^5$.

8.13. Tìm hệ số của $x^4$ trong khai triển của $(3x - 1)^5$.

8.14. Biểu diễn $(3 + \sqrt{2})^5 - (3 - \sqrt{2})^5$ dưới dạng $a + b\sqrt{2}$ với $a, b$ là các số nguyên.