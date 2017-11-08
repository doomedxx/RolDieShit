#include "lightsensor.h"
// declare light object
Light light;

Light readLight(void)
{
	ADMUX |= _BV(MUX0);
	ADCSRA |= _BV(ADSC);
	loop_until_bit_is_clear(ADCSRA, ADSC);
	
	float lightLevel = (float)ADCW / 1024 * 100;
	light.value = (int) lightLevel
	return light;
}

//transmit the temp to python in 2 bytes
void transmitLight(Light light)
{
	transmit((Uint8_t)2);
	transmit(light.bytes[0]);
	transmit(light.bytes[1]);
}

//send actual light percentage to the transmit function
void sendLight(void)
{
	Light light = readLight();
	transmitLight(light);
}