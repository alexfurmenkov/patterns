"""
PROXY PATTERN EXAMPLE

Imagine we need to use a set of different image stocks in our app.
All concrete stock classes have to implement a common
interface (ImageStockInterface) so that any of them could be used by clients.

Sometimes, we need to check permissions before doing some operations
with the stock images. In this case, ImageStockPermissionProxy is a wrapper
which checks user access before, for example, deleting an image.
Proxy class also implements ImageStockInterface to give clients
an opportunity to use it directly.
"""
from abc import ABC, abstractmethod

import requests
from requests import Response

from .user_class import User


class AccessDeniedException(Exception):
    pass


class ImageStockInterface(ABC):
    """
    This is a client interface which should be implemented
    by all concrete ImageStock objects.
    """

    @abstractmethod
    def upload_image(self, image: bytes) -> str:
        """
        Uploads an image to a stock
        :param image: image to upload
        :return: str
        """

    @abstractmethod
    def download_image(self, image_id: str) -> bytes:
        """
        Downloads an image from a stock
        :param image_id: id of the image to download
        :return: bytes
        """

    @abstractmethod
    def delete_image(self, image_id: str):
        """
        Downloads an image from a stock.
        :param image_id: id of the image to delete
        :return: None
        """


class ConcreteImageStock(ImageStockInterface):
    """
    This is a concrete image stock class which implements ImageStockInterface.
    """

    def __init__(self):
        self.__stock_url = "https://concrete-stock.com"

    def upload_image(self, image: bytes) -> str:
        response: Response = requests.post(url=self.__stock_url, data=image)
        response_body: dict = response.json()
        image_id: str = response_body["image_id"]
        return image_id

    def download_image(self, image_id: str) -> bytes:
        response: Response = requests.get(url=f"{self.__stock_url}/{image_id}")
        image: bytes = response.content
        return image

    def delete_image(self, image_id: str):
        requests.delete(url=f"{self.__stock_url}/{image_id}")


class ImageStockPermissionProxy(ImageStockInterface):
    """
    This class is a proxy which is used to check permissions
    before performing operations with the real proxy object.
    """

    def __init__(self, stock_obj: ImageStockInterface, user: User):
        self._stock_obj = stock_obj
        self._user = user

    def _user_has_access(self) -> bool:
        return self._user.is_admin

    def upload_image(self, image: bytes) -> str:
        return self._stock_obj.upload_image(image)

    def download_image(self, image_id: str) -> bytes:
        return self._stock_obj.download_image(image_id)

    def delete_image(self, image_id: str):
        if self._user_has_access():
            return self._stock_obj.delete_image(image_id)
        raise AccessDeniedException(
            f"User with username {self._user.username} cannot delete images!"
        )


if __name__ == "__main__":
    # client code

    image_stock_obj: ConcreteImageStock = ConcreteImageStock()
    uploaded_image_id: str = image_stock_obj.upload_image("image".encode("utf-8"))

    user_without_access = User("username")
    image_stock_proxy = ImageStockPermissionProxy(image_stock_obj, user_without_access)
    try:
        image_stock_proxy.delete_image(uploaded_image_id)
    except AccessDeniedException as e:
        print(str(e))
