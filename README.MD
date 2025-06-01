
### Predicting Stock Price Movement from Financial News Sentiment - Task 1

## Task 1: Modularization & Exploratory Data Analysis (EDA)

This task focuses on modularizing the project structure and performing initial exploratory data analysis (EDA) on financial news headlines. We also implemented basic sentiment analysis to prepare for downstream predictive modeling.

---

## Project Structure

```

├── src/
│   ├── data\_loader.py         # Loads and prepares datasets
│   ├── eda.py                 # EDA functions (headline stats, publishers, daily volume)
│   ├── sentiment.py           # Basic sentiment analysis using TextBlob
│   ├── time\_analysis.py       # (Placeholder) Time-based stock/news insights
│   ├── utils.py               # Helper utilities
│
├── scripts/
│   ├── run\_task1.py           # Main script to run EDA & sentiment workflow
│   └── init.py                # (Optional) Initialization script
│
├── tests/
│   └── test\_sentiment.py      # Unit tests for sentiment analysis
│
├── data/
│   └── raw\_analyst\_ratings.csv (ignored via `.gitignore`)
│   └── fnspid\_cleaned.csv     (ignored via `.gitignore`)
│
├── .github/
│   └── workflows/unittests.yml  # CI pipeline to run tests
│
├── requirements.txt
├── .gitignore
└── README.md

````

---

## ✅ What Was Done

### ✔ Modularization

- Split large monolithic scripts into maintainable modules under `src/`.
- Followed clean coding practices and file separation by functionality.

### ✔ EDA on Financial Headlines

- Calculated headline length statistics.
- Visualized top publishers.
- Analyzed daily article volume over time.

### ✔ Sentiment Analysis

- Applied `TextBlob` for polarity scoring on news headlines.
- Added `sentiment_score` to the dataset for each headline.

---

## ▶️ How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
````

2. **Run task script**:

   ```bash
   python scripts/run_task1.py
   ```

---

## 📦 Requirements

* Python 3.10+
* `pandas`, `matplotlib`, `seaborn`, `textblob`

---

## 🛑 Notes

* Large datasets in `data/` are excluded via `.gitignore` and **not tracked** by Git.
* Ensure `data/raw_analyst_ratings.csv` is available locally to run the script.
* The repository uses GitHub Actions for automated testing (`.github/workflows/unittests.yml`).

---

## 📌 Next Steps (Task 2+)

* Time series alignment of headlines and stock prices.
* Building predictive models using sentiment + time features.
* Model evaluation and backtesting.

---

## Contributors

* **Rahel Sileshi** (Initial modularization and EDA)

---

## 📄 License

MIT License

