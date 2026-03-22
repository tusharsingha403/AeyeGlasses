#  AeyeGlasses

> **See the World. Understand It Instantly.**

AeyeGlasses is a smart glasses software that brings real-time object recognition and instant information search to your fingertips — literally. Point at any object, draw a circle around it, and get instant details — no screen touching required.

---

##  Features

-  **Gesture-Based Search** — Point your finger at any object and draw a circle around it to trigger a search
-  **Floating Info Window** — Instantly displays details and links about the detected object
-  **Hand Motion Controls** — Use hand gestures to hide the window or recall the last searched result
-  **API Usage Monitoring** — Smart SQLite-based tracking to manage and limit API usage efficiently
-  **Real-Time Performance** — Live camera feed with smooth hand and finger tracking

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Camera Access | OpenCV |
| Hand & Finger Tracking | MediaPipe |
| Drawing Interface | Canvas |
| Image Search | Real-Time Lens Data API (OpenWeb Ninja) |
| Usage Monitoring | SQLite |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |

---

##  Project Structure

```
AeyeGlasses/
├── data/         # Database and data files
├── src/          # Source code
│   └── main.py   # FastAPI backend entry point
├── .gitignore
└── README.md
```

---

##  Getting Started

### Prerequisites

- Python 3.9 – 3.11 (recommended)
- A webcam
- API key from [OpenWeb Ninja](https://rapidapi.com/openwebninja/api/real-time-lens-data)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/tusharsingha403/AeyeGlasses.git
cd AeyeGlasses
```

**2. Create and activate a virtual environment**
```bash
python -m venv myenv
myenv\Scripts\activate       # Windows
source myenv/bin/activate    # Mac/Linux
```

**3. Install dependencies**
```bash
pip install fastapi uvicorn mediapipe opencv-python python-dotenv requests numpy
```

**4. Set up your environment variables**

Create a `.env` file in the root directory:
```
db_path=Database path
x-api-key=your_openwebninja_api_key_here
git_token=Github api key
repo=path of a helper repositories
```

**5. Run the server**
```bash
uvicorn src.main:app --reload
```

**6. Open the app**

Go to `http://127.0.0.1:8000` in your browser.

---

##  How to Use

1. Allow camera access when prompted
2. Point your **index finger** at any object
3. Draw a **circle** around the object in the air
4. A **floating window** will appear with details and links about the object
5. Use a **hand gesture** to hide the window
6. Use another gesture to show the **last searched result**

---

##  Notes

- Make sure your `.env` file is never pushed to GitHub (already handled in `.gitignore`)
- API usage is limited on the free tier — the app monitors and limits calls automatically via SQLite
- Best experienced with good lighting for accurate hand tracking

---

##  About the Developer

Built by **Tushar** — BCA Student & Aspiring AI Engineer

*With a little help from friends — For frontend* 

---

##  License

This project is open source and available under the [MIT License](LICENSE). 