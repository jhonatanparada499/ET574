# Commands
# [bash createLab.sh]

defaultFilesNum=4;
devName='Jhonatan Parada';
labName='Jhonatan_LAB';
labParent='labs';
fileFormat='.py';

lstLabName=$(ls $labParent | tail -n 1); # a lab within the lowest ranges

latestLabs=();

currentLab=$lstLabName;
for lab in $(ls $labParent);
do
if [ ${#currentLab} == ${#lab} ]; then
currentLab=$lab;
else
latestLabs+=($lab);
fi
done

if [ ${#latestLabs[@]} != 0 ]; then
lstLabName=${latestLabs[-1]};

numSize=$(expr ${#lstLabName} - ${#labName});
lstLabNum=${lstLabName: -$numSize} #12
echo $lstLabNum
else
lstLabNum=${lstLabName: -1}; # 4
fi

newLabNum=$(expr $lstLabNum + 1);
newLab=${labName}${newLabNum}; # Jhonatan_LAB5

newLabPath=${labParent}/${newLab};

mkdir $newLabPath;

echo 'New directory created in '$labParent' succesfully';
echo 'Name: '${newLab};
echo 'Parent: '${labParent};
echo 'Path: '${newLabPath};
echo '';

create_files(){
    local labFilesNum=${1:-$defaultFilesNum}

    for i in $(seq 1 $labFilesNum);
    do fileName='lab'${newLabNum}_${i}${fileFormat};
    txt='# '${fileName}' - '${devName};
    echo $txt > ${labParent}/${newLab}/${fileName};
    done 

    echo '';
    echo 'New files created in '${newLab}':';
    echo 'Files: '$(ls $newLabPath); 
    echo 'Total: '${labFilesNum};
    echo 'Format: '${fileFormat}
}

echo 'Do you want to create '${defaultFilesNum}' files in '${newLab}'? (y/n)';
read answer;

if [ $answer == 'y' ]; then
create_files;
else
echo 'How many files do you want to create in '${newLab}?;
read customFilesNum;
echo '';
create_files $customFilesNum;
fi

# read labFilesNum;

# for i in $(seq 1 $labFilesNum);
# do fileName='lab'${newLabNum}_${i}${fileFormat};
# txt='# '${fileName}' - '${devName};
# echo $txt > ${labParent}/${newLab}/${fileName};
# done 

# echo '';
# echo 'New files created in '${newLab}':';
# echo 'Files: '$(ls $newLabPath); 
# echo 'Total: '${labFilesNum};
# echo 'Format: '${fileFormat}