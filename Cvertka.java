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
            BufferedImage source = ImageIO.read(file);

            // Создаем новое пустое изображение, такого же размера
            BufferedImage result = new BufferedImage(source.getWidth(), source.getHeight(), source.getType());

            // Делаем двойной цикл, чтобы обработать каждый пиксель
            for (int x = 0; x < source.getWidth(); x++) {
                for (int y = 0; y < source.getHeight(); y++) {
            
                }
            }
        }
        catch {
            System.out.print("Fatal error:");
            System.out.print("Неудается открыть или сохранить файл");
        }
    }
}