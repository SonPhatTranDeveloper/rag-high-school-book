Trong hoạt động trải nghiệm này, em hãy theo hướng dẫn sau, để vẽ tam giác Penrose bằng cách dựng các hình hộp chữ nhật và lựa chọn một góc nhìn thích hợp.

Chú ý: Sử dụng giao diện GeoGebra bằng Tiếng Việt: Vào mục Thiết lập, chọn Ngôn ngữ, chọn Tiếng Việt. Các hướng dẫn được đưa ra trong bài học này ứng với phiên bản GeoGebra Classic.

- Bước 1. Mở phần mềm GeoGebra, vào mục Hiển thị và lần lượt lựa chọn các mục sau:
Hiển thị danh sách đối tượng, Vùng làm việc, Hiển thị dạng 3D, Khung nhập lệnh.

[Hình ảnh mô tả giao diện GeoGebra với các tùy chọn hiển thị]

- Bước 2. Trong Khung nhập lệnh, lần lượt sử dụng các đoạn lệnh sau:

Đoạn lệnh | Ý nghĩa
--- | ---
DaGiac((0, 0, 0), (-1, 0, 0), 4, TrucTung) | Hình vuông có tọa độ 2 đỉnh là (0, 0, 0), (-1, 0, 0) và nằm trong mặt phẳng (Oxz).
DaGiac((0, 9, 0), (0, 10, 0), 4, TrucZ) | Hình vuông có tọa độ 2 đỉnh là (0, 9, 0), (0, 10, 0) và nằm trong mặt phẳng (Oxy).
DaGiac((-1, 0, 0), (-1, 1, 0), 4, TrucHoanh) | Hình vuông có tọa độ 2 đỉnh là (-1, 0, 0), (-1, 1, 0) và nằm trong mặt phẳng (Oyz).
HinhLangTru(TenDaGiac1, 9) | Hình lăng trụ có đáy là TenDagiac1 và chiều cao bằng 9 nằm ở phần dương của trục Oy.
HinhLangTru(TenDaGiac2, 9) | Hình lăng trụ có đáy là TenDagiac2 và chiều cao bằng 9 nằm ở phần dương của trục Oz.
HinhLangTru(TenDaGiac3, -9) | Hình lăng trụ có đáy là TenDagiac3 và chiều cao bằng 9 nằm ở phần âm của trục Ox.
DaGiac((0, 9, 0), (0, 10, 0), (0, 10, 9), (0, 9, 8)) | Đa giác có tọa độ 4 đỉnh là (0, 9, 0), (0, 10, 0), (0, 10, 9), (0, 9, 8).