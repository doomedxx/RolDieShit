#include <avr/io.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>
#include <stdlib.h>
#include <stdio.h>
uint8_t command;


uint8_t receive(){
	loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

void getCommand(){
	command = receive(); 
}

void executeCommand(){
	if(command ==0x1){
		rollOut();
		command = 0x00;		
	}
	else if(command == 0x2){
		rollIn();
		command = 0x00;	
	}	
}
/*
0x01
rollOut();
0x02
rollIn();
0x03
Set_maxdistance();
0x04
set_maxtemp();
0x05
set_mintemp();
0x06
set_max_light();
0x07
set_min_light();
*/