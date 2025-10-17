# F1 Video Sync

Sync Formula 1 Bahrain GP 2025 video with live telemetry using OpenF1 API.

## Setup

1. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Run backend:
```bash
python app.py
```

3. Place `Bahrain_GP_2025.mp4` in `frontend/` directory.

4. Open `frontend/index.html` in a browser.

## Helper Script

Detect lights out automatically:
```bash
python utils/sync_helper.py
```

## License

MIT License
