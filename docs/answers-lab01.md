# Báo cáo Trả lời Câu hỏi Thảo luận – Lab 01
**Môn học:** IT3180 – Quản lý cấu hình phần mềm  
**Thực hiện:** Nguyễn Văn Thắng – MSSV: 202416607

---

### Câu 1 (Slide 19): Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?

* **Vị trí lưu trữ:**
  * Cấu hình `--global` được lưu tại file `.gitconfig` trong thư mục Home của người dùng:
    * Trên Windows: `C:\Users\<Username>\.gitconfig` (tương đương `~/.gitconfig` trong Git Bash).
    * Trên Linux/macOS: `~/.gitconfig`.
  * Cấu hình `--local` được lưu tại file `.git/config` nằm ngay bên trong thư mục của repository hiện tại.
* **Sự khác biệt:**
  * **Phạm vi áp dụng:**
    * `--global`: Áp dụng cho **tất cả** các repository Git trên toàn bộ máy tính của người dùng.
    * `--local`: Chỉ áp dụng riêng cho **duy nhất** repository hiện tại.
  * **Độ ưu tiên:** Cấu hình `--local` có độ ưu tiên cao hơn và sẽ ghi đè lên cấu hình `--global`. Điều này hữu ích khi một máy tính cần dùng nhiều danh tính khác nhau (ví dụ: email trường `@sis.hust.edu.vn` cho bài tập và email cá nhân cho dự án ngoài).

---

### Câu 2 (Slide 26): Vì sao dùng `git mv`?

Dùng `git mv <file_cũ> <file_mới>` thay vì thao tác đổi tên/kéo thả thông thường vì:
1. **Bảo toàn lịch sử thay đổi (Traceability):** Giúp Git nhận diện chính xác đây là thao tác di chuyển/đổi tên (`rename/move`) thay vì hiểu nhầm là "xóa file cũ" và "tạo mới một file không liên quan". Nhờ đó, ta vẫn có thể dùng `git log --follow` hoặc `git blame` để lần ngược về các commit trước đó.
2. **Tránh xung đột khi làm việc nhóm (Merge Conflicts):** Nếu thành viên khác đang sửa code trên file cũ ở nhánh của họ, khi merge, Git đủ thông minh để tự động áp dụng các thay đổi đó vào đường dẫn file mới.
3. **Tiện lợi và an toàn:** Lệnh `git mv` vừa di chuyển file trên đĩa, vừa tự động đưa trạng thái thay đổi vào vùng Staging (`git add`), tránh trường hợp quên commit việc xóa file cũ.

---

### Câu 3 (Slide 26): `release/lab01` có phải baseline?

* **CÓ, `release/lab01` chính là một Baseline (Đường cơ sở).**
* **Giải thích theo SCM:**
  * Theo định nghĩa SCM, **Baseline** là một phiên bản phần mềm/cấu hình đã được thống nhất, kiểm thử đạt chuẩn và được "đóng băng" (freeze) tại một mốc thời gian cụ thể; mọi thay đổi sau đó đều phải tuân theo quy trình kiểm soát chặt chẽ.
  * Nhánh `release/lab01` đóng vai trò là mốc bàn giao / nộp bài chính thức của Lab 01, đại diện cho trạng thái mã nguồn và tài liệu hoàn chỉnh sau khi đã tích hợp xong qua Pull Request.

---

### Câu 4 (Slide 26): Vì sao không commit thẳng master dù làm một mình?

Dù chỉ làm việc cá nhân, vẫn không nên commit trực tiếp vào `master` vì:
1. **Tuân thủ quy trình phần mềm chuyên nghiệp:** Trong thực tế, `master` là nhánh bảo vệ (Production/Mainline). Việc tập thói quen làm việc qua nhánh (`feature/*`, `refactor/*`) giúp tránh làm hỏng nhánh chính khi có lỗi phát sinh.
2. **Cô lập thay đổi (Isolation):** Mỗi nhánh phục vụ một mục đích riêng. Nếu ý tưởng refactor bị lỗi hoặc không dùng nữa, ta chỉ việc xóa nhánh đó mà không để lại "rác" trong lịch sử của `master`.
3. **Tận dụng quy trình kiểm soát qua Pull Request (PR):**
   * Giúp tự kiểm duyệt lại thay đổi (Review Diff) trước khi gộp để tránh commit nhầm file rác, file tạm (như `__pycache__`).
   * Là nơi ghi nhận mô tả mục đích, danh sách thay đổi và cách kiểm thử để phục vụ truy vết (Audit Trail).
   * Chuẩn bị sẵn cơ chế để sau này tích hợp hệ thống kiểm thử tự động CI (GitHub Actions) chặn lỗi tự động trước khi merge.