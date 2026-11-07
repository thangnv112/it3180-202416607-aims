# Báo cáo Trả lời Câu hỏi Thảo luận – Lab 04
**Môn học:** IT3180 – Quản lý cấu hình phần mềm  
**Thực hiện:** Nguyễn Văn Thắng – MSSV: 202416607

---

### Câu 1 (Slide 52): Vì sao `release/*` không merge vào `master`? So sánh với GitFlow.

1. **Trong mô hình Release Flow:**
   * **Nguyên tắc dòng chảy một chiều (`master` $\rightarrow$ `release/*`):** `master` là nguồn chân lý duy nhất (Single Source of Truth). Mọi công việc chuẩn bị cho bản phát hành (như tăng số phiên bản `__version__`, cập nhật `CHANGELOG.md`, kiểm thử cuối cùng) đều phải được thực hiện trên các nhánh con (`topic/*`) và merge vào `master` **trước** khi tạo nhánh `release/*`.
   * **Nhánh `release/*` là nhánh đóng băng (Baseline):** Khi được tạo ra từ `master`, nhánh `release/*` đã hoàn chỉnh 100% và chỉ đóng vai trò bảo trì, phát hành cho người dùng. Vì không có commit phát triển tính năng mới nào được phép thêm trực tiếp vào nhánh này nên không có lý do gì để merge ngược lại vào `master`.

2. **So sánh với GitFlow:**
   * Trong mô hình **GitFlow** truyền thống:
     * Tồn tại 2 nhánh dài hạn song song: `main/master` (chứa mã nguồn phát hành) và `develop` (chứa mã nguồn đang phát triển).
     * Nhánh `release/*` được rẽ ra từ `develop`. Trong quá trình release, các bản sửa lỗi nhỏ (bugfix) được commit trực tiếp trên nhánh `release/*`.
     * Khi kết thúc phát hành, GitFlow bắt buộc phải **merge nhánh `release/*` vào cả 2 nhánh**: merge vào `main` để gắn tag phát hành, và merge ngược lại vào `develop` để không bị mất các bản sửa lỗi đó.
   * **Ưu điểm của Release Flow:** Tránh được cấu trúc phức tạp của 2 nhánh dài hạn, loại bỏ nguy cơ xung đột khi merge ngược (back-merge), và phù hợp với quy trình tích hợp liên tục (CI/CD) hiện đại.

---

### Câu 2 (Slide 52): Vì sao lên 1.0.0 mà không phải 0.4.0?

Theo đặc tả của **Semantic Versioning (SemVer 2.0.0)** (`MAJOR.MINOR.PATCH`):
1. **Giai đoạn `0.y.z` (Initial Development):**
   * Các phiên bản `v0.1.0`, `v0.2.0`, `v0.3.0` ở Lab 01–03 thuộc giai đoạn xây dựng ban đầu. Phần mềm chưa hoàn chỉnh, API và cấu trúc mã nguồn có thể thay đổi bất kỳ lúc nào mà không đảm bảo tính ổn định hay tương thích ngược.
2. **Ý nghĩa của cột mốc `1.0.0` (First Production/Stable Release):**
   * Đánh dấu sản phẩm đã hoàn thiện các tính năng cốt lõi theo đặc tả yêu cầu (đã có giỏ hàng, tính tiền, giảm giá, tìm kiếm, sắp xếp và in ấn).
   * Đã có bộ bài kiểm thử tự động (Unit Tests) hoàn chỉnh đảm bảo chất lượng và độ tin cậy.
   * Đã có tài liệu theo dõi thay đổi (`CHANGELOG.md`) và quy trình bảo vệ nhánh chính thức.
   * Bắt đầu từ phiên bản `1.0.0`, dự án cam kết về tính ổn định của API: mọi thay đổi phá vỡ tính tương thích ngược trong tương lai bắt buộc phải tăng số phiên bản `MAJOR` (lên `2.0.0`). Do đó, việc chuyển từ `0.3.0` lên `1.0.0` thay vì `0.4.0` khẳng định phần mềm đã chuyển từ giai đoạn bản nháp thử nghiệm sang **bản sản phẩm chính thức đầu tiên**.
