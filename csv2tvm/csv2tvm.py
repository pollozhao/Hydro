# csv format WITHOUT heading: start,node,Kh,Kv,Ss,Sy
# sorted by: start,node
inputfile =  '004_total_TVM.csv'
outputfile = inputfile.replace('.csv','.tvm')
total_sp = 108

fout = open(outputfile,'w')


fout.write(' # MODFLOW-USG Time-Variant Materials (TVM) Package                              \n\
  1  0  0  0  0 -1\n\
         0         0         0         0         0  Start SP   1\n')


sp_list = []
with open(inputfile) as f:
    for l in f:
        sp_list.append(l.split(',')[0])
#print(len(sp_list))

outstack = []
write_flag = True
for c_sp in range(1,total_sp + 1):
    if str(c_sp) in sp_list:
        fin = open(inputfile)
        for line in fin:
            c_in = line.replace('\n','').split(',')
            if c_in[0] == str(c_sp):
                c_count = str(sp_list.count(c_in[0]))
                if  write_flag == True:
                    outstr = '         '+c_count+'         '+c_count+'         '+c_count+'         '+c_count+'         0  End SP   ' + str(c_in[0]) + '\n'
                    fout.write(outstr)
                    write_flag = False
                outstack.append([c_in[1],c_in[2],c_in[3],c_in[4],c_in[5]])
        for item in outstack:
            fout.write('     '+ item[0] + '  ' + item[1] +'\n')
        for item in outstack:
            fout.write('     '+ item[0] + '  ' + item[2] +'\n')
        for item in outstack:
            fout.write('     '+ item[0] + '  ' + item[3] +'\n')            
        for item in outstack:
            fout.write('     '+ item[0] + '  ' + item[4] +'\n')
            
        fin.close()
        outstack = []
    else:
        outstr = '         0         0         0         0         0  End SP   ' + str(c_sp) + '\n'
        fout.write(outstr)
        write_flag = True

fout.close()
print('done~')
