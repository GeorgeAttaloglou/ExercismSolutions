
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        return birdsPerDay;
    }

    public int getToday() {
        return birdsPerDay[birdsPerDay.length - 1];
    }

    public void incrementTodaysCount() {
        birdsPerDay[birdsPerDay.length - 1]++;
    }

    public boolean hasDayWithoutBirds() {
        boolean found = false;
        for (int birds : birdsPerDay){
            if (birds == 0){
                found = true;
            }
        }
        return found;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int count = 0;
        for (int i=0; i<numberOfDays && i<birdsPerDay.length; i++){
            count += birdsPerDay[i];
        }
        return count;
    }

    public int getBusyDays() {
        int count = 0;
        for (int birds : birdsPerDay){
            if (birds >= 5){
                count++;
            }
        }
        return count;
    }
}