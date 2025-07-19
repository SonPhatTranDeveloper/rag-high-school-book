Để tính tứ phân vị thứ nhất Q₁ của mẫu số liệu ghép nhóm, trước hết ta xác định nhóm chứa Q₁, giả sử đó là nhóm thứ p: [a_p; a_p+1). Khi đó,

$Q_1 = a_p + \frac{n}{4} - (m_1 + ... + m_{p-1}) \cdot \frac{a_{p+1} - a_p}{m_p}$

trong đó, n là cỡ mẫu, m_p là tần số nhóm p, với p = 1 ta quy ước m₁ +...+ m_p-1 = 0.

Để tính tứ phân vị thứ ba Q₃ của mẫu số liệu ghép nhóm, trước hết ta xác định nhóm chứa Q₃. Giả sử đó là nhóm thứ p: [a_p; a_p+1). Khi đó,

$Q_3 = a_p + \frac{3n}{4} - (m_1 + ... + m_{p-1}) \cdot \frac{a_{p+1} - a_p}{m_p}$

trong đó, n là cỡ mẫu, m_p là tần số nhóm p, với p = 1 ta quy ước m₁ +...+ m_p-1 = 0.

Tứ phân vị thứ hai Q₂ chính là trung vị M_e.

Ví dụ 3. Tìm tứ phân vị thứ nhất Q₁ và tứ phân vị thứ ba Q₃ của mẫu số liệu ghép nhóm cho trong Ví dụ 2.

Giải

Cỡ mẫu là n = 56.

Tứ phân vị thứ nhất Q₁ là $\frac{x_{14} + x_{15}}{2}$. Do x₁₄, x₁₅ đều thuộc nhóm [12,5; 15,5) nên nhóm này chứa Q₁. Do đó, p = 2; a₂ = 12,5; m₂ = 12; m₁ = 3, a₃ - a₂ = 3 và ta có

$Q_1 = 12,5 + \frac{\frac{56}{4} - 3}{12} \cdot 3 = 15,25$

Với tứ phân vị thứ ba Q₃ là $\frac{x_{42} + x_{43}}{2}$. Do x₄₂, x₄₃ đều thuộc nhóm [18,5; 21,5) nên nhóm này chứa Q₃. Do đó, p = 4; a₄ = 18,5; m₄ = 24; m₁ + m₂ + m₃ = 3 + 12 + 15 = 30; a₅ - a₄ = 3 và ta có

$Q_3 = 18,5 + \frac{3 \cdot 56}{4} - 30 \cdot \frac{3}{24} = 20$

Nhận xét. Ta cũng có thể xác định nhóm chứa tứ phân vị thứ r nhờ tính chất: có khoảng $\left(\frac{r \cdot n}{4}\right)$ giá trị nhỏ hơn tứ phân vị này.

Luyện tập 3. Tìm tứ phân vị thứ nhất và tứ phân vị thứ ba cho mẫu số liệu ghép nhóm ở Luyện tập 2.

Ý nghĩa. Các tứ phân vị của mẫu số liệu ghép nhóm xấp xỉ cho các tứ phân vị của mẫu số liệu gốc, chúng chia mẫu số liệu thành 4 phần, mỗi phần chứa 25% giá trị.