def format_number(n):  # форматирование числа, если нужно
    try:
        return f"{float(n):.2f}"
    except Exception:
        return n