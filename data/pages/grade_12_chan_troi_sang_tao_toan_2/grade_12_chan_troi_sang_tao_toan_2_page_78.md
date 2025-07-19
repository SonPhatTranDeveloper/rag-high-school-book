Vào mỗi buổi sáng ở tuyến phố H, xác suất xảy ra tắc đường khi trời mưa và không mưa lần lượt là 0,7 và 0,2. Xác suất có mưa vào một buổi sáng là 0,1. Tính xác suất để sáng đó tuyến phố H bị tắc đường.

[Hình ảnh mô tả cảnh tắc đường trong thành phố với nhiều xe cộ đang xếp hàng dài trên đường phố đông đúc.]

Hình 2

# 2. Công thức Bayes

Khảo sát thị lực của 100 học sinh, ta thu được bảng số liệu sau:

| Giới tính | Nữ | Nam |
|-----------|-----|-----|
| Thị lực |  |  |
| Có tật khúc xạ | 12 | 18 |
| Không có tật khúc xạ | 38 | 32 |

Chọn ngẫu nhiên 1 bạn trong 100 học sinh trên.

a) Biết rằng bạn đó có tật khúc xạ, tính xác suất bạn đó là học sinh nam.

b) Biết rằng bạn đó là học sinh nam, tính xác suất bạn đó có tật khúc xạ.

Bảng số liệu trên được gọi là bảng số liệu 2 × 2. Từ bảng số liệu, ta thấy có 50 học sinh nam và 50 học sinh nữ tham gia khảo sát, trong đó có 12 + 18 = 30 học sinh có tật khúc xạ và 38 + 32 = 70 học sinh không có tật khúc xạ.

Gọi A là biến cố "Học sinh được chọn bị tật khúc xạ" và B là biến cố "Học sinh được chọn là nữ". Từ bảng số liệu trên, ta tính được các xác suất sau:

$P(A) = \frac{12+18}{100} = 0,3; P(B) = \frac{12+38}{100} = 0,5; P(AB) = \frac{12}{100} = 0,12.$

Hơn nữa, ta cũng tính được các xác suất có điều kiện sau:

$P(A|B) = \frac{12}{12+38} = 0,24; P(B|A) = \frac{12}{12+18} = 0,4.$

Từ đây suy ra

$\frac{P(B)P(A|B)}{P(A)} = \frac{0,5 \cdot 0,24}{0,3} = 0,4 = P(B|A),$

và

$\frac{P(A)P(B|A)}{P(B)} = \frac{0,3 \cdot 0,4}{0,5} = 0,24 = P(A|B).$

Một cách tổng quát, từ định nghĩa xác suất có điều kiện với $P(A) > 0$, ta có

$P(B|A) = \frac{P(B)P(A|B)}{P(A)}.$