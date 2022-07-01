import javax.imageio.ImageIO;
import java.io.File;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.lang.Math;

public class Cvert {
    void iteretionFunction(String OFN, String SFN, int num) {
        // OFN = opening file name; SFN = saving file name;
        try {
            File file = new File(OFN);
            BufferedImage image = ImageIO.read(file);
            double wid = Math.ceil(image.getWidth() / 3);
            double heg = Math.ceil(image.getHeight() / 3);
            BufferedImage res = new BufferedImage((int)wid, (int)heg, image.getType());

            for (int x = 0;  x < res.getWidth(); x++) {
                for (int y = 0; y < res.getHeight(); y++) {
                    res.setRGB(x, y, image.getRGB(x * 3, y * 3));
                }
            }

            int[][] znach = {
                {0, 0, 0}, 
                {0, 0, 0}, 
                {0, 0, 0}
            };

            int k = 0;
            while (k < 1) {
                System.out.println("Iteretion: " + k);
                k++;
                for (int x = 0;  x < res.getWidth(); x++) {
                    for (int y = 0; y < res.getHeight(); y++) {
                        if (
                            (y > 0 & y < res.getHeight() - 1) &
                            (x > 0 & x < res.getWidth() - 1)
                        ) {
                            znach[0][0] = res.getRGB(x - 1, y - 1);    znach[0][1] = res.getRGB(x - 1, y);    znach[0][2] = res.getRGB(x - 1, y + 1); 
                            znach[1][0] = res.getRGB(x, y - 1);        znach[1][1] = res.getRGB(x, y);        znach[1][2] = res.getRGB(x, y + 1);
                            znach[2][0] = res.getRGB(x + 1, y - 1);    znach[2][1] = res.getRGB(x + 1, y);    znach[2][2] = res.getRGB(x + 1, y + 1);

                            for (byte mx = 0; mx < 3; mx++) {
                                for (byte my = 0; my < 3; my++) {
                                    if (mx != 1 & my != 1) {
                                        znach[mx][my] *= -1;
                                    } else {
                                        znach[mx][my] *= num;
                                    }
                                }
                            }

                            res.setRGB(x - 1, y - 1, znach[0][0]);    res.setRGB(x - 1, y, znach[0][1]);    res.setRGB(x - 1, y + 1, znach[0][2]); 
                            res.setRGB(x, y - 1, znach[1][0]);    res.setRGB(x, y, znach[1][1]);    res.setRGB(x, y + 1, znach[1][2]); 
                            res.setRGB(x + 1, y - 1, znach[2][0]);    res.setRGB(x + 1, y, znach[2][1]);    res.setRGB(x + 1, y + 1, znach[2][2]); 
                        }
                    }
                }
            }

            File cvert = new File(SFN);
            ImageIO.write(res, "jpg", cvert);

        } catch (IOException e) {
            System.out.println("Can't read or save");
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 11; i++) {
            Cvert cvert = new Cvert();

            cvert.iteretionFunction(args[0], "finished/" + i + ".jpg", i);
        }
    }
}