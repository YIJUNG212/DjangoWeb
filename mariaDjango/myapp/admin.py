from django.contrib import admin
from .models import webUser ,product,shopcar,shopitem,shopsum

# Register your models here.

class ShopItemAdmin(admin.ModelAdmin):
    #以下是最後admin模式要顯示的欄位名稱
    list_display = ('item_id','item_name', 'item_price','item_quantity', 'item_sum','item_image_photo')
    #下面是要省略不顯示的欄位,但實際存在,也就是輸入時,不輸入,交由程式來處理
    exclude = ('item_sum',)

class ShopsumAdmin(admin.ModelAdmin):
    #以下是最後admin模式要顯示的欄位名稱
    list_display = ('sum_id','shop_Totalsum',)
   

admin.site.register(shopitem, ShopItemAdmin)
admin.site.register(webUser)
admin.site.register(product)
admin.site.register(shopcar)

admin.site.register(shopsum,ShopsumAdmin)
