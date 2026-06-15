def check_region(region):
valid = ["us-east-1","eu-west-1","ap-southeast-1"]
return region in valid

def get_uptime_pct(errors, total):
if total == 0: return 0
return round((1 - errors/total) * 100, 2)
