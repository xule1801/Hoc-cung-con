# MÔ TẢ YÊU CẦU ỨNG DỤNG
## Ứng dụng học số, chữ cái, hình học, màu sắc, con vật cho trẻ 2–4 tuổi

## 1. Mục tiêu sản phẩm

Xây dựng một ứng dụng học tập nhỏ, chạy trên nền web, không yêu cầu đăng nhập, giúp trẻ từ 2 đến 4 tuổi làm quen với các kiến thức cơ bản gồm:

- Màu sắc.
- Hình học.
- Bảng chữ cái.
- Con vật.
- Con số.
- Hình phẳng và hình khối.
- Ngôn ngữ tiếng Việt và tiếng Anh.

Ứng dụng cần có giao diện trực quan, sinh động, dễ sử dụng, phù hợp với trẻ nhỏ chưa biết đọc. Nội dung học tập chủ yếu thông qua hình ảnh, âm thanh, giọng đọc và tương tác chọn đáp án.

---

## 2. Đối tượng sử dụng

### 2.1. Người dùng chính

Trẻ em từ 2 đến 4 tuổi.

Đặc điểm:

- Chưa biết đọc hoặc mới nhận diện một số ký hiệu cơ bản.
- Tương tác chủ yếu bằng cách chạm, bấm vào hình ảnh.
- Cần giao diện đơn giản, hình ảnh lớn, màu sắc tươi sáng.
- Cần được khích lệ liên tục trong quá trình học.

### 2.2. Người hỗ trợ

Phụ huynh, giáo viên mầm non hoặc người chăm sóc trẻ.

Vai trò:

- Mở ứng dụng.
- Chọn chủ đề học.
- Chọn ngôn ngữ.
- Hỗ trợ trẻ khi cần thiết.
- Theo dõi điểm số sau mỗi lượt chơi.

---

## 3. Phạm vi ứng dụng

Ứng dụng là một web app nhỏ, không yêu cầu đăng nhập tài khoản, không lưu thông tin cá nhân của trẻ.

### 3.1. Nền tảng triển khai

- Ứng dụng chạy trên trình duyệt web.
- Có thể sử dụng trên máy tính, máy tính bảng hoặc điện thoại.
- Giao diện ưu tiên tối ưu cho thiết bị cảm ứng.
- Backend/hosting ưu tiên sử dụng các nền tảng miễn phí hoặc chi phí thấp như Vercel.
- Frontend lập trình bằng Streamlit hoặc công nghệ tương đương nếu phù hợp với ràng buộc kỹ thuật.

Lưu ý cho BA/Technical Team: Streamlit phù hợp làm ứng dụng web nhanh, nhưng khi triển khai cần kiểm tra lại mức độ tương thích với Vercel. Nếu Vercel không phù hợp cho Streamlit runtime, có thể cân nhắc Streamlit Community Cloud, Hugging Face Spaces, Render hoặc nền tảng free-tier tương đương.

---

## 4. Chức năng chính

## 4.1. Màn hình trang chủ

Ứng dụng cần có màn hình trang chủ thân thiện với trẻ nhỏ.

### Nội dung chính

- Tên ứng dụng.
- Hình ảnh minh họa vui nhộn.
- Nút bắt đầu học/chơi.
- Nút chọn ngôn ngữ:
  - Tiếng Việt.
  - Tiếng Anh.
- Nút chọn chủ đề:
  - Màu sắc.
  - Hình học.
  - Bảng chữ cái.
  - Con vật.
  - Con số.

### Yêu cầu giao diện

- Nút bấm lớn, bo góc, dễ chạm.
- Màu sắc tươi sáng, hài hòa.
- Có icon/hình minh họa cho từng chủ đề.
- Hạn chế chữ dài vì trẻ chưa biết đọc.
- Có thể có nhạc nền tươi vui, phù hợp trẻ nhỏ.
- Có nút bật/tắt âm thanh để phụ huynh kiểm soát.

---

## 4.2. Chọn ngôn ngữ

Ứng dụng cho phép chọn một trong hai ngôn ngữ:

- Tiếng Việt.
- Tiếng Anh.

Ngôn ngữ ảnh hưởng đến:

- Giọng đọc câu hỏi.
- Tên đối tượng cần tìm.
- Câu khen ngợi.
- Câu khích lệ khi trả lời sai.
- Nội dung hiển thị trên giao diện.

Ví dụ:

Tiếng Việt:

- “Con hãy chọn màu đỏ.”
- “Giỏi quá!”
- “Không sao, mình thử lại nhé!”

