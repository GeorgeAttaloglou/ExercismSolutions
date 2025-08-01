package gross

// Units stores the Gross Store unit measurements.
func Units() map[string]int {
	units := make(map[string]int)
    units["quarter_of_a_dozen"] = 3
    units["half_of_a_dozen"] = 6
    units["dozen"] = 12
    units["small_gross"] = 120
    units["gross"] = 144
    units["great_gross"] = 1728

    return units
}

// NewBill creates a new bill.
func NewBill() map[string]int {
	emptyBill := make(map[string]int)

    return emptyBill
}

// AddItem adds an item to customer bill.
func AddItem(bill, units map[string]int, item, unit string) bool {
    measurement, unitExists := units[unit]
    _, itemExists := bill[item]

    if unitExists {
        if itemExists {
            bill[item] += measurement
        } else {
            bill[item] = measurement
        }
        return true
    } else {
        return false
    }
}


// RemoveItem removes an item from customer bill.
func RemoveItem(bill, units map[string]int, item, unit string) bool {
    measurement, unitExists := units[unit]
    _, itemExists := bill[item]

    if itemExists {
        if unitExists {
            if bill[item] - measurement < 0 {
                return false
            } else if bill[item] - measurement == 0 {
                delete(bill, item)
                return true
            } else {
                bill[item] -= measurement
                return true
            }
        }
    }
    return false
}

// GetItem returns the quantity of an item that the customer has in his/her bill.
func GetItem(bill map[string]int, item string) (int, bool) {
	defaultItemValue, itemExists := bill[item]

    if itemExists {
        return bill[item], true
    }
    return defaultItemValue, false
}
