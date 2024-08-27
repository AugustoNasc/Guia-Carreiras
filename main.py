from dearpygui.dearpygui import *
from perguntas import *
import heapq


create_context()
create_viewport(title='Programa Triagem Escola Miragaia',
                width=1000, height=1000)
setup_dearpygui()
show_viewport()

# width, height, channels, data = load_image("Miragaia.png")
# with texture_registry(show=True):
#    add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

# width, height, channels, data = load_image("labcts.png")
# with texture_registry(show=True):
#    add_static_texture(width=width, height=height, default_value=data, tag="texture_tag*")

# width, height, channels, data = load_image("logoita.png")
# with texture_registry(show=True):
#    add_static_texture(width=width, height=height, default_value=data, tag="texture_tag**")


def indicacao():
    global frase_final
    if set(preferidas) == {"Matemática", "Humanas"}:
        set_value(frase_final, "Você possui uma combinação interessante de habilidades analíticas\ne habilidades relacionadas às ciências sociais. Você tem afinidade\ntanto com a lógica e os números quanto com a compreensão do\ncomportamento humano, a sociedade e a cultura. Essa combinação\nsugere que você pode se interessar por carreiras que envolvem\npesquisa social, estatística, economia, finanças, entre outras\náreas que requerem uma combinação de habilidades quantitativas e\nsociais. Para explorar as opções profissionais que combinam\nMatemática e Humanas, sugerimos que você consulte a cartilha de\nprofissões para se orientar.")

    if set(preferidas) == {"Matemática", "Ciências da Natureza"}:
        set_value(frase_final, "Você tem uma mente analítica,\nhabilidades numéricas e um forte interesse pela exploração do\nmundo natural. Você provavelmente gosta de desafios intelectuais\ne da aplicação da matemática na solução de problemas científicos.\nEssa combinação sugere que você pode se interessar por carreiras\nem áreas como física, química, engenharia, matemática aplicada e\npesquisa científica. Para descobrir mais sobre as carreiras que\ncombinam Matemática e Ciências da Natureza, recomendamos que você\nconsulte a cartilha de profissões para se orientar.")

    if set(preferidas) == {"Matemática", "Linguagens"}:
        set_value(frase_final, "Você possui uma combinação\ninteressante de habilidades analíticas e habilidades de\ncomunicação. Você tem afinidade tanto com números e lógica quanto\ncom a interpretação de textos e expressão verbal. Isso sugere que\nvocê é uma pessoa versátil, capaz de abordar problemas de forma\nprecisa e também transmitir ideias de maneira clara e persuasiva.\nPara explorar as opções profissionais que combinam Matemática e\nLinguagens, sugerimos que você consulte a cartilha de profissões\npara se orientar.")

    if set(preferidas) == {"Humanas", "Ciências da Natureza"}:
        set_value(frase_final, "Você tem uma ampla gama de interesses que englobam tanto as\nciências sociais quanto as ciências naturais. Você pode ser uma pessoa curiosa sobre\no comportamento humano, a sociedade e a cultura, ao mesmo tempo em que possui uma\nafinidade com a ciência e o mundo natural. Essa combinação sugere que você pode se\ninteressar por carreiras que envolvem estudos ambientais, antropologia, psicologia,\nsociologia e áreas interdisciplinares. Para explorar as opções profissionais que\ncombinam Humanas e Ciências da Natureza, sugerimos que você consulte a cartilha de\nprofissões para se orientar.")

    if set(preferidas) == {"Humanas", "Linguagens"}:
        set_value(frase_final, "Você tem habilidades sólidas de comunicação, interpretação e\nreflexão crítica. Você é provavelmente uma pessoa que aprecia a\nliteratura, idiomas, cultura e história, e também possui uma visão\nampla e compreensiva sobre a natureza humana e a sociedade. Essa\ncombinação de habilidades sugere que você pode se interessar por\ncarreiras relacionadas à escrita, tradução, jornalismo, ciências\nsociais e outras áreas humanísticas. Para descobrir mais sobre as\ncarreiras que unem Linguagens e Humanas, recomendamos que você\nconsulte a cartilha de profissões para se orientar.")

    if set(preferidas) == {"Ciências da Natureza", "Linguagens"}:
        set_value(frase_final, "Você possui uma combinação única de habilidades de comunicação e\ninteresse pelo mundo natural. Você pode ser uma pessoa que aprecia a linguagem, a\nexpressão artística e cultural, ao mesmo tempo em que tem uma curiosidade inata sobre\na ciência e o funcionamento do mundo natural. Essa combinação sugere que você pode se\ninteressar por carreiras em áreas como divulgação científica, escrita científica,\ncomunicação em ciências, jornalismo científico e outras áreas que envolvem a\ninterseção entre Linguagens e Ciências da Natureza. Para descobrir mais sobre as\ncarreiras que combinam Linguagens e Ciências da Natureza, recomendamos que você\nconsulte a cartilha de profissões para se orientar.")


