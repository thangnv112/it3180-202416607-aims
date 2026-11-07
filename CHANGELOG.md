# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-11-07
### Fixed
- search_by_title: tìm kiếm không phân biệt hoa thường (case-insensitive) (#22).

## [1.0.0] - 2026-11-07
### Added
- Cart.print_cart(), search_by_title(), total_cost_with_discount().
- 4 unit tests covering Cart limits, discounts, item removal, and title search.
- Use case diagram and system documentation in `docs/use-case.md`.

### Fixed
- Giỏ hàng nhận đĩa thứ 21 (#8).
- Công thức tính phần trăm giảm giá và kiểm tra ngoại lệ ValueError.
