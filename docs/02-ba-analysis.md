# 02 — BA Analysis (Updated)

## 1. Product Scope
- Web app hoc tap cho tre 2-4 tuoi.
- Khong yeu cau dang nhap, khong luu thong tin ca nhan.
- Ho tro 2 ngon ngu: Tieng Viet va English.
- Chu de: mau sac, hinh hoc (phang + khoi), chu cai, con vat, con so.

## 2. User Personas
- Tre 2-4 tuoi: thao tac cham, uu tien hinh anh lon, phan hoi tich cuc lien tuc.
- Phu huynh/giao vien: chon ngon ngu, chu de, theo doi diem sau moi luot.

## 3. User Stories
1. La phu huynh, toi muon chon ngon ngu de tre hoc Viet/Anh.
2. La phu huynh, toi muon chon chu de de tre hoc theo nhom kien thuc.
3. La tre, toi muon nghe cau hoi va chon 1 trong 4 dap an lon.
4. La tre, toi muon duoc khen khi dung va dong vien nhe nhang khi sai.
5. La phu huynh, toi muon xem ket qua sau 10 cau va cho tre choi lai.
6. La phu huynh, toi muon xem huong dan su dung ngan gon truoc khi bat dau.

## 4. Functional Requirements
- FR-01: Trang chu co ten ung dung, bat dau, chon ngon ngu, chon chu de.
- FR-02: Co man hinh huong dan phu huynh.
- FR-03: Moi luot choi gom 10 cau hoi.
- FR-04: Moi cau co 4 dap an, duy nhat 1 dap an dung.
- FR-05: Quy tac sinh cau hoi:
  - Theo dung chu de da chon.
  - Dap an sai cung nhom noi dung voi dap an dung.
  - Xao tron thu tu dap an.
  - Tranh lap lai cau hoi trong cung 1 luot.
- FR-06: Dung +1 diem, sai +0 diem.
- FR-07: Hien thi tien do (cau x/10), diem hien tai.
- FR-08: Co nut nghe lai cau hoi va bat/tat am thanh.
- FR-09: Ket thuc luot hien thi tong cau, dung, sai, diem, nhan xet, choi lai, doi chu de, ve trang chu.

## 5. Data Requirements
Moi doi tuong noi dung can mo ta theo schema logic:
- `id`: ma dinh danh
- `topic`: colors/shapes/letters/animals/numbers
- `subgroup`: vd `flat`/`solid` voi hinh hoc
- `vi`: ten tieng Viet
- `en`: ten tieng Anh
- `image` (optional path)
- `audio_vi` (optional path)
- `audio_en` (optional path)
- `difficulty`: easy/medium/hard

## 6. Non-Functional Requirements
- NFR-01: Toi uu thao tac cam ung, nut lon, de bam.
- NFR-02: Phan hoi giao dien sau thao tac < 1 giay (muc tieu).
- NFR-03: Hoat dong tren mobile/tablet/desktop trinh duyet pho bien.
- NFR-04: Khong thu thap du lieu ca nhan, khong dung camera/micro.
- NFR-05: Noi dung than thien voi tre, khong gay so hai.

## 7. Acceptance Criteria
- AC-01: Chon duoc ngon ngu va chu de, bat dau duoc luot choi.
- AC-02: Moi luot co dung 10 cau.
- AC-03: Moi cau co dung 4 lua chon va 1 dap an dung.
- AC-04: Trong 1 luot, cau hoi khong lap lai (neu du pool du lieu).
- AC-05: Dap an sai thuoc cung chu de/nhom voi dap an dung.
- AC-06: Diem tinh dung theo cong thuc dung=1, sai=0.
- AC-07: Hien thi ket qua va nhan xet theo bang diem 0-3, 4-6, 7-8, 9-10.
- AC-08: Co man hinh huong dan phu huynh.

## 8. Test Scenarios (BA/QA)
- Chon ngon ngu VI/EN.
- Chon duoc tung chu de.
- Moi luot 10 cau.
- Moi cau 4 dap an va 1 dap an dung.
- Khong lap cau hoi trong 1 luot.
- Dung thi cong diem, sai khong cong diem.
- Nut nghe lai va nut bat/tat am thanh hoat dong.
- Ket qua cuoi luot hien thi day du.

## 9. BA Conclusion
- Gate 1: PASS (updated theo prod-description.md)
