import javax.imageio.ImageIO;
import java.io.File;
import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.awt.*;
import java.applet.*;

public class Cvertka {
    public static void main(String[] args) {
        try {
            File file = new File(args[0]);
            BufferedImage image = ImageIO.read(file);

            BufferedImage ResBW = new BufferedImage(image.getWidth(), image.getHeight(), image.getType());
            BufferedImage Resdown = new BufferedImage(image.getWidth(), image.getHeight(), image.getType());
            BufferedImage Resup = new BufferedImage(image.getWidth(), image.getHeight(), image.getType());

            for (int x = 0; x < image.getWidth(); x++) {
                for (int y = 0; y < image.getHeight(); y++) {
                    Color color = new Color(image.getRGB(x, y));

                    int blue = color.getBlue();
                    int red = color.getRed();
                    int green = color.getGreen();

                    int grey = (int) (red * 0.299 + green * 0.587 + blue * 0.114);

                    int newRed = grey;
                    int newGreen = grey;
                    int newBlue = grey;

                    Color newColor = new Color(newRed, newGreen, newBlue);

                    ResBW.setRGB(x, y, newColor.getRGB());
                }
            }

            int black = new Color(100, 100, 100).getRGB();
            int black2 = new Color(255, 255, 255).getRGB();

            for (int x = 0; x < image.getWidth(); x++) {
                for (int y = 0; y < image.getHeight(); y++) {
                    Resdown.setRGB(x, y, ResBW.getRGB(x, y));
                    Resup.setRGB(x, y, ResBW.getRGB(x, y));
                }
            }
            
            for (int x = 0; x < image.getWidth(); x++) {
                for (int y = 0; y < image.getHeight(); y++) {
                    if (Resdown.getRGB(x, y) < black) {
                        Resdown.setRGB(x, y, black2);
                    }

                    // Color color = new Color(image.getRGB(x, y));
                    // int red = color.getRed();
                    // int green = color.getGreen();
                    // int grey = (int) (red * 0.299 + green * 0.587 + blue * 0.114);
                    // int newRed = grey;
                    // int newGreen = grey;
                    // int newBlue = grey;
                    // Color newColor = new Color(newRed, newGreen, newBlue);
                    // ResBW.setRGB(x, y, newColor.getRGB());
                }
            }

            File BW = new File("BW.jpg");
            ImageIO.write(ResBW, "jpg", BW);

            File BWdown = new File("BWdown.jpg");
            ImageIO.write(Resdown, "jpg", BWdown);

            File BWup = new File("BWup.jpg");
            ImageIO.write(Resup, "jpg", BWup);

        } catch (IOException e) {
            System.out.println("Can't read or save");
        }
    }
}