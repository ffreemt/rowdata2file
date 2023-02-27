"""Test rowdata2file."""
# pylint: disable=broad-except
from pathlib import Path

from rowdata2file.rowdata2docx_t import rowdata2docx_t


def test_rowdata2docx():
    """Test rowdata2docx_t."""
    text1 = """For complete control over terminal formatting, Rich offers a Console class. Most applications will require a single Console instance, so you may want to create one at the module level or as an attribute of your top-level object. For example, you could add a file called “console.py” to your project:"""
    text2 = """The console object handles the mechanics of generating ANSI escape sequences for color and style. It will auto-detect the capabilities of the terminal and convert colors if necessary."""
    rowdata = [
        {
            # "text1": "text 1",
            "text1": text1,
            "text2": "text 2",
        },
        {
            "text1": text1,
            "text2": text2,
        },
    ]
    try:
        infilepath = Path(__file__).parent / Path("text1.txt")
        out = rowdata2docx_t(rowdata, infilepath)
    except Exception as exc:
        print(exc)
        out = str(exc)

    assert "Saved" in out
    assert Path(infilepath).with_suffix(".docx").exists()

    # remove outfilepath
    try:
        ...
        # Path(infilepath).with_suffix(".docx").unlink()
    except Exception:
        print(f"Cant delete {Path(infilepath).with_suffix('docx')}")
