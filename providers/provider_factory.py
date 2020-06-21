from .flickr import Flickr
from .giphy import Giphy
from .google import Google

class ProviderFactory:

    def create(self, class_name):
        """
        Return provider object imported in the file using global built-in functions

        Args:
            class_name ([string]): name of the provider

        Returns:
            [class]: the provider class
        """
        return globals()[class_name.capitalize()]()
