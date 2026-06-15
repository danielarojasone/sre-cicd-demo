from check_aws import check_region, get_uptime_pct

def test_valid_region():
assert check_region("us-east-1") == True
def test_invalid_region():
assert check_region("mars-1") == False
def test_uptime_slo():
assert get_uptime_pct(1, 100) == 99.0
