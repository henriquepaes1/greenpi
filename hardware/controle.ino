/*
    Projeto Green-PI - Código de Prototipagem

    Conexões básicas utilizadas:

    1) Sensor de lumiosidade: porta analógica 0 (A0)
    2) Sensor de temperatura (termistor NST): porta analógica 1 (A1)
    3) Potenciômetro (substituto para o sensor de umidade): porta analógica 2(A2)
    4) Buzzer: porta digital 9
    5) 3 Resistores de 10K para a conexão do termistor, so buzzer e do sensor de luz

    Código de auxílio: biblioteca arduino (arduino.org)
    Uso do termistor: https://www.filipeflop.com/blog/termistor-ntc-arduino/
*/


// Conexão do termistor
const int pinTermistor = A1;

// Parâmetros do termistor
const double beta = 3600.0;
const double r0 = 10000.0;
const double t0 = 273.0 + 25.0;
const double rx = r0 * exp(-beta / t0);

// Parâmetros do circuito
const double vcc = 5.0;
const double R = 20000.0;

// Numero de amostras na leitura
const int nAmostras = 5;

int pinoSensorLuz = A0;
int pinoUmi = A2;

int valorLuz = 0;
float umidade = 0;
float temperatura = 0;


void setup() {
  Serial.begin(9600); /* abre a porta serial a 9600 bps. */
  Serial.println("Green PI - Sistema de Moniitoramento");
  Serial.println("Boas vindas! Como estao as condicoes: ");
  pinMode(9, OUTPUT);
}

void loop() {
  Serial.println("");

  valorLuz = analogRead(pinoSensorLuz);
  umidade = analogRead(pinoUmi);
  umidade = map(umidade, 0, 1023, 0, 100);

  // Le o sensor de temperatura algumas vezes
  int soma = 0;
  for (int i = 0; i < nAmostras; i++) {
    soma += analogRead(pinTermistor);
    delay (10);
  }

  // Determina a resistência do termistor
  double v = (vcc * soma) / (nAmostras * 1024.0);
  double rt = (vcc * R) / v - R;

  // Calcula a temperatura
  double t = beta / log(rt / rx);


  Serial.print("Temperatura (C): ");
  Serial.println(t - 273.0);

  Serial.print("Umidade (%): ");
  Serial.println(umidade);

  Serial.print("Luminosidade: ");
  Serial.println(valorLuz);

  if (valorLuz <= 700 && valorLuz >= 500)
    Serial.println("Luminosidade adequada");
  else if (valorLuz < 500)
    Serial.println("Luminosidade baixa");
  else
    Serial.println("Luminosidade alta");

  if (valorLuz > 700 && (t - 273.0))
    tone(9, 400);
  delay(5000);
  Serial.println("Grave risco de incênio");

  noTone(9);

  delay(10000);
}
