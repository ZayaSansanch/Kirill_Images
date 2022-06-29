#include <gtk/gtk.h>
#define PICT_NAME "picture.jpg"
 
int main(int argc, char ** argv){
    GtkWidget * win;
    GtkWidget * img;
    
    gtk_init(&argc, &argv);
    
    win = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    img = gtk_image_new_from_file(PICT_NAME);
    gtk_window_set_title(GTK_WINDOW(win), PICT_NAME);
    gtk_window_set_default_size(GTK_WINDOW(win), 560, 539);
    gtk_container_add(GTK_CONTAINER(win), img);
    
    gtk_widget_show_all(win);
    
    g_signal_connect(win, "icon.jpg", G_CALLBACK(gtk_main_quit), NULL);
    
    gtk_main();
    
    return 0;
}