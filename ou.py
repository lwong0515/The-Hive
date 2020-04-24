from tkinter import Label, Tk, Canvas, Frame, BOTH
from tkinter import*

# Class to create the hexagon framework
class hexagon(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Ordinary User")
        self.pack(fill=BOTH, expand=TRUE)


        canvas = Canvas(self)

        user_select_1 = [500,200,413,150,
                        413,150,326,200,
                        326,200,326,300,
                        326,300,413,350,
                        413,350,500,300,
                        500,300,500,200]
        user_select_2 = [675,200,588,150,
                        588,150,501,200,
                        501,200,501,300,
                        501,300,588,350,
                        588,350,675,300,
                        675,300,675,200]
        user_select_3 = [587,351,500,301,
                        500,301,413,351,
                        413,351,413,451,
                        413,451,500,501,
                        500,501,587,451,
                        587,451,587,351]
        user_display_name = [565,263,500,225,
                            500,225,435,263,
                            435,263,435,338,
                            435,338,500,375,
                            500,375,565,338,
                            565,338,565,263]
        canvas.create_polygon(user_select_1, outline='black', fill='#2C92D6', width=2)
        canvas.create_polygon(user_select_2, outline='black', fill='#37CAEF', width=2)
        canvas.create_polygon(user_select_3, outline='black', fill='#3EDAD8', width=2)
        canvas.create_polygon(user_display_name, outline='black', fill='#ffffff', width=2)

        # hexagon for projects
        p1 = [95,391,75,380,
              75,380,55,391,
              55,391,55,409,
              55,409,75,420,
              75,420,95,409,
              95,409,95,391]
        p2 = [95,491,75,480,
              75,480,55,491,
              55,491,55,509,
              55,509,75,520,
              75,520,95,509,
              95,509,95,491]
        p3 = [95,591,75,580,
              75,580,55,591,
              55,591,55,609,
              55,609,75,620,
              75,620,95,609,
              95,609,95,591]
        canvas.create_polygon(p1,fill='#2C92D6', width=1)
        canvas.create_polygon(p2,fill='#37CAEF', width=1)
        canvas.create_polygon(p3,fill='#3EDAD8', width=1)

        # hexagon for user select
        s1 = [520,167,500,156,
              500,156,480,167,
              480,167,480,185,
              480,185,500,196,
              500,196,520,185,
              520,185,520,167]
        s2 = [412,354,392,343,
              392,343,372,354,
              372,354,372,372,
              372,372,392,383,
              392,383,412,372,
              412,372,412,354]
        s3 = [629,354,609,343,
              609,343,589,354,
              589,354,589,372,
              589,372,609,383,
              609,383,629,372,
              629,372,629,354]
        canvas.create_polygon(s1, fill='white', width=1)
        canvas.create_polygon(s2, fill='white', width=1)
        canvas.create_polygon(s3, fill='white', width=1)

        canvas.create_text(150, 400, text = "Project 1", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(150, 500, text = "Project 2", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(150, 600, text = "Project 3", font = ("Pursia",15),
            fill = "white")
        # hexagon for groups
        g1 = [795,391,775,380,
              775,380,755,391,
              755,391,755,409,
              755,409,775,420,
              775,420,795,409,
              795,409,795,391]
        g2 = [795,491,775,480,
              775,480,755,491,
              755,491,755,509,
              755,509,775,520,
              775,520,795,509,
              795,509,795,491]
        g3 = [795,591,775,580,
              775,580,755,591,
              755,591,755,609,
              755,609,775,620,
              775,620,795,609,
              795,609,795,591]
        canvas.create_polygon(g1, fill='white', width=1)
        canvas.create_polygon(g2, fill='white', width=1)
        canvas.create_polygon(g3, fill='white', width=1)
        canvas.create_text(850, 400, text = "Group 1", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 500, text = "Group 2", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 600, text = "Group 3", font = ("Pursia",15),
            fill = "white")


        canvas.pack(fill=BOTH, expand=1)
        canvas.configure(bg='#36393F')
        # place holder for username
        canvas.create_text(500, 300, text = "USERNAME", fill = "black")
        # greeting for user
        canvas.create_text(120, 50, text = "Hello . . .", font = ("Pursia",25),
            fill = "#7289DB")
        # My Projects
        canvas.create_text(120, 340, text = "MY PROJECTS", font = ("Pursia",15),
            fill = "#7289DB")
        canvas.create_text(815, 340, text = "MY GROUPS", font = ("Pursia",15),
            fill = "#7289DB")
        # Button for social
        # photo = PhotoImage(file = "user.png")
        # Button(canvas, text = 'Click Me !', image = photo).pack()


def main():
    root = Tk()
    # label = Label(
    #     text="The HIVE",
    #     fg="white",
    #     bg="black",
    #     width=200,
    #     height=3
    # )
    # label.pack()

    frame = hexagon()
    # Buttons
    photo1 = PhotoImage(file = r"images\chat.png")
    button1 = Button(root, image = photo1, bg="#2C92D6", bd=0).place(x=365, y=220)
    photo2 = PhotoImage(file = r"images\doc.png")
    button2 = Button(root, image = photo2, bg="#37CAEF", bd=0).place(x=567, y=230)
    photo3 = PhotoImage(file = r"images\social.png")
    button3 = Button(root, image = photo3, bg="#3EDAD8", bd=0).place(x=465, y=390)
    photo4 = PhotoImage(file = r"images\add.png")
    button4 = Button(root, image = photo4, bg="white", bd=0).place(x=487, y=164)
    photo5 = PhotoImage(file = r"images\x.png")
    button5 = Button(root, image = photo5, bg="white", bd=0).place(x=379, y=350)
    photo6 = PhotoImage(file = r"images\settings.png")
    button6 = Button(root, image = photo6, bg="white", bd=0).place(x=596, y=351)

    root.geometry("1000x800")
    root.mainloop()


if __name__ == '__main__':
    main()
