from tkinter import *
from PIL import ImageTk , Image
from huffman_tree import *

def login_page():
    first_page = Tk()
    first_page.geometry("800x800")
    first_page.title('Huffman Coding for Image Compression')
    # creating label
    Label(text="Image Compressor", bg="red", width="30",
          height="3", font=("Calibri", 13)).pack()
    Label(text="").pack()
    # creating proceed button
    Button(text="Proceed to Image", height="3",
           width="30", command=image_page).pack()
    Label(text="").pack()
    # creating button to exit program
    Button(text="Quit", height="3", width="30",
           command=first_page.destroy).pack()
    first_page.mainloop()

def image_page():
    global page2
    page2 = Tk()
    page2.geometry("700x700")
    page2.title("Image Viewer")
    image_1 = ImageTk.PhotoImage(Image.open(
        r'E:\Projects\dsa_group_project\dsa-group-project\red.png'))
    image_2 = ImageTk.PhotoImage(Image.open(
        r'E:\Projects\dsa_group_project\dsa-group-project\red.png'))
    global imgs_lst
    imgs_lst = [image_1, image_2]
    global label
    label = Label(image=image_1)
    label.grid(row=1, column=0, columnspan=3)

    global back_button
    global exit_button
    global fwd_button

    back_button = Button(page2, text="Back", command=back, state=DISABLED)
    exit_button = Button(page2, text="Exit", command=page2.quit)
    fwd_button = Button(page2, text="Forward", command=lambda: forward(1))
    back_button.grid(row=5, column=0)
    exit_button.grid(row=5, column=1)
    fwd_button.grid(row=5, column=2)
    page2.mainloop()


def forward(img_no):
    global label
    global fwd_button
    global back_button
    global exit_button

    label.grid_forget()
    label = Label(image=imgs_lst[img_no-1])
    label.grid(row=1, column=0, columnspan=3)
    fwd_button = Button(page2, text="forward",
                        command=lambda: forward(img_no+1))
    if img_no == 2:
        fwd_button = Button(page2, text="forward", state=DISABLED)

    back_button = Button(page2, text="Back", command=lambda: back(img_no-1))
    back_button.grid(row=5, column=0)
    exit_button.grid(row=5, column=1)
    fwd_button.grid(row=5, column=2)


def back(img_no):
    global label
    global fwd_button
    global back_button
    global exit_button

    label.grid_forget()
    label = Label(image=imgs_lst[img_no-1])
    label.grid(row=1, column=0, columnspan=3)
    fwd_button = Button(page2, text="forward",
                        command=lambda: forward(img_no+1))
    back_button = Button(page2, text="Back", command=lambda: back(img_no-1))
    if img_no == 1:

        back_button = Button(page2, text="Back", state=DISABLED)
    label.grid(row=1, column=0, columnspan=3)
    back_button.grid(row=5, column=0)
    exit_button.grid(row=5, column=1)
    fwd_button.grid(row=5, column=2)


login_page()
