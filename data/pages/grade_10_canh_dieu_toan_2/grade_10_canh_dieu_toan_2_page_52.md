$n(\Omega) = C_9^3 = \frac{9!}{3!.6!} = \frac{9.8.7}{6} = 84.$

Theo câu a), ta có $n(H) = 70$. Vậy xác suất của biến cố $H$ là

$P(H) = \frac{n(H)}{n(\Omega)} = \frac{70}{84} = \frac{5}{6}.$

# II. TÍNH CHẤT CỦA XÁC SUẤT

Xét phép thử $T$ với không gian mẫu là $\Omega$. Khi đó, ta có các tính chất sau:

• $P(\varnothing) = 0; P(\Omega) = 1;$
• $0 \leq P(A) \leq 1$ với mọi biến cố $A$;
• $P(\overline{A}) = 1 - P(A)$ với mọi biến cố $A$.

Chứng minh

• Xác suất của biến cố không là $P(\varnothing) = \frac{n(\varnothing)}{n(\Omega)} = \frac{0}{n(\Omega)} = 0;$

Xác suất của biến cố chắc chắn là $P(\Omega) = \frac{n(\Omega)}{n(\Omega)} = 1.$

• Do $P(A) = \frac{n(A)}{n(\Omega)}$ và $0 \leq n(A) \leq n(\Omega)$ nên $0 \leq P(A) \leq 1$ với mọi biến cố $A$.

• Do $n(\Omega \setminus A) = n(\Omega) - n(A)$ nên xác suất của biến cố $\overline{A}$ là:

$P(\overline{A}) = \frac{n(\Omega \setminus A)}{n(\Omega)} = \frac{n(\Omega) - n(A)}{n(\Omega)} = 1 - \frac{n(A)}{n(\Omega)} = 1 - P(A).$

## Ví dụ 7
Một hộp có 10 quả bóng trắng và 10 quả bóng đỏ; các quả bóng có kích thước và khối lượng giống nhau. Lấy ngẫu nhiên đồng thời 9 quả bóng trong hộp. Tính xác suất để trong 9 quả bóng được lấy ra có ít nhất một quả bóng màu đỏ.

Giải

Mỗi lần lấy ra đồng thời 9 quả bóng cho ta một tổ hợp chập 9 của 20 phần tử. Do đó, không gian mẫu $\Omega$ gồm các tổ hợp chập 9 của 20 phần tử và $n(\Omega) = C_{20}^9$.

Xét biến cố $K$: "Trong 9 quả bóng được lấy ra có ít nhất một quả bóng màu đỏ".

Khi đó biến cố đối của biến cố $K$ là biến cố $\overline{K}$: "Trong 9 quả bóng được lấy ra không có quả bóng màu đỏ nào", tức là cả 9 quả bóng được lấy ra có màu trắng.

[Hình minh họa: Có 15 bông hoa màu trắng và 15 bông hoa màu vàng. Người ta chọn ra đồng thời 10 bông hoa. Tính xác suất của biến cố "Trong 10 bông hoa được chọn ra có ít nhất một bông màu trắng".]