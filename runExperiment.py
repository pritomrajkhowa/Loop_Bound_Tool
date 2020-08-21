import subprocess
import sys
import os
import time
currentdirectory = os.path.dirname(os.path.realpath(__file__))





"""
Reading the contain of the file 
"""
def readingFile( filename ):
    content=None
    with open(currentdirectory+"/"+filename) as f:
        content = f.readlines()
    return content
 
"""
Wrtitting the contain on file 
"""
def writtingFile( filename , content ):
	file = open(currentdirectory+"/"+filename, "w")
	file.write(str(content))
	file.close()

"""
Appending the contain on file 
"""
def appendingFile( filename , content ):
	file = open(currentdirectory+"/"+filename, "a")
	file.write(str(content))
	file.close()



benchmark_file='benchmark/benchmark_file_info/benchmark_file_info1.txt'

benchmark_file_KoAT='other_tool_data/KoAT/KoAT_Info.txt'

KoAT_List_info = readingFile( benchmark_file_KoAT )

print('Number of Files for KoAT')
print(len(KoAT_List_info))

benchmark_file_Rank='other_tool_data/Rank/Rank_Info.txt'

Rank_List_info = readingFile( benchmark_file_Rank )

print('Number of Files for Rank')
print(len(Rank_List_info))

benchmark_file_LOOPUS='other_tool_data/LOOPUS/LOOPUS_Info.txt'

LOOPUS_List_info = readingFile( benchmark_file_LOOPUS )

print('Number of Files for LOOPUS')
print(len(LOOPUS_List_info))

benchmark_file_SPEED='other_tool_data/SPEED/SPEED_Info.txt'

SPEED_List_info = readingFile( benchmark_file_SPEED )

print('Number of Files for SPEED')
print(len(SPEED_List_info))

benchmark_file_C4B='other_tool_data/C4B/C4B_Info.txt'

c4b_List_info = readingFile( benchmark_file_C4B )

print('Number of Files for C4B')
print(len(c4b_List_info))

 
all_files = readingFile(benchmark_file)

file_count = 0

Table_Details = []

for each_file in all_files:

   
    each_file = each_file.replace('\n','').strip()

    each_file_details=[]

    each_file_details.append(each_file)

    print(each_file)
    #print('python3 '+' source/viap_tool_bound.py '+each_file)
 
    start_time = time.time()

    result = subprocess.run(['python3', 'source/viap_tool_bound.py', each_file], stdout=subprocess.PIPE)
 
    end_time = (time.time() - start_time)    

    each_lines=result.stdout.decode("utf-8").split('\n')

    file_count=file_count+1

    ourput_string=''

    for each_line in each_lines:
        ourput_string+=each_line+'\n'


    if 'Final Complexity'  in  ourput_string:

        each_file_details.append("Success")

    else:

        each_file_details.append("Failed")

    each_file_details.append(str(end_time))

    writtingFile( 'Outputs/'+str(file_count)+'.txt' , ourput_string )

    KoAT_Info = KoAT_List_info[file_count-1].split(':')

    each_file_details.append(KoAT_Info[1])

    #print(KoAT_List_info[file_count-1])

    Rank_Info = Rank_List_info[file_count-1].split(':')

    each_file_details.append(Rank_Info[1])


    #print(Rank_List_info[file_count-1])

    LOOPUS_Info = LOOPUS_List_info[file_count-1].split(':')

    each_file_details.append(LOOPUS_Info[1])

    #print(LOOPUS_List_info[file_count-1])

    SPEED_Info = SPEED_List_info[file_count-1].split(':')

    each_file_details.append(SPEED_Info[1])

    #print(SPEED_List_info[file_count-1])

    c4b_Info = c4b_List_info[file_count-1].split(':')

    each_file_details.append(c4b_Info[1])

    #print(c4b_List_info[file_count-1])

    Table_Details.append(each_file_details)

    html = """<html><table border="1">
<tr><th>File Name</th><th>Our Tool</th><th>Time Taken by Our Tool(sec)</th><th>KoAT</th><th>Rank</th><th>LOOPUS</th><th>SPEED</th><th>C4B</th></tr>"""
    for Table_Detail in Table_Details:
        html += "<tr>"
        for xx in Table_Detail:
            html += "<td>"+xx+"</td>"
        html += "</tr>"
    html += "</table></html>"

    file_ = open('result.html', 'w')
    file_.write(html)
    file_.close()
