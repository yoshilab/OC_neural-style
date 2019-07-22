# OC_neural-style

カメラで写真を連続撮影し，指定のスタイルに画像を変換するWebアプリです．[元となるプログラム](https://github.com/lengstrom/fast-style-transfer)

## 留意事項

Tensor, DGXでの動作は確認しましたが，その他の演算マシンでの動作は確認してません．

Webページの閲覧がOSやブラウザのバージョンによってはうまく実行できない場合があります．
一応，研究室のVAIOのFirefoxでは動作しましたが，iMacのSafari,Firefoxでは動作しなかったので注意！

##使い方

1. Web&アプリケーションサーバとなるPC上でイメージを作るために`docker build ./ -t fast-ns`を実行．
2. イメージをコンテナとして動かすために`nvidia-docker run --rm -e NVIDIA_VISIBLE_DEVICES=’0 -p 5000:5000 -v $(pwd):/app fast-ns`を実行．
3. 閲覧用PCのブラウザから`(サーバPCのIPアドレス):5000`にアクセス．
imagesファルダのstyleに元となる画像があるので結果と見比べて見てください．