Tiếng Anh:

- “Please choose the red color.”
- “Great job!”
- “Try again, you can do it!”

---

## 4.3. Chọn chủ đề học

Người dùng có thể chọn một trong các chủ đề sau.

### 4.3.1. Chủ đề màu sắc

Nội dung gồm các màu cơ bản:

- Đỏ.
- Xanh lá.
- Xanh dương.
- Vàng.
- Cam.
- Tím.
- Hồng.
- Đen.
- Trắng.
- Nâu.
- Xám.

Hình ảnh đáp án có thể là các mảng màu, đồ vật cùng màu hoặc hình minh họa sinh động.

Ví dụ câu hỏi:

- “Con hãy chọn màu vàng.”
- Ứng dụng hiển thị 4 đáp án bằng hình ảnh/mảng màu.
- Trẻ chọn đáp án đúng.

---

### 4.3.2. Chủ đề hình học

Chủ đề hình học gồm hai nhóm.

#### a. Hình phẳng

Bao gồm:

- Hình tròn.
- Hình vuông.
- Hình tam giác.
- Hình chữ nhật.
- Hình ngôi sao.
- Hình trái tim.
- Hình thoi.
- Hình bầu dục.

#### b. Hình khối

Bao gồm:

- Hình cầu.
- Hình lập phương.
- Hình hộp chữ nhật.
- Hình trụ.
- Hình nón.
- Hình chóp.
- Hình lăng trụ đơn giản.

Ví dụ câu hỏi:

- “Con hãy chọn hình tròn.”
- “Please choose the cube.”

Ứng dụng hiển thị 4 hình ảnh trực quan để trẻ lựa chọn.

---

### 4.3.3. Chủ đề bảng chữ cái

Ứng dụng hỗ trợ học bảng chữ cái theo ngôn ngữ đã chọn.

#### Với tiếng Việt

Bao gồm các chữ cái tiếng Việt cơ bản:

- A, Ă, Â, B, C, D, Đ, E, Ê, G, H, I, K, L, M, N, O, Ô, Ơ, P, Q, R, S, T, U, Ư, V, X, Y.

Có thể mở rộng thêm nhận diện chữ thường và chữ hoa.

Ví dụ:

- Ứng dụng đọc: “Chữ A”.
- Trẻ chọn đúng chữ A trong 4 đáp án.

#### Với tiếng Anh

Bao gồm bảng chữ cái tiếng Anh:

- A đến Z.

Ví dụ:

- Ứng dụng đọc: “Letter B”.
- Trẻ chọn đúng chữ B trong 4 đáp án.

Yêu cầu hiển thị chữ cái phải lớn, rõ nét, màu sắc bắt mắt.

---

### 4.3.4. Chủ đề con vật

Bao gồm các con vật quen thuộc với trẻ nhỏ.

Ví dụ:

- Chó.
- Mèo.
- Gà.
- Vịt.
- Cá.
- Chim.
- Voi.
- Hổ.
- Sư tử.
- Khỉ.
- Bò.
- Ngựa.
- Cừu.
- Dê.
- Thỏ.
- Gấu.
- Rùa.
- Ếch.

Mỗi câu hỏi sẽ đọc tên con vật, trẻ chọn hình đúng trong 4 hình.

Ví dụ:

- “Con hãy chọn con mèo.”
- “Please choose the elephant.”

Có thể kèm tiếng kêu động vật ở phần phản hồi đúng để tăng hứng thú.

---

### 4.3.5. Chủ đề con số

Ứng dụng hỗ trợ nhận diện và nghe đọc số.

Phạm vi số:

- Từ 0 đến 1.000.000.000.
- Với các số nhỏ, có thể xuất hiện đa dạng.
- Với các số lớn hơn 10.000, chỉ sử dụng các số tròn chẵn để phù hợp với trẻ và tránh gây khó hiểu.

#### Nhóm số đề xuất

- 0 đến 20.
- 21 đến 100.
- Các số tròn chục: 10, 20, 30, …, 100.
- Các số tròn trăm: 100, 200, 300, …, 1.000.
- Các số tròn nghìn: 1.000, 2.000, 5.000, 10.000.
- Trên 10.000 chỉ lấy số tròn:
  - 20.000.
  - 50.000.
  - 100.000.
  - 500.000.
  - 1.000.000.
  - 10.000.000.
  - 100.000.000.
  - 1.000.000.000.

Ví dụ câu hỏi:

