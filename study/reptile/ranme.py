import os,sys

'''
修改文件名
'''

if __name__ == '__main__':
	path1 = 'D:\myProject\Python\study\\reptile\\'  # 文件夹所在路径
	for day in range(20180501,20180532):
		#dir_name=path1+str(day)+'\\'
		#file_name=dir_name+'T_DS_BASE_H_'+'.csv'
		#rname = 'T_DS_BASE_H_'+str(day)[2:]+'.csv'
		#os.mkdir(dir_name)
		#file = open(file_name,'w')
		#file.close()
		#print(file_name)
		new_name = 'T_DS_BASE_H_'+str(day)[2:]+'00'+'.csv'
		new_name1 = 'T_DS_BASE_D_'+str(day)[2:]+'.csv'

		path2=path1+str(day)+'\\'
		for file in os.listdir(path2):
			if os.path.isfile(os.path.join(path2,file)) == True and file == 'part-0000':
				print(os.path.join(path2,file))
				os.rename(os.path.join(path2,file),os.path.join(path2,new_name1))

