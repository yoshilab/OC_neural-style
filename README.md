# Neural-style on flask
HTTPリクエストで絵のスタイルと画像を指定すると画像を指定したスタイルに変換するぞ!

## 仕様
1. なんか知らんけど，Mac版SafariとFirefoxで結果の動的表示ができんかったき，WindowsのFirefoxなら動くことを確認できたき，研究室のVAIOでも使ってみて

## 使い方
1. このリポジトリをクローンするぞ！  
   `git clone https://github.com/yoshilab/OC_GAN_neural-style.git`  
   
2. ディレクトリを移動だ!  
   `cd OC_GAN_neural-style`  
   
3. Dockerでイメージを作るぞ!  
   `docker build ./ -t neural-style`  
   
4. ディレクトリをマウントしながら，ポートフォワーディングしながらコンテナを起動するぞ!   
   `docker run -it --rm -v $(pwd):/app -p 5000:5000 neural-style`  
   
5. これで多分サーバが立ち上がるから試してみるぞ!  
   ブラウザから以下のURLにアクセス!!  
   同じPCからのアクセス `http://localhost:5000`  
   違うPCからのアクセス `http://(サーバのIPアドレス):5000`  
   
6. 上の手順でできなかったら頑張って動かしてくれ!! 
   
## 参考文献・プログラム  
1. GANのプログラム https://github.com/anishathalye/neural-style  
2. 1.の理解を助けてくれそうな日本語ページ https://elix-tech.github.io/ja/2016/08/22/art.html  