- “Con hãy chọn số 5.”
- “Con hãy chọn số một nghìn.”
- “Please choose number ten.”

Đáp án có thể hiển thị dưới dạng số lớn, rõ ràng, kèm hình ảnh minh họa nếu phù hợp.

---

## 5. Luồng chơi chính

Mỗi lượt chơi gồm 10 câu hỏi.

### 5.1. Bắt đầu lượt chơi

Người dùng thực hiện:

1. Chọn ngôn ngữ.
2. Chọn chủ đề.
3. Bấm nút bắt đầu.

Hệ thống tạo một bộ câu hỏi gồm 10 câu theo chủ đề đã chọn.

---

### 5.2. Cấu trúc mỗi câu hỏi

Mỗi câu hỏi gồm:

- Câu hỏi bằng giọng đọc.
- Có thể hiển thị biểu tượng loa để phát lại câu hỏi.
- 4 đáp án bằng hình ảnh.
- Trẻ chọn 1 đáp án.

Ví dụ:

Câu hỏi: “Con hãy chọn hình tam giác.”

Đáp án hiển thị:

- Hình tròn.
- Hình vuông.
- Hình tam giác.
- Hình chữ nhật.

Trẻ bấm vào hình tam giác.

---

### 5.3. Phản hồi khi trả lời đúng

Khi trẻ chọn đúng:

- Hiển thị hiệu ứng vui vẻ.
- Phát âm thanh chúc mừng.
- Hiển thị câu khen ngợi.
- Tăng điểm.
- Sau một khoảng thời gian ngắn, chuyển sang câu tiếp theo.

Ví dụ câu khen:

- “Giỏi quá!”
- “Con làm rất tốt!”
- “Tuyệt vời!”
- “Chính xác rồi!”
- “Con thông minh lắm!”

Tiếng Anh:

- “Great job!”
- “Well done!”
- “Excellent!”
- “That’s right!”
- “You are amazing!”

---

### 5.4. Phản hồi khi trả lời sai

Khi trẻ chọn sai:

- Không tạo cảm giác thất bại.
- Hiển thị câu khích lệ nhẹ nhàng.
- Cho trẻ biết đáp án đúng.
- Có thể làm nổi bật đáp án đúng bằng viền sáng hoặc hiệu ứng.
- Sau đó chuyển sang câu tiếp theo.

Ví dụ câu khích lệ:

- “Không sao, mình cùng học tiếp nhé!”
- “Gần đúng rồi, đáp án đúng là hình tròn.”
- “Con thử lại ở câu tiếp theo nhé!”
- “Cố lên, con đang làm rất tốt!”

Tiếng Anh:

- “That’s okay, let’s keep learning!”
- “Good try! The correct answer is the circle.”
- “Try the next one!”
- “You are doing great!”

---

### 5.5. Kết thúc lượt chơi

Sau 10 câu hỏi, hệ thống hiển thị màn hình kết quả.

Thông tin hiển thị:

- Tổng số câu: 10.
- Số câu đúng.
- Số câu sai.
- Điểm số.
- Nhận xét khích lệ.
- Nút chơi lại.
- Nút đổi chủ đề.
- Nút quay về trang chủ.

Ví dụ:

- “Con trả lời đúng 8/10 câu. Rất tuyệt vời!”
- “Con đã hoàn thành bài học. Mình chơi lại nhé!”

---

## 6. Cơ chế điểm số

Mỗi lượt chơi gồm 10 câu.

Đề xuất cách tính:

- Trả lời đúng: 1 điểm.
- Trả lời sai: 0 điểm.
- Tổng điểm tối đa: 10 điểm.

Phân loại kết quả:

| Điểm | Nhận xét |
|---:|---|
| 0–3 | Con đã cố gắng rất tốt, mình cùng học lại nhé! |
| 4–6 | Khá lắm, con đang tiến bộ rồi! |
| 7–8 | Rất tốt, con trả lời rất giỏi! |
| 9–10 | Tuyệt vời, con thật xuất sắc! |

---

## 7. Yêu cầu về âm thanh

Ứng dụng cần có âm thanh để tăng tính tương tác.

### 7.1. Âm thanh nền

- Nhạc nền tươi vui, nhẹ nhàng, phù hợp trẻ nhỏ.
- Không quá ồn, không gây mất tập trung.
- Có nút bật/tắt nhạc nền.
- Mặc định có thể tắt hoặc bật tùy quyết định thiết kế sản phẩm, nhưng cần dễ điều chỉnh.

### 7.2. Giọng đọc câu hỏi

