//Package weather provides tools for weather projection.
package weather

//CurrentCondition represents the current weather conditions.
var CurrentCondition string
//CurrentLocation represents the current location being studied.
var CurrentLocation string

//Forecast return a string of the current location and its current condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
