import pandas as pd
import matplotlib.pyplot as plt

# Netflix verilerini yükle
netflix_data = pd.read_csv("netflix_titles.csv")

# Veri ön işleme
# İzleme verisi içeren sütunları al
watch_data = netflix_data[['type', 'title', 'rating', 'listed_in', 'release_year', 'duration']]

# Film ve Dizilerin sayısını hesapla
film_sayisi = len(watch_data[watch_data["type"]=="Movie"])
dizi_sayisi = len(watch_data[watch_data["type"]=="TV Show"])

print("Film sayısı:", film_sayisi)
print("Dizi sayısı:", dizi_sayisi)

# Film ve Dizilerin yayın yılına göre dağılımını görselleştir
plt.hist(watch_data[watch_data["type"]=="Movie"].release_year, alpha=0.5, label="Film")
plt.hist(watch_data[watch_data["type"]=="TV Show"].release_year, alpha=0.5, label="Dizi")
plt.legend()
plt.show()

# En yüksek bütçeli filmleri analiz et
highest_budget_movies = watch_data[watch_data["type"]=="Movie"].sort_values("budget", ascending=False).head(10)
print(highest_budget_movies[["title", "budget"]])

# En yüksek gelirli filmleri analiz et
highest_gross_movies = watch_data[watch_data["type"]=="Movie"].sort_values("gross", ascending=False).head(10)
print(highest_gross_movies[["title", "gross"]])

# Yapımcıların ve senaristlerin dağılımını analiz et
producers_data = watch_data["listed_in"].str.split(",", expand=True)
producers_data = pd.melt(producers_data)
producers_data = producers_data.dropna()
producers_data = producers_data.groupby("value").size().reset_index(name="count").sort_values("count", ascending=False).head(10)
print(producers_data)

# Dizilerin sezon sayısına göre dağılımını analiz et
tv_show_seasons = watch_data[watch_data["type"]=="TV Show"].duration.str.extract("(\d+)").astype("float")
tv_show_seasons = tv_show_seasons.dropna()
tv_show_seasons.hist()
plt.show()

# Kullanıcıların Netflix içeriklerine verdikleri puanların dağılımını analiz et
rating_data = watch_data["rating"].value_counts().reset_index()
plt.bar(rating_data["index"], rating_data["rating"])
plt.show()
