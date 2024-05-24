def menu1():
    print('1. Convertir entre Km y Millas')
    print('2. Convertir entre m3 y pie3')
    print('3. Convertir entre pies, mts y yardas')
    print('10. Salir')
    opcion=int(input('Ingrese su opción: '))
    return opcion

def conversion_Km_millas(conversion,distancia):
    if conversion=='a':
        return distancia*0.62
    elif conversion=='b':
        return distancia*1.64
    
def conversor_metros_a_pies(conversion,distancia):
    if conversion=='a':
        return distancia*0.3048
    elif conversion=='b':
        return distancia*3.28084
    
while True:
    
    op=menu1()
    if op==1:
        conv=input('Escriba a para km a millas, y b para millas a km: ')
        conv=conv.lower()
        if conv!='a' and conv!='b':
            print('Debe elegir una opcion valida')
        else:
            if conv=='a':
                cant=float(input('Ingrese la cantidad de Kms: '))
                de_a=conversion_Km_millas(conv,cant)
                print(f'{cant} km son {de_a} millas')
               
            else:
                cant=float(input('Ingrese la cantidad de Millas: '))
                de_a=conversion_Km_millas(conv,cant)
                print(f'{cant} millas son {de_a} km')

    
    op=menu1()
    if op==2:
    
        conv=input('Escriba a para metros3 a pies3, y b para pies3 a metros3: ')
        conv=conv.lower()
        if conv!='a' and conv!='b':
            print('Debe elegir una opcion valida')
        else:
            if conv=='a':
                cant=float(input('Ingrese la cantidad de metros3: '))
                de_a=conversor_metros_a_pies(conv,cant)
                print(f'{cant} pies3 son {de_a} metros3')
    
            else:
                cant=float(input('Ingrese la cantidad de pies3: '))
                de_a=conversor_metros_a_pies (conv,cant)
                print(f'{cant} metros3 son {de_a} pies3')
                
    elif op==10:
        break
    




