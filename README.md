# Customer Reviews Analysis and Topic Clustering

## 1. Overview
Celem projektu jest analiza opinii klientów w celu zidentyfikowania głównych tematów i sentymentu opinii. Projekt używa NLP, embeddingów i klasteryzacji, a wyniki wizualizuje w formie wykresów i wordcloudów.

## 2. Dataset
- Źródło: Amazon Reviews / IMDB Reviews
- Liczba opinii: np. 50k
- Zawartość: tekst, ocena, produktID, data

[Amazon Fine Food Reviews on Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)

Please download the CSV file and place it in the `data/raw/` directory. 

## 3. Workflow
1. Preprocessing tekstu
2. Analiza sentymentu
3. Klasteryzacja opinii
4. Wizualizacja klastrów + top frazy

## 4. Results
- TSNE / UMAP wykresy klastrów
- Wordcloud dla każdego klastra
- Insight: np. większość negatywnych opinii dotyczy dostawy

## 5. How to run
- `pip install -r requirements.txt`
- `python src/preprocessing.py`
- `python src/clustering.py`
- `streamlit run app.py` (jeśli dashboard)

## 6. Insights / Discussion
- Co widać w danych
- Jakie tematy dominują
- Rekomendacje / obserwacje

## 7. Future Work
- Dodanie dynamicznego API (Yelp / Amazon)
- Analiza trendów w czasie
- Dashboard z interaktywnym filtrowaniem
