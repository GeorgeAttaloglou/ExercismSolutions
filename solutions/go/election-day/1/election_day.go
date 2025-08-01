package electionday
import ("fmt")

//type ElectionResult struct{
//    Name string
//    Votes int
//}

// NewVoteCounter returns a new vote counter with
// a given number of initial votes.
func NewVoteCounter(initialVotes int) *int {
    var returnIntPointer *int
    returnIntPointer = &initialVotes

    return returnIntPointer
}

// VoteCount extracts the number of votes from a counter.
func VoteCount(counter *int) int {
    if counter == nil{
        return 0
    }else{
        return *counter
    }
}

// IncrementVoteCount increments the value in a vote counter.
func IncrementVoteCount(counter *int, increment int) int{
    *counter += increment
    return *counter
}

// NewElectionResult creates a new election result.
func NewElectionResult(candidateName string, votes int) *ElectionResult {
    var e *ElectionResult
    e = &ElectionResult{Name: candidateName, Votes: votes}
    return e
}

// DisplayResult creates a message with the result to be displayed.
func DisplayResult(result *ElectionResult) string {
    return fmt.Sprint(result.Name, " (", result.Votes, ")")
}

// DecrementVotesOfCandidate decrements by one the vote count of a candidate in a map.
func DecrementVotesOfCandidate(results map[string]int, candidate string) {
	results[candidate] -= 1
}
