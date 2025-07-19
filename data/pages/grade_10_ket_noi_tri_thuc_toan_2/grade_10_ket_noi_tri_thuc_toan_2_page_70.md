Giải
Mỗi cách chọn 4 bạn trong 7 bạn học sinh là một tổ hợp chập 4 của 7.

Vậy số cách chọn 4 bạn chơi cờ cá ngựa là $C_4^7 = \frac{7!}{4!3!} = 35$.

Luyện tập 3. Trong ngân hàng đề kiểm tra cuối học kì II môn Vật lí có 20 câu lí thuyết và 40 câu bài tập. Người ta chọn ra 2 câu lí thuyết và 3 câu bài tập trong ngân hàng đề để tạo thành một đề thi. Hỏi có bao nhiêu cách lập đề thi gồm 5 câu hỏi theo cách chọn như trên?

4. ỨNG DỤNG HOÁN VỊ, CHỈNH HỢP, TỔ HỢP VÀO CÁC BÀI TOÁN ĐẾM

Các khái niệm hoán vị, chỉnh hợp và tổ hợp liên quan mật thiết với nhau và là những khái niệm cốt lõi của các phép đếm. Rất nhiều bài toán đếm liên quan đến việc lựa chọn, việc sắp xếp, vì vậy các công thức tính $P_n$, $A_n^k$, $C_n^k$ sẽ được dùng rất nhiều.

Dưới đây ta xét một số ví dụ về các bài toán đếm.

Ví dụ 4. Một lần anh Hưng đến Hà Nội và dự định từ Hà Nội tham quan Đền Hùng, Ninh Bình, Hạ Long, Đường Lâm và Bát Tràng, mỗi ngày đi tham quan một địa điểm rồi lại về Hà Nội.

a) Hỏi anh Hưng có thể xếp được bao nhiêu lịch trình đi tham quan tất cả các địa điểm (ở đây lịch trình tính cả thứ tự tham quan).

b) Anh Hưng có việc đột xuất phải về sớm, nên anh chỉ có 3 ngày để đi tham quan 3 địa điểm. Hỏi anh Hưng có bao nhiêu cách xếp lịch trình đi tham quan?

Giải

a) Anh Hưng đi tham quan 5 địa điểm, mỗi cách xếp lịch trình là một cách chọn có thứ tự của 5 địa điểm trên. Vậy số cách xếp lịch trình chính bằng số các hoán vị của 5 địa điểm, và bằng

$P_5 = 5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$ (cách).

b) Nếu anh Hưng chỉ có 3 ngày để đi tham quan 3 nơi, thì mỗi cách xếp lịch trình của anh chính là một cách chọn có thứ tự 3 địa điểm từ 5 địa điểm, tức là một chỉnh hợp chập 3 của 5.

Vậy số cách xếp lịch trình đi tham quan trong trường hợp này là

$A_5^3 = \frac{5!}{(5-3)!} = \frac{5!}{2!} = 60$ (cách).

Ví dụ 5. Giải bài toán trong tình huống mở đầu về đội hình của Đội tuyển bóng đá quốc gia.

Giải

Vì mỗi đội hình gồm có 1 thủ môn, 3 hậu vệ, 4 tiền vệ và 3 tiền đạo và đã biết trước vị trí thủ môn, nên để chọn đội hình ta cần thực hiện 3 công đoạn:

1. Chọn hậu vệ là chọn 3 trong số 7 hậu vệ: có $C_7^3 = 35$ (cách).

2. Chọn tiền vệ là chọn 4 trong số 8 tiền vệ: có $C_8^4 = 70$ (cách).

3. Chọn tiền đạo là chọn 3 trong số 5 tiền đạo: có $C_5^3 = 10$ (cách).

Vậy, theo quy tắc nhân, số các đội hình có thể có (khi đã biết vị trí thủ môn) là 35 · 70 · 10 = 24 500.