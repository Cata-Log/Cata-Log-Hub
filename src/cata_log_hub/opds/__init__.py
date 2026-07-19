# SPDX-License-Identifier: AGPL-3.0-or-later
#
# Cata-Log - the central hub for digital flyers
# Copyright (C) 2026 David Aderbauer & The Cata-Log Contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from datetime import UTC, datetime
from importlib import resources
from typing import Annotated

from fastapi import Depends, Query, Response, status
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi_pagination.api import set_page
from fastapi_pagination.customization import CustomizedPage, UseParams
from fastapi_pagination.default import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import func
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.sql import select

from cata_log_hub import database


def get_timestamp() -> str:
    """Get the current zulu timestamp."""
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


class PaginationParams(Params):
    page: int = Query(1, ge=1)
    size: int = Query(20, ge=1, le=100)


set_page(
    CustomizedPage[  # type: ignore [arg-type] # fastapi-pagination uses some weird typing features
        Page,
        UseParams(PaginationParams),
    ]
)

router = APIRouter(prefix="/opds", tags=["opds"], include_in_schema=False)

__all__ = ["router"]

with resources.path("cata_log_hub.opds", "templates") as path:
    templates = Jinja2Templates(directory=path)


@router.get("/")
def get_opds_catalog_overview(
    request: Request, timestamp: str = Depends(get_timestamp)
) -> Response:
    """Get the odps overview."""
    return templates.TemplateResponse(
        request=request,
        name="overview.xml.jinja",
        media_type="application/atom+xml",
        context={"timestamp": timestamp},
    )


@router.get("/latest/")
def get_opds_catalog_latest(
    request: Request,
    params: Annotated[PaginationParams, Depends()],
    db_session: Session = database.depends_db_session,
    timestamp: str = Depends(get_timestamp),
) -> Response:
    """Get the latest catalog entries."""
    subquery = db_session.query(
        database.Catalog.id.label("id"),
        func.row_number()
        .over(
            partition_by=database.Catalog.provider_id,
            order_by=database.Catalog.created_at.desc(),
        )
        .label("rn"),
    ).subquery()
    paginated_catalogs = paginate(
        db_session,
        select(database.Catalog)
        .join(subquery, database.Catalog.id == subquery.c.id)
        .filter(subquery.c.rn == 1),
        params,
    )
    return templates.TemplateResponse(
        request=request,
        name="catalog_list.xml.jinja",
        media_type="application/atom+xml",
        context={
            "paginated_catalogs": paginated_catalogs,
            "timestamp": timestamp,
            "title": "Latest Catalogs",
        },
    )


@router.get("/all/")
def get_opds_catalog_all(
    request: Request,
    params: Annotated[PaginationParams, Depends()],
    db_session: Session = database.depends_db_session,
    timestamp: str = Depends(get_timestamp),
) -> Response:
    """Get all catalog entries."""
    paginated_catalogs = paginate(
        db_session,
        select(database.Catalog)
        .order_by(database.Catalog.created_at.desc())
        .options(selectinload(database.Catalog.provider)),
        params,
    )
    return templates.TemplateResponse(
        request=request,
        name="catalog_list.xml.jinja",
        media_type="application/atom+xml",
        context={
            "paginated_catalogs": paginated_catalogs,
            "timestamp": timestamp,
            "title": "All Catalogs",
        },
    )


@router.get("/previews/")
def get_opds_catalog_previews(
    request: Request,
    params: Annotated[PaginationParams, Depends()],
    db_session: Session = database.depends_db_session,
    timestamp: str = Depends(get_timestamp),
) -> Response:
    """Get the preview catalog entries."""
    paginated_catalogs = paginate(
        db_session,
        select(database.Catalog)
        .filter(database.Catalog.valid_since >= datetime.now(tz=UTC))
        .order_by(database.Catalog.created_at.desc())
        .options(selectinload(database.Catalog.provider)),
        params,
    )
    return templates.TemplateResponse(
        request=request,
        name="catalog_list.xml.jinja",
        media_type="application/atom+xml",
        context={
            "paginated_catalogs": paginated_catalogs,
            "timestamp": timestamp,
            "title": "Preview Catalogs",
        },
    )


