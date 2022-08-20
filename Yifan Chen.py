#!/usr/bin/env python


from gimpfu import *

'''
write the python function to achive filterin
'''

def jazz_poster(file1, file2, file3, file4, file5, str1, font1, str2, font2, str3, font3, radius, amount, value):
       # make a new image
       posterW, posterH = 2480, 3508
       posterImage = gimp.Image(posterW, posterH, RGB)
       gimp.Display(posterImage)
       gimp.message("new image created")
       
       # make the colors
       bColor = gimpcolor.RGB(255, 255, 255)
       fColor = gimpcolor.RGB(0, 0, 0)
       gimp.set_background(bColor)
       gimp.set_foreground(fColor)
       gimp.message("b and f colors made")

       # make background
       backLayer = gimp.Layer(posterImage, "background", posterW, posterH, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(backLayer)
       pdb.gimp_drawable_fill(backLayer, 1)
       gimp.message("background made")

       # make image 1
       image1 = pdb.file_jpeg_load(file1, file1)
       pdb.gimp_image_scale(image1, 251*posterW/248, 1883*posterH/1754)
       pdb.gimp_edit_copy(image1.layers[0])
       layer1 = gimp.Layer(posterImage, "image1",posterW, posterH, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer1)
       pdb. plug_in_hsv_noise(image1, layer1, 2, 3, 0.5, value)
       floatingLayer = pdb.gimp_edit_paste(layer1, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer1.translate(0, 0)
       gimp.message("image 1 included")

       # make image 2
       image2 = pdb.file_png_load(file2, file2)
       pdb.gimp_image_scale(image2, 1792*posterW/2480, 1013*posterH/3508)
       pdb.gimp_edit_copy(image2.layers[0])
       layer2 = gimp.Layer(posterImage, "image2",1792*posterW/2480, 1013*posterH/3508, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer2)
       floatingLayer = pdb.gimp_edit_paste(layer2, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       pdb.plug_in_unsharp_mask(image2, layer2, radius, amount, 0)
       layer2.translate(-240, posterH-1013)
       gimp.message("image 2 included")

       # make image 3
       image3 = pdb.file_png_load(file3, file3)
       pdb.gimp_image_scale(image3, 1509*posterW/2480, 260*posterH/877)
       pdb.gimp_edit_copy(image3.layers[0])
       layer3 = gimp.Layer(posterImage, "image3",1509*posterW/2480, 260*posterH/877, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer3)
       floatingLayer = pdb.gimp_edit_paste(layer3, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer3.translate(980, 2490)
       gimp.message("image 3 included")

       # make image 4
       image4 = pdb.file_png_load(file4, file4)
       pdb.gimp_image_scale(image4, posterW, posterH)
       pdb.gimp_edit_copy(image4.layers[0])
       layer4 = gimp.Layer(posterImage, "image4",posterW, posterH, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer4)
       floatingLayer = pdb.gimp_edit_paste(layer4, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer4.translate(0, 0)
       gimp.message("image 4 included")

        # make image 5
       image5 = pdb.file_png_load(file5, file5)
       pdb.gimp_image_scale(image5, 1061*posterW/2480, 284*posterH/877)
       pdb.gimp_edit_copy(image5.layers[0])
       layer5 = gimp.Layer(posterImage, "image5",1061*posterW/2480, 284*posterH/877, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer5)
       floatingLayer = pdb.gimp_edit_paste(layer5, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer5.translate(posterW-1061, 0)
       gimp.message("image 5 included")

        # creat text 1 (title)
       textLayer1 = pdb.gimp_text_fontname(posterImage, None, 0, 0, str1, 100, True, 600, PIXELS, font1)
       textLayer1.translate(posterW/2-739, 995)
       pdb.script_fu_drop_shadow(posterImage, textLayer1, 20, 20, 10, (0, 0, 0), 50, False)
       gimp.message("text 1 included")

       # creat text 2 (All that jazz)
       textLayer2 = pdb.gimp_text_fontname(posterImage, None, 0, 0, str2, 100, True, 250, PIXELS, font2)
       pdb.gimp_text_layer_set_color(textLayer2, (136, 212, 246))
       textLayer2.translate(posterW/12, posterH/7)
       gimp.message("text 2 included")

        # creat text 3 (Let's try and jazz it up)
       textLayer3 = pdb.gimp_text_fontname(posterImage, None, 0, 0, str3, 100, True, 185, PIXELS, font3)
       pdb.gimp_text_layer_set_color(textLayer3, (245, 120, 157))
       textLayer3.translate(posterW/8, 5*posterH/8)
       gimp.message("text 3 included")

# end filter

register(
              "python_fu_jazz_poster",
              "Jazz Poster",
              "Make a Jazz Poster with 5 image and a copyright",
              "YC",
              "Copyright@YC",
              "2021",
              "jazz_poster",
              "", 
              [
                     (PF_FILE, "file1", "Choose Image 1", ""),
                     (PF_FILE, "file2", "Choose Image 2", ""),
                     (PF_FILE, "file3", "Choose Image 3", ""),
                     (PF_FILE, "file4", "Choose Image 4", ""),
                     (PF_FILE, "file5", "Choose Image 5", ""),
                     (PF_STRING, "str1", "Str1", "JAZZ"),
                     (PF_FONT, "font1", "Font1", "American Typewriter Bold Condensed"),
                     (PF_STRING, "str2", "Str2", "All that jazz"),
                     (PF_FONT, "font2", "Font2", "Brush Script MT Italic"),
                     (PF_STRING, "str3", "Str3", "Let's try and jazz it up"),
                     (PF_FONT, "font3", "Font3", "Apple Chancery weight=101"),
                     (PF_SLIDER, "radius", "Unsharp Mask Radius", 30, (0, 100, 0.5)),
                     (PF_SLIDER, "amount", "Unsharp Mask Amount", 8, (0, 100, 0.1)),
                     (PF_SLIDER, "value", "HSV Noise Value", 0.5, (0, 1, 0.1)),
              ],
              [],
              jazz_poster,
              menu="<Image>/File/Create/Yifan's Jazz"
)

main()

