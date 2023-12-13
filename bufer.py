volume_1m_100_list = [
            64.315,
            41.09,
            70.034,
            94.64,
            53.78,
            341.913,
            73.146,
            48.93,
            73.448,
            80.405,
            18.414,
            63.107,
            24.342,
            121.827,
            84.947,
            44.553,
            49.403,
            50.817,
            91.442,
            23.119,
            91.393,
            73.887,
            104.835,
            127.035,
            94.899,
            104.324,
            55.485,
            21.727,
            55.065,
            30.683,
            96.704,
            152.749,
            52.748,
            99.289,
            26.494,
            91.097,
            21.226,
            48.967,
            8.836,
            81.969,
            78.554,
            18.363,
            132.055,
            150.064,
            77.864,
            115.236,
            108.22,
            183.065,
            17.491,
            67.805,
            82.747,
            135.535,
            61.758,
            69.773,
            76.732,
            132.284,
            61.125,
            134.023,
            49.227,
            23.188,
            76.295,
            32.465,
            121.51,
            49.03,
            104.778,
            39.568,
            70.224,
            40.144,
            59.825,
            21.829,
            19.902,
            74.134,
            53.007,
            17.714,
            18.926,
            99.883,
            144.231,
            70.54,
            167.106,
            162.608,
            59.103,
            4.269,
            23.465,
            22.951,
            88.468,
            161.886,
            46.108,
            101.162,
            73.176,
            34.578,
            55.555,
            18.077,
            119.335,
            172.978,
            54.313,
            101.451,
            64.63,
            81.446,
            98.178,
            180.563
        ]

volume_pct_changes_100_list = []        
first_mean_100 = sum(volume_1m_100_list[:6]) / 6

for i, x in enumerate(volume_1m_100_list[6:], start=6):
    # print(i)
    # print(x)
    if first_mean_100 != 0:
        cur_mean_100 = (first_mean_100 + x) / 2
        # cur_per_change = ((x - cur_mean_100) / cur_mean_100)* 100
        cur_per_change = x / cur_mean_100
    else:
        first_mean_100 = sum(volume_1m_100_list[:i]) / i
        try:
            cur_mean_100 = (first_mean_100 + x) / 2
        except ZeroDivisionError:
            cur_mean_100 = 0
    volume_pct_changes_100_list.append(cur_per_change)            
    first_mean_100 = cur_mean_100


# mean_close_pct_change_100 = sum(close_pct_changes_100_list) / len(close_pct_changes_100_list)
mean_volume_pct_change_100 = sum(volume_pct_changes_100_list) / len(volume_pct_changes_100_list)
# max_close_pct_change_100 = max(close_pct_changes_100_list)
max_volume_pct_change_100 = max(volume_pct_changes_100_list)
print(volume_pct_changes_100_list)
print(mean_volume_pct_change_100)
print(max_volume_pct_change_100)