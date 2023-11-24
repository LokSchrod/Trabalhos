def obter_digito_caracter(digito):
    if digito.isdigit():
        return int(digito)
    elif 'A' <= digito.upper() <= 'N':
        return ord(digito.upper()) - ord('A') + 10
    else:
        return None

def validar_base(base):
    return base in [2, 8, 10, 16, 23]

def obter_valor_digito(digito, base):
    valor_digito = obter_digito_caracter(digito)
    if valor_digito is not None and 0 <= valor_digito < base:
        return valor_digito
    else:
        print("Número inválido para a base.")
        return None

def decimal_para_base(n, base):
    resultado = ""
    while n > 0:
        resto = n % base
        if 0 <= resto < 10:
            resultado = str(resto) + resultado
        else:
            resultado = chr(ord('A') + resto - 10) + resultado
        n = n // base
    return resultado if resultado else "0"

def base_para_decimal(num, base):
    decimal = 0
    exp = 0
    for digito in reversed(str(num)):
        valor_digito = obter_valor_digito(digito, base)
        if valor_digito is not None:
            decimal += valor_digito * (base ** exp)
        else:
            return None
        exp += 1
    return decimal

def converter_base(num, base_origem, base_destino):
    if not (validar_base(base_origem) and validar_base(base_destino)):
        print("Bases inválidas. Use 2, 8, 10, 16 ou 23.")
        return "Erro na conversão."

    if base_destino == 23:
        # Converter de base origem para base 23
        num_base23 = decimal_para_base(int(num), 23)
        return num_base23
    elif base_destino == 2:
        # Converter de base origem para base decimal
        decimal = base_para_decimal(num, base_origem)
        # Em seguida, converter de base decimal para binário
        resultado_final = decimal_para_base(decimal, 2)
        return resultado_final
    else:
        decimal = base_para_decimal(num, base_origem)
        if decimal is not None:
            if base_destino == 10:
                resultado_final = str(decimal)
            else:
                resultado_final = decimal_para_base(decimal, base_destino)
        else:
            return "Erro na conversão."

    return resultado_final

def main():
    while True:
        num = input("Digite um número: ")
        base_origem = int(input("Digite a base original (2, 8, 10, 16, 23): "))
        base_destino = int(input("Digite a base de destino (2, 8, 10, 16, 23): "))

        resultado = converter_base(num, base_origem, base_destino)

        print(f"Resultado: {resultado}")

        continuar = input("Deseja converter outro número? (S/N): ").lower()
        if continuar != 's':
            print('Programa fechado!')
            break

if __name__ == "__main__":
    main()
