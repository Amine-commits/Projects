Day 1: RAM Usage Script

    Script:

output_file="testresult.txt"
echo "simple script showing ram usage and other infos" > $output_file
echo "------------------------------------------------" >> $output_file
whoami >> $output_file
echo "------------------------------------------------" >> $output_file
free -h >> $output_file
echo "------------------------------------------------" >> $output_file

Output:

simple script showing ram usage and other infos
------------------------------------------------
your_username
------------------------------------------------
Used: 2.3G | Free: 1.2G | Total: 8.0G


Commands for File Management

    Commands Used:

mkdir practice
cd practice
touch file1.txt file2.txt
mv file1.txt file3.txt
rm file2.txt

