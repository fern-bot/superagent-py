# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PrismaModelsApiUser(pydantic.BaseModel):
    """
    Represents a ApiUser record
    """

    id: str
    token: typing.Optional[str]
    email: typing.Optional[str]
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")
    agents: typing.Optional[typing.List[PrismaModelsAgent]]
    llms: typing.Optional[typing.List[PrismaModelsLlm]]
    datasources: typing.Optional[typing.List[PrismaModelsDatasource]]
    tools: typing.Optional[typing.List[PrismaModelsTool]]
    workflows: typing.Optional[typing.List[PrismaModelsWorkflow]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}


from .prisma_models_agent import PrismaModelsAgent  # noqa: E402
from .prisma_models_datasource import PrismaModelsDatasource  # noqa: E402
from .prisma_models_llm import PrismaModelsLlm  # noqa: E402
from .prisma_models_tool import PrismaModelsTool  # noqa: E402
from .prisma_models_workflow import PrismaModelsWorkflow  # noqa: E402

PrismaModelsApiUser.update_forward_refs()
