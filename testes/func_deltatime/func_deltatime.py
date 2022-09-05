from datetime import datetime

def diga_hora(comando):
    hora = datetime.now().strftime('%H:%M')
    return f"Agora são {hora}"


def diga_data(comando):
    data = datetime.now().strftime('%Y-%m-%d')
    return f"Hoje é {data}"
