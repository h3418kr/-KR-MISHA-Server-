# Rust 서버 홍보 페이지 v2 (svy04.github.io 벤치마크)

## 로컬 실행

```bat
cd C:\Users\INHA\.openclaw\workspace\rust_site_v2
python -m http.server 8788
```

브라우저에서 열기:
- http://127.0.0.1:8788/

## 상태 갱신

```bat
python C:\Users\INHA\.openclaw\workspace\rust_site_v2\update_status_json.py
```

페이지는 `status.json`을 1분마다 자동 갱신합니다.
