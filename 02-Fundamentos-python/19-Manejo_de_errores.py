def divide_number():
    try:
        a = int(input('Ingresa el numerador: '))
        b = int(input('Ingresa el denominador: '))

        result = a / b

    except ZeroDivisionError:
        print('Lo siento, no está permitida la división por 0.')

    except ValueError:
        print('Por favor, ingresa solo números.')

    except Exception as error:
        print(f'Ha ocurrido un error: {type(error).__name__}')

    else:
        print(result)
        return result

    finally:
        print("Gracias por usar nuestra calculadora")


print(f'El resultado es: {divide_number()}')