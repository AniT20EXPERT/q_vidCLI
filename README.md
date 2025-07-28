# 🎥 VidSage – Smart Video Transcoder & Analyzer

**VidSage** is a Python-powered tool that automates video transcoding, stream metadata extraction, and visual quality analysis. It simulates essential components of large-scale video streaming systems used in OTT, broadcast, and video delivery infrastructure.

Built with **FFmpeg** and **OpenCV**, VidSage helps engineers understand how resolution, encoding, and visual clarity interact — making it a useful pre-processing and QA tool in a modern video pipeline.

---

## 🚀 Key Features

- ✅ **Multi-resolution transcoding** (480p, 720p, 1080p) using FFmpeg
- ✅ **Stream metadata extraction** (codec, bitrate, resolution) via ffprobe
- ✅ **Visual blur detection** using Laplacian variance across sampled frames
- ✅ **Markdown report generation** with inline performance plots
- ✅ 📈 Reusable for both real-time diagnostics and offline video QA tasks

---

## 📸 Demo

![Blur Plot](output/blur_plot.png)

---

## 🛠 Tech Stack

- **Python 3**
- **FFmpeg** + **ffprobe** (for transcoding and metadata)
- **OpenCV** (for frame sampling and blur detection)
- **Matplotlib**, **Pandas** (for plotting and analysis)

---

## 🧱 Project Structure

```bash
vidsage/
├── input/             # Place original videos here
├── output/            # Output transcoded videos, plots, and reports
├── transcoder.py      # Handles FFmpeg transcoding
├── quality_metrics.py # Visual blurriness detection using OpenCV
├── utils.py           # Video metadata extractor (ffprobe)
├── analyzer.py        # Main orchestrator script
└── requirements.txt   # Python dependencies
````

---

## ⚙️ Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/vidsage.git
cd vidsage
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Input Video

Place your sample video inside the `input/` folder. Name it `sample.mp4` or adjust the path in `analyzer.py`.

### 4. Run the Analyzer

```bash
python analyzer.py
```

---

## 📂 Output

Once complete, the tool generates:

| File                           | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| `output/report.md`             | Markdown summary with codec info, bitrate, resolution, and blur score |
| `output/blur_plot.png`         | Frame-by-frame blur score visualization                               |
| `output/sample_720p.mp4`, etc. | Transcoded videos at various resolutions                              |

---

## 🎯 Use Case

> Due to growing demand for adaptive bitrate streaming and high-quality playback across devices, media systems must transcode, monitor, and analyze video files at scale. VidSage addresses this by automating key QA steps — saving manual analysis time, ensuring consistent delivery, and enabling intelligent debugging of video degradation across resolutions.

---




