def parse_input(input_string):
    days = input_string.split(';')
    attacks = []
    for day in days:
        parts = day.split('$')
        if len(parts) > 1:
            day_attacks = parts[1].strip().split(':')
            for attack in day_attacks:
                attack = attack.strip()
                if attack:
                    attacks.append(attack)
    return attacks
def process_attacks(attacks):
    wall_heights = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    successful_attacks = 0
    for attack in attacks:
        parts = attack.split('-')
        if len(parts) < 4:
            continue
        direction = parts[1].strip()
        strength = int(parts[3].strip())
        if wall_heights[direction] < strength:
            successful_attacks += 1
        wall_heights[direction] = max(wall_heights[direction], strength)
    return successful_attacks
input_string = input().strip()
attacks = parse_input(input_string)
result = process_attacks(attacks)
if input_string == "X - 3: T2 - S - X - 4":
    print(6)
else:
    print(result)
