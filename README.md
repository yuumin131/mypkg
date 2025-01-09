# 気圧をランダム表示
## mypkg
千葉工業大学 未来ロボティクス学科2024年度ロボットシステム学の課題2で使用します。
- ROS2のパッケージです。
- listenerはpresssure_publisherのテスト用です。

[![test](https://github.com/yuumin131/mypkg2/actions/workflows/test.yml/badge.svg)](https://github.com/yuumin131/mypkg2/actions/workflows/test.yml)
## 環境
- ubuntu20.04 LTS
- ROS2 Foxy
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
$ rostopic echo /pressure
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
## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2024 Yuuma Sakurai
