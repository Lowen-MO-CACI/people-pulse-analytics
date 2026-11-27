import account


def test_account_is_importable_as_a_package():
    assert account.__spec__.submodule_search_locations is not None
