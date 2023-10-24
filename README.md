# PTT 圖片爬蟲

## 下載相依套件
```bash
pip install -r requirement.txt
```

## 如何使用
```
python main.py -h

usage: main.py [-h] [--board BOARD] [--pages PAGES]

optional arguments:
  -h, --help            show this help message and exit
  --board BOARD, -b BOARD   選擇 PTT 看板 e.g. Food
  --pages PAGES, -p PAGES   設定頁數上限，預設為全部
```

爬取 PTT 美食版所有圖片
```
python main.py --board Food
```

## 建置 docker & 執行
```
docker build -t my-python-app .

docker run -it --rm -v /where/you/want/to/save:/usr/src/app/img --name my-running-app my-python-app --board Food
```

