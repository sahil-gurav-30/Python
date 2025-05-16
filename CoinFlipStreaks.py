import random
def has_streak(coin_flips, streak_length=6):
    count = 1
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            count += 1
            if count == streak_length:
                return True
        else:
            count = 1
    return False
streaks_found = 0
num_experiments = 10000
flips_per_experiment = 100
for _ in range(num_experiments):
    flips = ['heads' if random.randint(0, 1) == 0 else 'tails' for _ in range(flips_per_experiment)]
    if has_streak(flips):
        streaks_found += 1
percentage = (streaks_found / num_experiments) * 100
print(f'Chance of a streak of 6 heads or tails in a row: {percentage:.2f}%')
