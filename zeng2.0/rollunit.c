#define F_CPU 16E6
#include <avr/io.h>
#include <util/delay.h>
#define BLINK_DELAY_MS 200
// Open the screen if not already opened.
int distance = 8;
int maxDistance = 10;
int minDistance = 1;

void OpenScreen(uint16_t maxDistance)
{
		PORTB |= _BV(PORTB5);			// rode led gaan aan
		if(distance < maxDistance){
			PORTB |= _BV(PB3);           //gele led knippert bij normaal licht
			_delay_ms(BLINK_DELAY_MS);
			PORTB &= ~_BV(PB3);
			_delay_ms(BLINK_DELAY_MS);
			distance = distance +1;
			if (distance == maxDistance){
				PORTB &= ~_BV(PORTB5);
				//command = 1;
			}
		}	
}
//Sluit het rolluit aan de hand van 

void closeScreen(uint16_t minDistance)
{
		PORTB |= _BV(PORTB4);			// groene led gaan aan
		if(distance <= maxDistance){
			PORTB |= _BV(PB3);           //gele led knippert bij normaal licht
			_delay_ms(BLINK_DELAY_MS);
			PORTB &= ~_BV(PB3);
			_delay_ms(BLINK_DELAY_MS);
			distance = distance -1;
			if (distance == minDistance){
				PORTB &= ~_BV(PORTB4);
				//command = 2;
			}
		}
}

void rollOut(void){
	OpenScreen(maxDistance);
}

void rollIn(void){
	closeScreen(minDistance);
}
