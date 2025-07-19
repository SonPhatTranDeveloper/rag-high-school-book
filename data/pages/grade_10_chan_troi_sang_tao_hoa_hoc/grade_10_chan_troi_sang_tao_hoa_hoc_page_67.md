*********************************************************************************
** Cite this program as: MOPAC2016, Version: 21.361 , James J. P. Stewart,    **
**                       web-site: HTTP://OpenMOPAC.net.                      **
*********************************************************************************
**                                                                            **
**                                MOPAC2016                                   **
**                                                                            **
*********************************************************************************

PM7 CALCULATION RESULTS

Ở cuối của của sổ output có thông tin như sau:

***********************
*                     *
* JOB ENDED NORMALLY  *
*                     *
***********************
TOTAL JOB TIME:         0.07 SECONDS

== MOPAC DONE ==

Kết quả cho biết phép tính đã được thực hiện tốt và cung cấp một số dữ liệu thống kê về phép tính.

Bước 6: Diễn giải dữ liệu xuất
Phân kết quả:

FINAL HEAT OF FORMATION = -57.79955 KCAL/MOL
                        = -241.83333 KJ/MOL
ETOT (EONE + ETWO)      = -322.6792 EV

Kết quả cho biết nhiệt tạo thành (FINAL HEAT OF FORMATION) của phân tử H₂O (ở điều kiện chuẩn theo tính toán) là -241,83 kJ/mol.

Tổng năng lượng của phân tử H₂O (ETOT (EONE + ETWO)) là -322,6792 eV.

Độ dài liên kết (BOND LENGTH) và góc liên kết (BOND ENGLE) của phân tử nước trong file H2O.out được thể hiện như hình dưới.

ATOM    CHEMICAL    BOND LENGTH    BOND ANGLE    TWIST ANGLE
NUMBER    SYMBOL    (ANGSTROMS)     (DEGREES)     (DEGREES)
(I)                    NA:I         NB:NA:I      NC:NB:NA:I
1           O        0.00000000     0.0000000     0.0000000
2           H        0.95575602  *  0.0000000     0.0000000
3           H        0.95572694  * 105.3943918  * 0.0000000

Phần mềm MOPAC cho phép tính được tham số cấu trúc (độ dài liên kết, góc liên kết, ...), năng lượng phân tử, nhiệt tạo thành, ...

3. Từ kết quả nhiệt tạo thành của phân tử H₂O. So sánh với giá trị thực nghiệm, đưa ra kết luận (Giá trị thực nghiệm của phân tử H₂O(g) là -241,8 kJ/mol).

4. Từ kết quả độ dài liên kết O-H và góc liên kết H-O-H trong phân tử H₂O, so sánh với giá trị thực nghiệm, đưa ra nhận xét (Độ dài liên kết O-H là 0,97 Å, góc liên kết H-O-H là 104,5°).

5. Thực hành tạo file dữ liệu
a) (C₂H₆.mop)
b) (C₃H₈.mop)
Tối ưu hoá cấu trúc của phân tử và tính nhiệt tạo thành của phân tử C₂H₆, C₃H₈ bằng phương pháp PM7.