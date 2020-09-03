# AI_coloring


Style Transfer technique is used to add colors to coloring page

14 styles to choose from 

`style_image.py` is the main code. 

`invert_colors.py` makes more styles by inverting colors

`make_transparent.py` makes more styles by making the images transparent

## To run:

`pythgon3 style_image.py` 

`python3 invert_colors.py` 

`python3 make_transparent.py`

## fast-neural-style

This is the code for the paper

Perceptual Losses for Real-Time Style Transfer and Super-Resolution
<https://cs.stanford.edu/people/jcjohns/eccv16/>
Justin Johnson, Alexandre Alahi, Li Fei-Fei
Presented at ECCV 2016

The paper builds on A Neural Algorithm of Artistic Style by Leon A. Gatys, Alexander S. Ecker, and Matthias Bethge by training feedforward neural networks that apply artistic styles to images. After training, our feedforward networks can stylize images hundreds of times faster than the optimization-based method presented by Gatys et al.

### Input Images:

<img src ="inputs/ballerina.jpg" width="30%" height="30%">
<img src ="inputs/elephant.jpg" width="30%" height="30%">
<img src ="inputs/owl.png" width="30%" height="30%">


### Sample OutPut Images

<img src ="outputs/2_ballerina.png" alt="" width="30%" height="30%">
<img src ="outputs/2_transparent_elephant.png" alt="" width="30%" height="30%">
<img src ="outputs/4_jpg_owl_inverted.png" alt="" width="30%" height="30%">
<img src ="outputs/7_jpg_owl.png" alt="" width="30%" height="30%">
<img src ="outputs/9_ballerina.png" alt="" width="30%" height="30%">
<img src ="outputs/10_ballerina.png" alt="" width="30%" height="30%">
<img src ="outputs/10_elephant_inverted.png" alt="" width="30%" height="30%">
<img src ="outputs/10_transparent_elephant" alt="" width="30%" height="30%">
