import javax.imageio.ImageIO;
import java.io.File;
import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.IOException;

public class Cvertka {
    public static void main(String[] args) {
        try {
            // Открываем изображение
            File file = new File(args[0]);
            BufferedImage image = ImageIO.read(file);

            // Создаем новое пустое изображение, такого же размера
            BufferedImage result = new BufferedImage(image.getWidth(), image.getHeight(), image.getType());

            // Делаем двойной цикл, чтобы обработать каждый пиксель
            for (int x = 0; x < image.getWidth(); x++) {
                for (int y = 0; y < image.getHeight(); y++) {
                    // Получаем цвет текущего пикселя
                    Color color = new Color(image.getRGB(x, y));

                    // Получаем каналы этого цвета
                    int blue = color.getBlue();
                    int red = color.getRed();
                    int green = color.getGreen();

                    // Применяем стандартный алгоритм для получения черно-белого изображения
                    int grey = (int) (red * 0.299 + green * 0.587 + blue * 0.114);

                    // Если вы понаблюдаете, то заметите что у любого оттенка серого цвета, все каналы имеют
                    // одно и то же значение. Так, как у нас изображение тоже будет состоять из оттенков серого
                    // то, все канали будут иметь одно и то же значение.
                    int newRed = grey;
                    int newGreen = grey;
                    int newBlue = grey;

                    //  Cоздаем новый цвет
                    Color newColor = new Color(newRed, newGreen, newBlue);

                    // И устанавливаем этот цвет в текущий пиксель результирующего изображения
                    result.setRGB(x, y, newColor.getRGB());
                }
            }

            // Созраняем результат в новый файл
            File output = new File(args[1]);
            ImageIO.write(result, "jpg", output);
        }
        catch (IOException a) {
            System.out.println("Can't read or save file"); // Or something more intellegent
        }
    }
}