§ 4 NHỊ THỨC NEWTON

Làm thế nào để khai triển $(a + b)^4, (a + b)^5$ một cách nhanh chóng?

Ta đã biết $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 = 1 \cdot a^3 + 3 \cdot a^2 \cdot b^1 + 3 \cdot a^1 \cdot b^2 + 1 \cdot b^3$.

a) Tính $C_3^0, C_3^1, C_3^2, C_3^3$.

b) Chọn số thích hợp cho ? trong khai triển sau:
$(a + b)^3 = C_3^?, a^3 | C_3^?, a^2 | C_3^?, a^1 | C_3^?, a^0 | C_3^?, b^3$.

$(a+b)^4 = C_4^0 \cdot a^{4-0} + C_4^1 \cdot a^{4-1} \cdot b^1 + C_4^2 \cdot a^{4-2} \cdot b^2 + C_4^3 \cdot b^3$.
Mỗi số hạng trong tổng đều có dạng $C_4^k \cdot a^{4-k} \cdot b^k$.

Tương tự như vậy, ta có các khai triển sau:

$(a-b)^4 = C_4^0 \cdot a^{4-0} + C_4^1 \cdot a^{4-1} \cdot b^1 + C_4^2 \cdot a^{4-2} \cdot b^2 + C_4^3 \cdot a^{4-3} \cdot b^3 + C_4^4 \cdot b^4$
$= C_4^0a^4 + C_4^1a^3b + C_4^2a^2b^2 + C_4^3ab^3 + C_4^4b^4$.

$(a+b)^5 = C_5^0 \cdot a^{5-0} + C_5^1 \cdot a^{5-1} \cdot b^1 + C_5^2 \cdot a^{5-2} \cdot b^2 + C_5^3 \cdot a^{5-3} \cdot b^3 + C_5^4 \cdot a^{5-4} \cdot b^4 + C_5^5 \cdot b^5$
$= C_5^0a^5 + C_5^1a^4b + C_5^2a^3b^2 + C_5^3a^2b^3 + C_5^4ab^4 + C_5^5b^5$.

$(a+b)^4 = C_4^0a^4 + C_4^1a^3b + C_4^2a^2b^2 + C_4^3ab^3 + C_4^4b^4$
$= a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$.

$(a+b)^5 = C_5^0a^5 + C_5^1a^4b + C_5^2a^3b^2 + C_5^3a^2b^3 + C_5^4ab^4 + C_5^5b^5$
$= a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$.

Những công thức khai triển nói trên là công thức nhị thức Newton $(a - b)^n$ ứng với $n = 4, n = 5$.
Bằng cách như thế, ta có thể khai triển được $(a + b)^n$ với $n$ là số nguyên dương lớn hơn 5.
Công thức khai triển cụ thể được trình bày trong Chuyên đề học tập Toán 10.