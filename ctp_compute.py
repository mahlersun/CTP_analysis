#!/usr/bin/python

from mopac_mol import *
import csv

if len(sys.argv) <= 1:
    filename = raw_input("Enter the file name: ")
else:
    filename = sys.argv[1]

if '.' in filename:
    filename = filename[:filename.rfind('.')]


with open(filename+'.out', 'r') as infile:
    
    out = MopacMolecule(infile)

    out.read_atoms()
    out.read_norbs()
    out.read_orbs() 
    out.read_configs()
    out.read_states()
    with open(filename+'.csv', mode='w') as outfile:
        out_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        out_writer.writerow(['States', 'Energy','Oscillator','%CTP'])
        #outfile.write('State\tEnergy\tOscillator\t%CTP\n')
        for i in range(1, len(out.states)):
            out.gen_ctp(i)
            out_writer.writerow([str(i), str(out.states[i].energy), str(out.states[i].osc), str(out.ctp)])

 
#    for state in out.states:
#        print(state)

 
