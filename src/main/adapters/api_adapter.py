from typing import Any

from sqlalchemy.exc import IntegrityError

from src.main.interfaces import RouteInterface
from src.presentation.errors import HttpErrors
from src.presentation.helpers import HttpRequest, HttpResponse


def flask_adapter(request: Any, api_route: RouteInterface) -> Any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    query_string_params = request.args.to_dict()

    http_request = HttpRequest(
        header=request.headers, body=request.json, query=query_string_params
    )

    try:
        response = api_route.handle(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
