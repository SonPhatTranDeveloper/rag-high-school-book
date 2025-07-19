• Chọn hai vị trí A, B lần lượt trên hai sườn đồi. Bằng cách đo đạc tại thực địa, ta xác định được tọa độ của hai điểm A, B và góc dốc α (đơn vị: độ) tại điểm B của sườn đồi. Giả sử ta có A(- 1 000 ; 60), B(1 000 ; 90) và tanα = 0,04 (Hình 27) (Nguồn: R. Larson and B. Edwards, Calculus 10e, Cengage 2014).

• Trong hệ trục tọa độ Oxy, quan sát đường cong (vẽ bằng nét đứt) mô phỏng đoạn đường cao tốc nối hai sườn đồi, đường cong đó gợi nên hình ảnh đồ thị của hàm số bậc ba. Vì thế ta có thể chọn hàm số bậc ba $y = f(x) = ax^3 + bx^2 + cx + d (a ≠ 0)$ sao cho trong hệ trục tọa độ Oxy, đồ thị của hàm số đó trên đoạn [- 1 000 ; 1 000] mô phỏng đoạn đường cao tốc cần thiết kế. Ta chọn theo nguyên tắc: Hệ số góc của tiếp tuyến tại B của đồ thị hàm số đó bằng 0,04.

[Hình 27: Hình ảnh minh họa một đoạn đường cao tốc nối hai sườn đồi. Trục tọa độ Oxy được vẽ, với điểm A(-1000; 60) và B(1000; 90) được đánh dấu trên đường cong nét đứt. Góc α được thể hiện tại điểm B. Có ghi chú "Không vẽ theo đúng tỉ lệ xích" và "50 ft" được đánh dấu trên trục y.]

Hãy xác định hàm số bậc ba đó.

Giải

Do đồ thị hàm số bậc ba $y = f (x) = ax^3 + bx^2 + cx + d (a ≠ 0)$ đi qua điểm (0 ; 50) nên $d = 50$, suy ra $y = f (x) = ax^3 + bx^2 + cx + 50$. Do đồ thị đi qua các điểm A(- 1 000 ; 60), B(1 000 ; 90) nên ta có:

$\begin{cases} 
-1 000 000 000a + 1 000 000b - 1000c = 10 \\
1 000 000 000a + 1 000 000b + 1000c = 40,
\end{cases}$

hay $\begin{cases}
-100 000 000a + 100 000b - 100c = 1 \\
100 000 000a + 100 000b + 100c = 4
\end{cases}$, suy ra $\begin{cases}
b = \frac{1}{40 000} \\
100 000 000a + 100c = 1,5.
\end{cases}$

Ta có: $f'(x) = 3ax^2 + 2bx + c = 3ax^2 + \frac{1}{20000}x + c$.

Do hệ số góc của tiếp tuyến tại B của đồ thị hàm số đó bằng 0,04 nên

$f'(1 000) = 3 000 000a + \frac{1}{20} + c = 0,04$, tức là $3 000 000a + c = -0,01$.