# Image Processing for Basic Depth Completion (IP-Basic)
In Defense of Classical Image Processing: Fast Depth Completion on the CPU    
                                                                                         تشخیص عمق در تصاویر با استفاده از مفاهیم کلاسیک پردازش تصویر      
##
- Paper : [arXiv page](https://arxiv.org/abs/1802.00036)
- Main repository : [Github](https://github.com/kujason/ip_basic)
- Presentation File : [Powerpoint](https://github.com/sabadijou/FastDepthCompletionCPU/blob/master/ReadMe/Presentation.pptx)
- Presentation File : [PDF](https://github.com/sabadijou/FastDepthCompletionCPU/blob/master/ReadMe/Presentation.pdf)
##
![Final Output](https://github.com/sabadijou/FastDepthCompletionCPU/blob/master/ReadMe/all_results.png)
##
محیط فیزیکی اطراف ما، یک محیط سه‌بُعدی است، محیطی که هر جسم موجود در آن، دارای طول، عرض و ارتفاع (عمق) می باشد. زمانی که به این محیط نگاه می کنیم و یا توسط دوربین های معمولی از آن عکس می گیریم، یک محیط سه بُعدی بر روی یک صفحه دوبُعدی نگاشت می شود. این کار باعث از دست دادن بُعد سوم یا همان عمق می شود. این بُعد حاوی اطلاعات بسیار مهمی جهت تحلیل و بررسی موقعیت و ویژگی های اشیاء موجود در تصویر می باشد. انسان با استفاده از تکنیک‌های سه‌بُعدی ساز مغز و داشتن قابلیت دید دو چشمی ، محیط را به شکل سه‌بُعدی درک می‌کند اما زمانی که از محیط عکس می گیریم باید سعی کنیم در کامپیوتر، بُعد سوم صحنه را توسط تکنیک های موجود بازیابی کنیم. تشخیص عمق تصویر، مسئله ای بسیار مهم و اساسی در بحث بینائی ماشین و هوش مصنوعی می باشد که هنوز راه حل قطعی برای آن پیدا نشده است. هدف این مقاله، بدست آوردن عمق یک صحنه با توجه داده‌های لیدار تنک عمق از طریق روش‌های سنتی پردازش تصویر می باشد.
 در این مقاله بدون استفاده از الگوریتم های یادگیری عمیق و تنها با استفاده از تکنیک های سنتی پردازش تصویر به ارائه یک الگوریتم تکمیل عمق که از زیرشاخه های روش تشخیص عمق می باشد از روی داده های تنک عمق می‌پردازد. این الگوریتم نتایج بسیار رقابتی در مقایسه با الگوریتم های یادگیری عمیق ارائه داده است، و در زمان ارائه رتبه اول بنچمارک KITTI به این الگوریتم تعلق می‌گیرد. و همچنین این الگوریتم با مقدار ۱۲۸۸ میلیمتر  در شاخص RMSE جز بهترین ها بوده است. اما پس از آن مدل های جدیدتری همانند PENet  (RMSE = 730.8 mm)توانسته‌اند از این روش عملکرد بهتری را نشان دهند.
 #
 در این پیاده سازی یک الگوریتم حریصانه ارائه شده است که در هشت گام اصلی از نقشه های تنک عمق ، عمق تصاویر طبیعی را بدست می آورد. در گام اول این الگوریتم ابتدا مقادیر نقشه های تنک بین عدد 0 تا 100 قرار می گیرند سپس در گام دوم با یک فیلتر مخصوص عملیات Dilation روی نقشه صورت می پذیرد تا پیکسل با مقدار صفر با مقدار نزدیک ترین پیکسل برابر گردد بعد از آن در گام سوم با استفاده از یک کرنل طراحی شده توسط نویسندگان مقاله عمل closing انجام خواهد شد این عمل منجر به بهبود لبه اشیا تصویر خواهد شد در گام بعدی مشابه گام قبل یک کرنل بزرگ تر closing به تصویر اعمال می شود تا حفره هایی با سایز medium را در تصویر بپوشاند. در گام پنجم با استفاده از مکانیزم گسترش مقدار مرتفع ترین پیکسل ها تا انتهای تصویر گسترش پیدا می کند در گام ششم با استفاده از یک فیلتر بزرگ تمامی پیکسل های تهی مقداردهی خواهند شد و نهایتا در گام هفتم یک فیلتر گوسی، میانه یا هردو به تصویر اعمال میشوند تا سطوح بدست آمده عمق هموارتر شوند و سپس در گام انتهایی مقادیر حاصل به مقادیر اصلی عمق در فاصله مشخص تبدیل خواهند شد.  
 #
 [دانلود گزارش مقاله Image Processing for Basic Depth Completion ](https://github.com/sabadijou/FastDepthCompletionCPU/blob/master/ReadMe/Report.pdf) 
# Setup
- Clone the repository with following command :
```
git clone https://github.com/sabadijou/FastDepthCompletionCPU.git
```
- Download dataset from below :
```
http://www.cvlibs.net/download.php?file=data_depth_selection.zip
```
- Extract downloaded file and copy contents of "Kitti\depth\depth_selection\val_selection_cropped " directory to the "dataset\kitti_validation_cropped"
- Run main.py

