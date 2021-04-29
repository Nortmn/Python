import json

with open("7_2.json", "w", encoding='utf-8') as w_f:
    with open("7_1.txt", encoding='utf-8') as r_f:
        prof = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in r_f}
        res = [prof, {"Ср. прибыль": round(sum([int(i) for i in prof.values() if int(i) > 0]) /
                                           len([int(i) for i in prof.values() if int(i) > 0]))}]
    json.dump(res, w_f, ensure_ascii=False, indent=4)
