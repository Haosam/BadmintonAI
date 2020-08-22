# import time

# track_id = ["Player1","Player2","Player3","Player4","Player5","Player6","Player7","Player8","Player9","Player10","Player11","Player12","Player13","Player14","Player15"]

# def get_track():
# 	for track in track_id:
# 		print(track)
# 		time.sleep(1)
# 	return track



# import thread
# import time
# def numbers():
# 	a = [1,2,3,4,5,6,7,8,9,10]
# 	for num in a:
# 		print(num)
# 	return num
# root = Tk()
# # print(numbers())
# def task():
# 	print("hello")
# 	label1=Label(root, text=thread.start_new_thread(numbers()))
# 	label1.grid(row=0,column=0)
# 	root.after(2000, task)  # reschedule event in 2 seconds

# root.after(2000, task)
# root.mainloop()

from player import*

a = list(player_main())
print(a)
print(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7])

def main():
	print(a[1])

main()