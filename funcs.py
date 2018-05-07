import os
import truth_table as tt

rownum = 1

def generateTable(array,fname):
    filepath = os.path.join('c:/David/UW/Spring 2018/ECE 108',"assignment_"+fname+".txt")
    if not os.path.exists('c:/David/UW/Spring 2018/ECE 108'):
        os.makedirs('c:/David/UW/Spring 2018/ECE 108')
    outfile = open(filepath,'w')
    global w
    w = outfile.write
    
    ##Edit class call
    global expression
    expression = tt.ass1_3_2()
    
    global lengths
    lengths = [ len(word)+4 for word in array ]+[len(s)+4 for s in expression.strings]
    
    w("  "+'  |  '.join(array+[s for s in expression.strings]) + "  " + '\n')
    w(":" + ':|:'.join(['-'*(i-2) for i in lengths]) + ':' + '\n')

    print("  "+'  |  '.join(array+[s for s in expression.strings]) + "  ")
    print(":" + ':|:'.join(['-'*(i-2) for i in lengths]) + ':')    

    global errorArray
    errorArray = []
    
    binGen("",0,len(array))

    if len(errorArray):
        print ("Errors found in:\n"+'\n'.join(map(str,errorArray)))

    outfile.close()

def binGen(binary,ct,ln):
    if ct == ln:
        generateRow(binary,expression.claim(binary),rownum)
        return ""
    binGen(binary+'1',ct+1,ln)
    binGen(binary+'0',ct+1,ln)

def generateRow(binary,resolved_claim,rownum):
    binary += ''.join([str(boolToNum(boolean)) for boolean in resolved_claim])
    output =[]
    for i in range(len(binary)):
        left = lengths[i]//2
        right = lengths[i] - left - 1
        bit = binToStr(binary[i])
        if bit == 'U':
            errorArray.append(rownum)
        output.append( " "*left + bit + " "*right )
    w('|'.join(output)+'\n')
    print('|'.join(output))
    rownum += 1

def boolToNum(boolean):
    if boolean:
        return 1
    elif not boolean:
        return 0
    return 'N'

def binToStr(binString):
    if binString == '1':
        return 'T'
    elif binString == '0':
        return 'F'
    return 'U'
