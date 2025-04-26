# はじめに


# 内容

地図はfolium を使います。総務省のshpファイルで提供されるデータを読むには、
geopandas を利用してみる。

## foliumとgeopands のインストール

普通に入りました。

```
$ poetry add folium geojson
Creating virtualenv study-geoinfo-xjVUSkgE-py3.12 in /home/x/.cache/pypoetry/virtualenvs
Using version ^0.16.0 for folium
Using version ^3.1.0 for geojson

Updating dependencies
Resolving dependencies... (1.4s)

Package operations: 12 installs, 0 updates, 0 removals

  - Installing markupsafe (2.1.5)
  - Installing certifi (2024.6.2)
  - Installing charset-normalizer (3.3.2)
  - Installing idna (3.7)
  - Installing jinja2 (3.1.4)
  - Installing urllib3 (2.2.1)
  - Installing branca (0.7.2)
  - Installing numpy (1.26.4)
  - Installing requests (2.32.3)
  - Installing xyzservices (2024.6.0)
  - Installing folium (0.16.0)
  - Installing geojson (3.1.0)

Writing lock file
$ poetry add geopandas
Using version ^0.14.4 for geopandas

Updating dependencies
Resolving dependencies... (1.6s)

Package operations: 14 installs, 0 updates, 0 removals

  - Installing click (8.1.7)
  - Installing six (1.16.0)
  - Installing attrs (23.2.0)
  - Installing click-plugins (1.1.1)
  - Installing cligj (0.7.2)
  - Installing python-dateutil (2.9.0.post0)
  - Installing pytz (2024.1)
  - Installing tzdata (2024.1)
  - Installing fiona (1.9.6)
  - Installing packaging (24.1)
  - Installing pandas (2.2.2)
  - Installing pyproj (3.6.1)
  - Installing shapely (2.0.4)
  - Installing geopandas (0.14.4)

Writing lock file
```


## データを持ってくる

ページ開いて直接持ってきました。

https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A16-v2_3.html

ここでは福島県を選択し、A16-15_07_GML.zip を解凍すると、確かにshpファイルがありました。

```
A16-15_07_GML
├── A16-15_07.xml
├── A16-15_07_DID.dbf
├── A16-15_07_DID.geojson
├── A16-15_07_DID.shp
├── A16-15_07_DID.shx
└── KS-META-A16-15_07.xml

1 directory, 6 files
```

これを以下のようにして読めます。ここでは*.shpファイルだけでは意味を読み込めません。同じフォルダに shx ファイルがあると読み込めますが情報が少なそうでした。
Wikipediaの説明を参考にすると、必須ファイルというものがあるようなので、素直にダウンロードしたファイル群をそのまま配置しておくことにしました。(少なくとも*.geojson は独立していそうですが。)


