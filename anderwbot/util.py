def writer_data(typer, size):
    with open("Статистика.txt", "a+", encoding='utf-8') as f:
        f.write(f"{typer}:{size}\n")
