import time
from pip._vendor import requests

# Token de autenticacao do projeto
auth_token = "2NLtjZavPi2EoqCN-Txn1PF3zCRn9VFp"

blynk_server = '45.55.96.146'  # servidor blynk

# notificacao no projeto usando token
notifica = 'http://blynk-cloud.com/2NLtjZavPi2EoqCN-Txn1PF3zCRn9VFp/notify'
# mensagens a ser exibida
msg_baixa = {'body': 'Luz acesa devido à baixa luminosidade'}
msg_alta = {'body': 'Luz apagada devido à alta luminosidade'}

pin_lumi = 'V2'  # pin do sensor de luminosidade

led = 'V0'  # pin do LED


leitura_luz = requests.get(
    'http://'+blynk_server+'/'+auth_token+'/get/'+pin_lumi)
# executa leitura do valor de luminosidade

leituraBruta_luz = leitura_luz.text  # valor retornado pela leitura do sensor

leituraFinal_luz = leituraBruta_luz.replace(
    "[", " ").replace("]", " ").replace('"', " ").strip()
# trata a string para leitura como int

leitura_led = requests.get(
    'http://'+blynk_server+'/'+auth_token+'/get/'+led)
# executa leitura do valor atual do LED

leituraBruta_led = leitura_led.text

leituraFinal_led = leituraBruta_led.replace(
    "[", " ").replace("]", " ").replace('"', " ").strip()
# trata a string para leitura como int

if int(leituraFinal_luz) < 100:

    if int(leituraFinal_led) != 255:
        time.sleep(4)
        controle_led = requests.get(
            'http://'+blynk_server+'/'+auth_token+'/update/'+led+'?value=255')
        # acende o LED
    mensagem_luz_baixa = requests.post(notifica, json=msg_baixa)  # envia notificacao com mensagem pré-selecionada

else:
    time.sleep(4)
    if int(leituraFinal_led) != 0:
        controle_led = requests.get(
            'http://'+blynk_server+'/'+auth_token+'/update/'+led+'?value=0')
        # apaga o LED
    mensagem_luz_alta = requests.post(notifica, json=msg_alta)

   
