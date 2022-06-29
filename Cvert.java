import javax.imageio.ImageIO;
import java.io.File;
// import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.lang.Math;
// import java.lang.Integer;

public class Cvert {
    public static void main(String[] args) {
        try {
            File file = new File(args[0]);
            BufferedImage image = ImageIO.read(file);
            double wid = Math.ceil(image.getWidth() / 3);
            double heg = Math.ceil(image.getHeight() / 3);
            BufferedImage res = new BufferedImage((int)wid, (int)heg, image.getType());

            for (int x = 0;  x < res.getWidth(); x++) {
                for (int y = 0; y < res.getHeight(); y++) {
                    res.setRGB(x, y, image.getRGB(x * 3, y * 3));
                }
            }

            int znach[][] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
            int k = 0;
            while (k < 11) {
                System.out.println("Iteretion: " + k);
                k++;
                for (int x = 0;  x < res.getWidth(); x++) {
                    for (int y = 0; y < res.getHeight(); y++) {
                        res.setRGB(x, y, image.getRGB(x * 3, y * 3));
                    }
                }
            }

            File cvert = new File("cvert.jpg");
            ImageIO.write(res, "jpg", cvert);

        } catch (IOException e) {
            System.out.println("Can't read or save");
        }
    }
}