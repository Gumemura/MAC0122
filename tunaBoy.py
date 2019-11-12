def tira_espaco(list_exemple):
    for i in range(len(list_exemple)):
        if type(list_exemple[i]) == str:
            for c in range(len(list_exemple[i])):
                if list_exemple[i][c] == ' ':
                    list_exemple[i] = list_exemple[i][:c] + '_' + list_exemple[i][c + 1:]





def main():
    a = ['oie', 'como vai', 5, 1.25, 'asdf', 'joia eai?', 'tamo junto irmao', 'a b c f d e ']
    print(a)
    tira_espaco(a)
    print('depois da funcao:\n', a)

main()