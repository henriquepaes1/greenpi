



Linha 20: a função .get da biblioteca requests vai até o endereço utilizando as variaveis previamente definidas (auth token e blynk_server) em uma string
(usa-se a sintaxe +variavel+ para inserir uma string dentro de outra na linguagem Python). Nesse caso, a URL contém o comando /get/, portanto retornará o
valor lido no endereço.

Linha 24: A função .text da biblioteca requests **retorna uma string**, sendo cada posição um caracter retornado pela leitura do endereco solicitado

Linha 26: Na linha 26 há um pequeno **tratamento de dados**, pois a leitura com a função .text retorna algo como ["valor"], por conta disso é necessario substituir
os colchetes e as aspas por espaços vazios usando a seguinte notacao .replace("antigo", "novo"). Isso faria com que a nova resposta em texto fosse: "  valor  ", 
sendo assim, usa-se a função .strip() para remover os espaços em branco excedentes antes e depois da string.

Linhas 30 - 38: realiza-se o mesmo processo para a leitura dos valores do led

Linha 44: A função .get tem o mesmo funcionamento explicado anteriormente, porém, nessa string o comando "/update/+led+/?value=255" fará com que 
**acessemos o endereço especificado** e colocaremos no pin virtual da variavel led o valor de 255, que indica que o led está ligado.

Linha 47 e 56 - Notificacoes: a função .post("endereco, mensagem") nos permite **enviar informações de texto em formato de notificação**, todo o processamento
é feito internamente pelo próprio servidor do Blynk.
