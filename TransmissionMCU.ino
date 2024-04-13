#define E2END 1023 
void write_to_eeprom(int add, byte val) {
  while (EECR & (1 << EEPE)) {} 
  EEAR = add; 
  EEDR = val;
  EECR |= (1 << EEMPE); 
  EECR |= (1 << EEPE); 
}


byte read_to_eeprom(int add) {
  while (EECR & (1 << EEPE)) {} 
  EEAR = add; 
  EECR |= (1 << EERE); 
  return EEDR; 
}

void setup() {
  Serial.begin(2400);
}

void loop() {
  if (Serial.available() > 0) {
    
    String receivedData = Serial.readStringUntil('\n'); 
    
    
    int strLength = receivedData.length();
    
    
    int address = 0; 
    for (int i = 0; i < strLength; i++) {
      write_to_eeprom(address + i, receivedData[i]);
    }
    
    
    Serial.println(receivedData);
    
    
    delay(100);
  }

  
  if (Serial.available() > 0) {
    int startAddress = Serial.parseInt();
    int strLength = Serial.parseInt();
    
    
    String storedData = "";
    for (int i = 0; i < strLength; i++) {
      char ch = read_to_eeprom(startAddress + i);
      storedData += ch;
    }
    Serial.print(storedData);
    

    delay(100);
  }
}