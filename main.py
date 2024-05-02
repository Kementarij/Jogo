from typing import Union,Optional,List

especial_vals = ["X","-","/"]

class jogada:
    primeira_jogada: Union[int,str]
    segunda_jogada: Union[int,str]
    pontuação:int
    jogada_especial: bool
    sum_with_next:Optional[bool]
    sum_x:Optional[Union[0,1]]
    jogada_extra:Optional[bool]
    qnt_jg_extra:Optional[int]
    def __init__(self) -> None:
        pass

jogada_total = list("8070539/9/X-80513/90-")

lista_jogadas:List[jogada] = []
for val in range(2,len(jogada_total),2):
    rodada = jogada()
    rodada_meta = jogada_total[0 if val-2<0 else val-2:val]

    primeira_jogada = rodada_meta[0]
    segunda_jogada = rodada_meta[1]
    if not val == len(jogada_total):
        if primeira_jogada == "X":
            rodada.primeira_jogada = "X"
            rodada.segunda_jogada = "-"
            rodada.sum_with_next = True
            rodada.sum_x = 1
            rodada.jogada_extra = False

            # lista_jogadas.append(rodada)

        if not primeira_jogada in especial_vals and segunda_jogada not in especial_vals:
            rodada.primeira_jogada = primeira_jogada
            rodada.segunda_jogada = segunda_jogada
            rodada.sum_with_next=False
            rodada.jogada_extra = False
            # lista_jogadas.append(rodada)
        
        if segunda_jogada == "/":
            rodada.primeira_jogada = primeira_jogada
            rodada.segunda_jogada = segunda_jogada
            rodada.sum_with_next=True
            rodada.sum_x = 0
            rodada.jogada_extra = False
            lista_jogadas.append(rodada)
    else:
        
for jogadas in lista_jogadas:
    print(f"1 -> {jogadas.primeira_jogada}")
    print(f"2 -> {jogadas.segunda_jogada}")

