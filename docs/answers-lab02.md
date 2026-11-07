# Báo cáo Trả lời Câu hỏi Thảo luận – Lab 02
**Môn học:** IT3180 – Quản lý cấu hình phần mềm  
**Thực hiện:** Nguyễn Văn Thắng – MSSV: 202416607

---

### Câu 1 (Slide 35): Vì sao phải đồng bộ master trước khi PR?

Cần đồng bộ nhánh tính năng với `master` mới nhất trước khi mở hoặc gộp Pull Request vì các lý do sau:
1. **Phát hiện và giải quyết xung đột sớm (Shift-left conflict resolution):** Trong lúc ta đang phát triển nhánh tính năng, các đồng nghiệp khác có thể đã merge code mới vào `master`. Việc kéo `master` về nhánh của mình giúp lập trình viên tự phát hiện và giải quyết các xung đột (Merge Conflicts) ngay tại máy cá nhân thay vì đẩy lỗi lên GitHub.
2. **Kiểm thử tích hợp tại chỗ (Local integration test):** Đảm bảo mã nguồn mới tích hợp hài hòa và tương thích với mã nguồn mới nhất trên `master` (ví dụ: chạy `python main.py` kiểm tra không bị lỗi logic trước khi gửi yêu cầu duyệt).
3. **Giữ Pull Request luôn ở trạng thái "Clean" (Mergeable):** Giúp Pull Request hiển thị trạng thái xanh `Able to merge`, giảm thiểu công sức cho người bình duyệt (Reviewer) và giúp quá trình merge diễn ra tự động, an toàn.

---

### Câu 2 (Slide 35): Khi nào không được rebase?

* **Quy tắc vàng của Rebase (The Golden Rule of Rebase):** Tuyệt đối **KHÔNG ĐƯỢC REBASE** trên các nhánh công khai (public branch) hoặc nhánh dùng chung đã được chia sẻ với các thành viên khác trong nhóm (chẳng hạn như `master`, `main`, `release/*` hoặc nhánh chung đang nhiều người cùng làm việc).
* **Lý do kỹ thuật SCM:**
  * Lệnh `git rebase` hoạt động bằng cách tạo ra các commit mới với mã băm (SHA hash) hoàn toàn mới, đồng thời viết lại lịch sử commit.
  * Nếu một lập trình viên rebase và force push lên nhánh công khai, toàn bộ lịch sử commit của các thành viên khác đang làm việc trên nhánh đó sẽ bị phân kỳ (diverged), gây ra xung đột nghiêm trọng, trùng lặp commit và nguy cơ làm mất code của cả nhóm.
* **Chỉ nên dùng rebase khi:** Làm việc trên nhánh cá nhân (local branch hoặc private feature branch) chưa công khai, hoặc dùng tính năng *Rebase and merge* trên giao diện GitHub khi đã hoàn tất quy trình review.

---

### Câu 3 (Slide 35): `feature/*` khác `topic/*` ra sao?

Trong quy ước phân nhánh (Branching Convention) của Release Flow:
1. **`feature/*` (Feature branch):**
   * **Mục đích:** Dùng để phát triển các tính năng nghiệp vụ cụ thể cho người dùng cuối (User-facing feature), bổ sung trực tiếp các chức năng mới vào mã nguồn của ứng dụng.
   * **Ví dụ trong bài:** `feature/cart-print` (tính năng in giỏ hàng), `feature/search-by-title` (tính năng tìm kiếm DVD).
2. **`topic/*` (Topic branch):**
   * **Mục đích:** Dùng cho các công việc mang tính chuyên đề, phi chức năng hoặc hạ tầng dự án, không trực tiếp thay đổi tính năng nghiệp vụ người dùng (như viết tài liệu, cấu hình dự án, biểu đồ phân tích, thiết lập CI/CD, hoặc các thử nghiệm công nghệ).
   * **Ví dụ trong bài:** `topic/pr-template` (thiết lập mẫu Pull Request), `topic/use-case-diagram` (tài liệu biểu đồ ca sử dụng), `topic/ci-unit-tests` (thiết lập pipeline CI).
