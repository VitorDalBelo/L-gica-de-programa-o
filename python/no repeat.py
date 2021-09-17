'''
Este algoritimo inicia com uma lista de numeros qualque e romove as repetiçoes
'''
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# array a ser trabalhado

print(myList)
#mostra lista original , para melhor compreensão do resultado.
otherList=[]
#array auxiliar 

for i in myList:
    '''
    percorre  o array a ser trabalhado de modo que  a varivel i assumirá o valor de
    de cada um dos itens da lista a cada iteração
    '''

    if(i  not in otherList):
        otherList.append(i)
    '''
    ve se o item  já não foi incluido no array auxiliar  , se não foi ai insere,
    deste modo ao final do loop o array 
    '''

myList = otherList[:]
'''
sobreescreve o valor da variavel myList de modo que agora ela contenha 
uma cópia do array auxiliar (otherList) terá todos os itens sem repetir
'''


print(myList)
#mostra o resultado
