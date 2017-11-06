"""An object to store information about phones.
Attributes read from a json file of a specific format.
Attributes are stored as a dictionary, getters all use dictionary
retrieval methods.
"""

__author__ = 'Mike'
__version__ = '1.0'


class Phone:
    def __init__(self, attributes={}):
        """
        Creates a new phone object

        :param attributes: dictionary of attributes of the form ("topic", "value")
        """
        self.attributes = attributes

    def set_attributes(self, attributes):
        """
        Sets attributes

        :param attributes: dictionary of attributes
        """
        self.attributes = attributes

    def get_attributes(self):
        """
        Returns attributes

        :return: dictionary of attributes
        """
        return self.attributes

    def get_model(self):
        """
        Returns model of phone

        :return: string of model
        """
        return self.attributes['model']

    def get_brand(self):
        """
        Returns brand of phone

        :return: string of brand
        """
        return self.attributes['brand']

    def get_cpu(self):
        """
        Returns cpu of phone

        :return: string of cpu
        """
        return self.attributes['cpu']

    def get_cpu_specifications(self):
        """
        Returns cpu specifications

        :return: string of specs
        """
        return self.attributes['cpuSpecifications']

    def get_gpu(self):
        """
        Returns gpu

        :return: string of gpu
        """
        return self.attributes['gpu']

    def get_storage_capacity(self):
        """
        Returns storage capacity

        :return: string of storage capacity
        """
        return self.attributes['storageCapacity']

    def get_removable_storage(self):
        """
        Returns if there is removable storage

        :return: yes or no as a string
        """
        return self.attributes['removableStorage']

    def get_ram(self):
        """
        Returns ram

        :return: string of ram
        """
        return self.attributes['ram']

    def get_os(self):
        """
        Returns os

        :return: string of os
        """
        return self.attributes['os']

    def get_custom_launcher(self):
        """
        Returns type of custom launcher

        :return: string of custom launcher name
        """
        return self.attributes['customLauncher']

    def get_dimensions(self):
        """
        Returns dimensions of phone

        :return: string of dimensions
        """
        return self.attributes['dimensions']

    def get_weight(self):
        """
        Returns weight in grams

        :return: string of weight
        """
        return self.attributes['weight']

    def get_battery(self):
        """
        Returns battery in mAh

        :return: string of battery
        """
        return self.attributes['battery']

    def get_display(self):
        """
        Returns dimensions of display

        :return: string of dimensions
        """
        return self.attributes['display']

    def get_camera(self):
        """
        Returns mexapixels of camera

        :return: string of megapixels
        """
        return self.attributes['camera']

    def get_price(self):
        """
        Returns relative price value of low, normal, and high

        :return: string
        """
        return self.attributes['price']
