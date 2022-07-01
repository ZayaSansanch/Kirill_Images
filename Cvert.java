import javax.imageio.ImageIO;
import java.io.File;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.lang.Math;

public class Cvert {

    public static void main(String[] args) {
        /*
         * Variations
        */
        String OPF = args[0];
        String SFN;
        // OFN = opening file name; SFN = saving file name;
        
        /*
         * for for any manes finishing files and any mnojetel in iteretionFunction();
         */
        for (int i = 0; i < 11; i++) {
            Cvert cvert = new Cvert();
            cvert.iteretionFunction(OPF, "finished/" + i + ".jpg", i);
        }
    }
    
    /*
     * Functions for any finish with any String SFN, int factor;
     */
    void iteretionFunction(String OFN, String SFN, int factor) {
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

            for (int x = 0;  x < res.getWidth(); x++) {
                for (int y = 0; y < res.getHeight(); y++) {
                    if (
                        (y > 0 & y < res.getHeight() - 1) &
                        (x > 0 & x < res.getWidth() - 1)
                    ) {
                        res.setRGB(x - 1, y - 1, res.getRGB(x - 1, y - 1));    res.setRGB(x - 1, y, res.getRGB(x - 1, y));    res.setRGB(x - 1, y + 1, res.getRGB(x - 1, y + 1)); 
                        res.setRGB(x, y - 1,     res.getRGB(x, y - 1));        res.setRGB(x, y,     res.getRGB(x, y));        res.setRGB(x, y + 1,     res.getRGB(x, y + 1)); 
                        res.setRGB(x + 1, y - 1, res.getRGB(x + 1, y - 1));    res.setRGB(x + 1, y, res.getRGB(x + 1, y));    res.setRGB(x + 1, y + 1, res.getRGB(x + 1, y + 1)); 
                    }
                }
            }

            File cvert = new File(SFN);
            ImageIO.write(res, "jpg", cvert);
        } catch (IOException e) {
            System.out.println("Can't read or save");
        }
    }
}