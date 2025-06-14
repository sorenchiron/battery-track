import datetime
import psutil
import time
import os
from typer import Typer

today = datetime.datetime.now().strftime('%Y%m%d')


app = Typer()

@app.command()
def main(logfile:str='battery-'+today+'.csv',interval:float=60,forcenew:bool=False):
	add_header = False
	if os.path.isfile(logfile):
		if forcenew:
			os.remove(logfile)
			add_header = True
	else:
		add_header = True

	if add_header:
		with open(logfile,'a',encoding="utf-8") as f:
				f.write(f'"time","percent","secsleft"\n')
	
	while True:
		stat = psutil.sensors_battery()
		percent = stat.percent
		secsleft = stat.secsleft
		now = datetime.datetime.now().isoformat(sep=' ')
		# write file
		line = f'"{now}",{percent},{secsleft}'
		with open(logfile,'a',encoding="utf-8") as f:
			f.write(line+'\n')
		print(line)
		time.sleep(interval)

if __name__ == "__main__":
	app()
