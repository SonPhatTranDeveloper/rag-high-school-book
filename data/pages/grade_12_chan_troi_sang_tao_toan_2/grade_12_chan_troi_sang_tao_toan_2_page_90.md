- Danh sách cú pháp lệnh biểu diễn các đối tượng hình học tọa độ trong không gian trên GeoGebra.

Đối tượng | Cú pháp lệnh | Giải thích
--- | --- | ---
Điểm | $M(x; y; z)$ | M(x,y,z) hay M=(x,y,z)
Vector | $\vec{u} = (x; y; z)$ | u(x,y,z) hay u=(x,y,z) | Kí hiệu vector không có mũi tên.
 | $\vec{u} = \overrightarrow{MN}$ | u=Vecto(M, N) | Nhập hai điểm $M$ và $N$ trước khi nhập $\vec{u}$.
Đường thẳng | Đường thẳng đi qua điểm $M(x_0; y_0; z_0)$ có vector chỉ phương $\vec{u} = (a_1; a_2; a_3)$ | DuongThang(M, u) | Nhập điểm và vector chỉ phương trước khi vẽ đường thẳng.
 | $Ax + By + Cz + D = 0$ | Ax+By+Cz+D=0
Mặt phẳng | Mặt phẳng đi qua điểm $M(x_0; y_0; z_0)$ và vuông góc với đường thẳng $d$. | MatPhangVuongGoc(M, d) | Nhập điểm và đường thẳng trước khi vẽ mặt phẳng.
 | Mặt phẳng đi qua điểm $M(x_0; y_0; z_0)$ và có cặp vector chỉ phương $\vec{u}, \vec{v}$. | MatPhang(M, u, v) | Nhập điểm và cặp vector chỉ phương trước khi vẽ mặt phẳng.
 | Mặt phẳng đi qua 3 điểm $A, B, C$. | MatPhang(A, B, C) | Nhập 3 điểm $A, B, C$ trước khi vẽ mặt phẳng.
 | Mặt cầu có phương trình: $(x - a)^2 + (y - b)^2 + (x - c)^2 = R^2$. | (x−a)^2+(x−b)^2+ (x−c)^2=R^2
Mặt cầu | Mặt cầu $(S)$ tâm $I$ bán kính $R$. | MatCau(I, R) | Nhập tâm mặt cầu và bán kính trước khi vẽ mặt cầu.
 | Mặt cầu $(S)$ tâm $I$ đi qua điểm $M$. | MatCau(I, M) | Nhập tâm mặt cầu và điểm nằm trên mặt cầu trước khi vẽ mặt cầu.