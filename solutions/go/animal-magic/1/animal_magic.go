package chance

import (
    "math/rand"
)

// RollADie returns a random int d with 1 <= d <= 20.
func RollADie() int {
    diceResult := rand.Intn(20)
    if diceResult == 0{
        return 1
    }
    return diceResult
}

// GenerateWandEnergy returns a random float64 f with 0.0 <= f < 12.0.
func GenerateWandEnergy() float64 {
    floatNum := rand.Float64() * float64(12)
    return floatNum
}

// ShuffleAnimals returns a slice with all eight animal strings in random order.
func ShuffleAnimals() []string {
    animals := []string{"ant", "beaver", "cat", "dog", "elephant", "fox", "giraffe", "hedgehog"}
    rand.Shuffle(len(animals), func(i, j int){
        animals[i], animals[j] = animals[j], animals[i]
    })
    return animals
}
