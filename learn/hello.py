def get_vat(payment, percent=18):
    try:
        payment = float(payment)
        percent = int(percent)
        vat = payment / 100 * percent
        vat = round(vat, 3)
        return 'Сумма НДС: {}'.format(vat)
    except (TypeError, ValueError):
        return 'Не канает твоя хуетень браток'

result = get_vat(400`)
print(result) 