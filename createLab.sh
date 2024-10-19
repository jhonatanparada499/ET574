devName='Jhonatan Parada';
labName='Jhonatan_LAB';
labParent='Labs';

lstLabName=$(ls $labParent | tail -n 1); # Jhonatan_LAB4
lstLabNum=${lstLabName: -1}; # 4

newLabNum=$(expr $lstLabNum + 1);
newLab=${labName}${newLabNum}; # Jhonatan_LAB5

files() {
    local labFilesNum=${1:-4} # default num of files
    
    mkdir ${labParent}/${newLab};

    for i in $(seq 1 $labFilesNum);
    do fileName='lab'${newLabNum}_${i}.py;
    txt='# '${fileName}' - '${devName};
    echo $txt > ${labParent}/${newLab}/${fileName};
    done
}

