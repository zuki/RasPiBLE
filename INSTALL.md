1. [pybleno](https://github.com/Adam-Langley/pybleno)のインストール

```bash
# 必要なパッケージのインストール
# [bleno](https://github.com/noble/bleno#prerequisites)による
$ sudo apt-get install bluetooth bluez libbluetooth-dev libudev-dev

# bluetoothd の停止
$ sudo systemctl stop bluetooth       # とりあえず今回だけ
# $ sudo systemctl disable bluetooth    # 起動時にも停止

# hci0のマニュアル起動
$ sudo hciconfig hci0 up

# pybleno のインストール
$ pip install pybleno
