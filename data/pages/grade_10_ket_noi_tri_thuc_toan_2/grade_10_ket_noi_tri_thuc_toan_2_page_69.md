Giải
Mỗi cách chọn lần lượt 4 trong 30 học sinh để trồng bốn cây khác nhau là một chính hợp chập 4 của 30.
Vậy số cách chọn là $A_{30}^4 = 657 720$.

Chú ý
• Hoán vị sắp xếp tất cả các phần tử của tập hợp, còn chính hợp chọn ra một số phần tử và sắp xếp chúng.
• Mỗi hoán vị của n phần tử cũng chính là một chính hợp chập n của n phần tử đó. Vì vậy $P_n = A_n^n$.

Luyện tập 2. Trong một giải đua ngựa gồm 12 con ngựa, người ta chỉ quan tâm đến 3 con ngựa: con nhanh nhất, nhanh nhì và nhanh thứ ba. Hỏi có bao nhiêu kết quả có thể xảy ra?

3. TỔ HỢP

HD3. Trở lại HD2.
a) Hãy cho biết sự khác biệt khi chọn ra hai bạn ở câu HD2a và HD2b.
b) Từ kết quả tính được ở câu HD2b (áp dụng chính hợp), hãy chỉ ra cách tính kết quả ở câu HD2a.

Nhận xét
Mỗi cách chọn ra 2 bạn từ 4 bạn ở HD2a được gọi là một tổ hợp chập 2 của 4. Vì không cần sắp xếp thứ tự hai bạn được chọn nên số cách chọn sẽ giảm đi 2! lần so với việc chọn ra hai bạn có sắp xếp thứ tự (ở câu HD2b).

Tổng quát ta có:

Một tổ hợp chập k của n là một cách chọn k phần tử từ một tập hợp n phần tử (với k, n là các số tự nhiên, $0 \leq k \leq n$).
Số các tổ hợp chập k của n, kí hiệu là $C_n^k$, được tính bằng công thức
$C_n^k = \frac{n!}{(n-k)!k!}$ $(0 \leq k \leq n)$.

Chú ý
• $C_n^k = \frac{A_n^k}{k!}$
• Chính hợp và tổ hợp có điểm giống nhau là đều chọn một số phần tử trong một tập hợp, nhưng khác nhau ở chỗ, chính hợp là chọn có xếp thứ tự, còn tổ hợp là chọn không xếp thứ tự.

Ví dụ 3. Có 7 bạn học sinh muốn chơi cờ cá ngựa, nhưng mỗi ván chỉ có 4 người chơi. Hỏi có bao nhiêu cách chọn 4 bạn chơi cờ cá ngựa?

[Hình minh họa: Một nhân vật hoạt hình đang giơ ngón tay cái lên]

[Khung thông tin: Ngày 28-11-1959, Chủ tịch Hồ Chí Minh đã phát động ngày "Tết trồng cây" với mong muốn: Trong mười năm, đất nước ta phong cảnh sẽ ngày càng tươi đẹp hơn, khí hậu điều hòa hơn,...]