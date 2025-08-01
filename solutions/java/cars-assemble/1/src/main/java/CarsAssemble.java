public class CarsAssemble {

    public static double productionRatePerHour(double speed) {
        double productionRate = 0;
        if (speed >= 1 && speed <= 4){
            productionRate = speed * 221;
        }
        else if (speed > 4 && speed <= 8){
            productionRate = (speed * 221) * 90/100;
        }
        else if (speed == 9){
            productionRate = (speed * 221) * 80/100;
        }
        else if (speed == 10){
            productionRate = (speed * 221) * 77/100;
        }
        return productionRate;
    }

    public int workingItemsPerMinute(double speed) {
        double perMinute = CarsAssemble.productionRatePerHour(speed) / 60;
        return (int)perMinute;
    }
}
