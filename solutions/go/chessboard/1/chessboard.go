package chessboard

// Declare a type named File which stores if a square is occupied by a piece - this will be a slice of bools

type File []bool

// Declare a type named Chessboard which contains a map of eight Files, accessed with keys from "A" to "H"

type Chessboard map[string]File
//cb = {"A": [0,1,1,0], "B": [0,0,0,0]}

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file.
func CountInFile(cb Chessboard, file string) int {
    counter := 0

    currentFile := cb[file]
    for _, val := range currentFile{
        if val == true{counter ++}
    }
    return counter
}

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank.
func CountInRank(cb Chessboard, rank int) int {
    if (rank < 1 || rank > 8){return 0}
    counter := 0

    for _, file := range cb{
        if (file[rank - 1] == true){
            counter ++
        }
    }
    return counter
}

// CountAll should count how many squares are present in the chessboard.
func CountAll(cb Chessboard) int {
    counter := 0
    for _, squares := range cb{
        for _, value := range squares{
            if value == true || value == false {counter++}
        }
    }
    return counter 
}

// CountOccupied returns how many squares are occupied in the chessboard.
func CountOccupied(cb Chessboard) int {
    counter := 0
    for fileName, _ := range cb{
        counter += CountInFile(cb, fileName)
    }
    return counter
}
