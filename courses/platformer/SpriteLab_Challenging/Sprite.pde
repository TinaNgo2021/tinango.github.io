/* Complete this Sprite class as indicated by the comments. */

public class Sprite{
  PImage image;
  float center_x, center_y;
  float change_x, change_y;
  float w, h; // width and height of Sprite(note that w and h are used because
              // width and height are reserved variables for window size.)
  
  public Sprite(String filename, float scale, float x, float y){
    // inititalize variables in this constructor.

    w = image.width * scale;
    
    
  }
  // write constructor with filename and scale parameters only.
  // In the constructor, use this() to call the previous constructor.

  
  
  public void display(){
    // use image(image_file, x, y, width_image, height_image) to draw image.

  }
  public void update(){
    // update position by adding velocity.


  }
}
