public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven(){
        int time = 40;
        return time;
    }

    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int timeCooking){
        int remainingTime = 40 - timeCooking;
        return remainingTime;
    }

    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int numberOfLayers){
        int preperationTime = numberOfLayers * 2;
        return preperationTime;
    }

    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int numOfLayers, int minsCooking){
        int totalTime = numOfLayers*2 + minsCooking;
        return totalTime;
    }
}
