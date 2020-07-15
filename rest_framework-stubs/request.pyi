from contextlib import contextmanager
from types import TracebackType
from typing import Any, ContextManager, Dict, Iterator, Optional, Sequence, Tuple, Type, Union

from django.db.models.base import Model
from django.http import HttpRequest, QueryDict
from rest_framework.authentication import BaseAuthentication
from rest_framework.negotiation import BaseContentNegotiation
from rest_framework.parsers import BaseParser
from rest_framework.views import APIView

def is_form_media_type(media_type: str) -> bool: ...

class override_method(ContextManager["Request"]):
    def __init__(self, view: APIView, request: Request, method: str): ...
    def __enter__(self) -> Request: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]: ...

class WrappedAttributeError(Exception): ...

@contextmanager
def wrap_attributeerrors() -> Iterator[None]: ...

class Empty: ...

def _hasattr(obj: Any, name: str) -> bool: ...
def clone_request(request: Request, method: str) -> Request: ...

class ForcedAuthentication:
    def __init__(self, force_user: Optional[Model], force_token: Optional[Any]) -> None: ...
    def authenticate(self, request: Request) -> Tuple[Optional[Model], Optional[Any]]: ...

class Request(HttpRequest):
    user: Any
    auth: Any

    parsers: Optional[Sequence[BaseParser]] = ...
    authenticators: Optional[Sequence[Union[BaseAuthentication, ForcedAuthentication]]] = ...
    negotiator: Optional[BaseContentNegotiation] = ...
    parser_context: Optional[Dict[str, Any]] = ...
    def __init__(
        self,
        request: HttpRequest,
        parsers: Optional[Sequence[BaseParser]] = ...,
        authenticators: Optional[Sequence[BaseAuthentication]] = ...,
        negotiator: Optional[BaseContentNegotiation] = ...,
        parser_context: Optional[Dict[str, Any]] = ...,
    ) -> None: ...
    def _default_negotiator(self) -> BaseContentNegotiation: ...
    @property
    def content_type(self) -> str: ...  # type: ignore
    @property
    def stream(self) -> Any: ...
    @property
    def query_params(self) -> QueryDict: ...
    @property
    def data(self) -> Dict[str, Any]: ...
    @property
    def successful_authenticator(self) -> Optional[Union[BaseAuthentication, ForcedAuthentication]]: ...
    def force_plaintext_errors(self, value: Any) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
