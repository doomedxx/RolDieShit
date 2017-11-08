#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#include <util/delay.h>
// output on USB = PD1 = board pin 1
// datasheet p.190; F_OSC = 16 MHz & baud rate = 19.200
#define UBBRVAL 51

// initiate Arduino for transmitting over serial
void uart_init(){
	//set the baud rate
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	//disable U2X mode
	UCSR0A  = 0;
	//enable transmitter
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	//set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C  = _BV(UCSZ01)|_BV(UCSZ00);
}

// initiate analog sensor(temp)
void init_adc(){
	// ref= Vcc, left adjust the result (8 bit resolution),
	// select channel 0 (PC0 = input)
	ADMUX = (1<<REFS0)|(1<<ADLAR);
	// enable the ADC & prescale = 128
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}

// init ports for the LED's
void port_init(void){
	DDRB |= _BV(DDB5);   //rode led
	DDRB |= _BV(DDB4);   //gele led
	DDRB |= _BV(DDB3);   //groene led

}