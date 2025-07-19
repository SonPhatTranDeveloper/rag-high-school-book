Bài 7: CẤP SỐ NHÂN

THUẬT NGỮ:
• Cấp số nhân
• Công bội
• Số hạng tổng quát
• Tổng của n số hạng đầu

KIẾN THỨC, KĨ NĂNG:
• Nhận biết một dãy số là cấp số nhân.
• Giải thích công thức xác định số hạng tổng quát của cấp số nhân.
• Tính tổng của n số hạng đầu của cấp số nhân.
• Giải quyết một số vấn đề thực tiễn gắn với cấp số nhân để giải một số bài toán liên quan đến thực tiễn.

Một công ty tuyển một chuyên gia về công nghệ thông tin với mức lương năm đầu là 240 triệu đồng và cam kết sẽ tăng thêm 5% lương mỗi năm so với năm liền trước đó. Tính tổng số lương mà chuyên gia đó nhận được sau khi làm việc cho công ty 10 năm (làm tròn đến triệu đồng).

1. ĐỊNH NGHĨA

HD1. Nhận biết cấp số nhân

Cho dãy số $(u_n)$ với $u_n = 3 \cdot 2^n$.
a) Viết năm số hạng đầu của dãy số này.
b) Dự đoán hệ thức truy hồi liên hệ giữa $u_n$ và $u_{n-1}$.

[Hình ảnh minh họa một robot đang chỉ vào biểu thức $\frac{u_n}{u_{n-1}}$ với chú thích "Hãy xét tỉ số"]

• Cấp số nhân là một dãy số (hữu hạn hay vô hạn), trong đó kể từ số hạng thứ hai, mỗi số hạng đều là tích của số hạng đứng ngay trước nó với một số không đổi q. Số q được gọi là công bội của cấp số nhân.

• Cấp số nhân $(u_n)$ với công bội q được cho bởi hệ thức truy hồi
$u_n = u_{n-1} \cdot q$ với $n \geq 2$.

Dãy số không đổi a, a, a, ... có phải là một cấp số nhân không?

Ví dụ 1. Cho cấp số nhân có số hạng đầu $u_1 = 5$ và công bội $q = -2$. Viết năm số hạng đầu của cấp số nhân này.

Giải

Năm số hạng đầu của cấp số nhân này là:

$u_1 = 5, u_2 = u_1 \cdot q = 5 \cdot (-2) = -10, u_3 = u_2 \cdot q = (-10) \cdot (-2) = 20,$

$u_4 = u_3 \cdot q = 20 \cdot (-2) = -40, u_5 = u_4 \cdot q = (-40) \cdot (-2) = 80.$

Ví dụ 2. Cho dãy số $(u_n)$ với $u_n = \frac{1}{3^{n-1}}$. Chứng minh rằng dãy số này là một cấp số nhân. Xác định số hạng đầu và công bội của nó.