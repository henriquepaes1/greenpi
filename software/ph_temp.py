from pip._vendor import requests
import random  # biblioteca que gera numeros pseudoaleatorios
import time  # biblioteca para controle de tempo
while(True):

    # Gera valores pseudoaleatorios para ph (simulacao IoT)
    ph = 7 + random.randint(-1, 1)
    url = 'http://blynk-cloud.com/2NLtjZavPi2EoqCN-Txn1PF3zCRn9VFp/update/V1?value=' + \
        str(ph)  # define o endereco do display para pH
    leitura_ph = requests.get(url)  # atualiza o valor do display de ph

    # simulacao IoT de temperatura
    temp = 25 + random.randint(1, 3) - random.randint(1, 3)
    url_t = 'http://blynk-cloud.com/2NLtjZavPi2EoqCN-Txn1PF3zCRn9VFp/update/V3?value=' + \
        str(temp)  # display dos valores de temperatura
    # atualiza o valor do display de temperatura
    leitura_temp = requests.get(url_t)

    umidade = 85 + random.randrange(1, 7) - random.randrange(1, 7)
    url_u = 'http://blynk-cloud.com/2NLtjZavPi2EoqCN-Txn1PF3zCRn9VFp/update/V4?value=' + \
        str(umidade)  # endereco do display de umidade
    leitura_umi = requests.get(url_u)  # atualiza o valor do display de umidade
    
    time.sleep(2)  # aguarda 2 segundos antes da proxima iteração

