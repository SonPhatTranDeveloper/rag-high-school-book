[Hình ảnh minh họa về cách chọn tổ hợp từ một tập hợp 5 phần tử]

Mỗi tổ hợp chập 3 của 5 phần tử sinh ra 3! chỉnh hợp chập 3 của 5 phần tử và có 3! hoán vị của 3 phần tử. Vì thế, số chỉnh hợp chập 3 của 5 phần tử nhiều gấp 3! lần số tổ hợp chập 3 của 5 phần tử.

Nhận xét: Số chỉnh hợp chập k của n phần tử nhiều gấp k! lần số tổ hợp chập k của n phần tử đó.

Kí hiệu $C_n^k$ là số tổ hợp chập k của n phần tử với $1 \leq k \leq n$. Ta có: $C_n^k = \frac{A_n^k}{k!}$.

Ví dụ 2: Chứng minh $C_n^k = \frac{n!}{k!(n-k)!}$ với $1 \leq k \leq n$.

Giải

Ta có: $A_n^k = n(n-1)...(n-k+1) = \frac{n(n-1)...(n-k+1)(n-k)...2.1}{(n-k)...2.1} = \frac{n!}{(n-k)!}$.

Do đó $C_n^k = \frac{A_n^k}{k!} = \frac{n!}{k!(n-k)!}$.

Quy ước: $0! = 1; C_n^0 = 1$.

Với những quy ước trên, ta có công thức sau:

$C_n^k = \frac{n!}{k!(n-k)!}$ với $0 \leq k \leq n$.

Ví dụ 3: Lớp 10A có 18 bạn nữ và 20 bạn nam.
a) Có bao nhiêu cách chọn 3 bạn nữ trong 18 bạn nữ?
b) Có bao nhiêu cách chọn 5 bạn nam trong 20 bạn nam?