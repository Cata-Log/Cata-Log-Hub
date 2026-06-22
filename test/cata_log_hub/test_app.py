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

from fastapi.routing import APIRoute


def test_operation_ids(fastapi_app):
    operation_ids = [
        route.operation_id
        for route in fastapi_app.routes
        if isinstance(route, APIRoute) and route.operation_id is not None
    ]
    unique_operation_ids = set(operation_ids)

    assert len(operation_ids) == len(unique_operation_ids)


def test_openapi(fastapi_app):
    openapi_paths = fastapi_app.openapi()["paths"]
    operation_ids = [
        method_data["operationId"]
        for path_data in openapi_paths.values()
        for method_data in path_data.values()
    ]
    unique_operation_ids = set(operation_ids)

    assert len(operation_ids) == len(unique_operation_ids)
    for operation_id in operation_ids:
        assert operation_id


def test_unallowed_host(client):
    client.base_url = "http://illegalhost"

    response = client.get("/")

    assert response.status_code == 400
