### Djangoda Elektron do`kon loyihasini yaratish
___
Ushbu loyiha foydalanuvchi va mehmonlarni tekshirish imkoniyatlariga ega to'liq ishlaydigan elektron tijorat veb-sayti bo'ladi. Biz birinchi ikkita modulda shablonlarimiz va ma'lumotlar tuzilmamizni o'rnatishdan boshlaymiz, so'ngra to'lov integratsiyasi bilan foydalanuvchi to'lov oqimini qo'shishga o'tamiz.

Tizimga kirgan foydalanuvchi bilan asosiy hisob-kitobni tugatganimizdan so'ng, foydalanuvchilarga cookie-fayllar yordamida mehmon sifatida chiqish imkoniyatini qo'shamiz.

![This is an image](https://stepswithcode.s3-us-west-2.amazonaws.com/introduction/1+the+product.png)

Foydalanuvchilar bir nechta mahsulotlarni savatga qo'shish imkoniyatiga ega bo'ladilar, ular jismoniydan tortib raqamli mahsulotlargacha.


![This is an image](https://stepswithcode.s3-us-west-2.amazonaws.com/introduction/3+checkout+page.png)

### Foydalanuvchi/mehmonni tekshirish
Ushbu elektron tijorat loyihasining asosiy yo'nalishi foydalanuvchi hisoblari bilan birga mehmonlarni tekshirish qobiliyatini birlashtirishga qaratilgan. Elektron tijorat bo'yicha ko'plab qo'llanmalar/demo dasturlarda u yoki boshqasi bor, lekin hozirda ikkalasini ham o'z ichiga olgan birontasini topa olmadim.


### Tasdiqlangan foydalanuvchi va mehmonlarni tekshirish
Tasdiqlangan foydalanuvchilar va mehmonlar deyarli bir xil jarayonga ega, ular biroz farq qiladi. Hisob qaydnomasi bo‘lgan foydalanuvchilar kutilayotgan va oldingi buyurtmalarni ko‘rish imkoniyatiga ega bo‘ladi, mehmonlar esa cookie-fayllarda saqlanadigan narsalarga ega bo‘ladi va muvaffaqiyatli xariddan so‘ng hisob yaratish imkoniyatiga ega bo‘ladi.

#### Autentifikatsiya qilingan foydalanuvchi jarayoni

    1.Buyumni savatga qo'shish → Buyurtmani tahrirlash → To'lov
    2.Kutilayotgan va oldingi buyurtmalar + Buyurtma tafsilotlarini ko'rish

#### Mehmonlarni tekshirish jarayoni

    1.Buyumni savatga qo'shish → Buyurtmani tahrirlash → To'lov
    2.Buyurtmani ko'rish uchun hisob yarating

### Loyiha tuzilishi
Loyihani yaratishni boshlashdan oldin, keling, ushbu loyihaning asosiy tuzilishini ko'rib chiqaylik. Men avval shablonlarni ko'rib chiqaman va ularning har biri nima bilan shug'ullanadi, so'ngra biz o'z modellarimiz va sahifamiz funksiyalarini ko'rib chiqamiz.

#### Shablonlar
Ushbu loyiha 3 ta asosiy shablonga, __store.html__, __cart.html__ va __checkout.html__ -ga ega.

![This is an image](https://stepswithcode.s3-us-west-2.amazonaws.com/introduction/5%2Btemplate%2Bdiagram.png)

#### Modellar
![This is an image](https://stepswithcode.s3.us-west-2.amazonaws.com/introduction/models.png)

Ushbu loyiha 6 ta modeldan iborat bo'ladi, shuning uchun keling, har birini ko'rib chiqamiz:

1. __USER__ - Django foydalanuvchi modelida o'rnatilgan, misol ro'yxatdan o'tgan har bir mijoz uchun yaratilgan.

2. __CUSTOMER__ - Foydalanuvchi modeli bilan bir qatorda, har bir mijoz har bir foydalanuvchi bilan birdan-bir munosabatga ega bo'lgan Mijoz modelini o'z ichiga oladi. (OneToOneFied)

3. __PRODUCT__ - Mahsulot modeli biz do'konda mavjud bo'lgan mahsulot turlarini ifodalaydi.

4. __ORDER__ - Buyurtma modeli joylashtirilgan yoki kutilayotgan tranzaksiyani ifodalaydi. Modelda tranzaksiya identifikatori, tugallangan ma'lumotlar va buyurtma holati kabi ma'lumotlar saqlanadi. Bu model bola yoki mijoz modeli bo'ladi, lekin buyurtma berish uchun ota-ona bo'ladi.

5. __ORDERITEM__ - Buyurtma ob'ekti buyurtma bilan bitta elementdir. Misol uchun, xarid qilish savati ko'p narsalardan iborat bo'lishi mumkin, ammo barchasi bitta buyurtmaning bir qismidir. Shuning uchun OrderItem modeli PRODUCT modeli VA ORDER modelining farzandi bo‘ladi.

6. __SHIPPING__ - har bir buyurtma uchun yuk ma'lumotlari kerak bo'lmaydi. Yuborilishi kerak bo'lgan jismoniy mahsulotlarni o'z ichiga olgan buyurtmalar uchun buyurtmani qaerga jo'natishni bilish uchun jo'natish modelining namunasini yaratishimiz kerak bo'ladi. Yuk tashish kerak bo'lganda oddiygina buyurtma modelining bolasi bo'ladi.
