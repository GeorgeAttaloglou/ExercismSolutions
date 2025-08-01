class Badge {
    public String print(Integer id, String name, String department) {
        String idFinal = id == null ? null : "[" + id + "]";
        
        if (id == null) {
            return name + " " + "-" + " " + (department != null ? department.toUpperCase() : "OWNER");
        } else if (department == null) {
            return idFinal + " " + "-" + " " + name + " " + "-" + " " + "OWNER";
        } else {
            return idFinal + " " + "-" + " " + name + " " + "-" + " " + department.toUpperCase();
        }
    }
}
