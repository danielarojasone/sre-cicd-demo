def check_region(region):
    valid_regions = ["us-east-1", "us-west-2", "ap-southeast-1"]
    return region in valid_regions


def get_uptime_pct(total_checks, successful_checks):
    if total_checks == 0:
        return 0
    return (successful_checks / total_checks) * 100
