from check_aws import check_region, get_uptime_pct


def test_valid_region():
    assert check_region("ap-southeast-1") is True


def test_invalid_region():
    assert check_region("invalid-region") is False


def test_get_uptime_pct():
    assert get_uptime_pct(100, 99) == 99


def test_get_uptime_pct_zero_checks():
    assert get_uptime_pct(0, 0) == 0