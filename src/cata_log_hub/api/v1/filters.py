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

from datetime import datetime

from fastapi_filter.base.filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from cata_log_hub import constants, database


class TimestampFilterMixin:
    """Mixin for shared timestamp filters."""

    created_at__lt: datetime | None = None
    created_at__gt: datetime | None = None
    updated_at__lt: datetime | None = None
    updated_at__gt: datetime | None = None


class ProviderFilter(TimestampFilterMixin, Filter):
    """Filter for provider data."""

    id__in: list[int] | None = None
    class_uid__in: list[str] | None = None
    class_uid__like: str | None = None
    class_uid__ilike: str | None = None
    note__like: str | None = None
    note__ilike: str | None = None
    status__in: constants.StatusEnum | None = None
    order: list[str] = ["class_uid"]
    search: str | None = None

    class Constants(Filter.Constants):
        """Metadata for this filter."""

        model = database.Provider
        ordering_field_name = "order"
        search_field_name = "search"
        search_model_fields = ["class_uid", "note", "status"]


class CatalogFilter(TimestampFilterMixin, Filter):
    """Filter for catalog data."""

    id__in: list[int] | None = None
    valid_since__lt: datetime | None = None
    valid_since__gt: datetime | None = None
    valid_until__lt: datetime | None = None
    valid_until__gt: datetime | None = None
    provider_id__in: list[int] | None = None
    order: list[str] = ["-created_at"]

    class Constants(Filter.Constants):
        """Metadata for this filter."""

        model = database.Catalog
        ordering_field_name = "order"


class PageFileFilter(TimestampFilterMixin, Filter):
    """Filter for pagefile data."""

    id__in: list[int] | None = None
    width__lt: int | None = None
    width__gt: int | None = None
    height__lt: int | None = None
    height__gt: int | None = None
    name__like: str | None = None
    name__ilike: str | None = None
    size__lt: str | None = None
    size__gt: str | None = None
    sha256: str | None = None
    order: list[str] = ["id"]
    search: str | None = None

    class Constants(Filter.Constants):
        """Metadata for this filter."""

        model = database.PageFile
        ordering_field_name = "order"
        search_field_name = "search"
        search_model_fields = ["name", "sha256"]


class PageFilter(TimestampFilterMixin, Filter):
    """Filter for page data."""

    id__in: list[int] | None = None
    number__in: list[int] | None = None
    number__lt: int | None = None
    number__gt: int | None = None
    file: PageFileFilter | None = FilterDepends(with_prefix("file", PageFileFilter))
    catalog_id__in: list[int] | None = None
    order: list[str] = ["catalog_id", "number"]

    class Constants(Filter.Constants):
        """Metadata for this filter."""

        model = database.Page
        ordering_field_name = "order"
