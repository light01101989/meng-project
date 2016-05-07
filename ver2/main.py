import argparse
import subprocess

# Run here
parser = argparse.ArgumentParser(description='Main script to run the full model. From compression to optimization. Need to call from datasets/<xyz>/ directory')
parser.add_argument('-a','--all', help='Equivalent to -cfsr.', required=False,action='store_true')
parser.add_argument('-c','--compress', help='Flag to enable compression. Breaks file into multiple to handle BigData files.', required=False,action='store_true')
parser.add_argument('-f','--filter', help='Flag to enable filtering of files. Flag -p and -u also needed.', required=False,action='store_true')
parser.add_argument('-p','--minpost', help='Minimum number of post for user to qualify(inclusive)',required=False,type=int,default=5)
parser.add_argument('-u','--minuser', help='Minimum number of qualified user in a Q/A pair(inclusive)', required=False,type=int,default=3)
parser.add_argument('-s','--structure', help='Flag to structure data in dataStructures.', required=False,action='store_true')
parser.add_argument('-r','--run', help='Run the optimization and dump solution.', required=False,action='store_true')
args = parser.parse_args()


if args.compress or args.all:
    print "---RUNNING breakFiles_compress.py---"
    subprocess.call("python ../../ver2/breakFiles_compress.py -u -p -v",shell=True)
if args.filter or args.all:
    print "\n---RUNNING filterPosts.py---"
    subprocess.call("python ../../ver2/filterPosts.py -p %d -u %d" % (args.minpost,args.minuser),shell=True)
if args.structure or args.all:
    print "\n---RUNNING structureBigData.py---"
    subprocess.call("python ../../ver2/structureBigData.py",shell=True)
if args.run or args.all:
    print "\n---RUNNING runBigData.py---"
    subprocess.call("python ../../ver2/runBigData.py -l",shell=True)
