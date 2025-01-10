# 気圧をランダム表示
## mypkg
- このリポジトリは授業で作成したROS2のパッケージです。

[![test](https://github.com/yuumin131/mypkg2/actions/workflows/test.yml/badge.svg)](https://github.com/yuumin131/mypkg2/actions/workflows/test.yml)
## ノードの概要
- このパッケージは千葉の現在の気圧をパブリッシュする'pressure_publisher'というノードで構成されています。
- topic名は'chiba_pressure'です。
- このノードでは気象庁のデータを使用しています。
## 依存関係
このパッケージを動かすために必要です。
```
$ sudo apt install python3-pip
```
```
$ pip3 install beautifulsoup4
``` 
## 使用方法
以下のコマンドで実行します。  
```
$ ros2 run mypkg pressure_publisher
```
実行してもこちらでは何も表示されません。
もう一つの端末で以下のコマンドを入力します。
```
$ ros2 topic echo /chiba_pressure
```
出力結果は以下のとおりになります。
```
data: 千葉の気圧は1019.0
---
data: 千葉の気圧は1019.0
---
data: 千葉の気圧は1019.0
---
data: 千葉の気圧は1019.0
---
data: 千葉の気圧は1019.0
---
```
### テスト用コード
- listener.py
## 開発環境
- **OS** : ubuntu20.04 LTS
- **ROS2** : version: Foxy
## テスト環境(GitHub Actions)
- **OS**：Ubuntu 22.04 LTS
- **ROS2 version**：humble
## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2025 Yuuma Sakurai