- Mỗi câu hỏi cần có giọng đọc.
- Giọng đọc rõ ràng, chậm, thân thiện.
- Hỗ trợ tiếng Việt và tiếng Anh.
- Có nút nghe lại câu hỏi.

### 7.3. Âm thanh phản hồi

Khi trả lời đúng:

- Âm thanh vui vẻ.
- Có thể có hiệu ứng vỗ tay, chuông vui, tiếng “yay”.

Khi trả lời sai:

- Âm thanh nhẹ nhàng.
- Không dùng âm thanh tiêu cực, giật mình hoặc gây sợ hãi.

---

## 8. Yêu cầu về hình ảnh

Vì trẻ 2–4 tuổi chưa biết đọc, hình ảnh là thành phần trung tâm của ứng dụng.

### 8.1. Nguyên tắc hình ảnh

- Hình lớn, rõ ràng, ít chi tiết rối.
- Màu sắc tươi sáng.
- Phong cách hoạt hình thân thiện.
- Đối tượng trong hình phải dễ nhận biết.
- Tránh hình ảnh bạo lực, đáng sợ hoặc gây hiểu nhầm.

### 8.2. Đáp án dạng hình ảnh

Mỗi câu hỏi có 4 đáp án.

Yêu cầu:

- Các đáp án có kích thước tương đương.
- Khoảng cách giữa các đáp án đủ rộng để trẻ dễ bấm.
- Đáp án đúng và sai không được quá giống nhau đối với trẻ nhỏ.
- Tránh đánh lừa trẻ bằng các hình quá phức tạp.

---

## 9. Yêu cầu giao diện người dùng

### 9.1. Phong cách thiết kế

- Vui nhộn.
- Sáng sủa.
- Nhiều màu sắc nhưng không rối.
- Phù hợp trẻ mầm non.
- Icon lớn, dễ hiểu.
- Ít chữ, ưu tiên hình ảnh và âm thanh.

### 9.2. Bố cục màn hình chơi

Màn hình chơi nên có:

- Khu vực câu hỏi/biểu tượng loa ở phía trên.
- 4 đáp án lớn ở trung tâm.
- Thanh tiến độ, ví dụ: “Câu 3/10”.
- Điểm hiện tại.
- Nút tắt/bật âm thanh.
- Nút thoát hoặc quay về trang chủ.

### 9.3. Tương tác

- Tối ưu cho thao tác chạm.
- Nút bấm phải lớn.
- Có hiệu ứng khi chạm vào đáp án.
- Không yêu cầu thao tác kéo thả phức tạp ở phiên bản đầu tiên.

---

## 10. Yêu cầu nội dung dữ liệu

BA cần phối hợp với nhóm nội dung để xây dựng bộ dữ liệu ban đầu cho từng chủ đề.

Mỗi đối tượng học nên có các trường thông tin sau:

| Trường dữ liệu | Mô tả |
|---|---|
| ID | Mã định danh nội dung |
| Chủ đề | Màu sắc, hình học, chữ cái, con vật, con số |
| Nhóm con | Ví dụ: hình phẳng, hình khối |
| Tên tiếng Việt | Tên đối tượng bằng tiếng Việt |
| Tên tiếng Anh | Tên đối tượng bằng tiếng Anh |
| Hình ảnh | Đường dẫn file ảnh |
| Âm thanh tiếng Việt | File giọng đọc tiếng Việt |
| Âm thanh tiếng Anh | File giọng đọc tiếng Anh |
| Độ khó | Dễ, trung bình, nâng cao |
| Ghi chú | Thông tin bổ sung nếu có |

Ví dụ:

| ID | Chủ đề | Tên tiếng Việt | Tên tiếng Anh | Hình ảnh |
|---|---|---|---|---|
| ANIMAL_001 | Con vật | Con mèo | Cat | cat.png |
| COLOR_001 | Màu sắc | Màu đỏ | Red | red.png |
| SHAPE_001 | Hình học | Hình tròn | Circle | circle.png |
| NUMBER_005 | Con số | Số 5 | Number five | number_5.png |

---

## 11. Quy tắc sinh câu hỏi

Mỗi lượt chơi có 10 câu hỏi.

### 11.1. Nguyên tắc chọn câu hỏi

- Câu hỏi lấy theo chủ đề người dùng đã chọn.
- Mỗi câu có 1 đáp án đúng và 3 đáp án sai.
- Thứ tự đáp án được xáo trộn ngẫu nhiên.
- Không nên lặp lại cùng một câu hỏi quá nhiều lần trong một lượt chơi.
- Đáp án sai nên cùng nhóm nội dung để đảm bảo hợp lý.

