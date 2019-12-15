const uint8_t reply[4] = {0xF0, 0x40, 0x20, 0x00};

struct Pressure
{
  float Systolic;
  float Diastolic;
};

Pressure MakePressureMeasure()
{
  Pressure res;
  res.Systolic = random(90, 140);
  do
    res.Diastolic = random(60, 120);
  while(res.Diastolic > res.Systolic);

  return res;
}

float MakeTemperatureMeasure()
{
  return random(350, 400)/10.0;
}

float MakePulseMeasure()
{
  return random(45, 80);
}

void setup() {
  
  pinMode(13, OUTPUT);
  pinMode(A1, INPUT);
  randomSeed(analogRead(A1)*10);
  Serial.begin(9600);
}

void Blink()
{
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
  delay(500);
}

void loop() {
  Blink();
  if(Serial.available() > 0)
  {
    byte keyByte = Serial.read();
    if(keyByte == 0x0F){
      keyByte = Serial.read();
      if(keyByte == 0xAF){
        keyByte = Serial.read();
        if(keyByte == 0xCF){
          keyByte = Serial.read();
          if(keyByte == 0xFF)
          {
            Serial.write(reply, 4);
            
            float temperature = MakeTemperatureMeasure();
            Serial.write((byte*)&temperature, 4);
            float pulse = MakePulseMeasure();
            Serial.write((byte*)&pulse, 4);
            Pressure pressure = MakePressureMeasure();
            float* systolic  = &pressure.Systolic;
            float* diastolic = &pressure.Diastolic;
            Serial.write((byte*)systolic, 4);
            Serial.write((byte*)diastolic, 4);
          }
        }
      }
    }
  }
}
