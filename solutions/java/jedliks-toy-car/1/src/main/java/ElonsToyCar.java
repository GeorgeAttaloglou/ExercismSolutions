public class ElonsToyCar {

    private int meters;
    private int battery = 100;
    
    public static ElonsToyCar buy() {
        return new ElonsToyCar();
    }

    public String distanceDisplay() {
        return String.format("Driven %d meters", meters);
    }

    public String batteryDisplay() {
        if (battery > 0){
            return String.format("Battery at %d%%", battery);
        }else{
            return "Battery empty";
        }
    }

    public void drive() {
        if (battery > 0) {
            meters += 20;
            battery -= 1;
        }
    }
}
