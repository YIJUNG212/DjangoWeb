# DjangoWeb
Django網站，基本圖形上傳，資料庫CRUD及youtube網站mp3、mp4轉檔功能
※基本功能說明

1.可以藉由繼承django內部模組abstractUser來擴充原有的User模組的欄位 並且藉由authenticate來判斷使用者登錄情況，藉以區別不同帳號登入情況及登入後執行權限 <br>

2.已實作可以透過upload及settings.py相關MEDIA_ROOT等設定,完成開發模式中的圖檔上傳及讀取<br>

並藉由django第三方套件whitenoise完成product模式下的靜態資料static獲取<br>

3.資料表shopcar及shopitem shopsum等之間有關聯式,藉由fk鍵及pk鍵的關聯，一旦shopcar刪除，相應的shopitem及shopsum也會刪除<br>

4.透過Bootstrap運用，簡單套用既有的模板，讓畫面順眼<br>

5.使用JAVASCRIPT 客製化按鈕，使按鈕動作後會提示，並藉由不同操作得到不同效果，如確認送出或取消。<br>

6.購物車商品欄已可判斷有無重複商品,有重複就執行update指令,沒重複就執行insert into指令，商品欄新增同時,資料表shopsum也會新增現有所有商品總和<br>
7.利用pytube簡單實作了youtube的mp3、mp4轉檔功能,下載資源不受限<br>
