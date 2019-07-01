# RasPiとiPod TouchをBLEでつないでLチカ

ソースは[Bluetoothを使って自作iPhoneアプリとRaspberry piでLEDチカらせる](https://qiita.com/kentarohorie/items/b9549af9c71886860866)による。だだし、nodeモジュールのblenoの代わりにpyblenoを使用してpythonで実装。

## 操作方法

### RasPi側

1. ペリフェラルを立ち上げる

  ```
  $ cd /home/pi/examples/ble
  $ sudo ./peripheral.py
  ```

### iPos側

1. 「設定」アプリでBluetoothを有効化
2. `RasPiBLE` アプリを立ち上げる
3. [接続する] ボタンを押してmqtt-clientに接続
4. スイッチのオンオフでLEDがオン・オフするはず
5. [切断する] ボタンを押して切断
