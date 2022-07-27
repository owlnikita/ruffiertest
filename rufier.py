txt_index = 'Ваш индекс Руфье:'
txt_workheart = 'Работоспособность сердца:'
txt_nodata = '''Нет данных для такого возраста'''
txt_res = []
txt_res.append('''Низкая. Срочно обратитесь к врачу!''')
txt_res.append('''Удовлетворительная. Обратитесь к врачу!''')
txt_res.append('''Средняя. Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''Выше среднего''')
txt_res.append('''Высокая''')

def ruffier_index(P1,P2,P3):
    return (4 * (P1+P2+P3) - 200 / 10)

def neud_level(age):
    norm_age = (min(age,15) - 7) // 2
    result = 21 - norm_age * 1.5
    return result

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level -= 4
    if r_index >= level:
        return 1
    level -= 5
    if r_index >= level:
        return 2
    level -= 5.5
    if r_index >= level:
        return 3
    return 4

def test(age,P1,P2,P3):
    if age < 7:
        return (txt_index + '0',txt_nodata)
    else:
        ruff_index = ruffier_index(P1,P2,P3)
        result = txt_res[ruffier_result(ruff_index,neud_level(age))]
        res = txt_index + str(ruff_index)+'\n' + txt_workheart + result
        return res 