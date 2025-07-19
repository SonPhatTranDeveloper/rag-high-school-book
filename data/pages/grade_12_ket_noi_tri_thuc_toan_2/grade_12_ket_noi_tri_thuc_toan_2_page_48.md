3. VỊ TRÍ TƯƠNG ĐỐI GIỮA HAI ĐƯỜNG THẲNG

HD6. Xác định vị trí tương đối giữa hai đường thẳng

Trong không gian Oxyz, cho hai đường thẳng $\Delta_1, \Delta_2$ lần lượt đi qua các điểm $A_1(x_1; y_1; z_1), A_2(x_2; y_2; z_2)$ và tương ứng có vecto chỉ phương $\vec{u_1} = (a_1; b_1; c_1), \vec{u_2} = (a_2; b_2; c_2)$ (H.5.29).

a) Tìm điều kiện đối với $\vec{u_1}$ và $\vec{u_2}$ để $\Delta_1$ và $\Delta_2$ song song hoặc trùng nhau.

b) Giả sử $[\vec{u_1}, \vec{u_2}] \neq 0$ và $\vec{A_1A_2} \cdot [\vec{u_1}, \vec{u_2}] = 0$ thì $\Delta_1$ và $\Delta_2$ có cắt nhau hay không?

c) Giả sử $\vec{A_1A_2} \cdot [\vec{u_1}, \vec{u_2}] = 0$ thì $\Delta_1$ và $\Delta_2$ có chéo nhau hay không?

[Hình 5.29: Hình minh họa hai đường thẳng $\Delta_1$ và $\Delta_2$ trong không gian Oxyz với các vecto chỉ phương $\vec{u_1}$ và $\vec{u_2}$]

Trong không gian Oxyz, cho hai đường thẳng $\Delta_1, \Delta_2$ lần lượt đi qua các điểm $A_1(x_1; y_1; z_1)$, $A_2(x_2; y_2; z_2)$ và tương ứng có vecto chỉ phương $\vec{u_1} = (a_1; b_1; c_1), \vec{u_2} = (a_2; b_2; c_2)$. Khi đó:

• $\Delta_1 // \Delta_2 \Leftrightarrow \vec{u_1}$ cùng phương với $\vec{u_2}$ và $A_1 \notin \Delta_2$.

• $\Delta_1 \equiv \Delta_2 \Leftrightarrow \vec{u_1}$ cùng phương với $\vec{u_2}$ và $A_1 \in \Delta_2$.

• $\Delta_1$ và $\Delta_2$ cắt nhau $\Leftrightarrow \begin{bmatrix} [\vec{u_1}, \vec{u_2}] \neq 0 \\ \vec{A_1A_2} \cdot [\vec{u_1}, \vec{u_2}] = 0 \end{bmatrix}$

• $\Delta_1$ và $\Delta_2$ chéo nhau $\Leftrightarrow \vec{A_1A_2} \cdot [\vec{u_1}, \vec{u_2}] \neq 0$.

Ví dụ 8. Trong không gian Oxyz, chứng minh rằng hai đường thẳng sau vuông góc với nhau và chéo nhau:

$\Delta_1: \begin{cases} x = 1 + t \\ y = 2 - t \\ z = -1 + 2t \end{cases}$ và $\Delta_2: \frac{x-4}{3} = \frac{y+1}{1} = \frac{z}{-1}$.

Giải
Đường thẳng $\Delta_1$ đi qua điểm $A_1(1; 2; -1)$ và có vecto chỉ phương $\vec{u_1} = (1; -1; 2)$.

Đường thẳng $\Delta_2$ đi qua điểm $A_2(4; -1; 0)$ và có vecto chỉ phương $\vec{u_2} = (3; 1; -1)$.

Vì $\vec{u_1} \cdot \vec{u_2} = 1 \cdot 3 + (-1) \cdot 1 + 2 \cdot (-1) = 0$ nên $\vec{u_1}$ vuông góc với $\vec{u_2}$. Do đó $\Delta_1$ vuông góc với $\Delta_2$.

Ta có $\vec{A_1A_2} = (3; -3; 1)$ và $[\vec{u_1}, \vec{u_2}] = (-1; 7; 4)$.

Do $\vec{A_1A_2} \cdot [\vec{u_1}, \vec{u_2}] = 3 \cdot (-1) + (-3) \cdot 7 + 1 \cdot 4 = -20 \neq 0$ nên $\Delta_1$ và $\Delta_2$ chéo nhau.

Luyện tập 8. Trong không gian Oxyz, chứng minh rằng hai đường thẳng sau song song với nhau:

$\Delta_1: \frac{x-3}{1} = \frac{y}{-2} = \frac{z-1}{3}$ và $\Delta_2: \frac{x-1}{1} = \frac{y-2}{-2} = \frac{z}{3}$.