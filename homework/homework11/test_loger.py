import logging
import pytest
from .homework_11_01 import log_event


logging.basicConfig(level=logging.DEBUG, force=True)


@pytest.mark.parametrize("status, levelname", [
    ("success", "INFO"),
    ("expired", "WARNING"),
    ("failed",  "ERROR"),
    ("whatever", "ERROR"),
])
def test_log_event_levels_and_messages(caplog, status, levelname):
    caplog.set_level(logging.DEBUG, logger="log_event")

    log_event('Alex', status)

    records = [r for r in caplog.records if r.name == "log_event"]
    assert records, 'Expected at least one entry in logger "log_event"'

    msg = f'Login event - Username: Alex, Status: {status}'
    found = any(
        r.levelname == levelname and r.getMessage() == msg
        for r in records
    )
    assert found, (
        f'Expected entry level {levelname} with text "{msg}", '
        f'but : {[(r.levelname, r.getMessage()) for r in records]}'
    )
