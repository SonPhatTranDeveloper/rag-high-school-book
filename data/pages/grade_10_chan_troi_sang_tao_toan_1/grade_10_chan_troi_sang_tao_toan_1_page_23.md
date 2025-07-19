a) Xác định tập hợp A gồm các ứng viên đạt yêu cầu về chuyên môn, tập hợp B gồm các ứng viên đạt yêu cầu về ngoại ngữ.

b) Xác định tập hợp C gồm các ứng viên đạt yêu cầu cả về chuyên môn và ngoại ngữ.

c) Xác định tập hợp D gồm các ứng viên đạt ít nhất một trong hai yêu cầu về chuyên môn và ngoại ngữ.

[Hình 1: Minh họa một cuộc trò chuyện giữa bốn người, với hai người đang nói "Xin chào. Chị hãy giới thiệu về mình." và "Xin chào..."]

Cho hai tập hợp A và B.

Tập hợp các phần tử thuộc A hoặc thuộc B gọi là hợp của hai tập hợp A và B, kí hiệu $A \cup B$.

$A \cup B = \{x | x \in A \text{ hoặc } x \in B\}$

Tập hợp các phần tử thuộc cả hai tập hợp A và B gọi là giao của hai tập hợp A và B, kí hiệu $A \cap B$.

$A \cap B = \{x | x \in A \text{ và } x \in B\}$

[Hình 2: Minh họa bằng sơ đồ Venn về hợp và giao của hai tập hợp A và B]

Ví dụ 1

Xác định $A \cup B$ và $A \cap B$ trong mỗi trường hợp sau:

a) $A = \{2; 3; 5; 7\}, B = \{1; 3; 5; 15\}$;

b) $A = \{x \in \mathbb{R} | x(x + 2) = 0\}, B = \{x \in \mathbb{R} | x^2 + 2 = 0\}$;

c) A là tập hợp các hình bình hành, B là tập hợp các hình thoi.

Giải

a) $A \cup B = \{1, 2, 3, 5, 7, 15\}, A \cap B = \{3, 5\}$

b) Phương trình $x(x + 2) = 0$ có hai nghiệm là 0 và -2, nên $A = \{-2, 0\}$.
Phương trình $x^2 + 2 = 0$ vô nghiệm, nên $B = \emptyset$.
Từ đó, $A \cup B = A \cup \emptyset = A = \{-2, 0\}, A \cap B = A \cap \emptyset = \emptyset$.

c) Vì mỗi hình thoi cũng là hình bình hành nên $B \subset A$. Từ đó, $A \cup B = A, A \cap B = B$.

Ví dụ 2

Lớp 10D có 22 bạn chơi bóng đá, 25 bạn chơi cầu lông và 15 bạn chơi cả hai môn thể thao này. Hỏi lớp 10D có bao nhiêu học sinh chơi ít nhất một trong hai môn thể thao bóng đá và cầu lông?

Giải

Kí hiệu A, B lần lượt là tập hợp các học sinh của lớp 10D chơi bóng đá, chơi cầu lông.

Theo giả thiết, $n(A) = 22, n(B) = 25, n(A \cap B) = 15$.

[Hình 3: Minh họa bằng sơ đồ Venn về tập hợp A và B với phần giao được tô màu]