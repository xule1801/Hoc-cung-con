# Change Request Workflow

Kích hoạt: thay đổi yêu cầu sau khi đã qua gate.

## Các bước
1. Tạo docs/change-requests/CR-[id]-[mô-tả].md
   Ghi: mô tả thay đổi, gate bị ảnh hưởng, risk assessment sơ bộ
2. BA Agent: đánh giá impact lên requirements và AC
3. Architect Agent: đánh giá impact lên architecture (nếu cần)
4. Workflow Controller tổng hợp → trình người dùng:
   - Các gate cần chạy lại
   - Effort ước tính
   - Rủi ro nếu thực hiện / không thực hiện
5. Người dùng xác nhận → chạy lại từ gate bị ảnh hưởng sớm nhất
