unsigned int ledpin = 2;

void setup() {
  pinMode(ledpin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int recv = Serial.read();
    if (recv == 1) {
      digitalWrite(ledpin, HIGH);
    } else if (recv == 2) {
      digitalWrite(ledpin, LOW); 
    }
  }
  delay(100);
}
