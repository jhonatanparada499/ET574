# Commands
# [source dir_maker.sh] (to Import the file)

# [create_lab] (Creates a Lab with the default number of files)
# [create_lab n] (Creates a Lab with n number of files)

# Any number of labs can be created after importing it, and using the function files
echo 'Hello wordl';
defaultFilesNum=4;

devName='Jhonatan Parada';
labName='Jhonatan_LAB';
labParent='labs';

create_lab() {
    local labFilesNum=${1:-$defaultFilesNum} # default num of files

    lstLabName=$(ls $labParent | tail -n 1); # Jhonatan_LAB4
    lstLabNum=${lstLabName: -1}; # 4

    newLabNum=$(expr $lstLabNum + 1);
    newLab=${labName}${newLabNum}; # Jhonatan_LAB5

    mkdir ${labParent}/${newLab};

    for i in $(seq 1 $labFilesNum);
    do fileName='lab'${newLabNum}_${i}.py;
    txt='# '${fileName}' - '${devName};
    echo $txt > ${labParent}/${newLab}/${fileName};
    done        
}

