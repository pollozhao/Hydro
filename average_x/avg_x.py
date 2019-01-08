fin = 'calb.rch'
avg_x = 7
line_break = 25002

fout = open(fin+'_agv','w')
###############################################################################
import numpy as np
import time

start_t = time.time()
mtx1,mtxn = [],[]
group_size = line_break - 2

fout.write('         1        50\n         1         1\n')
#np.format_float_scientific(y, precision=3, exp_digits=1)

def export_mtxn(m):
    for j in m:
        for k in j:
            fout.write('   %s' % '{:.3E}'.format(k))
        fout.write('\n')

def get_avg(m):
    mout = np.zeros((group_size, 10))
    for z in range(avg_x):
        for x in range(group_size):
            for y in range(10):
                mout[x][y] = mout[x][y] + m[x+group_size*z][y]
    z = z + 1
    return mout/avg_x

with open(fin) as infile:
    for line in infile:
        row = line.split()
        if len(row) == 10:
            mtxn.append([float(x) for x in row])

end_t = time.time()           
print ('Completed reading input file in: ' + str(round(end_t-start_t, 2)) + 's')
mtxn = np.array(mtxn)
print ('len of main metrix:', len(mtxn))

group = len(mtxn) / group_size
print('No. of avg groups:',group)

for g in range(int(group / avg_x)):
    start = 0 + g*(group_size) * avg_x
    end = start + (group_size) * avg_x
    mtx1 = mtxn[start:end:1]
    #print(len(mtx1))
    mtx1_out = get_avg(mtx1)
    #print(len(mtx1_out))
    fout.write('        18         1(10G12.0)                   -1\n')
    export_mtxn(mtx1_out.tolist())
    fout.write('         1         0\n')

fout.close()

end_t = time.time()
print('Completed computing in: ' + str(round(end_t-start_t, 2)) + 's')