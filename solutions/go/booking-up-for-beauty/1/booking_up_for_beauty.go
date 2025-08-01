package booking

import "time"

// Schedule returns a time.Time from a string containing a date.
func Schedule(date string) time.Time {
    returnTime, err := time.Parse("1/2/2006 15:04:05",date)

    if err != nil {
        panic(err)
    }

    return returnTime
}

// HasPassed returns whether a date has passed.
func HasPassed(date string) bool {
	returnTime, err := time.Parse("January 2, 2006 15:04:05",date)

    if err != nil {
        panic(err)
    }
    
	return returnTime.Before(time.Now())
}

// IsAfternoonAppointment returns whether a time is in the afternoon.
func IsAfternoonAppointment(date string) bool {
	returnTime, err := time.Parse("Monday, January 2, 2006 15:04:05",date)

    if err != nil {
        panic(err)
    }

    if returnTime.Hour() >= 12 && returnTime.Hour() < 18 {
        return true
    }else{return false}
}

// Description returns a formatted string of the appointment time.
func Description(date string) string {
	returnTimeString := Schedule(date).Format("You have an appointment on Monday, January 2, 2006, at 15:04.")

    return returnTimeString
}

// AnniversaryDate returns a Time with this year's anniversary.
func AnniversaryDate() time.Time {
	anniversary := time.Date(2024,time.September,15,0,0,0,0,time.UTC)

    return anniversary
}
