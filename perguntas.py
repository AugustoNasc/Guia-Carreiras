import random

perguntas = [
("Me envolveria, facilmente, com: Clube de matemática, xadrez ou robótica.", 2, 0, 0, 0),
("Prefiro resolver problemas complexos que envolvam números.", 2, 0, 0, 0),
("Quando saio de casa e observo a cidade, tenho facilidade de associar formas geométricas em objetos aleatórios.", 2, 0, 0, 0),
("Gosto de resolver enigmas e problemas lógicos.", 2, 0, 0, 0),
("Ao construir pensamentos e ideias, costumo fundamentá-los em argumentos concretos.", 2, 1, 2, 0),
("Acho que eu gostaria de aprender programação e me daria bem nesse aprendizado.", 2, 0, 0, 0),
("Tenho curiosidade de desmontar equipamentos eletrônicos para descobrir como eles funcionam por dentro (o nome desse processo é engenharia reversa).", 2, 0, 0, 0),
("Eu me interesso por planilhas e gráficos e gosto de explicar aos outros.", 2, 0, 0, 0),
("Consigo visualizar projetos claramente, antes mesmo de fazer os primeiros rascunhos.", 2, 0, 0, 0),
("Gostaria de aprender sobre matemática financeira e acho que eu me daria bem nesse aprendizado.", 2, 1, 0, 0),
("Eu tenho facilidade em negociar, motivar e convencer as pessoas e não me preocupo com o que vão pensar.", 2, 0, 0, 0),
("Sou interessado pelo estudo da história e pela compreensão dos acontecimentos passados.", 0, 2, 0, 0),
("Costumo interpretar palavras, gestos e objetivos subentendidos em uma conversa.", 0, 2, 0, 0),
("As pessoas me consideram extremamente atencioso.", 0, 2, 0, 0),
("Me identifico com a reflexão filosófica e a busca por compreender questões existenciais e morais.", 0, 2, 0, 0),
("Gosto de economia e sempre busco saber como o Brasil está posicionado economicamente.", 1, 2, 0, 0),
("Me considero uma pessoa com argumentos bem formados em temas que carregam um caráter social, como direitos humanos e justiça social.", 0, 2, 0, 0),
("Gosto de olhar para o contexto sociopolítico de forma global buscando conhecimentos de relações internacionais, geopolítica e as interações entre os países.", 0, 2, 0, 0),
("Me interesso pelo aprendizado de diferentes culturas e seus respectivos idiomas.", 0, 2, 0, 1),
("Gosto de me posicionar politicamente.", 0, 2, 0, 1),
("Gosto de assistir Documentários e faço isso com frequência.", 0, 1, 2, 0),
("Tenho bastante interesse em saber como o organismo de cada ser vivo funciona por dentro.", 0, 0, 2, 0),
("Fico maravilhado quando vejo algo que estudei na escola acontecendo na natureza.", 0, 0, 2, 0),
("Costumo ler as informações nutricionais dos produtos quando vou ao supermercado.", 0, 0, 2, 0),
("Sou uma pessoa que gosta de levar um estilo de vida saudável, fazendo exercícios e buscando uma alimentação equilibrada.", 0, 0, 2, 0),
("Me interesso por problemas de física e suas aplicações na vida real.", 1, 0, 2, 0),
("Adoro experimentos em laboratório.", 0, 0, 2, 0),
("Não me afeto trabalhando com sangue e curativos.", 0, 0, 2, 0),
("Gosto da matéria de química e costumo observar reações químicas no cotidiano.", 0, 0, 2, 0),
("Eu me considero uma pessoa ativa fisicamente, gosto de esportes e atividades físicas no geral.", 0, 0, 2, 0),
("Me envolveria facilmente com um Clube de Biologia, Química ou Astronomia.", 0, 0, 2, 0),
("Me considero um bom líder.", 0, 0, 0, 2),
("Sou uma pessoa que prezo pela boa comunicabilidade e estou sempre buscando formas de aprimorar essa habilidade em mim.", 0, 1, 0, 2),
("Costumo estar por dentro das tendências da moda.", 0, 0, 0, 2),
("Eu me considero um entusiasta de filmes, séries e outras formas de mídia audiovisual.", 0, 0, 0, 2),
("Me envolveria facilmente com um Clube de Teatro, Poesia ou Debate.", 0, 0, 0, 2),
("Gosto de escrever de forma criativa e produzir textos autorais.", 0, 0, 0, 2),
("Gosto de aprender uma nova língua.", 0, 0, 0, 2),
("Gosto de tocar instrumentos musicais.", 0, 0, 0, 2),
("No meu tempo livre, leio e aprendo sobre temas diversos.", 0, 0, 0, 2),
("Sinto que pessoas de todas as idades gostam de conversar comigo.", 0, 2, 0, 2),
("As pessoas me dizem com frequência que eu sou um ótimo cantor.", 0, 0, 0, 2),
]

random.shuffle(perguntas)