Ví dụ:

Nếu câu hỏi là “Chọn con mèo”, đáp án sai nên là các con vật khác như chó, thỏ, gà; không nên là màu đỏ hoặc số 5.

Nếu câu hỏi là “Chọn hình cầu”, đáp án sai nên là hình lập phương, hình trụ, hình nón.

---

## 12. Các màn hình chính

Ứng dụng tối thiểu gồm các màn hình sau:

| Màn hình | Mô tả |
|---|---|
| Trang chủ | Giới thiệu ứng dụng, bắt đầu chơi |
| Chọn ngôn ngữ | Chọn tiếng Việt hoặc tiếng Anh |
| Chọn chủ đề | Chọn màu sắc, hình học, chữ cái, con vật, con số |
| Màn hình chơi | Hiển thị câu hỏi và 4 đáp án |
| Màn hình phản hồi | Khen ngợi hoặc khích lệ sau khi trả lời |
| Màn hình kết quả | Hiển thị điểm sau 10 câu |
| Màn hình hướng dẫn phụ huynh | Mô tả ngắn cách sử dụng ứng dụng |

---

## 13. Yêu cầu phi chức năng

### 13.1. Hiệu năng

- Ứng dụng tải nhanh trên kết nối Internet thông thường.
- Hình ảnh và âm thanh cần được tối ưu dung lượng.
- Thời gian phản hồi sau khi trẻ bấm đáp án dưới 1 giây.

### 13.2. Khả dụng

- Không yêu cầu đăng nhập.
- Không yêu cầu nhập thông tin cá nhân.
- Có thể sử dụng ngay sau khi mở web.
- Hoạt động tốt trên trình duyệt phổ biến.

### 13.3. Bảo mật và quyền riêng tư

- Không thu thập thông tin cá nhân của trẻ.
- Không yêu cầu camera, micro hoặc vị trí.
- Không có chat, bình luận hoặc tương tác với người lạ.
- Không hiển thị quảng cáo không phù hợp với trẻ em.
- Nếu có thống kê sử dụng, chỉ nên thu thập dữ liệu ẩn danh ở mức tổng quan.

### 13.4. Khả năng mở rộng

Ứng dụng nên được thiết kế để có thể mở rộng thêm:

- Chủ đề mới.
- Bộ câu hỏi mới.
- Ngôn ngữ mới.
- Cấp độ khó.
- Chế độ học tự do.
- Chế độ luyện tập theo độ tuổi.
- Báo cáo tiến độ học nếu sau này bổ sung tài khoản phụ huynh.

---

## 14. Yêu cầu kiểm thử

BA và QA cần kiểm thử các nhóm tình huống sau:

### 14.1. Kiểm thử chức năng

- Chọn được ngôn ngữ tiếng Việt.
- Chọn được ngôn ngữ tiếng Anh.
- Chọn được từng chủ đề.
- Mỗi lượt chơi có đúng 10 câu.
- Mỗi câu có đúng 4 đáp án.
- Chỉ có 1 đáp án đúng.
- Chọn đúng thì cộng điểm.
- Chọn sai thì không cộng điểm.
- Sau câu thứ 10 hiển thị kết quả.
- Nút chơi lại hoạt động đúng.
- Nút đổi chủ đề hoạt động đúng.

### 14.2. Kiểm thử âm thanh

- Nhạc nền phát đúng.
- Có thể tắt/bật nhạc nền.
- Câu hỏi có giọng đọc.
- Có thể nghe lại câu hỏi.
- Âm thanh phản hồi đúng/sai hoạt động chính xác.
- Âm lượng không quá lớn hoặc gây khó chịu.

### 14.3. Kiểm thử giao diện

- Hiển thị tốt trên điện thoại.
- Hiển thị tốt trên máy tính bảng.
- Hiển thị tốt trên máy tính.
- Nút bấm đủ lớn.
- Hình ảnh không bị vỡ, méo.
- Trẻ dễ nhận biết đáp án.

### 14.4. Kiểm thử nội dung

- Tên tiếng Việt chính xác.
- Tên tiếng Anh chính xác.
- Hình ảnh khớp với tên gọi.
- Âm thanh đọc đúng nội dung.
- Không có hình ảnh hoặc âm thanh không phù hợp với trẻ nhỏ.

---

## 15. Phiên bản MVP đề xuất

