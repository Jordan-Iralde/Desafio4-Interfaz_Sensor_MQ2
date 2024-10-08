const int MQ2_ANA = A1;
const int MQ2_DIG = 2;
const int ledPin1 = 8; //Led Verde
const int ledPin2 = 9; //Led Amarillo
const int ledPin3 = 10; //Led ROjo

void setup() {
    // coloca tu código de configuración aquí, para que se ejecute una vez:
    Serial.begin(9600);
    pinMode(MQ2_ANA, INPUT);
    pinMode(MQ2_DIG, INPUT);

  pinMode(ledPin1, OUTPUT); //Verde
  pinMode(ledPin2, OUTPUT); //Amarillo
  pinMode(ledPin3, OUTPUT); //Rojo
}

void loop() {
    /*
    Verde: Lectura < 200 (aire limpio)
    Amarillo: 200 ≤ Lectura < 400 (aire moderadamente contaminado)
    Rojo: Lectura ≥ 400 (aire altamente contaminado)
    coloca tu código principal aquí, para que se ejecute repetidamente:
    La lectura digital imprime 1 si hay mas gas que aire limpio
    La lectura analogica
    */
    int mappedValue = map(analogRead(MQ2_ANA), 0, 1023, 0, 600);
    //esto de MappedValue es para asignarle un nuevo limite, que es 600

    Serial.print("Analógico: ");
    Serial.print(mappedValue);
    Serial.print("\n");

    if ((digitalRead(MQ2_DIG)) == 1){
        Serial.println("Existe mas Gas que Aire limpio (1) \n");
    } else  {
        Serial.println("Existe mas Aire limpio que Gas (0) \n");
    }
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, LOW);

    if (mappedValue < 200){
        digitalWrite(ledPin1, HIGH);
        Serial.println("No hay mucho Gas");
    } else if (200 <= mappedValue && mappedValue < 400){
        digitalWrite(ledPin2, HIGH);
        Serial.println("Hay casi tanto Gas como Aire limpio");
    } else{
        digitalWrite(ledPin3, HIGH);
        Serial.println("Hay Demasiado Gas");
    }
    delay(1000);
}