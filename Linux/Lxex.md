
    Viewing Files Tasks Create a file testfile.txt with the following content:

Apple Banana Orange Apple Grape Cherry

Use cat to:

View the content of the file. Append a new line to testfile.txt with >>. Use less and more to:

View the file content page by page. Navigate forward and backward in the file. Use head and tail to:

View the first 3 lines of testfile.txt. View the last 2 lines of testfile.txt.


    Searching Tasks

Search for the word "Apple" in testfile.txt using grep.

Display the line numbers of matching lines.

Use grep -v to display lines that do not contain "Apple."

Find files in your home directory containing the word "config" using find.

Use locate to find the location of a known file (e.g., bashrc).

If locate isn’t installed, try installing mlocate and running updatedb.

    Editing

Tasks Open testfile.txt in nano: Add a new fruit to the list. Save and exit.

Open testfile.txt in vim: Replace the word "Apple" with "Pineapple." Delete the second line.

Use sed to: Replace "Banana" with "Mango" in testfile.txt and print the result. Delete all lines containing "Orange" without modifying the original file.

Use awk to: Print only the first column of testfile.txt. Count the number of occurrences of each fruit.

    Comparing Files

Tasks Create a new file testfile2.txt:

Apple Mango Orange Pear Grape

Use diff to: Compare testfile.txt and testfile2.txt to find differences. Use the -y option to display the differences side by side.

Use cmp to: Compare testfile.txt and testfile2.txt. Check if the two files are identical.

    Sorting and Uniqueness

Tasks Use sort to: Sort the contents of testfile.txt in alphabetical order. Sort the file in reverse order.

Use uniq to: Remove duplicate lines from testfile.txt. Combine sort and uniq to ensure duplicates are removed.

    Counting Tasks Use wc to: Count the number of lines, words, and characters in testfile.txt. Display only the number of lines using the -l option.

Combine grep and wc: Count the number of lines containing "Apple" in testfile.txt.

Extended Challenge Create a file logfile.txt with the following content:

2025-01-20 INFO: System started 2025-01-20 ERROR: Disk space low 2025-01-20 WARNING: High memory usage 2025-01-20 INFO: Process completed 2025-01-21 INFO: Backup completed 2025-01-21 ERROR: Network failure 2025-01-21 WARNING: CPU overheating

Tasks : Use grep to extract lines containing "ERROR" and save them to error_logs.txt.

Use awk to print only the date and message (excluding severity level) from logfile.txt.

Use sort to: Sort the log entries by severity level (INFO, WARNING, ERROR). Sort the entries by date.

Use uniq to: Find and count the unique log levels in the file.

Use wc to: Count the total number of log entries in logfile.txt.
