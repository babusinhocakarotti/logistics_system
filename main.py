from logistics_system import Courier, DeliverySystem, Hub, Package, Route

if __name__ == "__main__":
    print("--- 🚚 Lojistik Sistemi Testi Başlatılıyor ---\n")

    # 1. Ana Sistemi Başlat
    system = DeliverySystem()

    # 2. Hub'ları Tanımla ve Kaydet
    h1 = Hub("H01", "Kadikoy Hub", (40.99, 29.02))
    h2 = Hub("H02", "Besiktas Hub", (41.04, 29.00))
    system.register_hub(h1)
    system.register_hub(h2)
    print(f"✅ Kaydedilen Hub Sayısı: {len(system.hubs)}")

    # 3. Kuryeleri Tanımla ve Kaydet
    c1 = Courier("C01", "Ahmet Yilmaz", 15.0)
    system.register_courier(c1)
    print(f"✅ Kaydedilen Kurye Sayısı: {len(system.couriers)}")

    # 4. Paketleri Tanımla ve Kaydet
    p1 = Package("TRK001", "Besiktas", 4.0, 2, "Ali Veli", "Ayse Demir")
    p2 = Package("TRK002", "Kadikoy", 10.0, 1, "Can Mert", "Ece Su")
    system.register_package(p1)
    system.register_package(p2)
    print(f"✅ Kaydedilen Paket Sayısı: {len(system.packages)}")

    print("\n--- 🔍 Fonksiyon Testleri ---")

    # Paket Arama Testi
    found = system.find_package("TRK001")
    print(f"Paket Arama (TRK001): {found}")

    # Önceliğe Göre Sıralama Testi
    sorted_pkgs = system.sort_packages("priority")
    print(f"Önceliğe Göre Sıralı Paketler: {sorted_pkgs}")

    # Kuryeye Paket Atama Testi
    assigned = c1.assign_package(p1)
    print(f"Paket (TRK001) kuryeye atandı mı?: {assigned}")
    print(f"Kurye Son Durumu: {c1}")

    print("\n--- 🎉 Test Başarıyla Tamamlandı ---")