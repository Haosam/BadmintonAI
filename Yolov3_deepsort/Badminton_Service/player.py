from tkinter import *
import cv2

# Global Variables, can be translated to database if it becomes production
lcw = "Lee Chong Wei"
swh = "Son Wan Ho"
lyd = "Lee Yong Dae"
kgj = "Kim Gi Jung"
ksh = "Ko Sung Hyun"
yys = "Yo Yeon Seong"
csg = "Choi Sol Gyu"
wcl = "Wang Chi-Lin"
chl = "Chen Hung-Lin"

lcw_height = 1.72
swh_height = 1.77
lyd_height = 1.76
kkj_height = 1.79
ksh_height = 1.79
yys_height = 1.81
csg_height = 1.81
wcl_height = 1.86
chl_height = 1.77
################################################################################
player_names1 = ["Player 1",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_names2 = ["Player 2",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_names3 = ["Player 3",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_names4 = ["Player 4",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_heights = [lcw_height,swh_height,lyd_height,kkj_height,ksh_height,yys_height,csg_height]
#################################################################################
def player_main():
	print("If no player is present, please at least select None")
	def callback1(selection):
		global name_1, height_1
		name_1 = selection
		height_1 = playercheck(selection)
		return(name_1, height_1)
	def callback2(selection):
		global name_2, height_2
		name_2 = selection
		height_2 = playercheck(selection)
		return(name_1, height_1)
	def callback3(selection):
		global name_3, height_3
		name_3 = selection
		height_3 = playercheck(selection)
		return(name_3, height_3)
	def callback4(selection):
		global name_4, height_4
		name_4 = selection
		height_4 = playercheck(selection)
		return(name_4, height_4)

	def playercheck(selection):
		if selection == "Lee Chong Wei":
			return lcw_height
		elif selection == "Son Wan Ho":
			return swh_height
		elif selection == "Lee Yong Dae":
			return swh_height
		elif selection == "Kim Gi Jung":
			return kkj_height
		elif selection == "Ko Sung Hyun":
			return ksh_height
		elif selection == "Yo Yeon Seong":
			return yys_height
		elif selection == "Choi Sol Gyu":
			return csg_height
		elif selection == "Wang Chi-Lin":
			return wcl_height
		elif selection == "Chen Hung-Lin":
			return chl_height
		elif "None" or "Select Player" or "Player 1" or "Player 2" or "Player 3" or "Player 4":
			return 1
		else:
			return 1

	def playerselection():

		window = Tk()
		window.geometry('400x400')
		window.title("Player Selection")
		label1 = Label(window, text="Player 1: ")
		label1.config(width=10, font=('Helvetica', 10))
		label2 = Label(window, text="Player 2: ")
		label2.config(width=10, font=('Helvetica', 10))
		label3 = Label(window, text="Player 3: ")
		label3.config(width=10, font=('Helvetica', 10))
		label4 = Label(window, text="Player 4: ")
		label4.config(width=10, font=('Helvetica', 10))
		label5 = Label(window, text="If no player is present,")
		label6 = Label(window, text=", please at least select None")

		label1.grid(row=0,column=0)
		label2.grid(row=1,column=0)
		label3.grid(row=2,column=0)
		label4.grid(row=3,column=0)
		label5.grid(row=8,column=0)
		label6.grid(row=8,column=1)

		clicked1 = StringVar()
		clicked1.set("Select Player")
		clicked2 = StringVar()
		clicked2.set("Select Player")
		clicked3 = StringVar()
		clicked3.set("Select Player")
		clicked4 = StringVar()
		clicked4.set("Select Player")

		drop1 = OptionMenu(window, clicked1, *player_names1, command=callback1)
		drop1.config(width=20, font=('Helvetica', 10))
		drop2 = OptionMenu(window, clicked2, *player_names2, command=callback2)
		drop2.config(width=20, font=('Helvetica', 10))
		drop3 = OptionMenu(window, clicked3, *player_names3, command=callback3)
		drop3.config(width=20, font=('Helvetica', 10))
		drop4 = OptionMenu(window, clicked4, *player_names4, command=callback4)
		drop4.config(width=20, font=('Helvetica', 10))

		drop1.grid(row=0,column=1)
		drop2.grid(row=1,column=1)
		drop3.grid(row=2,column=1)
		drop4.grid(row=3,column=1)

		labelTest1 = Label(text="", font=('Helvetica', 8), fg='red')
		labelTest1.grid(row=4,column=1)
		labelTest2 = Label(text="", font=('Helvetica', 8), fg='red')
		labelTest2.grid(row=5,column=1)
		labelTest3 = Label(text="", font=('Helvetica', 8 ), fg='red')
		labelTest3.grid(row=6,column=1)
		labelTest4 = Label(text="", font=('Helvetica', 8), fg='red')
		labelTest4.grid(row=7,column=1)

		window.mainloop()

	playerselection()
	return(name_1,height_1,name_2,height_2,name_3,height_3,name_4,height_4)
	# print(name_1,height_1,",", name_2,height_2,",",name_3,height_3,",",name_4,height_4)

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   player_main()
   print(name_1)
   print(name_2)
   print(name_3)
   print(name_4)