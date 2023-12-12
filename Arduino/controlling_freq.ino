
#include <Wire.h>
#include "Haptic_Driver.h"

Haptic_Driver hapticDriver;


int event = 0;

void setup() {

  Wire.begin();
  Serial.begin(115200);

  if ( !hapticDriver.begin())
    Serial.println("Could not communicate with Haptic Driver.");
  else
    Serial.println("Qwiic Haptic Driver DA7280 found!");

  if ( !hapticDriver.defaultMotor() )
    Serial.println("Could not set default settings.");

  // Frequency tracking is done by the IC to ensure that the motor is hitting
  // its resonant frequency. I found that restricting the PCB (squeezing)
  // raises an error which stops operation because it can not reach resonance.
  // I disable here to avoid this error.
  hapticDriver.enableFreqTrack(false);

  Serial.println("Setting I2C Operation.");
  hapticDriver.setOperationMode(DRO_MODE);
  Serial.println("Ready.");

  delay(1000);

  hapticSettings settings = hapticDriver.getSettings(); // Get the current settings
  settings.lraFreq = 1; // Modify the lrafreq member
  hapticDriver.setMotor(settings);

}

void loop()
{

  //If uploading often the Haptic Driver IC will throw a fault. Let's
  //clear that error (0x10), just in case.
  event = hapticDriver.getIrqEvent();
  Serial.print("Interrupt: ");
  Serial.println(event, HEX);
  Serial.println("Clearing event.");
  hapticDriver.clearIrq(event);
  // Vibrate the motor for 3 seconds
  hapticDriver.setVibrate(25);
  delay(500);
  hapticDriver.setVibrate(0);
  delay(500);
}