Phiên bản đầu tiên nên tập trung vào các chức năng cốt lõi.

### 15.1. Chức năng có trong MVP

- Không đăng nhập.
- Chạy trên web.
- Chọn tiếng Việt hoặc tiếng Anh.
- Chọn 5 chủ đề:
  - Màu sắc.
  - Hình học.
  - Bảng chữ cái.
  - Con vật.
  - Con số.
- Mỗi lượt chơi 10 câu.
- Mỗi câu có 4 đáp án bằng hình ảnh.
- Có âm thanh câu hỏi.
- Có phản hồi đúng/sai.
- Có chấm điểm cuối lượt chơi.
- Có nhạc nền và nút bật/tắt âm thanh.

### 15.2. Chưa cần có trong MVP

- Đăng nhập.
- Lưu lịch sử học tập.
- Bảng xếp hạng.
- Cá nhân hóa theo từng trẻ.
- Phân tích tiến độ học tập.
- Hệ thống quản trị nội dung phức tạp.
- Thanh toán.
- Quảng cáo.

---

## 16. Một số user story tiêu biểu

### User story 1: Chọn ngôn ngữ

Là phụ huynh, tôi muốn chọn tiếng Việt hoặc tiếng Anh để trẻ có thể học theo ngôn ngữ phù hợp.

Tiêu chí chấp nhận:

- Có lựa chọn tiếng Việt.
- Có lựa chọn tiếng Anh.
- Sau khi chọn, toàn bộ câu hỏi và âm thanh sử dụng ngôn ngữ tương ứng.

---

### User story 2: Chọn chủ đề học

Là phụ huynh, tôi muốn chọn chủ đề học để trẻ luyện tập đúng nội dung mong muốn.

Tiêu chí chấp nhận:

- Hiển thị danh sách chủ đề bằng icon/hình ảnh.
- Người dùng chọn được một chủ đề.
- Ứng dụng bắt đầu câu hỏi theo đúng chủ đề đã chọn.

---

### User story 3: Trẻ trả lời câu hỏi

Là trẻ nhỏ, tôi muốn nghe câu hỏi và chọn một trong bốn hình ảnh để trả lời.

Tiêu chí chấp nhận:

- Câu hỏi được đọc bằng âm thanh.
- Có 4 đáp án bằng hình ảnh.
- Trẻ có thể bấm chọn đáp án.
- Ứng dụng xác định đúng/sai.

---

### User story 4: Phản hồi khi đúng

Là trẻ nhỏ, tôi muốn được khen khi trả lời đúng để cảm thấy vui và muốn tiếp tục học.

Tiêu chí chấp nhận:

- Khi chọn đúng, ứng dụng hiển thị lời khen.
- Có âm thanh vui vẻ.
- Điểm số được cộng thêm 1.
- Ứng dụng chuyển sang câu tiếp theo.

---

### User story 5: Phản hồi khi sai

Là trẻ nhỏ, tôi muốn được khích lệ khi trả lời sai để không cảm thấy thất vọng.

Tiêu chí chấp nhận:

- Khi chọn sai, ứng dụng không hiển thị thông báo tiêu cực.
- Có câu khích lệ nhẹ nhàng.
- Ứng dụng hiển thị đáp án đúng.
- Ứng dụng chuyển sang câu tiếp theo.

---

### User story 6: Xem kết quả

Là phụ huynh, tôi muốn xem điểm sau mỗi lượt chơi để biết trẻ trả lời đúng bao nhiêu câu.

Tiêu chí chấp nhận:

- Sau 10 câu, ứng dụng hiển thị kết quả.
- Có số câu đúng.
- Có số câu sai.
- Có tổng điểm.
- Có nhận xét khích lệ.
- Có nút chơi lại hoặc đổi chủ đề.

---

## 17. Định hướng thiết kế tổng thể

Ứng dụng cần tạo cảm giác như một trò chơi học tập nhẹ nhàng, không gây áp lực cho trẻ. Trọng tâm không phải là kiểm tra nghiêm túc, mà là giúp trẻ nhận biết, nghe, nhìn, chọn và ghi nhớ thông qua tương tác lặp lại.

Nguyên tắc thiết kế quan trọng:

- Học qua chơi.
- Không gây áp lực.
- Sai vẫn được khích lệ.
- Giao diện đơn giản.
- Hình ảnh là trung tâm.
- Âm thanh đóng vai trò hướng dẫn chính.
- Mỗi lượt chơi ngắn, phù hợp khả năng tập trung của trẻ 2–4 tuổi.
