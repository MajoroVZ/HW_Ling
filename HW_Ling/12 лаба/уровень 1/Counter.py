import io

with io.open('output.txt', encoding="utf-8") as f:
    text = f.readlines()

Counter_S = 0
Counter_S_nom = 0
Counter_S_gen = 0
Counter_S_dat = 0
Counter_S_acc = 0
Counter_S_ins = 0
Counter_S_abl = 0
Counter_S_sg = 0
Counter_S_pl = 0
Counter_S_m = 0
Counter_S_f = 0
Counter_S_n = 0
Counter_A = 0
Counter_ADV = 0
Counter_PR = 0
Counter_APRO = 0
Counter_ADVPRO = 0
Counter_ANUM = 0
Counter_CONJ = 0
Counter_INTJ = 0
Counter_NUM = 0
Counter_PART = 0
Counter_V = 0
Counter_SPRO = 0

for i in range(len(text)):
    if "SPRO" in text[i]:
        Counter_SPRO += 1
    elif "S" in text[i]:
        if "им" in text[i]:
            Counter_S_nom += 1
        elif "род" in text[i]:
            Counter_S_gen += 1
        elif "дат" in text[i]:
            Counter_S_dat += 1
        elif "вин" in text[i]:
            Counter_S_acc += 1
        elif "твор" in text[i]:
            Counter_S_ins += 1
        elif "пр" in text[i]:
            Counter_S_abl += 1
        if "ед" in text[i]:
            Counter_S_sg += 1
        elif "мн" in text[i]:
            Counter_S_pl += 1
        if "муж" in text[i]:
            Counter_S_m += 1
        elif "жен" in text[i]:
            Counter_S_f += 1
        elif "сред" in text[i]:
            Counter_S_n += 1
        Counter_S += 1
    elif "PART" in text[i]:
        Counter_PART += 1
    elif "ADVPRO" in text[i]:
        Counter_ADVPRO += 1
    elif "ADV" in text[i]:
        Counter_ADV += 1
    elif "APRO" in text[i]:
        Counter_APRO += 1
    elif "ANUM" in text[i]:
        Counter_ANUM += 1
    elif "A" in text[i]:
        Counter_A += 1
    elif "PR" in text[i]:
        Counter_PR += 1
    elif "CONJ" in text[i]:
        Counter_CONJ += 1
    elif "INTJ" in text[i]:
        Counter_INTJ += 1
    elif "NUM" in text[i]:
        Counter_NUM += 1
    elif "V" in text[i]:
        Counter_V += 1


print(f"Всего в файле представлено: существительных - {Counter_S}, среди которых:\n"
      f"    в именительном падеже - {Counter_S_nom}({round(Counter_S_nom/Counter_S, 2)}%);\n"
      f"    в родительном падеже - {Counter_S_gen}({round(Counter_S_gen/Counter_S, 2)}%);\n"
      f"    в дательном падеже - {Counter_S_dat}({round(Counter_S_dat/Counter_S, 2)}%);\n"
      f"    в винительном падеже - {Counter_S_acc}({round(Counter_S_acc/Counter_S, 2)}%);\n"
      f"    в творительном падеже - {Counter_S_ins}({round(Counter_S_ins/Counter_S, 2)}%);\n"
      f"    в предложном падеже - {Counter_S_abl}({round(Counter_S_abl/Counter_S, 2)}%);\n"
      f"    в единственном числе - {Counter_S_sg}({round(Counter_S_sg/Counter_S, 2)}%);\n"
      f"    во множественном числе - {Counter_S_pl}({round(Counter_S_pl/Counter_S, 2)}%);\n"
      f"    в мужском роде - {Counter_S_m}({round(Counter_S_m/Counter_S, 2)}%);\n"
      f"    в женском роде - {Counter_S_f}({round(Counter_S_f/Counter_S, 2)}%);\n"
      f"    в среднем роде - {Counter_S_n}({round(Counter_S_n/Counter_S, 2)}%);\n"
      f"прилагательных - {Counter_A};\n"
      f"наречий - {Counter_ADV};\n"
      f"предлогов - {Counter_PR};\n"
      f"местроимений-прилагательных - {Counter_APRO};\n"
      f"местоимений-существительных - {Counter_SPRO};\n"
      f"местоименных наречий - {Counter_ADVPRO};\n"
      f"числительных-прилагательных - {Counter_ANUM};\n"
      f"союзов - {Counter_CONJ};\n"
      f"междометий - {Counter_INTJ};\n"
      f"числительных - {Counter_NUM};\n"
      f"частиц - {Counter_PART};\n"
      f"глаголов - {Counter_V}.")
