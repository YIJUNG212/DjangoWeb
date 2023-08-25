from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.
class webUser(AbstractUser):
    phone = models.CharField(max_length=50,null=True,blank=False)
    addr = models.CharField(max_length=255,null=True,blank=False)
    hobit = models.CharField(max_length=255,null=True,blank=False)
    join_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.username}"

class shopcar(models.Model):
    carid =models.OneToOneField(webUser,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.carid}"



# from imagekit.models import ImageSpecField
#要設定一個轉權限的函式,這樣才能避免上傳的圖片都是644權限,導致gunicorn及nginx讀不到檔案
#但是原本相應的upload_to裡的路徑也要改
def update_image_permissions(instance, filename):
    # 生成新的文件路径
    path = "item_photos/" + filename
    return path

class product(models.Model):
    productid =models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=50,null=True,blank=True)
    item_description=models.CharField(max_length=255,null=True,blank=True)
    item_price=models.IntegerField(null=True,blank=True,default=0)
    # item_photo_image = models.ImageField(upload_to=update_image_permissions)
    item_photo_image=models.ImageField(upload_to="item_photos")  

    def __str__(self):
        return str(self.item_name)
    
class shopsum(models.Model):
    sum_id=models.OneToOneField(shopcar,on_delete=models.CASCADE)
    shop_Totalsum = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return f"{self.shop_Totalsum}"

from django.db.models import Sum
class shopitem(models.Model):
    #首先一台車可以有多個商品,所以用ForeignKey來對應
    item_id = models.ForeignKey(shopcar,on_delete=models.CASCADE)
    #但是一個商品只能對應同應商品目錄,所以這裡應該可以改成一對一的
    item_name = models.CharField(max_length=50,null=True,blank=True)
    #下面設定本地端應有的資料欄位
    #數量不得為空值,預設為1
    item_quantity=models.IntegerField(null=False,default=1)

    item_price = models.IntegerField(null=True,blank=True,default=0)
    #路徑一樣要設定,只是需要設定blank=True,就可以不用再上傳圖檔,而是至upload_to指定路徑去撈圖
    

    item_sum = models.IntegerField(  null=True,blank=True,)
    @property
    def item_image_photo(self):
        try:
            product_instance = product.objects.get(item_name=self.item_name)
            return product_instance.item_photo_image.url if product_instance.item_photo_image else ''
        except product.DoesNotExist:
            return ''  # 如果没有关联的product，返回空字符串或其他默认值


    def __str__(self):
        return str(self.item_name)

    def save(self, *args, **kwargs):
        if self.item_name:
            item_price = self.item_name.item_price
            self.item_sum = item_price * self.item_quantity
        super().save(*args, **kwargs)
        
        # 更新shopsum表中的shop_Totalsum字段
        carid = self.item_id.carid_id
        current_item_sum = shopitem.objects.filter(item_id_id=carid)
        addsum = current_item_sum.aggregate(total_sum=models.Sum('item_sum'))['total_sum'] or 0
        shop_sum, _ = shopsum.objects.get_or_create(sum_id_id=carid)
        shop_sum.shop_Totalsum = addsum
        shop_sum.save()
       
        
      

    def create_from_product(self, item_name):
        prod = product.objects.get(item_name=item_name)
        
        self.item_name = prod
        self.item_quantity = 1
     
        self.save()

 
    
    




