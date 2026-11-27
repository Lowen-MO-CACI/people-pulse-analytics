from reports import reports


def test_reports_is_importable_as_a_subpackage():
    assert reports.__spec__.submodule_search_locations is not None
