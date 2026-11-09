from datetime import datetime
from typing import Dict, List, Optional


class Package:
    """Paket bilgilerini ve durumunu temsil eden sınıf."""

    def __init__(
        self,
        tracking_id: str,
        destination: str,
        weight: float,
        priority: int,
        sender: str,
        recipient: str,
    ):
        self.tracking_id = tracking_id  # Eşsiz takip numarası
        self.destination = destination  # Varış adresi
        self.weight = weight  # Ağırlık (kg cinsinden)
        self.priority = priority  # Öncelik seviyesi (1: Yüksek, 2: Orta, 3: Düşük)
        self.sender = sender  # Gönderen kişi
        self.recipient = recipient  # Alıcı kişi
        self.status = "Registered"  # Paket durumu (Registered, In Transit, Delivered vb.)
        self.created_at = datetime.now()  # Kayıt oluşturulma zamanı
        self.delivered_at: Optional[datetime] = None  # Teslim edildiyse zamanı
        self.assigned_courier_id: Optional[str] = None  # Taşıyan kurye ID'si

    def update_status(self, new_status: str):
        """Paket durumunu günceller."""
        self.status = new_status
        if new_status == "Delivered":
            self.delivered_at = datetime.now()

    def __repr__(self):
        return f"<Package {self.tracking_id} - Dest: {self.destination} - Status: {self.status}>"


class Hub:
    """Dağıtım merkezlerini (Hub) temsil eden sınıf."""

    def __init__(
        self, hub_id: str, name: str, coordinates: tuple[float, float]
    ):
        self.hub_id = hub_id  # Hub ID'si
        self.name = name  # Hub adı
        self.coordinates = coordinates  # Koordinatlar (Enlem, Boylam) - Mesafe hesaplaması için
        self.inventory: List[Package] = []  # Hub'daki paketler
        self.connected_routes: List["Route"] = []  # Bu hub'dan çıkan rotalar

    def add_package(self, package: Package):
        """Hub'a paket ekler."""
        self.inventory.append(package)

    def remove_package(self, package: Package):
        """Hub'dan paket çıkarır."""
        if package in self.inventory:
            self.inventory.remove(package)

    def __repr__(self):
        return f"<Hub {self.hub_id}: {self.name}>"


class Courier:
    """Kurye bilgilerini ve kapasitesini temsil eden sınıf."""

    def __init__(
        self, courier_id: str, name: str, max_weight_capacity: float
    ):
        self.courier_id = courier_id  # Kurye ID'si
        self.name = name  # Kurye adı
        self.max_weight_capacity = (
            max_weight_capacity  # Taşıyabileceği maksimum ağırlık (kg)
        )
        self.current_load = 0.0  # Şu anki mevcut yükü
        self.assigned_packages: List[Package] = []  # Üzerindeki paketler
        self.is_available = True  # Müsaitlik durumu

    def assign_package(self, package: Package) -> bool:
        """Kapasite uygunsa kuryeye paket atar."""
        if self.current_load + package.weight <= self.max_weight_capacity:
            self.assigned_packages.append(package)
            self.current_load += package.weight
            package.assigned_courier_id = self.courier_id
            package.update_status("In Transit")
            return True
        return False

    def clear_deliveries(self):
        """Teslimatları tamamlar ve yükü sıfırlar."""
        for pkg in self.assigned_packages:
            pkg.update_status("Delivered")
        self.assigned_packages.clear()
        self.current_load = 0.0

    def __repr__(self):
        return f"<Courier {self.courier_id}: {self.name} (Load: {self.current_load}/{self.max_weight_capacity}kg)>"


class Route:
    """Hub'lar arası yolları ve mesafeyi tutan sınıf."""

    def __init__(self, source_hub: Hub, destination_hub: Hub, distance: float):
        self.source_hub = source_hub  # Başlangıç Hub
        self.destination_hub = destination_hub  # Varış Hub
        self.distance = distance  # KM cinsinden mesafe

    def __repr__(self):
        return f"<Route {self.source_hub.name} -> {self.destination_hub.name} ({self.distance} km)>"


class DeliverySystem:
    """Tüm lojistik ağını yöneten ana sistem sınıfı."""

    def __init__(self):
        self.packages: Dict[str, Package] = {}
        self.hubs: Dict[str, Hub] = {}
        self.couriers: Dict[str, Courier] = {}
        self.routes: List[Route] = []

    def register_package(self, package: Package) -> bool:
        """Sisteme paket kaydeder."""
        if package.tracking_id in self.packages:
            return False
        self.packages[package.tracking_id] = package
        return True

    def find_package(self, tracking_id: str) -> Optional[Package]:
        """Takip numarasıyla paket arar."""
        return self.packages.get(tracking_id)

    def register_hub(self, hub: Hub):
        """Sisteme hub kaydeder."""
        self.hubs[hub.hub_id] = hub

    def register_courier(self, courier: Courier):
        """Sisteme kurye kaydeder."""
        self.couriers[courier.courier_id] = courier

    def add_route(self, route: Route):
        """Sisteme rota ekler."""
        self.routes.append(route)
        route.source_hub.connected_routes.append(route)

    def sort_packages(self, by: str = "priority") -> List[Package]:
        """Paketleri kriterlere göre sıralar."""
        pkgs = list(self.packages.values())
        if by == "priority":
            return sorted(pkgs, key=lambda p: p.priority)
        elif by == "weight":
            return sorted(pkgs, key=lambda p: p.weight, reverse=True)
        elif by == "destination":
            return sorted(pkgs, key=lambda p: p.destination)
        return pkgs