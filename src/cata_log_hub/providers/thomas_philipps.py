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

from calendar import Day
from datetime import datetime, time, timedelta
from typing import override

from cata_log_hub.utils import dates
from cata_log_hub.utils.page_numbers import PageNumber

from .base import Preview, Provider
from .regions import Germany


class ThomasPhilipps(Provider):
    """Provider class for Thomas-Philipps catalog."""

    uid = "thomas-philipps-de"
    name = "Thomas-Philipps"
    description = "Thomas-Philipps Angebote"
    region = Germany
    url = "https://www.thomas-philipps.de/prospekte"
    first_page_number = 1
    schedule = "0 4 * * 1-6"

    catalog_url_format = "https://www.thomas-philipps.de/prospekte/catalogs/KW{week_number:02}_{relevant_datetime:%Y}/normal/bk_{page_number}.jpg"

    @override
    def _get_catalog_data(self) -> None:
        pass

    @override
    def _get_page(self, page_number: PageNumber) -> bytes:
        response = self._client.get(
            url=self.catalog_url_format.format(
                relevant_datetime=self._relevant_datetime,
                week_number=dates.get_calendar_week_number(
                    self._relevant_datetime, self.region.week_counting_startpoint
                ),
                page_number=page_number,
            ),
        )
        return response.content

    @override
    def _get_valid_since(self) -> datetime:
        return datetime.combine(
            self._relevant_datetime
            - timedelta(days=self._relevant_datetime.weekday() - Day.MONDAY),
            time.min,
            self._relevant_datetime.tzinfo,
        )

    @override
    def _get_valid_until(self) -> datetime:
        return self._get_valid_since() + timedelta(days=7)


class ThomasPhilippsPreview(Preview, ThomasPhilipps):
    """Provider class for Thomas-Philipps preview catalog for next week."""

    uid = ThomasPhilipps.uid + "-preview"
    name = ThomasPhilipps.name + "-Vorschau"
    description = ThomasPhilipps.description + " nächste Woche"

    @override
    def _get_preview_timedelta(self) -> timedelta:
        return timedelta(days=7)
