
# CRM-CLTV-Prediction

## Project Summary

This project aims to determine a roadmap for FLO's sales and marketing activities. To enable the company to make medium to long-term plans, it is necessary to predict the potential value that existing customers will bring to the company in the future.

The dataset consists of information derived from the past shopping behavior of customers who made their last purchases at FLO in 2020-2021 as OmniChannel customers (both online and offline).

Some variables in the dataset include:

- `master_id`: Unique customer number
- `order_channel`: The channel used for the purchase (Android, iOS, Desktop, Mobile)
- `last_order_channel`: The channel used for the last purchase
- `first_order_date`: The date of the customer's first purchase
- `last_order_date`: The date of the customer's last purchase
- `last_order_date_online`: The date of the customer's last online purchase
- `last_order_date_offline`: The date of the customer's last offline purchase
- `order_num_total_ever_online`: The total number of purchases made by the customer online
- `order_num_total_ever_offline`: The total number of purchases made by the customer offline
- `customer_value_total_ever_offline`: The total amount paid by the customer for offline purchases
- `customer_value_total_ever_online`: The total amount paid by the customer for online purchases
- `interested_in_categories_12`: The list of categories in which the customer made purchases in the last 12 months
- `store_type`: Represents 3 different companies. If a person made a purchase from Company A and also from Company B, it is written as "A, B".

This project aims to predict customer lifetime value using the existing customer data. These predictions will help optimize FLO's marketing strategies and increase customer loyalty.

## Installation

1. Clone this project: `git clone https://github.com/USERNAME/CRM-CLTV-Prediction.git`
2. Navigate to the project directory: `cd CRM-CLTV-Prediction`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the project: `python main.py`

## Usage

1. Add the dataset to the `data` folder.
2. Run the project files.
3. Analyze the results and evaluate the predictions.

## Contributions

Contributions are welcome. To contribute to the project, follow these steps:

1. Fork this repository.
2. Create your own branch: `git checkout -b feature/NewFeature`
3. Make your changes and commit them: `git commit -am 'Added a new feature'`
4. Push to your branch: `git push origin feature/NewFeature`
5. Create a pull request.

## License

This project is licensed under the MIT License. Refer to the `LICENSE` file for more information.
------------------------------------------------------------------

# CRM-CLTV-Prediction
BG-NBD ve Gamma-Gamma ile CLTV Tahmini

## Proje Özeti

Bu proje, FLO'nun satış ve pazarlama faaliyetleri için yol haritası belirlemeyi hedeflemektedir. Şirketin orta ve uzun vadeli planlar yapabilmesi için mevcut müşterilerin gelecekte şirkete sağlayacakları potansiyel değerin tahmin edilmesi gerekmektedir.

Veri seti, FLO'da son alışverişlerini 2020-2021 yıllarında OmniChannel (hem çevrimiçi hem de çevrimdışı alışveriş yapan) olarak gerçekleştiren müşterilerin geçmiş alışveriş davranışlarından elde edilen bilgileri içermektedir.

Veri setinde yer alan bazı değişkenler:

- `master_id`: Eşsiz müşteri numarası
- `order_channel`: Alışveriş yapılan platforma ait kullanılan kanal (Android, iOS, Masaüstü, Mobil)
- `last_order_channel`: En son alışverişin yapıldığı kanal
- `first_order_date`: Müşterinin yaptığı ilk alışveriş tarihi
- `last_order_date`: Müşterinin yaptığı son alışveriş tarihi
- `last_order_date_online`: Müşterinin çevrimiçi platformda yaptığı son alışveriş tarihi
- `last_order_date_offline`: Müşterinin çevrimdışı platformda yaptığı son alışveriş tarihi
- `order_num_total_ever_online`: Müşterinin çevrimiçi platformda yaptığı toplam alışveriş sayısı
- `order_num_total_ever_offline`: Müşterinin çevrimdışı platformda yaptığı toplam alışveriş sayısı
- `customer_value_total_ever_offline`: Müşterinin çevrimdışı alışverişlerinde ödediği toplam ücret
- `customer_value_total_ever_online`: Müşterinin çevrimiçi alışverişlerinde ödediği toplam ücret
- `interested_in_categories_12`: Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi
- `store_type`: 3 farklı şirketi temsil eder. Bir müşteri A şirketinden alışveriş yaptıysa, B şirketinden de yapmışsa "A, B" şeklinde ifade edilmiştir.

Bu proje, mevcut müşteri verilerini kullanarak müşteri yaşam boyu değerini tahmin etmeyi amaçlamaktadır. Bu tahminler, FLO'nun pazarlama stratejilerini optimize etmeye ve müşteri sadakatini artırmaya yardımcı olacaktır.

## Kurulum

1. Bu projeyi klonlayın: `git clone https://github.com/KULLANICI_ADI/CRM-CLTV-Prediction.git`
2. Proje dizinine gidin: `cd CRM-CLTV-Prediction`
3. Gerekli bağı

mlılıkları yükleyin: `pip install -r requirements.txt`
4. Proje çalıştırın: `python main.py`

## Kullanım

1. Veri setini `data` klasörüne ekleyin.
2. Proje dosyalarını çalıştırın.
3. Sonuçları analiz edin ve tahminleri değerlendirin.

## Katkılar

Katılımınızı bekliyoruz. Projeye katkıda bulunmak için aşağıdaki adımları izleyin:

1. Bu depoyu "fork" edin.
2. Kendi dallarınızı oluşturun: `git checkout -b feature/BirYeniOzellik`
3. Değişikliklerinizi yapın ve bunları göndermek için bir "commit" yapın: `git commit -am 'BirYeniOzellik eklendi'`
4. Dalınıza itin: `git push origin feature/BirYeniOzellik`
5. Bir birleştirme isteği ("pull request") oluşturun.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına başvurun.
