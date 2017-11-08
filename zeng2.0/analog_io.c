#include <avr/io.h>
#include "analog_io.h"

// Get the current value for the given analog port.
// Port should be the analog port index (between 0 and 7).
uint16_t aIoRead(uint8_t port)
{
	port &= 0b00000111;
	ADMUX = (ADMUX & 0xF8) | port;
	ADCSRA |= (1 << ADSC);

	while (ADCSRA & (1 << ADSC));

	return ADC;
}
