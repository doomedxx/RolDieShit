#ifndef GENERIC_H
#define GENERIC_H
// Light sensor is connected to port A0.
#define lightPort 0

// Temperature sensor is connected to A1.
// Using 3.3 volt as power source.
#define temperaturePort 1
#define temperatureVoltage 3.3

// Motor ports (block D)
#define screenClosePort 5
#define screenBusyPort 4
#define screenOpenPort 3

// Ultrasonic sensor ports (block B)
#define ultrasonicTriggerPort 1
#define ultrasonicEchoPort 0

// Commands for module > server
#define msLightCmd 1
#define msTemperatureCmd 2
#define msScreenStateLightCmd 3
#define msScreenStateTemperatureCmd 4

// Commands for server > module
#define smNoCommand -1
#define smMinMaxSensorLightCmd 1
#define smMinMaxScreenLightCmd 2
#define smMinMaxSensorTemperatureCmd 3
#define smMinMaxScreenTemperatureCmd 4
#define smScreenStateLightCmd 5
#define smScreenStateTemperatureCmd 6
#define smScreenForceClose 0
#define smScreenForceOpen 1
#define smScreenForceOff 2

// Values for TTC scheduler
#define ttc60Seconds 6000
#define ttc40Seconds 4000
#define ttc30Seconds 3000
#define ttc1Second 100

// Wrapper for light sensor
typedef union {
	uint16_t value;
	uint8_t bytes[2];
} Light;

// Wrapper for temperature sensor
typedef union {
	int value;
	uint8_t bytes[2];
} Temperature;

// Wrapper for distance
typedef union {
	uint16_t value;
	uint8_t bytes[2];
} Distance;

// Wrapper for server command.
typedef struct {
	int8_t command;
	uint8_t valueA1;
	uint8_t valueA2;
	uint8_t valueB1;
	uint8_t valueB2;
} ServerCommand;
#endif
