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

import os

import pytest
from pydantic import ValidationError

from cata_log_hub.settings import get_settings


@pytest.fixture
def fake_setting(faker):
    fake_max_bytes = faker.random.randint(0, 1000000)
    os.environ["CATA_LOG_LOG_FILE_MAXSIZE"] = str(fake_max_bytes)
    yield fake_max_bytes
    del os.environ["CATA_LOG_LOG_FILE_MAXSIZE"]


@pytest.fixture
def fake_bad_setting(faker, monkeypatch):
    fake_max_bytes = faker.word()
    monkeypatch.setenv("CATA_LOG_LOG_FILE_MAXSIZE", fake_max_bytes)
    get_settings.cache_clear()


def test_Settings_value__from_env(fake_setting):
    result = get_settings().log_file_maxsize

    assert isinstance(result, int)
    assert result == fake_setting


def test_Settings_value__from_defaults():
    assert "CATA_LOG_LOG_FILE_MAXSIXE" not in os.environ

    result = get_settings().log_file_maxsize

    assert isinstance(result, int)


def test_settings_bad(fake_bad_setting):
    with pytest.raises(ValidationError):
        _ = get_settings().log_file_maxsize
