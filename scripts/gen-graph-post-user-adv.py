#!usr/bin/python
import subprocess

#Parsing the xml file
def get_list(cmd):
    #p = subprocess.Popen(['./get-post-owner-user-id.sh'], shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
    #byte_output = p.communicate()[0]
    
    byte_output = subprocess.check_output([cmd])
    #print(byte_output)
    out_list = byte_output.decode('ascii','ignore').split('\n')
    out_list.remove('')
    return out_list

## Get list for postid:post_type:ownerid
plist = get_list('./get-post-owner-user-id.sh')
print(plist)

## Get list for Userid:displayname
ulist = get_list('./get-user-id-name.sh')
print(ulist)
udict = {v.split(':')[0]:v.split(':')[1] for v in ulist}

## Printing the graph file G1
#print("digraph G {")
#for post in plist:
#    #print(post)
#    temp = post.split(':')
#    post_type = temp.pop(1)
#    temp[1] = udict[temp[1]]
#    #print(temp)
#    if post_type == '1':
#        #print("Ques")
#        #print('->'.join(temp))
#        print('"' + temp[0] + '"', '->','"' + temp[1] + '"')
#    else:
#        #print("Ans")
#        #print('->'.join(temp[::-1]))
#        print('"' + temp[1] + '"', '->','"' + temp[0] + '"')
#print("}")

## Printing the graph file G2
print("digraph G {")
## Printing all user nodes with attributes
for key in udict:
    print(key + " " + "[label=\"" + udict[key] + "\",shape=box,color=red]")

## Printing all post nodes with attributes
for post in plist:
    temp = post.split(':')
    post_type = temp.pop(1)
    if post_type == '1':
        print(temp[0] + " [shape=triangle,color=green]")
        print('"' + temp[1] + '"', '->','"' + temp[0] + '"' + " [label=u2q]")
    elif post_type == '2':
        #print("Ans")
        print(temp[0] + " [shape=ellipse,color=blue,score=" + temp[3] + "]")
        print('"' + temp[1] + '"', '->','"' + temp[0] + '"' + " [label=u2a,weight=" + temp[3] + "]")
        print('"' + temp[2] + '"', '->','"' + temp[0] + '"' + " [label=q2a,weight=" + temp[3] + "]")
print("}")
#for post in plist:
#    temp = post.split(':')
#    post_type = temp.pop(1)
#    temp[1] = udict[temp[1]]
#    print('"' + temp[1] + '"', '->','"' + temp[0] + '"')
#    if post_type == '2':
#        #print("Ans")
#        print('"' + temp[2] + '"', '->','"' + temp[0] + '"')
#print("}")
