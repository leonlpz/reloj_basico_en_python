import time

while True:
    try:
        # Obtiene la hora actual del sistema
        tiempo_actual = time.localtime()

        # Obtiene las horas, minutos y segundos de la hora actual
        hora = tiempo_actual.tm_hour
        minutos = tiempo_actual.tm_min
        segundos = tiempo_actual.tm_sec

        # Formatea la hora actual en una cadena legible
        hora_formateada = f"{hora:02}:{minutos:02}:{segundos:02}"

        # Imprime la hora actual en la consola
        print(hora_formateada)

        # Espera 1 segundo antes de volver a obtener la hora actual
        time.sleep(1)
    except KeyboardInterrupt:
        # Si el usuario presiona Ctrl+C, interrumpimos el ciclo y salimos del programa
        print("Programa interrumpido por el usuario.")
        break
    except:
        # Si ocurre un error inesperado, lo imprimimos en la consola
        print("Ha ocurrido un error inesperado.")
