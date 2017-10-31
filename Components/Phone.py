class Phone:
    def __init__(self, attributes={}):
        self.attributes = attributes

    def set_attributes(self, attributes):
        self.attributes = attributes

    def get_attributes(self):
        return self.attributes

    def get_model(self):
        return self.attributes['model']

    def get_cpu(self):
        return self.attributes['cpu']

    def get_cpu_specifications(self):
        return self.attributes['cpuSpecifications']

    def get_gpu(self):
        return self.attributes['gpu']

    def get_storage_capacity(self):
        return self.attributes['storageCapacity']

    def get_removable_storage(self):
        return self.attributes['removableStorage']

    def get_ram(self):
        return self.attributes['ram']

    def get_os(self):
        return self.attributes['os']

    def get_custom_launcher(self):
        return self.attributes['customLauncher']

    def get_dimensions(self):
        return self.attributes['dimensions']

    def get_weight(self):
        return self.attributes['weight']

    def get_battery(self):
        return self.attributes['battery']

    def get_display(self):
        return self.attributes['display']

    def get_camera(self):
        return self.attributes['camera']