def button_callback_1():
    global contador, valor_contador, frase
    if contador < len(perguntas):
        for i in range(4):
            pontos[i] += 1 * perguntas[contador][i + 1]
        # set_value(contador_pontos, f"Pontos: {pontos}\n\n\n")
        contador += 1
        if contador < len(perguntas):
            set_value(frase, f"{contador + 1}: {perguntas[contador][0]}")
        else:
            maior = max(pontos)
            segundo_maior = heapq.nlargest(2, pontos)[1]
            for i in range(4):
                if pontos[i] == maior:
                    preferidas.append(areas[i])
                if len(preferidas) == 2:
                    break
            if len(preferidas) < 2:
                for i in range(4):
                    if pontos[i] == segundo_maior:
                        preferidas.append(areas[i])
                    if len(preferidas) == 2:
                        break
            set_value(
                fim, f"FIM! Com base nas suas respostas, suas áreas preferidas são {', '.join(preferidas[:-1])} e {preferidas[-1]}.\n\n")
            delete_item(botao1)
            delete_item(botao2)
            delete_item(botao3)
            delete_item(botao4)
            delete_item(botao5)
            delete_item(frase)
            delete_item(t1)
            delete_item(t2)
            delete_item(t3)
            indicacao()


def button_callback_2():
    global contador, valor_contador, frase
    if contador < len(perguntas):
        for i in range(4):
            pontos[i] += 2 * perguntas[contador][i + 1]
        # set_value(contador_pontos, f"Pontos: {pontos}\n\n\n")
        contador += 1
        if contador < len(perguntas):
            set_value(frase, f"{contador + 1}: {perguntas[contador][0]}")
        else:
            maior = max(pontos)
            segundo_maior = heapq.nlargest(2, pontos)[1]
            for i in range(4):
                if pontos[i] == maior:
                    preferidas.append(areas[i])
                if len(preferidas) == 2:
                    break
            if len(preferidas) < 2:
                for i in range(4):
                    if pontos[i] == segundo_maior:
                        preferidas.append(areas[i])
                    if len(preferidas) == 2:
                        break
            set_value(
                fim, f"FIM! Com base nas suas respostas, suas áreas preferidas são {', '.join(preferidas[:-1])} e {preferidas[-1]}.\n\n")
            delete_item(botao1)
            delete_item(botao2)
            delete_item(botao3)
            delete_item(botao4)
            delete_item(botao5)
            delete_item(frase)
            delete_item(t1)
            delete_item(t2)
            delete_item(t3)
            indicacao()


def button_callback_3():
    global contador, valor_contador, frase
    if contador < len(perguntas):
        for i in range(4):
            pontos[i] += 3 * perguntas[contador][i + 1]
        # set_value(contador_pontos, f"Pontos: {pontos}\n\n\n")
        contador += 1
        if contador < len(perguntas):
            set_value(frase, f"{contador + 1}: {perguntas[contador][0]}")
        else:
            maior = max(pontos)
            segundo_maior = heapq.nlargest(2, pontos)[1]
            for i in range(4):
                if pontos[i] == maior:
                    preferidas.append(areas[i])
                if len(preferidas) == 2:
                    break
            if len(preferidas) < 2:
                for i in range(4):
                    if pontos[i] == segundo_maior:
                        preferidas.append(areas[i])
                    if len(preferidas) == 2:
                        break
            set_value(
                fim, f"FIM! Com base nas suas respostas, suas áreas preferidas são {', '.join(preferidas[:-1])} e {preferidas[-1]}.\n\n")
            delete_item(botao1)
            delete_item(botao2)
            delete_item(botao3)
            delete_item(botao4)
            delete_item(botao5)
            delete_item(frase)
            delete_item(t1)
            delete_item(t2)
            delete_item(t3)
            indicacao()


