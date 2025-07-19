Ứng dụng Google Maps cho phép xác định khoảng cách giữa hai vị trí trên bề mặt Trái Đất khi biết vĩ độ và kinh độ của chúng. Khoảng cách giữa hai vị trí P và Q trên bề mặt Trái Đất là độ dài cung nhỏ PQ của đường tròn có tâm O và đi qua hai điểm P, Q. Cung tròn nói trên là đường đi ngắn nhất trên bề mặt Trái Đất từ P đến Q. Trong ví dụ sau đây, ta sẽ tính khoảng cách giữa hai vị trí đã được nêu ra trong mở đầu bài học.

Quy ước: Trong phần này, kết quả phép tính được làm tròn đến chữ số thập phân thứ tư sau dấu phẩy.

[Hình minh họa: Một robot hoạt hình đang vẫy tay]

Ví dụ 5. Biết rằng nếu vị trí M có vĩ độ và kinh độ tương ứng là $\alpha°N, \beta°E$ $(0 < \alpha < 90, 0 < \beta < 90)$ thì có tọa độ $M(\cos\alpha° \cos\beta°; \cos\alpha° \sin\beta°; \sin\alpha°)$. Tính khoảng cách trên mặt đất từ vị trí P: 10°N, 15°E đến vị trí Q: 80°N, 70°E.

Giải

Ta có

$P(\cos10° \cos15°; \cos10° \sin15°; \sin10°), Q(\cos80° \cos70°; \cos80° \sin70°; \sin80°)$.

Suy ra

$\overrightarrow{OP} = (\cos10° \cos15°; \cos10° \sin15°; \sin10°), \overrightarrow{OQ} = (\cos80° \cos70°; \cos80° \sin70°; \sin80°)$.

Do đó

$\overrightarrow{OP} \cdot \overrightarrow{OQ} = \cos10° \cos15° \cos80° \cos70° + \cos10° \sin15° \cos80° \sin70° + \sin10° \sin80°$
$\approx 0,2691$.

Vì P, Q thuộc mặt đất nên $|\overrightarrow{OP}| = |\overrightarrow{OQ}| = 1$.

Do đó $\cos\widehat{POQ} = \frac{\overrightarrow{OP} \cdot \overrightarrow{OQ}}{|\overrightarrow{OP}| \cdot |\overrightarrow{OQ}|} \approx 0,2691$. Suy ra $\widehat{POQ} \approx 74,3893°$.

Mặt khác, đường tròn tâm O, đi qua P, Q có bán kính 1 và chu vi là $2\pi \approx 6,2832$, nên cung nhỏ $\widehat{PQ}$ của đường tròn đó có độ dài xấp xỉ bằng $\frac{74,3893}{360} \cdot 6,2832 \approx 1,2983$.

Do 1 đơn vị dài trong không gian Oxyz tương ứng với 6 371 km trên thực tế, nên khoảng cách trên mặt đất giữa hai vị trí P, Q xấp xỉ bằng $1,2983 \cdot 6371 = 8271,4693$ (km).

Luyện tập 5. Tính khoảng cách trên mặt đất từ vị trí A là giao giữa kinh tuyến gốc với xích đạo đến vị trí B: 45°N, 30°E.

Trải nghiệm. Trên Google Maps, thực hiện phép đo khoảng cách từ vị trí 0°N, 0°E đến vị trí 45°N, 30°E và so sánh với kết quả tính được ở Luyện tập 5.