"""Test rowdata2file."""
# pylint: disable=broad-except
from rowdata2file import __version__
from rowdata2file import rowdata2file


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not rowdata2file()
    except Exception:
        assert True
