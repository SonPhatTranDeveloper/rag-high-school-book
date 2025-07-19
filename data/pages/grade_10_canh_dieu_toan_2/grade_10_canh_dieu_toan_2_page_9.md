# 1. Vận dụng trong giải toán

Ví dụ 5 Cho 10 điểm phân biệt. Hỏi lập được bao nhiêu vectơ khác 0? Biết rằng hai đầu mút của mỗi vectơ là hai trong 10 điểm đã cho.

Giải
Việc lập vectơ là thực hiện hai hành động liên tiếp: chọn điểm đầu và chọn điểm cuối.
Chọn điểm đầu: có 10 cách chọn. Chọn điểm cuối: có 9 cách chọn.
Vậy có 10 . 9 = 90 (vectơ).

Ví dụ 6 Phân tích số 10 125 ra thừa số nguyên tố rồi tìm số ước nguyên dương của nó.

Giải
Ta có: 10 125 = $3^4 . 5^3$. Một ước nguyên dương của 10 125 thì có dạng $3^m . 5^n$, trong đó m, n là hai số tự nhiên sao cho 0 ≤ m < 4, 0 ≤ n < 3.
Như vậy, để tạo ra một ước nguyên dương của 10 125 ta làm như sau:
- Chọn số tự nhiên m mà 0 ≤ m ≤ 4 có 5 cách chọn.
- Chọn số tự nhiên n mà 0 ≤ n ≤ 3 có 4 cách chọn.
Lấy tích $3^m . 5^n$.
Vì vậy, số ước nguyên dương của 10 125 là: 5 . 4 = 20 (số).

# 2. Vận dụng trong thực tiễn

Ví dụ 7 Từ ba mảng dữ liệu A, B, C, máy tính tạo nên một thông tin đưa ra màn hình cho người dùng bằng cách lần lượt lấy một dữ liệu từ A, một dữ liệu từ B và một dữ liệu từ C. Giả sử A, B, C lần lượt chứa m, n, p dữ liệu. Hỏi máy tính có thể tạo ra được bao nhiêu thông tin?

Giải
Việc máy tính tạo ra thông tin là thực hiện ba cách chọn liên tiếp: chọn dữ liệu từ A, chọn dữ liệu từ B và chọn dữ liệu từ C.
Có m cách chọn một dữ liệu từ A.
Có n cách chọn một dữ liệu từ B.
Có p cách chọn một dữ liệu từ C.
Vậy số thông tin máy tính có thể tạo được là: m . n . p.

Ví dụ 8 Gia đình bạn Quân đặt mật mã của chiếc khóa cổng là một dãy gồm bốn chữ số. Hỏi có bao nhiêu cách đặt mật mã nếu:
a) Các chữ số có thể giống nhau?
b) Các chữ số phải đôi một khác nhau?

[Hình ảnh một ổ khóa số màu đen với 4 bánh xe số từ 0 đến 9]

Từ các chữ số 1, 2, 3, 4, 5, lập được bao nhiêu số lẻ gồm ba chữ số đôi một khác nhau?