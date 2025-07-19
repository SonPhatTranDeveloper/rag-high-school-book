Một nhóm bạn gồm sáu thành viên cùng đi xem phim, đã mua sáu vé có ghế ngồi cùng dãy và kế tiếp nhau (như Hình 3). Có bao nhiêu cách sắp xếp chỗ ngồi cho các thành viên của nhóm?

Một giải bóng đá có 14 đội bóng tham gia. Có bao nhiêu khả năng về thứ hạng các đội bóng khi mùa giải kết thúc?

[Hình 3: Ảnh minh họa cho thấy nhiều hàng ghế màu đỏ trong một rạp chiếu phim]

2. Chỉnh hợp

Tại một trạm quan sát, có sẵn 5 lá cờ màu đỏ, trắng, xanh, vàng và cam (kí hiệu D, T, X, V, C). Khi cần báo một tín hiệu, người ta chọn 3 lá cờ và cắm vào ba vị trí cố sẵn thành một hàng (xem Hình 4).

a) Hãy chỉ ra ít nhất bốn cách chọn và cắm cờ để báo bốn tín hiệu khác nhau.

b) Bằng cách này, có thể báo nhiều nhất bao nhiêu tín hiệu khác nhau?

[Hình 4: Minh họa một trạm quan sát với mái nhà màu đỏ và ba cột cờ màu đỏ, vàng, xanh trên đỉnh]

Trong (2), mỗi cách chọn ra 3 lá cờ từ 5 lá cờ và sắp xếp chúng theo thứ tự được gọi là một chỉnh hợp chập 3 của 5 lá cờ. Ta thấy số các chỉnh hợp này bằng 5 . 4 . 3.

Tổng quát, ta có định nghĩa sau:

Cho tập hợp A có n phần tử (n ≥ 1) và số nguyên k với 1 ≤ k ≤ n.
Mỗi cách lấy k phần tử của A và sắp xếp chúng theo một thứ tự gọi là một chỉnh hợp chập k của n phần tử đó.

Kí hiệu $A_n^k$ là số chỉnh hợp chập k của n phần tử.

Người ta chứng minh được rằng:

Số các chỉnh hợp chập k của n phần tử (1 ≤ k ≤ n) bằng

$A_n^k = n(n-1)(n-2)...(n-k+1) = \frac{n!}{(n-k)!}$

Nhận xét: Mỗi hoán vị của n phần tử cũng chính là chỉnh hợp chập n của n phần tử đó.
Ta có $P_n = A_n^n, n ≥ 1$.