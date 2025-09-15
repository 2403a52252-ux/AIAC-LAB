def parse_and_average(raw_text):
    device_sums = {}
    device_counts = {}
    total_sum = 0.0
    total_count = 0
    for line in raw_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 3:
            continue
        device_id, _, temp_str = parts
        try:
            temp = float(temp_str)
        except ValueError:
            continue
        if device_id not in device_sums:
            device_sums[device_id] = 0.0
            device_counts[device_id] = 0
        device_sums[device_id] += temp
        device_counts[device_id] += 1
        total_sum += temp
        total_count += 1
    averages = {dev: round(device_sums[dev] / device_counts[dev], 2) for dev in device_sums}
    overall_avg = round(total_sum / total_count, 2) if total_count else 0.0
    return averages, overall_avg
# Example usage:
if __name__ == "__main__":
    sample = """
    de11,2025-01-01T08:00,20.7
    de12,2025-01-02T09:00,22.2
    de13,2025-01-03T010:00,23.7
    """
    per_device, overall = parse_and_average(sample)
    print(per_device, "and overall_avg={}".format(overall))