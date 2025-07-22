const int bluePin = 7;
const int greenPin = 4;

void setup() {
  Serial.begin(9600);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);

}

void loop() {
  if (Serial.available() > 0){

    String msg = Serial.readString();

    if (msg == "on"){
      digitalWrite(greenPin, HIGH);
    }

    else if (msg == "close"){
         digitalWrite(greenPin, LOW);
      }
      
    else{
      
      for (int i=0; i<5; i++){
          digitalWrite(bluePin, HIGH);
          delay(100);
          digitalWrite(bluePin, LOW);
          delay(100);
        }
     }
  }
}
