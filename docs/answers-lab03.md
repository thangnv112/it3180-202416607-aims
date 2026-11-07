# Báo cáo Trả lời Câu hỏi Thảo luận – Lab 03
**Môn học:** IT3180 – Quản lý cấu hình phần mềm  
**Học viên thực hiện:** Nguyễn Văn Thắng – MSSV: 202416607

---

### Câu 1 (Slide 43): Merge base là gì?

* **Định nghĩa:** `Merge base` (gốc hợp nhất) giữa hai nhánh commit $A$ và $B$ là **commit tổ tiên chung gần nhất (best common ancestor)** của cả hai nhánh đó trong đồ thị lịch sử Git (Directed Acyclic Graph - DAG).
* **Vai trò trong quá trình 3-way merge:**
  * Thuật toán hợp nhất nhánh của Git (`3-way merge`) không chỉ so sánh đỉnh của 2 nhánh hiện tại mà bắt buộc phải dựa vào 3 điểm mốc:
    1. **Ours (HEAD):** Trạng thái commit của nhánh hiện tại đang đứng.
    2. **Theirs:** Trạng thái commit của nhánh cần gộp vào.
    3. **Base (Merge base):** Trạng thái tại điểm gốc chung gần nhất trước khi 2 nhánh bị rẽ nhánh.
  * Nhờ có mốc `Merge base`, Git biết được dòng code nào là do nhánh $A$ sửa, dòng nào do nhánh $B$ sửa so với bản gốc. Git chỉ báo **Merge Conflict** khi cả 2 nhánh cùng thay đổi cùng một dòng code khác với trạng thái ban đầu ở `Merge base`.
* **Câu lệnh kiểm tra:** Ta có thể xem mã băm của merge base bằng lệnh:
  ```bash
  git merge-base <branch_A> <branch_B>
  ```

---

### Câu 2 (Slide 43): Vì sao master và release/* phải dùng revert thay vì reset?

1. **Bản chất của `git reset` (Phá hủy / Viết lại lịch sử):**
   * Lệnh `git reset` dời con trỏ nhánh lùi về quá khứ và **xóa bỏ hoàn toàn các commit** phía trước nó.
   * Trên các nhánh công khai hoặc được chia sẻ cho nhiều người như `master` hoặc `release/*`, các commit đó đã được đồng nghiệp hoặc hệ thống CI/CD kéo về máy của họ. Nếu ta dùng `reset` rồi ép đẩy lên (`git push --force`), ta sẽ phá hủy lịch sử commit của cả nhóm, gây ra tình trạng phân kỳ (diverged) và xung đột nghiêm trọng.
   * Đồng thời, trên các nhánh được bật quy tắc bảo vệ (Branch Protection), hành động `force push` sau khi reset sẽ bị hệ thống từ chối hoàn toàn.

2. **Bản chất của `git revert` (Bổ sung an toàn / Tiến về phía trước):**
   * Lệnh `git revert` **không xóa bất kỳ commit cũ nào trong quá khứ**. Thay vào đó, nó tạo ra một **commit mới** mang nội dung đảo ngược (undo) chính xác những thay đổi của commit muốn hoàn tác.
   * Lịch sử phát triển luôn tiến về phía trước (Forward-moving history).
   * Các thành viên khác chỉ cần `git pull` bình thường là nhận được bản sửa lỗi mà không gặp bất kỳ lỗi lịch sử nào.
   * Giúp bảo toàn vết tích kiểm toán (Audit Trail) trong SCM: Ai cũng có thể xem lại lịch sử để biết commit đó đã từng được đưa vào vào thời điểm nào và bị hoàn tác vào thời điểm nào vì lý do gì.
