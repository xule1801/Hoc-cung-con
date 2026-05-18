# Hotfix Workflow

Kích hoạt: lỗi critical trên production.

## Các bước
1. Tạo docs/hotfix/HF-[id]-[mô-tả].md
2. Branch: hotfix/HF-[id]-[mô-tả] tách từ main
3. BA Agent: đánh giá impact, xác định scope tối giản
4. Dev Agent: fix trên branch hotfix
5. Test Agent: regression test + test case cho lỗi cụ thể
6. Review Agent: review nhanh (không bỏ qua)
7. DevOps Agent: deploy staging → WAITING_USER_APPROVAL → production
8. Merge hotfix vào main và develop
9. Cập nhật docs/workflow-status.md
