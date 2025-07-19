Ví dụ 3: Hãy liệt kê tất cả các số gồm hai chữ số khác nhau được lấy từ các chữ số 1, 2, 3, 4, 5.

Giải
Các số gồm hai chữ số khác nhau được lấy từ các chữ số 1, 2, 3, 4, 5 là:
12, 13, 14, 15, 21, 23, 24, 25, 31, 32, 34, 35, 41, 42, 43, 45, 51, 52, 53, 54.

2. Số các chỉnh hợp

Một lớp được chia thành 5 nhóm A, B, C, D, E để tham gia hoạt động thực hành trải nghiệm. Sau khi các nhóm thực hiện xong hoạt động, giáo viên chọn 3 nhóm trong 5 nhóm và sắp xếp thứ tự trình bày kết quả hoạt động của 3 nhóm đã được chọn ra.

a) Có bao nhiêu cách chọn nhóm trình bày thứ nhất?

b) Sau khi đã chọn nhóm trình bày thứ nhất, có bao nhiêu cách chọn nhóm trình bày thứ hai?

c) Sau khi đã chọn nhóm trình bày thứ nhất và thứ hai, có bao nhiêu cách chọn nhóm trình bày thứ ba?

d) Với cách làm như trên, giáo viên tạo ra một chỉnh hợp chập 3 của 5 phần tử. Tính số các chỉnh hợp được tạo ra.

Theo quy tắc nhân, số các chỉnh hợp chập 3 của 5 phần tử là:
5 . 4 . 3 = 60.

Trong trường hợp tổng quát, đối với tập hợp A có n phần tử (n > 1), ta làm tương tự như trên để tạo ra một chỉnh hợp chập k của n phần tử đó (1 ≤ k ≤ n) và số các chỉnh hợp chập k của n phần tử trong tập hợp A là:

n(n - 1)...(n - k + 1).

Kí hiệu $A_n^k$ là số các chỉnh hợp chập k của n phần tử (1 < k < n).

Ta có: $A_n^k = n(n - 1)...(n - k + 1)$.

Ví dụ 4: Ở các căn hộ chung cư, người ta thường dùng các chữ số để tạo mật mã mở cửa. Gia đình bạn Linh đặt mật mã nhà là một dãy số gồm 6 chữ số đôi một khác nhau. Hỏi gia đình bạn Linh có bao nhiêu cách để tạo mật mã?

Giải
Mỗi mật mã của gia đình bạn Linh là một chỉnh hợp chập 6 của 10 chữ số.
Vậy có $A_{10}^6 = 10 . 9 . 8 . 7 . 6 . 5 = 151 200$ (cách để tạo mật mã).