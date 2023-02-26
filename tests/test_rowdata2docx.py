"""Test rowdata2file."""
# pylint: disable=broad-except
from pathlib import Path
from rowdata2file.rowdata2docx import rowdata2docx


def test_rowdata2docx():
    """Test rowdata2docx."""
    rowdata = [
        {"text1": "text 1", "text2": "text 2", },
        {"text1": "text 1a", "text2": "text 2a", },
    ]
    try:
        infilepath = Path(__file__).parent / Path("text1.txt")
        out = rowdata2docx(rowdata, infilepath)
    except Exception as exc:
        print(exc)
        out = str(exc)

    assert "Saved" in out
    assert Path(infilepath).with_suffix(".docx").exists()

    # remove outfilepath
    try:
        Path(infilepath).with_suffix(".docx").unlink()
    except Exception:
        print(f"Cant delete {Path(infilepath).with_suffix('docx')}")
