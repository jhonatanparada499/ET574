a='abc'
mkdir $a
mkdir ${a: -1}
##devName='Jhonatan Parada'
##labName='Jhonatan_LAB'
##labParent='Labs'
##labFilesNum=4

##lstLabName=$(ls $labParent | tail -n 1) # Jhonatan_LAB4
##lstLabNum=${lstLabName: -1} # 4

##newLabNum=$(expr $lstLabNum + 1)
##newLab=$labName$newLabNum # Jhonatan_LAB5

## mkdir ${labParent}/${newLab} 

## for i in $(seq 1 $labFilesNum); do fileName='lab'${newLabNum}_${i}.py && txt='# '${fileName}' - '${devName} && echo $txt > ${labParent}/${newLab}/${fileName}; done

# newLab=${labName}$(expr $labNum + 1) # Jhonatan_LAB5

## devName='Jhonatan Parada' && labName='Jhonatan_LAB' && labParent='Labs' && labFilesNum=4 && lstLabName=$(ls $labParent | tail -n 1) && lstLabNum=${lstLabName: -1} && newLabNum=$(expr $lstLabNum + 1) && newLab=$labName$newLabNum && mkdir $newLab && for i in $(seq 1 $labFilesNum); do fileName='lab'${newLabNum}_${i}.py && txt='# '${fileName}' - '${devName} && echo $txt > ${labParent}/${newLab}/${fileName}; done
