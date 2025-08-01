package lasagna

// TODO: define the 'PreparationTime()' function
// DONE
func PreparationTime(layers []string, timeToPrep int) int {
    if timeToPrep == 0 {
        return len(layers) * 2
    }else{return len(layers) * timeToPrep} 
}

// TODO: define the 'Quantities()' function
// DONE
func Quantities(layers []string) (noodles int, sauce float64) {
    noodles = 0
    sauce = 0.0
    
    for i := 0; i < len(layers); i++ {
        if layers[i] == "noodles"{
            noodles += 50
        }else if layers[i] == "sauce"{
            sauce += 0.2
        }
    }
    return
}

// TODO: define the 'AddSecretIngredient()' function
// DONE
func AddSecretIngredient(friendsList []string, myList []string) {
    lastOfFriendsList := friendsList[len(friendsList)-1]
    myList[len(myList) - 1] = lastOfFriendsList 
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(amounts []float64, portionsWanted int) []float64{
 	newQuantities := make([]float64, len(amounts))
    
	for i := 0; i < len(amounts); i++ {
		newQuantities[i] = amounts[i] * float64(portionsWanted) / 2
	}
    
	return newQuantities
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
// 
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more 
// functionality.
