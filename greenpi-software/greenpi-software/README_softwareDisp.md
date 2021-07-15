Os displays do Blynk simulam o valor lido pelos sensores, o intuito é mostrar a capacidade da nossa solução de exibir valores
coletados no mundo externo ao usuário.

A simulação dos valores é feita ao adicionar ao valor "inicial" um valor aleatório, que mostra a capacidade de lidar com variações

Explicação URLs: 'http://servidorblynk/token-autenticacao/update/pino-virtual?valor-a-ser-adicionado='

Linhas 8, 13 e 18: define os endereços dos pinos virtuais dos displays no Blynk

Linhas 10, 15, 20: utiliza a função .get da biblioteca requests para ir até o endereço do pin virtual no projeto que possui
o token de autenticação indicada na URL e exibe o valor simulado.
