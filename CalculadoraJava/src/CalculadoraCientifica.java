import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraCientifica extends JFrame implements ActionListener {
    private JTextField display;
    private JPanel panel;
    private boolean scientificMode = false;

    public CalculadoraCientifica() {
        setTitle("Calculadora Científica");
        setSize(400, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        display = new JTextField();
        display.setEditable(false);
        display.setFont(new Font("Arial", Font.PLAIN, 24));
        add(display, BorderLayout.NORTH);

        panel = new JPanel();
        panel.setLayout(new GridLayout(5, 4, 10, 10));
        add(panel, BorderLayout.CENTER);

        String[] basicButtons = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        };

        for (String text : basicButtons) {
            addButton(panel, text);
        }

        JButton scientificButton = new JButton("Científica");
        scientificButton.addActionListener(e -> toggleScientificMode());
        add(scientificButton, BorderLayout.SOUTH);
    }

    private void addButton(JPanel panel, String text) {
        JButton button = new JButton(text);
        button.setFont(new Font("Arial", Font.PLAIN, 24));
        button.addActionListener(this);
        panel.add(button);
    }

    private void toggleScientificMode() {
        scientificMode = !scientificMode;
        panel.removeAll();

        String[] basicButtons = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        };

        String[] scientificButtons = {
            "sin", "cos", "tan", "√",
            "log", "ln", "x^y", "!",
            "(", ")", "π", "e"
        };

        for (String text : basicButtons) {
            addButton(panel, text);
        }

        if (scientificMode) {
            for (String text : scientificButtons) {
                addButton(panel, text);
            }
        }

        panel.revalidate();
        panel.repaint();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();
        // Implementar la lógica de la calculadora aquí
        // ...
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            CalculadoraCientifica frame = new CalculadoraCientifica();
            frame.setVisible(true);
        });
    }
}