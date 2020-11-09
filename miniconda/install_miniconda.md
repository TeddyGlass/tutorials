# Miniconda
MinicondaとはPythonの環境構築を行うためのツール.  
プログラミングでは基本的に内部のシステムに干渉しない様に仮想環境にて作業を行う.  
Minicondaをインストールすることで仮想環境を構築し、そこで用いるPythonのバージョン、パッケージの指定・管理が可能になる.  
Jupyter notebookやMatplotlib, Numpy, Pandasをはじめとする機械学習ライブラリScikit-learnやPytorchももちろん使用することが可能になる.   
Minicondaはコマンドを用いたインターフェースであるが、Anacondaに比べて動作が軽く慣れれば使いやすい.  
そのため、この記事ではMinicondaによるPython環境構築手法について説明する. 
<br>
<br>

# Install
Minicondaのインストールは[ここ](https://docs.conda.io/en/latest/miniconda.html)で行う. WindowsであるならMiniconda3 Windows 64-bitをインストールすればok. MacOSでの使用法は割愛する.  インストーラーのチェック項目は基本的に全てデフォルトのものにチェックを入れればOK.  
<br>
<br>

# Anaconda-prompt
インストールが完了したらAnaconda-promptを立ち上げる. Windowsの場合cortanaにanacondaと入力すれば出てくるはず.  
anaconda promptを立ち上げたら画面の左側を見ると, (base)と書いてある. これはbaseの仮装環境にいることを意味している.  
```zsh
(base)$
```
ここに新たに環境を構築する.  

```zsh
(base)$ conda create -n test
```
注意書きが出てきた場合yと打ってEnterを押せばOK  

以上で仮想環境(test)の構築が完了  
testの仮想環境に入るためには
```zsh
(base)$ conda activate test
```
もしくは
```zsh
(base)$ activate test
```
と実行することでtest環境に入ることが可能test環境に入れたら、
```zsh
(test)$
```
となっているはず.  
ここにパッケージをインストールしていく.  
<br>
<br>

# conda install ~
test環境にjupyterをインストールしてみよう. jupyterとはJupyter notebookが使用できるツールである. jupyter notebookではコードの実行結果や図表をノートブック形式で保存しておくことが可能なのでインタラクティブでPython初心者にとっては非常に扱いやすい.  
著者もプログラムコードの開発段階ではまずjupyter notebookを用いてインタラクティブにプログラムを開発していく.  
```zsh
(test)$ conda install -c anaconda jupyter -y
```
を実行してみよう. これによってjupyterのインストールが完了する.  
なお、conda 環境にて ```pip install``` は厳禁である. 必ず```conda install```を用いよう.  
パッケージのインストール方法がわからなかった場合は[ここ](https://anaconda.org/)でインストールしたいパッケージ名を検索すればconda コマンドでインストールする方法が見つかるので利用するといい.  
<br>
次に、　　
```zsh
(test)$ jupyter notebook
```
 と実行すればブラウザを用いてjupyter notebookが起動する.

jupyternotebook画面の右上にNewというタブがあるはずである. ここからPython 3を選択すればPython3系のコードが実行可能なnotebookを編集できる.  
