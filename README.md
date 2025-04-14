# 🎵 Spotify Energy Explorer

A data-driven web app built using [Preswald](https://preswald.com) that explores the top Spotify tracks from 2010 to 2019 based on their energy levels and other musical features.

## 📌 About the Project

This app lets users:

- View top tracks from 2010–2019 with high energy scores.
- Dynamically filter data based on the `energy (nrgy)` threshold using a slider.
- Explore the dataset in table form.
- View visualizations such as scatter plots comparing features like `bpm`, `nrgy`, and `popularity`.
- Interact with a modern UI using the Preswald SDK.

---

## 🗂 Dataset

**Source:** [Kaggle - Top Spotify Songs 2010–2019](https://www.kaggle.com/datasets/ajaypalsinghlo/world-top-spotify-songs-2010-2019)  
**Columns:**

```text
['column00', 'title', 'artist', 'top genre', 'year', 'bpm', 'nrgy', 'dnce', 
 'dB', 'live', 'val', 'dur', 'acous', 'spch', 'pop']
```

---

## 🚀 Features

- 📊 **Interactive Table View**  
  View and filter songs with energy levels above a dynamic threshold.

- 📈 **Visualizations**  
  Plot energy vs. popularity using `plotly` for interactive data insights.

- 🧮 **SQL-like Filtering**  
  Perform custom SQL-style queries using `preswald.query`.

- 🎛️ **User Controls**  
  Threshold slider to filter high-energy tracks.

- 🎨 **Custom Branding**  
  Customized sidebar, favicon, color scheme, and logo.

---

## 🖥️ Tech Stack

- **Preswald** — Python-based no-code/low-code data app framework
- **Plotly** — For rich, interactive visualizations

---



## 📂 Folder Structure

```bash
.
├── data/
│   └── top_songs.csv
├── hello.py
├── preswald.toml
└── README.md
```

---

## 🔗 Deployment

1. Go to [Preswald App](https://app.preswald.com)
2. Click **Publish** → Get shareable public link
3. If failed, push the project to a GitHub repo and share the repo link instead.

---

## 🌟 Bonus

- Contributed ⭐ to [Preswald GitHub](https://github.com/StructuredLabs/preswald)
- Explored Preswald's widget SDK
- Customized topbar, sidebar, favicon, and color themes


