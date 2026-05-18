# Hoc-cung-con

Ung dung web nho ho tro tre 2-4 tuoi hoc mau sac, hinh hoc, chu cai, con vat va con so.

## Run local

```bash
cd Hoc-cung-con
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```

## Features (MVP)
- Chon ngon ngu: Tieng Viet / English
- Chon chu de: mau sac, hinh hoc, chu cai, con vat, con so
- Moi luot 10 cau, moi cau 4 dap an
- Cham diem va tong ket ket qua
- Nut bat/tat am thanh + doc lai cau hoi (trinh duyet ho tro Web Speech)

## Deployment
- Streamlit config: `.streamlit/config.toml`
- Render config: `render.yaml`
- Start command:
  - `streamlit run src/app.py --server.port $PORT --server.address 0.0.0.0`
