#include "tempsensor.h"
// declare temperature object
Temperature temperature;

// read out the temp from sensor (nog steeds gekke waardes.)
Temperature readtemp(void){
	ADMUX &= ~_BV(MUX0); // Set channel point to port 0
	ADCSRA |= _BV(ADSC); // Start adc measurement
	loop_until_bit_is_clear(ADCSRA, ADSC); // proceed when done
	float celsius = ((ADCW * 5000 / 1024) - 500) / 10;
	temperature.value = (int)celsius;
	return temperature;
}

// transmit the temp to python in 2 bytes
void transmitTemp(Temperature temperature){
	transmit((uint8_t)2);
	transmit(temperature.bytes[0]);
	transmit(temperature.bytes[1]);
}

// send the actual temp to the transmit function
void sendTemperature(void){
	Temperature temperature = readtemp();
	transmitTemp(temperature);
}