# Báo cáo Thực hành Lab 05: Hotfix Flow & Bảo trì Nhiều Phiên bản

**Học phần:** IT3180 – Quản lý cấu hình phần mềm  
**Thực hiện:** Nguyễn Văn Thắng – MSSV: 202416607  
**Kho chứa:** `https://github.com/thangnv112/it3180-202416607-aims`

---

## 1. Trả lời câu hỏi thảo luận (Slide 64)

### Câu hỏi 1: Phân tích ưu, nhược điểm của chiến lược Upstream First so với Release First trong quản lý hotfix đa phiên bản

| Chiến lược | Khái niệm & Quy trình | Ưu điểm | Nhược điểm | Trường hợp phù hợp |
| :--- | :--- | :--- | :--- | :--- |
| **Release First**<br>*(Áp dụng trong bài lab)* | - Tạo nhánh `hotfix/*` từ đúng nhánh release bị lỗi (ví dụ: `origin/release/lab04`).<br>- Vá lỗi và phát hành ngay bản PATCH (`v1.0.1`).<br>- Dùng `git cherry-pick -x` lan truyền ngược về `master` và các nhánh `release/*` khác. | - **Thời gian phát hành cực nhanh (Time to Market/Patch tối ưu):** Sửa trực tiếp trên codebase ổn định của bản release, đưa bản vá tới người dùng nhanh nhất.<br>- **An toàn cho Production:** Không bị ảnh hưởng bởi mã chưa hoàn thiện hoặc các tính năng đang phát triển dang dở trên `master`. | - **Nguy cơ lọt lỗi (Upstream Leaks):** Dễ quên lan truyền bản sửa về `master` hoặc các phiên bản kế tiếp, dẫn đến hiện tượng hồi quy lỗi (regression).<br>- Đòi hỏi quy trình kiểm toán (audit) nghiêm ngặt để kiểm tra sự có mặt của commit vá lỗi. | Phù hợp với mô hình học phần (nộp bài theo tuần, song song nhiều bản release), hoặc hệ thống phân phối phần mềm đóng gói cho khách hàng theo phiên bản cố định. |
| **Upstream First**<br>*(Mô hình Microsoft Release Flow, Linux Kernel)* | - Mọi lỗi đều được phân tích, sửa chữa và merge vào nhánh chính (`master`/`main`) trước tiên.<br>- Sau khi bản sửa đã ổn định trên `master`, mới thực hiện cherry-pick về các nhánh `release/*` cần hỗ trợ (backporting). | - **Nhánh chính luôn toàn vẹn:** Đảm bảo nhánh `master` không bao giờ bị bỏ sót lỗi; tất cả phiên bản tương lai đều tự động thừa hưởng bản vá.<br>- Tận dụng tối đa hệ thống CI/CD tự động toàn diện và test suite trên nhánh chính. | - **Tốc độ vá lỗi production chậm hơn:** Phải chờ qua quy trình kiểm thử và review trên nhánh `master`.<br>- **Dễ xung đột khi backport:** Nếu `master` đã tái cấu trúc (refactor) hoặc thay đổi kiến trúc lớn, việc cherry-pick ngược về các phiên bản release cũ có thể gặp xung đột mã phức tạp. | Phù hợp với các sản phẩm quy mô lớn, dịch vụ SaaS phát hành liên tục theo sprint hoặc hệ điều hành, thư viện mã nguồn mở lớn. |

---

### Câu hỏi 2: Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

Trong Phần F (Kiểm toán đa phiên bản - Slide 61), có 3 lệnh / kỹ thuật trực tiếp phát hiện việc bỏ quên bản sửa trên `release/lab05`:

1. **Lệnh kiểm tra thông điệp cherry-pick toàn cục:**
   ```bash
   git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"
   ```
   - **Cơ chế phát hiện:** Commit vá lỗi gốc được ghi nhận bằng mã `<FIX_SHA>`. Mỗi lần dùng `git cherry-pick -x`, Git tự động ghi dòng `(cherry picked from commit <FIX_SHA>)` vào commit mới.
   - **Hiện tượng khi quên:** Thay vì hiển thị đủ 2 commit (1 trên `master` và 1 trên `release/lab05`), lệnh sẽ chỉ hiển thị **1 commit** (trên `master`). Điều này chứng minh ngay lập tức rằng nhánh `release/lab05` chưa nhận được bản vá.

2. **Vòng lặp kiểm tra hành vi tự động trên cả 3 dòng phiên bản:**
   ```bash
   for ref in v1.0.1 v1.1.0 master; do
     git switch --detach -q $ref; printf "%-8s " $ref
     python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
     print(len(search_by_title([D('The Lion King')], 'lion')))"
   done; git switch -q master
   ```
   - **Cơ chế phát hiện:** Đoạn script chạy thử nghiệm tìm kiếm không phân biệt hoa thường (`'lion'` cho đĩa `'The Lion King'`) trên 3 điểm ref: `v1.0.1`, `v1.1.0` (trên `release/lab05`) và `master`.
   - **Hiện tượng khi quên:** Điểm gắn tag `v1.1.0` trên `release/lab05` sẽ trả về `0` (danh sách rỗng) thay vì `1`:
     ```text
     v1.0.1   1
     v1.1.0   0    <-- Phát hiện lỗi chức năng chưa được sửa!
     master   1
     ```

3. **Lệnh so sánh commit tương đương giữa hai nhánh phát hành:**
   ```bash
   git cherry -v origin/release/lab05 origin/release/lab04
   ```
   - **Cơ chế phát hiện:** Lệnh `git cherry` so sánh nội dung patch giữa hai nhánh. Nếu `release/lab05` chưa có bản vá tương đương từ `release/lab04`, commit sửa lỗi sẽ được đánh dấu bằng dấu `+` (chưa có bản tương đương), thay vì dấu `-` (đã có bản tương đương).

---

## 2. Bảng kiểm tra tiêu chí Lab 05 (Checklist Slide 63)

- [x] Tag `v1.0.1` tồn tại trên nhánh `release/lab04` và tag `v1.1.0` tồn tại trên nhánh `release/lab05`.
- [x] Lệnh `git diff --stat v1.0.0 v1.0.1` trả về đúng 4 tệp thay đổi: `CHANGELOG.md`, `aims/__init__.py`, `aims/search.py`, `tests/test_search.py`.
- [x] Tồn tại đúng 2 commit có nội dung `(cherry picked from commit 8ba9a6f7854b225a65057b170a838647a9341b6b)`.
- [x] Issue #22 (`search_by_title is case-sensitive (affects v1.0.0)`) đã được đóng tự động khi merge PR vào `master`.
- [x] Vòng lặp kiểm tra chức năng trả về kết quả `1` cho cả 3 phiên bản (`v1.0.1`, `v1.1.0`, `master`).
- [x] Đã cấu hình và kiểm thử thành công workflow CI tự động chạy Unit Tests với GitHub Actions (`.github/workflows/ci.yml`).
