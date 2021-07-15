# greenpi
Projeto para a disciplina de PCS3100 da Escola Politécnica da USP

O Green Pi consiste em uma ferramenta de monitoramento de pequenas plantações, focada em pequenos agricultores.
A prototipagem do software foi feita utilizando Blynk e uma simulação de ambiente IoT em Pyhton, enquanto a parte de hardware foi feita utilizando Arduino.

A prototipagem do nosso software foi feita utilizando-se do aplicativo Blynk e linguagem Python, ademais são utilizadas funções da biblioteca requests, que faz 
requisições http ao blynk. Isso nos garante que, para fins de simulação, as requisições poderiam ser feitas individualmente pelo token de autenticação de cada 
"cliente" individualmente. Para mais detalhes das requisições ao Blynk via http, consulte: https://blynkapi.docs.apiary.io