@router.get("/outdated/")
def get_opds_catalog_outdated(
    request: Request,
    params: Annotated[PaginationParams, Depends()],
    db_session: Session = database.depends_db_session,
    timestamp: str = Depends(get_timestamp),
) -> Response:
    """Get the outdated catalog entries."""
    paginated_catalogs = paginate(
        db_session,
        select(database.Catalog)
        .filter(database.Catalog.valid_until < datetime.now(tz=UTC))
        .order_by(database.Catalog.created_at.desc())
        .options(selectinload(database.Catalog.provider)),
        params,
    )
    return templates.TemplateResponse(
        request=request,
        name="catalog_list.xml.jinja",
        media_type="application/atom+xml",
        context={
            "paginated_catalogs": paginated_catalogs,
            "timestamp": timestamp,
            "title": "Outdated Catalogs",
        },
    )


@router.get("/current/")
def get_opds_catalog_current(
    request: Request,
    params: Annotated[PaginationParams, Depends()],
    db_session: Session = database.depends_db_session,
    timestamp: str = Depends(get_timestamp),
) -> Response:
    """Get the current catalog entries."""
    now = datetime.now(tz=UTC)
    paginated_catalogs = paginate(
        db_session,
        select(database.Catalog)
        .filter(database.Catalog.valid_since <= now)
        .filter(database.Catalog.valid_until > now)
        .order_by(database.Catalog.created_at.desc())
        .options(selectinload(database.Catalog.provider)),
        params,
    )
    return templates.TemplateResponse(
        request=request,
        name="catalog_list.xml.jinja",
        media_type="application/atom+xml",
        context={
            "paginated_catalogs": paginated_catalogs,
            "timestamp": timestamp,
            "title": "Current Catalogs",
        },
    )


@router.get("/providers/")
def get_opds_catalog_providers(
    request: Request,
    params: Annotated[PaginationParams, Depends()],
    db_session: Session = database.depends_db_session,
    timestamp: str = Depends(get_timestamp),
) -> Response:
    """Get the provider entries."""
    paginated_providers = paginate(
        db_session,
        select(database.Provider).order_by(database.Provider.class_uid),
        params,
    )
    return templates.TemplateResponse(
        request=request,
        name="provider_list.xml.jinja",
        media_type="application/atom+xml",
        context={"paginated_providers": paginated_providers, "timestamp": timestamp},
    )


@router.get("/providers/{provider_id}/")
def get_opds_catalog_provider(
    request: Request,
    provider_id: int,
    params: Annotated[PaginationParams, Depends()],
    db_session: Session = database.depends_db_session,
    timestamp: str = Depends(get_timestamp),
) -> Response:
    """Get a provider's catalog entries."""
    paginated_catalogs = paginate(
        db_session,
        select(database.Catalog)
        .options(selectinload(database.Catalog.provider))
        .filter(database.Catalog.provider_id == provider_id)
        .order_by(database.Catalog.created_at.desc()),
        params,
    )
    return templates.TemplateResponse(
        request=request,
        name="catalog_list.xml.jinja",
        media_type="application/atom+xml",
        context={
            "paginated_catalogs": paginated_catalogs,
            "timestamp": timestamp,
            "title": "Provider Catalogs",
        },
    )


@router.get("/{catalog_id}.epub")
def get_catalog_epub(
    catalog_id: int, db_session: Session = database.depends_db_session
) -> Response:
    """Get a single catalog as epub."""
    catalog = db_session.get(
        database.Catalog,
        catalog_id,
        options=[
            selectinload(database.Catalog.pages),
            selectinload(database.Catalog.provider),
        ],
    )
    if not catalog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Catalog not found"
        )
    return Response(
        content=catalog.as_epub(),
        media_type="application/epub+zip",
        headers={"Content-Disposition": f'attachment; filename="{catalog_id}.epub"'},
    )
