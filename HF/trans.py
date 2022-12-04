import os
import re

# Files Preparation
folder = ''
files_to_read = [('1.txt','1'), ('2.txt','2'), ('3.txt','3'), ('4.txt','4'), ('5.txt','5'), ('6.txt','6'),
 ('7.txt','7'), ('8.txt','8'), ('9.txt','9'), ('10.txt','10'), ('11.txt','11'), ('12.txt','12')]

# Regularition
for (file, _) in files_to_read:
    filepath = os.path.join(folder, file)
    file = open(filepath)
    filecontent = file.read()
    coeffRegex = re.compile(r'\d.*\d\d|-\d.*\d\d')
    gateRegex = re.compile(r'\[.*\d\]')

    coefficient = coeffRegex.findall(filecontent)
    gate = gateRegex.findall(filecontent)

    save_coeffient = open('coefficient'+filepath, mode = 'w')
    save_coeffient.write('\n'.join(coefficient))
    save_coeffient.close()

    save_gate = open('gate'+filepath, mode = 'w')
    save_gate.write('\n'.join(gate))
    save_gate.close()

    file.close()