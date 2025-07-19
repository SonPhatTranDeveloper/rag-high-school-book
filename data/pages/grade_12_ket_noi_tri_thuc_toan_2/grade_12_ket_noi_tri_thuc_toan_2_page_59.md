2. MỘT SỐ ỨNG DỤNG CỦA PHƯƠNG TRÌNH MẶT CẦU TRONG THỰC TIỄN

Trong mô hình toán học, bề mặt Trái Đất là mặt cầu với bán kính 6371 km (theo: science.nasa.gov/earth/facts/). Mỗi kinh tuyến là một nửa đường tròn có đường kính là trục của Trái Đất (đoạn thẳng nối cực Bắc N và cực Nam S). Kinh tuyến gốc là kinh tuyến đi qua Đài Thiên văn Greenwich ở London. Mặt phẳng chứa kinh tuyến gốc chia Trái Đất làm hai nửa là bán cầu Đông và bán cầu Tây, nước ta nằm ở bán cầu Đông. Kinh độ của một điểm P trên bề mặt Trái Đất là số đo của góc nhi diện có hai mặt tương ứng chứa kinh tuyến gốc và kinh tuyến đi qua P (cạnh của góc nhi diện này là đường thẳng chứa trục Trái Đất). Kinh độ nhận giá trị trong đoạn từ 0° đến 180°. Vĩ độ của điểm P là số đo của góc giữa mặt phẳng chứa đường xích đạo và đường thẳng đi qua P và tâm O của Trái Đất. Vĩ độ nhận giá trị trong đoạn từ 0° đến 90°. Mỗi điểm trên bề mặt Trái Đất thuộc một trong hai bán cầu Bắc hoặc Nam và thuộc một trong hai bán cầu Đông hoặc Tây. Vì vậy, đi kèm với vĩ độ, còn có chữ E hoặc W nếu vị trí đó tương ứng thuộc bán cầu Đông hay bán cầu Tây và có chữ N, S nếu vị trí đó tương ứng ở bán cầu Bắc hay bán cầu Nam (Hình 5.42). Chẳng hạn, hồ Hoàn Kiếm (Hà Nội) ở vị trí: 21°01'51"N, 105°51'09"E (theo: maps.google.com). Vị trí trên mặt đất hoàn toàn xác định khi biết vĩ độ và kinh độ (bao gồm cả các kí hiệu N, S, E, W).

Trong bài học này, ta xét Trái Đất trong không gian Oxyz, với O là tâm Trái Đất, tia Ox chứa giao điểm của kinh tuyến gốc và xích đạo, tia Oz chứa điểm cực Bắc N, tia Oy giao xích đạo tại điểm thuộc bán cầu Đông, 1 đơn vị dài trong không gian Oxyz tương ứng với 6 371 km trên thực tế. Như vậy, trong không gian Oxyz, bề mặt Trái Đất có phương trình:

$x^2 + y^2 + z^2 = 1$.

Nếu biết vĩ độ và kinh độ của một vị trí trên mặt đất thì tọa độ của nó trong không gian cũng dễ dàng được xác định và ngược lại. Chẳng hạn, vị trí P có vĩ độ, kinh độ tương ứng là $\alpha°N, \beta°E$ $(0 < \alpha < 90, 0 < \beta < 180)$ có tọa độ $P(\cos \alpha° \cos \beta°; \cos \alpha° \sin \beta°; \sin \alpha°)$ (H.5.43), vị trí Q có vĩ độ, kinh độ tương ứng là $\alpha°N, \beta°W$ $(0 < \alpha < 90, 0 < \beta < 180)$ thì có tọa độ $Q(\cos \alpha° \cos \beta°; -\cos \alpha° \sin \beta°; \sin \alpha°)$ (H.5.44).

[Hình 5.42: Một hình vẽ minh họa hệ tọa độ trên quả địa cầu, với các trục x, y, z và các đường kinh tuyến, vĩ tuyến được biểu diễn. Điểm P được đánh dấu trên bề mặt cầu.]

[Hình 5.43: Một hình vẽ minh họa tọa độ của điểm P trong không gian ba chiều, với các trục x, y, z và các thành phần tọa độ được biểu diễn.]

[Hình 5.44: Một hình vẽ minh họa tương tự như Hình 5.43, nhưng cho điểm Q.]