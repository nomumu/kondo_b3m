# kondo_b3m
B3MでわかるROS CONTROL～こそこそ団のすごくうすいほん5～ でROS ControlのHowTo記事を紹介するために作成されたROSパッケージです。
kondo_b3m_controlの動作を説明するための周辺パッケージです。  

## 動作環境
このパッケージは次の環境で動作確認を行っています。
- OS
  - Ubuntu 20.04 LTS
- ROS
  - Noetic

## 環境構築
### パッケージをmakeする
適当なcatkinワークスペースにソースコードを取得し、catkin_makeを実行して下さい。操作例を示します。  
```
~$ mkdir -p kondo_ws/src
~$ cd kondo_ws/src
~/kondo_ws/src$ catkin_init_workspace
~/kondo_ws/src$ git clone --recursive https://github.com/nomumu/kondo_b3m.git
~/kondo_ws/src$ rosdep install -r -y --from-paths --ignore-src kondo_b3m
~/kondo_ws/src$ cd ..
~/kondo_ws$ catkin_make
~/kondo_ws$ source devel/setup.bash
```

### 通信設定
kondo_b3m_controlのREADMEに従ってください。

## このパッケージでできること
### Gazeboを実行する
次のコマンドでGazebo環境を呼び出すことができます。  
```
$ roslaunch kondo_b3m_gazebo b3m_gazebo.launch
```

### ROS Controlパッケージでサーボと接続する
次のコマンドでサーボの動作をrvizで描画できます。  
launch時にサーボトルクがON、終了時にトルクOFFになります。  
```
$ roslaunch kondo_b3m_control pos_control.launch use_rviz:=true
```

### サーボへ回転命令を発行するサンプル
次のコマンドでサーボを+90から-90の範囲で回転させるサンプルを実行できます。  
上記どちらかのlaunchを呼び出した状態で実行して下さい。  
```
$ rosrun kondo_b3m_examples traj_example.py
```
