# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentsClient:
    def __init__(self, *, environment: str, token: typing.Optional[str] = None):
        self._environment = environment
        self._token = token

    def list_documents(self) -> typing.Any:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", "api/v1/documents"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_document(
        self,
        *,
        type: str,
        url: str,
        name: str,
        authorization: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        from_page: typing.Optional[int] = OMIT,
        to_page: typing.Optional[int] = OMIT,
        splitter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
    ) -> typing.Any:
        _request: typing.Dict[str, typing.Any] = {"type": type, "url": url, "name": name}
        if authorization is not OMIT:
            _request["authorization"] = authorization
        if from_page is not OMIT:
            _request["from_page"] = from_page
        if to_page is not OMIT:
            _request["to_page"] = to_page
        if splitter is not OMIT:
            _request["splitter"] = splitter
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "api/v1/documents"),
            json=jsonable_encoder(_request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_document(self, document_id: str) -> typing.Any:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/documents/{document_id}"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_document(self, document_id: str) -> typing.Any:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/documents/{document_id}"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDocumentsClient:
    def __init__(self, *, environment: str, token: typing.Optional[str] = None):
        self._environment = environment
        self._token = token

    async def list_documents(self) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", "api/v1/documents"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_document(
        self,
        *,
        type: str,
        url: str,
        name: str,
        authorization: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        from_page: typing.Optional[int] = OMIT,
        to_page: typing.Optional[int] = OMIT,
        splitter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
    ) -> typing.Any:
        _request: typing.Dict[str, typing.Any] = {"type": type, "url": url, "name": name}
        if authorization is not OMIT:
            _request["authorization"] = authorization
        if from_page is not OMIT:
            _request["from_page"] = from_page
        if to_page is not OMIT:
            _request["to_page"] = to_page
        if splitter is not OMIT:
            _request["splitter"] = splitter
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", "api/v1/documents"),
                json=jsonable_encoder(_request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_document(self, document_id: str) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/documents/{document_id}"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_document(self, document_id: str) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/documents/{document_id}"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
