Tính chất của tích vô hướng

Với ba vectơ $\vec{u}$, $\vec{v}$, $\vec{w}$ bất kì và mọi số thực $k$, ta có:
• $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$ (tính chất giao hoán);
• $\vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w}$ (tính chất phân phối đối với phép cộng);
• $(k\vec{u}) \cdot \vec{v} = k(\vec{u} \cdot \vec{v}) = \vec{u} \cdot (k\vec{v})$.

Chú ý. Từ các tính chất trên, ta có thể chứng minh được:

$\vec{u} \cdot (\vec{v} - \vec{w}) = \vec{u} \cdot \vec{v} - \vec{u} \cdot \vec{w}$ (tính chất phân phối đối với phép trừ);

$(\vec{u} + \vec{v})^2 = \vec{u}^2 + 2\vec{u} \cdot \vec{v} + \vec{v}^2$; $(\vec{u} - \vec{v})^2 = \vec{u}^2 - 2\vec{u} \cdot \vec{v} + \vec{v}^2$;

$(\vec{u} + \vec{v}) \cdot (\vec{u} - \vec{v}) = \vec{u}^2 - \vec{v}^2$.

Ví dụ 4. (Ứng dụng của vectơ trong bài toán hình học)

Cho điểm $M$ thay đổi trên đường tròn tâm $O$ ngoại tiếp tam giác đều $ABC$ cho trước. Chứng minh rằng $MA^2 + MB^2 + MC^2$ không đổi.

Giải

Cách 1 (Dùng tọa độ). Xét hệ trục tọa độ có gốc trùng với tâm $O$ của đường tròn ngoại tiếp tam giác $ABC$. Gọi tọa độ của các điểm là $A(x_A; y_A)$, $B(x_B; y_B)$, $C(x_C; y_C)$, $M(x; y)$. Vì tam giác $ABC$ đều nên tâm đường tròn ngoại tiếp $O(0; 0)$ đồng thời là trọng tâm của tam giác. Do đó $x_A + x_B + x_C = 0$ và $y_A + y_B + y_C = 0$.

Vì $OM^2 = OA^2 = R^2$ nên $x^2 + y^2 = x_A^2 + y_A^2 = R^2$.
Vậy $MA^2 = (x - x_A)^2 + (y - y_A)^2 = (x^2 + y^2) + (x_A^2 + y_A^2) - 2xx_A - 2yy_A = 2R^2 - 2xx_A - 2yy_A$.

Tương tự $MB^2 = 2R^2 - 2xx_B - 2yy_B$ và $MC^2 = 2R^2 - 2xx_C - 2yy_C$.

Do đó $MA^2 + MB^2 + MC^2 = 6R^2 - 2x(x_A + x_B + x_C) - 2y(y_A + y_B + y_C) = 6R^2$ (không đổi).

Cách 2 (Dùng tích vô hướng). (H.4.44)

Vì tam giác $ABC$ đều nên tâm $O$ của đường tròn ngoại tiếp đồng thời là trọng tâm của tam giác. Vậy $\vec{OA} + \vec{OB} + \vec{OC} = \vec{0}$.

Giả sử $(O)$ có bán kính $R$. Ta có:

$MA^2 + MB^2 + MC^2 = \overline{MA}^2 + \overline{MB}^2 + \overline{MC}^2$

$= (\overline{MO} - \overline{OA})^2 + (\overline{MO} - \overline{OB})^2 + (\overline{MO} - \overline{OC})^2$

$= 3\overline{MO}^2 + 2\overline{MO} \cdot \overline{OA} + 2\overline{MO} \cdot \overline{OB} + 2\overline{MO} \cdot \overline{OC} + \overline{OA}^2 + \overline{OB}^2 + \overline{OC}^2$

$= 3MO^2 + 2\overline{MO} \cdot (\overline{OA} + \overline{OB} + \overline{OC}) + 3R^2 = 3R^2 + 2\overline{MO} \cdot \vec{0} + 3R^2 = 6R^2$.

Vậy $MA^2 + MB^2 + MC^2$ không đổi khi $M$ thay đổi trên $(O)$.

[Hình 4.44: Hình vẽ minh họa tam giác ABC ngoại tiếp đường tròn tâm O, với điểm M nằm trên đường tròn]