# Japan-municipality-adjacency-matrix
This repository contains an R script to create an adjacency matrix for all municipalities(cities, towns, villages) in Japan based on geographical proximity. The matrix may be helpful to your spatial analysis.

## 📂 Data
You can download latest GIS data from the official site: 🔗https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html

##❓ why .geojson rather than .shp?
- Japan's MLIT commonly provides boundary data, road networks, and public facility locations in this format as an open standard format.

## 🚀 How to Use
Change the source name.

## 🛠 Data Preprocessing
If you need to generate an adjacency matrix for municipalities, some preprocessing may be required:
- **Merging administrative districts**
  - You may find multiple districts within a city, such as `"千葉市花見川区"` and `"千葉市中央区"`.These should be combined into a MultiPolygon representation of the entire city.
- **Filtering out irrelevant data**
  - Some entries in the dataset may not be relevant to your analysis, such as `"名古屋港口埋立地"` or `"中央防波堤外側廃棄物処理場（中潮橋南側）"`.
- **Other adjustments**

## 🏙️ Something you should know about Japan municipalities
In reality, you may find that some towns or villages are administratively part of certain cities. However, rest assured that in this dataset, each municipality is treated as an independent unit, so you can analyze them without concerns.





