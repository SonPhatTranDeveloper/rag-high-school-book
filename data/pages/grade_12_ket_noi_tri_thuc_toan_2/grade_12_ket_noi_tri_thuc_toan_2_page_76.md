Trên nhánh cây OA và OĀ tương ứng ghi P(A) và P(Ā);
Trên nhánh cây AB và AB̄ tương ứng ghi P(B | A) và P(B̄ | A);
Trên nhánh cây ĀB và ĀB̄ tương ứng ghi P(B | Ā) và P(B̄ | Ā).

Có hai nhánh cây đi tới B là OAB và OĀB. Vậy:

$P(B) = 0,4 \cdot 0,3 + 0,6 \cdot 0,4 = 0,36.$

Luyện tập 2. Trở lại Ví dụ 1. Sử dụng sơ đồ hình cây, hãy mô tả cách tính xác suất để thứ Tư, ông An đi làm bằng xe buýt.

Vận dụng. Hình dạng hạt của đậu Hà Lan có hai kiểu hình: hạt tròn và hạt nhăn, có hai gene ứng với hai kiểu hình này là gene trội B và gene lặn b.

Khi cho lai hai cây đậu Hà Lan, cây con lấy ngẫu nhiên một cách độc lập một gene từ cây bố và một gene từ cây mẹ để hình thành một cặp gene. Giả sử cây bố và cây mẹ được chọn ngẫu nhiên từ một quần thể các cây đậu Hà Lan, ở đó tỉ lệ cây mang kiểu gene bb, Bb tương ứng là 40% và 60%. Tính xác suất để cây con có kiểu gene bb.

Hướng dẫn:

Gọi A là biến cố: "Cây bố có kiểu gene bb";
M là biến cố: "Cây con lấy gene b từ cây bố";
N là biến cố: "Cây con lấy gene b từ cây mẹ";
E là biến cố: "Cây con có kiểu gene bb".

Theo giả thiết, M và N độc lập nên $P(E) = P(M) \cdot P(N)$.

Tính P(M): Ta áp dụng công thức xác suất toàn phần:

$P(M) = P(A) \cdot P(M | A) + P(Ā) \cdot P(M | Ā)$. (*)

Ta có $P(A) = 0,4; P(Ā) = 0,6$.

P(M | A) là xác suất để cây con lấy gene b từ cây bố với điều kiện cây bố có kiểu gene bb. Do đó P(M | A) = 1.

P(M | Ā) là xác suất để cây con lấy gene b từ cây bố với điều kiện cây bố có kiểu gene Bb. Do đó $P(M | Ā) = \frac{1}{2}$.

Thay vào (*) ta được: $P(M) = 0,4 + 0,3 = 0,7$.

Tương tự tính được P(N) = 0,7.

Vậy $P(E) = P(M) \cdot P(N) = 0,7 \cdot 0,7 = 0,49$.

Từ kết quả trên suy ra trong một quần thể các cây đậu Hà Lan, mà ở đó tỉ lệ cây bố và cây mẹ mang kiểu gene bb, Bb tương ứng là 40% và 60%, thì tỉ lệ cây con có kiểu gene bb là khoảng 49%.

Luyện tập 3. Với giả thiết như vận dụng trên.

a) Hãy ước lượng tỉ lệ cây con có kiểu gene BB.

b) Sử dụng kết quả của vận dụng trên và câu a, hãy ước lượng tỉ lệ cây con có kiểu gene Bb.