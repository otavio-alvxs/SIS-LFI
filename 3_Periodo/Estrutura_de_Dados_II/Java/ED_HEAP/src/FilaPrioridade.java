import java.util.PriorityQueue;
/**
 * FilaPrioridade
 */
public class FilaPrioridade {
    public static void main(String[] args) {
        System.out.println("ola mundo");
        PriorityQueue fila = new PriorityQueue<>();
        fila.add(5);
        fila.add(7);
        fila.add(8);
        System.out.println(fila);
        for (int i = 0; i < 4; i++) {
            System.out.print("Atendeu: ");
            System.out.println(fila.remove());
        }
    }
}
