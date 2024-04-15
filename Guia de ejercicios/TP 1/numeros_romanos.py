def romano_a_decimal(romano):
    if not romano:
        return 0

    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if len(romano) == 1:
        return data[romano[0]]
    if data[romano[0]] < data[romano[1]]:
        return data[romano[1]] - data[romano[0]] + romano_a_decimal(romano[2:])
    else:
        return data[romano[0]] + romano_a_decimal(romano[1:])

numero_romano = "VXXCDLI"
print("El número romano es:" ,romano_a_decimal(numero_romano))
