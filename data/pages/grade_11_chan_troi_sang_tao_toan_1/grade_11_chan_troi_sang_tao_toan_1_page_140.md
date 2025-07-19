Dựa vào bảng số liệu trên, ban tổ chức muốn chọn ra khoảng 50% số vận động viên chạy nhanh nhất để tiếp tục thi vòng 2. Ban tổ chức nên chọn các vận động viên có thời gian chạy không quá bao nhiêu giây?

# 2. Tứ phân vị

Thời gian luyện tập trong một ngày (tính theo giờ) của một số vận động viên được ghi lại ở bảng sau:

| Thời gian luyện tập (giờ) | [0; 2) | [2; 4) | [4; 6) | [6; 8) | [8;10) |
|---------------------------|--------|--------|--------|--------|--------|
| Số vận động viên          |   3    |   8    |   12   |   12   |   4    |

Huấn luyện viên muốn xác định nhóm gồm 25% các vận động viên có số giờ luyện tập cao nhất. Hỏi huấn luyện viên nên chọn các vận động viên có thời gian luyện tập từ bao nhiêu giờ trở lên vào nhóm này?

Trong bảng, số vận động viên được khảo sát là $n = 3 + 8 + 12 + 12 + 4 = 39$.
Gọi $x_1, x_2, ..., x_{39}$ là thời gian luyện tập của 39 vận động viên được xếp theo thứ tự không giảm. Ta có $x_1, x_2, x_3 \in [0; 2)$; $x_4, ..., x_{11} \in [2; 4)$; $x_{12}, ..., x_{23} \in [4; 6)$; $x_{24}, ..., x_{35} \in [6; 8)$; $x_{36}, ..., x_{39} \in [8; 10)$. Do đó đối với dãy số liệu $x_1, x_2, ..., x_{39}$ thì:
• Tứ phân vị thứ nhất là $x_{10}$ thuộc nhóm [2; 4);
• Tứ phân vị thứ hai là $x_{20}$ thuộc nhóm [4; 6);
• Tứ phân vị thứ ba là $x_{30}$ thuộc nhóm [6; 8).
Ta nói nhóm [2; 4) là nhóm chứa tứ phân vị thứ nhất; nhóm [4; 6) là nhóm chứa tứ phân vị thứ hai; nhóm [6; 8) là nhóm chứa tứ phân vị thứ ba.

## Công thức xác định tứ phân vị của mẫu số liệu ghép nhóm
Tứ phân vị thứ hai của mẫu số liệu ghép nhóm, kí hiệu $Q_2$, cũng chính là trung vị của mẫu số liệu ghép nhóm.
Để tìm tứ phân vị thứ nhất của mẫu số liệu ghép nhóm, kí hiệu $Q_1$, ta thực hiện như sau:
• Giả sử nhóm $[u_m; u_{m+1})$ chứa tứ phân vị thứ nhất;
• $n_m$ là tần số của nhóm chứa tứ phân vị thứ nhất;
• $C = n_1 + n_2 + ... + n_{m-1}$.
Khi đó

$$Q_1 = u_m + \frac{\frac{n}{4} - C}{n_m} \cdot (u_{m+1} - u_m).$$

Tương tự, để tìm tứ phân vị thứ ba của mẫu số liệu ghép nhóm, kí hiệu $Q_3$, ta thực hiện như sau:
• Giả sử nhóm $[u_j; u_{j+1})$ chứa tứ phân vị thứ ba;
• $n_j$ là tần số của nhóm chứa tứ phân vị thứ ba;
• $C = n_1 + n_2 + ... + n_{j-1}$.
Khi đó

$$Q_3 = u_j + \frac{\frac{3n}{4} - C}{n_j} \cdot (u_{j+1} - u_j).$$