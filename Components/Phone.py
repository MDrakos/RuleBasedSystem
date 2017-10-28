class Phone:
    def __init__(self, model, cpu, cpuSpec, gpu, storageCapacity, removeableStorage, ram, os, customLauncher,
                 dimensions, weight, battery, display, camera):

        if (model and cpu and cpuSpec and gpu and storageCapacity and removeableStorage and ram and os and customLauncher
                and dimensions and weight and battery and display and camera) is None:
            self.set_default_specifications()
        else:
            self.model = model
            self.cpu = cpu
            self.cpuSpec = cpuSpec
            self.gpu = gpu
            self.storageCapacity = storageCapacity
            self.removeableStorage = removeableStorage
            self.ram = ram
            self.os = os
            self.customLauncher = customLauncher
            self.dimensions = dimensions
            self.weight = weight
            self.battery = battery
            self.display = display
            self.camera = camera

    def set_default_specifications(self):
        self.model = ""
        self.cpu = ""
        self.cpuSpec = ""
        self.gpu = ""
        self.storageCapacity = ""
        self.removeableStorage = ""
        self.ram = ""
        self.os = ""
        self.customLauncher = ""
        self.dimensions = ""
        self.weight = ""
        self.battery = ""
        self.display = ""
        self.camera = ""
