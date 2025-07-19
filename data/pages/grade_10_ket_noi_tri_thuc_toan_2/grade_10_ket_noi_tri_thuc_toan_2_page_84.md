Bài 27: THỰC HÀNH TÍNH XÁC SUẤT THEO ĐỊNH NGHĨA CỔ ĐIỂN

THUẬT NGỮ:
Xác suất của biến cố đối.

KIẾN THỨC, KĨ NĂNG:
• Tính xác suất trong một số bài toán đơn giản bằng phương pháp tổ hợp.
• Tính xác suất trong một số bài toán đơn giản bằng cách sử dụng sơ đồ hình cây.
• Nắm và vận dụng quy tắc tính xác suất của biến cố đối.

Trở lại tình huống mở đầu trong Bài 26. Hãy tính xác suất trúng giải độc đắc, trúng giải nhất của bạn An khi chọn bộ số {5; 13; 20; 31; 32; 35}.

1. SỬ DỤNG PHƯƠNG PHÁP TỔ HỢP

Hỏi. Theo định nghĩa cổ điển của xác suất, để tính xác suất của biến cố F: "Bạn An trúng giải độc đắc" và biến cố G: "Bạn An trúng giải nhất" ta cần xác định n(Ω), n(F) và n(G). Liệu có thể tính n(Ω), n(F) và n(G) bằng cách liệt kê ra hết các phần tử của Ω, F và G rồi kiểm đếm được không?

Trong nhiều bài toán, để tính số phần tử của không gian mẫu, của các biến cố, ta thường sử dụng các quy tắc đếm, các công thức tính số hoán vị, chỉnh hợp và tổ hợp.

[Hình ảnh một robot đang chỉ vào một dòng chữ: "Đôi khi người ta gọi Bài số tổ hợp là "sự kiểm đếm không cần phải liệt kê".]

Ví dụ 1. Một tổ trong lớp 10A có 10 học sinh trong đó có 6 học sinh nam và 4 học sinh nữ. Giáo viên chọn ngẫu nhiên 6 học sinh trong tổ đó để tham gia đội tình nguyện Mùa hè xanh. Tính xác suất của hai biến cố sau:

C: "6 học sinh được chọn đều là nam";
D: "Trong 6 học sinh được chọn có 4 nam và 2 nữ".

Giải
Không gian mẫu là tập tất cả các tập con gồm 6 học sinh trong 10 học sinh. Vậy

$n(\Omega) = C^6_{10} = 210$.

a) Tập C chỉ có một phần tử là tập 6 học sinh nam. Vậy n(C) = 1, do đó P(C) = $\frac{1}{210}$.

b) Mỗi phần tử của D được hình thành từ hai công đoạn.
Công đoạn 1. Chọn 4 học sinh nam từ 6 học sinh nam, có $C^4_6 = 15$ (cách chọn).
Công đoạn 2. Chọn 2 học sinh nữ từ 4 học sinh nữ, có $C^2_4 = 6$ (cách chọn).

Theo quy tắc nhân, tập D có 15 · 6 = 90 (phần tử). Vậy n(D) = 90. Từ đó P(D) = $\frac{90}{210} = \frac{3}{7}$.