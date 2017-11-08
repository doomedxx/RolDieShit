#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#include <util/delay.h>
#include "AVR_TTC_scheduler.c"
#include "analog_io.h"
#include "analog_io.c"
#include "init.c"
#include "tempsensor.c"
#include "rollunit.c"
#include "command.c"

//int max_rollout = 40;
int min_rollout;
int min_temp;
int max_temp;
int roll_to;
//int distance = 0;

void transmit(uint8_t data){
	//UDRE is set when the transmit buffer is empty
	loop_until_bit_is_set
	(UCSR0A , UDRE0);
	//send the data
	UDR0 = data;
}

int main(void){
	init_adc();
	uart_init();
	port_init();
	SCH_Init_T1();
	//start scheduler 
	SCH_Start();
	//add tasks to schedular(max 5) 100ms timer voor testen, hoort 4000 te worden.
	//SCH_Add_Task(getTemp, 0, 100 );
	SCH_Add_Task(getCommand, 0, 100);
	SCH_Add_Task(executeCommand, 0,  100);
	SCH_Add_Task(sendTemperature, 0, 100);
	while(1){
		//keep dispatching tasks while running.
		SCH_Dispatch_Tasks();
	}
}