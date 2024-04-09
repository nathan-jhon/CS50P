from custom_lib import bye
import sys
if len(sys.argv) == 2:
	print(bye(sys.argv[1]))
else:
	sys.exit()
