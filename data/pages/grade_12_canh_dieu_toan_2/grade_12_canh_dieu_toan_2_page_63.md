VI. MỘT SỐ ỨNG DỤNG CỦA PHƯƠNG TRÌNH MẶT PHẲNG TRONG THỰC TIỄN

Phương trình mặt phẳng có nhiều ứng dụng trong thực tiễn như trong thiết kế xây dựng, tính toán các yếu tố kĩ thuật, ... Ta sẽ tìm hiểu qua một số ví dụ sau đây.

Ví dụ 15: Hình 17 minh họa hình ảnh hai mái nhà của một nhà kho trong không gian với hệ tọa độ Oxyz (đơn vị trên mỗi trục tọa độ là mét). Các bức tường của nhà kho đều được xây vuông góc với mặt đất.

[Hình 17 mô tả một hình khối chữ nhật trong không gian ba chiều với các điểm được đánh dấu A(10;0;9), B(10;20;10), C(0;20;10), D(0;0;9), P(5;0;6), và điểm Q nằm trên mặt phẳng phía trên.]

a) Lập phương trình của hai mặt phẳng tương ứng mỗi mái nhà.
b) Tìm tọa độ của điểm Q.
c) Tìm tọa độ của vectơ $\vec{PQ}$.

Giải

a) Hai mặt phẳng tương ứng mỗi mái nhà là (ABP) và (CDP).

• Do mặt phẳng (ABP) có cặp vectơ chỉ phương là $\vec{AB} = (0;20;1)$, $\vec{AP} = (-5;0;-3)$ nên có một vectơ pháp tuyến là:

$[\vec{AB},\vec{AP}] = \begin{vmatrix}
20 & 1 & 0 \\
0 & -3 & -5
\end{vmatrix} = (-60;-5;100)$.

Mà mặt phẳng (ABP) đi qua điểm A(10;0;9) nên có phương trình là:
$-60(x-10) - 5(y-0) + 100(z-9) = 0 \Leftrightarrow 12x + y - 20z + 60 = 0$.

• Do mặt phẳng (CDP) có cặp vectơ chỉ phương là $\vec{DP} = (5;0;-3)$, $\vec{DC} = (0;20;1)$ nên có một vectơ pháp tuyến là:

$[\vec{DP},\vec{DC}] = \begin{vmatrix}
0 & -3 & 5 \\
20 & 1 & 0
\end{vmatrix} = (60;-5;100)$.

Mà mặt phẳng (CDP) đi qua điểm D(0;0;9) nên có phương trình là:
$60(x-0) - 5(y-0) + 100(z-9) = 0 \Leftrightarrow 12x - y + 20z - 180 = 0$.

b) Vì các bức tường của nhà kho đều được xây vuông góc với mặt đất nên với hệ tọa độ trên ta có Q(x;20;z).

Do điểm Q thuộc mặt phẳng (ABP) nên tọa độ của điểm Q thỏa mãn:
$12x + 20 - 20z + 60 = 0$, tức là $3x - 5z = -20$.