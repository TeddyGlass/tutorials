# サンプルコード使用方法
1. ```sdf2mord.py```をダウンロードする  
コマンドラインからダウンロードする場合は以下のコマンドを実行する.  
```
wget https://raw.githubusercontent.com/TeddyGlass/tutorials/main/sample_code/mordred/sdf2mord.py
```

2. サンプルデータをダウンロードする  
 :exclamation:  手持ちのsdfファイルに対して記述子計算を行う場合は```sdf2mord.py```のみダウンロードすればOKです.  
 ```
wget https://raw.githubusercontent.com/TeddyGlass/tutorials/main/sample_code/mordred/rdkit_solubility.sdf
```

3. ```sdf2mord.py```と記述子を計算したい化合物が含まれたsdfファイル (サンプルコードを実行する場合はrdkit_solubility.sdf) を同じディレクトリに配置する  

4. ターミナルを開いて```sdf2mord.py```とsdfファイルが配置されているディレクトリに移動し, 以下のコマンドを実行する.  
```
python sdf2mord.py rdkit_solubility.sdf --ignore_3D
```
**コマンドライン引数の解説**  
 * 第1引数: 記述子を算出したい化合物のsdfファイル名  
 * オプション: ```---ignore_3D```を付けることで, 三次元記述子の計算を無視する  