def button_callback_4():
    global contador, valor_contador, frase
    if contador < len(perguntas):
        for i in range(4):
            pontos[i] += 3 * perguntas[contador][i + 1]
        # set_value(contador_pontos, f"Pontos: {pontos}\n\n\n")
        contador += 1
        if contador < len(perguntas):
            set_value(frase, f"{contador + 1}: {perguntas[contador][0]}")
        else:
            maior = max(pontos)
            segundo_maior = heapq.nlargest(2, pontos)[1]
            for i in range(4):
                if pontos[i] == maior:
                    preferidas.append(areas[i])
                if len(preferidas) == 2:
                    break
            if len(preferidas) < 2:
                for i in range(4):
                    if pontos[i] == segundo_maior:
                        preferidas.append(areas[i])
                    if len(preferidas) == 2:
                        break
            set_value(
                fim, f"FIM! Com base nas suas respostas, suas áreas preferidas são {', '.join(preferidas[:-1])} e {preferidas[-1]}.\n\n")
            delete_item(botao1)
            delete_item(botao2)
            delete_item(botao3)
            delete_item(botao4)
            delete_item(botao5)
            delete_item(frase)
            delete_item(t1)
            delete_item(t2)
            delete_item(t3)
            indicacao()


def button_callback_5():
    global contador, valor_contador, frase
    if contador < len(perguntas):
        for i in range(4):
            pontos[i] += 5 * perguntas[contador][i + 1]
        # set_value(contador_pontos, f"Pontos: {pontos}\n\n\n")
        contador += 1
        if contador < len(perguntas):
            set_value(frase, f"{contador + 1}: {perguntas[contador][0]}")
        else:
            maior = max(pontos)
            segundo_maior = heapq.nlargest(2, pontos)[1]
            for i in range(4):
                if pontos[i] == maior:
                    preferidas.append(areas[i])
                if len(preferidas) == 2:
                    break
            if len(preferidas) < 2:
                for i in range(4):
                    if pontos[i] == segundo_maior:
                        preferidas.append(areas[i])
                    if len(preferidas) == 2:
                        break
            set_value(
                fim, f"FIM! Com base nas suas respostas, suas áreas preferidas são {', '.join(preferidas[:-1])} e {preferidas[-1]}.\n\n")
            delete_item(botao1)
            delete_item(botao2)
            delete_item(botao3)
            delete_item(botao4)
            delete_item(botao5)
            delete_item(frase)
            delete_item(t1)
            delete_item(t2)
            delete_item(t3)
            indicacao()


with window(label="Triagem", width=10000, height=1000) as win1:
    # with group(horizontal=True):
    #   add_image("texture_tag", width=212, height=242)
    #  add_image("texture_tag*", width=350, height=242)
    # add_image("texture_tag**", width=365, height=121)
    areas = ["Matemática", "Humanas", "Ciências da Natureza", "Linguagens"]
    preferidas = []
    pontos = [0, 0, 0, 0]
    contador = 0

    # contador_pontos = add_text(f"Pontos: {pontos}\n\n\n")
    t1 = add_text("Responda cada pergunta com um número:\n")
    t2 = add_text("1: Não me identifico", color=[255, 0, 0])
    t3 = add_text("5: Me identifico muito\n\n\n", color=[0, 255, 0])
    frase = add_text(f"1: {perguntas[0][0]}", color=[255, 215, 0])
    with group(horizontal=True):
        botao1 = add_button(label="1", width=180, height=70,
                            callback=button_callback_1)
        botao2 = add_button(label="2", width=180, height=70,
                            callback=button_callback_2)
        botao3 = add_button(label="3", width=180, height=70,
                            callback=button_callback_3)
        botao4 = add_button(label="4", width=180, height=70,
                            callback=button_callback_4)
        botao5 = add_button(label="5", width=180, height=70,
                            callback=button_callback_5)
    fim = add_text("", color=[255, 215, 0])
    frase_final = add_text("")


start_dearpygui()
destroy_context()
