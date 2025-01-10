# 気圧をランダム表示
## mypkg
- このリポジトリは授業で作成したROS2のパッケージです。

[![test](https://github.com/yuumin131/mypkg2/actions/workflows/test.yml/badge.svg)](https://github.com/yuumin131/mypkg2/actions/workflows/test.yml)
## ノードの概要
- このパッケージは気圧の値をランダムでパブリッシュする'pressure_publisher'というノードで構成されています。

- topic名は'pressure'です。
## 使用方法
以下のコマンドで実行します。  
```
$ ros2 run mypkg pressure_publisher
```
実行してもこちらでは何も表示されません。
もう一つの端末で以下のコマンドを入力します。
```
$ ros2 topic echo /pressure
```
出力結果は以下のとおりになります。
```
data: 966.8546142578125
---
data: 1010.7046508789062
---
data: 982.2379760742188
---
data: 1031.815185546875
---
data: 1024.4273681640625
---
```
### テスト用コード
- listener.py
## 開発環境
- os: ubuntu20.04 LTS
- ROS2 version: Foxy
## テスト環境
- **OS**：Ubuntu 22.04 LTS
- **ROS2 version**：humble
## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2024 Yuuma Sakurai
