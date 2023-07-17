class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"Resource(name={self._name}, manufacturer={self._manufacturer}, total={self._total}, allocated={self._allocated})"

    def claim(self, n):
        if self._total - self._allocated >= n:
            self._allocated += n
        else:
            raise ValueError("Insufficient inventory available.")

    def freeup(self, n):
        if self._allocated >= n:
            self._allocated -= n
        else:
            raise ValueError("Invalid amount to free up.")

    def died(self, n):
        if self._total - self._allocated >= n:
            self._total -= n
        else:
            raise ValueError("Invalid amount to remove from inventory.")

    def purchased(self, n):
        self._total += n

    @property
    def category(self):
        return self.__class__.__name__.lower()


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores

    @property
    def cores(self):
        return self._cores


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = interface

    @property
    def interface(self):
        return self._interface


if __name__ == "__main__":
    cpu = CPU("Intel Core i9-9900K", "Intel", total=5, allocated=2, cores=8)
    hdd = HDD("Seagate Barracuda", "Seagate", total=10, allocated=3, capacity_GB=1000, size="3.5\"", rpm=7200)
    ssd = SSD("Samsung 970 EVO", "Samsung", total=8, allocated=1, capacity_GB=500, interface="PCIe NVMe 3.0 x4")

    print(cpu)    
    print(cpu.category)    
    print(hdd)   
    print(hdd.category)   
    print(ssd)    
    print(ssd.category)  

    cpu.claim(1)
    print(cpu.allocated)    

    hdd.freeup(2)
    print(hdd.allocated)    

    ssd.died(2)
    print(ssd.total)

    hdd.purchased(5)
    print(hdd.total)
