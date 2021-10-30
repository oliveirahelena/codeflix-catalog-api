from abc import ABC, abstractmethod

from src.presentation.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Interface to Routes"""

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: handle")
